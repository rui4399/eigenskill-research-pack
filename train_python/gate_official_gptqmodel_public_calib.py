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


def parse_labeled_path(raw: str) -> tuple[str, Path]:
    if "=" not in raw:
        raise argparse.ArgumentTypeError("expected label=path")
    label, path = raw.split("=", 1)
    label = label.strip()
    if not label:
        raise argparse.ArgumentTypeError("label cannot be empty")
    return label, Path(path)


def load_eval_pairs(
    *,
    summaries: list[tuple[str, Path]],
    guards: list[tuple[str, Path]],
) -> list[tuple[str, dict[str, Any], dict[str, Any]]]:
    guard_by_label = dict(guards)
    summary_labels = [label for label, _ in summaries]
    guard_labels = list(guard_by_label)
    if set(summary_labels) != set(guard_labels):
        raise ValueError(f"eval summary labels {summary_labels} do not match guard labels {guard_labels}")
    return [(label, load_json(summary_path), load_json(guard_by_label[label])) for label, summary_path in summaries]


def eval_failures(label: str, summary: dict[str, Any], guard: dict[str, Any], args: argparse.Namespace) -> tuple[list[str], dict[str, Any]]:
    failures: list[str] = []
    comparison = summary.get("comparison", {}) if isinstance(summary.get("comparison"), dict) else {}
    fp16 = summary.get("fp16", {}) if isinstance(summary.get("fp16"), dict) else {}
    gptq = summary.get("gptq", {}) if isinstance(summary.get("gptq"), dict) else {}
    tokens = int(summary.get("tokens") or 0)
    ratio = comparison.get("ppl_ratio_gptq_vs_fp16")

    if not summary.get("passed"):
        failures.append(f"{label} GPTQModel eval summary did not pass")
    if tokens <= 0:
        failures.append(f"{label} eval has no tokens")
    if not finite(fp16.get("ppl")) or not finite(gptq.get("ppl")):
        failures.append(f"{label} has non-finite FP16 or GPTQ PPL")
    if not finite(ratio):
        failures.append(f"{label} GPTQ/FP16 ppl ratio is non-finite")
    elif float(ratio) > args.max_ppl_ratio:
        failures.append(f"{label} ppl ratio {float(ratio):.4f} > {args.max_ppl_ratio:.4f}")
    failures.extend(guard_failures(guard, args.max_memory_ratio))
    return failures, {
        "label": label,
        "prompt_count": summary.get("prompt_count"),
        "tokens": tokens,
        "artifact_reused": bool(summary.get("artifact_reused")),
        "fp16_ppl": fp16.get("ppl"),
        "gptq_ppl": gptq.get("ppl"),
        "ppl_ratio_gptq_vs_fp16": ratio,
        "delta_nll_gptq_minus_fp16": comparison.get("delta_nll_gptq_minus_fp16"),
        "guard_max_memory_used_ratio": guard.get("max_memory_used_ratio"),
        "guard_max_memory_used_mib": guard.get("max_memory_used_mib"),
    }


def build_result(
    *,
    summary: dict[str, Any],
    guard: dict[str, Any],
    args: argparse.Namespace,
    evals: list[tuple[str, dict[str, Any], dict[str, Any]]] | None = None,
) -> dict[str, Any]:
    failures: list[str] = []
    package = summary.get("package", {}) if isinstance(summary.get("package"), dict) else {}
    artifact = summary.get("artifact", {}) if isinstance(summary.get("artifact"), dict) else {}
    calibration_count = int(summary.get("calibration_count") or 0)

    if not summary.get("passed"):
        failures.append("fresh GPTQModel quantization summary did not pass")
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
    failures.extend(guard_failures(guard, args.max_memory_ratio))

    eval_inputs = evals if evals is not None else [("primary", summary, guard)]
    eval_rows: list[dict[str, Any]] = []
    total_eval_tokens = 0
    min_eval_slices = int(getattr(args, "min_eval_slices", 1) or 1)
    min_total_tokens = int(getattr(args, "min_total_tokens", getattr(args, "min_tokens", 0)) or 0)
    if len(eval_inputs) < min_eval_slices:
        failures.append(f"eval slices {len(eval_inputs)} < {min_eval_slices}")
    for label, eval_summary, eval_guard in eval_inputs:
        row_failures, row = eval_failures(label, eval_summary, eval_guard, args)
        failures.extend(row_failures)
        eval_rows.append(row)
        total_eval_tokens += int(row["tokens"] or 0)
    if total_eval_tokens < min_total_tokens:
        failures.append(f"total eval tokens {total_eval_tokens} < {min_total_tokens}")

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
            "eval_slice_count": len(eval_inputs),
            "total_eval_tokens": total_eval_tokens,
            "prompt_count": summary.get("prompt_count"),
            "tokens": total_eval_tokens,
            "fp16_ppl": eval_rows[0].get("fp16_ppl") if eval_rows else None,
            "gptq_ppl": eval_rows[0].get("gptq_ppl") if eval_rows else None,
            "ppl_ratio_gptq_vs_fp16": eval_rows[0].get("ppl_ratio_gptq_vs_fp16") if eval_rows else None,
            "delta_nll_gptq_minus_fp16": eval_rows[0].get("delta_nll_gptq_minus_fp16") if eval_rows else None,
            "guard_max_memory_used_ratio": guard.get("max_memory_used_ratio"),
            "guard_max_memory_used_mib": guard.get("max_memory_used_mib"),
            "evals": eval_rows,
        },
        "failures": failures,
        "claim_boundary": (
            "Valid claim: one fresh public-calibration GPTQModel W4 group-128 smoke ran under guard, "
            "saved/reloaded a local artifact, and produced tiny labeled FP16-vs-GPTQ PPL diagnostics. "
            "Invalid claim: this is a complete official AWQ/GPTQ competitive baseline, SOTA PTQ result, "
            "task-retention proof, or production runtime."
        ),
    }


