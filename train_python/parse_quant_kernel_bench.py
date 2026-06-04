#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_rows(text: str) -> list[dict]:
    rows: list[dict] = []
    for line in text.splitlines():
        parts = line.split()
        if not parts:
            continue
        if not parts[0].isdigit():
            continue
        if len(parts) == 11:
            rows.append(
                {
                    "d": int(parts[0]),
                    "active_rows": int(parts[1]),
                    "dense_ms": float(parts[2]),
                    "int4_ms": float(parts[3]),
                    "selected_ms": float(parts[4]),
                    "scalar_ms": float(parts[5]),
                    "int4_speedup": float(parts[6]),
                    "selected_speedup": float(parts[7]),
                    "scalar_speedup": float(parts[8]),
                    "int4_rel_l2": float(parts[9]),
                    "selected_rel_l2": float(parts[10]),
                }
            )
        elif len(parts) == 17:
            rows.append(
                {
                    "d": int(parts[0]),
                    "active_rows": int(parts[1]),
                    "dense_ms": float(parts[2]),
                    "dense_avx2_ms": float(parts[3]),
                    "int4_ms": float(parts[4]),
                    "selected_ms": float(parts[5]),
                    "selected_avx2_ms": float(parts[6]),
                    "scalar_ms": float(parts[7]),
                    "dense_avx2_speedup": float(parts[8]),
                    "int4_speedup": float(parts[9]),
                    "selected_speedup": float(parts[10]),
                    "selected_avx2_speedup": float(parts[11]),
                    "scalar_speedup": float(parts[12]),
                    "dense_avx2_rel_l2": float(parts[13]),
                    "int4_rel_l2": float(parts[14]),
                    "selected_rel_l2": float(parts[15]),
                    "selected_avx2_rel_l2": float(parts[16]),
                }
            )
        elif len(parts) == 20:
            rows.append(
                {
                    "d": int(parts[0]),
                    "active_rows": int(parts[1]),
                    "dense_ms": float(parts[2]),
                    "dense_avx2_ms": float(parts[3]),
                    "int4_ms": float(parts[4]),
                    "int3_ms": float(parts[5]),
                    "selected_ms": float(parts[6]),
                    "selected_avx2_ms": float(parts[7]),
                    "scalar_ms": float(parts[8]),
                    "dense_avx2_speedup": float(parts[9]),
                    "int4_speedup": float(parts[10]),
                    "int3_speedup": float(parts[11]),
                    "selected_speedup": float(parts[12]),
                    "selected_avx2_speedup": float(parts[13]),
                    "scalar_speedup": float(parts[14]),
                    "dense_avx2_rel_l2": float(parts[15]),
                    "int4_rel_l2": float(parts[16]),
                    "int3_rel_l2": float(parts[17]),
                    "selected_rel_l2": float(parts[18]),
                    "selected_avx2_rel_l2": float(parts[19]),
                }
            )
        elif len(parts) == 26:
            rows.append(
                {
                    "d": int(parts[0]),
                    "active_rows": int(parts[1]),
                    "dense_ms": float(parts[2]),
                    "dense_avx2_ms": float(parts[3]),
                    "int4_ms": float(parts[4]),
                    "int3_ms": float(parts[5]),
                    "mixed_ms": float(parts[6]),
                    "selected_ms": float(parts[7]),
                    "selected_avx2_ms": float(parts[8]),
                    "mixed_selected_ms": float(parts[9]),
                    "scalar_ms": float(parts[10]),
                    "dense_avx2_speedup": float(parts[11]),
                    "int4_speedup": float(parts[12]),
                    "int3_speedup": float(parts[13]),
                    "mixed_speedup": float(parts[14]),
                    "selected_speedup": float(parts[15]),
                    "selected_avx2_speedup": float(parts[16]),
                    "mixed_selected_speedup": float(parts[17]),
                    "scalar_speedup": float(parts[18]),
                    "dense_avx2_rel_l2": float(parts[19]),
                    "int4_rel_l2": float(parts[20]),
                    "int3_rel_l2": float(parts[21]),
                    "mixed_rel_l2": float(parts[22]),
                    "selected_rel_l2": float(parts[23]),
                    "selected_avx2_rel_l2": float(parts[24]),
                    "mixed_selected_rel_l2": float(parts[25]),
                }
            )
    return rows


def summarize(rows: list[dict]) -> dict:
    best_selected = max(rows, key=lambda row: row["selected_speedup"])
    best_selected_avx2 = max(rows, key=lambda row: row.get("selected_avx2_speedup", row["selected_speedup"]))
    best_dense_avx2 = max(rows, key=lambda row: row.get("dense_avx2_speedup", 1.0))
    best_scalar = max(rows, key=lambda row: row["scalar_speedup"])
    int4_faster = [row for row in rows if row["int4_speedup"] > 1.0]
    mixed_faster = [row for row in rows if row.get("mixed_speedup", 0.0) > 1.0]
    mixed_selected_faster = [row for row in rows if row.get("mixed_selected_speedup", 0.0) > 1.0]
    summary = {
        "rows": len(rows),
        "best_selected_speedup": best_selected,
        "best_selected_avx2_speedup": best_selected_avx2,
        "best_dense_avx2_speedup": best_dense_avx2,
        "best_scalar_speedup": best_scalar,
        "int4_faster_than_dense_cases": len(int4_faster),
        "int4_all_cases_slower_than_dense": len(int4_faster) == 0,
        "mixed_faster_than_dense_cases": len(mixed_faster),
        "mixed_selected_faster_than_dense_cases": len(mixed_selected_faster),
        "max_int4_rel_l2": max(row["int4_rel_l2"] for row in rows),
        "max_selected_rel_l2": max(row["selected_rel_l2"] for row in rows),
    }
    if "dense_avx2_rel_l2" in rows[0]:
        summary["max_dense_avx2_rel_l2"] = max(row["dense_avx2_rel_l2"] for row in rows)
        summary["max_selected_avx2_rel_l2"] = max(row["selected_avx2_rel_l2"] for row in rows)
    if "mixed_rel_l2" in rows[0]:
        best_mixed = max(rows, key=lambda row: row["mixed_speedup"])
        best_mixed_selected = max(rows, key=lambda row: row["mixed_selected_speedup"])
        summary["best_mixed_speedup"] = best_mixed
        summary["best_mixed_selected_speedup"] = best_mixed_selected
        summary["max_mixed_rel_l2"] = max(row["mixed_rel_l2"] for row in rows)
        summary["max_mixed_selected_rel_l2"] = max(row["mixed_selected_rel_l2"] for row in rows)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/eigenskill_quant_kernel_benchmark.txt")
    parser.add_argument("--out", default="outputs/eigenskill_quant_kernel_benchmark_summary.json")
    args = parser.parse_args()

    rows = parse_rows(Path(args.input).read_text(encoding="utf-8"))
    output = {
        "input": args.input,
        "benchmark": "quant_kernel_bench",
        "rows": rows,
        "summary": summarize(rows),
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"out": str(out), "summary": output["summary"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
