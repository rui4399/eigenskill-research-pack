#!/usr/bin/env python3
from __future__ import annotations

"""Gate tiny public-task execution smokes for official PTQ artifacts.

This gate is deliberately small and conservative. It verifies that FP16 and
official-package quantized artifacts can be loaded, evaluated on the same public
task formats, and compared under a GPU guard. It is not a leaderboard or broad
task-retention benchmark. Formats where the FP16 baseline is already zero are
tracked as execution-only evidence.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_case_spec(spec: str) -> tuple[str, str, Path, Path]:
    parts = spec.split("=", 2)
    if len(parts) != 3 or not all(part.strip() for part in parts):
        raise ValueError(f"case must be VARIANT:FORMAT=SUMMARY_JSON=GUARD_JSON: {spec}")
    label, summary_path, guard_path = parts
    if ":" not in label:
        raise ValueError(f"case label must be VARIANT:FORMAT: {spec}")
    variant, task_format = [part.strip() for part in label.split(":", 1)]
    if not variant or not task_format:
        raise ValueError(f"variant and format cannot be empty: {spec}")
    return variant, task_format, Path(summary_path), Path(guard_path)


def _aggregate(payload: dict[str, Any]) -> dict[str, Any]:
    baseline = payload.get("baseline", {}) if isinstance(payload.get("baseline"), dict) else {}
    return baseline.get("aggregate", {}) if isinstance(baseline.get("aggregate"), dict) else {}


def case_summary(variant: str, task_format: str, summary_path: Path, guard_path: Path) -> dict[str, Any]:
    payload = load_json(summary_path)
    guard = load_json(guard_path)
    aggregate = _aggregate(payload)
    tasks = int(aggregate.get("tasks") or payload.get("task_count") or 0)
    passes = int(aggregate.get("passes") or 0)
    accuracy = float(aggregate.get("accuracy") if aggregate.get("accuracy") is not None else (passes / max(tasks, 1)))
    return {
        "variant": variant,
        "task_format": task_format,
        "summary_path": str(summary_path),
        "guard_path": str(guard_path),
        "model": payload.get("model"),
        "tasks": tasks,
        "passes": passes,
        "accuracy": accuracy,
        "mean_tokens_per_second": float(aggregate.get("mean_tokens_per_second") or 0.0),
        "mean_ttft_seconds": float(aggregate.get("mean_ttft_seconds") or 0.0),
        "guard_returncode": guard.get("returncode"),
        "killed_by_guard": bool(guard.get("killed_by_guard")),
        "killed_by_timeout": bool(guard.get("killed_by_timeout")),
        "guard_max_memory_used_ratio": float(guard.get("max_memory_used_ratio") or 0.0),
        "guard_max_memory_used_mib": guard.get("max_memory_used_mib"),
        "guard_memory_total_mib": guard.get("memory_total_mib"),
    }


def _case_key(case: dict[str, Any]) -> tuple[str, str]:
    return str(case["variant"]), str(case["task_format"])


def build_comparisons(cases: list[dict[str, Any]], baseline_variant: str) -> tuple[list[str], list[dict[str, Any]]]:
    failures: list[str] = []
    by_key = {_case_key(case): case for case in cases}
    comparisons: list[dict[str, Any]] = []
    formats = sorted({str(case["task_format"]) for case in cases})
    for task_format in formats:
        baseline = by_key.get((baseline_variant, task_format))
        if baseline is None:
            failures.append(f"missing baseline case {baseline_variant}:{task_format}")
            continue
        for case in cases:
            if case["task_format"] != task_format or case["variant"] == baseline_variant:
                continue
            drop = float(baseline["accuracy"]) - float(case["accuracy"])
            comparisons.append(
                {
                    "variant": case["variant"],
                    "task_format": task_format,
                    "baseline_variant": baseline_variant,
                    "baseline_accuracy": baseline["accuracy"],
                    "accuracy": case["accuracy"],
                    "accuracy_drop_vs_baseline": drop,
                    "baseline_passes": baseline["passes"],
                    "passes": case["passes"],
                    "baseline_tasks": baseline["tasks"],
                    "tasks": case["tasks"],
                }
            )
    return failures, comparisons


def build_result(cases: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    evidence_label = getattr(args, "evidence_label", "tiny public MMLU/GSM8K smoke tasks")
    matrix_title = getattr(args, "matrix_title", "Official PTQ Task-Execution Smoke Matrix")
    variants = sorted({str(case["variant"]) for case in cases})
    formats = sorted({str(case["task_format"]) for case in cases})
    required_variants = list(args.required_variants)
    required_formats = list(args.required_formats)

    for variant in required_variants:
        if variant not in variants:
            failures.append(f"missing required variant {variant}")
    for task_format in required_formats:
        if task_format not in formats:
            failures.append(f"missing required task format {task_format}")
    for variant in required_variants:
        for task_format in required_formats:
            if (variant, task_format) not in {_case_key(case) for case in cases}:
                failures.append(f"missing required case {variant}:{task_format}")

    for case in cases:
        label = f"{case['variant']}:{case['task_format']}"
        if case["tasks"] < args.min_tasks_per_case:
            failures.append(f"{label}: tasks {case['tasks']} < required {args.min_tasks_per_case}")
        if case["guard_returncode"] != 0:
            failures.append(f"{label}: guard returncode {case['guard_returncode']} != 0")
        if case["killed_by_guard"]:
            failures.append(f"{label}: killed by GPU guard")
        if case["killed_by_timeout"]:
            failures.append(f"{label}: killed by timeout")
        if case["guard_max_memory_used_ratio"] > args.max_memory_ratio:
            failures.append(
                f"{label}: VRAM ratio {case['guard_max_memory_used_ratio']:.4f} > {args.max_memory_ratio:.4f}"
            )

    comparison_failures, comparisons = build_comparisons(cases, str(args.baseline_variant))
    failures.extend(comparison_failures)
    for comparison in comparisons:
        if comparison["accuracy_drop_vs_baseline"] > args.max_accuracy_drop:
            failures.append(
                f"{comparison['variant']}:{comparison['task_format']} accuracy drop "
                f"{comparison['accuracy_drop_vs_baseline']:.4f} > {args.max_accuracy_drop:.4f}"
            )

    max_drop = max((float(row["accuracy_drop_vs_baseline"]) for row in comparisons), default=0.0)
    baseline_zero_accuracy_formats = sorted(
        {
            str(case["task_format"])
            for case in cases
            if case["variant"] == args.baseline_variant and float(case["accuracy"]) <= 0.0
        }
    )
    summary = {
        "case_count": len(cases),
        "variant_count": len(variants),
        "format_count": len(formats),
        "variants": variants,
        "task_formats": formats,
        "baseline_variant": args.baseline_variant,
        "total_tasks": sum(int(case["tasks"]) for case in cases),
        "total_passes": sum(int(case["passes"]) for case in cases),
        "mean_accuracy": mean([float(case["accuracy"]) for case in cases]) if cases else 0.0,
        "max_accuracy_drop_vs_fp16": max_drop,
        "baseline_zero_accuracy_formats": baseline_zero_accuracy_formats,
        "max_guard_vram_ratio": max((float(case["guard_max_memory_used_ratio"]) for case in cases), default=0.0),
        "mean_tokens_per_second": mean([float(case["mean_tokens_per_second"]) for case in cases]) if cases else 0.0,
        "mean_ttft_seconds": mean([float(case["mean_ttft_seconds"]) for case in cases]) if cases else 0.0,
    }
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "matrix_title": matrix_title,
        "evidence_label": evidence_label,
        "summary": summary,
        "cases": cases,
        "comparisons": comparisons,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated "
            f"on the same {evidence_label} under GPU guard. Formats with zero FP16 "
            "accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task "
            "retention, SOTA PTQ quality, or a production inference benchmark."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        f"# {result.get('matrix_title', 'Official PTQ Task-Execution Smoke Matrix')}",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- variants: `{summary['variants']}`",
        f"- task formats: `{summary['task_formats']}`",
        f"- total tasks across cases: `{summary['total_tasks']}`",
        f"- total passes across cases: `{summary['total_passes']}`",
        f"- max accuracy drop vs `{summary['baseline_variant']}`: `{summary['max_accuracy_drop_vs_fp16']:.4f}`",
        f"- zero-accuracy baseline formats: `{summary['baseline_zero_accuracy_formats']}`",
        f"- peak guard VRAM ratio: `{summary['max_guard_vram_ratio']:.4f}`",
        "",
        "## Cases",
        "",
        "| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for case in result["cases"]:
        source = str(case["summary_path"]).replace("\\", "/")
        lines.append(
            f"| `{case['variant']}` | `{case['task_format']}` | {case['tasks']} | {case['passes']} | "
            f"{case['accuracy']:.4f} | {case['mean_tokens_per_second']:.4f} | "
            f"{case['mean_ttft_seconds']:.6f} | {case['guard_max_memory_used_ratio']:.4f} | `{source}` |"
        )
    lines.extend(["", "## Comparisons Against Baseline", ""])
    lines.extend(
        [
            "| variant | format | baseline accuracy | quant accuracy | drop |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for row in result["comparisons"]:
        lines.append(
            f"| `{row['variant']}` | `{row['task_format']}` | {row['baseline_accuracy']:.4f} | "
            f"{row['accuracy']:.4f} | {row['accuracy_drop_vs_baseline']:.4f} |"
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
    parser = argparse.ArgumentParser(description="Gate official PTQ tiny task-execution smokes.")
    parser.add_argument("--case", action="append", required=True, help="VARIANT:FORMAT=SUMMARY_JSON=GUARD_JSON")
    parser.add_argument("--baseline-variant", default="fp16")
    parser.add_argument("--required-variant", dest="required_variants", action="append", default=[])
    parser.add_argument("--required-format", dest="required_formats", action="append", default=[])
    parser.add_argument("--min-tasks-per-case", type=int, default=4)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--max-accuracy-drop", type=float, default=0.25)
    parser.add_argument("--matrix-title", default="Official PTQ Task-Execution Smoke Matrix")
    parser.add_argument("--evidence-label", default="tiny public MMLU/GSM8K smoke tasks")
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()
    if not args.required_variants:
        args.required_variants = ["fp16", "autoawq", "gptqmodel"]
    if not args.required_formats:
        args.required_formats = ["mmlu", "gsm8k"]

    cases = [case_summary(*parse_case_spec(spec)) for spec in args.case]
    result = build_result(cases, args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "failures": result["failures"]}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
