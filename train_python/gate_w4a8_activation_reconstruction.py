#!/usr/bin/env python3
from __future__ import annotations

"""Gate W4A8 activation reconstruction evidence."""

import argparse
import json
from pathlib import Path
from typing import Any


def load_result(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_gate(result: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    summary = result.get("summary", {})
    failures: list[str] = []
    modules_ok = int(summary.get("modules_ok", 0))
    if modules_ok < args.min_modules:
        failures.append(f"modules_ok {modules_ok} < {args.min_modules}")
    if float(summary.get("max_activation_added_rel_l2", 1.0e9)) > args.max_activation_added_rel_l2:
        failures.append(
            f"max activation-added rel-L2 {float(summary.get('max_activation_added_rel_l2')):.6f} "
            f"> {args.max_activation_added_rel_l2:.6f}"
        )
    if float(summary.get("p90_w4a8_rel_l2", 1.0e9)) > args.max_p90_w4a8_rel_l2:
        failures.append(
            f"p90 W4A8 rel-L2 {float(summary.get('p90_w4a8_rel_l2')):.6f} > {args.max_p90_w4a8_rel_l2:.6f}"
        )
    if float(summary.get("median_compression_vs_fp32", 0.0)) < args.min_median_compression:
        failures.append(
            f"median compression {float(summary.get('median_compression_vs_fp32')):.4f} < {args.min_median_compression:.4f}"
        )
    if float(result.get("peak_cuda_memory_ratio", 1.0)) > args.max_memory_ratio:
        failures.append(
            f"peak CUDA memory ratio {float(result.get('peak_cuda_memory_ratio')):.4f} > {args.max_memory_ratio:.4f}"
        )
    return {
        "passed": not failures,
        "failures": failures,
        "summary": {
            "modules_ok": modules_ok,
            "median_w4a8_rel_l2": summary.get("median_w4a8_rel_l2"),
            "p90_w4a8_rel_l2": summary.get("p90_w4a8_rel_l2"),
            "max_w4a8_rel_l2": summary.get("max_w4a8_rel_l2"),
            "median_activation_added_rel_l2": summary.get("median_activation_added_rel_l2"),
            "max_activation_added_rel_l2": summary.get("max_activation_added_rel_l2"),
            "median_activation_input_rel_l2": summary.get("median_activation_input_rel_l2"),
            "median_compression_vs_fp32": summary.get("median_compression_vs_fp32"),
            "peak_cuda_memory_ratio": result.get("peak_cuda_memory_ratio"),
        },
        "thresholds": {
            "min_modules": args.min_modules,
            "max_activation_added_rel_l2": args.max_activation_added_rel_l2,
            "max_p90_w4a8_rel_l2": args.max_p90_w4a8_rel_l2,
            "min_median_compression": args.min_median_compression,
            "max_memory_ratio": args.max_memory_ratio,
        },
    }


def fmt(value: Any, digits: int = 6) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def write_markdown(path: Path, gate: dict[str, Any], source: Path) -> None:
    s = gate["summary"]
    lines = [
        "# W4A8 Activation Reconstruction Gate",
        "",
        f"Status: **{'PASS' if gate['passed'] else 'FAIL'}**",
        "",
        "## Source",
        "",
        f"- JSON: `{source.as_posix()}`",
        "",
        "## Summary",
        "",
        f"- modules OK: `{s['modules_ok']}`",
        f"- median W4A8 rel-L2: `{fmt(s['median_w4a8_rel_l2'])}`",
        f"- p90 W4A8 rel-L2: `{fmt(s['p90_w4a8_rel_l2'])}`",
        f"- max W4A8 rel-L2: `{fmt(s['max_w4a8_rel_l2'])}`",
        f"- median activation-added rel-L2 vs W4A16: `{fmt(s['median_activation_added_rel_l2'])}`",
        f"- max activation-added rel-L2 vs W4A16: `{fmt(s['max_activation_added_rel_l2'])}`",
        f"- median activation input rel-L2: `{fmt(s['median_activation_input_rel_l2'])}`",
        f"- median compression vs FP32: `{fmt(s['median_compression_vs_fp32'], 4)}x`",
        f"- peak CUDA memory ratio: `{fmt(s['peak_cuda_memory_ratio'], 4)}`",
        "",
        "## Thresholds",
        "",
    ]
    for key, value in gate["thresholds"].items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Failures", ""])
    lines.extend([f"- {failure}" for failure in gate["failures"]] or ["- none"])
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "Valid claim: selected real Qwen3 module activations have bounded added drift from A8 activation quantization.",
            "",
            "Invalid claim: this gate does not prove end-to-end LLM acceleration, full-model quality retention, mobile deployment, or SOTA quantization.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate W4A8 activation reconstruction evidence.")
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--min-modules", type=int, default=8)
    parser.add_argument("--max-activation-added-rel-l2", type=float, default=0.05)
    parser.add_argument("--max-p90-w4a8-rel-l2", type=float, default=0.25)
    parser.add_argument("--min-median-compression", type=float, default=3.5)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    gate = build_gate(load_result(args.json), args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(gate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, gate, args.json)
    print(json.dumps({"passed": gate["passed"], "summary": gate["summary"], "failures": gate["failures"]}, ensure_ascii=False, indent=2))
    if not gate["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
