#!/usr/bin/env python3
from __future__ import annotations

"""Gate QuaRot/SpinQuant-style rotation-family proxy artifacts."""

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
    policy_hist = payload.get("policy_hist", {})
    return {
        "label": label,
        "path": str(path),
        "method": payload.get("method"),
        "source": payload.get("source"),
        "record_count": int(payload.get("record_count") or 0),
        "rotated_count": int(payload.get("rotated_count") or 0),
        "rotation_budget_fraction": float(payload.get("rotation_budget_fraction") or 0.0),
        "rotated_cost_fraction": float(payload.get("rotated_cost_fraction") or 0.0),
        "base_positive_sensitivity": float(payload.get("base_positive_sensitivity") or 0.0),
        "projected_positive_sensitivity_after_rotation": float(
            payload.get("projected_positive_sensitivity_after_rotation") or 0.0
        ),
        "projected_reduction_ratio": float(payload.get("projected_reduction_ratio") or 0.0),
        "policy_hist": policy_hist if isinstance(policy_hist, dict) else {},
    }


def build_result(cases: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    required_policy_tokens = [token.strip().lower() for token in args.required_policy_tokens.split(",") if token.strip()]
    if len(cases) < args.min_cases:
        failures.append(f"case count {len(cases)} < required {args.min_cases}")
    for case in cases:
        method = str(case.get("method") or "").lower()
        if args.required_method_token.lower() not in method:
            failures.append(f"{case['label']}: method {case.get('method')!r} lacks token {args.required_method_token!r}")
        if case["record_count"] < args.min_records:
            failures.append(f"{case['label']}: records {case['record_count']} < required {args.min_records}")
        if case["rotated_count"] < args.min_rotated:
            failures.append(f"{case['label']}: rotated_count {case['rotated_count']} < required {args.min_rotated}")
        if case["rotated_cost_fraction"] > case["rotation_budget_fraction"] + args.budget_tolerance:
            failures.append(
                f"{case['label']}: rotated cost {case['rotated_cost_fraction']:.6f} > "
                f"budget {case['rotation_budget_fraction']:.6f}"
            )
        if case["projected_reduction_ratio"] < args.min_reduction_ratio:
            failures.append(
                f"{case['label']}: projected reduction {case['projected_reduction_ratio']:.6f} < "
                f"required {args.min_reduction_ratio:.6f}"
            )
        policy_names = {str(name).lower() for name, count in case["policy_hist"].items() if int(count) > 0}
        for token in required_policy_tokens:
            if not any(token in name for name in policy_names):
                failures.append(f"{case['label']}: policy histogram lacks token {token!r}")
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": len(cases),
            "total_records": sum(case["record_count"] for case in cases),
            "total_rotated": sum(case["rotated_count"] for case in cases),
            "max_rotated_cost_fraction": max((case["rotated_cost_fraction"] for case in cases), default=0.0),
            "mean_projected_reduction_ratio": (
                sum(case["projected_reduction_ratio"] for case in cases) / len(cases) if cases else 0.0
            ),
        },
        "cases": cases,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: QuaRot/SpinQuant-style rotation-family proxy artifacts exist, rotate measured modules "
            "under budget, and record projected sensitivity reduction. Invalid claim: this is a faithful official "
            "QuaRot/SpinQuant reproduction or proof of activation-rotation quality retention."
        ),
    }


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        "# Rotation Family Proxy Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        f"Cases: `{result['summary']['case_count']}`",
        f"Total records: `{result['summary']['total_records']}`",
        f"Total rotated: `{result['summary']['total_rotated']}`",
        "",
        "## Cases",
        "",
        "| case | method | records | rotated | cost frac | budget | reduction | policies |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for case in result["cases"]:
        lines.append(
            f"| `{case['label']}` | `{case['method']}` | {case['record_count']} | {case['rotated_count']} | "
            f"{case['rotated_cost_fraction']:.6f} | {case['rotation_budget_fraction']:.6f} | "
            f"{case['projected_reduction_ratio']:.6f} | `{case['policy_hist']}` |"
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
    parser = argparse.ArgumentParser(description="Gate rotation-family proxy artifacts.")
    parser.add_argument("--case", action="append", required=True, help="LABEL=SUMMARY_JSON")
    parser.add_argument("--min-cases", type=int, default=2)
    parser.add_argument("--min-records", type=int, default=10)
    parser.add_argument("--min-rotated", type=int, default=1)
    parser.add_argument("--required-method-token", default="rotation")
    parser.add_argument("--required-policy-tokens", default="quarot,spinquant")
    parser.add_argument("--min-reduction-ratio", type=float, default=0.01)
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
