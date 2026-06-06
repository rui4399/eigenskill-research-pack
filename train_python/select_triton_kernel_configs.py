#!/usr/bin/env python3
from __future__ import annotations

"""Select deployable Triton block configs from tuning JSONL evidence."""

import argparse
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


def valid_for_selection(row: dict[str, Any], max_rel_l2: float, max_vram_ratio: float) -> bool:
    if row.get("returncode") != 0:
        return False
    if finite_float(row.get("grouped_mixed_ms")) is None:
        return False
    rel_l2 = finite_float(row.get("grouped_rel_l2"))
    if rel_l2 is None or rel_l2 > max_rel_l2:
        return False
    vram = finite_float(row.get("guard_max_memory_used_ratio"))
    if vram is not None and vram > max_vram_ratio:
        return False
    return True


def group_key(row: dict[str, Any]) -> tuple[int, int, int, int]:
    return (int(row.get("rows", 0)), int(row.get("cols", 0)), int(row.get("batch", 0)), int(row.get("high_every", 0)))


def compact_config(row: dict[str, Any]) -> dict[str, Any]:
    keys = [
        "rows",
        "cols",
        "batch",
        "high_every",
        "block_m",
        "block_n",
        "block_k",
        "grouped_mixed_ms",
        "torch_fp16_ms",
        "rowwise_mixed_ms",
        "grouped_speedup_vs_torch_fp16",
        "grouped_speedup_vs_rowwise",
        "compression_ratio_vs_fp16",
        "grouped_rel_l2",
        "guard_max_memory_used_ratio",
    ]
    return {key: row.get(key) for key in keys}


