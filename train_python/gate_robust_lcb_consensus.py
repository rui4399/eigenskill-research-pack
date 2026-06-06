#!/usr/bin/env python3
from __future__ import annotations

"""Gate robust-LCB consensus allocation artifacts.

This gate is intentionally narrow. It verifies that robust-LCB consensus
allocation summaries exist, use the expected policy/key, satisfy the declared
bit budget, and expose the robustness fields needed for paper-safe analysis.
It does not claim downstream quality or SOTA competitiveness.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_case_spec(spec: str) -> tuple[str, Path]:
    if "=" not in spec:
        raise ValueError(f"case must be LABEL=SUMMARY_JSON: {spec}")
    label, raw_path = spec.split("=", 1)
    if not label.strip() or not raw_path.strip():
        raise ValueError(f"case must be LABEL=SUMMARY_JSON: {spec}")
    return label.strip(), Path(raw_path)


def summary_for_policy(payload: dict[str, Any], allocation_key: str) -> dict[str, Any]:
    for summary in payload.get("summaries", []) or []:
        if summary.get("name") == allocation_key:
            return summary
    return {}


def high_bit_count(payload: dict[str, Any], allocation_key: str, high_bits: int = 8) -> int:
    allocation = payload.get("allocations", {}).get(allocation_key, [])
    return sum(1 for bit in allocation if int(bit) == high_bits)


def consistent_selected_count(payload: dict[str, Any]) -> int:
    count = 0
    for row in payload.get("selected_modules", []) or []:
        ratio = float(row.get("calibration_consistency_ratio") or 0.0)
        lcb = float(row.get("robust_lcb_positive_delta_nll") or 0.0)
        score = float(row.get("robust_lcb_score_delta_per_cost") or 0.0)
        if ratio > 0.0 and lcb > 0.0 and score >= 0.0:
            count += 1
    return count


def robust_field_count(payload: dict[str, Any]) -> int:
    required = {
        "robust_lcb_positive_delta_nll",
        "robust_lcb_score_delta_per_cost",
        "calibration_consistency_ratio",
    }
    count = 0
    for row in payload.get("selected_modules", []) or []:
        if required.issubset(row.keys()):
            count += 1
    return count


def case_summary(label: str, path: str | Path, payload: dict[str, Any], allocation_key: str | None = None) -> dict[str, Any]:
    key = allocation_key or str(payload.get("policy_name") or "")
    summary = summary_for_policy(payload, key)
    return {
        "label": label,
        "path": str(path),
        "model": payload.get("model", ""),
        "policy": payload.get("policy"),
        "policy_name": payload.get("policy_name"),
        "score_key": payload.get("score_key"),
        "allocation_key": key,
        "avg_bits": float(summary.get("avg_bits") or 0.0),
        "budget_avg_bits": float(payload.get("budget_avg_bits") or summary.get("budget_avg_bits") or 0.0),
        "bit_hist": summary.get("bit_hist", {}),
        "high_bit_modules": high_bit_count(payload, key),
        "selected_modules": len(payload.get("selected_modules", []) or []),
        "robust_field_rows": robust_field_count(payload),
        "consistent_selected_modules": consistent_selected_count(payload),
        "protected_ratio": float(summary.get("positive_delta_nll_protected_ratio") or 0.0),
    }


def build_result(cases: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    if len(cases) < args.min_cases:
        failures.append(f"case count {len(cases)} < required {args.min_cases}")
    for case in cases:
        if case["policy"] != args.required_policy:
            failures.append(f"{case['label']}: policy {case['policy']!r} != {args.required_policy!r}")
        if case["policy_name"] != args.required_allocation_key:
            failures.append(
                f"{case['label']}: policy_name {case['policy_name']!r} != {args.required_allocation_key!r}"
            )
        if case["allocation_key"] != args.required_allocation_key:
            failures.append(
                f"{case['label']}: allocation key {case['allocation_key']!r} != {args.required_allocation_key!r}"
            )
        if case["avg_bits"] > args.target_avg_bits + args.budget_tolerance:
            failures.append(
                f"{case['label']}: avg_bits {case['avg_bits']:.6f} > target {args.target_avg_bits:.6f}"
            )
        if case["high_bit_modules"] < args.min_high_bit_modules:
            failures.append(
                f"{case['label']}: high-bit modules {case['high_bit_modules']} < required {args.min_high_bit_modules}"
            )
        if case["robust_field_rows"] < case["selected_modules"]:
            failures.append(
                f"{case['label']}: robust fields present for {case['robust_field_rows']}/{case['selected_modules']} selected modules"
            )
        if case["consistent_selected_modules"] < args.min_consistent_selected:
            failures.append(
                f"{case['label']}: consistent selected modules {case['consistent_selected_modules']} < required {args.min_consistent_selected}"
            )

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": len(cases),
            "max_avg_bits": max((case["avg_bits"] for case in cases), default=0.0),
            "target_bits": args.target_avg_bits,
            "total_high_bit_modules": sum(case["high_bit_modules"] for case in cases),
            "consistent_selected_modules": sum(case["consistent_selected_modules"] for case in cases),
            "selected_modules": sum(case["selected_modules"] for case in cases),
        },
        "cases": cases,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: robust-LCB consensus allocation artifacts exist across the gated model family, "
            "respect the configured average-bit budget, and expose selected-module consistency evidence. "
            "Invalid claim: this gate proves downstream PPL, task accuracy, mobile deployment, or SOTA quality."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        "# Robust LCB Consensus Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        f"Cases: `{result['summary']['case_count']}`",
        f"Total high-bit modules: `{result['summary']['total_high_bit_modules']}`",
        f"Consistent selected modules: `{result['summary']['consistent_selected_modules']}`",
        "",
        "## Cases",
        "",
        "| case | model | avg bits | high-bit modules | selected | consistent selected | protected ratio | bit hist | source |",
        "|---|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for case in result["cases"]:
        lines.append(
            f"| `{case['label']}` | `{case['model']}` | {case['avg_bits']:.6f} | "
            f"{case['high_bit_modules']} | {case['selected_modules']} | "
            f"{case['consistent_selected_modules']} | {case['protected_ratio']:.6f} | "
            f"`{case['bit_hist']}` | `{str(case['path']).replace(chr(92), '/')}` |"
        )
    lines.extend(["", "## Failures", ""])
    if result["failures"]:
        for failure in result["failures"]:
            lines.append(f"- {failure}")
    else:
        lines.append("- none")
    lines.extend(["", "## Claim Boundary", "", f"- {result['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate robust-LCB consensus allocation artifacts.")
    parser.add_argument("--case", action="append", required=True, help="LABEL=SUMMARY_JSON")
    parser.add_argument("--min-cases", type=int, default=3)
    parser.add_argument("--required-policy", default="robust_lcb")
    parser.add_argument("--required-allocation-key", default="loss_sensitive_robust_lcb_consensus_4to8")
    parser.add_argument("--target-avg-bits", type=float, default=4.5)
    parser.add_argument("--budget-tolerance", type=float, default=1.0e-6)
    parser.add_argument("--min-high-bit-modules", type=int, default=1)
    parser.add_argument("--min-consistent-selected", type=int, default=1)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    cases = []
    for label, path in map(parse_case_spec, args.case):
        cases.append(case_summary(label, path, load_json(path), args.required_allocation_key))
    result = build_result(cases, args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "out_json": str(args.out_json)}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
