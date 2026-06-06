#!/usr/bin/env python3
from __future__ import annotations

"""Measure generation while running a fused selected-row ESMP sidecar.

This is a deliberately conservative systems probe. It does not replace QKV in
the transformer path. Instead, it attaches a pre-hook to each selected layer's
q_proj module, takes the real hidden-state tensor used by HF generation, and
executes the fused selected-row packed ESMP kernel for q/k/v rows that share
that same input. The output is discarded after synchronization.

The resulting numbers answer a narrow but useful question: can the fused ESMP
selected-row runtime execute inside the real decode loop under the same loader,
with measured TTFT/tokens/s/memory and sidecar kernel latency?
"""

import argparse
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
except ModuleNotFoundError:  # pragma: no cover
    torch = None
    AutoModelForCausalLM = None
    AutoTokenizer = None

from benchmark_esmp_fused_selected_rows import (
    build_exact_modules_for_layer,
    build_fused_selected_groups,
    parse_suffixes,
    triton_fused_selected_forward,
)
from benchmark_esmp_selected_rows import parse_ints, select_even_rows
from eval_esmp_module_reconstruction import DEFAULT_MODEL, DEFAULT_PACKAGE_SUMMARY, load_package_modules, resolve_path, repo_root
from measure_esmp_generation_latency import DEFAULT_PROMPT, EsmpLinear, parse_layers, run_generation, select_modules


@dataclass
class SidecarStats:
    calls: int = 0
    cuda_event_ms: list[float] = field(default_factory=list)
    pending_events: list[tuple[Any, Any, tuple[int, ...]]] = field(default_factory=list)
    input_shapes: set[str] = field(default_factory=set)
    errors: list[str] = field(default_factory=list)

    def add_elapsed(self, elapsed_ms: float, shape: tuple[int, ...]) -> None:
        self.calls += 1
        self.cuda_event_ms.append(float(elapsed_ms))
        self.input_shapes.add("x".join(str(v) for v in shape))

    def add_pending(self, start: Any, end: Any, shape: tuple[int, ...]) -> None:
        self.calls += 1
        self.pending_events.append((start, end, shape))
        self.input_shapes.add("x".join(str(v) for v in shape))

    def finalize_pending(self) -> None:
        for start, end, _shape in self.pending_events:
            end.synchronize()
            self.cuda_event_ms.append(float(start.elapsed_time(end)))
        self.pending_events.clear()

    def clear(self) -> None:
        self.calls = 0
        self.cuda_event_ms.clear()
        self.pending_events.clear()
        self.input_shapes.clear()
        self.errors.clear()


@dataclass
class SidecarHandle:
    layer: int
    modules: list[str]
    selected_rows_per_module: int
    selected_rows_total: int
    low_rows_total: int
    high_rows_total: int
    handle: Any
    stats: SidecarStats

    def remove(self) -> None:
        self.handle.remove()


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


