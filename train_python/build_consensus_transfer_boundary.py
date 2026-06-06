#!/usr/bin/env python3
from __future__ import annotations

"""Audit consensus allocation transfer against single-split policies.

This is a boundary gate: it checks whether consensus avoids the worse
single-split policy and reports any regret versus the best single-split policy.
It should not be read as proof that consensus is always minimax-optimal.
"""

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CaseSpec:
    label: str
    left_eval: Path
    right_eval: Path
    left_policy: str = "wikitext_loss_sensitive"
    right_policy: str = "c4_loss_sensitive"
    consensus_policy: str = "wikitext_c4_consensus"


def finite(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def parse_case(raw: str) -> CaseSpec:
    parts = raw.split("=")
    if len(parts) not in (3, 6):
        raise ValueError(
            "case must be LABEL=LEFT_EVAL_JSON=RIGHT_EVAL_JSON or "
            "LABEL=LEFT_EVAL_JSON=RIGHT_EVAL_JSON=LEFT_POLICY=RIGHT_POLICY=CONSENSUS_POLICY"
        )
    label, left_eval, right_eval = [part.strip() for part in parts[:3]]
    if not label or not left_eval or not right_eval:
        raise ValueError(f"empty label/path in case spec: {raw}")
    if len(parts) == 6:
        left_policy, right_policy, consensus_policy = [part.strip() for part in parts[3:]]
        if not left_policy or not right_policy or not consensus_policy:
            raise ValueError(f"empty policy in case spec: {raw}")
        return CaseSpec(label, Path(left_eval), Path(right_eval), left_policy, right_policy, consensus_policy)
    return CaseSpec(label, Path(left_eval), Path(right_eval))


def read_ppl_rows(path: Path) -> dict[str, float]:
    data = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, float] = {}
    for row in data.get("results", []):
        if not isinstance(row, dict):
            continue
        name = str(row.get("name", "")).strip()
        metrics = row.get("metrics", {})
        ppl = finite(metrics.get("ppl") if isinstance(metrics, dict) else None)
        if name and ppl is not None:
            out[name] = ppl
    if not out:
        raise ValueError(f"{path}: no finite PPL result rows")
    return out


def require_row(rows: dict[str, float], name: str, path: Path) -> float:
    if name not in rows:
        raise ValueError(f"{path}: missing policy row {name}")
    return rows[name]


def slice_row(label: str, path: Path, rows: dict[str, float], spec: CaseSpec) -> dict[str, Any]:
    left = require_row(rows, spec.left_policy, path)
    right = require_row(rows, spec.right_policy, path)
    consensus = require_row(rows, spec.consensus_policy, path)
    best_single = min(left, right)
    worst_single = max(left, right)
    return {
        "slice": label,
        "path": str(path),
        "left_policy": spec.left_policy,
        "right_policy": spec.right_policy,
        "consensus_policy": spec.consensus_policy,
        "left_single_ppl": left,
        "right_single_ppl": right,
        "consensus_ppl": consensus,
        "best_single_ppl": best_single,
        "worst_single_ppl": worst_single,
        "consensus_margin_vs_left_single": left - consensus,
        "consensus_margin_vs_right_single": right - consensus,
        "consensus_margin_vs_best_single": best_single - consensus,
        "consensus_margin_vs_worst_single": worst_single - consensus,
        "consensus_regret_vs_best_single": consensus - best_single,
        "consensus_beats_left_single": consensus < left,
        "consensus_beats_right_single": consensus < right,
        "consensus_beats_best_single": consensus < best_single,
        "consensus_beats_worst_single": consensus < worst_single,
    }


def build_case(label: str, left_eval: Path, right_eval: Path, *, left_policy: str = "wikitext_loss_sensitive", right_policy: str = "c4_loss_sensitive", consensus_policy: str = "wikitext_c4_consensus") -> dict[str, Any]:
    spec = CaseSpec(label, left_eval, right_eval, left_policy, right_policy, consensus_policy)
    slices = [
        slice_row("left_eval", left_eval, read_ppl_rows(left_eval), spec),
        slice_row("right_eval", right_eval, read_ppl_rows(right_eval), spec),
    ]
    left_margins = [row["consensus_margin_vs_left_single"] for row in slices]
    right_margins = [row["consensus_margin_vs_right_single"] for row in slices]
    worst_margins = [row["consensus_margin_vs_worst_single"] for row in slices]
    best_regrets = [row["consensus_regret_vs_best_single"] for row in slices]
    return {
        "label": label,
        "left_eval": str(left_eval),
        "right_eval": str(right_eval),
        "left_policy": left_policy,
        "right_policy": right_policy,
        "consensus_policy": consensus_policy,
        "slice_count": len(slices),
        "consensus_wins_vs_left_single": sum(1 for row in slices if row["consensus_beats_left_single"]),
        "consensus_wins_vs_right_single": sum(1 for row in slices if row["consensus_beats_right_single"]),
        "consensus_wins_vs_best_single": sum(1 for row in slices if row["consensus_beats_best_single"]),
        "consensus_wins_vs_worst_single": sum(1 for row in slices if row["consensus_beats_worst_single"]),
        "mean_margin_vs_left_single": mean(left_margins),
        "mean_margin_vs_right_single": mean(right_margins),
        "mean_margin_vs_worst_single": mean(worst_margins),
        "min_margin_vs_worst_single": min(worst_margins) if worst_margins else None,
        "mean_regret_vs_best_single": mean(best_regrets),
        "max_regret_vs_best_single": max(best_regrets) if best_regrets else None,
        "slices": slices,
    }


