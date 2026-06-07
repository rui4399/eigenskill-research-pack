#!/usr/bin/env python3
from __future__ import annotations

"""Gate sensitivity-rank behavior across calibration and model perturbations."""

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import compare_sensitivity_splits as split


@dataclass(frozen=True)
class PerturbationCase:
    axis: str
    label: str
    left: Path
    right: Path


def parse_case(raw: str) -> PerturbationCase:
    if ":" not in raw or "=" not in raw:
        raise ValueError(f"case must be AXIS:LABEL=LEFT_JSON=RIGHT_JSON: {raw}")
    axis, rest = raw.split(":", 1)
    parts = rest.split("=")
    if len(parts) != 3:
        raise ValueError(f"case must be AXIS:LABEL=LEFT_JSON=RIGHT_JSON: {raw}")
    label, left, right = [part.strip() for part in parts]
    axis = axis.strip()
    if not axis or not label or not left or not right:
        raise ValueError(f"empty axis/label/path in case spec: {raw}")
    return PerturbationCase(axis=axis, label=label, left=Path(left), right=Path(right))


def compare_args(case: PerturbationCase, *, top_k: str, epsilon: float) -> SimpleNamespace:
    return SimpleNamespace(
        left=str(case.left),
        right=str(case.right),
        left_name="left",
        right_name="right",
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


def mean(values: list[float]) -> float | None:
    clean = [value for value in values if finite(value) is not None]
    if not clean:
        return None
    return sum(clean) / len(clean)


def top_jaccard(result: dict[str, Any], k: int = 20) -> float | None:
    for row in result.get("top_overlap", []) or []:
        if int(row.get("k", -1)) == k:
            return finite(row.get("jaccard"))
    return None


def rows_for_axis(entries: list[dict[str, Any]], axis: str) -> list[dict[str, Any]]:
    return [entry for entry in entries if entry.get("axis") == axis]


def axis_summary(entries: list[dict[str, Any]], axis: str) -> dict[str, Any]:
    rows = rows_for_axis(entries, axis)
    spearman = [entry["score_spearman"] for entry in rows if entry["score_spearman"] is not None]
    top20 = [entry["top20_jaccard"] for entry in rows if entry["top20_jaccard"] is not None]
    return {
        "case_count": len(rows),
        "mean_score_spearman": mean(spearman),
        "min_score_spearman": min(spearman) if spearman else None,
        "max_score_spearman": max(spearman) if spearman else None,
        "mean_top20_jaccard": mean(top20),
        "min_top20_jaccard": min(top20) if top20 else None,
        "max_top20_jaccard": max(top20) if top20 else None,
    }


def build_gate(
    cases: list[PerturbationCase],
    *,
    top_k: str = "10,20,40",
    epsilon: float = 1.0e-12,
    min_sample_size_cases: int = 2,
    min_model_scale_cases: int = 1,
    min_sample_size_spearman: float = 0.50,
    max_model_scale_spearman: float = 0.30,
    min_separation_margin: float = 0.20,
) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for case in cases:
        result = split.build_result(compare_args(case, top_k=top_k, epsilon=epsilon))
        entries.append(
            {
                "axis": case.axis,
                "label": case.label,
                "left": str(case.left),
                "right": str(case.right),
                "shared_modules": result.get("shared_modules"),
                "positive_jaccard": finite(result.get("positive_jaccard")),
                "score_spearman": finite(result.get("score_spearman")),
                "score_kendall_tau_a": finite(result.get("score_kendall_tau_a")),
                "top20_jaccard": top_jaccard(result, 20),
                "result": result,
            }
        )

    sample_size = axis_summary(entries, "sample_size")
    model_scale = axis_summary(entries, "model_scale")
    sample_spearman = finite(sample_size.get("mean_score_spearman"))
    scale_spearman = finite(model_scale.get("mean_score_spearman"))
    separation = sample_spearman - scale_spearman if sample_spearman is not None and scale_spearman is not None else None

    failures: list[str] = []
    if sample_size["case_count"] < min_sample_size_cases:
        failures.append(f"sample_size case count below threshold: {sample_size['case_count']} < {min_sample_size_cases}")
    if model_scale["case_count"] < min_model_scale_cases:
        failures.append(f"model_scale case count below threshold: {model_scale['case_count']} < {min_model_scale_cases}")
    if sample_spearman is None or sample_spearman < min_sample_size_spearman:
        failures.append(f"sample_size mean Spearman below threshold: {sample_spearman} < {min_sample_size_spearman}")
    if scale_spearman is None or scale_spearman > max_model_scale_spearman:
        failures.append(f"model_scale mean Spearman above threshold: {scale_spearman} > {max_model_scale_spearman}")
    if separation is None or separation < min_separation_margin:
        failures.append(f"perturbation separation margin below threshold: {separation} < {min_separation_margin}")

    axes = sorted({str(entry["axis"]) for entry in entries})
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": len(entries),
            "axis_count": len(axes),
            "axes": axes,
            "sample_size_case_count": sample_size["case_count"],
            "model_scale_case_count": model_scale["case_count"],
            "sample_size_mean_spearman": sample_spearman,
            "sample_size_min_top20_jaccard": sample_size["min_top20_jaccard"],
            "model_scale_mean_spearman": scale_spearman,
            "model_scale_mean_top20_jaccard": model_scale["mean_top20_jaccard"],
            "perturbation_separation_margin": separation,
            "min_sample_size_spearman": min_sample_size_spearman,
            "max_model_scale_spearman": max_model_scale_spearman,
            "min_separation_margin": min_separation_margin,
        },
        "axis_summaries": {
            "sample_size": sample_size,
            "model_scale": model_scale,
        },
        "entries": entries,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: in the measured Qwen2.5 sensitivity artifacts, increasing calibration sample count "
            "within the same model preserves sensitivity rankings substantially better than transferring the "
            "ranking across model scale. Invalid claim: this is downstream quality retention, a universal "
            "scaling law, or a production quantization method."
        ),
    }


