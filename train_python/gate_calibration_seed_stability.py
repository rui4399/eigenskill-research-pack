#!/usr/bin/env python3
from __future__ import annotations

"""Gate sensitivity-ranking stability across deterministic prompt seeds."""

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import compare_sensitivity_splits as split


@dataclass(frozen=True)
class SeedCase:
    label: str
    path: Path


def parse_case(raw: str) -> SeedCase:
    if "=" not in raw:
        raise ValueError(f"case must be LABEL=JSON: {raw}")
    label, path = [part.strip() for part in raw.split("=", 1)]
    if not label or not path:
        raise ValueError(f"empty label/path in case spec: {raw}")
    return SeedCase(label=label, path=Path(path))


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


def load_prompt_selection(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    selection = payload.get("prompt_selection", {})
    return selection if isinstance(selection, dict) else {}


def prompt_signature(selection: dict[str, Any]) -> tuple[Any, ...]:
    return (
        selection.get("source"),
        selection.get("pool_size"),
        selection.get("sample_size"),
        tuple(selection.get("selected_indices", []) or []),
    )


def compare_args(left: SeedCase, right: SeedCase, *, top_k: str, epsilon: float) -> SimpleNamespace:
    return SimpleNamespace(
        left=str(left.path),
        right=str(right.path),
        left_name=left.label,
        right_name=right.label,
        top_k=top_k,
        epsilon=epsilon,
    )


def build_gate(
    cases: list[SeedCase],
    *,
    top_k: str = "10,20,40",
    epsilon: float = 1.0e-12,
    min_cases: int = 2,
    min_pairs: int = 1,
    require_prompt_selection: bool = True,
) -> dict[str, Any]:
    if len(cases) != len({case.label for case in cases}):
        raise ValueError("case labels must be unique")

    prompt_rows = []
    signatures = set()
    missing_prompt_selection = []
    for case in cases:
        selection = load_prompt_selection(case.path)
        if not selection:
            missing_prompt_selection.append(case.label)
        signature = prompt_signature(selection)
        signatures.add(signature)
        prompt_rows.append(
            {
                "label": case.label,
                "path": str(case.path),
                "source": selection.get("source"),
                "pool_size": selection.get("pool_size"),
                "sample_size": selection.get("sample_size"),
                "seed": selection.get("seed"),
                "selected_indices": selection.get("selected_indices", []),
            }
        )

    pairs = []
    for left, right in combinations(cases, 2):
        result = split.build_result(compare_args(left, right, top_k=top_k, epsilon=epsilon))
        pairs.append(
            {
                "left": left.label,
                "right": right.label,
                "shared_modules": result.get("shared_modules"),
                "positive_jaccard": finite(result.get("positive_jaccard")),
                "score_spearman": finite(result.get("score_spearman")),
                "score_kendall_tau_a": finite(result.get("score_kendall_tau_a")),
                "top20_jaccard": top_jaccard(result, 20),
                "result": result,
            }
        )

    spearman = [row["score_spearman"] for row in pairs if row["score_spearman"] is not None]
    top20 = [row["top20_jaccard"] for row in pairs if row["top20_jaccard"] is not None]
    positive = [row["positive_jaccard"] for row in pairs if row["positive_jaccard"] is not None]
    finite_pairs = sum(1 for row in pairs if row["score_spearman"] is not None)

    failures: list[str] = []
    if len(cases) < min_cases:
        failures.append(f"case count below threshold: {len(cases)} < {min_cases}")
    if len(pairs) < min_pairs:
        failures.append(f"pair count below threshold: {len(pairs)} < {min_pairs}")
    if finite_pairs < min_pairs:
        failures.append(f"finite pair metrics below threshold: {finite_pairs} < {min_pairs}")
    if require_prompt_selection and missing_prompt_selection:
        failures.append(f"missing prompt_selection metadata: {missing_prompt_selection}")
    if require_prompt_selection and len(signatures) < min_cases:
        failures.append(f"unique prompt selections below threshold: {len(signatures)} < {min_cases}")

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": len(cases),
            "pair_count": len(pairs),
            "finite_pair_count": finite_pairs,
            "unique_prompt_selection_count": len(signatures),
            "mean_score_spearman": mean(spearman),
            "min_score_spearman": min(spearman) if spearman else None,
            "max_score_spearman": max(spearman) if spearman else None,
            "mean_top20_jaccard": mean(top20),
            "min_top20_jaccard": min(top20) if top20 else None,
            "mean_positive_jaccard": mean(positive),
            "min_positive_jaccard": min(positive) if positive else None,
        },
        "prompt_selections": prompt_rows,
        "pairs": pairs,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for "
            "pairwise ranking stability under the same model and prompt pool. Invalid claim: "
            "this alone proves downstream quality retention, SOTA quantization, or deployment speed."
        ),
    }


def fmt(value: Any, digits: int = 4) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}f}"


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    lines = [
        "# Calibration Seed Stability Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- cases: `{summary['case_count']}`",
        f"- pairs: `{summary['pair_count']}`",
        f"- finite pairs: `{summary['finite_pair_count']}`",
        f"- unique prompt selections: `{summary['unique_prompt_selection_count']}`",
        f"- mean score/cost Spearman: `{fmt(summary['mean_score_spearman'])}`",
        f"- min score/cost Spearman: `{fmt(summary['min_score_spearman'])}`",
        f"- mean top-20 Jaccard: `{fmt(summary['mean_top20_jaccard'])}`",
        f"- min top-20 Jaccard: `{fmt(summary['min_top20_jaccard'])}`",
        f"- mean positive-set Jaccard: `{fmt(summary['mean_positive_jaccard'])}`",
        "",
        "## Prompt Selections",
        "",
        "| label | source | pool | sample | seed | selected indices |",
        "|---|---|---:|---:|---:|---|",
    ]
    for row in report["prompt_selections"]:
        lines.append(
            f"| `{row['label']}` | `{row['source']}` | {row['pool_size']} | {row['sample_size']} | "
            f"{row['seed']} | `{row['selected_indices']}` |"
        )
    lines.extend(
        [
            "",
            "## Pairwise Stability",
            "",
            "| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in report["pairs"]:
        lines.append(
            f"| `{row['left']}` | `{row['right']}` | {row['shared_modules']} | "
            f"{fmt(row['score_spearman'])} | {fmt(row['positive_jaccard'])} | {fmt(row['top20_jaccard'])} |"
        )
    lines.extend(["", "## Claim Boundary", "", report["claim_boundary"], "", "## Failures", ""])
    if report["failures"]:
        lines.extend(f"- {failure}" for failure in report["failures"])
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate calibration seed stability across sensitivity artifacts.")
    parser.add_argument("--case", action="append", required=True, help="LABEL=JSON")
    parser.add_argument("--top-k", default="10,20,40")
    parser.add_argument("--epsilon", type=float, default=1.0e-12)
    parser.add_argument("--min-cases", type=int, default=2)
    parser.add_argument("--min-pairs", type=int, default=1)
    parser.add_argument("--allow-missing-prompt-selection", action="store_true")
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    report = build_gate(
        [parse_case(raw) for raw in args.case],
        top_k=args.top_k,
        epsilon=args.epsilon,
        min_cases=args.min_cases,
        min_pairs=args.min_pairs,
        require_prompt_selection=not args.allow_missing_prompt_selection,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
