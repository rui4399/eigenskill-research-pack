#!/usr/bin/env python3
from __future__ import annotations

"""Measure generation with a real fused ESMP QKV replacement.

This is stronger than the sidecar smoke: selected layers have their q_proj,
k_proj, and v_proj modules replaced by wrappers that share one fused packed ESMP
QKV runtime. The first projection call for a hidden-state tensor computes the
concatenated Q/K/V output once; the following projection wrappers return cached
slices.

It is still a controlled smoke, not a production runtime. The goal is to verify
that a packed fused QKV replacement can sit inside HF generation and report
TTFT/tokens/s/memory/text effects under the same GPU guard used elsewhere.
"""

import argparse
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import torch
    import torch.nn as nn
    from transformers import AutoModelForCausalLM, AutoTokenizer
except ModuleNotFoundError:  # pragma: no cover
    torch = None
    nn = None
    AutoModelForCausalLM = None
    AutoTokenizer = None

try:
    import triton
    from triton_mixed_gemm import _int4_grouped_matmul_kernel, _int8_grouped_matmul_kernel
except ModuleNotFoundError:  # pragma: no cover
    triton = None
    _int4_grouped_matmul_kernel = None
    _int8_grouped_matmul_kernel = None

from benchmark_esmp_fused_selected_rows import build_exact_modules_for_layer, parse_suffixes
from eval_esmp_module_reconstruction import DEFAULT_MODEL, DEFAULT_PACKAGE_SUMMARY, load_package_modules, resolve_path, repo_root
from measure_esmp_generation_latency import (
    DEFAULT_PROMPT,
    EsmpLinear,
    parse_layers,
    replace_module,
    run_generation,
    select_modules,
)


@dataclass
class FusedQKVStats:
    wrapper_calls: int = 0
    dense_role_calls: int = 0
    fused_compute_calls: int = 0
    cache_hits: int = 0
    cache_misses: int = 0
    cuda_event_ms: list[float] = field(default_factory=list)
    pending_events: list[tuple[Any, Any]] = field(default_factory=list)
    input_shapes: set[str] = field(default_factory=set)

    def clear(self) -> None:
        self.wrapper_calls = 0
        self.dense_role_calls = 0
        self.fused_compute_calls = 0
        self.cache_hits = 0
        self.cache_misses = 0
        self.cuda_event_ms.clear()
        self.pending_events.clear()
        self.input_shapes.clear()

    def finalize_pending(self) -> None:
        for start, end in self.pending_events:
            end.synchronize()
            self.cuda_event_ms.append(float(start.elapsed_time(end)))
        self.pending_events.clear()


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    pos = (len(ordered) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(ordered) - 1)
    frac = pos - lo
    return float(ordered[lo] * (1.0 - frac) + ordered[hi] * frac)


def summarize_ms(values: list[float]) -> dict[str, float]:
    if not values:
        return {"sum": 0.0, "mean": 0.0, "median": 0.0, "p90": 0.0, "max": 0.0}
    ordered = sorted(values)
    mid = len(ordered) // 2
    median = ordered[mid] if len(ordered) % 2 else 0.5 * (ordered[mid - 1] + ordered[mid])
    return {
        "sum": float(sum(values)),
        "mean": float(sum(values) / len(values)),
        "median": float(median),
        "p90": percentile(values, 0.9),
        "max": float(max(values)),
    }


def cat_or_empty_1d(chunks: list[torch.Tensor], device: torch.device, dtype: torch.dtype) -> torch.Tensor:
    if chunks:
        return torch.cat(chunks, dim=0).contiguous()
    return torch.empty((0,), device=device, dtype=dtype)


def cat_or_empty_2d(chunks: list[torch.Tensor], rows: int, cols: int, device: torch.device, dtype: torch.dtype) -> torch.Tensor:
    if chunks:
        return torch.cat(chunks, dim=0).contiguous()
    return torch.empty((rows, cols), device=device, dtype=dtype)


