#!/usr/bin/env python3
from __future__ import annotations

"""Gate a minimal matched FP16-vs-AutoAWQ PPL comparison."""

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


def build_result(summary: dict[str, Any], guard: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    package = summary.get("package", {}) or {}
    comparison = summary.get("comparison", {}) or {}
    guard_ratio = float(guard.get("max_memory_used_ratio") or 0.0)
    tokens = int(summary.get("tokens") or 0)
    ratio = comparison.get("ppl_ratio_awq_vs_fp16")

    if not summary.get("passed"):
        failures.append("summary did not pass")
    if package.get("name") != args.require_package:
        failures.append(f"package {package.get('name')} != {args.require_package}")
    if tokens < args.min_tokens:
        failures.append(f"tokens {tokens} < {args.min_tokens}")
    if not finite(ratio):
        failures.append("ppl ratio is non-finite")
    elif float(ratio) > args.max_ppl_ratio:
        failures.append(f"ppl ratio {float(ratio):.4f} > {args.max_ppl_ratio:.4f}")
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
            "prompt_count": summary.get("prompt_count", 0),
            "tokens": tokens,
            "fp16_ppl": summary.get("fp16", {}).get("ppl"),
            "awq_ppl": summary.get("awq", {}).get("ppl"),
            "ppl_ratio_awq_vs_fp16": ratio,
            "delta_nll_awq_minus_fp16": comparison.get("delta_nll_awq_minus_fp16"),
            "guard_max_memory_used_ratio": guard_ratio,
        },
        "failures": failures,
        "claim_boundary": (
            "Valid claim: a minimal matched FP16-vs-AutoAWQ PPL comparison completed under guard. "
            "Invalid claim: this is a complete official AWQ/GPTQ baseline, SOTA comparison, or broad task-retention result."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        "# Official AutoAWQ Matched PPL Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- model: `{summary['model']}`",
        f"- package: `{summary['package']} {summary['package_version']}`",
        f"- prompts: `{summary['prompt_count']}`",
        f"- tokens: `{summary['tokens']}`",
        f"- FP16 PPL: `{summary['fp16_ppl']}`",
        f"- AutoAWQ PPL: `{summary['awq_ppl']}`",
        f"- PPL ratio AWQ/FP16: `{summary['ppl_ratio_awq_vs_fp16']}`",
        f"- delta NLL AWQ-FP16: `{summary['delta_nll_awq_minus_fp16']}`",
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
    parser = argparse.ArgumentParser(description="Gate matched FP16-vs-AutoAWQ PPL.")
    parser.add_argument("--summary-json", type=Path, required=True)
    parser.add_argument("--guard-json", type=Path, required=True)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--min-tokens", type=int, default=16)
    parser.add_argument("--max-ppl-ratio", type=float, default=20.0)
    parser.add_argument("--require-package", default="autoawq")
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
