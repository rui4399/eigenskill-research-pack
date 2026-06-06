#!/usr/bin/env python3
from __future__ import annotations

"""Gate a small multi-model public-task evidence ladder.

This combines already-gated public MMLU/GSM8K subset runs. It is meant to
prevent a single public-task result from being presented without its weaker
local sibling, not to claim scale-law monotonicity or leaderboard quality.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_case_spec(spec: str) -> tuple[str, Path]:
    parts = spec.split("=", 1)
    if len(parts) != 2 or not all(part.strip() for part in parts):
        raise ValueError(f"case must be LABEL=GATE_JSON: {spec}")
    return parts[0].strip(), Path(parts[1])


def _formats(value: str) -> set[str]:
    return {item.strip() for item in value.split(",") if item.strip()}


def _first_model_name(payload: dict[str, Any]) -> str:
    for case in payload.get("cases", []) or []:
        model = case.get("model")
        if model:
            return str(model)
    return "unknown"


def case_summary(label: str, path: Path) -> dict[str, Any]:
    payload = load_json(path)
    summary = payload.get("summary", {}) or {}
    task_count = int(summary.get("total_tasks") or 0)
    passes = int(summary.get("total_passes") or 0)
    formats = sorted(str(item) for item in (summary.get("task_formats") or []) if item)
    return {
        "label": label,
        "path": str(path),
        "source_passed": bool(payload.get("passed")),
        "model": _first_model_name(payload),
        "task_count": task_count,
        "passes": passes,
        "accuracy": (passes / task_count) if task_count else 0.0,
        "task_formats": formats,
        "max_guard_vram_ratio": float(summary.get("max_guard_vram_ratio") or 0.0),
        "mean_tokens_per_second": float(summary.get("mean_tokens_per_second") or 0.0),
        "mean_ttft_seconds": float(summary.get("mean_ttft_seconds") or 0.0),
    }


def build_result(cases: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    required_formats = _formats(args.require_formats)
    distinct_models = {case["model"] for case in cases if case["model"] != "unknown"}

    if len(cases) < args.min_models:
        failures.append(f"model cases {len(cases)} < required {args.min_models}")
    if args.require_distinct_model_names and len(distinct_models) < min(args.min_models, len(cases)):
        failures.append(f"distinct model names {len(distinct_models)} < required {min(args.min_models, len(cases))}")

    for case in cases:
        formats = set(case["task_formats"])
        missing_formats = sorted(required_formats.difference(formats))
        if not case["source_passed"]:
            failures.append(f"{case['label']}: source public-task gate did not pass")
        if case["task_count"] < args.min_tasks_per_model:
            failures.append(f"{case['label']}: tasks {case['task_count']} < required {args.min_tasks_per_model}")
        if missing_formats:
            failures.append(f"{case['label']}: missing required task formats: {missing_formats}")
        if case["max_guard_vram_ratio"] > args.max_memory_ratio:
            failures.append(
                f"{case['label']}: max VRAM ratio {case['max_guard_vram_ratio']:.4f} > {args.max_memory_ratio:.4f}"
            )

    best = max(cases, key=lambda item: (item["passes"], item["accuracy"]), default=None)
    worst = min(cases, key=lambda item: (item["passes"], item["accuracy"]), default=None)
    if best is None:
        failures.append("no model cases supplied")
        best_passes = 0
        best_accuracy = 0.0
    else:
        best_passes = int(best["passes"])
        best_accuracy = float(best["accuracy"])
        if best_passes < args.min_best_total_passes:
            failures.append(f"best model passes {best_passes} < required {args.min_best_total_passes}")
        if best_accuracy < args.min_best_accuracy:
            failures.append(f"best model accuracy {best_accuracy:.4f} < required {args.min_best_accuracy:.4f}")

    summary = {
        "model_count": len(cases),
        "distinct_model_count": len(distinct_models),
        "total_tasks": sum(case["task_count"] for case in cases),
        "total_passes": sum(case["passes"] for case in cases),
        "mean_accuracy": mean([case["accuracy"] for case in cases]) if cases else 0.0,
        "best_label": best["label"] if best else None,
        "best_model": best["model"] if best else None,
        "best_total_passes": best_passes,
        "best_accuracy": best_accuracy,
        "worst_label": worst["label"] if worst else None,
        "worst_model": worst["model"] if worst else None,
        "worst_accuracy": float(worst["accuracy"]) if worst else 0.0,
        "best_minus_worst_passes": (int(best["passes"]) - int(worst["passes"])) if best and worst else 0,
        "best_minus_worst_accuracy": (float(best["accuracy"]) - float(worst["accuracy"])) if best and worst else 0.0,
        "max_guard_vram_ratio": max((case["max_guard_vram_ratio"] for case in cases), default=0.0),
        "mean_tokens_per_second": mean([case["mean_tokens_per_second"] for case in cases]) if cases else 0.0,
        "mean_ttft_seconds": mean([case["mean_ttft_seconds"] for case in cases]) if cases else 0.0,
    }

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": summary,
        "cases": cases,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: public-task evidence is reported as a guarded multi-model ladder. "
            "Invalid claim: this proves monotonic scaling, fused quantized retention, SOTA quality, or leaderboard performance."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        "# Public Task Model Ladder Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        f"Models: `{summary['model_count']}`",
        f"Total tasks: `{summary['total_tasks']}`",
        f"Total passes: `{summary['total_passes']}`",
        f"Best model: `{summary['best_label']}` / `{summary['best_model']}`",
        f"Best passes: `{summary['best_total_passes']}`",
        f"Best accuracy: `{summary['best_accuracy']:.4f}`",
        f"Peak guard VRAM ratio: `{summary['max_guard_vram_ratio']:.4f}`",
        "",
        "## Model Cases",
        "",
        "| label | model | formats | tasks | passes | accuracy | mean tok/s | mean TTFT s | VRAM ratio | source |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for case in result["cases"]:
        source = str(case["path"]).replace("\\", "/")
        formats = ",".join(case["task_formats"])
        lines.append(
            f"| `{case['label']}` | `{case['model']}` | `{formats}` | {case['task_count']} | {case['passes']} | "
            f"{case['accuracy']:.4f} | {case['mean_tokens_per_second']:.4f} | "
            f"{case['mean_ttft_seconds']:.6f} | {case['max_guard_vram_ratio']:.4f} | `{source}` |"
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
    parser = argparse.ArgumentParser(description="Gate a multi-model public-task evidence ladder.")
    parser.add_argument("--case", action="append", required=True, help="LABEL=PUBLIC_TASK_GATE_JSON")
    parser.add_argument("--min-models", type=int, default=2)
    parser.add_argument("--min-tasks-per-model", type=int, default=100)
    parser.add_argument("--require-formats", default="mmlu,gsm8k")
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--min-best-total-passes", type=int, default=30)
    parser.add_argument("--min-best-accuracy", type=float, default=0.30)
    parser.add_argument("--require-distinct-model-names", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    cases = [case_summary(label, path) for label, path in map(parse_case_spec, args.case)]
    result = build_result(cases, args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "out_json": str(args.out_json)}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