def format_float(value: Any) -> str:
    if not finite(value):
        return "NA"
    return f"{float(value):.6f}"


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    eval_rows = summary.get("evals") if isinstance(summary.get("evals"), list) else []
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
        f"- eval slices: `{summary['eval_slice_count']}`",
        f"- total eval tokens: `{summary['total_eval_tokens']}`",
        f"- peak VRAM ratio: `{summary['guard_max_memory_used_ratio']}`",
        "",
        "## Evaluation Slices",
        "",
        "| slice | prompts | tokens | FP16 PPL | GPTQ PPL | ratio | artifact reused | peak VRAM |",
        "|---|---:|---:|---:|---:|---:|---|---:|",
    ]
    for row in eval_rows:
        lines.append(
            "| "
            f"`{row['label']}` | "
            f"{row['prompt_count']} | "
            f"{row['tokens']} | "
            f"{format_float(row['fp16_ppl'])} | "
            f"{format_float(row['gptq_ppl'])} | "
            f"{format_float(row['ppl_ratio_gptq_vs_fp16'])} | "
            f"`{row['artifact_reused']}` | "
            f"{format_float(row['guard_max_memory_used_ratio'])} |"
        )
    lines.extend([
        "",
        "## Metrics",
        "",
        "| run | PPL |",
        "|---|---:|",
        f"| `fp16` | {format_float(summary['fp16_ppl'])} |",
        f"| `gptqmodel_w4g128` | {format_float(summary['gptq_ppl'])} |",
        "",
        "## Comparison",
        "",
        f"- PPL ratio GPTQ/FP16: `{format_float(summary['ppl_ratio_gptq_vs_fp16'])}`",
        f"- delta NLL GPTQ-FP16: `{format_float(summary['delta_nll_gptq_minus_fp16'])}`",
        "",
        "## Failures",
        "",
    ])
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
    parser.add_argument("--eval-summary", type=parse_labeled_path, action="append", default=[])
    parser.add_argument("--eval-guard", type=parse_labeled_path, action="append", default=[])
    parser.add_argument("--min-tokens", type=int, default=128)
    parser.add_argument("--min-eval-slices", type=int, default=1)
    parser.add_argument("--min-total-tokens", type=int)
    parser.add_argument("--min-calibration-texts", type=int, default=1)
    parser.add_argument("--max-memory-ratio", type=float, default=0.85)
    parser.add_argument("--max-ppl-ratio", type=float, default=5.0)
    parser.add_argument("--allow-reused-artifact", action="store_true")
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()
    args.require_fresh_quantization = not args.allow_reused_artifact
    if args.min_total_tokens is None:
        args.min_total_tokens = args.min_tokens

    summary = load_json(args.summary_json)
    guard = load_json(args.guard_json)
    evals = None
    if args.eval_summary or args.eval_guard:
        evals = load_eval_pairs(summaries=args.eval_summary, guards=args.eval_guard)

    result = build_result(summary=summary, guard=guard, evals=evals, args=args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "failures": result["failures"]}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
