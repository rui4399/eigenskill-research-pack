#!/usr/bin/env python3
from __future__ import annotations

"""Gate a matched official PTQ evidence pack across PPL, tasks, and runtime."""

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class PplCase:
    variant: str
    label: str
    path: Path


def parse_ppl_case(raw: str) -> PplCase:
    if ":" not in raw or "=" not in raw:
        raise ValueError(f"PPL case must be VARIANT:LABEL=PATH: {raw}")
    variant, rest = raw.split(":", 1)
    label, path = rest.split("=", 1)
    variant = variant.strip()
    label = label.strip()
    path = path.strip()
    if not variant or not label or not path:
        raise ValueError(f"empty variant/label/path in PPL case: {raw}")
    return PplCase(variant=variant, label=label, path=Path(path))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def finite(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def variant_quant_key(payload: dict[str, Any], variant: str) -> str:
    if variant == "autoawq":
        return "awq"
    if variant == "gptqmodel":
        return "gptq"
    if variant in payload:
        return variant
    raise ValueError(f"unsupported or missing quant variant key: {variant}")


def ppl_ratio(payload: dict[str, Any], variant: str) -> float | None:
    comparison = payload.get("comparison", {})
    for key, value in comparison.items():
        if key.startswith("ppl_ratio_"):
            return finite(value)
    quant_key = variant_quant_key(payload, variant)
    fp16_ppl = finite(payload.get("fp16", {}).get("ppl"))
    quant_ppl = finite(payload.get(quant_key, {}).get("ppl"))
    if fp16_ppl is None or quant_ppl is None or fp16_ppl <= 0.0:
        return None
    return quant_ppl / fp16_ppl


def ppl_row(case: PplCase) -> dict[str, Any]:
    payload = load_json(case.path)
    quant_key = variant_quant_key(payload, case.variant)
    return {
        "variant": case.variant,
        "label": case.label,
        "path": str(case.path),
        "passed": bool(payload.get("passed", False)),
        "model": payload.get("model"),
        "package": payload.get("package", {}),
        "tokens": int(payload.get("tokens", 0) or 0),
        "prompt_count": int(payload.get("prompt_count", 0) or 0),
        "fp16_ppl": finite(payload.get("fp16", {}).get("ppl")),
        "quant_ppl": finite(payload.get(quant_key, {}).get("ppl")),
        "ppl_ratio_vs_fp16": ppl_ratio(payload, case.variant),
        "failures": payload.get("failures", []),
    }


def task_rows(task_matrix: dict[str, Any], variant: str) -> list[dict[str, Any]]:
    return [row for row in task_matrix.get("cases", []) or [] if row.get("variant") == variant]


def task_summary_for_variant(task_matrix: dict[str, Any], variant: str) -> dict[str, Any]:
    rows = task_rows(task_matrix, variant)
    total_tasks = sum(int(row.get("tasks", 0) or 0) for row in rows)
    total_passes = sum(int(row.get("passes", 0) or 0) for row in rows)
    max_vram = max((finite(row.get("guard_max_memory_used_ratio")) or 0.0 for row in rows), default=None)
    formats = sorted({str(row.get("task_format")) for row in rows})
    return {
        "variant": variant,
        "case_count": len(rows),
        "formats": formats,
        "total_tasks": total_tasks,
        "total_passes": total_passes,
        "mean_accuracy": total_passes / total_tasks if total_tasks else None,
        "max_guard_vram_ratio": max_vram,
    }


def comparison_for_variant(task_matrix: dict[str, Any], variant: str) -> dict[str, Any]:
    comparisons = [row for row in task_matrix.get("comparisons", []) or [] if row.get("variant") == variant]
    max_drop = max((finite(row.get("accuracy_drop_vs_baseline")) or 0.0 for row in comparisons), default=None)
    zero_formats = [
        row.get("task_format")
        for row in comparisons
        if finite(row.get("baseline_accuracy")) == 0.0
    ]
    return {
        "variant": variant,
        "comparison_count": len(comparisons),
        "max_accuracy_drop_vs_fp16": max_drop,
        "zero_fp16_accuracy_formats": sorted({str(item) for item in zero_formats}),
    }


def runtime_summary_for_variant(runtime_profile: dict[str, Any], variant: str) -> dict[str, Any]:
    profiles = runtime_profile.get("profiles", {})
    comparisons = runtime_profile.get("comparisons", []) or []
    profile = profiles.get(variant, {})
    comparison = next((row for row in comparisons if row.get("variant") == variant), {})
    return {
        "variant": variant,
        "total_tasks": int(profile.get("total_tasks", 0) or 0),
        "mean_tokens_per_second": finite(profile.get("mean_tokens_per_second")),
        "mean_ttft_seconds": finite(profile.get("mean_ttft_seconds")),
        "max_guard_vram_ratio": finite(profile.get("max_guard_vram_ratio")),
        "tokens_per_second_ratio_vs_fp16": finite(comparison.get("tokens_per_second_ratio_vs_baseline")),
        "ttft_ratio_vs_fp16": finite(comparison.get("ttft_ratio_vs_baseline")),
        "vram_ratio_vs_fp16": finite(comparison.get("vram_ratio_vs_baseline")),
    }


def mean(values: list[float]) -> float | None:
    clean = [value for value in values if finite(value) is not None]
    if not clean:
        return None
    return sum(clean) / len(clean)


def build_gate(
    ppl_cases: list[PplCase],
    *,
    task_matrix_path: Path,
    runtime_profile_path: Path,
    required_variants: list[str],
    required_ppl_labels: list[str],
    min_total_task_executions: int = 300,
    max_ppl_ratio: float = 1.35,
    max_accuracy_drop: float = 0.25,
    max_guard_vram_ratio: float = 0.90,
) -> dict[str, Any]:
    ppl_rows = [ppl_row(case) for case in ppl_cases]
    task_matrix = load_json(task_matrix_path)
    runtime_profile = load_json(runtime_profile_path)

    variant_rows: dict[str, dict[str, Any]] = {}
    failures: list[str] = []
    for variant in required_variants:
        rows = [row for row in ppl_rows if row["variant"] == variant]
        labels = sorted({str(row["label"]) for row in rows})
        missing_labels = sorted(set(required_ppl_labels).difference(labels))
        task = task_summary_for_variant(task_matrix, variant)
        task_cmp = comparison_for_variant(task_matrix, variant)
        runtime = runtime_summary_for_variant(runtime_profile, variant)
        ratios = [row["ppl_ratio_vs_fp16"] for row in rows if row["ppl_ratio_vs_fp16"] is not None]
        max_ratio = max(ratios) if ratios else None
        variant_rows[variant] = {
            "variant": variant,
            "ppl": rows,
            "ppl_labels": labels,
            "ppl_token_total": sum(int(row.get("tokens", 0) or 0) for row in rows),
            "max_ppl_ratio_vs_fp16": max_ratio,
            "mean_ppl_ratio_vs_fp16": mean(ratios),
            "task": task,
            "task_comparison": task_cmp,
            "runtime": runtime,
        }
        if missing_labels:
            failures.append(f"{variant}: missing PPL labels {missing_labels}")
        if any(not row["passed"] for row in rows):
            failures.append(f"{variant}: at least one PPL input did not pass")
        if max_ratio is None or max_ratio > max_ppl_ratio:
            failures.append(f"{variant}: max PPL ratio above threshold: {max_ratio} > {max_ppl_ratio}")
        if task["total_tasks"] <= 0:
            failures.append(f"{variant}: missing task rows")
        if task_cmp["max_accuracy_drop_vs_fp16"] is None or task_cmp["max_accuracy_drop_vs_fp16"] > max_accuracy_drop:
            failures.append(
                f"{variant}: task accuracy drop above threshold: {task_cmp['max_accuracy_drop_vs_fp16']} > {max_accuracy_drop}"
            )
        if runtime["total_tasks"] <= 0:
            failures.append(f"{variant}: missing runtime profile")
        if runtime["max_guard_vram_ratio"] is None or runtime["max_guard_vram_ratio"] > max_guard_vram_ratio:
            failures.append(f"{variant}: runtime VRAM above guard threshold: {runtime['max_guard_vram_ratio']} > {max_guard_vram_ratio}")

    task_total = int(task_matrix.get("summary", {}).get("total_tasks", 0) or 0)
    runtime_total = int(runtime_profile.get("summary", {}).get("total_tasks", 0) or 0)
    if not task_matrix.get("passed", False):
        failures.append("task matrix did not pass")
    if not runtime_profile.get("passed", False):
        failures.append("runtime profile did not pass")
    if task_total < min_total_task_executions:
        failures.append(f"task executions below threshold: {task_total} < {min_total_task_executions}")
    if runtime_total < min_total_task_executions:
        failures.append(f"runtime task executions below threshold: {runtime_total} < {min_total_task_executions}")

    max_ppl = max(
        (row["max_ppl_ratio_vs_fp16"] for row in variant_rows.values() if row["max_ppl_ratio_vs_fp16"] is not None),
        default=None,
    )
    max_drop = max(
        (
            row["task_comparison"]["max_accuracy_drop_vs_fp16"]
            for row in variant_rows.values()
            if row["task_comparison"]["max_accuracy_drop_vs_fp16"] is not None
        ),
        default=None,
    )
    max_vram_ratio = max(
        (
            row["runtime"]["vram_ratio_vs_fp16"]
            for row in variant_rows.values()
            if row["runtime"]["vram_ratio_vs_fp16"] is not None
        ),
        default=None,
    )
    max_speed_ratio = max(
        (
            row["runtime"]["tokens_per_second_ratio_vs_fp16"]
            for row in variant_rows.values()
            if row["runtime"]["tokens_per_second_ratio_vs_fp16"] is not None
        ),
        default=None,
    )

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "variant_count": len(required_variants),
            "variants": required_variants,
            "ppl_slice_count": len(ppl_rows),
            "required_ppl_labels": required_ppl_labels,
            "total_ppl_tokens": sum(int(row.get("tokens", 0) or 0) for row in ppl_rows),
            "task_total_executions": task_total,
            "runtime_total_executions": runtime_total,
            "max_ppl_ratio_vs_fp16": max_ppl,
            "max_accuracy_drop_vs_fp16": max_drop,
            "max_vram_ratio_vs_fp16": max_vram_ratio,
            "max_tokens_per_second_ratio_vs_fp16": max_speed_ratio,
            "max_guard_vram_ratio": runtime_profile.get("summary", {}).get("max_guard_vram_ratio"),
            "max_ppl_ratio_threshold": max_ppl_ratio,
            "max_accuracy_drop_threshold": max_accuracy_drop,
            "max_guard_vram_threshold": max_guard_vram_ratio,
        },
        "variant_rows": variant_rows,
        "source_paths": {
            "task_matrix": str(task_matrix_path),
            "runtime_profile": str(runtime_profile_path),
            "ppl_cases": [str(case.path) for case in ppl_cases],
        },
        "failures": failures,
        "claim_boundary": (
            "Valid claim: the local official AutoAWQ and GPTQModel Qwen2.5-0.5B W4/G128 artifacts "
            "have matched public-calibration PPL slices, matched 50-row public MMLU/GSM8K task execution, "
            "and PC-side runtime/VRAM profiles. Invalid claim: this is a leaderboard-scale or large-model "
            "competitive AWQ/GPTQ baseline, a production runtime, mobile deployment, energy result, or SOTA PTQ evidence."
        ),
    }


