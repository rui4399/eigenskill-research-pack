#!/usr/bin/env python3
from __future__ import annotations

"""Gate the calibration split instability curve across calibration sizes."""

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CurveCase:
    n: int
    path: Path


METRICS: tuple[tuple[str, str], ...] = (
    ("mean_score_spearman", "mean score/cost Spearman"),
    ("mean_top20_jaccard", "mean top-20 Jaccard"),
    ("mean_positive_jaccard", "mean positive-set Jaccard"),
)


def parse_case(raw: str) -> CurveCase:
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
    return CurveCase(n=n, path=Path(right))


def finite(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


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


def load_case(case: CurveCase) -> dict[str, Any]:
    payload = json.loads(case.path.read_text(encoding="utf-8"))
    summary = payload.get("summary", {}) or {}
    return {
        "n": case.n,
        "path": str(case.path),
        "source_passed": bool(payload.get("passed")),
        "case_count": summary.get("case_count"),
        "pair_count": summary.get("pair_count"),
        "unique_prompt_selection_count": summary.get("unique_prompt_selection_count"),
        "mean_score_spearman": finite(summary.get("mean_score_spearman")),
        "mean_score_spearman_ci": summary.get("mean_score_spearman_ci"),
        "mean_top20_jaccard": finite(summary.get("mean_top20_jaccard")),
        "mean_top20_jaccard_ci": summary.get("mean_top20_jaccard_ci"),
        "mean_positive_jaccard": finite(summary.get("mean_positive_jaccard")),
        "mean_positive_jaccard_ci": summary.get("mean_positive_jaccard_ci"),
        "min_score_spearman": finite(summary.get("min_score_spearman")),
        "min_top20_jaccard": finite(summary.get("min_top20_jaccard")),
        "min_positive_jaccard": finite(summary.get("min_positive_jaccard")),
    }


def is_strictly_increasing(rows: list[dict[str, Any]], key: str) -> bool:
    values = [finite(row.get(key)) for row in rows]
    if any(value is None for value in values):
        return False
    return all(float(left) < float(right) for left, right in zip(values, values[1:]))


def ci_separates(left_ci: Any, right_ci: Any) -> bool | None:
    if not isinstance(left_ci, dict) or not isinstance(right_ci, dict):
        return None
    left_high = finite(left_ci.get("high"))
    right_low = finite(right_ci.get("low"))
    if left_high is None or right_low is None:
        return None
    return left_high < right_low


def build_curve(cases: list[CurveCase], *, min_points: int = 3) -> dict[str, Any]:
    if len(cases) != len({case.n for case in cases}):
        raise ValueError("calibration sizes must be unique")

    rows = sorted((load_case(case) for case in cases), key=lambda row: row["n"])
    failures: list[str] = []
    if len(rows) < min_points:
        failures.append(f"curve point count below threshold: {len(rows)} < {min_points}")
    failed_sources = [row for row in rows if not row["source_passed"]]
    if failed_sources:
        failures.append(f"source seed-stability gates failed: {[row['n'] for row in failed_sources]}")

    monotonic: dict[str, bool] = {}
    gains: dict[str, float | None] = {}
    ci_separation: dict[str, list[dict[str, Any]]] = {}
    for key, _ in METRICS:
        monotonic[key] = is_strictly_increasing(rows, key)
        first = finite(rows[0].get(key)) if rows else None
        last = finite(rows[-1].get(key)) if rows else None
        gains[key] = None if first is None or last is None else last - first
        ci_key = key + "_ci"
        ci_separation[key] = [
            {
                "left_n": left["n"],
                "right_n": right["n"],
                "separated": ci_separates(left.get(ci_key), right.get(ci_key)),
            }
            for left, right in zip(rows, rows[1:])
        ]
        if not monotonic[key]:
            failures.append(f"{key} is not strictly increasing across n")

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "point_count": len(rows),
            "min_n": rows[0]["n"] if rows else None,
            "max_n": rows[-1]["n"] if rows else None,
            "mean_score_spearman_gain": gains.get("mean_score_spearman"),
            "mean_top20_jaccard_gain": gains.get("mean_top20_jaccard"),
            "mean_positive_jaccard_gain": gains.get("mean_positive_jaccard"),
            "mean_score_spearman_monotonic": monotonic.get("mean_score_spearman", False),
            "mean_top20_jaccard_monotonic": monotonic.get("mean_top20_jaccard", False),
            "mean_positive_jaccard_monotonic": monotonic.get("mean_positive_jaccard", False),
        },
        "points": rows,
        "ci_separation": ci_separation,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: on Qwen2.5-0.5B-Instruct and this public WikiText2 prompt pool, "
            "six deterministic prompt seeds show that sensitivity-ranking stability improves "
            "as calibration prompt count increases from n=2 to n=8. Invalid claim: this curve "
            "alone proves downstream task retention, real quantized runtime speed, or large-model universality."
        ),
    }


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    lines = [
        "# CSI vs Calibration Size Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- curve points: `{summary['point_count']}`",
        f"- n range: `{summary['min_n']} -> {summary['max_n']}`",
        f"- mean score/cost Spearman gain: `{fmt(summary['mean_score_spearman_gain'])}`",
        f"- mean top-20 Jaccard gain: `{fmt(summary['mean_top20_jaccard_gain'])}`",
        f"- mean positive-set Jaccard gain: `{fmt(summary['mean_positive_jaccard_gain'])}`",
        f"- score/cost Spearman monotonic: `{summary['mean_score_spearman_monotonic']}`",
        f"- top-20 Jaccard monotonic: `{summary['mean_top20_jaccard_monotonic']}`",
        f"- positive-set Jaccard monotonic: `{summary['mean_positive_jaccard_monotonic']}`",
        "",
        "## Curve Points",
        "",
        "| n | source gate | cases | pairs | unique selections | mean Spearman | 95% CI | top-20 Jaccard | 95% CI | positive Jaccard | 95% CI |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in report["points"]:
        lines.append(
            f"| {row['n']} | `{row['path']}` | {row['case_count']} | {row['pair_count']} | "
            f"{row['unique_prompt_selection_count']} | {fmt(row['mean_score_spearman'])} | "
            f"{fmt_ci(row['mean_score_spearman_ci'])} | {fmt(row['mean_top20_jaccard'])} | "
            f"{fmt_ci(row['mean_top20_jaccard_ci'])} | {fmt(row['mean_positive_jaccard'])} | "
            f"{fmt_ci(row['mean_positive_jaccard_ci'])} |"
        )
    lines.extend(["", "## Adjacent CI Separation", ""])
    for key, label in METRICS:
        lines.append(f"### {label}")
        for row in report["ci_separation"].get(key, []):
            lines.append(f"- n={row['left_n']} -> n={row['right_n']}: `{row['separated']}`")
        lines.append("")
    lines.extend(["## Claim Boundary", "", report["claim_boundary"], "", "## Failures", ""])
    if report["failures"]:
        lines.extend(f"- {failure}" for failure in report["failures"])
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def svg_polyline(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.2f},{y:.2f}" for x, y in points)


def write_svg(path: Path, report: dict[str, Any]) -> None:
    rows = report["points"]
    width, height = 760, 440
    left, right, top, bottom = 72, 28, 28, 68
    plot_w = width - left - right
    plot_h = height - top - bottom
    n_values = [float(row["n"]) for row in rows]
    min_n, max_n = min(n_values), max(n_values)

    def x_for(n: float) -> float:
        if max_n == min_n:
            return left + plot_w / 2.0
        return left + (n - min_n) / (max_n - min_n) * plot_w

    def y_for(value: float) -> float:
        return top + (1.0 - value) * plot_h

    series = [
        ("mean_score_spearman", "Spearman", "#1f77b4"),
        ("mean_top20_jaccard", "Top-20 Jaccard", "#d62728"),
        ("mean_positive_jaccard", "Positive Jaccard", "#2ca02c"),
    ]
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="#333"/>',
        f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="#333"/>',
        f'<text x="{width/2}" y="{height-18}" text-anchor="middle" font-family="Arial" font-size="14">calibration prompts n</text>',
        f'<text x="18" y="{height/2}" text-anchor="middle" transform="rotate(-90 18 {height/2})" font-family="Arial" font-size="14">stability metric</text>',
        f'<text x="{width/2}" y="20" text-anchor="middle" font-family="Arial" font-size="16">CSI stability improves with calibration size</text>',
    ]
    for tick in [0.0, 0.25, 0.5, 0.75, 1.0]:
        y = y_for(tick)
        lines.append(f'<line x1="{left-5}" y1="{y:.2f}" x2="{width-right}" y2="{y:.2f}" stroke="#ddd"/>')
        lines.append(f'<text x="{left-10}" y="{y+4:.2f}" text-anchor="end" font-family="Arial" font-size="12">{tick:.2f}</text>')
    for row in rows:
        x = x_for(float(row["n"]))
        lines.append(f'<line x1="{x:.2f}" y1="{height-bottom}" x2="{x:.2f}" y2="{height-bottom+5}" stroke="#333"/>')
        lines.append(f'<text x="{x:.2f}" y="{height-bottom+22}" text-anchor="middle" font-family="Arial" font-size="12">{row["n"]}</text>')
    for idx, (key, label, color) in enumerate(series):
        pts = [(x_for(float(row["n"])), y_for(float(row[key]))) for row in rows if row.get(key) is not None]
        lines.append(f'<polyline points="{svg_polyline(pts)}" fill="none" stroke="{color}" stroke-width="3"/>')
        for x, y in pts:
            lines.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4.5" fill="{color}"/>')
        legend_y = 48 + idx * 22
        lines.append(f'<line x1="{width-210}" y1="{legend_y}" x2="{width-178}" y2="{legend_y}" stroke="{color}" stroke-width="3"/>')
        lines.append(f'<text x="{width-170}" y="{legend_y+4}" font-family="Arial" font-size="13">{label}</text>')
    lines.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate CSI stability as a function of calibration size n.")
    parser.add_argument("--case", action="append", required=True, help="N=gate_json")
    parser.add_argument("--min-points", type=int, default=3)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    parser.add_argument("--out-svg", type=Path)
    args = parser.parse_args()

    report = build_curve([parse_case(raw) for raw in args.case], min_points=args.min_points)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    if args.out_svg:
        write_svg(args.out_svg, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
