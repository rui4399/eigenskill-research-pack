#!/usr/bin/env python3
from __future__ import annotations

"""Gate PC-side runtime profiles derived from official PTQ task smokes.

This is a deliberately narrow runtime-profile gate. It reuses guarded
FP16/AutoAWQ/GPTQModel task-smoke summaries and checks that each variant has
positive TTFT/tokens-per-second measurements plus bounded peak VRAM. It is not a
mobile result, production runtime benchmark, or official AWQ/GPTQ competition.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def finite_float(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def positive_float(value: Any) -> float | None:
    number = finite_float(value)
    if number is None or number <= 0.0:
        return None
    return number


def _mean(values: list[float]) -> float:
    return mean(values) if values else 0.0


def profile_variant(cases: list[dict[str, Any]]) -> dict[str, Any]:
    tps = [float(case["mean_tokens_per_second"]) for case in cases]
    ttft = [float(case["mean_ttft_seconds"]) for case in cases]
    vram_ratio = [float(case["guard_max_memory_used_ratio"]) for case in cases]
    vram_mib = [float(case.get("guard_max_memory_used_mib") or 0.0) for case in cases]
    return {
        "variant": cases[0]["variant"] if cases else "",
        "case_count": len(cases),
        "task_formats": sorted({str(case["task_format"]) for case in cases}),
        "total_tasks": sum(int(case.get("tasks") or 0) for case in cases),
        "total_passes": sum(int(case.get("passes") or 0) for case in cases),
        "mean_accuracy": _mean([float(case.get("accuracy") or 0.0) for case in cases]),
        "mean_tokens_per_second": _mean(tps),
        "min_tokens_per_second": min(tps) if tps else 0.0,
        "mean_ttft_seconds": _mean(ttft),
        "max_ttft_seconds": max(ttft) if ttft else 0.0,
        "max_guard_vram_ratio": max(vram_ratio) if vram_ratio else 0.0,
        "max_guard_vram_mib": max(vram_mib) if vram_mib else 0.0,
        "guard_memory_total_mib": max([float(case.get("guard_memory_total_mib") or 0.0) for case in cases], default=0.0),
    }


def build_profiles(cases: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for case in cases:
        grouped.setdefault(str(case["variant"]), []).append(case)
    return {variant: profile_variant(rows) for variant, rows in sorted(grouped.items())}


def build_comparisons(profiles: dict[str, dict[str, Any]], baseline_variant: str) -> tuple[list[str], list[dict[str, Any]]]:
    failures: list[str] = []
    baseline = profiles.get(baseline_variant)
    if baseline is None:
        return [f"missing baseline variant {baseline_variant}"], []

    baseline_tps = positive_float(baseline.get("mean_tokens_per_second"))
    baseline_ttft = positive_float(baseline.get("mean_ttft_seconds"))
    baseline_vram = positive_float(baseline.get("max_guard_vram_ratio"))
    comparisons: list[dict[str, Any]] = []
    for variant, profile in profiles.items():
        if variant == baseline_variant:
            continue
        tps = positive_float(profile.get("mean_tokens_per_second"))
        ttft = positive_float(profile.get("mean_ttft_seconds"))
        vram = positive_float(profile.get("max_guard_vram_ratio"))
        if baseline_tps is None or baseline_ttft is None or baseline_vram is None:
            failures.append(f"baseline {baseline_variant} has missing positive runtime metrics")
            break
        comparisons.append(
            {
                "variant": variant,
                "baseline_variant": baseline_variant,
                "tokens_per_second_ratio_vs_baseline": (tps / baseline_tps) if tps is not None else None,
                "ttft_ratio_vs_baseline": (ttft / baseline_ttft) if ttft is not None else None,
                "vram_ratio_vs_baseline": (vram / baseline_vram) if vram is not None else None,
                "mean_tokens_per_second": profile.get("mean_tokens_per_second"),
                "baseline_mean_tokens_per_second": baseline.get("mean_tokens_per_second"),
                "mean_ttft_seconds": profile.get("mean_ttft_seconds"),
                "baseline_mean_ttft_seconds": baseline.get("mean_ttft_seconds"),
                "max_guard_vram_ratio": profile.get("max_guard_vram_ratio"),
                "baseline_max_guard_vram_ratio": baseline.get("max_guard_vram_ratio"),
            }
        )
    return failures, comparisons


def build_result(matrix: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    cases = matrix.get("cases", [])
    if not isinstance(cases, list):
        cases = []
    failures: list[str] = []
    source_evidence_label = str(matrix.get("evidence_label") or "task-smoke executions")
    if not matrix.get("passed"):
        failures.append("source task-smoke matrix did not pass")
    profiles = build_profiles([case for case in cases if isinstance(case, dict)])

    for variant in args.required_variants:
        profile = profiles.get(variant)
        if profile is None:
            failures.append(f"missing required variant {variant}")
            continue
        if int(profile["case_count"]) < args.min_cases_per_variant:
            failures.append(f"{variant}: cases {profile['case_count']} < required {args.min_cases_per_variant}")
        if positive_float(profile.get("mean_tokens_per_second")) is None:
            failures.append(f"{variant}: mean tokens/s is not positive")
        elif float(profile["mean_tokens_per_second"]) < args.min_mean_tokens_per_second:
            failures.append(
                f"{variant}: mean tokens/s {profile['mean_tokens_per_second']:.4f} < "
                f"{args.min_mean_tokens_per_second:.4f}"
            )
        if positive_float(profile.get("mean_ttft_seconds")) is None:
            failures.append(f"{variant}: mean TTFT is not positive")
        elif float(profile["mean_ttft_seconds"]) > args.max_mean_ttft_seconds:
            failures.append(
                f"{variant}: mean TTFT {profile['mean_ttft_seconds']:.6f} > {args.max_mean_ttft_seconds:.6f}"
            )
        if float(profile.get("max_guard_vram_ratio") or 0.0) > args.max_memory_ratio:
            failures.append(
                f"{variant}: VRAM ratio {profile['max_guard_vram_ratio']:.4f} > {args.max_memory_ratio:.4f}"
            )

    comparison_failures, comparisons = build_comparisons(profiles, args.baseline_variant)
    failures.extend(comparison_failures)
    summary = {
        "source_case_count": int(matrix.get("summary", {}).get("case_count") or len(cases))
        if isinstance(matrix.get("summary"), dict)
        else len(cases),
        "variant_count": len(profiles),
        "variants": sorted(profiles),
        "baseline_variant": args.baseline_variant,
        "total_cases": sum(int(profile["case_count"]) for profile in profiles.values()),
        "total_tasks": sum(int(profile["total_tasks"]) for profile in profiles.values()),
        "mean_tokens_per_second": _mean([float(profile["mean_tokens_per_second"]) for profile in profiles.values()]),
        "mean_ttft_seconds": _mean([float(profile["mean_ttft_seconds"]) for profile in profiles.values()]),
        "max_guard_vram_ratio": max((float(profile["max_guard_vram_ratio"]) for profile in profiles.values()), default=0.0),
        "max_guard_vram_mib": max((float(profile["max_guard_vram_mib"]) for profile in profiles.values()), default=0.0),
    }
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "source_evidence_label": source_evidence_label,
        "summary": summary,
        "profiles": profiles,
        "comparisons": comparisons,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: this is a PC-side runtime profile over already-guarded official PTQ "
            f"{source_evidence_label}, reporting TTFT, tokens/s, and peak VRAM for FP16 and "
            "official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, "
            "production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    lines = [
        "# Official PTQ Runtime Profile Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- variants: `{summary['variants']}`",
        f"- total cases: `{summary['total_cases']}`",
        f"- total tasks: `{summary['total_tasks']}`",
        f"- mean tokens/s across variants: `{summary['mean_tokens_per_second']:.4f}`",
        f"- mean TTFT across variants: `{summary['mean_ttft_seconds']:.6f}` s",
        f"- peak guard VRAM ratio: `{summary['max_guard_vram_ratio']:.4f}`",
        f"- peak guard VRAM MiB: `{summary['max_guard_vram_mib']:.0f}`",
        "",
        "## Variant Profiles",
        "",
        "| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for variant, profile in result["profiles"].items():
        formats = ",".join(profile["task_formats"])
        lines.append(
            f"| `{variant}` | {profile['case_count']} | {profile['total_tasks']} | "
            f"{profile['mean_tokens_per_second']:.4f} | {profile['mean_ttft_seconds']:.6f} | "
            f"{profile['max_guard_vram_ratio']:.4f} | {profile['max_guard_vram_mib']:.0f} | `{formats}` |"
        )
    lines.extend(["", "## Comparisons Against Baseline", ""])
    lines.extend(["| variant | tok/s ratio | TTFT ratio | VRAM ratio |", "|---|---:|---:|---:|"])
    for row in result["comparisons"]:
        lines.append(
            f"| `{row['variant']}` | {row['tokens_per_second_ratio_vs_baseline']:.4f} | "
            f"{row['ttft_ratio_vs_baseline']:.4f} | {row['vram_ratio_vs_baseline']:.4f} |"
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
    parser = argparse.ArgumentParser(description="Gate official PTQ PC-side runtime profiles.")
    parser.add_argument("--matrix-json", type=Path, required=True)
    parser.add_argument("--baseline-variant", default="fp16")
    parser.add_argument("--required-variant", dest="required_variants", action="append", default=[])
    parser.add_argument("--min-cases-per-variant", type=int, default=2)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--min-mean-tokens-per-second", type=float, default=1.0)
    parser.add_argument("--max-mean-ttft-seconds", type=float, default=2.0)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()
    if not args.required_variants:
        args.required_variants = ["fp16", "autoawq", "gptqmodel"]

    result = build_result(load_json(args.matrix_json), args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "failures": result["failures"]}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
