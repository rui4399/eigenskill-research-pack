#!/usr/bin/env python3
"""Compare prompt-conditioned search results against held-out prompt suites.

This is a diagnostic, not a semantic benchmark. It quantifies how much a
precision policy selected on one prompt suite transfers to another prompt suite.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CandidateSpec:
    label: str
    train_path: Path
    heldout_path: Path


def resolve_path(path: str, root: Path) -> Path:
    p = Path(path)
    if p.is_absolute():
        return p
    return root / p


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_candidate(spec: str, root: Path) -> CandidateSpec:
    if "=" not in spec:
        raise ValueError(f"candidate must be LABEL=TRAIN_JSON,HELDOUT_JSON: {spec}")
    label, rest = spec.split("=", 1)
    parts = [part.strip() for part in rest.split(",") if part.strip()]
    if len(parts) != 2:
        raise ValueError(f"candidate must provide exactly two paths: {spec}")
    return CandidateSpec(
        label=label.strip(),
        train_path=resolve_path(parts[0], root),
        heldout_path=resolve_path(parts[1], root),
    )


def exact_failures(result: dict[str, Any]) -> list[int]:
    failed: list[int] = []
    for row in result.get("rows", []):
        comp = row.get("comparison", {})
        if not bool(comp.get("exact_match", False)):
            failed.append(int(row.get("id", len(failed))))
    return failed


def summarize_candidate(spec: CandidateSpec) -> dict[str, Any]:
    train = load_json(spec.train_path)
    heldout = load_json(spec.heldout_path)
    train_agg = train["aggregate"]
    heldout_agg = heldout["aggregate"]

    train_exact = float(train_agg["exact_match_rate"])
    heldout_exact = float(heldout_agg["exact_match_rate"])
    transfer_gap = train_exact - heldout_exact
    min_exact = min(train_exact, heldout_exact)
    denom = train_exact + heldout_exact
    harmonic_exact = 0.0 if denom <= 0 else 2.0 * train_exact * heldout_exact / denom

    train_prefix = float(train_agg["mean_common_prefix_ratio"])
    heldout_prefix = float(heldout_agg["mean_common_prefix_ratio"])
    prefix_gap = train_prefix - heldout_prefix

    heldout_failures = exact_failures(heldout)
    train_failures = exact_failures(train)
    if transfer_gap >= 0.20 and heldout_exact < 0.90:
        risk = "high_overfit"
    elif transfer_gap >= 0.10:
        risk = "moderate_gap"
    elif heldout_exact < train_exact:
        risk = "small_gap"
    else:
        risk = "stable_or_improved"

    return {
        "label": spec.label,
        "train_path": str(spec.train_path),
        "heldout_path": str(spec.heldout_path),
        "train_prompts": int(train_agg["prompts"]),
        "heldout_prompts": int(heldout_agg["prompts"]),
        "train_exact": int(train_agg["exact_matches"]),
        "heldout_exact": int(heldout_agg["exact_matches"]),
        "train_exact_rate": train_exact,
        "heldout_exact_rate": heldout_exact,
        "transfer_gap": transfer_gap,
        "min_exact_rate": min_exact,
        "harmonic_exact_rate": harmonic_exact,
        "train_mean_prefix": train_prefix,
        "heldout_mean_prefix": heldout_prefix,
        "prefix_gap": prefix_gap,
        "train_speedup": float(train_agg["mean_speedup_fused_vs_baseline"]),
        "heldout_speedup": float(heldout_agg["mean_speedup_fused_vs_baseline"]),
        "train_failures": train_failures,
        "heldout_failures": heldout_failures,
        "risk": risk,
    }


def fmt(x: float) -> str:
    return f"{x:.4f}"


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    rows = result["rows"]
    lines = [
        "# Prompt-Split Transfer Audit",
        "",
        f"Date: `{result['date']}`",
        "",
        "This audit compares a precision policy on the prompt suite used during search against a held-out prompt suite. It is designed to catch prompt-conditioned overfitting.",
        "",
        "## Summary",
        "",
        "| candidate | train exact | held-out exact | exact gap | min exact rate | train prefix | held-out prefix | held-out speed | risk |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| {label} | {train_exact}/{train_prompts} | {heldout_exact}/{heldout_prompts} | {gap} | {min_exact} | {train_prefix} | {heldout_prefix} | {heldout_speed}x | {risk} |".format(
                label=row["label"],
                train_exact=row["train_exact"],
                train_prompts=row["train_prompts"],
                heldout_exact=row["heldout_exact"],
                heldout_prompts=row["heldout_prompts"],
                gap=fmt(row["transfer_gap"]),
                min_exact=fmt(row["min_exact_rate"]),
                train_prefix=fmt(row["train_mean_prefix"]),
                heldout_prefix=fmt(row["heldout_mean_prefix"]),
                heldout_speed=fmt(row["heldout_speedup"]),
                risk=row["risk"],
            )
        )
    lines.extend(["", "## Candidate Details", ""])
    for row in rows:
        lines.extend(
            [
                f"### `{row['label']}`",
                "",
                f"- Train failures: `{row['train_failures']}`",
                f"- Held-out failures: `{row['heldout_failures']}`",
                f"- Harmonic exact rate: `{fmt(row['harmonic_exact_rate'])}`",
                f"- Prefix gap: `{fmt(row['prefix_gap'])}`",
                f"- Train JSON: `{row['train_path']}`",
                f"- Held-out JSON: `{row['heldout_path']}`",
                "",
            ]
        )

    best_min = max(rows, key=lambda r: (r["min_exact_rate"], r["heldout_exact_rate"], r["heldout_speedup"]))
    best_heldout = max(rows, key=lambda r: (r["heldout_exact_rate"], r["min_exact_rate"], r["heldout_speedup"]))
    lines.extend(
        [
            "## Interpretation",
            "",
            f"- Best worst-split candidate: `{best_min['label']}` with min exact rate `{fmt(best_min['min_exact_rate'])}`.",
            f"- Best held-out candidate: `{best_heldout['label']}` with held-out exact rate `{fmt(best_heldout['heldout_exact_rate'])}`.",
            "- A candidate with high train exact but lower held-out exact should be treated as diagnostic evidence, not as a deployable precision policy.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare prompt-suite transfer gaps for precision policies.")
    parser.add_argument("--candidate", action="append", required=True, help="LABEL=TRAIN_JSON,HELDOUT_JSON")
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    specs = [parse_candidate(spec, root) for spec in args.candidate]
    rows = [summarize_candidate(spec) for spec in specs]
    rows.sort(key=lambda r: (r["min_exact_rate"], r["heldout_exact_rate"], -r["transfer_gap"], r["heldout_speedup"]), reverse=True)

    result = {
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "rows": rows,
    }

    out_json = resolve_path(args.out_json, root)
    out_csv = resolve_path(args.out_csv, root)
    out_md = resolve_path(args.out_md, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with out_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    write_markdown(out_md, result)
    print(json.dumps({"out_json": str(out_json), "out_csv": str(out_csv), "out_md": str(out_md), "rows": rows}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
