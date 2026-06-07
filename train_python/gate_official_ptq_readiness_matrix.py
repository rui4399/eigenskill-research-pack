#!/usr/bin/env python3
from __future__ import annotations

"""Build a compact readiness matrix across official PTQ package probes.

This gate deliberately compares readiness evidence, not quantization quality.
It checks that official-package probes share the same model, W-bit/group-size
shape, and public eval labels before the repository presents them together.
"""

import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def finite(value: Any) -> bool:
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def parse_labeled_path(raw: str) -> tuple[str, Path]:
    if "=" not in raw:
        raise argparse.ArgumentTypeError("expected label=path")
    label, path = raw.split("=", 1)
    label = label.strip()
    if not label:
        raise argparse.ArgumentTypeError("label cannot be empty")
    return label, Path(path)


def normalize_quant_shape(summary: dict[str, Any]) -> dict[str, int | None]:
    config = summary.get("quant_config", {}) if isinstance(summary.get("quant_config"), dict) else {}
    bits = config.get("bits", config.get("w_bit"))
    group_size = config.get("group_size", config.get("q_group_size"))
    return {
        "bits": int(bits) if bits is not None else None,
        "group_size": int(group_size) if group_size is not None else None,
    }


def extract_eval_metrics(row: dict[str, Any], package: str) -> dict[str, Any]:
    quant_ppl = row.get(f"{package}_ppl")
    ratio = row.get(f"ppl_ratio_{package}_vs_fp16")
    if quant_ppl is None and package == "autoawq":
        quant_ppl = row.get("awq_ppl")
        ratio = row.get("ppl_ratio_awq_vs_fp16")
    if quant_ppl is None and package == "gptqmodel":
        quant_ppl = row.get("gptq_ppl")
        ratio = row.get("ppl_ratio_gptq_vs_fp16")
    return {
        "fp16_ppl": row.get("fp16_ppl"),
        "quant_ppl": quant_ppl,
        "ppl_ratio_vs_fp16": ratio,
        "guard_max_memory_used_ratio": row.get("guard_max_memory_used_ratio"),
    }


def build_case(label: str, gate_result: dict[str, Any], args: argparse.Namespace) -> tuple[list[str], dict[str, Any]]:
    failures: list[str] = []
    summary = gate_result.get("summary", {}) if isinstance(gate_result.get("summary"), dict) else {}
    package = summary.get("package") or label
    eval_rows = summary.get("evals") if isinstance(summary.get("evals"), list) else []
    label_set = {str(row.get("label")) for row in eval_rows if row.get("label") is not None}
    total_tokens = int(summary.get("total_eval_tokens") or 0)
    normalized_rows: list[dict[str, Any]] = []

    if not gate_result.get("passed"):
        failures.append(f"{package} gate did not pass")
    if len(eval_rows) < args.min_eval_slices:
        failures.append(f"{package} eval slices {len(eval_rows)} < {args.min_eval_slices}")
    if total_tokens < args.min_total_tokens:
        failures.append(f"{package} total eval tokens {total_tokens} < {args.min_total_tokens}")
    for required_label in args.required_labels:
        if required_label not in label_set:
            failures.append(f"{package} missing required eval label {required_label}")

    for row in eval_rows:
        metrics = extract_eval_metrics(row, str(package))
        ratio = metrics["ppl_ratio_vs_fp16"]
        memory_ratio = metrics["guard_max_memory_used_ratio"]
        tokens = int(row.get("tokens") or 0)
        if tokens <= 0:
            failures.append(f"{package}:{row.get('label')} eval has no tokens")
        if not finite(metrics["fp16_ppl"]) or not finite(metrics["quant_ppl"]):
            failures.append(f"{package}:{row.get('label')} has non-finite PPL")
        if not finite(ratio):
            failures.append(f"{package}:{row.get('label')} PPL ratio is non-finite")
        elif float(ratio) > args.max_ppl_ratio:
            failures.append(f"{package}:{row.get('label')} PPL ratio {float(ratio):.4f} > {args.max_ppl_ratio:.4f}")
        if finite(memory_ratio) and float(memory_ratio) > args.max_memory_ratio:
            failures.append(f"{package}:{row.get('label')} VRAM ratio {float(memory_ratio):.4f} > {args.max_memory_ratio:.4f}")
        normalized_rows.append(
            {
                "label": row.get("label"),
                "prompt_count": row.get("prompt_count"),
                "tokens": tokens,
                **metrics,
            }
        )

    case = {
        "input_label": label,
        "package": package,
        "package_version": summary.get("package_version"),
        "model": summary.get("model"),
        "quant_shape": normalize_quant_shape(summary),
        "calibration_source": summary.get("calibration_source"),
        "artifact_file_count": summary.get("artifact_file_count"),
        "artifact_total_bytes": summary.get("artifact_total_bytes"),
        "eval_slice_count": len(eval_rows),
        "total_eval_tokens": total_tokens,
        "eval_labels": sorted(label_set),
        "evals": normalized_rows,
    }
    return failures, case


