#!/usr/bin/env python3
from __future__ import annotations

"""Evaluate ESMP packed weights on real module activations.

This script links the real C++ ESMP packer artifact back to model quality at a
local module level. It samples inputs to selected Linear modules on prompt text,
loads the corresponding ``.esmp`` binary package, reconstructs the dequantized
weight matrix, and compares:

    F.linear(x, original_weight) vs F.linear(x, ESMP_dequant_weight)

The result is an activation-conditioned reconstruction report. It is not an
end-to-end perplexity or generation benchmark.
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
    import numpy as np
    import torch
    import torch.nn.functional as F
    from transformers import AutoModelForCausalLM, AutoTokenizer
except ModuleNotFoundError:  # pragma: no cover - runtime dependency check
    np = None
    torch = None
    F = None
    AutoModelForCausalLM = None
    AutoTokenizer = None

from esmp_format import dequantize_esmp_weight, read_esmp
from measure_module_output_sensitivity import DEFAULT_PROMPTS, collect_module_inputs, load_prompts


DEFAULT_MODEL = "Qwen/Qwen3-0.6B"
DEFAULT_PACKAGE_SUMMARY = "outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp/pack_summary.json"
DEFAULT_OUT_DIR = "outputs/real_system_packer_2026-06-05"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def resolve_path(path: str | Path, base: Path) -> Path:
    value = Path(path)
    return value if value.is_absolute() else base / value


def maybe_wsl_to_windows_path(path: str) -> str:
    if path.startswith("/mnt/") and len(path) > 6 and path[5] == "/":
        drive = path[5].upper()
        rest = path[7:].replace("/", "\\")
        return f"{drive}:\\{rest}"
    return path


def path_exists_cross(path: str | Path) -> Path:
    value = Path(path)
    if value.exists():
        return value
    converted = Path(maybe_wsl_to_windows_path(str(path)))
    if converted.exists():
        return converted
    return value


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_mean(values: list[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def safe_median(values: list[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    pos = (len(ordered) - 1) * q
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return float(ordered[lo])
    frac = pos - lo
    return float(ordered[lo] * (1.0 - frac) + ordered[hi] * frac)


def load_package_modules(package_summary: Path) -> list[dict[str, Any]]:
    summary = load_json(package_summary)
    modules = []
    for item in summary.get("modules", []):
        module = str(item.get("module") or "")
        out = str(item.get("out") or "")
        if not module or not out:
            continue
        modules.append(
            {
                "module": module,
                "bits": int(item.get("bits", 0)),
                "rows": int(item.get("rows", 0)),
                "cols": int(item.get("cols", 0)),
                "out": str(path_exists_cross(out)),
                "packer": item.get("packer", {}),
            }
        )
    return modules


def parse_layers(text: str) -> set[int] | None:
    if not text:
        return None
    values = set()
    for part in text.replace(";", ",").split(","):
        part = part.strip()
        if part:
            values.add(int(part))
    return values


def module_layer(name: str) -> int | None:
    marker = ".layers."
    if marker not in name:
        return None
    rest = name.split(marker, 1)[1]
    token = rest.split(".", 1)[0]
    return int(token) if token.isdigit() else None


def module_family(name: str) -> str:
    if ".self_attn." in name:
        return "attention"
    if ".mlp." in name:
        return "mlp"
    if name == "lm_head":
        return "lm_head"
    return "other"


def select_package_modules(
    modules: list[dict[str, Any]],
    model_modules: dict[str, torch.nn.Module],
    module_names: list[str],
    filters: list[str],
    layers: set[int] | None,
    include_lm_head: bool,
    max_modules: int,
) -> list[dict[str, Any]]:
    selected = []
    wanted = set(module_names)
    for item in modules:
        name = item["module"]
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
        path = Path(item["out"])
        if not path.exists():
            continue
        item = dict(item)
        item["family"] = module_family(name)
        item["layer"] = layer
        item["_module_ref"] = model_modules[name]
        selected.append(item)
        if max_modules and len(selected) >= max_modules:
            break
    return selected


def score_modules(
    modules: list[dict[str, Any]],
    sampled_inputs: dict[str, list[torch.Tensor]],
    device: str,
    chunk_rows: int,
    progress_every: int,
) -> list[dict[str, Any]]:
    records = []
    start_time = time.time()
    with torch.inference_mode():
        for idx, item in enumerate(modules, start=1):
            name = item["module"]
            rows = sampled_inputs.get(name, [])
            if not rows:
                records.append({"module": name, "sample_rows": 0, "error": "no_sampled_inputs"})
                continue

            esmp = read_esmp(Path(item["out"]))
            module = item["_module_ref"]
            expected_shape = tuple(module.weight.shape)
            if expected_shape != (esmp.rows, esmp.cols):
                records.append(
                    {
                        "module": name,
                        "sample_rows": 0,
                        "error": f"shape_mismatch model={expected_shape} esmp={(esmp.rows, esmp.cols)}",
                    }
                )
                continue

            x_cpu = torch.cat(rows, dim=0)
            qweight_cpu = dequantize_esmp_weight(esmp)
            base_weight_cpu = module.weight.detach().to(device="cpu", dtype=torch.float32)
            weight_diff = qweight_cpu - base_weight_cpu
            weight_diff_sq = float(weight_diff.pow(2).sum().item())
            weight_signal_sq = float(base_weight_cpu.pow(2).sum().item())
            weight_rel_l2 = math.sqrt(weight_diff_sq / max(weight_signal_sq, 1.0e-24))
            weight_max_abs = float(weight_diff.abs().max().item()) if weight_diff.numel() else 0.0

            qweight = qweight_cpu.to(device=device, dtype=torch.float32)
            weight = base_weight_cpu.to(device=device, dtype=torch.float32)
            sum_sq = 0.0
            signal_sq = 0.0
            max_abs = 0.0
            count = 0
            for start in range(0, int(x_cpu.shape[0]), chunk_rows):
                x = x_cpu[start : start + chunk_rows].to(device=device, dtype=torch.float32)
                base = F.linear(x, weight)
                pred = F.linear(x, qweight)
                diff = pred - base
                sum_sq += float(diff.pow(2).sum().detach().cpu().item())
                signal_sq += float(base.pow(2).sum().detach().cpu().item())
                max_abs = max(max_abs, float(diff.abs().max().detach().cpu().item()))
                count += int(diff.numel())
                del x, base, pred, diff

            output_mse = sum_sq / max(count, 1)
            output_signal = signal_sq / max(count, 1)
            normalized_mse = output_mse / max(output_signal, 1.0e-24)
            output_rel_l2 = math.sqrt(sum_sq / max(signal_sq, 1.0e-24))
            record = {
                "module": name,
                "family": item.get("family", "other"),
                "layer": item.get("layer"),
                "rows": esmp.rows,
                "cols": esmp.cols,
                "assigned_bits": int(item.get("bits", 0)),
                "avg_row_bits": esmp.avg_bits,
                "row_bits_histogram": esmp.bit_histogram,
                "sample_rows": int(x_cpu.shape[0]),
                "raw_fp32_bytes": esmp.raw_fp32_bytes,
                "package_bytes": esmp.package_bytes,
                "compression_vs_fp32": esmp.compression_vs_fp32,
                "weight_rel_l2": weight_rel_l2,
                "weight_max_abs": weight_max_abs,
                "output_mse": output_mse,
                "output_signal": output_signal,
                "normalized_output_mse": normalized_mse,
                "output_rel_l2": output_rel_l2,
                "output_max_abs": max_abs,
                "packer_verify_gemv_rel_l2": float(item.get("packer", {}).get("verify_gemv_rel_l2", -1.0)),
            }
            records.append(record)

            del qweight, weight, qweight_cpu, base_weight_cpu, weight_diff, x_cpu
            if device == "cuda":
                torch.cuda.empty_cache()
            gc.collect()
            if progress_every and (idx == 1 or idx % progress_every == 0 or idx == len(modules)):
                print(
                    json.dumps(
                        {
                            "progress": f"{idx}/{len(modules)}",
                            "module": name,
                            "output_rel_l2": output_rel_l2,
                            "elapsed_sec": round(time.time() - start_time, 2),
                        },
                        ensure_ascii=False,
                    ),
                    flush=True,
                )
    return records


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    ok = [record for record in records if "error" not in record]
    output_rel = [float(record["output_rel_l2"]) for record in ok]
    normalized = [float(record["normalized_output_mse"]) for record in ok]
    weight_rel = [float(record["weight_rel_l2"]) for record in ok]
    compression = [float(record["compression_vs_fp32"]) for record in ok]
    families: dict[str, dict[str, Any]] = {}
    for record in ok:
        family = str(record.get("family", "other"))
        bucket = families.setdefault(family, {"count": 0, "output_rel_l2": [], "compression_vs_fp32": []})
        bucket["count"] += 1
        bucket["output_rel_l2"].append(float(record["output_rel_l2"]))
        bucket["compression_vs_fp32"].append(float(record["compression_vs_fp32"]))
    for bucket in families.values():
        bucket["median_output_rel_l2"] = safe_median(bucket.pop("output_rel_l2"))
        bucket["median_compression_vs_fp32"] = safe_median(bucket.pop("compression_vs_fp32"))

    return {
        "modules_requested": len(records),
        "modules_ok": len(ok),
        "modules_failed": len(records) - len(ok),
        "median_output_rel_l2": safe_median(output_rel),
        "mean_output_rel_l2": safe_mean(output_rel),
        "p90_output_rel_l2": percentile(output_rel, 0.90),
        "median_normalized_output_mse": safe_median(normalized),
        "mean_normalized_output_mse": safe_mean(normalized),
        "median_weight_rel_l2": safe_median(weight_rel),
        "mean_weight_rel_l2": safe_mean(weight_rel),
        "median_compression_vs_fp32": safe_median(compression),
        "mean_compression_vs_fp32": safe_mean(compression),
        "families": families,
    }


def markdown_report(result: dict[str, Any]) -> str:
    summary = result["summary"]
    lines = [
        "# ESMP Activation Reconstruction Report",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Package summary: `{result['package_summary']}`",
        f"Prompts: `{result['prompt_count']}`",
        f"Max length: `{result['max_length']}`",
        f"Sample rows per module: `{result['sample_rows_per_module']}`",
        f"Device: `{result['device']}`",
        "",
        "## Aggregate",
        "",
        f"- Modules OK: `{summary['modules_ok']}/{summary['modules_requested']}`",
        f"- Median output rel-L2: `{summary['median_output_rel_l2']:.6f}`",
        f"- P90 output rel-L2: `{summary['p90_output_rel_l2']:.6f}`",
        f"- Median normalized output MSE: `{summary['median_normalized_output_mse']:.8f}`",
        f"- Median weight rel-L2: `{summary['median_weight_rel_l2']:.6f}`",
        f"- Median compression vs FP32: `{summary['median_compression_vs_fp32']:.4f}x`",
        f"- Peak CUDA memory allocated by script: `{result.get('peak_cuda_memory_mib', 0):.2f} MiB`",
        "",
        "## Family Summary",
        "",
        "| family | modules | median output rel-L2 | median compression vs FP32 |",
        "|---|---:|---:|---:|",
    ]
    for family, bucket in sorted(summary["families"].items()):
        lines.append(
            f"| {family} | {bucket['count']} | {bucket['median_output_rel_l2']:.6f} | "
            f"{bucket['median_compression_vs_fp32']:.4f}x |"
        )

    rows = [record for record in result["records"] if "error" not in record]
    rows = sorted(rows, key=lambda item: float(item["output_rel_l2"]), reverse=True)
    lines.extend(
        [
            "",
            f"## Per-Module Results ({len(rows)})",
            "",
            "| module | bits | sample rows | output rel-L2 | norm MSE | weight rel-L2 | compression |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for record in rows:
        lines.append(
            f"| `{record['module']}` | {record['assigned_bits']} | {record['sample_rows']} | "
            f"{record['output_rel_l2']:.6f} | {record['normalized_output_mse']:.8f} | "
            f"{record['weight_rel_l2']:.6f} | {record['compression_vs_fp32']:.4f}x |"
        )

    failures = [record for record in result["records"] if "error" in record]
    if failures:
        lines.extend(["", "## Failures", ""])
        for record in failures:
            lines.append(f"- `{record.get('module')}`: {record.get('error')}")

    lines.extend(
        [
            "",
            "## Scope",
            "",
            "- This evaluates ESMP package reconstruction on sampled real module activations.",
            "- It is a local module-quality check, not an end-to-end packed LLM runtime.",
            "- The next step is replacing the selected Linear modules during generation and measuring TTFT/tokens/s.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate ESMP dequantized weights on real activations.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--package-summary", default=DEFAULT_PACKAGE_SUMMARY)
    parser.add_argument("--prompts", default="")
    parser.add_argument("--limit-prompts", type=int, default=4)
    parser.add_argument("--max-length", type=int, default=96)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--module", action="append", default=[], help="Exact module name; may be repeated.")
    parser.add_argument("--module-filter", action="append", default=[], help="Substring filter; may be repeated.")
    parser.add_argument("--layers", default="", help="Comma-separated layer ids, e.g. 0,1,7,13,20,27")
    parser.add_argument("--include-lm-head", action="store_true")
    parser.add_argument("--max-modules", type=int, default=0)
    parser.add_argument("--sample-rows-per-module", type=int, default=64)
    parser.add_argument("--chunk-rows", type=int, default=32)
    parser.add_argument("--progress-every", type=int, default=8)
    parser.add_argument("--out-json", default=f"{DEFAULT_OUT_DIR}/esmp_activation_reconstruction.json")
    parser.add_argument("--out-jsonl", default=f"{DEFAULT_OUT_DIR}/esmp_activation_reconstruction.jsonl")
    parser.add_argument("--out-md", default=f"{DEFAULT_OUT_DIR}/ESMP_ACTIVATION_RECONSTRUCTION.md")
    args = parser.parse_args()

    if torch is None or np is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("This script requires numpy, torch, and transformers in the WSL GPU environment.")
    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")

    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    if args.device == "cuda":
        torch.cuda.reset_peak_memory_stats()

    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=args.local_files_only, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )
    model.eval()
    model.to(args.device)

    model_modules = {name: module for name, module in model.named_modules() if isinstance(module, torch.nn.Linear)}
    package_modules = load_package_modules(package_summary)
    selected = select_package_modules(
        modules=package_modules,
        model_modules=model_modules,
        module_names=args.module,
        filters=args.module_filter,
        layers=parse_layers(args.layers),
        include_lm_head=args.include_lm_head,
        max_modules=args.max_modules,
    )
    if not selected:
        raise SystemExit("No ESMP modules selected. Check --package-summary, --layers, --module-filter, or --module.")

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
    records = score_modules(
        modules=selected,
        sampled_inputs=sampled_inputs,
        device=args.device,
        chunk_rows=args.chunk_rows,
        progress_every=args.progress_every,
    )
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
        "peak_cuda_memory_mib": (
            float(torch.cuda.max_memory_allocated() / (1024**2)) if args.device == "cuda" else 0.0
        ),
    }

    out_json = resolve_path(args.out_json, root)
    out_jsonl = resolve_path(args.out_jsonl, root)
    out_md = resolve_path(args.out_md, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with out_jsonl.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_report(result), encoding="utf-8")

    print(
        json.dumps(
            {
                "out_json": str(out_json),
                "out_jsonl": str(out_jsonl),
                "out_md": str(out_md),
                "summary": result["summary"],
                "peak_cuda_memory_mib": result["peak_cuda_memory_mib"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )

    del model
    if args.device == "cuda":
        torch.cuda.empty_cache()
    gc.collect()


if __name__ == "__main__":
    main()
