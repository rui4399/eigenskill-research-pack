#!/usr/bin/env python3
"""Select precision policies by split-consensus rather than one prompt suite.

The input is the JSON emitted by ``compare_prompt_transfer.py``.  This selector
is intentionally conservative: it optimizes the worst observed split first and
penalizes prompt-suite transfer gaps.  The output is a ranking plus explicit
"best overall" and "best rowguard-only" recommendations.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def resolve_path(path: str, root: Path) -> Path:
    p = Path(path)
    if p.is_absolute():
        return p
    return root / p


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def family(label: str) -> str:
    if label.startswith("baseline"):
        return "baseline"
    if label in {"full_v8", "uniform_v8"}:
        return "full_precision_probe"
    if label.startswith("g"):
        return "rowguard"
    return "other"


def row_fail_count(row: dict[str, Any]) -> int:
    return len(set(row.get("train_failures", []))) + len(set(row.get("heldout_failures", [])))


def score_row(row: dict[str, Any]) -> dict[str, Any]:
    train_exact = float(row["train_exact_rate"])
    heldout_exact = float(row["heldout_exact_rate"])
    min_exact = float(row["min_exact_rate"])
    harmonic_exact = float(row["harmonic_exact_rate"])
    min_prefix = min(float(row["train_mean_prefix"]), float(row["heldout_mean_prefix"]))
    heldout_prefix = float(row["heldout_mean_prefix"])
    speed = clamp01(float(row["heldout_speedup"]))
    abs_gap = abs(float(row["transfer_gap"]))
    overfit_gap = max(0.0, float(row["transfer_gap"]))

    train_prompts = max(1, int(row["train_prompts"]))
    heldout_prompts = max(1, int(row["heldout_prompts"]))
    failure_density = row_fail_count(row) / float(train_prompts + heldout_prompts)

    # Exact matching dominates because this prompt suite is a deterministic
    # parity check against the dense model. Prefix/speed are tie-breakers.
    consensus_score = (
        0.45 * min_exact
        + 0.20 * harmonic_exact
        + 0.15 * min_prefix
        + 0.08 * heldout_prefix
        + 0.04 * speed
        - 0.10 * abs_gap
        - 0.05 * overfit_gap
        - 0.03 * failure_density
    )

    if min_exact >= 0.90 and abs_gap <= 0.10 and heldout_prefix >= 0.90:
        decision = "stable_reference"
    elif min_exact >= 0.75 and abs_gap <= 0.15 and heldout_prefix >= 0.75:
        decision = "candidate_needs_third_split"
    elif min_exact >= 0.75:
        decision = "diagnostic_only_gap_sensitive"
    else:
        decision = "reject_for_now"

    return {
        **row,
        "family": family(str(row["label"])),
        "abs_transfer_gap": abs_gap,
        "overfit_gap": overfit_gap,
        "min_prefix": min_prefix,
        "failure_density": failure_density,
        "consensus_score": consensus_score,
        "selector_decision": decision,
    }


def fmt(value: float) -> str:
    if math.isnan(value):
        return "nan"
    return f"{value:.4f}"


def choose_first(rows: list[dict[str, Any]], predicate) -> dict[str, Any] | None:
    for row in rows:
        if predicate(row):
            return row
    return None


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "label",
        "family",
        "selector_decision",
        "consensus_score",
        "train_exact_rate",
        "heldout_exact_rate",
        "min_exact_rate",
        "harmonic_exact_rate",
        "abs_transfer_gap",
        "train_mean_prefix",
        "heldout_mean_prefix",
        "min_prefix",
        "heldout_speedup",
        "failure_density",
        "risk",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key) for key in fieldnames})


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    rows = result["rows"]
    recs = result["recommendations"]
    lines = [
        "# Layer-20 V Rowguard Split-Consensus Selector",
        "",
        f"Date: `{result['date']}`",
        "",
        "This selector ranks precision policies with a conservative split-consensus score. It is a policy-selection audit, not a new generation benchmark.",
        "",
        "## Recommendations",
        "",
    ]
    for key in ["best_overall", "best_rowguard", "stable_rowguard"]:
        rec = recs.get(key)
        if rec is None:
            lines.append(f"- `{key}`: none")
            continue
        lines.append(
            "- `{key}`: `{label}` (`{decision}`), score `{score}`, min exact `{min_exact}`, held-out exact `{heldout_exact}`, gap `{gap}`".format(
                key=key,
                label=rec["label"],
                decision=rec["selector_decision"],
                score=fmt(float(rec["consensus_score"])),
                min_exact=fmt(float(rec["min_exact_rate"])),
                heldout_exact=fmt(float(rec["heldout_exact_rate"])),
                gap=fmt(float(rec["transfer_gap"])),
            )
        )

    lines.extend(
        [
            "",
            "## Ranking",
            "",
            "| rank | label | family | decision | score | train exact | held-out exact | min exact | harmonic | abs gap | held-out prefix | held-out speed | risk |",
            "|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for index, row in enumerate(rows, start=1):
        lines.append(
            "| {rank} | {label} | {family} | {decision} | {score} | {train_exact} | {heldout_exact} | {min_exact} | {harmonic} | {gap} | {prefix} | {speed}x | {risk} |".format(
                rank=index,
                label=row["label"],
                family=row["family"],
                decision=row["selector_decision"],
                score=fmt(float(row["consensus_score"])),
                train_exact=fmt(float(row["train_exact_rate"])),
                heldout_exact=fmt(float(row["heldout_exact_rate"])),
                min_exact=fmt(float(row["min_exact_rate"])),
                harmonic=fmt(float(row["harmonic_exact_rate"])),
                gap=fmt(float(row["abs_transfer_gap"])),
                prefix=fmt(float(row["heldout_mean_prefix"])),
                speed=fmt(float(row["heldout_speedup"])),
                risk=row["risk"],
            )
        )

    lines.extend(
        [
            "",
            "## Conservative Interpretation",
            "",
            "- The safest observed policy remains the existing baseline precision guard when optimizing worst-split exact match.",
            "- No rowguard policy should be presented as generalized yet unless it also survives a third prompt split or a larger held-out suite.",
            "- The strongest rowguard result is useful as a next candidate, not as a deployment claim.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank rowguard candidates using split-consensus transfer evidence.")
    parser.add_argument("--audit-json", required=True, help="JSON from compare_prompt_transfer.py")
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    audit_path = resolve_path(args.audit_json, root)
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    rows = [score_row(row) for row in audit["rows"]]
    rows.sort(
        key=lambda row: (
            row["consensus_score"],
            row["min_exact_rate"],
            row["harmonic_exact_rate"],
            -row["abs_transfer_gap"],
            row["heldout_speedup"],
        ),
        reverse=True,
    )

    best_overall = rows[0] if rows else None
    best_rowguard = choose_first(rows, lambda row: row["family"] == "rowguard")
    stable_rowguard = choose_first(
        rows,
        lambda row: row["family"] == "rowguard" and row["selector_decision"] == "stable_reference",
    )
    result = {
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "audit_json": str(audit_path),
        "scoring": {
            "formula": "0.45*min_exact + 0.20*harmonic_exact + 0.15*min_prefix + 0.08*heldout_prefix + 0.04*clipped_heldout_speed - 0.10*abs_gap - 0.05*overfit_gap - 0.03*failure_density",
            "primary_sort": "consensus_score desc, then min exact, harmonic exact, low gap, heldout speed",
        },
        "recommendations": {
            "best_overall": best_overall,
            "best_rowguard": best_rowguard,
            "stable_rowguard": stable_rowguard,
        },
        "rows": rows,
    }

    out_json = resolve_path(args.out_json, root)
    out_csv = resolve_path(args.out_csv, root)
    out_md = resolve_path(args.out_md, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_csv(out_csv, rows)
    write_markdown(out_md, result)
    print(json.dumps({"out_json": str(out_json), "out_csv": str(out_csv), "out_md": str(out_md), "recommendations": result["recommendations"]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
