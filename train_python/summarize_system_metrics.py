#!/usr/bin/env python3
from __future__ import annotations

"""Summarize end-to-end generation system metrics from JSON artifacts."""

import argparse
import json
from pathlib import Path
from typing import Any


def load_case(spec: str) -> tuple[str, Path, dict[str, Any]]:
    if "=" not in spec:
        raise ValueError(f"case must be LABEL=PATH, got {spec!r}")
    label, path_text = spec.split("=", 1)
    label = label.strip()
    path = Path(path_text.strip())
    if not label:
        raise ValueError(f"empty case label in {spec!r}")
    if not path.exists():
        raise FileNotFoundError(path)
    return label, path, json.loads(path.read_text(encoding="utf-8"))


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


def ratio(numerator: Any, denominator: Any) -> float | None:
    n = finite_float(numerator)
    d = finite_float(denominator)
    if n is None or d is None or d == 0.0:
        return None
    return n / d


def metric_row(label: str, path: Path, data: dict[str, Any]) -> dict[str, Any]:
    replaced = data.get("replaced_module_count")
    if replaced is None:
        replaced = data.get("replacement_count", 0)
    selected_compression = data.get("selected_compression_vs_fp32")
    if selected_compression in (None, 0, 0.0):
        selected_compression = data.get("replacement_compression_vs_fp32")
    cuda_event = data.get("replacement_cuda_event_ms") or {}
    return {
        "label": label,
        "path": str(path),
        "model": data.get("model"),
        "mode": data.get("mode"),
        "dtype": data.get("dtype"),
        "max_new_tokens": data.get("max_new_tokens"),
        "prompt_tokens": data.get("prompt_tokens"),
        "generated_tokens": data.get("generated_tokens_text_retokenized"),
        "ttft_seconds": finite_float(data.get("ttft_seconds")),
        "elapsed_seconds": finite_float(data.get("elapsed_seconds")),
        "tokens_per_second": finite_float(data.get("tokens_per_second")),
        "peak_gpu_memory_mib": finite_float(data.get("peak_gpu_memory_mib")),
        "replaced_module_count": int(replaced or 0),
        "replacement_compression_vs_fp32": finite_float(selected_compression),
        "replacement_cuda_event_mean_ms": finite_float(cuda_event.get("mean")),
        "replacement_cuda_event_p90_ms": finite_float(cuda_event.get("p90")),
    }


def add_baseline_ratios(rows: list[dict[str, Any]], baseline_label: str) -> None:
    baseline = next((row for row in rows if row["label"] == baseline_label), None)
    if baseline is None:
        raise ValueError(f"baseline label {baseline_label!r} was not found")
    for row in rows:
        row["ttft_speedup_vs_baseline"] = ratio(baseline.get("ttft_seconds"), row.get("ttft_seconds"))
        row["tps_ratio_vs_baseline"] = ratio(row.get("tokens_per_second"), baseline.get("tokens_per_second"))
        mem = finite_float(row.get("peak_gpu_memory_mib"))
        base_mem = finite_float(baseline.get("peak_gpu_memory_mib"))
        row["memory_delta_mib_vs_baseline"] = None if mem is None or base_mem is None else mem - base_mem
        row["memory_ratio_vs_baseline"] = ratio(mem, base_mem)


def fmt(value: Any, digits: int = 4) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def write_markdown(path: Path, rows: list[dict[str, Any]], baseline_label: str | None) -> None:
    lines = [
        "# End-to-End Generation System Metrics",
        "",
        "This report summarizes measured generation artifacts. It does not create a new benchmark run.",
        "Use it to keep TTFT, tokens/s, memory, and package-compression claims tied to concrete JSON files.",
        "",
    ]
    if baseline_label:
        lines.append(f"Baseline for ratios: `{baseline_label}`")
        lines.append("")
    lines.extend(
        [
            "| case | mode | max new | replaced | TTFT s | TPS | peak GPU MiB | TTFT speedup | TPS ratio | memory delta MiB | compression vs FP32 |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['label']} | {row.get('mode') or 'n/a'} | {row.get('max_new_tokens') or 'n/a'} | "
            f"{row.get('replaced_module_count', 0)} | {fmt(row.get('ttft_seconds'))} | "
            f"{fmt(row.get('tokens_per_second'))} | {fmt(row.get('peak_gpu_memory_mib'))} | "
            f"{fmt(row.get('ttft_speedup_vs_baseline'))} | {fmt(row.get('tps_ratio_vs_baseline'))} | "
            f"{fmt(row.get('memory_delta_mib_vs_baseline'))} | {fmt(row.get('replacement_compression_vs_fp32'))} |"
        )
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "- Valid claim: these JSON artifacts record local TTFT, tokens/s, peak allocated GPU memory, and selected-module compression for the listed smoke cases.",
            "- Invalid claim: these numbers prove production acceleration, mobile latency, energy savings, or model-quality retention.",
            "",
            "## Source Files",
            "",
        ]
    )
    lines.extend(f"- `{row['label']}`: `{row['path']}`" for row in rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize generation TTFT/TPS/memory JSON artifacts.")
    parser.add_argument("--case", action="append", required=True, help="Repeated LABEL=PATH case specs.")
    parser.add_argument("--baseline", default="", help="Optional label used for ratio columns.")
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/end_to_end_system_metrics.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/END_TO_END_SYSTEM_METRICS.md"))
    args = parser.parse_args()

    rows = [metric_row(label, path, data) for label, path, data in (load_case(spec) for spec in args.case)]
    if args.baseline:
        add_baseline_ratios(rows, args.baseline)
    result = {"baseline": args.baseline or None, "cases": rows}
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, rows, args.baseline or None)
    print(json.dumps({"out_json": str(args.out_json), "out_md": str(args.out_md), "cases": len(rows)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
