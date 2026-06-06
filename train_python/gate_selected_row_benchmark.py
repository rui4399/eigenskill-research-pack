#!/usr/bin/env python3
from __future__ import annotations

"""Gate selected-row ESMP benchmark evidence."""

import argparse
import json
import statistics
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


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


def speedup_vs_full(row: dict[str, Any]) -> float | None:
    for key in ("speedup_vs_dense_full", "speedup_vs_full_concat", "speedup_vs_dense_full_concat"):
        value = finite_float(row.get(key))
        if value is not None:
            return value
    return None


def rel_l2(row: dict[str, Any]) -> float | None:
    for key in ("rel_l2_vs_dense_selected", "rel_l2"):
        value = finite_float(row.get(key))
        if value is not None:
            return value
    return None


def runtime_rows(rows: list[dict[str, Any]], runtime: str) -> list[dict[str, Any]]:
    return [row for row in rows if row.get("ok") and row.get("runtime") == runtime]


def runtime_summary(rows: list[dict[str, Any]], runtime: str) -> dict[str, Any]:
    bucket = runtime_rows(rows, runtime)
    speedups = [value for row in bucket if (value := speedup_vs_full(row)) is not None]
    rels = [value for row in bucket if (value := rel_l2(row)) is not None]
    return {
        "runtime": runtime,
        "cases": len(bucket),
        "wins_vs_full": sum(1 for value in speedups if value > 1.0),
        "median_speedup_vs_full": statistics.median(speedups) if speedups else None,
        "best_speedup_vs_full": max(speedups) if speedups else None,
        "max_rel_l2": max(rels) if rels else None,
    }


def check_guard(guard: dict[str, Any] | None, args: argparse.Namespace) -> list[str]:
    if guard is None:
        return []
    failures: list[str] = []
    if int(guard.get("returncode", -1)) != 0:
        failures.append(f"guarded command returncode {guard.get('returncode')} != 0")
    if guard.get("killed_by_guard"):
        failures.append("guard killed command for memory")
    if guard.get("killed_by_timeout"):
        failures.append("guard killed command for timeout")
    ratio = finite_float(guard.get("max_memory_used_ratio"))
    if ratio is None:
        failures.append("guard missing max_memory_used_ratio")
    elif ratio > args.max_memory_ratio:
        failures.append(f"guard max memory ratio {ratio:.4f} > {args.max_memory_ratio:.4f}")
    return failures


