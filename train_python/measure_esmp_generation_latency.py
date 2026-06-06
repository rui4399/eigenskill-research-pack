#!/usr/bin/env python3
from __future__ import annotations

"""Measure generation after swapping selected Linear modules with ESMP modules.

This is a minimal end-to-end wiring check for the real ESMP binary package. It
does not claim a high-performance packed LLM runtime. Two modes are supported:

- on-demand: keep compact ESMP payloads and dequantize each swapped weight during
  forward; this is faithful to the package boundary but slow.
- cached: dequantize once into a dense buffer; this checks numerical wiring and
  generation compatibility but loses the packed-memory advantage for those rows.
"""

import argparse
import gc
import json
import time
from pathlib import Path
from threading import Thread
from typing import Any

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
except ModuleNotFoundError:  # pragma: no cover
    torch = None
    nn = None
    F = None
    AutoModelForCausalLM = None
    AutoTokenizer = None
    TextIteratorStreamer = None

from esmp_format import dequantize_esmp_weight, read_esmp
from eval_esmp_module_reconstruction import (
    DEFAULT_MODEL,
    DEFAULT_PACKAGE_SUMMARY,
    load_package_modules,
    module_layer,
    path_exists_cross,
    resolve_path,
    repo_root,
)
from triton_config_selector import (
    TritonKernelConfig,
    choose_kernel_config,
    estimate_periodic_high_every,
    load_kernel_configs,
)

try:
    import triton

    from triton_mixed_gemm import _int4_grouped_matmul_kernel, _int8_grouped_matmul_kernel
except ModuleNotFoundError:  # pragma: no cover
    triton = None
    _int4_grouped_matmul_kernel = None
    _int8_grouped_matmul_kernel = None


DEFAULT_PROMPT = "Explain mixed-precision quantization in one concise paragraph."
_MODULE_BASE = nn.Module if nn is not None else object


def sync_if_cuda(device: str) -> None:
    if torch is not None and device.startswith("cuda") and torch.cuda.is_available():
        torch.cuda.synchronize()


def peak_memory_mib(device: str) -> float:
    if torch is None or not device.startswith("cuda") or not torch.cuda.is_available():
        return 0.0
    return float(torch.cuda.max_memory_allocated() / (1024 * 1024))


def parse_layers(text: str) -> set[int] | None:
    if not text:
        return None
    values = set()
    for part in text.replace(";", ",").split(","):
        part = part.strip()
        if part:
            values.add(int(part))
    return values


def select_modules(
    package_modules: list[dict[str, Any]],
    model_modules: dict[str, torch.nn.Module],
    exact_modules: list[str],
    filters: list[str],
    layers: set[int] | None,
    include_lm_head: bool,
    max_modules: int,
) -> list[dict[str, Any]]:
    selected = []
    wanted = set(exact_modules)
    for item in package_modules:
        name = str(item["module"])
        if wanted and name not in wanted:
            continue
        if filters and not any(text in name for text in filters):
            continue
        layer = module_layer(name)
        if layers is not None and layer not in layers:
            continue
        if name == "lm_head" and not include_lm_head:
            continue
        if name not in model_modules:
            continue
        if not Path(path_exists_cross(str(item["out"]))).exists():
            continue
        selected.append(
            {
                "module": name,
                "bits": int(item.get("bits", 0)),
                "rows": int(item.get("rows", 0)),
                "cols": int(item.get("cols", 0)),
                "out": str(path_exists_cross(str(item["out"]))),
                "packer": item.get("packer", {}),
            }
        )
        if max_modules and len(selected) >= max_modules:
            break
    return selected


