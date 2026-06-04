#!/usr/bin/env python3
from __future__ import annotations

"""Render the consensus budget curve as a dependency-free SVG figure."""

import argparse
import csv
import html
from pathlib import Path


def load_rows(path: str) -> list[dict]:
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def budget_for_config(row: dict) -> float | None:
    config = row["config"]
    if config == "uniform_int4":
        return 4.0
    if config == "consensus_budget_4p25":
        return 4.25
    if config == "consensus_budget_4p50":
        return 4.50
    if config == "consensus_budget_4p75":
        return 4.75
    return None


def fmt(value: float) -> str:
    return f"{value:.1f}" if abs(value) >= 10 else f"{value:.2f}"


def render_svg(rows: list[dict], out_path: str) -> None:
    datasets = []
    by_dataset: dict[str, list[dict]] = {}
    for row in rows:
        by_dataset.setdefault(row["dataset"], []).append(row)
    for name in by_dataset:
        datasets.append(name)

    panel_w = 360
    panel_h = 250
    cols = 2
    rows_n = (len(datasets) + cols - 1) // cols
    width = cols * panel_w + 80
    height = rows_n * panel_h + 90
    margin_l = 58
    margin_t = 48
    plot_w = 250
    plot_h = 150

    palette = {
        "axis": "#2f3437",
        "grid": "#d8dde3",
        "line": "#225ea8",
        "point": "#d94801",
        "fp16": "#2ca25f",
        "text": "#1f2933",
    }

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<style>text{font-family:Arial,Helvetica,sans-serif}.title{font-size:18px;font-weight:700}.label{font-size:11px}.small{font-size:10px}</style>",
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
        '<text x="40" y="30" class="title" fill="#111827">Consensus budget curve, fake-quant PPL</text>',
    ]

    for idx, dataset in enumerate(datasets):
        col = idx % cols
        row_i = idx // cols
        x0 = 40 + col * panel_w
        y0 = 55 + row_i * panel_h
        data = by_dataset[dataset]
        fp16 = next(item for item in data if item["config"] == "fp16")
        curve = [item for item in data if budget_for_config(item) is not None]
        curve.sort(key=lambda item: budget_for_config(item) or 0.0)
        ppls = [float(item["ppl"]) for item in curve] + [float(fp16["ppl"])]
        y_min = min(ppls) * 0.96
        y_max = max(ppls) * 1.04
        if y_max <= y_min:
            y_max = y_min + 1.0

        def sx(avg_bits: float) -> float:
            return x0 + margin_l + (avg_bits - 4.0) / 0.75 * plot_w

        def sy(ppl: float) -> float:
            return y0 + margin_t + (y_max - ppl) / (y_max - y_min) * plot_h

        parts.append(f'<text x="{x0 + margin_l}" y="{y0 + 20}" class="label" font-weight="700" fill="{palette["text"]}">{html.escape(dataset)}</text>')
        parts.append(f'<rect x="{x0 + margin_l}" y="{y0 + margin_t}" width="{plot_w}" height="{plot_h}" fill="#fbfcfd" stroke="{palette["grid"]}"/>')

        for tick in [y_min, (y_min + y_max) * 0.5, y_max]:
            y = sy(tick)
            parts.append(f'<line x1="{x0 + margin_l}" y1="{y:.2f}" x2="{x0 + margin_l + plot_w}" y2="{y:.2f}" stroke="{palette["grid"]}" stroke-width="1"/>')
            parts.append(f'<text x="{x0 + margin_l - 8}" y="{y + 3:.2f}" text-anchor="end" class="small" fill="{palette["text"]}">{fmt(tick)}</text>')

        for tick in [4.0, 4.25, 4.5, 4.75]:
            x = sx(tick)
            parts.append(f'<line x1="{x:.2f}" y1="{y0 + margin_t}" x2="{x:.2f}" y2="{y0 + margin_t + plot_h}" stroke="{palette["grid"]}" stroke-width="1"/>')
            parts.append(f'<text x="{x:.2f}" y="{y0 + margin_t + plot_h + 18}" text-anchor="middle" class="small" fill="{palette["text"]}">{tick:.2f}</text>')

        fp16_y = sy(float(fp16["ppl"]))
        parts.append(f'<line x1="{x0 + margin_l}" y1="{fp16_y:.2f}" x2="{x0 + margin_l + plot_w}" y2="{fp16_y:.2f}" stroke="{palette["fp16"]}" stroke-width="1.5" stroke-dasharray="4 3"/>')
        parts.append(f'<text x="{x0 + margin_l + plot_w + 6}" y="{fp16_y + 3:.2f}" class="small" fill="{palette["fp16"]}">FP16</text>')

        points = [(sx(budget_for_config(item) or 4.0), sy(float(item["ppl"])), item) for item in curve]
        path = " ".join(("M" if i == 0 else "L") + f" {x:.2f} {y:.2f}" for i, (x, y, _item) in enumerate(points))
        parts.append(f'<path d="{path}" fill="none" stroke="{palette["line"]}" stroke-width="2.2"/>')
        for x, y, item in points:
            parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4" fill="{palette["point"]}"/>')
            parts.append(f'<text x="{x:.2f}" y="{y - 8:.2f}" text-anchor="middle" class="small" fill="{palette["text"]}">{float(item["ppl"]):.2f}</text>')

        parts.append(f'<text x="{x0 + margin_l + plot_w / 2}" y="{y0 + margin_t + plot_h + 38}" text-anchor="middle" class="small" fill="{palette["text"]}">average bits</text>')
        parts.append(f'<text x="{x0 + 12}" y="{y0 + margin_t + plot_h / 2}" transform="rotate(-90 {x0 + 12} {y0 + margin_t + plot_h / 2})" text-anchor="middle" class="small" fill="{palette["text"]}">PPL</text>')

    parts.extend(
        [
            f'<text x="40" y="{height - 24}" class="small" fill="{palette["text"]}">Solid line: uniform INT4 and consensus {4,8} budgets. Dashed green: FP16 reference. Short-slice fake quant; not a hardware result.</text>',
            "</svg>",
        ]
    )
    Path(out_path).write_text("\n".join(parts) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/consensus_budget_curve_summary.csv")
    parser.add_argument("--out", default="outputs/consensus_budget_curve.svg")
    args = parser.parse_args()
    render_svg(load_rows(args.input), args.out)
    print(args.out)


if __name__ == "__main__":
    main()
