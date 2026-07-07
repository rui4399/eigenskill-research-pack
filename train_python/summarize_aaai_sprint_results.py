#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean, pstdev
from typing import Any


def finite_float(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(number) or math.isinf(number):
        return None
    return number


def load_records(input_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(input_dir.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        method = payload.get("method")
        task = payload.get("task")
        accuracy = finite_float(payload.get("accuracy"))
        if not method or not task or accuracy is None:
            continue
        record = dict(payload)
        record["method"] = str(method)
        record["task"] = str(task)
        record["accuracy"] = accuracy
        record["source_path"] = str(path)
        records.append(record)
    return records


def build_win_loss(records: list[dict[str, Any]], proposed: str = "csi_guided") -> dict[str, dict[str, int]]:
    by_task_method: dict[tuple[str, str], list[float]] = defaultdict(list)
    for record in records:
        by_task_method[(record["task"], record["method"])].append(float(record["accuracy"]))
    tasks = sorted({record["task"] for record in records})
    methods = sorted({record["method"] for record in records if record["method"] != proposed})
    output: dict[str, dict[str, int]] = {}
    for method in methods:
        row = {"wins": 0, "losses": 0, "ties": 0}
        for task in tasks:
            ours = by_task_method.get((task, proposed), [])
            theirs = by_task_method.get((task, method), [])
            if not ours or not theirs:
                continue
            ours_mean = mean(ours)
            theirs_mean = mean(theirs)
            if abs(ours_mean - theirs_mean) < 1.0e-12:
                row["ties"] += 1
            elif ours_mean > theirs_mean:
                row["wins"] += 1
            else:
                row["losses"] += 1
        output[f"{proposed}_vs_{method}"] = row
    return output


def build_average_rank(records: list[dict[str, Any]]) -> dict[str, float]:
    by_task: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for record in records:
        by_task[record["task"]][record["method"]].append(float(record["accuracy"]))
    ranks: dict[str, list[float]] = defaultdict(list)
    for methods in by_task.values():
        ordered = sorted(((method, mean(values)) for method, values in methods.items()), key=lambda item: item[1], reverse=True)
        for index, (method, _score) in enumerate(ordered, start=1):
            ranks[method].append(float(index))
    return {method: mean(values) for method, values in sorted(ranks.items())}


def build_seed_stability(records: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    grouped: dict[str, list[float]] = defaultdict(list)
    for record in records:
        if record.get("seed") is None:
            continue
        grouped[record["method"]].append(float(record["accuracy"]))
    return {
        method: {
            "mean": mean(values),
            "std": pstdev(values) if len(values) > 1 else 0.0,
            "worst": min(values),
            "seeds": float(len(values)),
        }
        for method, values in sorted(grouped.items())
    }


def summarize(input_dir: Path) -> dict[str, Any]:
    records = load_records(input_dir)
    return {
        "record_count": len(records),
        "win_loss": build_win_loss(records),
        "average_rank": build_average_rank(records),
        "seed_stability": build_seed_stability(records),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summarize(Path(args.input_dir)), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
