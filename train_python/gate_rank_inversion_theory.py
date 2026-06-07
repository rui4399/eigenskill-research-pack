#!/usr/bin/env python3
from __future__ import annotations

"""Gate a plug-in rank-inversion risk analysis for CSI.

The math used in the paper is simple: if two module sensitivity estimators are
unbiased with mean gap Delta_ij and finite estimator variances, Chebyshev gives
an inversion probability upper bound proportional to
(Var_i + Var_j) / Delta_ij^2. This gate instantiates that statement with the
committed prompt-seed sensitivity artifacts. It is a theory-alignment and
diagnostic gate, not a proof that the plug-in bound is tight.
"""

import argparse
import json
import math
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class RiskCase:
    n: int
    path: Path


def parse_case(raw: str) -> RiskCase:
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
    return RiskCase(n=n, path=Path(right))


def finite(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number or math.isinf(number):
        return None
    return number


def mean(values: list[float]) -> float | None:
    return None if not values else sum(values) / len(values)


def variance(values: list[float]) -> float:
    if len(values) <= 1:
        return 0.0
    avg = sum(values) / len(values)
    return sum((value - avg) ** 2 for value in values) / (len(values) - 1)


def percentile(sorted_values: list[float], q: float) -> float | None:
    if not sorted_values:
        return None
    if len(sorted_values) == 1:
        return sorted_values[0]
    q = max(0.0, min(1.0, q))
    position = (len(sorted_values) - 1) * q
    lo = int(position)
    hi = min(lo + 1, len(sorted_values) - 1)
    weight = position - lo
    return sorted_values[lo] * (1.0 - weight) + sorted_values[hi] * weight


def fmt(value: Any, digits: int = 4) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}f}"


def fmt_sci(value: Any, digits: int = 3) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}e}"


def resolve_artifact_path(seed_gate_path: Path, raw_path: str) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    if path.exists():
        return path
    candidate = seed_gate_path.parent / path
    return candidate if candidate.exists() else path


def group_score(group: dict[str, Any]) -> float:
    positive_delta = max(float(group.get("positive_delta_nll", 0.0)), 0.0)
    cost = max(float(group.get("cost", group.get("param_count", 1.0))), 1.0e-12)
    return positive_delta / cost


def load_score_map(path: Path) -> dict[str, float]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    groups = payload.get("groups", [])
    if not isinstance(groups, list) or not groups:
        raise ValueError(f"{path}: missing non-empty groups")
    out: dict[str, float] = {}
    for group in groups:
        module = str(group.get("module") or group.get("name") or "")
        if not module:
            raise ValueError(f"{path}: group missing module/name")
        out[module] = group_score(group)
    return out


def load_case(case: RiskCase) -> dict[str, Any]:
    payload = json.loads(case.path.read_text(encoding="utf-8"))
    prompt_rows = payload.get("prompt_selections", [])
    if not isinstance(prompt_rows, list) or not prompt_rows:
        raise ValueError(f"{case.path}: missing prompt_selections")

    artifacts = []
    for row in prompt_rows:
        label = str(row.get("label", ""))
        raw_path = str(row.get("path", ""))
        if not label or not raw_path:
            raise ValueError(f"{case.path}: prompt selection missing label/path")
        artifact_path = resolve_artifact_path(case.path, raw_path)
        artifacts.append(
            {
                "label": label,
                "path": str(artifact_path),
                "scores": load_score_map(artifact_path),
            }
        )

    common_modules = set(artifacts[0]["scores"])
    for artifact in artifacts[1:]:
        common_modules &= set(artifact["scores"])
    if len(common_modules) < 2:
        raise ValueError(f"{case.path}: fewer than two shared modules")

    modules = sorted(common_modules)
    module_scores = {
        module: [float(artifact["scores"][module]) for artifact in artifacts]
        for module in modules
    }
    return {
        "n": case.n,
        "path": str(case.path),
        "source_passed": bool(payload.get("passed")),
        "artifact_count": len(artifacts),
        "module_count": len(modules),
        "module_scores": module_scores,
    }


def sign(value: float, eps: float) -> int:
    if value > eps:
        return 1
    if value < -eps:
        return -1
    return 0


def is_strictly_decreasing(rows: list[dict[str, Any]], key: str) -> bool:
    values = [finite(row.get(key)) for row in rows]
    if any(value is None for value in values):
        return False
    return all(float(left) > float(right) for left, right in zip(values, values[1:]))


