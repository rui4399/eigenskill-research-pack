#!/usr/bin/env python3
from __future__ import annotations

"""Rank ESMP rows/groups by activation-conditioned reconstruction error."""

import argparse
import json
import math
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

from esmp_format import dequantize_esmp_weight, read_esmp
from eval_esmp_module_reconstruction import DEFAULT_MODEL, load_package_modules, repo_root, resolve_path
from measure_module_output_sensitivity import collect_module_inputs, load_prompts


def find_package_module(modules: list[dict[str, Any]], name: str) -> dict[str, Any]:
    for item in modules:
        if str(item.get("module")) == name:
            return item
    raise SystemExit(f"module not found in package summary: {name}")


def rank_rows(
    x_cpu: torch.Tensor,
    weight_cpu: torch.Tensor,
    qweight_cpu: torch.Tensor,
    device: str,
    chunk_rows: int,
) -> tuple[list[float], list[float], list[float]]:
    rows = int(weight_cpu.shape[0])
    error_sq = torch.zeros(rows, dtype=torch.float64)
    signal_sq = torch.zeros(rows, dtype=torch.float64)
    with torch.inference_mode():
        weight = weight_cpu.to(device=device, dtype=torch.float32)
        qweight = qweight_cpu.to(device=device, dtype=torch.float32)
        delta = qweight - weight
        for start in range(0, int(x_cpu.shape[0]), chunk_rows):
            x = x_cpu[start : start + chunk_rows].to(device=device, dtype=torch.float32)
            diff = torch.nn.functional.linear(x, delta)
            base = torch.nn.functional.linear(x, weight)
            error_sq += diff.pow(2).sum(dim=0).detach().cpu().double()
            signal_sq += base.pow(2).sum(dim=0).detach().cpu().double()
            del x, diff, base
        del weight, qweight, delta
        if device == "cuda":
            torch.cuda.empty_cache()
    score = (error_sq / signal_sq.clamp_min(1.0e-24)).tolist()
    return [float(v) for v in score], [float(v) for v in error_sq.tolist()], [float(v) for v in signal_sq.tolist()]


def summarize_groups(row_scores: list[float], row_errors: list[float], row_signals: list[float], group_size: int) -> list[dict[str, Any]]:
    groups = []
    rows = len(row_scores)
    for start in range(0, rows, group_size):
        end = min(start + group_size, rows)
        scores = row_scores[start:end]
        errors = row_errors[start:end]
        signals = row_signals[start:end]
        groups.append(
            {
                "group": start // group_size,
                "start": start,
                "end": end,
                "rows": end - start,
                "mean_row_score": float(sum(scores) / max(len(scores), 1)),
                "max_row_score": float(max(scores) if scores else 0.0),
                "sum_error_sq": float(sum(errors)),
                "sum_signal_sq": float(sum(signals)),
                "group_score": float(sum(errors) / max(sum(signals), 1.0e-24)),
            }
        )
    groups.sort(key=lambda item: (float(item["group_score"]), float(item["mean_row_score"])), reverse=True)
    return groups


