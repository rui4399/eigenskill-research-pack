#!/usr/bin/env python3
from __future__ import annotations

"""Gate RTX 5070 W4A8-style Triton shape-family evidence.

This gate turns the delayed-dequantization Triton sweep into a machine-checkable
claim boundary. It is intentionally narrow: it checks kernel-level speed,
weight-payload compression, activation-quantization drift, and GPU guard memory
for committed JSONL sweep artifacts. It does not claim model quality retention.
"""

import argparse
import json
from pathlib import Path
from statistics import median
from typing import Any


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
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


def values(rows: list[dict[str, Any]], key: str) -> list[float]:
    out: list[float] = []
    for row in rows:
        value = finite_float(row.get(key))
        if value is not None:
            out.append(value)
    return out


def summarize(rows: list[dict[str, Any]], key: str) -> dict[str, float | None]:
    vals = values(rows, key)
    if not vals:
        return {"min": None, "median": None, "max": None}
    return {"min": min(vals), "median": median(vals), "max": max(vals)}


def build_result(rows: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    valid = [row for row in rows if int(row.get("returncode", -1)) == 0 and not row.get("guard_killed")]
    packed_speedups = values(valid, "int4_packed_x_i8_speedup_vs_torch_fp16")
    unpacked_speedups = values(valid, "int4_unpacked_i8_x_i8_speedup_vs_torch_fp16")
    compression = values(valid, "compression_ratio_vs_fp16")
    added_drift = values(valid, "int4_packed_x_i8_vs_w4a16_rel_l2")
    guard_ratios = values(valid, "guard_max_memory_used_ratio")
    packed_vs_w4a16 = values(valid, "int4_packed_x_i8_speedup_vs_packed_w4a16")

    failures: list[str] = []
    if len(valid) < args.min_configs:
        failures.append(f"valid configs {len(valid)} < {args.min_configs}")
    if len(packed_speedups) != len(valid):
        failures.append("some valid configs are missing packed W4xI8 speedups")
    if packed_speedups and min(packed_speedups) < args.min_packed_speedup:
        failures.append(f"min packed W4xI8 speedup {min(packed_speedups):.4f} < {args.min_packed_speedup:.4f}")
    if compression and min(compression) < args.min_compression:
        failures.append(f"min compression {min(compression):.4f} < {args.min_compression:.4f}")
    if added_drift and max(added_drift) > args.max_added_rel_l2:
        failures.append(f"max added rel-L2 {max(added_drift):.6f} > {args.max_added_rel_l2:.6f}")
    if guard_ratios and max(guard_ratios) > args.max_memory_ratio:
        failures.append(f"max guard memory ratio {max(guard_ratios):.4f} > {args.max_memory_ratio:.4f}")

    return {
        "passed": not failures,
        "failures": failures,
        "summary": {
            "total_configs": len(rows),
            "valid_configs": len(valid),
            "packed_w4_x_i8_speedup_vs_fp16": summarize(valid, "int4_packed_x_i8_speedup_vs_torch_fp16"),
            "w4_as_i8_x_i8_speedup_vs_fp16": summarize(valid, "int4_unpacked_i8_x_i8_speedup_vs_torch_fp16"),
            "packed_w4_x_i8_speedup_vs_w4a16": summarize(valid, "int4_packed_x_i8_speedup_vs_packed_w4a16"),
            "weight_payload_compression_vs_fp16": summarize(valid, "compression_ratio_vs_fp16"),
            "activation_added_rel_l2_vs_w4a16": summarize(valid, "int4_packed_x_i8_vs_w4a16_rel_l2"),
            "guard_peak_memory_ratio": summarize(valid, "guard_max_memory_used_ratio"),
            "all_packed_configs_beat_fp16": bool(packed_speedups) and min(packed_speedups) >= args.min_packed_speedup,
            "all_unpacked_configs_beat_fp16": bool(unpacked_speedups) and min(unpacked_speedups) >= args.min_packed_speedup,
            "all_packed_configs_beat_w4a16": bool(packed_vs_w4a16) and min(packed_vs_w4a16) >= args.min_packed_vs_w4a16_speedup,
        },
        "thresholds": {
            "min_configs": args.min_configs,
            "min_packed_speedup": args.min_packed_speedup,
            "min_packed_vs_w4a16_speedup": args.min_packed_vs_w4a16_speedup,
            "min_compression": args.min_compression,
            "max_added_rel_l2": args.max_added_rel_l2,
            "max_memory_ratio": args.max_memory_ratio,
        },
    }


def fmt(value: Any, digits: int = 4) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def stat_cell(stats: dict[str, Any]) -> str:
    return f"{fmt(stats.get('min'))} / {fmt(stats.get('median'))} / {fmt(stats.get('max'))}"


def write_markdown(path: Path, result: dict[str, Any], source: Path) -> None:
    summary = result["summary"]
    lines = [
        "# W4A8 Shape-Family Gate",
        "",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Source",
        "",
        f"- JSONL: `{source.as_posix()}`",
        "",
        "## Summary",
        "",
        f"- valid configs: `{summary['valid_configs']}/{summary['total_configs']}`",
        f"- all packed W4 x INT8 configs beat FP16: `{summary['all_packed_configs_beat_fp16']}`",
        f"- all W4-as-I8 x INT8 configs beat FP16: `{summary['all_unpacked_configs_beat_fp16']}`",
        f"- all packed W4 x INT8 configs beat packed W4A16: `{summary['all_packed_configs_beat_w4a16']}`",
        "",
        "| metric | min / median / max |",
        "|---|---:|",
        f"| packed W4 x INT8 speedup vs torch FP16 | {stat_cell(summary['packed_w4_x_i8_speedup_vs_fp16'])} |",
        f"| W4-as-I8 x INT8 speedup vs torch FP16 | {stat_cell(summary['w4_as_i8_x_i8_speedup_vs_fp16'])} |",
        f"| packed W4 x INT8 speedup vs packed W4A16 | {stat_cell(summary['packed_w4_x_i8_speedup_vs_w4a16'])} |",
        f"| weight payload compression vs FP16 | {stat_cell(summary['weight_payload_compression_vs_fp16'])} |",
        f"| activation added rel-L2 vs W4A16 | {stat_cell(summary['activation_added_rel_l2_vs_w4a16'])} |",
        f"| guard peak memory ratio | {stat_cell(summary['guard_peak_memory_ratio'])} |",
        "",
        "## Thresholds",
        "",
    ]
    for key, value in result["thresholds"].items():
        lines.append(f"- {key}: `{value}`")
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
            "Valid claim: the committed RTX 5070 W4A8-style shape-family sweep "
            "passes kernel-level speed, compression, drift, and guard-memory thresholds.",
            "",
            "Invalid claim: this gate does not prove end-to-end LLM speed, mobile "
            "deployment, energy savings, downstream task retention, or SOTA quantization.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate RTX 5070 W4A8-style shape-family evidence.")
    parser.add_argument("--jsonl", type=Path, required=True)
    parser.add_argument("--min-configs", type=int, default=8)
    parser.add_argument("--min-packed-speedup", type=float, default=1.0)
    parser.add_argument("--min-packed-vs-w4a16-speedup", type=float, default=1.0)
    parser.add_argument("--min-compression", type=float, default=3.5)
    parser.add_argument("--max-added-rel-l2", type=float, default=0.02)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    rows = read_jsonl(args.jsonl)
    result = build_result(rows, args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result, args.jsonl)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "failures": result["failures"]}, ensure_ascii=False, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
