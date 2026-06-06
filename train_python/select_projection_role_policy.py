#!/usr/bin/env python3
from __future__ import annotations

"""Select projection-role ESMP policies across deterministic task slices.

The selector consumes ``eval_chat_task_benchmark.py`` JSON outputs. It is a
diagnostic robustness gate: any split-level pass-count regression rejects a
candidate before speed is considered.
"""

import argparse
import csv
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def resolve_path(path: str | Path, root: Path) -> Path:
    p = Path(path)
    if p.is_absolute():
        return p
    return root / p


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _aggregate(result: dict[str, Any], split: str) -> dict[str, Any]:
    try:
        return result[split]["aggregate"]
    except KeyError as exc:
        raise ValueError(f"result missing {split}.aggregate") from exc


def parse_candidate(spec: str, split_names: list[str], root: Path) -> dict[str, Any]:
    if "=" not in spec:
        raise ValueError(f"candidate must be LABEL=JSON[,JSON...]: {spec}")
    label, rest = spec.split("=", 1)
    paths = [resolve_path(part.strip(), root) for part in rest.split(",") if part.strip()]
    if len(paths) != len(split_names):
        raise ValueError(f"{label} has {len(paths)} paths but {len(split_names)} split names were supplied")

    splits: list[dict[str, Any]] = []
    for split_name, path in zip(split_names, paths, strict=True):
        result = load_json(path)
        base = _aggregate(result, "baseline")
        fused = _aggregate(result, "fused")
        base_tasks = int(base["tasks"])
        fused_tasks = int(fused["tasks"])
        if base_tasks != fused_tasks:
            raise ValueError(f"{path} baseline/fused task counts differ: {base_tasks} vs {fused_tasks}")
        base_tps = float(base.get("mean_tokens_per_second") or 0.0)
        fused_tps = float(fused.get("mean_tokens_per_second") or 0.0)
        base_ttft = float(base.get("mean_ttft_seconds") or 0.0)
        fused_ttft = float(fused.get("mean_ttft_seconds") or 0.0)
        base_passes = int(base["passes"])
        fused_passes = int(fused["passes"])
        splits.append(
            {
                "name": split_name,
                "path": str(path),
                "tasks": base_tasks,
                "baseline_passes": base_passes,
                "fused_passes": fused_passes,
                "pass_delta": fused_passes - base_passes,
                "baseline_accuracy": float(base["accuracy"]),
                "fused_accuracy": float(fused["accuracy"]),
                "accuracy_delta": float(fused["accuracy"]) - float(base["accuracy"]),
                "baseline_tps": base_tps,
                "fused_tps": fused_tps,
                "speedup": fused_tps / base_tps if base_tps > 0.0 else 0.0,
                "baseline_ttft": base_ttft,
                "fused_ttft": fused_ttft,
                "ttft_ratio": fused_ttft / base_ttft if base_ttft > 0.0 else math.inf,
            }
        )
    return {"label": label.strip(), "splits": splits}


def family(label: str) -> str:
    if "full" in label or "qkv" in label:
        return "full_qkv"
    if "vonly" in label or "v_only" in label:
        return "v_only"
    if "qonly" in label or "q_only" in label:
        return "q_only"
    if "konly" in label or "k_only" in label:
        return "k_only"
    return "other"


def harmonic(values: list[float]) -> float:
    if not values or any(value <= 0.0 for value in values):
        return 0.0
    return float(len(values) / sum(1.0 / value for value in values))


def clamp(value: float, lo: float = 0.0, hi: float = 1.5) -> float:
    return max(lo, min(hi, value))


def score_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    splits = candidate["splits"]
    pass_deltas = [int(split["pass_delta"]) for split in splits]
    accuracy_deltas = [float(split["accuracy_delta"]) for split in splits]
    speedups = [float(split["speedup"]) for split in splits]
    ttft_ratios = [float(split["ttft_ratio"]) for split in splits]

    total_tasks = sum(int(split["tasks"]) for split in splits)
    total_pass_delta = sum(pass_deltas)
    min_accuracy_delta = min(accuracy_deltas)
    min_speedup = min(speedups)
    harmonic_speedup = harmonic(speedups)
    max_ttft_ratio = max(ttft_ratios)
    mean_accuracy_delta = sum(accuracy_deltas) / len(accuracy_deltas)

    if any(delta < 0 for delta in pass_deltas):
        decision = "reject_quality_regression"
    elif min_speedup >= 1.0 and max_ttft_ratio <= 1.0:
        decision = "conservative_candidate"
    elif min_speedup >= 0.95:
        decision = "quality_preserving_speed_neutral"
    else:
        decision = "diagnostic_runtime_regression"

    quality_term = 1.0 + min(0.25, max(-0.5, mean_accuracy_delta))
    speed_term = clamp(harmonic_speedup) / 1.5
    ttft_term = 1.0 / max(max_ttft_ratio, 1e-9)
    if decision == "reject_quality_regression":
        decision_penalty = 0.35
    elif decision == "diagnostic_runtime_regression":
        decision_penalty = 0.75
    else:
        decision_penalty = 1.0
    score = decision_penalty * (0.55 * quality_term + 0.30 * speed_term + 0.15 * min(1.0, ttft_term))

    return {
        **candidate,
        "family": family(str(candidate["label"])),
        "total_tasks": total_tasks,
        "total_pass_delta": total_pass_delta,
        "min_accuracy_delta": min_accuracy_delta,
        "mean_accuracy_delta": mean_accuracy_delta,
        "min_speedup": min_speedup,
        "harmonic_speedup": harmonic_speedup,
        "max_ttft_ratio": max_ttft_ratio,
        "selector_decision": decision,
        "selector_score": score,
    }