def fmt(value: Any, digits: int = 4) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}f}"


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    lines = [
        "# Official PTQ Matched Baseline Pack Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- variants: `{', '.join(summary['variants'])}`",
        f"- PPL slices: `{summary['ppl_slice_count']}`",
        f"- total PPL tokens: `{summary['total_ppl_tokens']}`",
        f"- task executions: `{summary['task_total_executions']}`",
        f"- runtime executions: `{summary['runtime_total_executions']}`",
        f"- max PPL ratio vs FP16: `{fmt(summary['max_ppl_ratio_vs_fp16'])}`",
        f"- max task accuracy drop vs FP16: `{fmt(summary['max_accuracy_drop_vs_fp16'])}`",
        f"- max VRAM ratio vs FP16: `{fmt(summary['max_vram_ratio_vs_fp16'])}`",
        f"- max tokens/s ratio vs FP16: `{fmt(summary['max_tokens_per_second_ratio_vs_fp16'])}`",
        "",
        "## Variant Evidence",
        "",
        "| variant | PPL labels | max PPL ratio | task rows | max task drop | tok/s ratio | VRAM ratio |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for variant, row in report["variant_rows"].items():
        runtime = row["runtime"]
        lines.append(
            f"| `{variant}` | `{','.join(row['ppl_labels'])}` | {fmt(row['max_ppl_ratio_vs_fp16'])} | "
            f"{row['task']['total_tasks']} | {fmt(row['task_comparison']['max_accuracy_drop_vs_fp16'])} | "
            f"{fmt(runtime['tokens_per_second_ratio_vs_fp16'])} | {fmt(runtime['vram_ratio_vs_fp16'])} |"
        )
    lines.extend(
        [
            "",
            "## PPL Slices",
            "",
            "| variant | label | tokens | FP16 PPL | quant PPL | ratio |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for variant, row in report["variant_rows"].items():
        for ppl in row["ppl"]:
            lines.append(
                f"| `{variant}` | `{ppl['label']}` | {ppl['tokens']} | {fmt(ppl['fp16_ppl'], 6)} | "
                f"{fmt(ppl['quant_ppl'], 6)} | {fmt(ppl['ppl_ratio_vs_fp16'], 6)} |"
            )
    lines.extend(["", "## Failures", ""])
    if report["failures"]:
        lines.extend(f"- {failure}" for failure in report["failures"])
    else:
        lines.append("- none")
    lines.extend(["", "## Claim Boundary", "", report["claim_boundary"]])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate a matched official PTQ evidence pack.")
    parser.add_argument("--ppl-case", action="append", required=True, help="VARIANT:LABEL=PATH")
    parser.add_argument("--task-matrix-json", type=Path, required=True)
    parser.add_argument("--runtime-profile-json", type=Path, required=True)
    parser.add_argument("--required-variants", default="autoawq,gptqmodel")
    parser.add_argument("--required-ppl-labels", default="wikitext2,c4")
    parser.add_argument("--min-total-task-executions", type=int, default=300)
    parser.add_argument("--max-ppl-ratio", type=float, default=1.35)
    parser.add_argument("--max-accuracy-drop", type=float, default=0.25)
    parser.add_argument("--max-guard-vram-ratio", type=float, default=0.90)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    report = build_gate(
        [parse_ppl_case(raw) for raw in args.ppl_case],
        task_matrix_path=args.task_matrix_json,
        runtime_profile_path=args.runtime_profile_json,
        required_variants=[item.strip() for item in args.required_variants.split(",") if item.strip()],
        required_ppl_labels=[item.strip() for item in args.required_ppl_labels.split(",") if item.strip()],
        min_total_task_executions=args.min_total_task_executions,
        max_ppl_ratio=args.max_ppl_ratio,
        max_accuracy_drop=args.max_accuracy_drop,
        max_guard_vram_ratio=args.max_guard_vram_ratio,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
