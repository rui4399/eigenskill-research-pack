#!/usr/bin/env python3
from __future__ import annotations

"""Gate bootstrap evidence that CSI stability improves from small to larger n.

This gate consumes calibration-seed-stability artifacts.  It does not rerun
model inference; it audits whether the observed n=2/4/8 stability curve is
large enough to survive a simple nonparametric trend check.
"""

import argparse
import json
import random
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class TrendCase:
    n: int
    path: Path


METRICS: tuple[tuple[str, str], ...] = (
    ("score_spearman", "score/cost Spearman"),
    ("top20_jaccard", "top-20 Jaccard"),
    ("positive_jaccard", "positive-set Jaccard"),
)


def parse_case(raw: str) -> TrendCase:
    if "=" not in raw:
        raise ValueError(f"case must be N=JSON: {raw}")
    left, right = [part.strip() for part in raw.split("=", 1)]
    if not left or not right:
        raise ValueError(f"empty N/path in case spec: {raw}")
    try:
        n = int(left)
    except ValueError as exc:
        raise ValueError(f"N must be an integer calibration size: {raw}") from exc
    if n <= 0:
        raise ValueError(f"N must be positive: {raw}")
    return TrendCase(n=n, path=Path(right))


def finite(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def mean(values: list[float]) -> float | None:
    clean = [value for value in values if finite(value) is not None]
    if not clean:
        return None
    return sum(clean) / len(clean)


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


def bootstrap_mean_gain_ci(
    left: list[float],
    right: list[float],
    *,
    samples: int,
    seed: int,
) -> dict[str, float | int | None]:
    if not left or not right or samples <= 0:
        return {"samples": 0, "mean": None, "low": None, "high": None, "probability_positive": None}
    rng = random.Random(seed)
    gains: list[float] = []
    for _ in range(samples):
        left_draw = [left[rng.randrange(len(left))] for _ in left]
        right_draw = [right[rng.randrange(len(right))] for _ in right]
        gains.append((sum(right_draw) / len(right_draw)) - (sum(left_draw) / len(left_draw)))
    gains.sort()
    return {
        "samples": samples,
        "mean": sum(gains) / len(gains),
        "low": percentile(gains, 0.025),
        "high": percentile(gains, 0.975),
        "probability_positive": sum(1 for gain in gains if gain > 0.0) / len(gains),
    }


def dominance_probability(left: list[float], right: list[float]) -> float | None:
    if not left or not right:
        return None
    wins = 0.0
    total = 0
    for left_value in left:
        for right_value in right:
            total += 1
            if right_value > left_value:
                wins += 1.0
            elif right_value == left_value:
                wins += 0.5
    return wins / total if total else None


def load_case(case: TrendCase) -> dict[str, Any]:
    payload = json.loads(case.path.read_text(encoding="utf-8"))
    pairs = payload.get("pairs", []) or []
    metrics: dict[str, list[float]] = {}
    for key, _ in METRICS:
        metrics[key] = [value for row in pairs if (value := finite(row.get(key))) is not None]
    return {
        "n": case.n,
        "path": str(case.path),
        "source_passed": bool(payload.get("passed")),
        "pair_count": len(pairs),
        "metrics": metrics,
    }


def analyze_step(
    left: dict[str, Any],
    right: dict[str, Any],
    *,
    bootstrap_samples: int,
    seed: int,
) -> dict[str, Any]:
    metrics = []
    for index, (key, label) in enumerate(METRICS):
        left_values = left["metrics"].get(key, [])
        right_values = right["metrics"].get(key, [])
        left_mean = mean(left_values)
        right_mean = mean(right_values)
        gain = None if left_mean is None or right_mean is None else right_mean - left_mean
        ci = bootstrap_mean_gain_ci(
            left_values,
            right_values,
            samples=bootstrap_samples,
            seed=seed + index * 997,
        )
        metrics.append(
            {
                "metric": key,
                "label": label,
                "left_mean": left_mean,
                "right_mean": right_mean,
                "mean_gain": gain,
                "bootstrap_gain_ci": ci,
                "dominance_probability": dominance_probability(left_values, right_values),
            }
        )
    return {
        "left_n": left["n"],
        "right_n": right["n"],
        "left_path": left["path"],
        "right_path": right["path"],
        "metrics": metrics,
    }


def build_gate(
    cases: list[TrendCase],
    *,
    min_points: int = 3,
    bootstrap_samples: int = 5000,
    bootstrap_seed: int = 20260607,
    min_full_range_gain_low: float = 0.0,
    min_full_range_dominance_probability: float = 0.90,
) -> dict[str, Any]:
    if len(cases) != len({case.n for case in cases}):
        raise ValueError("calibration sizes must be unique")
    points = sorted((load_case(case) for case in cases), key=lambda row: row["n"])

    failures: list[str] = []
    if len(points) < min_points:
        failures.append(f"trend point count below threshold: {len(points)} < {min_points}")
    failed_sources = [point["n"] for point in points if not point["source_passed"]]
    if failed_sources:
        failures.append(f"source seed-stability gates failed: {failed_sources}")

    adjacent_steps = [
        analyze_step(left, right, bootstrap_samples=bootstrap_samples, seed=bootstrap_seed + offset * 10000)
        for offset, (left, right) in enumerate(zip(points, points[1:]))
    ]
    full_range = (
        analyze_step(points[0], points[-1], bootstrap_samples=bootstrap_samples, seed=bootstrap_seed + 50000)
        if len(points) >= 2
        else None
    )

    full_metric_rows = full_range["metrics"] if full_range else []
    gain_lows = [
        value
        for row in full_metric_rows
        if (value := finite((row.get("bootstrap_gain_ci") or {}).get("low"))) is not None
    ]
    dominance = [
        value
        for row in full_metric_rows
        if (value := finite(row.get("dominance_probability"))) is not None
    ]
    min_gain_low = min(gain_lows) if gain_lows else None
    min_dominance = min(dominance) if dominance else None
    all_gain_ci_positive = bool(gain_lows) and all(value > min_full_range_gain_low for value in gain_lows)
    all_dominance_high = bool(dominance) and all(
        value >= min_full_range_dominance_probability for value in dominance
    )

    if not all_gain_ci_positive:
        failures.append(
            f"full-range bootstrap gain lower bound does not clear {min_full_range_gain_low}: {min_gain_low}"
        )
    if not all_dominance_high:
        failures.append(
            "full-range dominance probability below threshold "
            f"{min_full_range_dominance_probability}: {min_dominance}"
        )

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "point_count": len(points),
            "min_n": points[0]["n"] if points else None,
            "max_n": points[-1]["n"] if points else None,
            "bootstrap_samples": bootstrap_samples,
            "min_full_range_gain_low": min_gain_low,
            "min_full_range_dominance_probability": min_dominance,
            "all_full_range_gain_ci_positive": all_gain_ci_positive,
            "all_full_range_dominance_high": all_dominance_high,
        },
        "points": [
            {
                "n": point["n"],
                "path": point["path"],
                "source_passed": point["source_passed"],
                "pair_count": point["pair_count"],
                "metric_means": {key: mean(values) for key, values in point["metrics"].items()},
            }
            for point in points
        ],
        "adjacent_steps": adjacent_steps,
        "full_range": full_range,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: for Qwen2.5-0.5B-Instruct under the fixed public prompt pool, "
            "the n=8 seed-pair stability distribution dominates n=2 for the audited CSI "
            "metrics, and independent bootstrap confidence intervals for mean gain are "
            "positive. Invalid claim: this proves a universal scaling law, downstream "
            "quality retention, SOTA quantization, or deployment speed."
        ),
    }