def markdown_report(result: dict[str, Any]) -> str:
    lines = [
        "# ESMP Row/Group Error Ranking",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Module: `{result['module']}`",
        f"Package summary: `{result['package_summary']}`",
        f"Group size: `{result['group_size']}`",
        f"Sample rows: `{result['sample_rows']}`",
        f"Current row bits: `{result['row_bits_histogram']}`",
        "",
        "## Top Groups",
        "",
        "| rank | group | rows | group score | mean row score | max row score |",
        "|---:|---:|---|---:|---:|---:|",
    ]
    for rank, group in enumerate(result["groups"][: int(result["top_groups"])], start=1):
        lines.append(
            f"| {rank} | {group['group']} | `{group['start']}:{group['end']}` | "
            f"{group['group_score']:.8f} | {group['mean_row_score']:.8f} | {group['max_row_score']:.8f} |"
        )
    lines.extend(
        [
            "",
            "## Top Rows",
            "",
            "| rank | row | score | error sq | signal sq |",
            "|---:|---:|---:|---:|---:|",
        ]
    )
    for rank, row in enumerate(result["top_rows"], start=1):
        lines.append(
            f"| {rank} | {row['row']} | {row['score']:.8f} | {row['error_sq']:.6e} | {row['signal_sq']:.6e} |"
        )
    lines.extend(
        [
            "",
            "## Guardrail",
            "",
            "This ranks local module reconstruction error on sampled activations. It suggests row/head candidates for follow-up prompt-suite tests; it is not an end-to-end quality metric by itself.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank ESMP rows/groups by activation-conditioned reconstruction error.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--package-summary", required=True)
    parser.add_argument("--module", required=True)
    parser.add_argument("--prompt-file", default="")
    parser.add_argument("--prompt-limit", type=int, default=0)
    parser.add_argument("--max-length", type=int, default=96)
    parser.add_argument("--sample-rows", type=int, default=512)
    parser.add_argument("--chunk-rows", type=int, default=256)
    parser.add_argument("--group-size", type=int, default=128)
    parser.add_argument("--top-groups", type=int, default=8)
    parser.add_argument("--top-rows", type=int, default=24)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--out-json", default="outputs/real_system_packer_2026-06-05/esmp_row_group_ranking.json")
    parser.add_argument("--out-md", default="outputs/real_system_packer_2026-06-05/ESMP_ROW_GROUP_RANKING.md")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("missing dependencies: install torch and transformers")
    if args.device.startswith("cuda") and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")

    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
    package_item = find_package_module(load_package_modules(package_summary), args.module)
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=args.local_files_only, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        device_map=args.device,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )
    model_modules = dict(model.named_modules())
    module = model_modules.get(args.module)
    if module is None or not isinstance(module, torch.nn.Linear):
        raise SystemExit(f"model module is not Linear or does not exist: {args.module}")

    prompts = load_prompts(args.prompt_file, args.prompt_limit)
    module_record = {"module": args.module, "_module_ref": module}
    sampled_inputs, row_counts = collect_module_inputs(
        model,
        tokenizer,
        prompts,
        [module_record],
        device=args.device,
        max_length=args.max_length,
        sample_rows_per_module=args.sample_rows,
    )
    rows = sampled_inputs.get(args.module, [])
    if not rows:
        raise SystemExit(f"no sampled inputs for {args.module}")
    x_cpu = torch.cat(rows, dim=0)

    esmp = read_esmp(Path(str(package_item["out"])))
    qweight_cpu = dequantize_esmp_weight(esmp)
    weight_cpu = module.weight.detach().to(device="cpu", dtype=torch.float32)
    row_scores, row_errors, row_signals = rank_rows(x_cpu, weight_cpu, qweight_cpu, args.device, args.chunk_rows)
    groups = summarize_groups(row_scores, row_errors, row_signals, args.group_size)
    top_rows = sorted(
        (
            {"row": row, "score": row_scores[row], "error_sq": row_errors[row], "signal_sq": row_signals[row]}
            for row in range(len(row_scores))
        ),
        key=lambda item: float(item["score"]),
        reverse=True,
    )[: args.top_rows]

    result = {
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "model": args.model,
        "module": args.module,
        "package_summary": str(package_summary),
        "package_out": str(package_item["out"]),
        "group_size": int(args.group_size),
        "top_groups": int(args.top_groups),
        "sample_rows": int(x_cpu.shape[0]),
        "row_count": int(esmp.rows),
        "col_count": int(esmp.cols),
        "row_bits_histogram": esmp.bit_histogram,
        "row_counts": row_counts,
        "groups": groups,
        "top_rows": top_rows,
    }
    out_json = resolve_path(args.out_json, root)
    out_md = resolve_path(args.out_md, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    out_md.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "top_groups": groups[: args.top_groups]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