def build_result(benchmark: dict[str, Any], guard: dict[str, Any] | None, args: argparse.Namespace) -> dict[str, Any]:
    rows = benchmark.get("rows", [])
    ok_rows = [row for row in rows if row.get("ok")]
    failures = []
    failed_rows = [row for row in rows if not row.get("ok")]
    if len(ok_rows) < args.min_ok_rows:
        failures.append(f"ok rows {len(ok_rows)} < {args.min_ok_rows}")
    if len(failed_rows) > args.max_failed_rows:
        failures.append(f"failed rows {len(failed_rows)} > {args.max_failed_rows}")

    packed = runtime_summary(rows, args.packed_runtime)
    cached = runtime_summary(rows, args.cached_runtime)
    dense_selected = runtime_summary(rows, args.dense_selected_runtime)
    summaries = {
        args.packed_runtime: packed,
        args.cached_runtime: cached,
        args.dense_selected_runtime: dense_selected,
    }

    if packed["cases"] < args.min_packed_cases:
        failures.append(f"{args.packed_runtime} cases {packed['cases']} < {args.min_packed_cases}")
    if packed["wins_vs_full"] < args.min_packed_wins_vs_full:
        failures.append(f"{args.packed_runtime} wins {packed['wins_vs_full']} < {args.min_packed_wins_vs_full}")
    best = finite_float(packed["best_speedup_vs_full"])
    if best is None or best < args.min_best_packed_speedup_vs_full:
        failures.append(f"{args.packed_runtime} best speedup {best} < {args.min_best_packed_speedup_vs_full}")
    max_rel = finite_float(packed["max_rel_l2"])
    if max_rel is None or max_rel > args.max_rel_l2:
        failures.append(f"{args.packed_runtime} max rel-L2 {max_rel} > {args.max_rel_l2}")

    cached_median = finite_float(cached["median_speedup_vs_full"])
    if cached_median is None or cached_median < args.min_cached_median_speedup_vs_full:
        failures.append(f"{args.cached_runtime} median speedup {cached_median} < {args.min_cached_median_speedup_vs_full}")
    dense_selected_wins = int(dense_selected["wins_vs_full"])
    if dense_selected_wins < args.min_dense_selected_wins_vs_full:
        failures.append(f"{args.dense_selected_runtime} wins {dense_selected_wins} < {args.min_dense_selected_wins_vs_full}")

    failures.extend(check_guard(guard, args))
    return {
        "passed": not failures,
        "failures": failures,
        "summary": {
            "model": benchmark.get("model"),
            "module_count": benchmark.get("module_count"),
            "batches": benchmark.get("batches"),
            "selected_rows": benchmark.get("selected_rows"),
            "ok_rows": len(ok_rows),
            "failed_rows": len(failed_rows),
            "guard_max_memory_used_ratio": None if guard is None else guard.get("max_memory_used_ratio"),
            "guard_max_memory_used_mib": None if guard is None else guard.get("max_memory_used_mib"),
            "guard_memory_total_mib": None if guard is None else guard.get("memory_total_mib"),
        },
        "runtime_summaries": summaries,
        "thresholds": {
            "min_ok_rows": args.min_ok_rows,
            "max_failed_rows": args.max_failed_rows,
            "packed_runtime": args.packed_runtime,
            "min_packed_cases": args.min_packed_cases,
            "min_packed_wins_vs_full": args.min_packed_wins_vs_full,
            "min_best_packed_speedup_vs_full": args.min_best_packed_speedup_vs_full,
            "max_rel_l2": args.max_rel_l2,
            "cached_runtime": args.cached_runtime,
            "min_cached_median_speedup_vs_full": args.min_cached_median_speedup_vs_full,
            "dense_selected_runtime": args.dense_selected_runtime,
            "min_dense_selected_wins_vs_full": args.min_dense_selected_wins_vs_full,
            "max_memory_ratio": args.max_memory_ratio,
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
        "# Selected-Row Benchmark Gate",
        "",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- model: `{summary['model']}`",
        f"- modules: {summary['module_count']}",
        f"- batches: `{summary['batches']}`",
        f"- selected rows: `{summary['selected_rows']}`",
        f"- ok rows: {summary['ok_rows']}",
        f"- failed rows: {summary['failed_rows']}",
        f"- guard peak memory: {summary['guard_max_memory_used_mib']} / {summary['guard_memory_total_mib']} MiB ({fmt(summary['guard_max_memory_used_ratio'])})",
        "",
        "## Runtime Summaries",
        "",
        "| runtime | cases | wins vs full | median speedup vs full | best speedup vs full | max rel-L2 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for item in result["runtime_summaries"].values():
        lines.append(
            f"| `{item['runtime']}` | {item['cases']} | {item['wins_vs_full']} | "
            f"{fmt(item['median_speedup_vs_full'])} | {fmt(item['best_speedup_vs_full'])} | {fmt(item['max_rel_l2'])} |"
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
            "- Valid claim: selected-row routing has gated module-level evidence under the configured thresholds.",
            "- Invalid claim: this alone proves end-to-end token latency acceleration.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate selected-row ESMP benchmark evidence.")
    parser.add_argument("--benchmark-json", type=Path, required=True)
    parser.add_argument("--guard-json", type=Path, default=None)
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/selected_row_benchmark_gate.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/SELECTED_ROW_BENCHMARK_GATE.md"))
    parser.add_argument("--packed-runtime", default="triton_selected")
    parser.add_argument("--cached-runtime", default="cached_selected")
    parser.add_argument("--dense-selected-runtime", default="dense_selected")
    parser.add_argument("--min-ok-rows", type=int, default=1)
    parser.add_argument("--max-failed-rows", type=int, default=0)
    parser.add_argument("--min-packed-cases", type=int, default=1)
    parser.add_argument("--min-packed-wins-vs-full", type=int, default=1)
    parser.add_argument("--min-best-packed-speedup-vs-full", type=float, default=1.05)
    parser.add_argument("--max-rel-l2", type=float, default=0.25)
    parser.add_argument("--min-cached-median-speedup-vs-full", type=float, default=1.0)
    parser.add_argument("--min-dense-selected-wins-vs-full", type=int, default=1)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    args = parser.parse_args()

    guard = load_json(args.guard_json) if args.guard_json else None
    result = build_result(load_json(args.benchmark_json), guard, args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "failures": result["failures"], "out_json": str(args.out_json)}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
