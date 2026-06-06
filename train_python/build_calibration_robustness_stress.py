#!/usr/bin/env python3
from __future__ import annotations

"""Build a calibration-robustness stress gate from PPL summary artifacts.

This gate turns existing fake-quant PPL summaries into a machine-checkable
risk table. It is intentionally about robustness evidence, not about claiming a
new production quantizer.
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
    path: Path
    target: str = "auto"


TARGET_PRIORITY = [
    "wikitext_c4_consensus",
    "loss_sensitive_consensus_4to8",
    "loss_sensitive_robust_lcb_consensus_4to8",
    "cpp_loss_sensitive_budget",
    "loss_sensitive_full",
    "target",
]


def parse_case(raw: str) -> CaseSpec:
    parts = raw.split("=")
    if len(parts) not in (2, 3):
        raise ValueError(f"case must be LABEL=SUMMARY_JSON or LABEL=SUMMARY_JSON=TARGET: {raw}")
    label = parts[0].strip()
    path = parts[1].strip()
    target = parts[2].strip() if len(parts) == 3 else "auto"
    if not label or not path or not target:
        raise ValueError(f"empty label/path/target in case spec: {raw}")
    return CaseSpec(label=label, path=Path(path), target=target)


def finite(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def mean(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)


def read_results(path: Path) -> dict[str, float]:
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data.get("results", [])
    if not isinstance(rows, list) or not rows:
        raise ValueError(f"{path}: missing non-empty results array")
    out: dict[str, float] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        name = str(row.get("name", "")).strip()
        metrics = row.get("metrics", {})
        ppl = finite(metrics.get("ppl") if isinstance(metrics, dict) else None)
        if name and ppl is not None:
            out[name] = ppl
    if not out:
        raise ValueError(f"{path}: no finite PPL rows found")
    return out


def is_random_name(name: str) -> bool:
    return (
        name == "cpp_random_budget"
        or name.startswith("random_seed_")
        or name.startswith("random_budget_seed_")
    )


def find_uniform_name(results: dict[str, float]) -> str:
    for name in ("uniform_int4", "uniform_int4_group128", "uniform_int4_g128"):
        if name in results:
            return name
    candidates = [name for name in results if name.startswith("uniform") and "4" in name]
    if candidates:
        return sorted(candidates)[0]
    raise ValueError("summary is missing a uniform INT4 row")


def choose_target_name(results: dict[str, float], requested: str) -> str:
    if requested != "auto":
        if requested not in results:
            raise ValueError(f"requested target not found: {requested}")
        return requested
    for name in TARGET_PRIORITY:
        if name in results:
            return name
    raise ValueError("auto target could not find a known target row")


def build_case(label: str, path: Path, target: str = "auto") -> dict[str, Any]:
    results = read_results(path)
    if "fp16" not in results:
        raise ValueError(f"{path}: missing fp16 row")
    uniform_name = find_uniform_name(results)
    target_name = choose_target_name(results, target)
    random_rows = {name: ppl for name, ppl in results.items() if is_random_name(name)}
    if not random_rows:
        raise ValueError(f"{path}: missing random baseline rows")

    target_ppl = results[target_name]
    uniform_ppl = results[uniform_name]
    fp16_ppl = results["fp16"]
    best_random_name, best_random_ppl = min(random_rows.items(), key=lambda item: (item[1], item[0]))
    random_mean = mean(list(random_rows.values()))
    return {
        "label": label,
        "path": str(path),
        "target_name": target_name,
        "fp16_ppl": fp16_ppl,
        "uniform_name": uniform_name,
        "uniform_ppl": uniform_ppl,
        "target_ppl": target_ppl,
        "best_random_name": best_random_name,
        "best_random_ppl": best_random_ppl,
        "random_mean_ppl": random_mean,
        "random_count": len(random_rows),
        "target_margin_vs_uniform": uniform_ppl - target_ppl,
        "target_margin_vs_best_random": best_random_ppl - target_ppl,
        "target_margin_vs_random_mean": (random_mean - target_ppl) if random_mean is not None else None,
        "target_fp16_regret": target_ppl - fp16_ppl,
        "beats_uniform": target_ppl < uniform_ppl,
        "beats_best_random": target_ppl < best_random_ppl,
        "beats_random_mean": random_mean is not None and target_ppl < random_mean,
    }


def build_report(
    cases: list[CaseSpec],
    *,
    min_cases: int = 3,
    min_uniform_win_rate: float = 1.0,
    min_best_random_win_rate: float = 0.8,
    min_random_mean_win_rate: float = 1.0,
) -> dict[str, Any]:
    rows = [build_case(case.label, case.path, case.target) for case in cases]
    count = len(rows)
    uniform_wins = sum(1 for row in rows if row["beats_uniform"])
    best_random_wins = sum(1 for row in rows if row["beats_best_random"])
    random_mean_wins = sum(1 for row in rows if row["beats_random_mean"])
    uniform_margins = [row["target_margin_vs_uniform"] for row in rows]
    best_random_margins = [row["target_margin_vs_best_random"] for row in rows]
    random_mean_margins = [
        row["target_margin_vs_random_mean"]
        for row in rows
        if row["target_margin_vs_random_mean"] is not None
    ]
    fp16_regrets = [row["target_fp16_regret"] for row in rows]

    failures: list[str] = []
    if count < min_cases:
        failures.append(f"case count below threshold: {count} < {min_cases}")
    if count and uniform_wins / count < min_uniform_win_rate:
        failures.append(f"uniform win rate below threshold: {uniform_wins / count:.4f} < {min_uniform_win_rate:.4f}")
    if count and best_random_wins / count < min_best_random_win_rate:
        failures.append(
            f"best-random win rate below threshold: {best_random_wins / count:.4f} < {min_best_random_win_rate:.4f}"
        )
    if count and random_mean_wins / count < min_random_mean_win_rate:
        failures.append(
            f"random-mean win rate below threshold: {random_mean_wins / count:.4f} < {min_random_mean_win_rate:.4f}"
        )

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": count,
            "target_wins_vs_uniform": uniform_wins,
            "target_wins_vs_best_random": best_random_wins,
            "target_wins_vs_random_mean": random_mean_wins,
            "uniform_win_rate": uniform_wins / count if count else 0.0,
            "best_random_win_rate": best_random_wins / count if count else 0.0,
            "random_mean_win_rate": random_mean_wins / count if count else 0.0,
            "mean_margin_vs_uniform": mean(uniform_margins),
            "worst_margin_vs_uniform": min(uniform_margins) if uniform_margins else None,
            "mean_margin_vs_best_random": mean(best_random_margins),
            "worst_margin_vs_best_random": min(best_random_margins) if best_random_margins else None,
            "mean_margin_vs_random_mean": mean(random_mean_margins),
            "worst_margin_vs_random_mean": min(random_mean_margins) if random_mean_margins else None,
            "mean_fp16_regret": mean(fp16_regrets),
            "max_fp16_regret": max(fp16_regrets) if fp16_regrets else None,
        },
        "failures": failures,
        "cases": rows,
        "interpretation": (
            "Positive margins mean the target policy has lower PPL than the comparator. "
            "This is a robustness stress gate over committed fake-quant summaries, not a production quantizer or SOTA claim."
        ),
    }


def fmt(value: Any, digits: int = 4) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}f}"


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    status = "PASS" if report["passed"] else "FAIL"
    lines = [
        "# Calibration Robustness Stress Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{status}**",
        "",
        "## Summary",
        "",
        f"- cases: `{summary['case_count']}`",
        f"- target wins vs uniform: `{summary['target_wins_vs_uniform']}`",
        f"- target wins vs best random: `{summary['target_wins_vs_best_random']}`",
        f"- target wins vs random mean: `{summary['target_wins_vs_random_mean']}`",
        f"- mean margin vs uniform: `{fmt(summary['mean_margin_vs_uniform'])}`",
        f"- worst margin vs uniform: `{fmt(summary['worst_margin_vs_uniform'])}`",
        f"- mean margin vs best random: `{fmt(summary['mean_margin_vs_best_random'])}`",
        f"- worst margin vs best random: `{fmt(summary['worst_margin_vs_best_random'])}`",
        f"- mean FP16 regret: `{fmt(summary['mean_fp16_regret'])}`",
        "",
        "## Cases",
        "",
        "| case | target | FP16 | uniform | target | best random | random mean | margin vs uniform | margin vs best random | FP16 regret |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in report["cases"]:
        lines.append(
            f"| `{row['label']}` | `{row['target_name']}` | {fmt(row['fp16_ppl'])} | "
            f"{fmt(row['uniform_ppl'])} | {fmt(row['target_ppl'])} | "
            f"{fmt(row['best_random_ppl'])} | {fmt(row['random_mean_ppl'])} | "
            f"{fmt(row['target_margin_vs_uniform'])} | {fmt(row['target_margin_vs_best_random'])} | "
            f"{fmt(row['target_fp16_regret'])} |"
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
    parser = argparse.ArgumentParser(description="Build calibration-robustness stress evidence from PPL summaries.")
    parser.add_argument("--case", action="append", required=True, help="LABEL=SUMMARY_JSON or LABEL=SUMMARY_JSON=TARGET")
    parser.add_argument("--min-cases", type=int, default=3)
    parser.add_argument("--min-uniform-win-rate", type=float, default=1.0)
    parser.add_argument("--min-best-random-win-rate", type=float, default=0.8)
    parser.add_argument("--min-random-mean-win-rate", type=float, default=1.0)
    parser.add_argument("--out-json", type=Path, default=Path("outputs/calibration_robustness_stress_gate.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/CALIBRATION_ROBUSTNESS_STRESS_GATE.md"))
    args = parser.parse_args()

    report = build_report(
        [parse_case(raw) for raw in args.case],
        min_cases=args.min_cases,
        min_uniform_win_rate=args.min_uniform_win_rate,
        min_best_random_win_rate=args.min_best_random_win_rate,
        min_random_mean_win_rate=args.min_random_mean_win_rate,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