def build_report(
    cases: list[CaseSpec],
    *,
    min_cases: int = 2,
    max_regret_vs_best_single: float = 0.5,
    min_worst_single_win_rate: float = 1.0,
) -> dict[str, Any]:
    rows = [
        build_case(
            case.label,
            case.left_eval,
            case.right_eval,
            left_policy=case.left_policy,
            right_policy=case.right_policy,
            consensus_policy=case.consensus_policy,
        )
        for case in cases
    ]
    slice_count = sum(row["slice_count"] for row in rows)
    wins_vs_left = sum(row["consensus_wins_vs_left_single"] for row in rows)
    wins_vs_right = sum(row["consensus_wins_vs_right_single"] for row in rows)
    wins_vs_best = sum(row["consensus_wins_vs_best_single"] for row in rows)
    wins_vs_worst = sum(row["consensus_wins_vs_worst_single"] for row in rows)
    regrets = [slice_row["consensus_regret_vs_best_single"] for row in rows for slice_row in row["slices"]]
    worst_margins = [slice_row["consensus_margin_vs_worst_single"] for row in rows for slice_row in row["slices"]]
    max_regret = max(regrets) if regrets else None
    failures: list[str] = []
    if len(rows) < min_cases:
        failures.append(f"case count below threshold: {len(rows)} < {min_cases}")
    if max_regret is not None and max_regret > max_regret_vs_best_single:
        failures.append(f"regret vs best single exceeds boundary: {max_regret:.4f} > {max_regret_vs_best_single:.4f}")
    worst_rate = wins_vs_worst / slice_count if slice_count else 0.0
    if worst_rate < min_worst_single_win_rate:
        failures.append(f"worst-single win rate below threshold: {worst_rate:.4f} < {min_worst_single_win_rate:.4f}")
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": len(rows),
            "slice_count": slice_count,
            "consensus_wins_vs_left_single": wins_vs_left,
            "consensus_wins_vs_right_single": wins_vs_right,
            "consensus_wins_vs_best_single": wins_vs_best,
            "consensus_wins_vs_worst_single": wins_vs_worst,
            "worst_single_win_rate": worst_rate,
            "mean_margin_vs_worst_single": mean(worst_margins),
            "min_margin_vs_worst_single": min(worst_margins) if worst_margins else None,
            "mean_regret_vs_best_single": mean(regrets),
            "max_regret_vs_best_single": max_regret,
            "max_allowed_regret_vs_best_single": max_regret_vs_best_single,
        },
        "failures": failures,
        "cases": rows,
        "interpretation": (
            "Consensus transfer is treated as boundary evidence: it can avoid the worse single-split policy "
            "while still having bounded regret versus the best single-split policy on some slices."
        ),
    }


def fmt(value: Any, digits: int = 4) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}f}"


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    lines = [
        "# Consensus Transfer Boundary Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- cases: `{summary['case_count']}`",
        f"- slices: `{summary['slice_count']}`",
        f"- wins vs left single: `{summary['consensus_wins_vs_left_single']}`",
        f"- wins vs right single: `{summary['consensus_wins_vs_right_single']}`",
        f"- wins vs best single: `{summary['consensus_wins_vs_best_single']}`",
        f"- wins vs worst single: `{summary['consensus_wins_vs_worst_single']}`",
        f"- mean margin vs worst single: `{fmt(summary['mean_margin_vs_worst_single'])}`",
        f"- min margin vs worst single: `{fmt(summary['min_margin_vs_worst_single'])}`",
        f"- mean regret vs best single: `{fmt(summary['mean_regret_vs_best_single'])}`",
        f"- max regret vs best single: `{fmt(summary['max_regret_vs_best_single'])}`",
        "",
        "## Cases",
        "",
        "| case | slice | left single | right single | consensus | margin vs left | margin vs right | margin vs best | margin vs worst |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for case in report["cases"]:
        for row in case["slices"]:
            lines.append(
                f"| `{case['label']}` | `{row['slice']}` | {fmt(row['left_single_ppl'])} | "
                f"{fmt(row['right_single_ppl'])} | {fmt(row['consensus_ppl'])} | "
                f"{fmt(row['consensus_margin_vs_left_single'])} | {fmt(row['consensus_margin_vs_right_single'])} | "
                f"{fmt(row['consensus_margin_vs_best_single'])} | {fmt(row['consensus_margin_vs_worst_single'])} |"
            )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            report["interpretation"],
            "",
            "## Failures",
            "",
        ]
    )
    if report["failures"]:
        lines.extend(f"- {failure}" for failure in report["failures"])
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a consensus transfer boundary gate.")
    parser.add_argument("--case", action="append", required=True)
    parser.add_argument("--min-cases", type=int, default=2)
    parser.add_argument("--max-regret-vs-best-single", type=float, default=0.5)
    parser.add_argument("--min-worst-single-win-rate", type=float, default=1.0)
    parser.add_argument("--out-json", type=Path, default=Path("outputs/consensus_transfer_boundary_gate.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/CONSENSUS_TRANSFER_BOUNDARY_GATE.md"))
    args = parser.parse_args()
    report = build_report(
        [parse_case(raw) for raw in args.case],
        min_cases=args.min_cases,
        max_regret_vs_best_single=args.max_regret_vs_best_single,
        min_worst_single_win_rate=args.min_worst_single_win_rate,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
