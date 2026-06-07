#!/usr/bin/env python3
from __future__ import annotations

"""Evaluate W4A8-style activation drift on real module inputs.

This links the RTX 5070 W4A8 kernel gate back to model-conditioned data.  It
uses sampled inputs to selected Linear modules, reconstructs the ESMP weight,
then compares:

    FP activation + FP weight   -> base output
    FP activation + ESMP weight -> W4A16-style output
    A8 activation + ESMP weight -> W4A8-style output

The result is a local module reconstruction gate, not an end-to-end LLM speed or
quality benchmark.
"""

import argparse
import gc
import json
import math
import statistics
import time
from pathlib import Path
from typing import Any

try:
    import torch
    import torch.nn.functional as F
    from transformers import AutoModelForCausalLM, AutoTokenizer
except ModuleNotFoundError:  # pragma: no cover
    torch = None
    F = None
    AutoModelForCausalLM = None
    AutoTokenizer = None

from esmp_format import dequantize_esmp_weight, read_esmp
from eval_esmp_module_reconstruction import (
    DEFAULT_MODEL,
    DEFAULT_PACKAGE_SUMMARY,
    load_package_modules,
    parse_layers,
    resolve_path,
    repo_root,
    select_package_modules,
)
from measure_module_output_sensitivity import DEFAULT_PROMPTS, collect_module_inputs, load_prompts


DEFAULT_OUT_DIR = "outputs/w4a8_activation_reconstruction_2026_06_08"


