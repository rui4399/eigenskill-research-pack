#!/usr/bin/env python3
from __future__ import annotations

"""Gate a public-calibration GPTQModel smoke.

This is a readiness gate, not a competitive PTQ baseline. It verifies that an
official GPTQModel run used public calibration prompts, saved a local artifact,
reloaded it, and completed a tiny matched FP16-vs-GPTQ PPL diagnostic under the
GPU guard.
"""

import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def finite(value: Any) -> bool:
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def guard_failures(guard: dict[str, Any], max_memory_ratio: float) -> list[str]:
    failures: list[str] = []
    ratio = float(guard.get("max_memory_used_ratio") or 0.0)
    if guard.get("returncode") != 0:
        failures.append(f"guard returncode {guard.get('returncode')} != 0")
    if guard.get("killed_by_guard"):
        failures.append("killed by GPU guard")
    if guard.get("killed_by_timeout"):
        failures.append("killed by timeout")
    if ratio > max_memory_ratio:
        failures.append(f"VRAM ratio {ratio:.4f} > {max_memory_ratio:.4f}")
    return failures


def build_result(*, summary: dict[str, Any], guard: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    package = summary.get("package", {}) if isinstance(summary.get("package"), dict) else {}
    artifact = summary.get("artifact", {}) if isinstance(summary.get("artifact"), dict) else {}
    comparison = summary.get("comparison", {}) if isinstance(summary.get("comparison"), dict) else {}
    fp16 = summary.get("fp16", {}) if isinstance(summary.get("fp16"), dict) else {}
    gptq = summary.get("gptq", {}) if isinstance(summary.get("gptq"), dict) else {}
    tokens = int(summary.get("tokens") or 0)
    calibration_count = int(summary.get("calibration_count") or 0)
    ratio = comparison.get("ppl_ratio_gptq_vs_fp16")

    if not summary.get("passed"):
        failures.append("GPTQModel summary did not pass")
    if package.get("name") != "gptqmodel":
        failures.append(f"package {package.get('name')} != gptqmodel")
    if calibration_count < args.min_calibration_texts:
        failures.append(f"calibration texts {calibration_count} < {args.min_calibration_texts}")
    if not isinstance(summary.get("calibration_source"), list) or not summary.get("calibration_source"):
        failures.append("calibration source is not a public prompt file list")
    if int(artifact.get("file_count") or 0) <= 0:
        failures.append("no saved GPTQ artifact files")
    if args.require_fresh_quantization and summary.get("artifact_reused"):
        failures.append("formal GPTQModel gate reused an existing artifact")
    if tokens < args.min_tokens:
        failures.append(f"tokens {tokens} < {args.min_tokens}")
    if not finite(fp16.get("ppl")) or not finite(gptq.get("ppl")):
        failures.append("non-finite FP16 or GPTQ PPL")
    if not finite(ratio):
        failures.append("GPTQ/FP16 ppl ratio is non-finite")
    elif float(ratio) > args.max_ppl_ratio:
        failures.append(f"ppl ratio {float(ratio):.4f} > {args.max_ppl_ratio:.4f}")
    failures.extend(guard_failures(guard, args.max_memory_ratio))

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "model": summary.get("model"),
            "package": package.get("name"),
            "package_version": package.get("version"),
            "quant_config": summary.get("quant_config"),
            "calibration_source": summary.get("calibration_source"),
            "calibration_count": calibration_count,
            "artifact_file_count": artifact.get("file_count"),
            "artifact_total_bytes": artifact.get("total_bytes"),
            "artifact_reused": bool(summary.get("artifact_reused")),
            "prompt_count": summary.get("prompt_count"),
            "tokens": tokens,
            "fp16_ppl": fp16.get("ppl"),
            "gptq_ppl": gptq.get("ppl"),
            "ppl_ratio_gptq_vs_fp16": ratio,
            "delta_nll_gptq_minus_fp16": comparison.get("delta_nll_gptq_minus_fp16"),
            "guard_max_memory_used_ratio": guard.get("max_memory_used_ratio"),
            "guard_max_memory_used_mib": guard.get("max_memory_used_mib"),
        },
        "failures": failures,
        "claim_boundary": (
            "Valid claim: one public-calibration GPTQModel W4 group-128 smoke ran under guard, "
            "saved/reloaded a local artifact, and produced a tiny matched FP16-vs-GPTQ PPL diagnostic. "
            "Invalid claim: this is a complete official AWQ/GPTQ competitive baseline, SOTA PTQ result, "
            "task-retention proof, or production runtime."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        "# Official GPTQModel Public-Calibration Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- model: `{summary['model']}`",
        f"- package: `{summary['package']} {summary['package_version']}`",
        f"- quant config: `{summary['quant_config']}`",
        f"- calibration sources: `{summary['calibration_source']}`",
        f"- calibration texts: `{summary['calibration_count']}`",
        f"- artifact files: `{summary['artifact_file_count']}`",
        f"- artifact bytes: `{summary['artifact_total_bytes']}`",
        f"- artifact reused: `{summary['artifact_reused']}`",
        f"- prompts: `{summary['prompt_count']}`",
        f"- tokens: `{summary['tokens']}`",
        f"- peak VRAM ratio: `{summary['guard_max_memory_used_ratio']}`",
        "",
        "## Metrics",
        "",
        "| run | PPL |",
        "|---|---:|",
        f"| `fp16` | {float(summary['fp16_ppl']):.6f} |",
        f"| `gptqmodel_w4g128` | {float(summary['gptq_ppl']):.6f} |",
        "",
        "## Comparison",
        "",
        f"- PPL ratio GPTQ/FP16: `{float(summary['ppl_ratio_gptq_vs_fp16']):.6f}`",
        f"- delta NLL GPTQ-FP16: `{float(summary['delta_nll_gptq_minus_fp16']):.6f}`",
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
    parser = argparse.ArgumentParser(description="Gate public-calibration GPTQModel smoke.")
    parser.add_argument("--summary-json", type=Path, required=True)
    parser.add_argument("--guard-json", type=Path, required=True)
    parser.add_argument("--min-tokens", type=int, default=128)
    parser.add_argument("--min-calibration-texts", type=int, default=1)
    parser.add_argument("--max-memory-ratio", type=float, default=0.85)
    parser.add_argument("--max-ppl-ratio", type=float, default=5.0)
    parser.add_argument("--allow-reused-artifact", action="store_true")
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()
    args.require_fresh_quantization = not args.allow_reused_artifact

    result = build_result(summary=load_json(args.summary_json), guard=load_json(args.guard_json), args=args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "failures": result["failures"]}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
