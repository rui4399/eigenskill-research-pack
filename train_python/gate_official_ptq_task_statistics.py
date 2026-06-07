#!/usr/bin/env python3
from __future__ import annotations

"""Gate statistical intervals for matched official-PTQ task matrices.

This gate consumes already-generated task-evaluation summaries. It does not
rerun inference. Its purpose is to make the uncertainty around local task slices
explicit: per-case Wilson accuracy intervals, paired bootstrap deltas against an
FP16 baseline, and discordant-pair counts. Passing this gate is a statistics
reporting check, not a leaderboard, superiority, or production-runtime claim.
"""

import argparse
import json
import math
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_case_spec(spec: str) -> tuple[str, str, Path]:
    parts = spec.split("=", 1)
    if len(parts) != 2 or not all(part.strip() for part in parts):
        raise ValueError(f"case must be VARIANT:FORMAT=SUMMARY_JSON: {spec}")
    label, summary_path = parts
    if ":" not in label:
        raise ValueError(f"case label must be VARIANT:FORMAT: {spec}")
    variant, task_format = [part.strip() for part in label.split(":", 1)]
    if not variant or not task_format:
        raise ValueError(f"variant and format cannot be empty: {spec}")
    return variant, task_format, Path(summary_path)


def aggregate(payload: dict[str, Any]) -> dict[str, Any]:
    baseline = payload.get("baseline", {}) if isinstance(payload.get("baseline"), dict) else {}
    return baseline.get("aggregate", {}) if isinstance(baseline.get("aggregate"), dict) else {}


def rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    baseline = payload.get("baseline", {}) if isinstance(payload.get("baseline"), dict) else {}
    raw_rows = baseline.get("rows", [])
    return [row for row in raw_rows if isinstance(row, dict)]


def row_passed(row: dict[str, Any]) -> bool:
    score = row.get("score", {})
    return bool(score.get("passed")) if isinstance(score, dict) else False


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def percentile(sorted_values: list[float], q: float) -> float | None:
    if not sorted_values:
        return None
    if len(sorted_values) == 1:
        return sorted_values[0]
    position = (len(sorted_values) - 1) * q
    lo = int(position)
    hi = min(lo + 1, len(sorted_values) - 1)
    weight = position - lo
    return sorted_values[lo] * (1.0 - weight) + sorted_values[hi] * weight


def wilson_interval(passes: int, total: int, z: float = 1.959963984540054) -> dict[str, float | int | None]:
    if total <= 0:
        return {"passes": passes, "total": total, "mean": None, "low": None, "high": None}
    phat = passes / total
    denom = 1.0 + (z * z) / total
    center = (phat + (z * z) / (2.0 * total)) / denom
    radius = (z / denom) * math.sqrt((phat * (1.0 - phat) / total) + ((z * z) / (4.0 * total * total)))
    return {
        "passes": passes,
        "total": total,
        "mean": phat,
        "low": max(0.0, center - radius),
        "high": min(1.0, center + radius),
    }


def bootstrap_paired_delta(
    baseline: list[bool],
    candidate: list[bool],
    *,
    samples: int,
    seed: int,
) -> dict[str, float | int | None]:
    if len(baseline) != len(candidate) or not baseline or samples <= 0:
        return {"samples": 0, "mean": None, "low": None, "high": None, "probability_nonnegative": None}
    deltas = [(1.0 if c else 0.0) - (1.0 if b else 0.0) for b, c in zip(baseline, candidate)]
    rng = random.Random(seed)
    draws: list[float] = []
    for _ in range(samples):
        draws.append(mean([deltas[rng.randrange(len(deltas))] for _ in deltas]))
    draws.sort()
    return {
        "samples": samples,
        "mean": mean(draws),
        "low": percentile(draws, 0.025),
        "high": percentile(draws, 0.975),
        "probability_nonnegative": sum(1 for value in draws if value >= 0.0) / len(draws),
    }


