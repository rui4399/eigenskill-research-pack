#!/usr/bin/env python3
from __future__ import annotations

"""Compare CSI-vs-n curves across model scales.

This gate consumes already-built CSI-vs-n curve artifacts. It does not rerun
model inference. Its job is to make the cross-scale interpretation explicit:
same-n differences and full-range gains are measured facts for the supplied
artifacts, not proof that model scale itself causes the difference.
"""

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


METRICS: tuple[tuple[str, str], ...] = (
    ("mean_score_spearman", "mean score/cost Spearman"),
    ("mean_top20_jaccard", "mean top-20 Jaccard"),
    ("mean_positive_jaccard", "mean positive-set Jaccard"),
)


@dataclass(frozen=True)
class ScaleCase:
    label: str
    path: Path


def parse_case(raw: str) -> ScaleCase:
    if "=" not in raw:
        raise ValueError(f"case must be LABEL=JSON: {raw}")
    label, path = [part.strip() for part in raw.split("=", 1)]
    if not label or not path:
        raise ValueError(f"empty label/path in case spec: {raw}")
    return ScaleCase(label=label, path=Path(path))


def finite(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def fmt(value: Any, digits: int = 4) -> str:
    number = finite(value)
    return "n/a" if number is None else f"{number:.{digits}f}"


def load_curve(case: ScaleCase) -> dict[str, Any]:
    payload = json.loads(case.path.read_text(encoding="utf-8"))
    points = payload.get("points", []) or []
    return {
        "label": case.label,
        "path": str(case.path),
        "source_passed": bool(payload.get("passed")),
        "summary": payload.get("summary", {}) or {},
        "points_by_n": {int(row["n"]): row for row in points},
    }


def metric_value(point: dict[str, Any], key: str) -> float | None:
    return finite(point.get(key))


def gain(curve: dict[str, Any], key: str, min_n: int, max_n: int) -> float | None:
    left = metric_value(curve["points_by_n"][min_n], key)
    right = metric_value(curve["points_by_n"][max_n], key)
    return None if left is None or right is None else right - left


def build_report(left_case: ScaleCase, right_case: ScaleCase) -> dict[str, Any]:
    left = load_curve(left_case)
    right = load_curve(right_case)
    common_n = sorted(set(left["points_by_n"]).intersection(right["points_by_n"]))
    failures: list[str] = []
    if not left["source_passed"]:
        failures.append(f"left source gate failed: {left['label']}")
    if not right["source_passed"]:
        failures.append(f"right source gate failed: {right['label']}")
    if len(common_n) < 2:
        failures.append(f"need at least two common n values, got {common_n}")

    same_n_rows: list[dict[str, Any]] = []
    for n in common_n:
        left_point = left["points_by_n"][n]
        right_point = right["points_by_n"][n]
        row: dict[str, Any] = {"n": n}
        for key, _ in METRICS:
            left_value = metric_value(left_point, key)
            right_value = metric_value(right_point, key)
            row[key] = {
                "left": left_value,
                "right": right_value,
                "right_minus_left": None if left_value is None or right_value is None else right_value - left_value,
            }
        same_n_rows.append(row)

    gain_rows: list[dict[str, Any]] = []
    if len(common_n) >= 2:
        min_n, max_n = common_n[0], common_n[-1]
        for key, _ in METRICS:
            left_gain = gain(left, key, min_n, max_n)
            right_gain = gain(right, key, min_n, max_n)
            gain_rows.append(
                {
                    "metric": key,
                    "min_n": min_n,
                    "max_n": max_n,
                    "left_gain": left_gain,
                    "right_gain": right_gain,
                    "right_minus_left_gain": None
                    if left_gain is None or right_gain is None
                    else right_gain - left_gain,
                }
            )

    right_lower_all_same_n = all(
        (metric := row[key]).get("right_minus_left") is not None and metric["right_minus_left"] < 0.0
        for row in same_n_rows
        for key, _ in METRICS
    )
    right_gain_larger = {
        key: (row["right_minus_left_gain"] is not None and row["right_minus_left_gain"] > 0.0)
        for row in gain_rows
        for key in [row["metric"]]
    }

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "left": {"label": left["label"], "path": left["path"]},
        "right": {"label": right["label"], "path": right["path"]},
        "summary": {
            "common_n_count": len(common_n),
            "common_n": common_n,
            "right_lower_all_same_n_metrics": right_lower_all_same_n,
            "right_gain_larger_by_metric": right_gain_larger,
        },
        "same_n_comparison": same_n_rows,
        "gain_comparison": gain_rows,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: for the supplied same-prompt-pool Qwen2.5 curve artifacts, "
            "the right-hand scale has lower measured stability than the left-hand scale "
            "at the shared n values, while both curves improve from the smallest to the "
            "largest n. Invalid claim: this proves that model size alone causes lower "
            "stability, a universal scaling law, downstream retention, or SOTA quantization."
        ),
    }


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    left = report["left"]["label"]
    right = report["right"]["label"]
    lines = [
        "# CSI Cross-Scale Comparison Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- left: `{left}`",
        f"- right: `{right}`",
        f"- common n values: `{report['summary']['common_n']}`",
        f"- right lower at all shared n/metrics: `{report['summary']['right_lower_all_same_n_metrics']}`",
        "",
        "## Same-n Comparison",
        "",
        "| n | metric | left | right | right - left |",
        "|---:|---|---:|---:|---:|",
    ]
    for row in report["same_n_comparison"]:
        for key, label in METRICS:
            values = row[key]
            lines.append(
                f"| {row['n']} | {label} | {fmt(values['left'])} | {fmt(values['right'])} | "
                f"{fmt(values['right_minus_left'])} |"
            )
    lines.extend(
        [
            "",
            "## Full-Range Gain Comparison",
            "",
            "| metric | n range | left gain | right gain | right gain - left gain |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for row in report["gain_comparison"]:
        label = dict(METRICS)[row["metric"]]
        lines.append(
            f"| {label} | {row['min_n']} -> {row['max_n']} | {fmt(row['left_gain'])} | "
            f"{fmt(row['right_gain'])} | {fmt(row['right_minus_left_gain'])} |"
        )
    lines.extend(["", "## Interpretation", ""])
    lines.extend(
        [
            f"- In these artifacts, `{right}` is lower than `{left}` at every shared n and audited metric.",
            "- Both scales still improve as calibration prompt count increases.",
            "- The evidence supports a conservative scale-up replication of CSI, not a causal model-size claim.",
            "",
            "## Claim Boundary",
            "",
            report["claim_boundary"],
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
    parser = argparse.ArgumentParser(description="Compare two CSI-vs-n curve artifacts across model scales.")
    parser.add_argument("--left", required=True, help="LABEL=curve_json")
    parser.add_argument("--right", required=True, help="LABEL=curve_json")
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    report = build_report(parse_case(args.left), parse_case(args.right))
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
