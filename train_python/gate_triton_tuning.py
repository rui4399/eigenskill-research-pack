#!/usr/bin/env python3
from __future__ import annotations

"""Gate Triton mixed-GEMM tuning evidence.

The tuner emits one JSON object per kernel configuration. This script turns
that raw sweep into a repeatable evidence gate so a positive result is not just
a hand-picked markdown table.
"""

import argparse
import json
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


def valid_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [row for row in rows if row.get("returncode") == 0 and finite_float(row.get("grouped_mixed_ms")) is not None]


def best_by(rows: list[dict[str, Any]], key: str) -> dict[str, Any] | None:
    valid = [(finite_float(row.get(key)), row) for row in rows]
    valid = [(score, row) for score, row in valid if score is not None]
    if not valid:
        return None
    return max(valid, key=lambda item: item[0])[1]


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    valid = valid_rows(rows)
    fp16_speedups = [value for row in valid if (value := finite_float(row.get("grouped_speedup_vs_torch_fp16"))) is not None]
    rowwise_speedups = [value for row in valid if (value := finite_float(row.get("grouped_speedup_vs_rowwise"))) is not None]
    rel_l2_values = [value for row in valid if (value := finite_float(row.get("grouped_rel_l2"))) is not None]
    vram_ratios = [value for row in valid if (value := finite_float(row.get("guard_max_memory_used_ratio"))) is not None]
    compression_values = [value for row in valid if (value := finite_float(row.get("compression_ratio_vs_fp16"))) is not None]
    return {
        "total_configs": len(rows),
        "valid_configs": len(valid),
        "failed_configs": len(rows) - len(valid),
        "fp16_wins": sum(1 for value in fp16_speedups if value > 1.0),
        "rowwise_wins": sum(1 for value in rowwise_speedups if value > 1.0),
        "best_fp16_speedup": max(fp16_speedups) if fp16_speedups else None,
        "best_rowwise_speedup": max(rowwise_speedups) if rowwise_speedups else None,
        "max_rel_l2": max(rel_l2_values) if rel_l2_values else None,
        "max_guard_vram_ratio": max(vram_ratios) if vram_ratios else None,
        "best_compression_vs_fp16": max(compression_values) if compression_values else None,
        "best_fp16_config": best_by(valid, "grouped_speedup_vs_torch_fp16"),
        "best_rowwise_config": best_by(valid, "grouped_speedup_vs_rowwise"),
    }


def check_gate(summary: dict[str, Any], args: argparse.Namespace) -> list[str]:
    failures: list[str] = []
    if summary["valid_configs"] < args.min_valid_configs:
        failures.append(f"valid configs {summary['valid_configs']} < {args.min_valid_configs}")
    if summary["fp16_wins"] < args.min_fp16_wins:
        failures.append(f"FP16 wins {summary['fp16_wins']} < {args.min_fp16_wins}")
    best_fp16 = finite_float(summary.get("best_fp16_speedup"))
    if best_fp16 is None or best_fp16 < args.min_best_fp16_speedup:
        failures.append(f"best grouped/FP16 speedup {best_fp16} < {args.min_best_fp16_speedup}")
    if summary["rowwise_wins"] < args.min_rowwise_wins:
        failures.append(f"row-wise wins {summary['rowwise_wins']} < {args.min_rowwise_wins}")
    max_rel_l2 = finite_float(summary.get("max_rel_l2"))
    if max_rel_l2 is None or max_rel_l2 > args.max_rel_l2:
        failures.append(f"max grouped rel-L2 {max_rel_l2} > {args.max_rel_l2}")
    max_vram = finite_float(summary.get("max_guard_vram_ratio"))
    if max_vram is None or max_vram > args.max_vram_ratio:
        failures.append(f"max guard VRAM ratio {max_vram} > {args.max_vram_ratio}")
    return failures


def compact_config(row: dict[str, Any] | None) -> dict[str, Any] | None:
    if row is None:
        return None
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


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    status = "PASS" if result["passed"] else "FAIL"
    lines = [
        "# Triton Mixed-GEMM Evidence Gate",
        "",
        f"Status: **{status}**",
        "",
        "This gate evaluates packed INT4/INT8 Triton kernel tuning outputs. It is not an end-to-end LLM runtime claim.",
        "",
        "## Thresholds",
        "",
        f"- minimum valid configs: {result['thresholds']['min_valid_configs']}",
        f"- minimum FP16 wins: {result['thresholds']['min_fp16_wins']}",
        f"- minimum best grouped/FP16 speedup: {result['thresholds']['min_best_fp16_speedup']}",
        f"- minimum row-wise wins: {result['thresholds']['min_rowwise_wins']}",
        f"- maximum grouped rel-L2: {result['thresholds']['max_rel_l2']}",
        f"- maximum guard VRAM ratio: {result['thresholds']['max_vram_ratio']}",
        "",
        "## Observed",
        "",
        f"- total configs: {summary['total_configs']}",
        f"- valid configs: {summary['valid_configs']}",
        f"- FP16 wins: {summary['fp16_wins']}",
        f"- row-wise wins: {summary['rowwise_wins']}",
        f"- best grouped/FP16 speedup: {summary['best_fp16_speedup']}",
        f"- best grouped/row-wise speedup: {summary['best_rowwise_speedup']}",
        f"- best compression vs FP16: {summary['best_compression_vs_fp16']}",
        f"- max grouped rel-L2: {summary['max_rel_l2']}",
        f"- max guard VRAM ratio: {summary['max_guard_vram_ratio']}",
        "",
        "## Best FP16-Winning Config",
        "",
        "```json",
        json.dumps(compact_config(summary.get("best_fp16_config")), ensure_ascii=False, indent=2),
        "```",
        "",
        "## Failures",
        "",
    ]
    if result["failures"]:
        lines.extend(f"- {failure}" for failure in result["failures"])
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Triton tuning evidence against explicit thresholds.")
    parser.add_argument("--input", type=Path, required=True, help="Path to tuning_results.jsonl.")
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/triton_tuning_gate.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/TRITON_TUNING_GATE.md"))
    parser.add_argument("--min-valid-configs", type=int, default=8)
    parser.add_argument("--min-fp16-wins", type=int, default=1)
    parser.add_argument("--min-best-fp16-speedup", type=float, default=1.05)
    parser.add_argument("--min-rowwise-wins", type=int, default=1)
    parser.add_argument("--max-rel-l2", type=float, default=0.20)
    parser.add_argument("--max-vram-ratio", type=float, default=0.90)
    args = parser.parse_args()

    summary = summarize(load_jsonl(args.input))
    failures = check_gate(summary, args)
    result = {
        "passed": not failures,
        "input": str(args.input),
        "thresholds": {
            "min_valid_configs": args.min_valid_configs,
            "min_fp16_wins": args.min_fp16_wins,
            "min_best_fp16_speedup": args.min_best_fp16_speedup,
            "min_rowwise_wins": args.min_rowwise_wins,
            "max_rel_l2": args.max_rel_l2,
            "max_vram_ratio": args.max_vram_ratio,
        },
        "summary": summary,
        "failures": failures,
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "failures": failures, "out_json": str(args.out_json)}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
