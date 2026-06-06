#!/usr/bin/env python3
"""Rank rowguard candidates across three or more prompt splits.

This generalizes ``select_split_consensus_rowguard.py`` from a train/held-out
pair to an arbitrary list of prompt-suite result JSON files per candidate.
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


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def family(label: str) -> str:
    if label.startswith("baseline"):
        return "baseline"
    if label in {"full_v8", "uniform_v8"}:
        return "full_precision_probe"
    if label.startswith("g"):
        return "rowguard"
    return "other"


def exact_failures(result: dict[str, Any]) -> list[int]:
    failed: list[int] = []
    for row in result.get("rows", []):
        if not bool(row.get("comparison", {}).get("exact_match", False)):
            failed.append(int(row.get("id", len(failed))))
    return failed


def harmonic(values: list[float]) -> float:
    if not values or any(value <= 0.0 for value in values):
        return 0.0
    return float(len(values) / sum(1.0 / value for value in values))


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def parse_candidate(spec: str, split_names: list[str], root: Path) -> dict[str, Any]:
    if "=" not in spec:
        raise ValueError(f"candidate must be LABEL=JSON[,JSON...]: {spec}")
    label, rest = spec.split("=", 1)
    paths = [resolve_path(part.strip(), root) for part in rest.split(",") if part.strip()]
    if len(paths) != len(split_names):
        raise ValueError(f"{label} has {len(paths)} paths but {len(split_names)} split names were supplied")
    splits: list[dict[str, Any]] = []
    for name, path in zip(split_names, paths):
        result = load_json(path)
        agg = result["aggregate"]
        splits.append(
            {
                "name": name,
                "path": str(path),
                "prompts": int(agg["prompts"]),
                "exact_matches": int(agg["exact_matches"]),
                "exact_rate": float(agg["exact_match_rate"]),
                "mean_prefix": float(agg["mean_common_prefix_ratio"]),
                "mean_edit": float(agg["mean_char_edit_similarity"]),
                "speedup": float(agg["mean_speedup_fused_vs_baseline"]),
                "failures": exact_failures(result),
            }
        )
    return {"label": label.strip(), "splits": splits}


def score_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    exact_rates = [float(split["exact_rate"]) for split in candidate["splits"]]
    prefixes = [float(split["mean_prefix"]) for split in candidate["splits"]]
    speedups = [float(split["speedup"]) for split in candidate["splits"]]
    prompts = [int(split["prompts"]) for split in candidate["splits"]]
    failures = [len(split["failures"]) for split in candidate["splits"]]

    min_exact = min(exact_rates)
    mean_exact = sum(exact_rates) / len(exact_rates)
    harmonic_exact = harmonic(exact_rates)
    exact_span = max(exact_rates) - min_exact
    min_prefix = min(prefixes)
    mean_prefix = sum(prefixes) / len(prefixes)
    mean_speed = sum(speedups) / len(speedups)
    min_speed = min(speedups)
    failure_density = sum(failures) / max(sum(prompts), 1)

    score = (
        0.50 * min_exact
        + 0.18 * harmonic_exact
        + 0.12 * min_prefix
        + 0.06 * mean_prefix
        + 0.04 * clamp01(mean_speed)
        - 0.08 * exact_span
        - 0.03 * failure_density
    )

    if min_exact >= 0.90 and exact_span <= 0.10 and min_prefix >= 0.90:
        decision = "stable_reference"
    elif min_exact >= 0.75 and exact_span <= 0.25 and min_prefix >= 0.75:
        decision = "candidate_needs_larger_suite"
    elif min_exact >= 0.75:
        decision = "diagnostic_only_gap_sensitive"
    else:
        decision = "reject_for_now"

    return {
        **candidate,
        "family": family(candidate["label"]),
        "min_exact_rate": min_exact,
        "mean_exact_rate": mean_exact,
        "harmonic_exact_rate": harmonic_exact,
        "exact_span": exact_span,
        "min_prefix": min_prefix,
        "mean_prefix": mean_prefix,
        "mean_speedup": mean_speed,
        "min_speedup": min_speed,
        "failure_density": failure_density,
        "consensus_score": score,
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


def write_csv(path: Path, rows: list[dict[str, Any]], split_names: list[str]) -> None:
    fieldnames = [
        "label",
        "family",
        "selector_decision",
        "consensus_score",
        "min_exact_rate",
        "mean_exact_rate",
        "harmonic_exact_rate",
        "exact_span",
        "min_prefix",
        "mean_prefix",
        "mean_speedup",
        "failure_density",
    ] + [f"{name}_exact_rate" for name in split_names] + [f"{name}_failures" for name in split_names]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            flat = {key: row.get(key) for key in fieldnames}
            for split in row["splits"]:
                flat[f"{split['name']}_exact_rate"] = split["exact_rate"]
                flat[f"{split['name']}_failures"] = split["failures"]
            writer.writerow(flat)


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    rows = result["rows"]
    split_names = result["split_names"]
    recs = result["recommendations"]
    lines = [
        "# Layer-20 V Rowguard Multi-Split Selector",
        "",
        f"Date: `{result['date']}`",
        f"Splits: `{', '.join(split_names)}`",
        "",
        "This selector ranks candidates across all supplied prompt splits. It treats worst-split exact match as the primary signal and penalizes split-to-split instability.",
        "",
        "## Recommendations",
        "",
    ]
    for key in ["best_overall", "best_rowguard", "stable_rowguard"]:
        rec = recs.get(key)
        if rec is None:
            lines.append(f"- `{key}`: none")
        else:
            lines.append(
                "- `{key}`: `{label}` (`{decision}`), score `{score}`, min exact `{min_exact}`, exact span `{span}`".format(
                    key=key,
                    label=rec["label"],
                    decision=rec["selector_decision"],
                    score=fmt(float(rec["consensus_score"])),
                    min_exact=fmt(float(rec["min_exact_rate"])),
                    span=fmt(float(rec["exact_span"])),
                )
            )
    exact_headers = " | ".join(f"{name} exact" for name in split_names)
    lines.extend(
        [
            "",
            "## Ranking",
            "",
            f"| rank | label | family | decision | score | {exact_headers} | min exact | exact span | min prefix | mean speed |",
            f"|---:|---|---|---|---:|{'---:|' * len(split_names)}---:|---:|---:|---:|",
        ]
    )
    for index, row in enumerate(rows, start=1):
        split_cells = " | ".join(fmt(float(split["exact_rate"])) for split in row["splits"])
        lines.append(
            f"| {index} | {row['label']} | {row['family']} | {row['selector_decision']} | "
            f"{fmt(float(row['consensus_score']))} | {split_cells} | "
            f"{fmt(float(row['min_exact_rate']))} | {fmt(float(row['exact_span']))} | "
            f"{fmt(float(row['min_prefix']))} | {fmt(float(row['mean_speedup']))}x |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- A rowguard that is perfect on one split but weak on another should remain diagnostic-only.",
            "- A stable deployment claim requires high worst-split exact match across more prompts or task benchmarks.",
            "- The current scoring intentionally favors robustness over speed because these prompt-suite timings are noisy and quality failures dominate.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Select rowguard candidates across multiple prompt splits.")
    parser.add_argument("--split-name", action="append", required=True, help="Split name, repeated in the same order as candidate JSON paths.")
    parser.add_argument("--candidate", action="append", required=True, help="LABEL=JSON[,JSON...]")
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    rows = [score_candidate(parse_candidate(spec, args.split_name, root)) for spec in args.candidate]
    rows.sort(
        key=lambda row: (
            row["consensus_score"],
            row["min_exact_rate"],
            row["harmonic_exact_rate"],
            -row["exact_span"],
            row["mean_speedup"],
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
        "split_names": args.split_name,
        "scoring": {
            "formula": "0.50*min_exact + 0.18*harmonic_exact + 0.12*min_prefix + 0.06*mean_prefix + 0.04*clipped_mean_speed - 0.08*exact_span - 0.03*failure_density",
            "primary_sort": "consensus_score desc, then min exact, harmonic exact, low span, mean speed",
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
    write_csv(out_csv, rows, args.split_name)
    write_markdown(out_md, result)
    print(json.dumps({"out_json": str(out_json), "out_csv": str(out_csv), "out_md": str(out_md), "recommendations": result["recommendations"]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
