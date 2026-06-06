#!/usr/bin/env python3
from __future__ import annotations

"""Gate interaction-aware swap-search evidence.

The committed swap-search runs start from an additive sensitivity allocation,
try bounded one-out/one-in swaps, and evaluate each candidate with global PPL.
This gate turns those scattered outputs into a paper-facing boundary result:
global feedback can reveal interactions that the additive proxy misses, but
the current evidence is still a small fake-quant diagnostic.
"""

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EPS = 1.0e-9


@dataclass(frozen=True)
class SearchCaseSpec:
    label: str
    summary: Path
    guard: Path | None = None


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


def parse_search_case(raw: str) -> SearchCaseSpec:
    parts = [part.strip() for part in raw.split("=")]
    if len(parts) not in (2, 3):
        raise ValueError("search case must be LABEL=SUMMARY_JSON or LABEL=SUMMARY_JSON=GUARD_JSON")
    label, summary = parts[:2]
    if not label or not summary:
        raise ValueError(f"empty label/path in search case: {raw}")
    guard = Path(parts[2]) if len(parts) == 3 and parts[2] else None
    return SearchCaseSpec(label, Path(summary), guard)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_guard(path: Path | None) -> dict[str, Any] | None:
    if path is None:
        return None
    data = read_json(path)
    ratio = finite(data.get("max_memory_used_ratio"))
    if ratio is None:
        ratio = finite(data.get("max_memory_ratio"))
    return {
        "path": str(path),
        "returncode": int(finite(data.get("returncode")) or 0),
        "killed": bool(data.get("killed_by_guard", data.get("killed", False))),
        "max_memory_ratio": ratio,
        "max_memory_mib": finite(data.get("max_memory_used_mib")) or finite(data.get("max_memory_mib")),
        "memory_total_mib": finite(data.get("memory_total_mib")),
        "max_utilization_pct": finite(data.get("max_utilization_gpu_pct")) or finite(data.get("max_utilization_pct")),
    }


def trial_row(base_ppl: float, trial: dict[str, Any]) -> dict[str, Any]:
    swap = trial.get("swap", {}) if isinstance(trial.get("swap"), dict) else {}
    metrics = trial.get("metrics", {}) if isinstance(trial.get("metrics"), dict) else {}
    ppl = finite(metrics.get("ppl"))
    if ppl is None:
        raise ValueError("trial missing finite metrics.ppl")
    out_delta = finite(swap.get("out_delta"))
    in_delta = finite(swap.get("in_delta"))
    proxy_gain = None
    if out_delta is not None and in_delta is not None:
        proxy_gain = in_delta - out_delta
    global_improvement = base_ppl - ppl
    return {
        "out_module": str(swap.get("out_module", "-")),
        "in_module": str(swap.get("in_module", "-")),
        "ppl": ppl,
        "global_improvement_ppl": global_improvement,
        "proxy_gain": proxy_gain,
        "globally_improved": global_improvement > EPS,
        "locally_negative_but_globally_improved": proxy_gain is not None and proxy_gain < -EPS and global_improvement > EPS,
    }


def build_search_case(spec: SearchCaseSpec) -> dict[str, Any]:
    data = read_json(spec.summary)
    base_metrics = data.get("base_metrics", {}) if isinstance(data.get("base_metrics"), dict) else {}
    best = data.get("best", {}) if isinstance(data.get("best"), dict) else {}
    best_metrics = best.get("metrics", {}) if isinstance(best.get("metrics"), dict) else {}
    best_swap = best.get("swap", {}) if isinstance(best.get("swap"), dict) else {}
    base_ppl = finite(base_metrics.get("ppl"))
    best_ppl = finite(best_metrics.get("ppl"))
    if base_ppl is None or best_ppl is None:
        raise ValueError(f"{spec.summary}: missing finite base/best PPL")
    trials = [trial_row(base_ppl, trial) for trial in data.get("trials", []) if isinstance(trial, dict)]
    best_proxy_gain = None
    out_delta = finite(best_swap.get("out_delta"))
    in_delta = finite(best_swap.get("in_delta"))
    if out_delta is not None and in_delta is not None:
        best_proxy_gain = in_delta - out_delta
    guard = parse_guard(spec.guard)
    return {
        "label": spec.label,
        "summary_path": str(spec.summary),
        "guard": guard,
        "model": str(data.get("model", "")),
        "prompt_count": int(finite(data.get("prompt_count")) or 0),
        "max_length": int(finite(data.get("max_length")) or 0),
        "group_size": int(finite(data.get("group_size")) or 0),
        "base_ppl": base_ppl,
        "best_ppl": best_ppl,
        "best_improvement_ppl": base_ppl - best_ppl,
        "trial_count": len(trials),
        "improved_trial_count": sum(1 for row in trials if row["globally_improved"]),
        "interaction_counterexample_count": sum(1 for row in trials if row["locally_negative_but_globally_improved"]),
        "best_swap": {
            "out_module": str(best_swap.get("out_module", "-")),
            "in_module": str(best_swap.get("in_module", "-")),
            "proxy_gain": best_proxy_gain,
            "locally_negative": best_proxy_gain is not None and best_proxy_gain < -EPS,
        },
        "trials": trials,
    }


