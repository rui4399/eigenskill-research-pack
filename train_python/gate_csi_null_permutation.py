#!/usr/bin/env python3
from __future__ import annotations

"""Gate a permutation-null test for CSI stability gains.

The trend-significance gate checks bootstrap confidence intervals.  This gate
adds a complementary label-shuffle null: if calibration size did not matter,
then swapping the n labels across seed-pair metric values should often produce
an n=8-minus-n=2 gain as large as the observed one.
"""

import argparse
import json
import random
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class NullCase:
    n: int
    path: Path


METRICS: tuple[tuple[str, str], ...] = (
    ("score_spearman", "score/cost Spearman"),
    ("top20_jaccard", "top-20 Jaccard"),
    ("positive_jaccard", "positive-set Jaccard"),
)


def parse_case(raw: str) -> NullCase:
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
    return NullCase(n=n, path=Path(right))


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


def permutation_p_value(
    left: list[float],
    right: list[float],
    *,
    samples: int,
    seed: int,
) -> dict[str, float | int | None]:
    left_mean = mean(left)
    right_mean = mean(right)
    if left_mean is None or right_mean is None or not left or not right or samples <= 0:
        return {
            "samples": 0,
            "observed_gain": None,
            "extreme_count": None,
            "p_value": None,
        }

    observed_gain = right_mean - left_mean
    pooled = left + right
    left_count = len(left)
    rng = random.Random(seed)
    extreme_count = 0
    for _ in range(samples):
        shuffled = pooled[:]
        rng.shuffle(shuffled)
        null_left = shuffled[:left_count]
        null_right = shuffled[left_count:]
        null_gain = (sum(null_right) / len(null_right)) - (sum(null_left) / len(null_left))
        if null_gain >= observed_gain - 1.0e-12:
            extreme_count += 1
    return {
        "samples": samples,
        "observed_gain": observed_gain,
        "extreme_count": extreme_count,
        "p_value": (extreme_count + 1) / (samples + 1),
    }


def holm_adjust(p_values: list[float | None]) -> list[float | None]:
    indexed = [(index, float(value)) for index, value in enumerate(p_values) if finite(value) is not None]
    if not indexed:
        return [None for _ in p_values]
    indexed.sort(key=lambda item: item[1])
    adjusted = [None for _ in p_values]
    running = 0.0
    m = len(indexed)
    for rank, (index, p_value) in enumerate(indexed):
        candidate = min(1.0, (m - rank) * p_value)
        running = max(running, candidate)
        adjusted[index] = running
    return adjusted


def load_case(case: NullCase) -> dict[str, Any]:
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


