#!/usr/bin/env python3
from __future__ import annotations

"""Gate AWQ/GPTQ-style PTQ proxy artifacts."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PTQ_PACKAGE_NAMES = {"optimum", "auto_gptq", "gptqmodel", "awq"}


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
    summaries = payload.get("summaries", [])
    package_rows = payload.get("environment_packages", [])
    available_packages = [
        str(item.get("name"))
        for item in package_rows
        if isinstance(item, dict) and item.get("available") and str(item.get("name")) in PTQ_PACKAGE_NAMES
    ]
    methods = [str(item.get("name")) for item in summaries if isinstance(item, dict)]
    return {
        "label": label,
        "path": str(path),
        "method": payload.get("method"),
        "source": payload.get("source"),
        "record_count": int(payload.get("record_count") or 0),
        "methods": methods,
        "available_packages": available_packages,
        "summaries": summaries if isinstance(summaries, list) else [],
    }


def build_result(cases: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    required_methods = [token.strip().lower() for token in args.required_method_tokens.split(",") if token.strip()]
    if len(cases) < args.min_cases:
        failures.append(f"case count {len(cases)} < required {args.min_cases}")
    for case in cases:
        method = str(case.get("method") or "").lower()
        if args.required_artifact_token.lower() not in method:
            failures.append(f"{case['label']}: artifact method {case.get('method')!r} lacks token {args.required_artifact_token!r}")
        if case["record_count"] < args.min_records:
            failures.append(f"{case['label']}: records {case['record_count']} < required {args.min_records}")
        if args.require_external_package and not case["available_packages"]:
            failures.append(f"{case['label']}: no external PTQ package available in audit snapshot")
        method_names = [name.lower() for name in case["methods"]]
        for token in required_methods:
            if not any(token in name for name in method_names):
                failures.append(f"{case['label']}: method list lacks token {token!r}")
        for summary in case["summaries"]:
            if not isinstance(summary, dict):
                continue
            name = str(summary.get("name") or "")
            avg_bits = float(summary.get("avg_bits") or 0.0)
            target = float(summary.get("target_avg_bits") or args.target_avg_bits)
            protected_ratio = float(summary.get("positive_sensitivity_protected_ratio") or 0.0)
            if avg_bits > target + args.budget_tolerance:
                failures.append(f"{case['label']}:{name}: avg_bits {avg_bits:.6f} > target {target:.6f}")
            if protected_ratio < args.min_protected_ratio:
                failures.append(
                    f"{case['label']}:{name}: protected ratio {protected_ratio:.6f} < required {args.min_protected_ratio:.6f}"
                )
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": len(cases),
            "total_records": sum(case["record_count"] for case in cases),
            "available_package_count": len(
                sorted({pkg for case in cases for pkg in case.get("available_packages", [])})
            ),
            "method_count": sum(len(case["methods"]) for case in cases),
        },
        "cases": cases,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: AWQ/GPTQ-style proxy artifacts exist and an external PTQ ecosystem package is available. "
            "Invalid claim: this is an official AWQ/GPTQ run, GPU PTQ implementation, or SOTA baseline comparison."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        "# AWQ/GPTQ Proxy Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        f"Cases: `{result['summary']['case_count']}`",
        f"Total records: `{result['summary']['total_records']}`",
        "",
        "## Cases",
        "",
        "| case | records | packages | methods |",
        "|---|---:|---|---|",
    ]
    for case in result["cases"]:
        lines.append(
            f"| `{case['label']}` | {case['record_count']} | `{case['available_packages']}` | `{case['methods']}` |"
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
    parser = argparse.ArgumentParser(description="Gate AWQ/GPTQ-style proxy artifacts.")
    parser.add_argument("--case", action="append", required=True, help="LABEL=SUMMARY_JSON")
    parser.add_argument("--min-cases", type=int, default=2)
    parser.add_argument("--min-records", type=int, default=10)
    parser.add_argument("--required-artifact-token", default="awq_gptq")
    parser.add_argument("--required-method-tokens", default="awq,gptq")
    parser.add_argument("--target-avg-bits", type=float, default=4.5)
    parser.add_argument("--min-protected-ratio", type=float, default=0.05)
    parser.add_argument("--budget-tolerance", type=float, default=1.0e-6)
    parser.add_argument("--require-external-package", action="store_true")
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
