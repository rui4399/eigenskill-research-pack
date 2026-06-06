#!/usr/bin/env python3
from __future__ import annotations

"""Build a task-type-conditioned role-policy gate from regression analysis.

This is a diagnostic selector. It does not prove deployability; it converts
baseline/fused flip rows into a reproducible list of task types where a
candidate role is unsafe.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _candidate_type_row(candidate: dict[str, Any], task_type: str) -> dict[str, Any]:
    summary = candidate.get("type_summary", {}).get(task_type, {})
    baseline_passes = int(summary.get("baseline_passes", 0))
    fused_passes = int(summary.get("fused_passes", 0))
    regressions = int(summary.get("regressions", 0))
    fixes = int(summary.get("fixes", 0))
    return {
        "label": str(candidate["label"]),
        "speedup": float(candidate.get("speedup") or 0.0),
        "tasks": int(summary.get("tasks", 0)),
        "baseline_passes": baseline_passes,
        "fused_passes": fused_passes,
        "pass_delta": fused_passes - baseline_passes,
        "regressions": regressions,
        "fixes": fixes,
        "safe": regressions == 0 and fused_passes >= baseline_passes,
    }


def _task_types(reports: list[dict[str, Any]]) -> list[str]:
    names: set[str] = set()
    for report in reports:
        names.update(str(name) for name in report.get("type_summary", {}))
    return sorted(names)


def build_policy(regression_report: dict[str, Any]) -> dict[str, Any]:
    reports = list(regression_report.get("reports", []))
    policies: dict[str, dict[str, Any]] = {}
    for task_type in _task_types(reports):
        rows = [_candidate_type_row(candidate, task_type) for candidate in reports if task_type in candidate.get("type_summary", {})]
        safe_rows = [row for row in rows if row["safe"]]
        safe_rows.sort(key=lambda row: (row["speedup"], row["fused_passes"], row["label"]), reverse=True)
        rejected = sorted(row["label"] for row in rows if not row["safe"])
        recommended = safe_rows[0] if safe_rows else None
        policies[task_type] = {
            "decision": "type_safe_candidate" if recommended else "no_safe_candidate",
            "recommended_candidate": recommended["label"] if recommended else None,
            "recommended_speedup": recommended["speedup"] if recommended else None,
            "safe_candidates": [row["label"] for row in safe_rows],
            "rejected_candidates": rejected,
            "candidate_rows": rows,
        }

    candidate_rejections = {
        str(candidate["label"]): {
            "total_regressions": len(candidate.get("regressions", [])),
            "regression_types": sorted({str(row.get("type", "")) for row in candidate.get("regressions", [])}),
        }
        for candidate in reports
    }
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source_date": regression_report.get("date"),
        "task_type_policies": policies,
        "candidate_rejections": candidate_rejections,
        "interpretation": (
            "Use this as a failure-aware diagnostic gate. A per-task-type recommendation must be "
            "validated on a fresh split before it becomes a routing policy."
        ),
    }


def _fmt_speed(value: Any) -> str:
    if value is None:
        return "n/a"
    return f"{float(value):.4f}x"


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        "# Failure-Aware Role Policy Gate",
        "",
        f"Date: `{result['date']}`",
        "",
        result["interpretation"],
        "",
        "## Task-Type Policies",
        "",
        "| task type | decision | recommended | speed | safe candidates | rejected candidates |",
        "|---|---|---|---:|---|---|",
    ]
    for task_type, row in result["task_type_policies"].items():
        lines.append(
            f"| `{task_type}` | `{row['decision']}` | `{row['recommended_candidate'] or 'n/a'}` | "
            f"{_fmt_speed(row['recommended_speedup'])} | `{', '.join(row['safe_candidates']) or 'n/a'}` | "
            f"`{', '.join(row['rejected_candidates']) or 'n/a'}` |"
        )
    lines.extend(
        [
            "",
            "## Candidate Rejections",
            "",
            "| candidate | total regressions | regression types |",
            "|---|---:|---|",
        ]
    )
    for label, row in result["candidate_rejections"].items():
        lines.append(f"| `{label}` | {row['total_regressions']} | `{', '.join(row['regression_types']) or 'n/a'}` |")
    lines.extend(
        [
            "",
            "## Use",
            "",
            "- Treat `no_safe_candidate` as a hard stop for that task type under the tested policies.",
            "- Treat a `type_safe_candidate` as a next experiment, not as a deployment claim.",
            "- Validate any task-type-conditioned policy on a fresh split before adding it to a paper claim.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build a failure-aware role policy from regression analysis JSON.")
    parser.add_argument("--regression-json", required=True)
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args(argv)

    result = build_policy(load_json(Path(args.regression_json)))
    out_json = Path(args.out_json)
    out_md = Path(args.out_md)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(out_md, result)
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "task_types": len(result["task_type_policies"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
