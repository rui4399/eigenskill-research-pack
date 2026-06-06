#!/usr/bin/env python3
"""Lagrangian mixed-precision allocator for measured loss sensitivity.

This is the paper-facing allocator entry point. It expects measured
per-module loss sensitivity, not generic activation magnitude statistics.

Continuous objective:

    min_b sum_i S_i sigma_i^2 2^(-2 b_i)
    s.t.  sum_i c_i b_i <= B

The closed-form stationary point implemented here follows:

    b_i* = 0.5 log2((S_i sigma_i^2 ln 2) / (lambda c_i))

The continuous solution is clamped to the candidate bit range, then discretized
under the same weighted average-bit budget.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class SensitivityRecord:
    index: int
    name: str
    sensitivity: float
    variance: float
    cost: float


def _first_number(item: dict[str, Any], keys: list[str], default: float | None = None) -> float:
    for key in keys:
        if key in item and item[key] is not None:
            return float(item[key])
    if default is None:
        raise KeyError(f"none of the required numeric keys is present: {keys}")
    return float(default)


def load_sensitivities(path: str) -> list[SensitivityRecord]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    rows = data.get("groups", data) if isinstance(data, dict) else data
    if not isinstance(rows, list):
        raise ValueError("sensitivity JSON must be a list or an object with a groups list")

    records: list[SensitivityRecord] = []
    for i, item in enumerate(rows):
        if not isinstance(item, dict):
            raise ValueError(f"record {i} is not an object")
        sensitivity = _first_number(
            item,
            ["positive_delta_nll", "sensitivity", "delta_nll", "loss_sensitivity", "score"],
            0.0,
        )
        sensitivity = max(sensitivity, 0.0)
        variance = _first_number(item, ["variance", "sigma2", "activation_variance"], 1.0)
        cost = _first_number(item, ["cost", "param_count", "weight_params", "num_params"], 1.0)
        records.append(
            SensitivityRecord(
                index=int(item.get("index", i)),
                name=str(item.get("module", item.get("name", f"group_{i}"))),
                sensitivity=sensitivity,
                variance=max(variance, 1.0e-12),
                cost=max(cost, 1.0e-12),
            )
        )
    if not records:
        raise ValueError("no sensitivity records loaded")
    return records


def weighted_average_bits(records: list[SensitivityRecord], bits: list[int | float]) -> float:
    total_cost = sum(r.cost for r in records)
    return sum(r.cost * float(b) for r, b in zip(records, bits)) / max(total_cost, 1.0e-30)


def distortion(record: SensitivityRecord, bits: int | float) -> float:
    return record.sensitivity * record.variance * (2.0 ** (-2.0 * float(bits)))


def continuous_bit(record: SensitivityRecord, lam: float, min_bit: int, max_bit: int) -> float:
    signal = record.sensitivity * record.variance
    if signal <= 0.0:
        return float(min_bit)
    numerator = signal * math.log(2.0)
    denominator = max(lam * record.cost, 1.0e-300)
    value = 0.5 * math.log2(max(numerator / denominator, 1.0e-300))
    return min(float(max_bit), max(float(min_bit), value))


def solve_lambda(
    records: list[SensitivityRecord],
    target_avg_bits: float,
    min_bit: int,
    max_bit: int,
    iterations: int,
) -> tuple[float, list[float]]:
    min_avg = weighted_average_bits(records, [min_bit] * len(records))
    max_avg = weighted_average_bits(records, [max_bit] * len(records))
    if target_avg_bits <= min_avg:
        return math.inf, [float(min_bit)] * len(records)
    if target_avg_bits >= max_avg:
        return 0.0, [float(max_bit)] * len(records)

    lo = 1.0e-30
    hi = 1.0
    while weighted_average_bits(records, [continuous_bit(r, hi, min_bit, max_bit) for r in records]) > target_avg_bits:
        hi *= 2.0

    for _ in range(iterations):
        mid = math.sqrt(lo * hi)
        cont = [continuous_bit(r, mid, min_bit, max_bit) for r in records]
        if weighted_average_bits(records, cont) > target_avg_bits:
            lo = mid
        else:
            hi = mid
    final = [continuous_bit(r, hi, min_bit, max_bit) for r in records]
    return hi, final


def floor_to_candidates(value: float, candidates: list[int]) -> int:
    eligible = [bit for bit in candidates if bit <= value]
    return max(eligible) if eligible else min(candidates)


def next_candidate(current: int, candidates: list[int]) -> int | None:
    for bit in candidates:
        if bit > current:
            return bit
    return None


def previous_candidate(current: int, candidates: list[int]) -> int | None:
    for bit in reversed(candidates):
        if bit < current:
            return bit
    return None


def memory(records: list[SensitivityRecord], bits: list[int]) -> float:
    return sum(r.cost * b for r, b in zip(records, bits))


def discretize_under_budget(
    records: list[SensitivityRecord],
    continuous: list[float],
    candidates: list[int],
    target_avg_bits: float,
) -> list[int]:
    budget = target_avg_bits * sum(r.cost for r in records)
    alloc = [floor_to_candidates(b, candidates) for b in continuous]

    while memory(records, alloc) > budget:
        best: tuple[float, int, int] | None = None
        for i, (record, bit) in enumerate(zip(records, alloc)):
            prev_bit = previous_candidate(bit, candidates)
            if prev_bit is None:
                continue
            saved = record.cost * (bit - prev_bit)
            penalty = distortion(record, prev_bit) - distortion(record, bit)
            score = penalty / max(saved, 1.0e-30)
            if best is None or score < best[0]:
                best = (score, i, prev_bit)
        if best is None:
            break
        _, idx, prev_bit = best
        alloc[idx] = prev_bit

    while True:
        base = memory(records, alloc)
        best: tuple[float, int, int] | None = None
        for i, (record, bit) in enumerate(zip(records, alloc)):
            nxt = next_candidate(bit, candidates)
            if nxt is None:
                continue
            extra = record.cost * (nxt - bit)
            if base + extra > budget:
                continue
            gain = distortion(record, bit) - distortion(record, nxt)
            score = gain / max(extra, 1.0e-30)
            if best is None or score > best[0]:
                best = (score, i, nxt)
        if best is None:
            return alloc
        _, idx, nxt = best
        alloc[idx] = nxt


def allocate_bits_lagrangian(
    sensitivities: list[SensitivityRecord] | list[dict[str, Any]],
    costs: list[float] | None = None,
    target_budget: float = 4.5,
    candidates: list[int] | None = None,
    iterations: int = 100,
) -> dict[str, Any]:
    if candidates is None:
        candidates = [2, 3, 4, 8]
    candidates = sorted(set(int(bit) for bit in candidates))
    if len(candidates) < 2:
        raise ValueError("at least two candidate bit widths are required")

    if sensitivities and isinstance(sensitivities[0], SensitivityRecord):
        records = list(sensitivities)  # type: ignore[arg-type]
    else:
        records = []
        for i, item in enumerate(sensitivities):  # type: ignore[assignment]
            assert isinstance(item, dict)
            cost = float(costs[i]) if costs is not None else _first_number(item, ["cost", "param_count", "weight_params"], 1.0)
            records.append(
                SensitivityRecord(
                    index=int(item.get("index", i)),
                    name=str(item.get("module", item.get("name", f"group_{i}"))),
                    sensitivity=max(_first_number(item, ["positive_delta_nll", "sensitivity", "delta_nll"], 0.0), 0.0),
                    variance=max(_first_number(item, ["variance", "sigma2"], 1.0), 1.0e-12),
                    cost=max(cost, 1.0e-12),
                )
            )

    lam, continuous = solve_lambda(records, target_budget, min(candidates), max(candidates), iterations)
    allocation = discretize_under_budget(records, continuous, candidates, target_budget)
    avg_bits = weighted_average_bits(records, allocation)
    hist = {str(bit): allocation.count(bit) for bit in candidates}
    return {
        "method": "lagrangian_loss_sensitivity",
        "formula": "b_i = 0.5 * log2((S_i * sigma_i^2 * ln2) / (lambda * c_i))",
        "lambda": lam,
        "target_avg_bits": target_budget,
        "avg_bits": avg_bits,
        "budget_satisfied": avg_bits <= target_budget + 1.0e-9,
        "bits": allocation,
        "bit_hist": hist,
        "records": [asdict(r) | {"bits": b, "continuous_bits": cb} for r, b, cb in zip(records, allocation, continuous)],
        "objective_distortion": sum(distortion(r, b) for r, b in zip(records, allocation)),
    }


def markdown_report(result: dict[str, Any]) -> str:
    rows = sorted(result["records"], key=lambda x: (-x["bits"], -x["sensitivity"] * x["variance"] / max(x["cost"], 1.0e-30)))
    lines = [
        "# Lagrangian Loss-Sensitivity Allocation",
        "",
        f"Formula: `{result['formula']}`",
        f"Target average bits: `{result['target_avg_bits']}`",
        f"Solved lambda: `{result['lambda']}`",
        f"Actual average bits: `{result['avg_bits']:.6f}`",
        f"Budget satisfied: `{result['budget_satisfied']}`",
        f"Bit histogram: `{result['bit_hist']}`",
        "",
        "## Top Protected Records",
        "",
        "| rank | name | bits | continuous_bits | sensitivity | variance | cost |",
        "|---:|---|---:|---:|---:|---:|---:|",
    ]
    for rank, item in enumerate(rows[:32], 1):
        lines.append(
            f"| {rank} | `{item['name']}` | {item['bits']} | {item['continuous_bits']:.3f} | "
            f"{item['sensitivity']:.6g} | {item['variance']:.6g} | {item['cost']:.0f} |"
        )
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "This allocator uses measured per-module loss sensitivity. It is still a",
            "budgeted allocation proxy; model quality must be validated by downstream",
            "PPL and task-retention runs.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sensitivity-json", required=True)
    parser.add_argument("--target-avg-bits", type=float, default=4.5)
    parser.add_argument("--bits", default="2,3,4,8")
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument("--method-name", default="lagrangian_loss_sensitivity")
    parser.add_argument("--out-json", default="outputs/lagrangian_allocator_summary.json")
    parser.add_argument("--out-md", default="outputs/lagrangian_allocator_report.md")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    candidates = [int(x) for x in args.bits.split(",") if x.strip()]
    records = load_sensitivities(args.sensitivity_json)
    result = allocate_bits_lagrangian(
        records,
        target_budget=args.target_avg_bits,
        candidates=candidates,
        iterations=args.iterations,
    )
    result["method"] = args.method_name
    result["source"] = args.sensitivity_json

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "avg_bits": result["avg_bits"], "bit_hist": result["bit_hist"]}, indent=2))


if __name__ == "__main__":
    main()
