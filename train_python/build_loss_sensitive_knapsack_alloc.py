#!/usr/bin/env python3
from __future__ import annotations

"""Build exact-knapsack `{base, high}` allocation from measured loss sensitivity.

`measure_module_quant_sensitivity.py` produces module-level positive loss
increases after one-module fake quantization. The earlier allocation uses a
greedy score. This script solves the corresponding 0/1 knapsack exactly after
scaling parameter costs by a common divisor, which is appropriate for the
SmolLM2 Linear-module cost structure.

The output remains compatible with eval_weight_quant_ppl.py.
"""

import argparse
import functools
import json
from math import gcd
from pathlib import Path


def bit_hist(alloc: list[int]) -> dict[str, int]:
    hist: dict[str, int] = {}
    for bits in alloc:
        hist[str(bits)] = hist.get(str(bits), 0) + 1
    return hist


def summarize(name: str, groups: list[dict], alloc: list[int], budget_avg_bits: float) -> dict:
    total_cost = sum(float(g["cost"]) for g in groups)
    memory = sum(float(g["cost"]) * bits for g, bits in zip(groups, alloc))
    budget = budget_avg_bits * total_cost
    positive_total = sum(float(g.get("positive_delta_nll", 0.0)) for g in groups)
    positive_protected = sum(float(g.get("positive_delta_nll", 0.0)) for g, bits in zip(groups, alloc) if bits > min(alloc))
    return {
        "name": name,
        "groups": len(groups),
        "budget_avg_bits": budget_avg_bits,
        "memory": memory,
        "budget": budget,
        "budget_used": memory / max(budget, 1.0e-12),
        "avg_bits": memory / max(total_cost, 1.0e-12),
        "bit_hist": bit_hist(alloc),
        "positive_delta_nll_total": positive_total,
        "positive_delta_nll_protected": positive_protected,
        "positive_delta_nll_protected_ratio": positive_protected / max(positive_total, 1.0e-12),
    }


def exact_knapsack_alloc(groups: list[dict], budget_avg_bits: float, base_bits: int, high_bits: int) -> tuple[list[int], dict]:
    if high_bits <= base_bits:
        raise ValueError("--high-bits must be greater than --base-bits")
    costs = [int(round(float(g["cost"]))) for g in groups]
    values = [max(float(g.get("positive_delta_nll", 0.0)), 0.0) for g in groups]
    total_cost = sum(costs)
    remaining = int(round((budget_avg_bits - base_bits) * total_cost))
    if remaining <= 0:
        return [base_bits] * len(groups), {
            "scaled_unit": 1,
            "capacity": 0,
            "selected": 0,
            "solver": "exact_knapsack_dp",
        }

    unit = functools.reduce(gcd, [c for c in costs if c > 0])
    extra_costs = [((high_bits - base_bits) * c) // unit for c in costs]
    capacity = remaining // unit

    dp = [0.0] * (capacity + 1)
    keep = [[False] * (capacity + 1) for _ in groups]
    for i, (weight, value) in enumerate(zip(extra_costs, values)):
        if value <= 0.0 or weight <= 0:
            continue
        for cap in range(capacity, weight - 1, -1):
            candidate = dp[cap - weight] + value
            if candidate > dp[cap] + 1.0e-15:
                dp[cap] = candidate
                keep[i][cap] = True

    alloc = [base_bits] * len(groups)
    cap = capacity
    for i in range(len(groups) - 1, -1, -1):
        weight = extra_costs[i]
        if cap >= weight and keep[i][cap]:
            alloc[i] = high_bits
            cap -= weight

    meta = {
        "scaled_unit": unit,
        "capacity": capacity,
        "remaining_budget_unscaled": remaining,
        "selected": sum(1 for bits in alloc if bits == high_bits),
        "dp_value": dp[capacity],
        "unused_capacity": cap,
        "solver": "exact_knapsack_dp",
    }
    return alloc, meta


def markdown_report(result: dict) -> str:
    lines = [
        "# Loss-Sensitive Exact Knapsack Allocation",
        "",
        f"Source: `{result['source_json']}`",
        f"Base bits: `{result['base_bits']}`",
        f"High bits: `{result['high_bits']}`",
        f"Budget average bits: `{result['budget_avg_bits']}`",
        f"Solver: `{result['knapsack_meta']['solver']}`",
        f"Scaled unit: `{result['knapsack_meta']['scaled_unit']}` parameters",
        "",
        "## Results",
        "",
        "| method | avg bits | budget used | bit histogram | protected positive delta |",
        "|---|---:|---:|---|---:|",
    ]
    for item in result["summaries"]:
        lines.append(
            f"| {item['name']} | {item['avg_bits']:.4f} | {item['budget_used']:.4f} | "
            f"{item['bit_hist']} | {item['positive_delta_nll_protected_ratio']:.4f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This allocation solves the measured-sensitivity 0/1 knapsack exactly",
            "after integer scaling of module parameter costs. It is a policy",
            "allocation artifact, not a production quantized runtime.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-json", default="outputs/smollm2_module_loss_sensitivity_limit4_group128.json")
    parser.add_argument("--base-bits", type=int, default=4)
    parser.add_argument("--high-bits", type=int, default=8)
    parser.add_argument("--budget-avg-bits", type=float, default=4.5)
    parser.add_argument("--out-json", default="outputs/smollm2_loss_sensitive_exact_knapsack_alloc_4to8_limit4_group128_summary.json")
    parser.add_argument("--out-md", default="outputs/smollm2_loss_sensitive_exact_knapsack_alloc_4to8_limit4_group128_report.md")
    args = parser.parse_args()

    source = json.loads(Path(args.source_json).read_text(encoding="utf-8"))
    groups = source["groups"]
    uniform = [args.base_bits] * len(groups)
    exact, meta = exact_knapsack_alloc(groups, args.budget_avg_bits, args.base_bits, args.high_bits)
    result = {
        "source_json": args.source_json,
        "model": source.get("model", ""),
        "base_bits": args.base_bits,
        "high_bits": args.high_bits,
        "budget_avg_bits": args.budget_avg_bits,
        "groups": groups,
        "allocations": {
            f"uniform_int{args.base_bits}": uniform,
            "loss_sensitive_exact_knapsack_4to8": exact,
        },
        "summaries": [
            summarize(f"uniform_int{args.base_bits}", groups, uniform, args.budget_avg_bits),
            summarize("loss_sensitive_exact_knapsack_4to8", groups, exact, args.budget_avg_bits),
        ],
        "knapsack_meta": meta,
    }
    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "summaries": result["summaries"], "knapsack_meta": meta}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