class EsmpLinear(_MODULE_BASE):
    def __init__(
        self,
        source: nn.Linear,
        esmp_path: str,
        runtime: str,
        target_device: torch.device,
        target_dtype: torch.dtype,
        block_m: int,
        block_n: int,
        block_k: int,
        kernel_configs: list[TritonKernelConfig] | None = None,
        prefer_selector_fp16_win: bool = False,
    ) -> None:
        if torch is None or nn is None:
            raise RuntimeError("EsmpLinear requires torch")
        super().__init__()
        self.esmp_path = esmp_path
        self.runtime = runtime
        self.block_m = int(block_m)
        self.block_n = int(block_n)
        self.block_k = int(block_k)
        self.kernel_configs = kernel_configs or []
        self.prefer_selector_fp16_win = bool(prefer_selector_fp16_win)
        self.runtime_config_counts: dict[str, int] = {}
        self.runtime_config_examples: dict[str, dict[str, Any]] = {}
        self.esmp = read_esmp(Path(esmp_path))
        self.in_features = int(self.esmp.cols)
        self.out_features = int(self.esmp.rows)
        self.high_every = estimate_periodic_high_every(self.esmp.row_bits)
        if source.bias is not None:
            self.register_buffer("bias", source.bias.detach().to(device=target_device, dtype=target_dtype).clone())
        else:
            self.bias = None
        if self.runtime == "cached":
            weight = dequantize_esmp_weight(self.esmp).to(device=target_device, dtype=target_dtype)
            self.register_buffer("weight_dequant", weight)
        else:
            self.weight_dequant = None
        if self.runtime == "triton_grouped":
            if triton is None or _int4_grouped_matmul_kernel is None or _int8_grouped_matmul_kernel is None:
                raise RuntimeError("triton_grouped runtime requires triton")
            if target_device.type != "cuda":
                raise RuntimeError("triton_grouped runtime requires a CUDA device")
            self._init_triton_buffers(target_device)

    def _runtime_blocks(self, batch: int) -> tuple[int, int, int]:
        config = choose_kernel_config(
            self.kernel_configs,
            rows=self.out_features,
            cols=self.in_features,
            batch=batch,
            high_every=self.high_every,
            prefer_fp16_win=self.prefer_selector_fp16_win,
        )
        if config is None:
            event = {
                "selection": "static_cli",
                "requested_batch": batch,
                "rows": self.out_features,
                "cols": self.in_features,
                "high_every": self.high_every,
                "block_m": self.block_m,
                "block_n": self.block_n,
                "block_k": self.block_k,
            }
            self._record_runtime_config(event)
            return self.block_m, self.block_n, self.block_k
        event = {"selection": "selector", "requested_batch": batch, **config.as_runtime_dict()}
        self._record_runtime_config(event)
        return config.block_m, config.block_n, config.block_k

    def _record_runtime_config(self, event: dict[str, Any]) -> None:
        key = (
            f"{event.get('selection')}|shape={event.get('rows')}x{event.get('cols')}"
            f"|requested_batch={event.get('requested_batch')}|source_batch={event.get('batch')}"
            f"|block={event.get('block_m')}x{event.get('block_n')}x{event.get('block_k')}"
        )
        self.runtime_config_counts[key] = self.runtime_config_counts.get(key, 0) + 1
        self.runtime_config_examples.setdefault(key, event)

    def runtime_config_summary(self) -> list[dict[str, Any]]:
        summary = []
        for key, count in sorted(self.runtime_config_counts.items()):
            item = dict(self.runtime_config_examples[key])
            item["count"] = count
            summary.append(item)
        return summary

    def _init_triton_buffers(self, target_device: torch.device) -> None:
        import numpy as np

        row_bits = self.esmp.row_bits
        low_rows_np = np.nonzero(row_bits == 4)[0].astype(np.int64)
        high_rows_np = np.nonzero(row_bits == 8)[0].astype(np.int64)
        q4_stride = (self.esmp.cols + 1) // 2
        q4_np = np.empty((len(low_rows_np), q4_stride), dtype=np.uint8)
        q8_np = np.empty((len(high_rows_np), self.esmp.cols), dtype=np.int8)
        payload_u8 = np.frombuffer(self.esmp.payload, dtype=np.uint8)
        for slot, row in enumerate(low_rows_np):
            bit_offset = int(self.esmp.row_bit_offsets[int(row)])
            if bit_offset % 8 != 0:
                raise RuntimeError("triton_grouped currently requires byte-aligned INT4 rows")
            byte_offset = bit_offset // 8
            q4_np[slot, :] = payload_u8[byte_offset : byte_offset + q4_stride]
        for slot, row in enumerate(high_rows_np):
            bit_offset = int(self.esmp.row_bit_offsets[int(row)])
            if bit_offset % 8 != 0:
                raise RuntimeError("triton_grouped currently requires byte-aligned INT8 rows")
            byte_offset = bit_offset // 8
            q8_np[slot, :] = payload_u8[byte_offset : byte_offset + self.esmp.cols].view(np.int8)
        self.register_buffer("triton_q4", torch.from_numpy(q4_np).to(device=target_device))
        self.register_buffer("triton_q8", torch.from_numpy(q8_np).to(device=target_device))
        self.register_buffer("triton_low_rows", torch.from_numpy(low_rows_np).to(device=target_device))
        self.register_buffer("triton_high_rows", torch.from_numpy(high_rows_np).to(device=target_device))
        self.register_buffer(
            "triton_scales",
            torch.from_numpy(self.esmp.row_scales.astype(np.float32, copy=False)).to(device=target_device),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if self.runtime == "triton_grouped":
            return self._forward_triton_grouped(x)
        if self.weight_dequant is None:
            weight = dequantize_esmp_weight(self.esmp).to(device=x.device, dtype=x.dtype)
            try:
                return F.linear(x, weight, self.bias)
            finally:
                del weight
        return F.linear(x, self.weight_dequant.to(dtype=x.dtype), self.bias)

    def _forward_triton_grouped(self, x: torch.Tensor) -> torch.Tensor:
        if not x.is_cuda:
            raise RuntimeError("triton_grouped runtime requires CUDA input")
        original_shape = tuple(x.shape[:-1])
        flat = x.reshape(-1, self.in_features).contiguous()
        batch = int(flat.shape[0])
        block_m, block_n, block_k = self._runtime_blocks(batch)
        y = torch.empty((batch, self.out_features), device=x.device, dtype=torch.float32)
        if int(self.triton_low_rows.numel()) > 0:
            grid4 = (triton.cdiv(int(self.triton_low_rows.numel()), block_m), triton.cdiv(batch, block_n))
            _int4_grouped_matmul_kernel[grid4](
                flat,
                self.triton_q4,
                self.triton_low_rows,
                self.triton_scales,
                y,
                int(self.triton_low_rows.numel()),
                self.out_features,
                self.in_features,
                batch,
                int(self.triton_q4.shape[1]) if self.triton_q4.ndim == 2 else 0,
                block_m,
                block_n,
                block_k,
                num_warps=4,
            )
        if int(self.triton_high_rows.numel()) > 0:
            grid8 = (triton.cdiv(int(self.triton_high_rows.numel()), block_m), triton.cdiv(batch, block_n))
            _int8_grouped_matmul_kernel[grid8](
                flat,
                self.triton_q8,
                self.triton_high_rows,
                self.triton_scales,
                y,
                int(self.triton_high_rows.numel()),
                self.out_features,
                self.in_features,
                batch,
                block_m,
                block_n,
                block_k,
                num_warps=4,
            )
        if self.bias is not None:
            y = y + self.bias.float()
        return y.reshape(*original_shape, self.out_features).to(dtype=x.dtype)


def replace_module(model: torch.nn.Module, module_name: str, replacement: torch.nn.Module) -> None:
    parent_name, child_name = module_name.rsplit(".", 1)
    parent = model.get_submodule(parent_name)
    setattr(parent, child_name, replacement)


def render_chatml_user_prompt(prompt: str) -> str:
    return f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"


def build_generation_inputs(tokenizer, prompt: str, device: str, use_chat_template: bool = False):
    if use_chat_template:
        if not hasattr(tokenizer, "apply_chat_template"):
            raise ValueError("tokenizer does not support apply_chat_template")
        messages = [{"role": "user", "content": prompt}]
        try:
            encoded = tokenizer.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt",
            )
        except ImportError:
            return tokenizer(render_chatml_user_prompt(prompt), return_tensors="pt").to(device)
        if torch is not None and isinstance(encoded, torch.Tensor):
            return {"input_ids": encoded.to(device)}
        if hasattr(encoded, "to"):
            return encoded.to(device)
        return {key: value.to(device) if hasattr(value, "to") else value for key, value in dict(encoded).items()}
    return tokenizer(prompt, return_tensors="pt").to(device)