class FusedESMPQKVRuntime(nn.Module):
    def __init__(
        self,
        modules: list[str],
        sources: list[nn.Linear],
        runtimes: list[EsmpLinear],
        block_m: int,
        block_n: int,
        block_k: int,
        sync_mode: str,
    ) -> None:
        super().__init__()
        if not runtimes:
            raise ValueError("at least one runtime is required")
        self.modules = modules
        self.in_features = int(runtimes[0].in_features)
        self.out_splits = [int(runtime.out_features) for runtime in runtimes]
        self.total_out_features = int(sum(self.out_splits))
        self.block_m = int(block_m)
        self.block_n = int(block_n)
        self.block_k = int(block_k)
        self.sync_mode = sync_mode
        self.stats = FusedQKVStats()
        self.raw_fp32_bytes = int(sum(runtime.esmp.raw_fp32_bytes for runtime in runtimes))
        self.package_bytes = int(sum(runtime.esmp.package_bytes for runtime in runtimes))
        self.compression_vs_fp32 = float(self.raw_fp32_bytes / max(self.package_bytes, 1))

        device = runtimes[0].triton_scales.device
        q4_stride = int(runtimes[0].triton_q4.shape[1]) if runtimes[0].triton_q4.ndim == 2 else (self.in_features + 1) // 2
        q4_chunks: list[torch.Tensor] = []
        q8_chunks: list[torch.Tensor] = []
        low_row_indices: list[torch.Tensor] = []
        high_row_indices: list[torch.Tensor] = []
        scale_chunks: list[torch.Tensor] = []
        bias_chunks: list[torch.Tensor] = []
        offset = 0
        for source, runtime in zip(sources, runtimes, strict=True):
            if int(runtime.in_features) != self.in_features:
                raise ValueError("fused QKV requires matching input feature dimensions")
            if int(runtime.triton_low_rows.numel()):
                q4_chunks.append(runtime.triton_q4.contiguous())
                low_row_indices.append(runtime.triton_low_rows.long() + offset)
            if int(runtime.triton_high_rows.numel()):
                q8_chunks.append(runtime.triton_q8.contiguous())
                high_row_indices.append(runtime.triton_high_rows.long() + offset)
            scale_chunks.append(runtime.triton_scales.float().contiguous())
            if source.bias is not None:
                bias_chunks.append(source.bias.detach().to(device=device, dtype=torch.float32).contiguous())
            else:
                bias_chunks.append(torch.zeros(int(runtime.out_features), device=device, dtype=torch.float32))
            offset += int(runtime.out_features)

        self.register_buffer("q4", cat_or_empty_2d(q4_chunks, 0, q4_stride, device, torch.uint8))
        self.register_buffer("q8", cat_or_empty_2d(q8_chunks, 0, self.in_features, device, torch.int8))
        self.register_buffer("low_row_indices", cat_or_empty_1d(low_row_indices, device, torch.long))
        self.register_buffer("high_row_indices", cat_or_empty_1d(high_row_indices, device, torch.long))
        self.register_buffer("scales", torch.cat(scale_chunks, dim=0).contiguous())
        self.register_buffer("bias", torch.cat(bias_chunks, dim=0).contiguous())
        self.q4_stride = q4_stride
        self._cache_key: tuple[Any, ...] | None = None
        self._cache_chunks: tuple[torch.Tensor, ...] | None = None

    def _make_key(self, x: torch.Tensor) -> tuple[Any, ...]:
        return (int(x.data_ptr()), tuple(int(v) for v in x.shape), str(x.dtype), str(x.device))

    def _compute_fused(self, x: torch.Tensor) -> torch.Tensor:
        if triton is None or _int4_grouped_matmul_kernel is None or _int8_grouped_matmul_kernel is None:
            raise RuntimeError("fused QKV replacement requires Triton grouped kernels")
        flat = x.reshape(-1, self.in_features).contiguous()
        batch = int(flat.shape[0])
        y = torch.empty((batch, self.total_out_features), device=x.device, dtype=torch.float32)
        start = torch.cuda.Event(enable_timing=True)
        end = torch.cuda.Event(enable_timing=True)
        start.record()
        low_count = int(self.low_row_indices.numel())
        if low_count:
            grid4 = (triton.cdiv(low_count, self.block_m), triton.cdiv(batch, self.block_n))
            _int4_grouped_matmul_kernel[grid4](
                flat,
                self.q4,
                self.low_row_indices,
                self.scales,
                y,
                low_count,
                self.total_out_features,
                self.in_features,
                batch,
                int(self.q4_stride),
                self.block_m,
                self.block_n,
                self.block_k,
                num_warps=4,
            )
        high_count = int(self.high_row_indices.numel())
        if high_count:
            grid8 = (triton.cdiv(high_count, self.block_m), triton.cdiv(batch, self.block_n))
            _int8_grouped_matmul_kernel[grid8](
                flat,
                self.q8,
                self.high_row_indices,
                self.scales,
                y,
                high_count,
                self.total_out_features,
                self.in_features,
                batch,
                self.block_m,
                self.block_n,
                self.block_k,
                num_warps=4,
            )
        y = y + self.bias[None, :]
        end.record()
        if self.sync_mode == "per_call":
            end.synchronize()
            self.stats.cuda_event_ms.append(float(start.elapsed_time(end)))
        else:
            self.stats.pending_events.append((start, end))
        self.stats.fused_compute_calls += 1
        self.stats.input_shapes.add("x".join(str(v) for v in x.shape))
        return y.reshape(*x.shape[:-1], self.total_out_features).to(dtype=x.dtype)

    def forward_chunk(self, x: torch.Tensor, role_idx: int) -> torch.Tensor:
        self.stats.wrapper_calls += 1
        key = self._make_key(x)
        if self._cache_key == key and self._cache_chunks is not None:
            self.stats.cache_hits += 1
        else:
            self.stats.cache_misses += 1
            fused = self._compute_fused(x)
            self._cache_chunks = tuple(torch.split(fused, self.out_splits, dim=-1))
            self._cache_key = key
        assert self._cache_chunks is not None
        out = self._cache_chunks[role_idx]
        if role_idx == len(self.out_splits) - 1:
            self._cache_key = None
            self._cache_chunks = None
        return out

    def finalize_pending(self) -> None:
        self.stats.finalize_pending()

    def clear_stats(self) -> None:
        self.stats.clear()