def unique_sorted(values: list[Any]) -> list[Any]:
    return sorted({json.dumps(value, sort_keys=True): value for value in values}.values(), key=lambda item: json.dumps(item, sort_keys=True))


def build_result(*, cases: list[tuple[str, dict[str, Any]]], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    case_rows: list[dict[str, Any]] = []

    if len(cases) < args.min_packages:
        failures.append(f"package cases {len(cases)} < {args.min_packages}")

    for label, gate_result in cases:
        case_failures, case = build_case(label, gate_result, args)
        failures.extend(case_failures)
        case_rows.append(case)

    packages = sorted({str(case["package"]) for case in case_rows})
    for package in args.required_packages:
        if package not in packages:
            failures.append(f"missing required package {package}")

    models = unique_sorted([case.get("model") for case in case_rows if case.get("model")])
    quant_shapes = unique_sorted([case["quant_shape"] for case in case_rows])
    if args.require_same_model and len(models) > 1:
        failures.append(f"models are not aligned: {models}")
    if args.require_same_quant_shape and len(quant_shapes) > 1:
        failures.append(f"quant shapes are not aligned: {quant_shapes}")

    label_sets = [set(case["eval_labels"]) for case in case_rows]
    common_eval_labels = sorted(set.intersection(*label_sets)) if label_sets else []
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "package_count": len(case_rows),
            "packages": packages,
            "models": models,
            "quant_shapes": quant_shapes,
            "required_packages": list(args.required_packages),
            "required_eval_labels": list(args.required_labels),
            "common_eval_labels": common_eval_labels,
            "total_eval_tokens": sum(int(case["total_eval_tokens"] or 0) for case in case_rows),
            "cases": case_rows,
        },
        "failures": failures,
        "claim_boundary": (
            "Valid claim: official-package readiness probes are presented in one aligned matrix "
            "for the same model family, W-bit/group-size shape, and tiny public eval labels. "
            "Invalid claim: this matrix proves AWQ/GPTQ competitiveness, SOTA PTQ quality, "
            "task retention, or production runtime readiness."
        ),
    }


def format_float(value: Any) -> str:
    if not finite(value):
        return "NA"
    return f"{float(value):.6f}"


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        "# Official PTQ Readiness Matrix",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- packages: `{summary['packages']}`",
        f"- models: `{summary['models']}`",
        f"- quant shapes: `{summary['quant_shapes']}`",
        f"- common eval labels: `{summary['common_eval_labels']}`",
        f"- total eval tokens across probes: `{summary['total_eval_tokens']}`",
        "",
        "## Matrix",
        "",
        "| package | slice | prompts | tokens | FP16 PPL | quant PPL | ratio | peak VRAM |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for case in summary["cases"]:
        package = case["package"]
        for row in case["evals"]:
            lines.append(
                f"| `{package}` | `{row['label']}` | {row['prompt_count']} | {row['tokens']} | "
                f"{format_float(row['fp16_ppl'])} | {format_float(row['quant_ppl'])} | "
                f"{format_float(row['ppl_ratio_vs_fp16'])} | {format_float(row['guard_max_memory_used_ratio'])} |"
            )
    lines.extend(["", "## Failures", ""])
    if result["failures"]:
        lines.extend(f"- {failure}" for failure in result["failures"])
    else:
        lines.append("- none")
    lines.extend(["", "## Claim Boundary", "", f"- {result['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build official PTQ readiness matrix.")
    parser.add_argument("--case", type=parse_labeled_path, action="append", default=[])
    parser.add_argument("--required-package", dest="required_packages", action="append", default=[])
    parser.add_argument("--required-label", dest="required_labels", action="append", default=[])
    parser.add_argument("--min-packages", type=int, default=2)
    parser.add_argument("--min-eval-slices", type=int, default=2)
    parser.add_argument("--min-total-tokens", type=int, default=256)
    parser.add_argument("--max-ppl-ratio", type=float, default=2.0)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--allow-mixed-models", action="store_true")
    parser.add_argument("--allow-mixed-quant-shapes", action="store_true")
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()
    if not args.required_packages:
        args.required_packages = ["autoawq", "gptqmodel"]
    if not args.required_labels:
        args.required_labels = ["wikitext2", "c4"]
    args.require_same_model = not args.allow_mixed_models
    args.require_same_quant_shape = not args.allow_mixed_quant_shapes

    cases = [(label, load_json(path)) for label, path in args.case]
    result = build_result(cases=cases, args=args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "failures": result["failures"]}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
