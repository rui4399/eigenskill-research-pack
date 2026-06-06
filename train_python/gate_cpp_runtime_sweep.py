#!/usr/bin/env python3
from __future__ import annotations

"""Gate C++ ESMP runtime stratified sweep evidence."""

import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
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


def selected_speedup(row: dict[str, Any]) -> float | None:
    for key in ("selected_speedup_vs_full", "selected_speedup_vs_full_mixed_gemv"):
        value = finite_float(row.get(key))
        if value is not None:
            return value
    return None


def ok_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [row for row in rows if row.get("ok") or row.get("returncode") == 0]


def median(values: list[float]) -> float | None:
    return statistics.median(values) if values else None


def grouped_summary(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[str(row.get(key, "unknown"))].append(row)
    out = []
    for name, bucket in sorted(groups.items()):
        speedups = [value for row in bucket if (value := selected_speedup(row)) is not None]
        selected_ms = [value for row in bucket if (value := finite_float(row.get("selected_mixed_gemv_ms"))) is not None]
        full_ms = [value for row in bucket if (value := finite_float(row.get("full_mixed_gemv_ms"))) is not None]
        compression = [value for row in bucket if (value := finite_float(row.get("compression_ratio_vs_fp32"))) is not None]
        out.append(
            {
                key: name,
                "count": len(bucket),
                "median_selected_speedup_vs_full": median(speedups),
                "min_selected_speedup_vs_full": min(speedups) if speedups else None,
                "median_selected_ms": median(selected_ms),
                "median_full_ms": median(full_ms),
                "median_compression_vs_fp32": median(compression),
            }
        )
    return out


def build_result(rows: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    ok = ok_rows(rows)
    failed = [row for row in rows if row not in ok]
    speedups = [value for row in ok if (value := selected_speedup(row)) is not None]
    selected_ms = [value for row in ok if (value := finite_float(row.get("selected_mixed_gemv_ms"))) is not None]
    compression = [value for row in ok if (value := finite_float(row.get("compression_ratio_vs_fp32"))) is not None]
    wins = sum(1 for value in speedups if value > 1.0)
    summary = {
        "total_rows": len(rows),
        "ok_rows": len(ok),
        "failed_rows": len(failed),
        "wins_vs_full": wins,
        "median_selected_speedup_vs_full": median(speedups),
        "min_selected_speedup_vs_full": min(speedups) if speedups else None,
        "max_selected_speedup_vs_full": max(speedups) if speedups else None,
        "median_selected_ms": median(selected_ms),
        "median_compression_vs_fp32": median(compression),
    }
    failures = []
    if summary["ok_rows"] < args.min_ok_rows:
        failures.append(f"ok rows {summary['ok_rows']} < {args.min_ok_rows}")
    if summary["failed_rows"] > args.max_failed_rows:
        failures.append(f"failed rows {summary['failed_rows']} > {args.max_failed_rows}")
    if wins < args.min_wins_vs_full:
        failures.append(f"wins vs full {wins} < {args.min_wins_vs_full}")
    min_speedup = finite_float(summary["min_selected_speedup_vs_full"])
    if min_speedup is None or min_speedup < args.min_min_speedup_vs_full:
        failures.append(f"min selected/full speedup {min_speedup} < {args.min_min_speedup_vs_full}")
    median_speedup = finite_float(summary["median_selected_speedup_vs_full"])
    if median_speedup is None or median_speedup < args.min_median_speedup_vs_full:
        failures.append(f"median selected/full speedup {median_speedup} < {args.min_median_speedup_vs_full}")
    best_speedup = finite_float(summary["max_selected_speedup_vs_full"])
    if best_speedup is None or best_speedup < args.min_best_speedup_vs_full:
        failures.append(f"best selected/full speedup {best_speedup} < {args.min_best_speedup_vs_full}")
    median_selected_ms = finite_float(summary["median_selected_ms"])
    if median_selected_ms is None or median_selected_ms > args.max_median_selected_ms:
        failures.append(f"median selected ms {median_selected_ms} > {args.max_median_selected_ms}")
    median_compression = finite_float(summary["median_compression_vs_fp32"])
    if median_compression is None or median_compression < args.min_median_compression_vs_fp32:
        failures.append(f"median compression {median_compression} < {args.min_median_compression_vs_fp32}")
    return {
        "passed": not failures,
        "failures": failures,
        "summary": summary,
        "by_family": grouped_summary(ok, "family"),
        "by_layer_bucket": grouped_summary(ok, "layer_bucket"),
        "thresholds": {
            "min_ok_rows": args.min_ok_rows,
            "max_failed_rows": args.max_failed_rows,
            "min_wins_vs_full": args.min_wins_vs_full,
            "min_min_speedup_vs_full": args.min_min_speedup_vs_full,
            "min_median_speedup_vs_full": args.min_median_speedup_vs_full,
            "min_best_speedup_vs_full": args.min_best_speedup_vs_full,
            "max_median_selected_ms": args.max_median_selected_ms,
            "min_median_compression_vs_fp32": args.min_median_compression_vs_fp32,
        },
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
        "# C++ ESMP Runtime Sweep Gate",
        "",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- total rows: {summary['total_rows']}",
        f"- ok rows: {summary['ok_rows']}",
        f"- failed rows: {summary['failed_rows']}",
        f"- wins vs full mixed GEMV: {summary['wins_vs_full']}",
        f"- min selected/full speedup: {fmt(summary['min_selected_speedup_vs_full'])}",
        f"- median selected/full speedup: {fmt(summary['median_selected_speedup_vs_full'])}",
        f"- best selected/full speedup: {fmt(summary['max_selected_speedup_vs_full'])}",
        f"- median selected ms: {fmt(summary['median_selected_ms'], 6)}",
        f"- median compression vs FP32: {fmt(summary['median_compression_vs_fp32'])}x",
        "",
        "## By Family",
        "",
        "| family | count | median speedup | min speedup | median selected ms | median compression |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for item in result["by_family"]:
        lines.append(
            f"| `{item['family']}` | {item['count']} | {fmt(item['median_selected_speedup_vs_full'])} | "
            f"{fmt(item['min_selected_speedup_vs_full'])} | {fmt(item['median_selected_ms'], 6)} | "
            f"{fmt(item['median_compression_vs_fp32'])}x |"
        )
    lines.extend(["", "## By Layer Bucket", "", "| bucket | count | median speedup | min speedup | median selected ms | median compression |", "|---|---:|---:|---:|---:|---:|"])
    for item in result["by_layer_bucket"]:
        lines.append(
            f"| `{item['layer_bucket']}` | {item['count']} | {fmt(item['median_selected_speedup_vs_full'])} | "
            f"{fmt(item['min_selected_speedup_vs_full'])} | {fmt(item['median_selected_ms'], 6)} | "
            f"{fmt(item['median_compression_vs_fp32'])}x |"
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
            "- Valid claim: the C++ ESMP runtime has gated module-level selected-row speedup evidence.",
            "- Invalid claim: this alone proves full LLM end-to-end acceleration.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate C++ ESMP runtime stratified sweep JSONL.")
    parser.add_argument("--input-jsonl", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/cpp_runtime_sweep_gate.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/CPP_RUNTIME_SWEEP_GATE.md"))
    parser.add_argument("--min-ok-rows", type=int, default=1)
    parser.add_argument("--max-failed-rows", type=int, default=0)
    parser.add_argument("--min-wins-vs-full", type=int, default=1)
    parser.add_argument("--min-min-speedup-vs-full", type=float, default=1.05)
    parser.add_argument("--min-median-speedup-vs-full", type=float, default=1.05)
    parser.add_argument("--min-best-speedup-vs-full", type=float, default=1.05)
    parser.add_argument("--max-median-selected-ms", type=float, default=10.0)
    parser.add_argument("--min-median-compression-vs-fp32", type=float, default=1.0)
    args = parser.parse_args()

    result = build_result(load_jsonl(args.input_jsonl), args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "failures": result["failures"], "out_json": str(args.out_json)}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