def select_configs(rows: list[dict[str, Any]], max_rel_l2: float, max_vram_ratio: float) -> list[dict[str, Any]]:
    groups: dict[tuple[int, int, int, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[group_key(row)].append(row)

    selected: list[dict[str, Any]] = []
    for key, group_rows in sorted(groups.items()):
        eligible = [row for row in group_rows if valid_for_selection(row, max_rel_l2=max_rel_l2, max_vram_ratio=max_vram_ratio)]
        if not eligible:
            rows, cols, batch, high_every = key
            selected.append(
                {
                    "shape": f"{rows}x{cols}",
                    "rows": rows,
                    "cols": cols,
                    "batch": batch,
                    "high_every": high_every,
                    "status": "no_valid_config",
                    "selected": None,
                }
            )
            continue
        best = max(eligible, key=lambda row: finite_float(row.get("grouped_speedup_vs_torch_fp16")) or -1.0)
        fp16_speedup = finite_float(best.get("grouped_speedup_vs_torch_fp16"))
        rowwise_speedup = finite_float(best.get("grouped_speedup_vs_rowwise"))
        rows, cols, batch, high_every = key
        selected.append(
            {
                "shape": f"{rows}x{cols}",
                "rows": rows,
                "cols": cols,
                "batch": batch,
                "high_every": high_every,
                "status": "fp16_win" if fp16_speedup is not None and fp16_speedup > 1.0 else "fallback_best_available",
                "beats_fp16": bool(fp16_speedup is not None and fp16_speedup > 1.0),
                "beats_rowwise": bool(rowwise_speedup is not None and rowwise_speedup > 1.0),
                "eligible_configs": len(eligible),
                "selected": compact_config(best),
            }
        )
    return selected


def median(values: list[float]) -> float | None:
    return statistics.median(values) if values else None


def build_result(inputs: list[Path], selected: list[dict[str, Any]], thresholds: dict[str, Any]) -> dict[str, Any]:
    fp16_speedups = [
        value
        for item in selected
        if item.get("selected")
        if (value := finite_float(item["selected"].get("grouped_speedup_vs_torch_fp16"))) is not None
    ]
    rowwise_speedups = [
        value
        for item in selected
        if item.get("selected")
        if (value := finite_float(item["selected"].get("grouped_speedup_vs_rowwise"))) is not None
    ]
    fp16_winning_groups = sum(1 for item in selected if item.get("beats_fp16"))
    rowwise_winning_groups = sum(1 for item in selected if item.get("beats_rowwise"))
    valid_groups = sum(1 for item in selected if item.get("selected"))
    summary = {
        "total_groups": len(selected),
        "valid_groups": valid_groups,
        "fp16_winning_groups": fp16_winning_groups,
        "rowwise_winning_groups": rowwise_winning_groups,
        "selected_fp16_speedup_median": median(fp16_speedups),
        "selected_fp16_speedup_max": max(fp16_speedups) if fp16_speedups else None,
        "selected_rowwise_speedup_median": median(rowwise_speedups),
        "selected_rowwise_speedup_max": max(rowwise_speedups) if rowwise_speedups else None,
    }
    failures = []
    if summary["valid_groups"] < thresholds["min_valid_groups"]:
        failures.append(f"valid groups {summary['valid_groups']} < {thresholds['min_valid_groups']}")
    if summary["fp16_winning_groups"] < thresholds["min_fp16_winning_groups"]:
        failures.append(f"FP16-winning groups {summary['fp16_winning_groups']} < {thresholds['min_fp16_winning_groups']}")
    best = finite_float(summary.get("selected_fp16_speedup_max"))
    if best is None or best < thresholds["min_best_fp16_speedup"]:
        failures.append(f"best selected grouped/FP16 speedup {best} < {thresholds['min_best_fp16_speedup']}")
    return {
        "passed": not failures,
        "inputs": [str(path) for path in inputs],
        "thresholds": thresholds,
        "summary": summary,
        "selected_configs": selected,
        "failures": failures,
    }


def fmt(value: Any, digits: int = 4) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        "# Triton Kernel Config Selector",
        "",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "This selector chooses one grouped packed INT4/INT8 Triton block config per measured shape/batch/high_every group.",
        "It is a deployment-planning artifact for the prototype kernel, not an end-to-end runtime claim.",
        "",
        "## Summary",
        "",
        f"- total groups: {summary['total_groups']}",
        f"- valid groups: {summary['valid_groups']}",
        f"- FP16-winning groups: {summary['fp16_winning_groups']}",
        f"- row-wise-winning groups: {summary['rowwise_winning_groups']}",
        f"- selected grouped/FP16 speedup median: {fmt(summary['selected_fp16_speedup_median'])}",
        f"- selected grouped/FP16 speedup max: {fmt(summary['selected_fp16_speedup_max'])}",
        f"- selected grouped/row-wise speedup median: {fmt(summary['selected_rowwise_speedup_median'])}",
        f"- selected grouped/row-wise speedup max: {fmt(summary['selected_rowwise_speedup_max'])}",
        "",
        "## Selected Configs",
        "",
        "| shape | batch | high_every | status | BM | BN | BK | grouped/FP16 | grouped/row-wise | rel-L2 | VRAM ratio |",
        "|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in result["selected_configs"]:
        selected = item.get("selected") or {}
        lines.append(
            f"| {item['shape']} | {item['batch']} | {item['high_every']} | {item['status']} | "
            f"{selected.get('block_m', 'n/a')} | {selected.get('block_n', 'n/a')} | {selected.get('block_k', 'n/a')} | "
            f"{fmt(selected.get('grouped_speedup_vs_torch_fp16'))} | {fmt(selected.get('grouped_speedup_vs_rowwise'))} | "
            f"{fmt(selected.get('grouped_rel_l2'))} | {fmt(selected.get('guard_max_memory_used_ratio'))} |"
        )
    lines.extend(["", "## Failures", ""])
    if result["failures"]:
        lines.extend(f"- {failure}" for failure in result["failures"])
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "- Valid claim: the measured tuning sweep can be converted into a deterministic per-shape kernel config policy.",
            "- Invalid claim: unmeasured shapes, mobile kernels, or end-to-end LLM acceleration are covered by this selector.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Select per-shape Triton kernel configs from tuning JSONL evidence.")
    parser.add_argument("--input", action="append", type=Path, required=True, help="Path to tuning_results.jsonl; repeatable.")
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/triton_kernel_config_selector.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/TRITON_KERNEL_CONFIG_SELECTOR.md"))
    parser.add_argument("--max-rel-l2", type=float, default=0.20)
    parser.add_argument("--max-vram-ratio", type=float, default=0.90)
    parser.add_argument("--min-valid-groups", type=int, default=1)
    parser.add_argument("--min-fp16-winning-groups", type=int, default=1)
    parser.add_argument("--min-best-fp16-speedup", type=float, default=1.05)
    args = parser.parse_args()

    rows: list[dict[str, Any]] = []
    for path in args.input:
        rows.extend(load_jsonl(path))
    selected = select_configs(rows, max_rel_l2=args.max_rel_l2, max_vram_ratio=args.max_vram_ratio)
    thresholds = {
        "max_rel_l2": args.max_rel_l2,
        "max_vram_ratio": args.max_vram_ratio,
        "min_valid_groups": args.min_valid_groups,
        "min_fp16_winning_groups": args.min_fp16_winning_groups,
        "min_best_fp16_speedup": args.min_best_fp16_speedup,
    }
    result = build_result(args.input, selected, thresholds)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "failures": result["failures"], "out_json": str(args.out_json)}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