def parse_transfer_matrix(path: Path | None) -> dict[str, Any] | None:
    if path is None:
        return None
    data = read_json(path)
    rows: list[dict[str, Any]] = []
    for row in data.get("rows", []):
        if not isinstance(row, dict):
            continue
        improvement = finite(row.get("improvement"))
        if improvement is None:
            continue
        rows.append(
            {
                "dataset": str(row.get("dataset", "")),
                "base_ppl": finite(row.get("base")),
                "target_ppl": finite(row.get("target")),
                "improvement_ppl": improvement,
                "regret_ppl": max(0.0, -improvement),
                "guard_status": str(row.get("guard_status", "")),
            }
        )
    regrets = [float(row["regret_ppl"]) for row in rows]
    return {
        "path": str(path),
        "row_count": len(rows),
        "positive_rows": sum(1 for row in rows if float(row["improvement_ppl"]) > EPS),
        "nonnegative_rows": sum(1 for row in rows if float(row["improvement_ppl"]) >= -EPS),
        "max_regret_ppl": max(regrets) if regrets else None,
        "mean_improvement_ppl": mean([float(row["improvement_ppl"]) for row in rows]),
        "rows": rows,
    }


def build_report(
    cases: list[SearchCaseSpec],
    *,
    transfer_matrix: Path | None = None,
    min_cases: int = 3,
    min_improved_cases: int = 1,
    min_interaction_counterexamples: int = 1,
    min_total_trials: int = 8,
    max_transfer_regret_ppl: float = 0.02,
    max_guard_vram_ratio: float = 0.85,
) -> dict[str, Any]:
    rows = [build_search_case(case) for case in cases]
    transfer = parse_transfer_matrix(transfer_matrix)
    improvements = [float(row["best_improvement_ppl"]) for row in rows]
    guard_ratios = [
        float(row["guard"]["max_memory_ratio"])
        for row in rows
        if isinstance(row.get("guard"), dict) and finite(row["guard"].get("max_memory_ratio")) is not None
    ]
    killed_guards = [
        row["label"]
        for row in rows
        if isinstance(row.get("guard"), dict) and (row["guard"].get("killed") or row["guard"].get("returncode") not in (0, None))
    ]
    total_trials = sum(int(row["trial_count"]) for row in rows)
    improved_cases = sum(1 for row in rows if float(row["best_improvement_ppl"]) > EPS)
    interaction_counterexamples = sum(int(row["interaction_counterexample_count"]) for row in rows)
    max_guard = max(guard_ratios) if guard_ratios else None
    transfer_regret = transfer.get("max_regret_ppl") if isinstance(transfer, dict) else None
    failures: list[str] = []
    if len(rows) < min_cases:
        failures.append(f"search case count below threshold: {len(rows)} < {min_cases}")
    if total_trials < min_total_trials:
        failures.append(f"trial count below threshold: {total_trials} < {min_total_trials}")
    if improved_cases < min_improved_cases:
        failures.append(f"improved case count below threshold: {improved_cases} < {min_improved_cases}")
    if interaction_counterexamples < min_interaction_counterexamples:
        failures.append(
            "interaction counterexamples below threshold: "
            f"{interaction_counterexamples} < {min_interaction_counterexamples}"
        )
    if killed_guards:
        failures.append(f"guard failures: {', '.join(killed_guards)}")
    if max_guard is not None and max_guard > max_guard_vram_ratio:
        failures.append(f"guard VRAM ratio exceeds limit: {max_guard:.4f} > {max_guard_vram_ratio:.4f}")
    if transfer_regret is not None and transfer_regret > max_transfer_regret_ppl:
        failures.append(f"transfer regret exceeds boundary: {transfer_regret:.4f} > {max_transfer_regret_ppl:.4f}")
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": len(rows),
            "total_trials": total_trials,
            "improved_case_count": improved_cases,
            "improved_trial_count": sum(int(row["improved_trial_count"]) for row in rows),
            "interaction_counterexample_count": interaction_counterexamples,
            "mean_best_improvement_ppl": mean(improvements),
            "max_best_improvement_ppl": max(improvements) if improvements else None,
            "min_best_improvement_ppl": min(improvements) if improvements else None,
            "transfer_row_count": transfer.get("row_count") if isinstance(transfer, dict) else 0,
            "transfer_positive_rows": transfer.get("positive_rows") if isinstance(transfer, dict) else 0,
            "transfer_max_regret_ppl": transfer_regret,
            "max_allowed_transfer_regret_ppl": max_transfer_regret_ppl,
            "max_guard_vram_ratio": max_guard,
            "max_allowed_guard_vram_ratio": max_guard_vram_ratio,
        },
        "failures": failures,
        "cases": rows,
        "transfer": transfer,
        "interpretation": (
            "This gate supports a narrow interaction-aware diagnostic claim: bounded global-PPL swap search can "
            "find at least one improvement missed by the additive proxy, while current cross-split transfer "
            "evidence is only a small bounded-regret result."
        ),
    }