def install_sidecars(
    model: torch.nn.Module,
    package_modules: list[dict[str, Any]],
    package_summary: Path,
    layers: list[int],
    suffixes: list[str],
    selected_rows_per_module: int,
    device: torch.device,
    dtype: torch.dtype,
    block_m: int,
    block_n: int,
    block_k: int,
    sidecar_sync_mode: str,
) -> list[SidecarHandle]:
    model_modules = {name: module for name, module in model.named_modules() if isinstance(module, torch.nn.Linear)}
    handles: list[SidecarHandle] = []
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
        if len({int(source.in_features) for source in sources}) != 1:
            raise RuntimeError(f"layer {layer} QKV modules do not share input feature dimensions")
        runtimes = [
            EsmpLinear(source, item["out"], "triton_grouped", device, dtype, block_m, block_n, block_k)
            for source, item in zip(sources, items, strict=True)
        ]
        selected_by_module = [
            select_even_rows(int(source.out_features), selected_rows_per_module, device)
            for source in sources
        ]
        fused_groups = build_fused_selected_groups(runtimes, selected_by_module)
        stats = SidecarStats()

        def hook(_module, inputs, *, groups=fused_groups, stats=stats) -> None:
            if not inputs:
                return
            x = inputs[0]
            if not torch.is_tensor(x):
                return
            try:
                shape = tuple(int(v) for v in x.shape)
                start = torch.cuda.Event(enable_timing=True)
                end = torch.cuda.Event(enable_timing=True)
                start.record()
                with torch.inference_mode():
                    _ = triton_fused_selected_forward(x, groups, block_m, block_n, block_k)
                end.record()
                if sidecar_sync_mode == "per_call":
                    end.synchronize()
                    stats.add_elapsed(float(start.elapsed_time(end)), shape)
                else:
                    stats.add_pending(start, end, shape)
            except BaseException as exc:  # keep the generation failure diagnosable
                stats.errors.append(repr(exc))
                raise

        q_proj_name = exact_modules[0]
        handle = model_modules[q_proj_name].register_forward_pre_hook(hook)
        handles.append(
            SidecarHandle(
                layer=layer,
                modules=exact_modules,
                selected_rows_per_module=int(selected_rows_per_module),
                selected_rows_total=int(fused_groups["total_selected"]),
                low_rows_total=int(fused_groups["low_rows"]),
                high_rows_total=int(fused_groups["high_rows"]),
                handle=handle,
                stats=stats,
            )
        )
    # Keep these local tensors alive for as long as hooks are active.
    for handle in handles:
        setattr(handle, "_package_summary", package_summary)
    return handles


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure HF generation with fused selected-row ESMP sidecars.")
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
    parser.add_argument("--selected-rows", type=int, default=64)
    parser.add_argument("--block-m", type=int, default=32)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=64)
    parser.add_argument(
        "--sidecar-sync-mode",
        choices=["per_call", "end"],
        default="per_call",
        help="Use per-call CUDA synchronization for precise local timing or defer event sync until generation ends.",
    )
    parser.add_argument("--out", default="outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation.json")
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

    if args.device.startswith("cuda"):
        torch.cuda.reset_peak_memory_stats()
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=args.local_files_only, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )
    model.eval()
    model.to(device)

    handles = install_sidecars(
        model=model,
        package_modules=load_package_modules(package_summary),
        package_summary=package_summary,
        layers=layers,
        suffixes=suffixes,
        selected_rows_per_module=args.selected_rows,
        device=device,
        dtype=dtype,
        block_m=args.block_m,
        block_n=args.block_n,
        block_k=args.block_k,
        sidecar_sync_mode=args.sidecar_sync_mode,
    )

    warmup_metrics = []
    for _ in range(args.warmup_runs):
        warmup_metrics.append(run_generation(model, tokenizer, prompt, args.max_new_tokens))
    for handle in handles:
        handle.stats.clear()
    if args.device.startswith("cuda"):
        torch.cuda.reset_peak_memory_stats()
    metrics = run_generation(model, tokenizer, prompt, args.max_new_tokens)
    for handle in handles:
        handle.stats.finalize_pending()

    all_sidecar_ms = [value for handle in handles for value in handle.stats.cuda_event_ms]
    sidecars = [
        {
            "layer": handle.layer,
            "modules": handle.modules,
            "selected_rows_per_module": handle.selected_rows_per_module,
            "selected_rows_total": handle.selected_rows_total,
            "low_rows_total": handle.low_rows_total,
            "high_rows_total": handle.high_rows_total,
            "calls": handle.stats.calls,
            "input_shapes": sorted(handle.stats.input_shapes),
            "cuda_event_ms": summarize_ms(handle.stats.cuda_event_ms),
            "errors": handle.stats.errors,
        }
        for handle in handles
    ]
    for handle in handles:
        handle.remove()

    result = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "model": args.model,
        "device": str(model.device),
        "dtype": args.dtype,
        "package_summary": str(package_summary),
        "mode": "hf_generation_with_fused_selected_row_esmp_sidecar",
        "layers": layers,
        "suffixes": suffixes,
        "selected_rows_per_module": int(args.selected_rows),
        "block_m": int(args.block_m),
        "block_n": int(args.block_n),
        "block_k": int(args.block_k),
        "sidecar_sync_mode": args.sidecar_sync_mode,
        "max_new_tokens": int(args.max_new_tokens),
        "warmup_runs": int(args.warmup_runs),
        "warmup_metrics": warmup_metrics,
        "sidecars": sidecars,
        "sidecar_call_count": int(sum(handle.stats.calls for handle in handles)),
        "sidecar_cuda_event_ms": summarize_ms(all_sidecar_ms),
        "peak_gpu_memory_mib": float(torch.cuda.max_memory_allocated() / (1024 * 1024)) if args.device.startswith("cuda") else 0.0,
        **metrics,
        "interpretation_guardrail": (
            "Sidecar kernels execute on real generation activations but do not replace the "
            "transformer's dense QKV computation; this measures integration overhead, not "
            "end-to-end LLM acceleration."
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