def _input_ids_numel(inputs) -> int:
    input_ids = inputs["input_ids"] if isinstance(inputs, dict) else inputs.input_ids
    return int(input_ids.numel()) if hasattr(input_ids, "numel") else len(input_ids[0])


def run_generation(model, tokenizer, prompt: str, max_new_tokens: int, use_chat_template: bool = False) -> dict[str, Any]:
    inputs = build_generation_inputs(tokenizer, prompt, str(model.device), use_chat_template=use_chat_template)
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    kwargs = {
        **inputs,
        "max_new_tokens": max_new_tokens,
        "do_sample": False,
        "streamer": streamer,
        "pad_token_id": tokenizer.eos_token_id,
    }
    error_box: dict[str, BaseException] = {}

    def target() -> None:
        try:
            model.generate(**kwargs)
        except BaseException as exc:  # propagate after streamer is unblocked
            error_box["error"] = exc
            if hasattr(streamer, "on_finalized_text"):
                streamer.on_finalized_text("", stream_end=True)

    sync_if_cuda(str(model.device))
    start = time.perf_counter()
    thread = Thread(target=target)
    thread.start()
    first_text_time = None
    chunks: list[str] = []
    for chunk in streamer:
        now = time.perf_counter()
        if first_text_time is None and chunk:
            first_text_time = now
        chunks.append(chunk)
    thread.join()
    if error_box:
        raise RuntimeError(f"generation failed: {error_box['error']!r}") from error_box["error"]
    sync_if_cuda(str(model.device))
    end = time.perf_counter()
    generated_text = "".join(chunks)
    generated_ids = tokenizer(generated_text, return_tensors="pt", add_special_tokens=False).input_ids
    generated_tokens = int(generated_ids.numel())
    elapsed = end - start
    return {
        "prompt_tokens": _input_ids_numel(inputs),
        "generated_tokens_text_retokenized": generated_tokens,
        "ttft_seconds": None if first_text_time is None else first_text_time - start,
        "elapsed_seconds": elapsed,
        "tokens_per_second": generated_tokens / elapsed if elapsed > 0 else None,
        "generated_text": generated_text,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure generation with selected ESMP-swapped Linear modules.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--package-summary", default=DEFAULT_PACKAGE_SUMMARY)
    parser.add_argument("--prompt", default=DEFAULT_PROMPT)
    parser.add_argument("--prompt-file", default="")
    parser.add_argument("--max-new-tokens", type=int, default=32)
    parser.add_argument("--warmup-runs", type=int, default=0)
    parser.add_argument("--chat-template", action="store_true", help="Format the prompt as a single user chat message.")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--module", action="append", default=[])
    parser.add_argument("--module-filter", action="append", default=[])
    parser.add_argument("--layers", default="")
    parser.add_argument("--include-lm-head", action="store_true")
    parser.add_argument("--max-modules", type=int, default=3)
    parser.add_argument("--runtime", choices=["python_on_demand", "cached", "triton_grouped"], default="python_on_demand")
    parser.add_argument("--cache-dequant", action="store_true", help="Deprecated alias for --runtime cached.")
    parser.add_argument("--block-m", type=int, default=32)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=128)
    parser.add_argument("--kernel-config-selector", default="", help="Optional JSON output from select_triton_kernel_configs.py.")
    parser.add_argument("--prefer-selector-fp16-win", action="store_true", help="Prefer FP16-winning selector rows after batch/shape matching.")
    parser.add_argument("--no-esmp", action="store_true", help="Use the same loader path but do not replace modules.")
    parser.add_argument("--out", default="outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_generation_latency.json")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("missing dependencies: install torch and transformers")
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8").strip()
    else:
        prompt = args.prompt
    if not prompt:
        raise SystemExit("empty prompt")
    runtime = "cached" if args.cache_dequant else args.runtime
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    if args.device.startswith("cuda") and torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()

    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
    kernel_config_selector = resolve_path(args.kernel_config_selector, root) if args.kernel_config_selector else None
    kernel_configs = load_kernel_configs(kernel_config_selector) if kernel_config_selector else []
    if kernel_config_selector and not kernel_configs:
        raise SystemExit(f"No usable kernel configs in selector: {kernel_config_selector}")
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=args.local_files_only, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )
    model.eval()
    model.to(args.device)

    selected_raw_bytes = 0
    selected_package_bytes = 0
    replaced = []
    replacement_modules = []
    if not args.no_esmp:
        model_modules = {name: module for name, module in model.named_modules() if isinstance(module, torch.nn.Linear)}
        selected = select_modules(
            load_package_modules(package_summary),
            model_modules=model_modules,
            exact_modules=args.module,
            filters=args.module_filter,
            layers=parse_layers(args.layers),
            include_lm_head=args.include_lm_head,
            max_modules=args.max_modules,
        )
        if not selected:
            raise SystemExit("No modules selected for ESMP swap.")

        for item in selected:
            name = item["module"]
            source = model_modules[name]
            esmp = read_esmp(Path(item["out"]))
            selected_raw_bytes += esmp.raw_fp32_bytes
            selected_package_bytes += esmp.package_bytes
            replacement = EsmpLinear(
                source=source,
                esmp_path=item["out"],
                runtime=runtime,
                target_device=torch.device(args.device),
                target_dtype=dtype,
                block_m=args.block_m,
                block_n=args.block_n,
                block_k=args.block_k,
                kernel_configs=kernel_configs if runtime == "triton_grouped" else None,
                prefer_selector_fp16_win=args.prefer_selector_fp16_win,
            )
            replace_module(model, name, replacement)
            replacement_modules.append(replacement)
            replaced.append(
                {
                    "module": name,
                    "bits": item.get("bits"),
                    "rows": esmp.rows,
                    "cols": esmp.cols,
                    "package_bytes": esmp.package_bytes,
                    "raw_fp32_bytes": esmp.raw_fp32_bytes,
                    "compression_vs_fp32": esmp.compression_vs_fp32,
                }
            )
        del model_modules, selected

    gc.collect()
    if args.device.startswith("cuda") and torch.cuda.is_available():
        torch.cuda.empty_cache()

    warmup_metrics = []
    for _ in range(args.warmup_runs):
        warmup_metrics.append(run_generation(model, tokenizer, prompt, args.max_new_tokens, use_chat_template=args.chat_template))
    if args.device.startswith("cuda") and torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()
    metrics = run_generation(model, tokenizer, prompt, args.max_new_tokens, use_chat_template=args.chat_template)
    for record, replacement in zip(replaced, replacement_modules):
        if hasattr(replacement, "runtime_config_summary"):
            record["runtime_config_summary"] = replacement.runtime_config_summary()
    result = {
        "model": args.model,
        "device": str(model.device),
        "dtype": args.dtype,
        "package_summary": str(package_summary),
        "kernel_config_selector": str(kernel_config_selector) if kernel_config_selector else None,
        "kernel_config_count": len(kernel_configs),
        "mode": "hf_same_loader" if args.no_esmp else runtime,
        "block_m": args.block_m if runtime == "triton_grouped" else None,
        "block_n": args.block_n if runtime == "triton_grouped" else None,
        "block_k": args.block_k if runtime == "triton_grouped" else None,
        "chat_template": bool(args.chat_template),
        "max_new_tokens": args.max_new_tokens,
        "warmup_runs": args.warmup_runs,
        "warmup_metrics": warmup_metrics,
        "replaced_module_count": len(replaced),
        "replaced_modules": replaced,
        "selected_raw_fp32_bytes": selected_raw_bytes,
        "selected_package_bytes": selected_package_bytes,
        "selected_compression_vs_fp32": selected_raw_bytes / max(float(selected_package_bytes), 1.0),
        "peak_gpu_memory_mib": peak_memory_mib(args.device),
        **metrics,
    }
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    out = resolve_path(args.out, root)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")

    del model
    if args.device.startswith("cuda") and torch.cuda.is_available():
        torch.cuda.empty_cache()
    gc.collect()


if __name__ == "__main__":
    main()
