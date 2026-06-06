#!/usr/bin/env python3
from __future__ import annotations

"""Run a stratified C++ ESMP runtime sweep over packed Qwen modules."""

import argparse
import csv
import json
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any


DEFAULT_LAYERS = [0, 1, 7, 13, 20, 27]
DEFAULT_MODULES = [
    "self_attn__q_proj",
    "self_attn__k_proj",
    "self_attn__v_proj",
    "self_attn__o_proj",
    "mlp__gate_proj",
    "mlp__up_proj",
    "mlp__down_proj",
]


def parse_csv_ints(text: str) -> list[int]:
    return [int(item.strip()) for item in text.split(",") if item.strip()]


def parse_csv_text(text: str) -> list[str]:
    return [item.strip() for item in text.split(",") if item.strip()]


def run(command: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(command, text=True, encoding="utf-8", errors="replace", capture_output=True)
    return proc.returncode, proc.stdout, proc.stderr


def module_file(esmp_dir: Path, layer: int, module: str) -> Path:
    return esmp_dir / f"model__layers__{layer}__{module}.esmp"


def module_family(module: str) -> str:
    if module.startswith("self_attn"):
        return "attention"
    if module.startswith("mlp"):
        return "mlp"
    return "other"


def module_kind(module: str) -> str:
    return module.split("__", 1)[-1]


def layer_bucket(layer: int) -> str:
    if layer <= 1:
        return "early"
    if layer >= 20:
        return "late"
    return "middle"


def read_json(stdout: str) -> dict[str, Any]:
    return json.loads(stdout)


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "layer",
        "layer_bucket",
        "module",
        "family",
        "kind",
        "rows",
        "cols",
        "avg_bits",
        "compression_ratio_vs_fp32",
        "full_mixed_gemv_ms",
        "active_rows",
        "selected_mixed_gemv_ms",
        "selected_speedup_vs_full",
        "file_bytes",
        "fp32_equivalent_bytes",
        "returncode",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name) for name in fieldnames})


def fmt(value: Any, digits: int = 4) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def median(values: list[float]) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return 0.5 * (ordered[mid - 1] + ordered[mid])


