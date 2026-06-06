#!/usr/bin/env python3
from __future__ import annotations

"""Gate Q-Palette/IMPQ-style allocation proxy artifacts.

This gate checks that a measured-sensitivity rate-distortion allocation proxy
exists and respects its bit budget. It is not a claim of faithful official
reimplementation.
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


def case_summary(label: str, path: Path) -> dict[str, Any]:
    payload = load_json(path)
    records = payload.get("records", [])
    return {
        "label": label,
        "path": str(path),
        "method": payload.get("method"),
        "source": payload.get("source"),
        "record_count": len(records),
        "target_avg_bits": float(payload.get("target_avg_bits") or 0.0),
        "avg_bits": float(payload.get("avg_bits") or 0.0),
        "budget_satisfied": bool(payload.get("budget_satisfied")),
        "objective_distortion": float(payload.get("objective_distortion") or 0.0),
        "bit_hist": payload.get("bit_hist", {}),
    }


def build_result(cases: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    if len(cases) < args.min_cases:
        failures.append(f"case count {len(cases)} < required {args.min_cases}")
    for case in cases:
        method = str(case.get("method") or "").lower()
        if args.required_method_token.lower() not in method:
            failures.append(f"{case['label']}: method {case.get('method')!r} lacks token {args.required_method_token!r}")
        if case["record_count"] < args.min_records:
            failures.append(f"{case['label']}: records {case['record_count']} < required {args.min_records}")
        if not case["budget_satisfied"]:
            failures.append(f"{case['label']}: budget_satisfied is false")
        if case["avg_bits"] > case["target_avg_bits"] + args.budget_tolerance:
            failures.append(
                f"{case['label']}: avg_bits {case['avg_bits']:.6f} > target {case['target_avg_bits']:.6f}"
            )
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": len(cases),
            "total_records": sum(case["record_count"] for case in cases),
            "max_avg_bits": max((case["avg_bits"] for case in cases), default=0.0),
            "max_target_avg_bits": max((case["target_avg_bits"] for case in cases), default=0.0),
        },
        "cases": cases,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: Q-Palette-style measured-sensitivity allocation proxy artifacts exist and satisfy budget. "
            "Invalid claim: this is a faithful official Q-Palette/IMPQ/WINDQuant reproduction."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        "# Allocation Family Proxy Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        f"Cases: `{result['summary']['case_count']}`",
        f"Total records: `{result['summary']['total_records']}`",
        "",
        "## Cases",
        "",
        "| case | method | records | avg bits | target bits | budget | bit hist |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for case in result["cases"]:
        lines.append(
            f"| `{case['label']}` | `{case['method']}` | {case['record_count']} | "
            f"{case['avg_bits']:.6f} | {case['target_avg_bits']:.6f} | "
            f"{str(case['budget_satisfied']).lower()} | `{case['bit_hist']}` |"
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
    parser = argparse.ArgumentParser(description="Gate allocation-family proxy artifacts.")
    parser.add_argument("--case", action="append", required=True, help="LABEL=SUMMARY_JSON")
    parser.add_argument("--min-cases", type=int, default=2)
    parser.add_argument("--min-records", type=int, default=10)
    parser.add_argument("--required-method-token", default="q_palette")
    parser.add_argument("--budget-tolerance", type=float, default=1.0e-6)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    cases = [case_summary(label, path) for label, path in map(parse_case_spec, args.case)]
    result = build_result(cases, args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "out_json": str(args.out_json)}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