def fmt(value: Any, digits: int = 4) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}f}"


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    lines = [
        "# Interaction-Aware Swap Boundary Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- cases: `{summary['case_count']}`",
        f"- total trials: `{summary['total_trials']}`",
        f"- improved cases: `{summary['improved_case_count']}`",
        f"- improved trials: `{summary['improved_trial_count']}`",
        f"- interaction counterexamples: `{summary['interaction_counterexample_count']}`",
        f"- mean best improvement PPL: `{fmt(summary['mean_best_improvement_ppl'])}`",
        f"- max best improvement PPL: `{fmt(summary['max_best_improvement_ppl'])}`",
        f"- transfer rows: `{summary['transfer_row_count']}`",
        f"- transfer positive rows: `{summary['transfer_positive_rows']}`",
        f"- transfer max regret PPL: `{fmt(summary['transfer_max_regret_ppl'])}`",
        f"- max guard VRAM ratio: `{fmt(summary['max_guard_vram_ratio'])}`",
        "",
        "## Search Cases",
        "",
        "| case | prompts | trials | base PPL | best PPL | improvement | interaction counterexamples | best swap | best proxy gain |",
        "|---|---:|---:|---:|---:|---:|---:|---|---:|",
    ]
    for row in report["cases"]:
        swap = row["best_swap"]
        lines.append(
            f"| `{row['label']}` | {row['prompt_count']} | {row['trial_count']} | {fmt(row['base_ppl'])} | "
            f"{fmt(row['best_ppl'])} | {fmt(row['best_improvement_ppl'])} | "
            f"{row['interaction_counterexample_count']} | `{swap['out_module']} -> {swap['in_module']}` | "
            f"{fmt(swap['proxy_gain'], 6)} |"
        )
    if report.get("transfer"):
        lines.extend(
            [
                "",
                "## Transfer Rows",
                "",
                "| dataset | base PPL | target PPL | improvement | regret | guard |",
                "|---|---:|---:|---:|---:|---|",
            ]
        )
        for row in report["transfer"]["rows"]:
            lines.append(
                f"| `{row['dataset']}` | {fmt(row['base_ppl'])} | {fmt(row['target_ppl'])} | "
                f"{fmt(row['improvement_ppl'])} | {fmt(row['regret_ppl'])} | `{row['guard_status']}` |"
            )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            report["interpretation"],
            "",
            "Valid claim: bounded global-PPL feedback exposes interaction effects beyond independent module ranking.",
            "",
            "Invalid claim: this is not a production allocator, SOTA quantizer, or broad transfer guarantee.",
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
    parser = argparse.ArgumentParser(description="Build interaction-aware swap boundary gate.")
    parser.add_argument("--search-case", action="append", default=[], help="LABEL=SUMMARY_JSON or LABEL=SUMMARY_JSON=GUARD_JSON")
    parser.add_argument("--transfer-matrix", type=Path)
    parser.add_argument("--min-cases", type=int, default=3)
    parser.add_argument("--min-improved-cases", type=int, default=1)
    parser.add_argument("--min-interaction-counterexamples", type=int, default=1)
    parser.add_argument("--min-total-trials", type=int, default=8)
    parser.add_argument("--max-transfer-regret-ppl", type=float, default=0.02)
    parser.add_argument("--max-guard-vram-ratio", type=float, default=0.85)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    cases = [parse_search_case(raw) for raw in args.search_case]
    report = build_report(
        cases,
        transfer_matrix=args.transfer_matrix,
        min_cases=args.min_cases,
        min_improved_cases=args.min_improved_cases,
        min_interaction_counterexamples=args.min_interaction_counterexamples,
        min_total_trials=args.min_total_trials,
        max_transfer_regret_ppl=args.max_transfer_regret_ppl,
        max_guard_vram_ratio=args.max_guard_vram_ratio,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
