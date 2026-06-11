#!/usr/bin/env python3
from __future__ import annotations

"""Build paper-facing CSI cross-scale table and dual-curve figure artifacts."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


METRICS: tuple[tuple[str, str, str], ...] = (
    ("mean_score_spearman", "Spearman", "#1f77b4"),
    ("mean_top20_jaccard", "Top-20 Jaccard", "#d62728"),
    ("mean_positive_jaccard", "Positive Jaccard", "#2ca02c"),
)


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


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_curve(label: str, path: Path) -> dict[str, Any]:
    payload = load_json(path)
    points = payload.get("points", []) or []
    return {
        "label": label,
        "path": str(path),
        "passed": bool(payload.get("passed")),
        "points": points,
        "points_by_n": {int(row["n"]): row for row in points},
    }


def point_value(curve: dict[str, Any], n: int, metric: str) -> float | None:
    return finite(curve["points_by_n"].get(n, {}).get(metric))


def build_report(left_label: str, left_path: Path, right_label: str, right_path: Path) -> dict[str, Any]:
    left = load_curve(left_label, left_path)
    right = load_curve(right_label, right_path)
    common_n = sorted(set(left["points_by_n"]).intersection(right["points_by_n"]))
    failures: list[str] = []
    if not left["passed"]:
        failures.append(f"left curve gate failed: {left_label}")
    if not right["passed"]:
        failures.append(f"right curve gate failed: {right_label}")
    if len(common_n) < 2:
        failures.append(f"need at least two common n values, got {common_n}")

    same_n_table: list[dict[str, Any]] = []
    for n in common_n:
        row: dict[str, Any] = {"n": n}
        for metric, _, _ in METRICS:
            left_value = point_value(left, n, metric)
            right_value = point_value(right, n, metric)
            row[metric] = {
                "left": left_value,
                "right": right_value,
                "right_minus_left": None
                if left_value is None or right_value is None
                else right_value - left_value,
            }
        same_n_table.append(row)

    gain_table: list[dict[str, Any]] = []
    if len(common_n) >= 2:
        min_n, max_n = common_n[0], common_n[-1]
        for metric, _, _ in METRICS:
            left_gain = None
            right_gain = None
            left_min = point_value(left, min_n, metric)
            left_max = point_value(left, max_n, metric)
            right_min = point_value(right, min_n, metric)
            right_max = point_value(right, max_n, metric)
            if left_min is not None and left_max is not None:
                left_gain = left_max - left_min
            if right_min is not None and right_max is not None:
                right_gain = right_max - right_min
            gain_table.append(
                {
                    "metric": metric,
                    "min_n": min_n,
                    "max_n": max_n,
                    "left_gain": left_gain,
                    "right_gain": right_gain,
                    "right_minus_left_gain": None
                    if left_gain is None or right_gain is None
                    else right_gain - left_gain,
                }
            )

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "left": left,
        "right": right,
        "common_n": common_n,
        "same_n_table": same_n_table,
        "gain_table": gain_table,
        "failures": failures,
        "paper_claim": (
            "For the audited Qwen2.5 artifacts, 1.5B has lower CSI stability than 0.5B "
            "at each shared n in all three metrics, while both scales improve from n=2 "
            "to n=8. This is a cross-scale replication and comparison, not a causal "
            "scaling-law claim."
        ),
    }


def svg_polyline(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.2f},{y:.2f}" for x, y in points)


def write_svg(path: Path, report: dict[str, Any]) -> None:
    rows = report["same_n_table"]
    width, height = 920, 520
    left_pad, right_pad, top_pad, bottom_pad = 76, 190, 40, 72
    plot_w = width - left_pad - right_pad
    plot_h = height - top_pad - bottom_pad
    n_values = [float(row["n"]) for row in rows]
    min_n, max_n = min(n_values), max(n_values)

    def x_for(n: float) -> float:
        return left_pad + (n - min_n) / (max_n - min_n) * plot_w if max_n != min_n else left_pad + plot_w / 2.0

    def y_for(value: float) -> float:
        return top_pad + (1.0 - value) * plot_h

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width / 2}" y="24" text-anchor="middle" font-family="Arial" font-size="18">Qwen2.5 CSI stability across calibration size and scale</text>',
        f'<line x1="{left_pad}" y1="{top_pad}" x2="{left_pad}" y2="{height - bottom_pad}" stroke="#333"/>',
        f'<line x1="{left_pad}" y1="{height - bottom_pad}" x2="{width - right_pad}" y2="{height - bottom_pad}" stroke="#333"/>',
        f'<text x="{left_pad + plot_w / 2}" y="{height - 22}" text-anchor="middle" font-family="Arial" font-size="14">calibration prompts n</text>',
        f'<text x="20" y="{top_pad + plot_h / 2}" text-anchor="middle" transform="rotate(-90 20 {top_pad + plot_h / 2})" font-family="Arial" font-size="14">stability metric</text>',
    ]
    for tick in [0.0, 0.25, 0.5, 0.75, 1.0]:
        y = y_for(tick)
        lines.append(f'<line x1="{left_pad - 5}" y1="{y:.2f}" x2="{width - right_pad}" y2="{y:.2f}" stroke="#e6e6e6"/>')
        lines.append(f'<text x="{left_pad - 10}" y="{y + 4:.2f}" text-anchor="end" font-family="Arial" font-size="12">{tick:.2f}</text>')
    for row in rows:
        x = x_for(float(row["n"]))
        lines.append(f'<line x1="{x:.2f}" y1="{height - bottom_pad}" x2="{x:.2f}" y2="{height - bottom_pad + 5}" stroke="#333"/>')
        lines.append(f'<text x="{x:.2f}" y="{height - bottom_pad + 24}" text-anchor="middle" font-family="Arial" font-size="12">{row["n"]}</text>')

    labels = [report["left"]["label"], report["right"]["label"]]
    dash_by_label = {labels[0]: "", labels[1]: ' stroke-dasharray="7 5"'}
    for metric, label, color in METRICS:
        for scale_label, value_key in [(labels[0], "left"), (labels[1], "right")]:
            pts = [
                (x_for(float(row["n"])), y_for(float(row[metric][value_key])))
                for row in rows
                if row[metric][value_key] is not None
            ]
            dash = dash_by_label[scale_label]
            lines.append(f'<polyline points="{svg_polyline(pts)}" fill="none" stroke="{color}" stroke-width="3"{dash}/>')
            for x, y in pts:
                lines.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4" fill="{color}" stroke="white" stroke-width="1"/>')

    legend_x = width - right_pad + 28
    for idx, (metric, label, color) in enumerate(METRICS):
        y = 72 + idx * 28
        lines.append(f'<line x1="{legend_x}" y1="{y}" x2="{legend_x + 28}" y2="{y}" stroke="{color}" stroke-width="3"/>')
        lines.append(f'<text x="{legend_x + 36}" y="{y + 4}" font-family="Arial" font-size="12">{label}</text>')
    scale_y = 188
    lines.append(f'<line x1="{legend_x}" y1="{scale_y}" x2="{legend_x + 28}" y2="{scale_y}" stroke="#555" stroke-width="3"/>')
    lines.append(f'<text x="{legend_x + 36}" y="{scale_y + 4}" font-family="Arial" font-size="12">{labels[0]}</text>')
    lines.append(f'<line x1="{legend_x}" y1="{scale_y + 28}" x2="{legend_x + 28}" y2="{scale_y + 28}" stroke="#555" stroke-width="3" stroke-dasharray="7 5"/>')
    lines.append(f'<text x="{legend_x + 36}" y="{scale_y + 32}" font-family="Arial" font-size="12">{labels[1]}</text>')
    lines.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_markdown(path: Path, report: dict[str, Any], svg_path: Path) -> None:
    left = report["left"]["label"]
    right = report["right"]["label"]
    lines = [
        "# CSI Cross-Scale Paper Artifacts",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        f"Figure: `{svg_path}`",
        "",
        "## Same-n Stability Table",
        "",
        "| n | metric | 0.5B | 1.5B | 1.5B - 0.5B |",
        "|---:|---|---:|---:|---:|",
    ]
    for row in report["same_n_table"]:
        for metric, label, _ in METRICS:
            values = row[metric]
            lines.append(
                f"| {row['n']} | {label} | {fmt(values['left'])} | {fmt(values['right'])} | {fmt(values['right_minus_left'])} |"
            )
    lines.extend(
        [
            "",
            "## n=2 to n=8 Gain Table",
            "",
            "| metric | n range | 0.5B gain | 1.5B gain | 1.5B gain - 0.5B gain |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for row in report["gain_table"]:
        label = next(label for metric, label, _ in METRICS if metric == row["metric"])
        lines.append(
            f"| {label} | {row['min_n']} -> {row['max_n']} | {fmt(row['left_gain'])} | {fmt(row['right_gain'])} | {fmt(row['right_minus_left_gain'])} |"
        )
    lines.extend(
        [
            "",
            "## Paper Claim",
            "",
            report["paper_claim"],
            "",
            "## Source Artifacts",
            "",
            f"- `{left}`: `{report['left']['path']}`",
            f"- `{right}`: `{report['right']['path']}`",
            "",
            "## Failures",
            "",
        ]
    )
    if report["failures"]:
        lines.extend(f"- {failure}" for failure in report["failures"])
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build paper-ready CSI cross-scale artifacts.")
    parser.add_argument("--left-label", default="Qwen2.5-0.5B")
    parser.add_argument("--left-json", type=Path, default=Path("outputs/csi_vs_n_curve_qwen25_0p5b_2026_06_07.json"))
    parser.add_argument("--right-label", default="Qwen2.5-1.5B")
    parser.add_argument("--right-json", type=Path, default=Path("outputs/csi_vs_n_curve_qwen25_1p5b_2026_06_11.json"))
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    parser.add_argument("--out-svg", type=Path, required=True)
    args = parser.parse_args()

    report = build_report(args.left_label, args.left_json, args.right_label, args.right_json)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_svg(args.out_svg, report)
    write_markdown(args.out_md, report, args.out_svg)
    print(json.dumps({"passed": report["passed"], "failures": report["failures"]}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
