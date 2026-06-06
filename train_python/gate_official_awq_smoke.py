#!/usr/bin/env python3
from __future__ import annotations

"""Gate a faithful AutoAWQ smoke run.

This gate is intentionally narrow: it verifies that an AutoAWQ package was
actually imported, quantization produced local artifacts, a tiny generation
smoke ran, and the GPU guard stayed below the configured memory ceiling.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_result(summary: dict[str, Any], guard: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    package = summary.get("package", {}) or {}
    quant_config = summary.get("quant_config", {}) or {}
    artifact = summary.get("artifact", {}) or {}
    generation = summary.get("generation_smoke", {}) or {}
    guard_ratio = float(guard.get("max_memory_used_ratio") or 0.0)

    if not summary.get("passed"):
        failures.append("summary did not pass")
    if package.get("name") != args.require_package:
        failures.append(f"package {package.get('name')} != {args.require_package}")
    if int(quant_config.get("w_bit") or 0) != args.require_w_bit:
        failures.append(f"w_bit {quant_config.get('w_bit')} != {args.require_w_bit}")
    if int(quant_config.get("q_group_size") or 0) != args.require_q_group_size:
        failures.append(f"q_group_size {quant_config.get('q_group_size')} != {args.require_q_group_size}")
    if int(artifact.get("file_count") or 0) <= 0:
        failures.append("no quantized artifact files recorded")
    if int(artifact.get("total_bytes") or 0) < args.min_quantized_bytes:
        failures.append(f"artifact bytes {artifact.get('total_bytes')} < {args.min_quantized_bytes}")
    if not generation.get("ok"):
        failures.append("generation smoke did not pass")
    if guard.get("returncode") != 0:
        failures.append(f"guard returncode {guard.get('returncode')} != 0")
    if guard.get("killed_by_guard"):
        failures.append("killed by GPU guard")
    if guard.get("killed_by_timeout"):
        failures.append("killed by timeout")
    if guard_ratio > args.max_memory_ratio:
        failures.append(f"VRAM ratio {guard_ratio:.4f} > {args.max_memory_ratio:.4f}")

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "model": summary.get("model"),
            "package": package.get("name"),
            "package_version": package.get("version"),
            "w_bit": quant_config.get("w_bit"),
            "q_group_size": quant_config.get("q_group_size"),
            "artifact_file_count": artifact.get("file_count", 0),
            "artifact_total_bytes": artifact.get("total_bytes", 0),
            "guard_max_memory_used_ratio": guard_ratio,
        },
        "failures": failures,
        "claim_boundary": (
            "Valid claim: a minimal AutoAWQ quantization smoke completed under guard. "
            "Invalid claim: this is a competitive AWQ baseline, leaderboard result, or broad quality-retention proof."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        "# Official AutoAWQ Smoke Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- model: `{summary['model']}`",
        f"- package: `{summary['package']} {summary['package_version']}`",
        f"- quant config: `w_bit={summary['w_bit']}`, `q_group_size={summary['q_group_size']}`",
        f"- artifact files: `{summary['artifact_file_count']}`",
        f"- artifact bytes: `{summary['artifact_total_bytes']}`",
        f"- peak guard VRAM ratio: `{summary['guard_max_memory_used_ratio']:.4f}`",
        "",
        "## Failures",
        "",
    ]
    if result["failures"]:
        lines.extend(f"- {failure}" for failure in result["failures"])
    else:
        lines.append("- none")
    lines.extend(["", "## Claim Boundary", "", f"- {result['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate a minimal official AutoAWQ smoke run.")
    parser.add_argument("--summary-json", type=Path, required=True)
    parser.add_argument("--guard-json", type=Path, required=True)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--min-quantized-bytes", type=int, default=1024)
    parser.add_argument("--require-package", default="autoawq")
    parser.add_argument("--require-w-bit", type=int, default=4)
    parser.add_argument("--require-q-group-size", type=int, default=128)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    result = build_result(load_json(args.summary_json), load_json(args.guard_json), args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "failures": result["failures"]}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