def case_summary(variant: str, task_format: str, summary_path: Path) -> dict[str, Any]:
    payload = load_json(summary_path)
    agg = aggregate(payload)
    case_rows = rows(payload)
    tasks = int(agg.get("tasks") or payload.get("task_count") or len(case_rows))
    passes = int(agg.get("passes") or sum(1 for row in case_rows if row_passed(row)))
    return {
        "variant": variant,
        "task_format": task_format,
        "summary_path": str(summary_path),
        "model": payload.get("model"),
        "loader": payload.get("loader"),
        "hf_device_map": payload.get("hf_device_map", ""),
        "task_count": tasks,
        "row_count": len(case_rows),
        "passes": passes,
        "accuracy": passes / max(tasks, 1),
        "wilson_accuracy_ci_95": wilson_interval(passes, tasks),
    }


def _case_key(case: dict[str, Any]) -> tuple[str, str]:
    return str(case["variant"]), str(case["task_format"])


def rows_by_id(summary_path: str) -> dict[str, bool]:
    payload = load_json(Path(summary_path))
    out: dict[str, bool] = {}
    for index, row in enumerate(rows(payload)):
        row_id = str(row.get("id") if row.get("id") is not None else index)
        out[row_id] = row_passed(row)
    return out


def build_comparisons(
    cases: list[dict[str, Any]],
    *,
    baseline_variant: str,
    bootstrap_samples: int,
    bootstrap_seed: int,
) -> tuple[list[str], list[dict[str, Any]]]:
    failures: list[str] = []
    by_key = {_case_key(case): case for case in cases}
    comparisons: list[dict[str, Any]] = []
    formats = sorted({str(case["task_format"]) for case in cases})
    for task_format in formats:
        baseline = by_key.get((baseline_variant, task_format))
        if baseline is None:
            failures.append(f"missing baseline case {baseline_variant}:{task_format}")
            continue
        baseline_rows = rows_by_id(str(baseline["summary_path"]))
        for candidate in cases:
            if candidate["task_format"] != task_format or candidate["variant"] == baseline_variant:
                continue
            candidate_rows = rows_by_id(str(candidate["summary_path"]))
            shared_ids = sorted(set(baseline_rows).intersection(candidate_rows))
            base_values = [baseline_rows[row_id] for row_id in shared_ids]
            candidate_values = [candidate_rows[row_id] for row_id in shared_ids]
            baseline_only = sum(1 for b, c in zip(base_values, candidate_values) if b and not c)
            candidate_only = sum(1 for b, c in zip(base_values, candidate_values) if c and not b)
            both_correct = sum(1 for b, c in zip(base_values, candidate_values) if b and c)
            both_wrong = sum(1 for b, c in zip(base_values, candidate_values) if not b and not c)
            delta = (sum(candidate_values) / max(len(candidate_values), 1)) - (
                sum(base_values) / max(len(base_values), 1)
            )
            comparisons.append(
                {
                    "variant": candidate["variant"],
                    "task_format": task_format,
                    "baseline_variant": baseline_variant,
                    "shared_tasks": len(shared_ids),
                    "baseline_accuracy": baseline["accuracy"],
                    "candidate_accuracy": candidate["accuracy"],
                    "accuracy_delta_candidate_minus_baseline": delta,
                    "accuracy_drop_baseline_minus_candidate": -delta,
                    "paired_bootstrap_delta_ci_95": bootstrap_paired_delta(
                        base_values,
                        candidate_values,
                        samples=bootstrap_samples,
                        seed=bootstrap_seed + len(comparisons) * 997,
                    ),
                    "discordant_pairs": {
                        "baseline_only_correct": baseline_only,
                        "candidate_only_correct": candidate_only,
                        "both_correct": both_correct,
                        "both_wrong": both_wrong,
                    },
                }
            )
    return failures, comparisons