def grouped_summary(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("returncode") == 0:
            groups[str(row.get(key, ""))].append(row)
    summaries: list[dict[str, Any]] = []
    for name, items in sorted(groups.items()):
        selected_speedups = [float(row["selected_speedup_vs_full"]) for row in items if row.get("selected_speedup_vs_full") is not None]
        full_ms = [float(row["full_mixed_gemv_ms"]) for row in items if row.get("full_mixed_gemv_ms") is not None]
        selected_ms = [float(row["selected_mixed_gemv_ms"]) for row in items if row.get("selected_mixed_gemv_ms") is not None]
        comp = [float(row["compression_ratio_vs_fp32"]) for row in items if row.get("compression_ratio_vs_fp32") is not None]
        summaries.append(
            {
                key: name,
                "count": len(items),
                "median_full_ms": median(full_ms),
                "median_selected_ms": median(selected_ms),
                "median_selected_speedup_vs_full": median(selected_speedups),
                "median_compression_vs_fp32": median(comp),
            }
        )
    return summaries


def write_markdown(path: Path, rows: list[dict[str, Any]]) -> None:
    ok_rows = [row for row in rows if row.get("returncode") == 0]
    fastest_selected = sorted(ok_rows, key=lambda row: row.get("selected_mixed_gemv_ms") or 1.0e9)[:10]
    best_speedups = sorted(ok_rows, key=lambda row: row.get("selected_speedup_vs_full") or -1.0, reverse=True)[:10]
    lines = [
        "# C++ ESMP Runtime Stratified Sweep",
        "",
        "This report runs the existing C++ packed ESMP runtime on real Qwen3-0.6B Linear module packages.",
        "It measures module-level GEMV and selected-row execution; it is not end-to-end token latency.",
        "",
        f"- total module runs: {len(rows)}",
        f"- successful module runs: {len(ok_rows)}",
        "",
        "## Summary By Module Family",
        "",
        "| family | count | median full ms | median selected ms | median selected/full speedup | median compression vs FP32 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for item in grouped_summary(ok_rows, "family"):
        lines.append(
            f"| {item['family']} | {item['count']} | {fmt(item['median_full_ms'], 6)} | "
            f"{fmt(item['median_selected_ms'], 6)} | {fmt(item['median_selected_speedup_vs_full'])} | "
            f"{fmt(item['median_compression_vs_fp32'])}x |"
        )

    lines.extend(
        [
            "",
            "## Summary By Layer Bucket",
            "",
            "| bucket | count | median full ms | median selected ms | median selected/full speedup | median compression vs FP32 |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for item in grouped_summary(ok_rows, "layer_bucket"):
        lines.append(
            f"| {item['layer_bucket']} | {item['count']} | {fmt(item['median_full_ms'], 6)} | "
            f"{fmt(item['median_selected_ms'], 6)} | {fmt(item['median_selected_speedup_vs_full'])} | "
            f"{fmt(item['median_compression_vs_fp32'])}x |"
        )

    lines.extend(
        [
            "",
            "## Best Selected-Row Speedups",
            "",
            "| rank | layer | module | shape | avg bits | compression | full ms | selected rows | selected ms | speedup |",
            "|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for rank, row in enumerate(best_speedups, start=1):
        lines.append(
            f"| {rank} | {row.get('layer')} | `{row.get('module')}` | {row.get('rows')}x{row.get('cols')} | "
            f"{fmt(row.get('avg_bits'))} | {fmt(row.get('compression_ratio_vs_fp32'))}x | "
            f"{fmt(row.get('full_mixed_gemv_ms'), 6)} | {row.get('active_rows')} | "
            f"{fmt(row.get('selected_mixed_gemv_ms'), 6)} | {fmt(row.get('selected_speedup_vs_full'))} |"
        )

    lines.extend(
        [
            "",
            "## Fastest Selected-Row Runs",
            "",
            "| rank | layer | module | shape | avg bits | selected rows | selected ms | full ms |",
            "|---:|---:|---|---:|---:|---:|---:|---:|",
        ]
    )
    for rank, row in enumerate(fastest_selected, start=1):
        lines.append(
            f"| {rank} | {row.get('layer')} | `{row.get('module')}` | {row.get('rows')}x{row.get('cols')} | "
            f"{fmt(row.get('avg_bits'))} | {row.get('active_rows')} | "
            f"{fmt(row.get('selected_mixed_gemv_ms'), 6)} | {fmt(row.get('full_mixed_gemv_ms'), 6)} |"
        )

    failures = [row for row in rows if row.get("returncode") != 0]
    if failures:
        lines.extend(["", "## Failures", ""])
        for row in failures:
            lines.append(f"- layer={row.get('layer')} module={row.get('module')} rc={row.get('returncode')} error={row.get('error', '')}")

    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "- Valid claim: selected-row packed execution is consistently much faster than full packed GEMV for routed/bypass-like sparse row use.",
            "- Invalid claim: this proves end-to-end LLM token acceleration. That still requires a fused runtime path.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run C++ ESMP runtime sweep.")
    parser.add_argument("--esmp-dir", type=Path, default=Path("outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp"))
    parser.add_argument("--runtime-bench", type=Path, default=Path("build/cpp-wsl/mixed_precision_runtime_bench"))
    parser.add_argument("--layers", default=",".join(str(x) for x in DEFAULT_LAYERS))
    parser.add_argument("--modules", default=",".join(DEFAULT_MODULES))
    parser.add_argument("--iters", type=int, default=120)
    parser.add_argument("--warmup", type=int, default=15)
    parser.add_argument("--active-rows", type=int, default=64)
    parser.add_argument("--out-jsonl", type=Path, default=Path("outputs/real_system_packer_2026-06-05/esmp_runtime_stratified_sweep.jsonl"))
    parser.add_argument("--out-csv", type=Path, default=Path("outputs/real_system_packer_2026-06-05/esmp_runtime_stratified_sweep.csv"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/ESMP_RUNTIME_STRATIFIED_SWEEP.md"))
    args = parser.parse_args()

    layers = parse_csv_ints(args.layers)
    modules = parse_csv_text(args.modules)
    rows: list[dict[str, Any]] = []
    for layer in layers:
        for module in modules:
            path = module_file(args.esmp_dir, layer, module)
            row: dict[str, Any] = {
                "layer": layer,
                "layer_bucket": layer_bucket(layer),
                "module": module,
                "family": module_family(module),
                "kind": module_kind(module),
                "input": str(path),
            }
            if not path.exists():
                row.update({"returncode": -1, "error": "missing ESMP file"})
                rows.append(row)
                write_jsonl(args.out_jsonl, rows)
                continue
            command = [
                str(args.runtime_bench),
                "--input",
                str(path),
                "--iters",
                str(args.iters),
                "--warmup",
                str(args.warmup),
                "--active-rows",
                str(args.active_rows),
            ]
            code, stdout, stderr = run(command)
            row["returncode"] = code
            row["stderr_tail"] = stderr[-1200:]
            try:
                row.update(read_json(stdout))
            except json.JSONDecodeError:
                row["stdout_tail"] = stdout[-1200:]
            if row.get("full_mixed_gemv_ms") and row.get("selected_mixed_gemv_ms") and float(row["selected_mixed_gemv_ms"]) > 0:
                row["selected_speedup_vs_full"] = float(row["full_mixed_gemv_ms"]) / float(row["selected_mixed_gemv_ms"])
            rows.append(row)
            write_jsonl(args.out_jsonl, rows)

    write_csv(args.out_csv, rows)
    write_markdown(args.out_md, rows)
    print(json.dumps({"out_jsonl": str(args.out_jsonl), "out_csv": str(args.out_csv), "out_md": str(args.out_md), "runs": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