def safe_median(values: list[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    xs = sorted(values)
    pos = (len(xs) - 1) * q
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return float(xs[lo])
    frac = pos - lo
    return float(xs[lo] * (1.0 - frac) + xs[hi] * frac)


def rel_l2(diff: torch.Tensor, signal: torch.Tensor) -> float:
    num = float(diff.float().pow(2).sum().detach().cpu().item())
    den = float(signal.float().pow(2).sum().detach().cpu().item())
    return math.sqrt(num / max(den, 1.0e-24))


def quantize_activation_i8(x: torch.Tensor, qmax: int = 127) -> tuple[torch.Tensor, dict[str, float]]:
    flat = x.float()
    scale = flat.abs().amax(dim=1, keepdim=True).clamp_min(1.0e-8) / float(qmax)
    q = torch.round(flat / scale).clamp(-qmax, qmax)
    deq = q * scale
    saturation = float((q.abs() >= qmax).float().mean().detach().cpu().item())
    return deq.to(dtype=torch.float32), {
        "activation_input_rel_l2": rel_l2(deq - flat, flat),
        "activation_saturation_fraction": saturation,
    }


def score_modules(
    modules: list[dict[str, Any]],
    sampled_inputs: dict[str, list[torch.Tensor]],
    device: str,
    chunk_rows: int,
    progress_every: int,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    started = time.time()
    with torch.inference_mode():
        for idx, item in enumerate(modules, start=1):
            name = str(item["module"])
            rows = sampled_inputs.get(name, [])
            if not rows:
                records.append({"module": name, "error": "no_sampled_inputs", "sample_rows": 0})
                continue

            module = item["_module_ref"]
            esmp = read_esmp(Path(item["out"]))
            if tuple(module.weight.shape) != (esmp.rows, esmp.cols):
                records.append({"module": name, "error": "shape_mismatch", "sample_rows": 0})
                continue

            x_cpu = torch.cat(rows, dim=0)
            weight = module.weight.detach().to(device=device, dtype=torch.float32)
            qweight = dequantize_esmp_weight(esmp).to(device=device, dtype=torch.float32)

            sums = {
                "w_only_num": 0.0,
                "a_only_num": 0.0,
                "w4a8_num": 0.0,
                "added_num": 0.0,
                "signal": 0.0,
                "w4a16_signal": 0.0,
                "input_num": 0.0,
                "input_signal": 0.0,
            }
            saturation_weighted = 0.0
            row_total = 0

            for start in range(0, int(x_cpu.shape[0]), chunk_rows):
                x = x_cpu[start : start + chunk_rows].to(device=device, dtype=torch.float32)
                xq, qstats = quantize_activation_i8(x)
                base = F.linear(x, weight)
                w4a16 = F.linear(x, qweight)
                a8_fp = F.linear(xq, weight)
                w4a8 = F.linear(xq, qweight)

                sums["w_only_num"] += float((w4a16 - base).pow(2).sum().detach().cpu().item())
                sums["a_only_num"] += float((a8_fp - base).pow(2).sum().detach().cpu().item())
                sums["w4a8_num"] += float((w4a8 - base).pow(2).sum().detach().cpu().item())
                sums["added_num"] += float((w4a8 - w4a16).pow(2).sum().detach().cpu().item())
                sums["signal"] += float(base.pow(2).sum().detach().cpu().item())
                sums["w4a16_signal"] += float(w4a16.pow(2).sum().detach().cpu().item())
                sums["input_num"] += float((xq - x).pow(2).sum().detach().cpu().item())
                sums["input_signal"] += float(x.pow(2).sum().detach().cpu().item())
                saturation_weighted += qstats["activation_saturation_fraction"] * int(x.shape[0])
                row_total += int(x.shape[0])
                del x, xq, base, w4a16, a8_fp, w4a8

            signal = max(sums["signal"], 1.0e-24)
            w4a16_signal = max(sums["w4a16_signal"], 1.0e-24)
            input_signal = max(sums["input_signal"], 1.0e-24)
            records.append(
                {
                    "module": name,
                    "family": item.get("family", "other"),
                    "layer": item.get("layer"),
                    "rows": esmp.rows,
                    "cols": esmp.cols,
                    "assigned_bits": int(item.get("bits", 0)),
                    "avg_row_bits": esmp.avg_bits,
                    "row_bits_histogram": esmp.bit_histogram,
                    "sample_rows": int(x_cpu.shape[0]),
                    "compression_vs_fp32": esmp.compression_vs_fp32,
                    "w_only_rel_l2": math.sqrt(sums["w_only_num"] / signal),
                    "a_only_rel_l2": math.sqrt(sums["a_only_num"] / signal),
                    "w4a8_rel_l2": math.sqrt(sums["w4a8_num"] / signal),
                    "activation_added_rel_l2_vs_w4a16": math.sqrt(sums["added_num"] / w4a16_signal),
                    "activation_input_rel_l2": math.sqrt(sums["input_num"] / input_signal),
                    "activation_saturation_fraction": saturation_weighted / max(row_total, 1),
                }
            )
            del weight, qweight
            if device == "cuda":
                torch.cuda.empty_cache()
            gc.collect()
            if progress_every and (idx == 1 or idx % progress_every == 0 or idx == len(modules)):
                print(json.dumps({"progress": f"{idx}/{len(modules)}", "module": name, "elapsed_sec": round(time.time() - started, 2)}), flush=True)
    return records


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    ok = [record for record in records if "error" not in record]

    def vals(key: str) -> list[float]:
        return [float(record[key]) for record in ok]

    return {
        "modules_requested": len(records),
        "modules_ok": len(ok),
        "modules_failed": len(records) - len(ok),
        "median_w_only_rel_l2": safe_median(vals("w_only_rel_l2")),
        "median_w4a8_rel_l2": safe_median(vals("w4a8_rel_l2")),
        "p90_w4a8_rel_l2": percentile(vals("w4a8_rel_l2"), 0.90),
        "max_w4a8_rel_l2": max(vals("w4a8_rel_l2"), default=0.0),
        "median_activation_added_rel_l2": safe_median(vals("activation_added_rel_l2_vs_w4a16")),
        "p90_activation_added_rel_l2": percentile(vals("activation_added_rel_l2_vs_w4a16"), 0.90),
        "max_activation_added_rel_l2": max(vals("activation_added_rel_l2_vs_w4a16"), default=0.0),
        "median_activation_input_rel_l2": safe_median(vals("activation_input_rel_l2")),
        "max_activation_saturation_fraction": max(vals("activation_saturation_fraction"), default=0.0),
        "median_compression_vs_fp32": safe_median(vals("compression_vs_fp32")),
    }


def markdown_report(result: dict[str, Any]) -> str:
    s = result["summary"]
    lines = [
        "# W4A8 Activation Reconstruction Report",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Package summary: `{result['package_summary']}`",
        f"Device: `{result['device']}`",
        f"Prompts: `{result['prompt_count']}`; max length: `{result['max_length']}`",
        "",
        "## Aggregate",
        "",
        f"- Modules OK: `{s['modules_ok']}/{s['modules_requested']}`",
        f"- Median W4A16 output rel-L2: `{s['median_w_only_rel_l2']:.6f}`",
        f"- Median W4A8 output rel-L2: `{s['median_w4a8_rel_l2']:.6f}`",
        f"- P90 W4A8 output rel-L2: `{s['p90_w4a8_rel_l2']:.6f}`",
        f"- Max W4A8 output rel-L2: `{s['max_w4a8_rel_l2']:.6f}`",
        f"- Median activation-added rel-L2 vs W4A16: `{s['median_activation_added_rel_l2']:.6f}`",
        f"- P90 activation-added rel-L2 vs W4A16: `{s['p90_activation_added_rel_l2']:.6f}`",
        f"- Max activation-added rel-L2 vs W4A16: `{s['max_activation_added_rel_l2']:.6f}`",
        f"- Median activation input rel-L2: `{s['median_activation_input_rel_l2']:.6f}`",
        f"- Max activation saturation fraction: `{s['max_activation_saturation_fraction']:.6f}`",
        f"- Median compression vs FP32: `{s['median_compression_vs_fp32']:.4f}x`",
        f"- Peak CUDA allocated: `{result.get('peak_cuda_memory_mib', 0.0):.2f} MiB`",
        f"- Peak CUDA allocation ratio: `{result.get('peak_cuda_memory_ratio', 0.0):.4f}`",
        "",
        "## Per-Module Results",
        "",
        "| module | bits | samples | W4A16 rel-L2 | W4A8 rel-L2 | activation-added rel-L2 | activation input rel-L2 | compression |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    rows = sorted([r for r in result["records"] if "error" not in r], key=lambda r: float(r["activation_added_rel_l2_vs_w4a16"]), reverse=True)
    for r in rows:
        lines.append(
            f"| `{r['module']}` | {r['assigned_bits']} | {r['sample_rows']} | "
            f"{r['w_only_rel_l2']:.6f} | {r['w4a8_rel_l2']:.6f} | "
            f"{r['activation_added_rel_l2_vs_w4a16']:.6f} | {r['activation_input_rel_l2']:.6f} | "
            f"{r['compression_vs_fp32']:.4f}x |"
        )
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "Valid claim: on selected real Qwen3 module activations, the extra drift from per-row A8 activation quantization is measured and bounded.",
            "",
            "Invalid claim: this does not prove end-to-end generation speedup, full-model quality retention, mobile deployment, or SOTA quantization.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate W4A8 activation drift on real module inputs.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--package-summary", default=DEFAULT_PACKAGE_SUMMARY)
    parser.add_argument("--prompts", default="")
    parser.add_argument("--limit-prompts", type=int, default=4)
    parser.add_argument("--max-length", type=int, default=96)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--module", action="append", default=[])
    parser.add_argument("--module-filter", action="append", default=[])
    parser.add_argument("--layers", default="")
    parser.add_argument("--include-lm-head", action="store_true")
    parser.add_argument("--max-modules", type=int, default=8)
    parser.add_argument("--sample-rows-per-module", type=int, default=64)
    parser.add_argument("--chunk-rows", type=int, default=32)
    parser.add_argument("--progress-every", type=int, default=4)
    parser.add_argument("--out-json", default=f"{DEFAULT_OUT_DIR}/w4a8_activation_reconstruction.json")
    parser.add_argument("--out-jsonl", default=f"{DEFAULT_OUT_DIR}/w4a8_activation_reconstruction.jsonl")
    parser.add_argument("--out-md", default=f"{DEFAULT_OUT_DIR}/W4A8_ACTIVATION_RECONSTRUCTION.md")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("This script requires torch and transformers.")
    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but unavailable.")

    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    if args.device == "cuda":
        torch.cuda.reset_peak_memory_stats()

    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=args.local_files_only, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=dtype, local_files_only=args.local_files_only, trust_remote_code=True)
    model.eval().to(args.device)

    model_modules = {name: module for name, module in model.named_modules() if isinstance(module, torch.nn.Linear)}
    selected = select_package_modules(
        modules=load_package_modules(package_summary),
        model_modules=model_modules,
        module_names=args.module,
        filters=args.module_filter,
        layers=parse_layers(args.layers),
        include_lm_head=args.include_lm_head,
        max_modules=args.max_modules,
    )
    if not selected:
        raise SystemExit("No modules selected.")

    prompts = load_prompts(args.prompts, args.limit_prompts) if args.prompts else DEFAULT_PROMPTS[: args.limit_prompts]
    sampled_inputs, row_counts = collect_module_inputs(
        model=model,
        tokenizer=tokenizer,
        prompts=prompts,
        modules=selected,
        device=args.device,
        max_length=args.max_length,
        sample_rows_per_module=args.sample_rows_per_module,
    )
    records = score_modules(selected, sampled_inputs, args.device, args.chunk_rows, args.progress_every)
    peak_mib = float(torch.cuda.max_memory_allocated() / (1024**2)) if args.device == "cuda" else 0.0
    total_mib = float(torch.cuda.get_device_properties(0).total_memory / (1024**2)) if args.device == "cuda" else 0.0
    result = {
        "date": time.strftime("%Y-%m-%d"),
        "model": args.model,
        "package_summary": str(package_summary),
        "prompt_count": len(prompts),
        "max_length": args.max_length,
        "device": args.device,
        "dtype": args.dtype,
        "sample_rows_per_module": args.sample_rows_per_module,
        "row_count_min": min(row_counts.values()) if row_counts else 0,
        "row_count_max": max(row_counts.values()) if row_counts else 0,
        "selected_modules": [item["module"] for item in selected],
        "summary": summarize(records),
        "records": records,
        "peak_cuda_memory_mib": peak_mib,
        "peak_cuda_memory_ratio": peak_mib / max(total_mib, 1.0),
    }

    out_json = resolve_path(args.out_json, root)
    out_jsonl = resolve_path(args.out_jsonl, root)
    out_md = resolve_path(args.out_md, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with out_jsonl.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    out_md.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "summary": result["summary"], "peak_cuda_memory_ratio": result["peak_cuda_memory_ratio"]}, ensure_ascii=False, indent=2))

    del model
    if args.device == "cuda":
        torch.cuda.empty_cache()
    gc.collect()


if __name__ == "__main__":
    main()