def build_result(cases: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    variants = sorted({str(case["variant"]) for case in cases})
    formats = sorted({str(case["task_format"]) for case in cases})
    for case in cases:
        label = f"{case['variant']}:{case['task_format']}"
        if int(case["task_count"]) < args.min_tasks_per_case:
            failures.append(f"{label}: tasks {case['task_count']} < required {args.min_tasks_per_case}")
        if int(case["row_count"]) != int(case["task_count"]):
            failures.append(f"{label}: row count {case['row_count']} != task count {case['task_count']}")

    comparison_failures, comparisons = build_comparisons(
        cases,
        baseline_variant=args.baseline_variant,
        bootstrap_samples=args.bootstrap_samples,
        bootstrap_seed=args.bootstrap_seed,
    )
    failures.extend(comparison_failures)
    for row in comparisons:
        label = f"{row['variant']}:{row['task_format']}"
        if int(row["shared_tasks"]) < args.min_shared_tasks:
            failures.append(f"{label}: shared tasks {row['shared_tasks']} < required {args.min_shared_tasks}")
        ci = row["paired_bootstrap_delta_ci_95"]
        low = ci.get("low") if isinstance(ci, dict) else None
        if low is not None and float(low) < -float(args.max_ci_accuracy_drop):
            failures.append(
                f"{label}: paired bootstrap low delta {float(low):.4f} < -{args.max_ci_accuracy_drop:.4f}"
            )

    min_paired_delta_low = min(
        (
            float(row["paired_bootstrap_delta_ci_95"]["low"])
            for row in comparisons
            if row["paired_bootstrap_delta_ci_95"].get("low") is not None
        ),
        default=0.0,
    )
    summary = {
        "case_count": len(cases),
        "variant_count": len(variants),
        "format_count": len(formats),
        "variants": variants,
        "task_formats": formats,
        "baseline_variant": args.baseline_variant,
        "total_tasks": sum(int(case["task_count"]) for case in cases),
        "total_passes": sum(int(case["passes"]) for case in cases),
        "comparison_count": len(comparisons),
        "min_paired_bootstrap_delta_low": min_paired_delta_low,
        "bootstrap_samples": args.bootstrap_samples,
    }
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "matrix_title": args.matrix_title,
        "summary": summary,
        "cases": cases,
        "comparisons": comparisons,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: this gate reports statistical uncertainty for an already-guarded local "
            "official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap "
            "candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does "
            "not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, "
            "production speedup, mobile deployment, or energy savings."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        f"# {result.get('matrix_title', 'Official PTQ Task Statistics Gate')}",
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
        f"- bootstrap samples: `{summary['bootstrap_samples']}`",
        f"- minimum paired bootstrap delta lower bound: `{summary['min_paired_bootstrap_delta_low']:.4f}`",
        "",
        "## Case Accuracy Intervals",
        "",
        "| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for case in result["cases"]:
        ci = case["wilson_accuracy_ci_95"]
        source = str(case["summary_path"]).replace("\\", "/")
        lines.append(
            f"| `{case['variant']}` | `{case['task_format']}` | {case['task_count']} | {case['passes']} | "
            f"{case['accuracy']:.4f} | {float(ci['low']):.4f} | {float(ci['high']):.4f} | `{source}` |"
        )
    lines.extend(["", "## Paired Comparisons", ""])
    lines.extend(
        [
            "| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in result["comparisons"]:
        ci = row["paired_bootstrap_delta_ci_95"]
        discord = row["discordant_pairs"]
        lines.append(
            f"| `{row['variant']}` | `{row['task_format']}` | {row['shared_tasks']} | "
            f"{row['accuracy_delta_candidate_minus_baseline']:.4f} | {float(ci['low']):.4f} | "
            f"{float(ci['high']):.4f} | {float(ci['probability_nonnegative']):.4f} | "
            f"{discord['baseline_only_correct']} | {discord['candidate_only_correct']} |"
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
    parser = argparse.ArgumentParser(description="Gate statistical intervals for official PTQ task matrices.")
    parser.add_argument("--case", action="append", required=True, help="VARIANT:FORMAT=SUMMARY_JSON")
    parser.add_argument("--baseline-variant", default="fp16")
    parser.add_argument("--min-tasks-per-case", type=int, default=100)
    parser.add_argument("--min-shared-tasks", type=int, default=100)
    parser.add_argument("--max-ci-accuracy-drop", type=float, default=0.15)
    parser.add_argument("--bootstrap-samples", type=int, default=5000)
    parser.add_argument("--bootstrap-seed", type=int, default=20260608)
    parser.add_argument("--matrix-title", default="Official PTQ Task Statistics Gate")
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    case_specs = [parse_case_spec(raw) for raw in args.case]
    result = build_result([case_summary(*spec) for spec in case_specs], args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "failures": result["failures"]}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
