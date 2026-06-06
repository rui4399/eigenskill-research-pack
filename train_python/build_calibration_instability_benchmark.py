#!/usr/bin/env python3
from __future__ import annotations

"""Build a multi-model Calibration Split Instability benchmark."""

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import compare_sensitivity_splits as split


@dataclass(frozen=True)
class CaseSpec:
    label: str
    left: Path
    right: Path
    left_name: str
    right_name: str


def parse_case(raw: str) -> CaseSpec:
    parts = raw.split("=")
    if len(parts) != 3:
        raise ValueError(f"case must be LABEL=LEFT_JSON=RIGHT_JSON: {raw}")
    label, left, right = [part.strip() for part in parts]
    if not label or not left or not right:
        raise ValueError(f"empty label/path in case spec: {raw}")
    return CaseSpec(label=label, left=Path(left), right=Path(right), left_name="left", right_name="right")


def case_args(case: CaseSpec, top_k: str, epsilon: float) -> SimpleNamespace:
    return SimpleNamespace(
        left=str(case.left),
        right=str(case.right),
        left_name=case.left_name,
        right_name=case.right_name,
        top_k=top_k,
        epsilon=epsilon,
    )


def finite(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def mean(values: list[float]) -> float:
    return sum(values) / max(len(values), 1)


def top_jaccard(result: dict[str, Any], k: int) -> float | None:
    for row in result.get("top_overlap", []):
        if int(row.get("k", -1)) == k:
            return finite(row.get("jaccard"))
    return None


def build_benchmark(
    cases: list[CaseSpec],
    *,
    top_k: str = "10,20,40",
    epsilon: float = 1.0e-12,
    instability_spearman_threshold: float = 0.30,
    instability_jaccard_threshold: float = 0.55,
    min_cases: int = 3,
    min_unstable_cases: int = 2,
) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for case in cases:
        result = split.build_result(case_args(case, top_k=top_k, epsilon=epsilon))
        score_spearman = finite(result.get("score_spearman"))
        positive_jaccard = finite(result.get("positive_jaccard"))
        top20 = top_jaccard(result, 20)
        unstable = (
            score_spearman is not None
            and positive_jaccard is not None
            and (score_spearman <= instability_spearman_threshold or positive_jaccard <= instability_jaccard_threshold)
        )
        entries.append(
            {
                "label": case.label,
                "left": str(case.left),
                "right": str(case.right),
                "shared_modules": result["shared_modules"],
                "positive_jaccard": positive_jaccard,
                "score_spearman": score_spearman,
                "score_kendall_tau_a": finite(result.get("score_kendall_tau_a")),
                "top20_jaccard": top20,
                "unstable": unstable,
                "result": result,
            }
        )

    spearman_values = [entry["score_spearman"] for entry in entries if entry["score_spearman"] is not None]
    jaccard_values = [entry["positive_jaccard"] for entry in entries if entry["positive_jaccard"] is not None]
    top20_values = [entry["top20_jaccard"] for entry in entries if entry["top20_jaccard"] is not None]
    unstable_count = sum(1 for entry in entries if entry["unstable"])
    failures: list[str] = []
    if len(entries) < min_cases:
        failures.append(f"case count below threshold: {len(entries)} < {min_cases}")
    if unstable_count < min_unstable_cases:
        failures.append(f"unstable case count below threshold: {unstable_count} < {min_unstable_cases}")

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": len(entries),
            "unstable_case_count": unstable_count,
            "mean_score_spearman": mean(spearman_values),
            "min_score_spearman": min(spearman_values) if spearman_values else None,
            "max_score_spearman": max(spearman_values) if spearman_values else None,
            "mean_positive_jaccard": mean(jaccard_values),
            "mean_top20_jaccard": mean(top20_values),
            "instability_spearman_threshold": instability_spearman_threshold,
            "instability_jaccard_threshold": instability_jaccard_threshold,
        },
        "failures": failures,
        "entries": entries,
    }


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    status = "PASS" if report["passed"] else "FAIL"
    summary = report["summary"]
    lines = [
        "# Calibration Split Instability Benchmark",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{status}**",
        "",
        "## Aggregate",
        "",
        f"- cases: `{summary['case_count']}`",
        f"- unstable cases: `{summary['unstable_case_count']}`",
        f"- mean score/cost Spearman: `{summary['mean_score_spearman']:.4f}`",
        f"- mean positive-set Jaccard: `{summary['mean_positive_jaccard']:.4f}`",
        f"- mean top-20 Jaccard: `{summary['mean_top20_jaccard']:.4f}`",
        "",
        "## Cases",
        "",
        "| case | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard | unstable |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for entry in report["entries"]:
        top20 = entry["top20_jaccard"]
        lines.append(
            f"| `{entry['label']}` | {entry['shared_modules']} | {entry['score_spearman']:.4f} | "
            f"{entry['positive_jaccard']:.4f} | {top20:.4f} | {entry['unstable']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This benchmark measures how much module-sensitivity rankings move when",
            "the calibration distribution changes. Low score/cost rank correlation",
            "or low sensitive-set overlap supports the calibration-robustness problem",
            "definition; downstream PPL and task gates are still required before",
            "claiming a better quantizer.",
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
    parser = argparse.ArgumentParser(description="Build a multi-model calibration split instability benchmark.")
    parser.add_argument("--case", action="append", required=True, help="LABEL=LEFT_JSON=RIGHT_JSON")
    parser.add_argument("--top-k", default="10,20,40")
    parser.add_argument("--epsilon", type=float, default=1.0e-12)
    parser.add_argument("--instability-spearman-threshold", type=float, default=0.30)
    parser.add_argument("--instability-jaccard-threshold", type=float, default=0.55)
    parser.add_argument("--min-cases", type=int, default=3)
    parser.add_argument("--min-unstable-cases", type=int, default=2)
    parser.add_argument("--out-json", type=Path, default=Path("outputs/calibration_instability_benchmark.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/CALIBRATION_INSTABILITY_BENCHMARK.md"))
    args = parser.parse_args()

    report = build_benchmark(
        [parse_case(raw) for raw in args.case],
        top_k=args.top_k,
        epsilon=args.epsilon,
        instability_spearman_threshold=args.instability_spearman_threshold,
        instability_jaccard_threshold=args.instability_jaccard_threshold,
        min_cases=args.min_cases,
        min_unstable_cases=args.min_unstable_cases,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