def summarize_case(
    loaded: dict[str, Any],
    *,
    epsilon: float,
    margin_quantile: float,
    bound_cap: float,
) -> dict[str, Any]:
    module_scores: dict[str, list[float]] = loaded["module_scores"]
    modules = sorted(module_scores)
    score_mean = {module: sum(values) / len(values) for module, values in module_scores.items()}
    score_var = {module: variance(values) for module, values in module_scores.items()}

    rows: list[dict[str, Any]] = []
    for idx, left in enumerate(modules):
        for right in modules[idx + 1 :]:
            gap = abs(score_mean[left] - score_mean[right])
            mean_sign = sign(score_mean[left] - score_mean[right], epsilon)
            if mean_sign == 0:
                continue
            valid = 0
            inversions = 0
            for left_value, right_value in zip(module_scores[left], module_scores[right]):
                seed_sign = sign(left_value - right_value, epsilon)
                if seed_sign == 0:
                    continue
                valid += 1
                if seed_sign != mean_sign:
                    inversions += 1
            if valid == 0:
                continue
            noise = score_var[left] + score_var[right]
            chebyshev = bound_cap if gap <= epsilon else min(bound_cap, noise / (gap * gap))
            rows.append(
                {
                    "left": left,
                    "right": right,
                    "mean_gap": gap,
                    "variance_sum": noise,
                    "valid_seed_signs": valid,
                    "empirical_inversion_rate": inversions / valid,
                    "chebyshev_bound": chebyshev,
                }
            )

    if not rows:
        raise ValueError(f"n={loaded['n']}: no comparable module pairs")

    sorted_gaps = sorted(row["mean_gap"] for row in rows)
    threshold = percentile(sorted_gaps, margin_quantile)
    margin_rows = [row for row in rows if threshold is not None and row["mean_gap"] >= threshold]
    high_risk = sorted(
        rows,
        key=lambda row: (row["empirical_inversion_rate"], row["chebyshev_bound"], row["mean_gap"]),
        reverse=True,
    )[:10]

    return {
        "n": loaded["n"],
        "source_gate": loaded["path"],
        "source_passed": loaded["source_passed"],
        "artifact_count": loaded["artifact_count"],
        "module_count": loaded["module_count"],
        "pair_count": len(rows),
        "margin_quantile": margin_quantile,
        "margin_gap_threshold": threshold,
        "margin_pair_count": len(margin_rows),
        "mean_empirical_inversion_rate": mean([row["empirical_inversion_rate"] for row in rows]),
        "mean_chebyshev_bound": mean([row["chebyshev_bound"] for row in rows]),
        "median_chebyshev_bound": percentile(sorted(row["chebyshev_bound"] for row in rows), 0.5),
        "margin_empirical_inversion_rate": mean([row["empirical_inversion_rate"] for row in margin_rows]),
        "margin_chebyshev_bound": mean([row["chebyshev_bound"] for row in margin_rows]),
        "max_empirical_inversion_rate": max(row["empirical_inversion_rate"] for row in rows),
        "top_high_risk_pairs": high_risk,
    }


