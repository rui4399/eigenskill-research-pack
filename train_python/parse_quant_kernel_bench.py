#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_rows(text: str) -> list[dict]:
    rows: list[dict] = []
    for line in text.splitlines():
        parts = line.split()
        if len(parts) != 11:
            continue
        if not parts[0].isdigit():
            continue
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
    return rows


def summarize(rows: list[dict]) -> dict:
    best_selected = max(rows, key=lambda row: row["selected_speedup"])
    best_scalar = max(rows, key=lambda row: row["scalar_speedup"])
    int4_faster = [row for row in rows if row["int4_speedup"] > 1.0]
    return {
        "rows": len(rows),
        "best_selected_speedup": best_selected,
        "best_scalar_speedup": best_scalar,
        "int4_faster_than_dense_cases": len(int4_faster),
        "int4_all_cases_slower_than_dense": len(int4_faster) == 0,
        "max_int4_rel_l2": max(row["int4_rel_l2"] for row in rows),
        "max_selected_rel_l2": max(row["selected_rel_l2"] for row in rows),
    }


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