def fmt(value: float) -> str:
    if math.isinf(value):
        return "inf"
    if math.isnan(value):
        return "nan"
    return f"{value:.4f}"


def write_csv(path: Path, rows: list[dict[str, Any]], split_names: list[str]) -> None:
    fieldnames = [
        "label",
        "family",
        "selector_decision",
        "selector_score",
        "total_pass_delta",
        "min_accuracy_delta",
        "mean_accuracy_delta",
        "min_speedup",
        "harmonic_speedup",
        "max_ttft_ratio",
    ] + [f"{name}_pass_delta" for name in split_names] + [f"{name}_speedup" for name in split_names]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            flat = {key: row.get(key) for key in fieldnames}
            for split in row["splits"]:
                flat[f"{split['name']}_pass_delta"] = split["pass_delta"]
                flat[f"{split['name']}_speedup"] = split["speedup"]
            writer.writerow(flat)


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    rows = result["rows"]
    split_names = result["split_names"]
    speed_headers = " | ".join(f"{name} speed" for name in split_names)
    delta_headers = " | ".join(f"{name} pass delta" for name in split_names)
    lines = [
        "# Projection-Role Policy Selector",
        "",
        f"Date: `{result['date']}`",
        f"Splits: `{', '.join(split_names)}`",
        "",
        "This selector ranks ESMP projection-role policies across deterministic task slices. Any split-level pass-count regression is rejected before speed is considered.",
        "",
        "## Recommendations",
        "",
    ]
    for key in ("best_overall", "best_quality_preserving", "best_rejected"):
        rec = result["recommendations"].get(key)
        if rec is None:
            lines.append(f"- `{key}`: none")
        else:
            lines.append(
                f"- `{key}`: `{rec['label']}` (`{rec['selector_decision']}`), score `{fmt(float(rec['selector_score']))}`, "
                f"min speed `{fmt(float(rec['min_speedup']))}x`, max TTFT ratio `{fmt(float(rec['max_ttft_ratio']))}`"
            )
    lines.extend(
        [
            "",
            "## Ranking",
            "",
            f"| rank | label | family | decision | score | total pass delta | min acc delta | min speed | max TTFT ratio | {delta_headers} | {speed_headers} |",
            f"|---:|---|---|---|---:|---:|---:|---:|---:|{'---:|' * len(split_names)}{'---:|' * len(split_names)}",
        ]
    )
    for idx, row in enumerate(rows, start=1):
        deltas = " | ".join(str(split["pass_delta"]) for split in row["splits"])
        speeds = " | ".join(f"{fmt(float(split['speedup']))}x" for split in row["splits"])
        lines.append(
            f"| {idx} | {row['label']} | {row['family']} | {row['selector_decision']} | "
            f"{fmt(float(row['selector_score']))} | {row['total_pass_delta']} | "
            f"{fmt(float(row['min_accuracy_delta']))} | {fmt(float(row['min_speedup']))}x | "
            f"{fmt(float(row['max_ttft_ratio']))} | {deltas} | {speeds} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Quality regression on any split is a hard rejection for now.",
            "- Speed is treated as secondary because deterministic task pass count is currently the scarce resource.",
            "- A conservative candidate is not a deployment claim; it is the next policy to validate on larger task slices and real runtime paths.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def choose(rows: list[dict[str, Any]], predicate) -> dict[str, Any] | None:
    for row in rows:
        if predicate(row):
            return row
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Select projection-role policies across deterministic task slices.")
    parser.add_argument("--split-name", action="append", required=True)
    parser.add_argument("--candidate", action="append", required=True, help="LABEL=JSON[,JSON...]")
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    rows = [score_candidate(parse_candidate(spec, args.split_name, root)) for spec in args.candidate]
    rows.sort(
        key=lambda row: (
            row["selector_decision"] != "reject_quality_regression",
            row["selector_score"],
            row["min_speedup"],
            -row["max_ttft_ratio"],
        ),
        reverse=True,
    )
    result = {
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "split_names": args.split_name,
        "recommendations": {
            "best_overall": rows[0] if rows else None,
            "best_quality_preserving": choose(rows, lambda row: row["selector_decision"] != "reject_quality_regression"),
            "best_rejected": choose(rows, lambda row: row["selector_decision"] == "reject_quality_regression"),
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
    print(
        json.dumps(
            {
                "out_json": str(out_json),
                "out_csv": str(out_csv),
                "out_md": str(out_md),
                "best_overall": result["recommendations"]["best_overall"]["label"] if rows else None,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