def build_gate(
    cases: list[RiskCase],
    *,
    epsilon: float = 1.0e-15,
    margin_quantile: float = 0.75,
    bound_cap: float = 1.0,
    min_points: int = 3,
    max_final_margin_inversion_rate: float = 0.10,
) -> dict[str, Any]:
    if len(cases) != len({case.n for case in cases}):
        raise ValueError("calibration sizes must be unique")

    rows = [
        summarize_case(
            load_case(case),
            epsilon=epsilon,
            margin_quantile=margin_quantile,
            bound_cap=bound_cap,
        )
        for case in sorted(cases, key=lambda item: item.n)
    ]

    failures: list[str] = []
    if len(rows) < min_points:
        failures.append(f"point count below threshold: {len(rows)} < {min_points}")
    failed_sources = [row["n"] for row in rows if not row["source_passed"]]
    if failed_sources:
        failures.append(f"source seed-stability gates failed: {failed_sources}")

    decreasing_checks = {
        "mean_empirical_inversion_rate_decreasing": is_strictly_decreasing(
            rows, "mean_empirical_inversion_rate"
        ),
        "mean_chebyshev_bound_decreasing": is_strictly_decreasing(rows, "mean_chebyshev_bound"),
        "margin_empirical_inversion_rate_decreasing": is_strictly_decreasing(
            rows, "margin_empirical_inversion_rate"
        ),
        "margin_chebyshev_bound_decreasing": is_strictly_decreasing(rows, "margin_chebyshev_bound"),
    }
    for key, ok in decreasing_checks.items():
        if not ok:
            failures.append(f"{key} is false across n")

    final_margin_rate = finite(rows[-1].get("margin_empirical_inversion_rate")) if rows else None
    if final_margin_rate is None or final_margin_rate > max_final_margin_inversion_rate:
        failures.append(
            "final margin empirical inversion rate above threshold: "
            f"{final_margin_rate} > {max_final_margin_inversion_rate}"
        )

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "point_count": len(rows),
            "min_n": rows[0]["n"] if rows else None,
            "max_n": rows[-1]["n"] if rows else None,
            "margin_quantile": margin_quantile,
            "mean_empirical_inversion_rate_initial": rows[0]["mean_empirical_inversion_rate"] if rows else None,
            "mean_empirical_inversion_rate_final": rows[-1]["mean_empirical_inversion_rate"] if rows else None,
            "mean_chebyshev_bound_initial": rows[0]["mean_chebyshev_bound"] if rows else None,
            "mean_chebyshev_bound_final": rows[-1]["mean_chebyshev_bound"] if rows else None,
            "margin_empirical_inversion_rate_initial": rows[0]["margin_empirical_inversion_rate"] if rows else None,
            "margin_empirical_inversion_rate_final": rows[-1]["margin_empirical_inversion_rate"] if rows else None,
            "margin_chebyshev_bound_initial": rows[0]["margin_chebyshev_bound"] if rows else None,
            "margin_chebyshev_bound_final": rows[-1]["margin_chebyshev_bound"] if rows else None,
            "max_final_margin_inversion_rate": max_final_margin_inversion_rate,
            **decreasing_checks,
        },
        "points": rows,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: a Chebyshev-style plug-in rank-inversion analysis over the committed "
            "Qwen2.5-0.5B prompt-seed sensitivity artifacts shows decreasing empirical inversion "
            "risk and decreasing variance/gap^2 upper-bound proxies as calibration size increases. "
            "Invalid claim: this proves a tight theoretical bound, downstream task retention, "
            "large-model universality, or production quantization quality."
        ),
        "theory_note": (
            "For two unbiased sensitivity estimators with true gap Delta_ij, Chebyshev gives "
            "P[(hat{s}_i - hat{s}_j) changes sign] <= (Var[hat{s}_i] + Var[hat{s}_j]) / Delta_ij^2. "
            "This gate uses seed-level sample means and variances as a diagnostic plug-in estimator."
        ),
    }


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    lines = [
        "# Rank-Inversion Theory Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- n range: `{summary['min_n']} -> {summary['max_n']}`",
        f"- curve points: `{summary['point_count']}`",
        f"- margin quantile: `{fmt(summary['margin_quantile'], 2)}`",
        f"- mean empirical inversion rate: `{fmt(summary['mean_empirical_inversion_rate_initial'])} -> {fmt(summary['mean_empirical_inversion_rate_final'])}`",
        f"- mean Chebyshev proxy bound: `{fmt(summary['mean_chebyshev_bound_initial'])} -> {fmt(summary['mean_chebyshev_bound_final'])}`",
        f"- margin empirical inversion rate: `{fmt(summary['margin_empirical_inversion_rate_initial'])} -> {fmt(summary['margin_empirical_inversion_rate_final'])}`",
        f"- margin Chebyshev proxy bound: `{fmt(summary['margin_chebyshev_bound_initial'])} -> {fmt(summary['margin_chebyshev_bound_final'])}`",
        f"- mean empirical inversion decreasing: `{summary['mean_empirical_inversion_rate_decreasing']}`",
        f"- mean Chebyshev proxy decreasing: `{summary['mean_chebyshev_bound_decreasing']}`",
        f"- margin empirical inversion decreasing: `{summary['margin_empirical_inversion_rate_decreasing']}`",
        f"- margin Chebyshev proxy decreasing: `{summary['margin_chebyshev_bound_decreasing']}`",
        "",
        "## Theory Note",
        "",
        report["theory_note"],
        "",
        "## Curve Points",
        "",
        "| n | artifacts | modules | pairs | margin pairs | margin gap | mean inversion | mean bound | margin inversion | margin bound |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in report["points"]:
        lines.append(
            f"| {row['n']} | {row['artifact_count']} | {row['module_count']} | {row['pair_count']} | "
            f"{row['margin_pair_count']} | {fmt_sci(row['margin_gap_threshold'])} | "
            f"{fmt(row['mean_empirical_inversion_rate'])} | {fmt(row['mean_chebyshev_bound'])} | "
            f"{fmt(row['margin_empirical_inversion_rate'])} | {fmt(row['margin_chebyshev_bound'])} |"
        )
    lines.extend(["", "## Representative High-Risk Pairs", ""])
    for row in report["points"]:
        lines.append(f"### n={row['n']}")
        lines.append("")
        lines.append("| left | right | gap | variance sum | empirical inversion | bound |")
        lines.append("|---|---|---:|---:|---:|---:|")
        for pair in row["top_high_risk_pairs"][:5]:
            lines.append(
                f"| `{pair['left']}` | `{pair['right']}` | {fmt_sci(pair['mean_gap'])} | "
                f"{fmt_sci(pair['variance_sum'])} | {fmt(pair['empirical_inversion_rate'])} | "
                f"{fmt(pair['chebyshev_bound'])} |"
            )
        lines.append("")
    lines.extend(["## Claim Boundary", "", report["claim_boundary"], "", "## Failures", ""])
    if report["failures"]:
        lines.extend(f"- {failure}" for failure in report["failures"])
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate plug-in rank-inversion theory evidence for CSI.")
    parser.add_argument("--case", action="append", required=True, help="N=seed_stability_json")
    parser.add_argument("--epsilon", type=float, default=1.0e-15)
    parser.add_argument("--margin-quantile", type=float, default=0.75)
    parser.add_argument("--bound-cap", type=float, default=1.0)
    parser.add_argument("--min-points", type=int, default=3)
    parser.add_argument("--max-final-margin-inversion-rate", type=float, default=0.10)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    report = build_gate(
        [parse_case(raw) for raw in args.case],
        epsilon=args.epsilon,
        margin_quantile=args.margin_quantile,
        bound_cap=args.bound_cap,
        min_points=args.min_points,
        max_final_margin_inversion_rate=args.max_final_margin_inversion_rate,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