class FusedQKVProjection(nn.Module):
    def __init__(self, runtime: FusedESMPQKVRuntime, role_idx: int, dense_source: nn.Linear | None = None) -> None:
        super().__init__()
        self.runtime = runtime
        self.role_idx = int(role_idx)
        self.in_features = int(runtime.in_features)
        self.out_features = int(runtime.out_splits[role_idx])
        self.dense_source = dense_source
        self.bias = None

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if self.dense_source is not None:
            self.runtime.stats.dense_role_calls += 1
            return self.dense_source(x)
        return self.runtime.forward_chunk(x, self.role_idx)


def install_fused_qkv(
    model: torch.nn.Module,
    package_modules: list[dict[str, Any]],
    layers: list[int],
    suffixes: list[str],
    dense_roles: set[str] | None,
    device: torch.device,
    dtype: torch.dtype,
    block_m: int,
    block_n: int,
    block_k: int,
    sync_mode: str,
) -> list[FusedESMPQKVRuntime]:
    model_modules = {name: module for name, module in model.named_modules() if isinstance(module, torch.nn.Linear)}
    installed: list[FusedESMPQKVRuntime] = []
    dense_roles = set(dense_roles or set())
    for layer in layers:
        exact_modules = build_exact_modules_for_layer(layer, suffixes)
        selected_items = select_modules(
            package_modules,
            model_modules=model_modules,
            exact_modules=exact_modules,
            filters=[],
            layers=None,
            include_lm_head=False,
            max_modules=0,
        )
        selected_by_name = {str(item["module"]): item for item in selected_items}
        missing = [name for name in exact_modules if name not in selected_by_name]
        if missing:
            raise RuntimeError(f"missing ESMP package modules for layer {layer}: {missing}")
        items = [selected_by_name[name] for name in exact_modules]
        sources = [model_modules[str(item["module"])] for item in items]
        runtimes = [
            EsmpLinear(source, item["out"], "triton_grouped", device, dtype, block_m, block_n, block_k)
            for source, item in zip(sources, items, strict=True)
        ]
        fused_runtime = FusedESMPQKVRuntime(
            modules=exact_modules,
            sources=sources,
            runtimes=runtimes,
            block_m=block_m,
            block_n=block_n,
            block_k=block_k,
            sync_mode=sync_mode,
        )
        for role_idx, module_name in enumerate(exact_modules):
            suffix = suffixes[role_idx]
            dense_source = sources[role_idx] if suffix in dense_roles or module_name in dense_roles else None
            replace_module(model, module_name, FusedQKVProjection(fused_runtime, role_idx, dense_source))
        installed.append(fused_runtime)
    return installed


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure HF generation with fused ESMP QKV replacement.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--package-summary", default=DEFAULT_PACKAGE_SUMMARY)
    parser.add_argument("--prompt", default=DEFAULT_PROMPT)
    parser.add_argument("--prompt-file", default="")
    parser.add_argument("--max-new-tokens", type=int, default=16)
    parser.add_argument("--warmup-runs", type=int, default=1)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--layers", default="0")
    parser.add_argument("--suffixes", default="q_proj,k_proj,v_proj")
    parser.add_argument("--dense-roles", default="", help="Comma-separated suffixes or exact module names to keep as dense guards.")
    parser.add_argument("--block-m", type=int, default=32)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=64)
    parser.add_argument("--sync-mode", choices=["per_call", "end"], default="end")
    parser.add_argument("--no-fused", action="store_true")
    parser.add_argument("--out", default="outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation.json")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("missing dependencies: install torch and transformers")
    if args.device.startswith("cuda") and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8").strip()
    else:
        prompt = args.prompt
    if not prompt:
        raise SystemExit("empty prompt")

    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    device = torch.device(args.device)
    layers = sorted(parse_layers(args.layers) or set())
    suffixes = parse_suffixes(args.suffixes)
    dense_roles = set(parse_suffixes(args.dense_roles)) if args.dense_roles else set()

    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=args.local_files_only, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )
    model.eval()
    model.to(device)

    fused_runtimes: list[FusedESMPQKVRuntime] = []
    if not args.no_fused:
        fused_runtimes = install_fused_qkv(
            model=model,
            package_modules=load_package_modules(package_summary),
            layers=layers,
            suffixes=suffixes,
            dense_roles=dense_roles,
            device=device,
            dtype=dtype,
            block_m=args.block_m,
            block_n=args.block_n,
            block_k=args.block_k,
            sync_mode=args.sync_mode,
        )

    warmup_metrics = []
    for _ in range(args.warmup_runs):
        warmup_metrics.append(run_generation(model, tokenizer, prompt, args.max_new_tokens))
    for runtime in fused_runtimes:
        runtime.clear_stats()
    if args.device.startswith("cuda"):
        torch.cuda.reset_peak_memory_stats()
    metrics = run_generation(model, tokenizer, prompt, args.max_new_tokens)
    for runtime in fused_runtimes:
        runtime.finalize_pending()

    all_ms = [value for runtime in fused_runtimes for value in runtime.stats.cuda_event_ms]
    replacements = [
        {
            "modules": runtime.modules,
            "raw_fp32_bytes": runtime.raw_fp32_bytes,
            "package_bytes": runtime.package_bytes,
            "compression_vs_fp32": runtime.compression_vs_fp32,
            "wrapper_calls": runtime.stats.wrapper_calls,
            "dense_role_calls": runtime.stats.dense_role_calls,
            "fused_compute_calls": runtime.stats.fused_compute_calls,
            "cache_hits": runtime.stats.cache_hits,
            "cache_misses": runtime.stats.cache_misses,
            "input_shapes": sorted(runtime.stats.input_shapes),
            "cuda_event_ms": summarize_ms(runtime.stats.cuda_event_ms),
        }
        for runtime in fused_runtimes
    ]
    result = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "model": args.model,
        "device": str(model.device),
        "dtype": args.dtype,
        "package_summary": str(package_summary),
        "mode": "hf_same_loader" if args.no_fused else "hf_generation_with_fused_esmp_qkv_replacement",
        "layers": [] if args.no_fused else layers,
        "suffixes": [] if args.no_fused else suffixes,
        "dense_roles": [] if args.no_fused else sorted(dense_roles),
        "block_m": None if args.no_fused else int(args.block_m),
        "block_n": None if args.no_fused else int(args.block_n),
        "block_k": None if args.no_fused else int(args.block_k),
        "sync_mode": None if args.no_fused else args.sync_mode,
        "max_new_tokens": int(args.max_new_tokens),
        "warmup_runs": int(args.warmup_runs),
        "warmup_metrics": warmup_metrics,
        "replacement_count": len(fused_runtimes),
        "replacements": replacements,
        "replacement_raw_fp32_bytes": int(sum(runtime.raw_fp32_bytes for runtime in fused_runtimes)),
        "replacement_package_bytes": int(sum(runtime.package_bytes for runtime in fused_runtimes)),
        "replacement_compression_vs_fp32": float(
            sum(runtime.raw_fp32_bytes for runtime in fused_runtimes)
            / max(sum(runtime.package_bytes for runtime in fused_runtimes), 1)
        ),
        "replacement_dense_role_calls": int(sum(runtime.stats.dense_role_calls for runtime in fused_runtimes)),
        "replacement_cuda_event_ms": summarize_ms(all_ms),
        "peak_gpu_memory_mib": float(torch.cuda.max_memory_allocated() / (1024 * 1024)) if args.device.startswith("cuda") else 0.0,
        **metrics,
        "interpretation_guardrail": (
            "This replaces selected QKV projections with an approximate packed ESMP fused runtime. "
            "It is a controlled smoke, not a production-quality fused transformer runtime."
        ),
    }
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    out = resolve_path(args.out, root)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")

    del model
    if args.device.startswith("cuda"):
        torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