def fmt(value: Any, digits: int = 4) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}f}"


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    lines = [
        "# Sensitivity Perturbation Matrix Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- cases: `{summary['case_count']}`",
        f"- axes: `{', '.join(summary['axes'])}`",
        f"- sample-size mean Spearman: `{fmt(summary['sample_size_mean_spearman'])}`",
        f"- sample-size min top-20 Jaccard: `{fmt(summary['sample_size_min_top20_jaccard'])}`",
        f"- model-scale mean Spearman: `{fmt(summary['model_scale_mean_spearman'])}`",
        f"- model-scale mean top-20 Jaccard: `{fmt(summary['model_scale_mean_top20_jaccard'])}`",
        f"- perturbation separation margin: `{fmt(summary['perturbation_separation_margin'])}`",
        "",
        "## Cases",
        "",
        "| axis | case | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for entry in report["entries"]:
        lines.append(
            f"| `{entry['axis']}` | `{entry['label']}` | {entry['shared_modules']} | "
            f"{fmt(entry['score_spearman'])} | {fmt(entry['positive_jaccard'])} | {fmt(entry['top20_jaccard'])} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            report["claim_boundary"],
            "",
            "This gate separates two reviewer-critical questions. Calibration sample-size",
            "perturbation tests whether a sensitivity estimate stabilizes as more examples",
            "from the same model/setup are used. Model-scale perturbation tests whether the",
            "same sensitivity ranking can be reused across model sizes. The current evidence",
            "supports treating these as different failure modes.",
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
    parser = argparse.ArgumentParser(description="Gate sensitivity perturbation behavior across axes.")
    parser.add_argument("--case", action="append", required=True, help="AXIS:LABEL=LEFT_JSON=RIGHT_JSON")
    parser.add_argument("--top-k", default="10,20,40")
    parser.add_argument("--epsilon", type=float, default=1.0e-12)
    parser.add_argument("--min-sample-size-cases", type=int, default=2)
    parser.add_argument("--min-model-scale-cases", type=int, default=1)
    parser.add_argument("--min-sample-size-spearman", type=float, default=0.50)
    parser.add_argument("--max-model-scale-spearman", type=float, default=0.30)
    parser.add_argument("--min-separation-margin", type=float, default=0.20)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    report = build_gate(
        [parse_case(raw) for raw in args.case],
        top_k=args.top_k,
        epsilon=args.epsilon,
        min_sample_size_cases=args.min_sample_size_cases,
        min_model_scale_cases=args.min_model_scale_cases,
        min_sample_size_spearman=args.min_sample_size_spearman,
        max_model_scale_spearman=args.max_model_scale_spearman,
        min_separation_margin=args.min_separation_margin,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
