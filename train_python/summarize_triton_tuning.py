#!/usr/bin/env python3
from __future__ import annotations

"""Summarize Triton packed mixed-GEMM tuning JSONL files across shapes."""

import argparse
import csv
import json
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def finite_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def median(values: list[float]) -> float | None:
    return statistics.median(values) if values else None


def quantile(values: list[float], q: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    pos = q * (len(ordered) - 1)
    lo = int(pos)
    hi = min(lo + 1, len(ordered) - 1)
    frac = pos - lo
    return ordered[lo] * (1.0 - frac) + ordered[hi] * frac


def fmt(value: Any, digits: int = 4) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def summarize_group(rows: list[dict[str, Any]]) -> dict[str, Any]:
    valid = [row for row in rows if row.get("returncode") == 0 and row.get("grouped_mixed_ms") is not None]
    fp16_speedups = [v for row in valid if (v := finite_float(row.get("grouped_speedup_vs_torch_fp16"))) is not None]
    row_speedups = [v for row in valid if (v := finite_float(row.get("grouped_speedup_vs_rowwise"))) is not None]
    compressions = [v for row in valid if (v := finite_float(row.get("compression_ratio_vs_fp16"))) is not None]
    rel_l2s = [v for row in valid if (v := finite_float(row.get("grouped_rel_l2"))) is not None]
    vram_ratios = [v for row in valid if (v := finite_float(row.get("guard_max_memory_used_ratio"))) is not None]
    best_fp16 = max(valid, key=lambda row: finite_float(row.get("grouped_speedup_vs_torch_fp16")) or -1.0, default=None)
    best_rowwise = max(valid, key=lambda row: finite_float(row.get("grouped_speedup_vs_rowwise")) or -1.0, default=None)
    return {
        "count": len(rows),
        "valid_count": len(valid),
        "fp16_wins": sum(1 for value in fp16_speedups if value > 1.0),
        "rowwise_wins": sum(1 for value in row_speedups if value > 1.0),
        "fp16_speedup_min": min(fp16_speedups) if fp16_speedups else None,
        "fp16_speedup_median": median(fp16_speedups),
        "fp16_speedup_p90": quantile(fp16_speedups, 0.90),
        "fp16_speedup_max": max(fp16_speedups) if fp16_speedups else None,
        "rowwise_speedup_median": median(row_speedups),
        "rowwise_speedup_max": max(row_speedups) if row_speedups else None,
        "compression_median": median(compressions),
        "compression_max": max(compressions) if compressions else None,
        "rel_l2_median": median(rel_l2s),
        "rel_l2_max": max(rel_l2s) if rel_l2s else None,
        "guard_vram_ratio_max": max(vram_ratios) if vram_ratios else None,
        "best_fp16": best_fp16,
        "best_rowwise": best_rowwise,
    }


def write_csv(path: Path, summaries: list[dict[str, Any]]) -> None:
    fieldnames = [
        "shape",
        "batch",
        "high_every",
        "count",
        "valid_count",
        "fp16_wins",
        "rowwise_wins",
        "fp16_speedup_median",
        "fp16_speedup_p90",
        "fp16_speedup_max",
        "rowwise_speedup_median",
        "rowwise_speedup_max",
        "compression_median",
        "rel_l2_median",
        "guard_vram_ratio_max",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in summaries:
            writer.writerow({key: row.get(key) for key in fieldnames})


def write_markdown(path: Path, rows: list[dict[str, Any]], aggregate: dict[str, Any], top: list[dict[str, Any]]) -> None:
    lines = [
        "# Triton Mixed-GEMM Cross-Shape Tuning Summary",
        "",
        "This report aggregates packed INT4/INT8 Triton GEMM tuning runs across Qwen-like Linear shapes.",
        "It is a kernel benchmark summary, not an end-to-end transformer runtime result.",
        "",
        "## Aggregate",
        "",
        f"- total configs: {aggregate['count']}",
        f"- valid configs: {aggregate['valid_count']}",
        f"- configs faster than torch FP16: {aggregate['fp16_wins']}",
        f"- configs faster than row-wise dynamic mixed path: {aggregate['rowwise_wins']}",
        f"- grouped/FP16 speedup median: {fmt(aggregate['fp16_speedup_median'])}",
        f"- grouped/FP16 speedup p90: {fmt(aggregate['fp16_speedup_p90'])}",
        f"- grouped/FP16 speedup max: {fmt(aggregate['fp16_speedup_max'])}",
        f"- grouped/row-wise speedup median: {fmt(aggregate['rowwise_speedup_median'])}",
        f"- grouped/row-wise speedup max: {fmt(aggregate['rowwise_speedup_max'])}",
        f"- compression vs FP16 median: {fmt(aggregate['compression_median'])}x",
        f"- grouped rel-L2 median: {fmt(aggregate['rel_l2_median'])}",
        f"- max guard VRAM ratio: {fmt(aggregate['guard_vram_ratio_max'])}",
        "",
        "## Shape Summary",
        "",
        "| shape | batch | high_every | configs | FP16 wins | row-wise wins | median grouped/FP16 | max grouped/FP16 | median grouped/row-wise | max grouped/row-wise | median rel-L2 | max VRAM ratio |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['shape']} | {row['batch']} | {row['high_every']} | {row['valid_count']} | "
            f"{row['fp16_wins']} | {row['rowwise_wins']} | {fmt(row['fp16_speedup_median'])} | "
            f"{fmt(row['fp16_speedup_max'])} | {fmt(row['rowwise_speedup_median'])} | "
            f"{fmt(row['rowwise_speedup_max'])} | {fmt(row['rel_l2_median'])} | {fmt(row['guard_vram_ratio_max'])} |"
        )

    lines.extend(
        [
            "",
            "## Top Grouped vs Torch FP16 Cases",
            "",
            "| rank | shape | batch | high_every | BM | BN | BK | grouped ms | torch FP16 ms | speedup | compression vs FP16 | rel-L2 |",
            "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for rank, row in enumerate(top, start=1):
        lines.append(
            f"| {rank} | {row.get('rows')}x{row.get('cols')} | {row.get('batch')} | {row.get('high_every')} | "
            f"{row.get('block_m')} | {row.get('block_n')} | {row.get('block_k')} | "
            f"{fmt(row.get('grouped_mixed_ms'), 6)} | {fmt(row.get('torch_fp16_ms'), 6)} | "
            f"{fmt(row.get('grouped_speedup_vs_torch_fp16'))} | {fmt(row.get('compression_ratio_vs_fp16'))}x | "
            f"{fmt(row.get('grouped_rel_l2'))} |"
        )

    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "- Valid claim: grouped packed execution reduces row-wise dynamic overhead and can beat FP16 in a subset of tuned kernel shapes.",
            "- Invalid claim: end-to-end LLM acceleration, SOTA quantization quality, or Tensor Core production runtime.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize Triton tuning JSONL files.")
    parser.add_argument("--input", action="append", required=True, help="Path to tuning_results.jsonl; repeatable.")
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/triton_cross_shape_summary.json"))
    parser.add_argument("--out-csv", type=Path, default=Path("outputs/real_system_packer_2026-06-05/triton_cross_shape_summary.csv"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/TRITON_CROSS_SHAPE_SUMMARY.md"))
    args = parser.parse_args()

    all_rows: list[dict[str, Any]] = []
    for text in args.input:
        all_rows.extend(load_jsonl(Path(text)))

    groups: dict[tuple[int, int, int, int], list[dict[str, Any]]] = defaultdict(list)
    for row in all_rows:
        key = (int(row.get("rows", 0)), int(row.get("cols", 0)), int(row.get("batch", 0)), int(row.get("high_every", 0)))
        groups[key].append(row)

    summaries: list[dict[str, Any]] = []
    for (rows, cols, batch, high_every), items in sorted(groups.items()):
        summary = summarize_group(items)
        summary.update({"shape": f"{rows}x{cols}", "rows": rows, "cols": cols, "batch": batch, "high_every": high_every})
        summary.pop("best_fp16", None)
        summary.pop("best_rowwise", None)
        summaries.append(summary)

    aggregate = summarize_group(all_rows)
    valid = [row for row in all_rows if row.get("returncode") == 0 and row.get("grouped_mixed_ms") is not None]
    top = sorted(valid, key=lambda row: finite_float(row.get("grouped_speedup_vs_torch_fp16")) or -1.0, reverse=True)[:12]

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(
        json.dumps({"aggregate": aggregate, "shape_summaries": summaries, "top_grouped_vs_fp16": top}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_csv(args.out_csv, summaries)
    write_markdown(args.out_md, summaries, aggregate, top)
    print(json.dumps({"out_json": str(args.out_json), "out_csv": str(args.out_csv), "out_md": str(args.out_md), "configs": len(all_rows)}, indent=2))


if __name__ == "__main__":
    main()