def build_gate(
    cases: list[NullCase],
    *,
    permutation_samples: int = 20000,
    permutation_seed: int = 20260607,
    max_holm_p_value: float = 0.01,
    min_observed_gain: float = 0.0,
) -> dict[str, Any]:
    if len(cases) != len({case.n for case in cases}):
        raise ValueError("calibration sizes must be unique")
    if len(cases) < 2:
        raise ValueError("at least two calibration sizes are required")

    points = sorted((load_case(case) for case in cases), key=lambda row: row["n"])
    left = points[0]
    right = points[-1]
    failures: list[str] = []
    failed_sources = [point["n"] for point in points if not point["source_passed"]]
    if failed_sources:
        failures.append(f"source seed-stability gates failed: {failed_sources}")

    rows: list[dict[str, Any]] = []
    raw_p_values: list[float | None] = []
    for offset, (key, label) in enumerate(METRICS):
        left_values = left["metrics"].get(key, [])
        right_values = right["metrics"].get(key, [])
        result = permutation_p_value(
            left_values,
            right_values,
            samples=permutation_samples,
            seed=permutation_seed + offset * 997,
        )
        left_mean = mean(left_values)
        right_mean = mean(right_values)
        observed_gain = result.get("observed_gain")
        raw_p_values.append(finite(result.get("p_value")))
        rows.append(
            {
                "metric": key,
                "label": label,
                "left_n": left["n"],
                "right_n": right["n"],
                "left_mean": left_mean,
                "right_mean": right_mean,
                "observed_gain": observed_gain,
                "dominance_probability": dominance_probability(left_values, right_values),
                "permutation": result,
            }
        )

    adjusted = holm_adjust(raw_p_values)
    for row, adjusted_p in zip(rows, adjusted):
        row["holm_adjusted_p_value"] = adjusted_p

    gains = [value for row in rows if (value := finite(row.get("observed_gain"))) is not None]
    adjusted_values = [value for value in adjusted if value is not None]
    max_adjusted = max(adjusted_values) if adjusted_values else None
    min_gain = min(gains) if gains else None
    all_positive = bool(gains) and all(value > min_observed_gain for value in gains)
    all_significant = bool(adjusted_values) and all(value <= max_holm_p_value for value in adjusted_values)

    if not all_positive:
        failures.append(f"observed full-range gains do not clear {min_observed_gain}: {min_gain}")
    if not all_significant:
        failures.append(f"Holm-adjusted p-values exceed {max_holm_p_value}: {max_adjusted}")

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "min_n": left["n"],
            "max_n": right["n"],
            "point_count": len(points),
            "permutation_samples": permutation_samples,
            "min_observed_gain": min_gain,
            "max_holm_adjusted_p_value": max_adjusted,
            "all_observed_gains_positive": all_positive,
            "all_holm_significant": all_significant,
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
        "comparison": rows,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: under a Monte-Carlo permutation label-shuffle null, the measured "
            "largest-n stability metrics are unlikely to arise by chance from the pooled "
            "smallest-n/largest-n seed-pair values for the supplied artifacts. Invalid claim: "
            "this proves a universal scaling law, downstream quality retention, SOTA "
            "quantization, or deployment speed."
        ),
    }


def fmt(value: Any, digits: int = 4) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}f}"


def fmt_p(value: Any) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.6g}"


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    lines = [
        "# CSI Null Permutation Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- n range: `{summary['min_n']} -> {summary['max_n']}`",
        f"- points: `{summary['point_count']}`",
        f"- permutation samples: `{summary['permutation_samples']}`",
        f"- minimum observed gain: `{fmt(summary['min_observed_gain'])}`",
        f"- maximum Holm-adjusted p-value: `{fmt_p(summary['max_holm_adjusted_p_value'])}`",
        f"- all observed gains positive: `{summary['all_observed_gains_positive']}`",
        f"- all Holm-adjusted p-values significant: `{summary['all_holm_significant']}`",
        "",
        "## Full-Range Permutation Tests",
        "",
        "| metric | n=2 mean | n=8 mean | observed gain | dominance | raw p | Holm p | extreme count / samples |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in report["comparison"]:
        perm = row.get("permutation") or {}
        lines.append(
            f"| {row['label']} | {fmt(row['left_mean'])} | {fmt(row['right_mean'])} | "
            f"{fmt(row['observed_gain'])} | {fmt(row['dominance_probability'])} | "
            f"{fmt_p(perm.get('p_value'))} | {fmt_p(row.get('holm_adjusted_p_value'))} | "
            f"{perm.get('extreme_count')}/{perm.get('samples')} |"
        )
    lines.extend(["", "## Claim Boundary", "", report["claim_boundary"], "", "## Failures", ""])
    if report["failures"]:
        lines.extend(f"- {failure}" for failure in report["failures"])
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate a permutation-null CSI stability trend test.")
    parser.add_argument("--case", action="append", required=True, help="N=seed_stability_json")
    parser.add_argument("--permutation-samples", type=int, default=20000)
    parser.add_argument("--permutation-seed", type=int, default=20260607)
    parser.add_argument("--max-holm-p-value", type=float, default=0.01)
    parser.add_argument("--min-observed-gain", type=float, default=0.0)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    report = build_gate(
        [parse_case(raw) for raw in args.case],
        permutation_samples=args.permutation_samples,
        permutation_seed=args.permutation_seed,
        max_holm_p_value=args.max_holm_p_value,
        min_observed_gain=args.min_observed_gain,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