def fmt(value: Any, digits: int = 4) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}f}"


def fmt_ci(ci: Any, digits: int = 4) -> str:
    if not isinstance(ci, dict):
        return "n/a"
    low = finite(ci.get("low"))
    high = finite(ci.get("high"))
    if low is None or high is None:
        return "n/a"
    return f"[{low:.{digits}f}, {high:.{digits}f}]"


def write_step_table(lines: list[str], step: dict[str, Any]) -> None:
    lines.extend(
        [
            f"### n={step['left_n']} -> n={step['right_n']}",
            "",
            "| metric | left mean | right mean | mean gain | bootstrap 95% gain CI | P(right pair > left pair) | P(bootstrap gain > 0) |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in step["metrics"]:
        ci = row.get("bootstrap_gain_ci") or {}
        lines.append(
            f"| {row['label']} | {fmt(row['left_mean'])} | {fmt(row['right_mean'])} | "
            f"{fmt(row['mean_gain'])} | {fmt_ci(ci)} | {fmt(row['dominance_probability'])} | "
            f"{fmt(ci.get('probability_positive'))} |"
        )
    lines.append("")


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    lines = [
        "# CSI Trend Significance Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- points: `{summary['point_count']}`",
        f"- n range: `{summary['min_n']} -> {summary['max_n']}`",
        f"- bootstrap samples: `{summary['bootstrap_samples']}`",
        f"- minimum full-range gain lower CI bound: `{fmt(summary['min_full_range_gain_low'])}`",
        f"- minimum full-range dominance probability: `{fmt(summary['min_full_range_dominance_probability'])}`",
        f"- all full-range gain CIs positive: `{summary['all_full_range_gain_ci_positive']}`",
        f"- all full-range dominance probabilities high: `{summary['all_full_range_dominance_high']}`",
        "",
        "## Full-Range Trend",
        "",
    ]
    if report["full_range"]:
        write_step_table(lines, report["full_range"])
    lines.extend(["## Adjacent Steps", ""])
    for step in report["adjacent_steps"]:
        write_step_table(lines, step)
    lines.extend(["## Claim Boundary", "", report["claim_boundary"], "", "## Failures", ""])
    if report["failures"]:
        lines.extend(f"- {failure}" for failure in report["failures"])
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate CSI trend significance across calibration sizes.")
    parser.add_argument("--case", action="append", required=True, help="N=seed_stability_json")
    parser.add_argument("--min-points", type=int, default=3)
    parser.add_argument("--bootstrap-samples", type=int, default=5000)
    parser.add_argument("--bootstrap-seed", type=int, default=20260607)
    parser.add_argument("--min-full-range-gain-low", type=float, default=0.0)
    parser.add_argument("--min-full-range-dominance-probability", type=float, default=0.90)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    report = build_gate(
        [parse_case(raw) for raw in args.case],
        min_points=args.min_points,
        bootstrap_samples=args.bootstrap_samples,
        bootstrap_seed=args.bootstrap_seed,
        min_full_range_gain_low=args.min_full_range_gain_low,
        min_full_range_dominance_probability=args.min_full_range_dominance_probability,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
