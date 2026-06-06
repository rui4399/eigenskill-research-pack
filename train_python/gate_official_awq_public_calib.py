#!/usr/bin/env python3
from __future__ import annotations

"""Gate a public-calibration AutoAWQ baseline bundle.

This gate is stricter than the minimal AutoAWQ smoke: it requires public
calibration prompt files, a guarded quantization run, and at least two guarded
matched FP16-vs-AutoAWQ PPL eval slices. It is still not a GPTQ/AWQ
competitive baseline because it covers one package and tiny prompt slices.
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


def parse_labeled_path(raw: str) -> tuple[str, Path]:
    if "=" not in raw:
        raise argparse.ArgumentTypeError("expected label=path")
    label, path = raw.split("=", 1)
    label = label.strip()
    if not label:
        raise argparse.ArgumentTypeError("label cannot be empty")
    return label, Path(path)


def guard_failures(prefix: str, guard: dict[str, Any], max_memory_ratio: float) -> list[str]:
    failures: list[str] = []
    ratio = float(guard.get("max_memory_used_ratio") or 0.0)
    if guard.get("returncode") != 0:
        failures.append(f"{prefix} guard returncode {guard.get('returncode')} != 0")
    if guard.get("killed_by_guard"):
        failures.append(f"{prefix} killed by GPU guard")
    if guard.get("killed_by_timeout"):
        failures.append(f"{prefix} killed by timeout")
    if ratio > max_memory_ratio:
        failures.append(f"{prefix} VRAM ratio {ratio:.4f} > {max_memory_ratio:.4f}")
    return failures


def build_result(
    *,
    smoke: dict[str, Any],
    smoke_guard: dict[str, Any],
    evals: list[tuple[str, dict[str, Any], dict[str, Any]]],
    args: argparse.Namespace,
) -> dict[str, Any]:
    failures: list[str] = []
    calibration = smoke.get("calibration", {}) if isinstance(smoke.get("calibration"), dict) else {}
    calibration_source = calibration.get("source")
    calibration_plan = calibration.get("plan", {}) if isinstance(calibration.get("plan"), dict) else {}
    expected_blocks = int(calibration_plan.get("expected_awq_blocks") or 0)
    eval_rows: list[dict[str, Any]] = []
    total_tokens = 0

    if not smoke.get("passed"):
        failures.append("public-calibration AutoAWQ smoke did not pass")
    if not isinstance(calibration_source, list) or len(calibration_source) < 1:
        failures.append("calibration source is not a public prompt file list")
    if not calibration_plan.get("ok"):
        failures.append("calibration plan did not pass")
    if expected_blocks < args.min_awq_blocks:
        failures.append(f"AWQ calibration blocks {expected_blocks} < {args.min_awq_blocks}")
    failures.extend(guard_failures("smoke", smoke_guard, args.max_memory_ratio))

    if len(evals) < args.min_eval_slices:
        failures.append(f"eval slices {len(evals)} < {args.min_eval_slices}")

    for label, summary, guard in evals:
        tokens = int(summary.get("tokens") or 0)
        total_tokens += tokens
        ratio = summary.get("comparison", {}).get("ppl_ratio_awq_vs_fp16") if isinstance(summary.get("comparison"), dict) else None
        if not summary.get("passed"):
            failures.append(f"{label} eval summary did not pass")
        if tokens <= 0:
            failures.append(f"{label} eval has no tokens")
        if not finite(ratio):
            failures.append(f"{label} ppl ratio is non-finite")
        elif float(ratio) > args.max_ppl_ratio:
            failures.append(f"{label} ppl ratio {float(ratio):.4f} > {args.max_ppl_ratio:.4f}")
        failures.extend(guard_failures(label, guard, args.max_memory_ratio))
        eval_rows.append(
            {
                "label": label,
                "prompt_source": summary.get("prompt_source"),
                "prompt_count": summary.get("prompt_count"),
                "tokens": tokens,
                "fp16_ppl": summary.get("fp16", {}).get("ppl") if isinstance(summary.get("fp16"), dict) else None,
                "awq_ppl": summary.get("awq", {}).get("ppl") if isinstance(summary.get("awq"), dict) else None,
                "ppl_ratio_awq_vs_fp16": ratio,
                "guard_max_memory_used_ratio": guard.get("max_memory_used_ratio"),
            }
        )

    if total_tokens < args.min_total_tokens:
        failures.append(f"total eval tokens {total_tokens} < {args.min_total_tokens}")

    artifact = smoke.get("artifact", {}) if isinstance(smoke.get("artifact"), dict) else {}
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "model": smoke.get("model"),
            "package": smoke.get("package", {}).get("name") if isinstance(smoke.get("package"), dict) else None,
            "package_version": smoke.get("package", {}).get("version") if isinstance(smoke.get("package"), dict) else None,
            "quant_config": smoke.get("quant_config"),
            "calibration_source": calibration_source,
            "calibration_sample_count": calibration.get("sample_count"),
            "expected_awq_blocks": expected_blocks,
            "artifact_file_count": artifact.get("file_count"),
            "artifact_total_bytes": artifact.get("total_bytes"),
            "smoke_guard_max_memory_used_ratio": smoke_guard.get("max_memory_used_ratio"),
            "eval_slice_count": len(evals),
            "total_eval_tokens": total_tokens,
            "evals": eval_rows,
        },
        "failures": failures,
        "claim_boundary": (
            "Valid claim: one public-calibration AutoAWQ W4 group-128 baseline bundle ran under guard "
            "and was evaluated on tiny public WikiText2/C4 PPL slices. Invalid claim: this is a complete "
            "official AWQ/GPTQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        "# Official AutoAWQ Public-Calibration Baseline Gate",
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
        f"- calibration samples: `{summary['calibration_sample_count']}`",
        f"- expected AWQ calibration blocks: `{summary['expected_awq_blocks']}`",
        f"- artifact files: `{summary['artifact_file_count']}`",
        f"- artifact bytes: `{summary['artifact_total_bytes']}`",
        f"- quantization peak VRAM ratio: `{summary['smoke_guard_max_memory_used_ratio']}`",
        f"- eval slices: `{summary['eval_slice_count']}`",
        f"- total eval tokens: `{summary['total_eval_tokens']}`",
        "",
        "## Eval Slices",
        "",
        "| label | prompts | tokens | FP16 PPL | AutoAWQ PPL | ratio | peak VRAM |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for item in summary["evals"]:
        lines.append(
            f"| `{item['label']}` | {item['prompt_count']} | {item['tokens']} | "
            f"{float(item['fp16_ppl']):.6f} | {float(item['awq_ppl']):.6f} | "
            f"{float(item['ppl_ratio_awq_vs_fp16']):.6f} | "
            f"{float(item['guard_max_memory_used_ratio']):.4f} |"
        )
    lines.extend(["", "## Failures", ""])
    if result["failures"]:
        lines.extend(f"- {failure}" for failure in result["failures"])
    else:
        lines.append("- none")
    lines.extend(["", "## Claim Boundary", "", f"- {result['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate public-calibration AutoAWQ baseline bundle.")
    parser.add_argument("--smoke-summary-json", type=Path, required=True)
    parser.add_argument("--smoke-guard-json", type=Path, required=True)
    parser.add_argument("--eval-summary", action="append", type=parse_labeled_path, default=[])
    parser.add_argument("--eval-guard", action="append", type=parse_labeled_path, default=[])
    parser.add_argument("--min-eval-slices", type=int, default=2)
    parser.add_argument("--min-total-tokens", type=int, default=256)
    parser.add_argument("--min-awq-blocks", type=int, default=1)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--max-ppl-ratio", type=float, default=5.0)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    guard_map = {label: path for label, path in args.eval_guard}
    evals: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
    for label, summary_path in args.eval_summary:
        guard_path = guard_map.get(label)
        if guard_path is None:
            raise SystemExit(f"missing --eval-guard for label {label}")
        evals.append((label, load_json(summary_path), load_json(guard_path)))

    result = build_result(
        smoke=load_json(args.smoke_summary_json),
        smoke_guard=load_json(args.smoke_guard_json),
        evals=evals,
        args=args,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "failures": result["failures"]}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
