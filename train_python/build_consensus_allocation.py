#!/usr/bin/env python3
from __future__ import annotations

"""Build a consensus `{base, high}` allocation from two calibration probes.

The input files are expected to be allocation summaries produced from measured
module-level loss sensitivity. The consensus policy keeps modules selected by
both probes first, then spends the remaining bit budget on modules with the
highest average loss-per-extra-bit score across the two probes.

The output remains compatible with eval_weight_quant_ppl.py.
"""

import argparse
import json
import math
from pathlib import Path


def load_allocation(path: str, method: str) -> tuple[list[dict], list[int], dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    groups = data["groups"]
    bits = [int(x) for x in data["allocations"][method]]
    if len(groups) != len(bits):
        raise ValueError(f"{path}: groups and allocation length differ")
    return groups, bits, data


def bit_hist(bits: list[int]) -> dict[str, int]:
    hist: dict[str, int] = {}
    for bit in bits:
        hist[str(bit)] = hist.get(str(bit), 0) + 1
    return hist


def summarize(name: str, groups: list[dict], alloc: list[int], budget_avg_bits: float, base_bits: int) -> dict:
    total_cost = sum(float(group["cost"]) for group in groups)
    memory = sum(float(group["cost"]) * bits for group, bits in zip(groups, alloc))
    budget = budget_avg_bits * total_cost
    positive_total = sum(float(group.get("positive_delta_nll", 0.0)) for group in groups)
    positive_protected = sum(
        float(group.get("positive_delta_nll", 0.0))
        for group, bits in zip(groups, alloc)
        if bits > base_bits
    )
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


def module_set(groups: list[dict], bits: list[int], high_bits: int) -> set[str]:
    return {group["module"] for group, bit in zip(groups, bits) if bit == high_bits}


def consensus_groups(left_groups: list[dict], right_groups: list[dict], robust_gamma: float = 1.0) -> list[dict]:
    rows = []
    for left, right in zip(left_groups, right_groups):
        if left["module"] != right["module"]:
            raise ValueError(f"module order differs: {left['module']} != {right['module']}")
        cost = float(right.get("cost", left.get("cost", 0.0)))
        left_pos = float(left.get("positive_delta_nll", 0.0))
        right_pos = float(right.get("positive_delta_nll", 0.0))
        avg_pos = 0.5 * (left_pos + right_pos)
        std_pos = math.sqrt(0.5 * ((left_pos - avg_pos) ** 2 + (right_pos - avg_pos) ** 2))
        robust_lcb = max(avg_pos - robust_gamma * std_pos, 0.0)
        row = dict(right)
        row.update(
            {
                "left_positive_delta_nll": left_pos,
                "right_positive_delta_nll": right_pos,
                "avg_positive_delta_nll": avg_pos,
                "positive_delta_nll_std": std_pos,
                "robust_lcb_positive_delta_nll": robust_lcb,
                "calibration_consistency_ratio": robust_lcb / max(avg_pos, 1.0e-12),
                "consensus_score_delta_per_cost": avg_pos / max(cost, 1.0e-12),
                "robust_lcb_score_delta_per_cost": robust_lcb / max(cost, 1.0e-12),
                "left_sensitivity_rank": int(left.get("sensitivity_rank", 0)),
                "right_sensitivity_rank": int(right.get("sensitivity_rank", 0)),
            }
        )
        rows.append(row)
    return rows


def build_consensus(
    groups: list[dict],
    left_bits: list[int],
    right_bits: list[int],
    budget_avg_bits: float,
    base_bits: int,
    high_bits: int,
    score_key: str = "consensus_score_delta_per_cost",
) -> tuple[list[int], dict]:
    total_cost = sum(float(group["cost"]) for group in groups)
    target_memory = budget_avg_bits * total_cost
    alloc = [base_bits] * len(groups)
    memory = base_bits * total_cost
    upgrade_costs = [(high_bits - base_bits) * float(group["cost"]) for group in groups]

    selected: set[int] = set()
    intersection = [i for i, (a, b) in enumerate(zip(left_bits, right_bits)) if a == high_bits and b == high_bits]
    intersection.sort(key=lambda i: (-float(groups[i].get(score_key, 0.0)), groups[i]["module"]))
    skipped_intersection: list[str] = []
    for i in intersection:
        extra = upgrade_costs[i]
        if memory + extra <= target_memory + 1.0e-6:
            alloc[i] = high_bits
            memory += extra
            selected.add(i)
        else:
            skipped_intersection.append(groups[i]["module"])

    candidates = [i for i in range(len(groups)) if i not in selected]
    candidates.sort(
        key=lambda i: (
            -float(groups[i].get(score_key, 0.0)),
            -float(groups[i].get("avg_positive_delta_nll", 0.0)),
            float(groups[i].get("cost", 0.0)),
            groups[i]["module"],
        )
    )

    ranked_additions: list[str] = []
    for i in candidates:
        extra = upgrade_costs[i]
        if memory + extra <= target_memory + 1.0e-6:
            alloc[i] = high_bits
            memory += extra
            selected.add(i)
            ranked_additions.append(groups[i]["module"])

    meta = {
        "score_key": score_key,
        "target_memory": target_memory,
        "actual_memory": memory,
        "budget_used": memory / max(target_memory, 1.0e-12),
        "intersection_candidates": len(intersection),
        "intersection_selected": len(intersection) - len(skipped_intersection),
        "skipped_intersection": skipped_intersection,
        "ranked_additions": len(ranked_additions),
        "ranked_addition_modules": ranked_additions,
    }
    return alloc, meta


def selected_rows(groups: list[dict], alloc: list[int], high_bits: int, limit: int, score_key: str = "consensus_score_delta_per_cost") -> list[dict]:
    rows = []
    for group, bits in zip(groups, alloc):
        if bits != high_bits:
            continue
        rows.append(
            {
                "module": group["module"],
                "param_count": int(group.get("param_count", group.get("weight_params", 0))),
                "avg_positive_delta_nll": float(group.get("avg_positive_delta_nll", 0.0)),
                "left_positive_delta_nll": float(group.get("left_positive_delta_nll", 0.0)),
                "right_positive_delta_nll": float(group.get("right_positive_delta_nll", 0.0)),
                "consensus_score_delta_per_cost": float(group.get("consensus_score_delta_per_cost", 0.0)),
                "robust_lcb_positive_delta_nll": float(group.get("robust_lcb_positive_delta_nll", 0.0)),
                "robust_lcb_score_delta_per_cost": float(group.get("robust_lcb_score_delta_per_cost", 0.0)),
                "calibration_consistency_ratio": float(group.get("calibration_consistency_ratio", 0.0)),
                "left_rank": int(group.get("left_sensitivity_rank", 0)),
                "right_rank": int(group.get("right_sensitivity_rank", 0)),
            }
        )
    rows.sort(key=lambda row: (-float(row.get(score_key, 0.0)), -row["avg_positive_delta_nll"], row["module"]))
    return rows[:limit]


def markdown_report(result: dict) -> str:
    summary = next(item for item in result["summaries"] if item["name"] == result["policy_name"])
    lines = [
        "# Qwen Consensus Loss-Sensitive Allocation",
        "",
        f"Left allocation: `{result['left_path']}`",
        f"Right allocation: `{result['right_path']}`",
        f"Policy: `{result['policy']}`",
        f"Score key: `{result['score_key']}`",
        "",
        "## Summary",
        "",
        "| metric | value |",
        "|---|---:|",
        f"| modules | {summary['groups']} |",
        f"| average bits | {summary['avg_bits']:.4f} |",
        f"| budget used | {summary['budget_used']:.4f} |",
        f"| bit histogram | {summary['bit_hist']} |",
        f"| 2p 8-bit overlap | {result['overlap']['left_high_overlap']} |",
        f"| 8p 8-bit overlap | {result['overlap']['right_high_overlap']} |",
        f"| locked intersection modules | {result['consensus_meta']['intersection_selected']} |",
        f"| ranked additions | {result['consensus_meta']['ranked_additions']} |",
        "",
        "## Top Consensus 8-bit Modules",
        "",
        "| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in result["selected_modules"]:
        score = float(row.get(result["score_key"], row["consensus_score_delta_per_cost"]))
        lines.append(
            f"| `{row['module']}` | {row['param_count']} | {row['avg_positive_delta_nll']:.6f} | "
            f"{row['robust_lcb_positive_delta_nll']:.6f} | {row['calibration_consistency_ratio']:.4f} | "
            f"{row['left_positive_delta_nll']:.6f} | {row['right_positive_delta_nll']:.6f} | "
            f"{score:.3e} | {row['left_rank']} | {row['right_rank']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This allocation is a stability-oriented policy: it prioritizes modules that",
            "both calibration probes selected, then fills unused budget by average",
            "or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL",
            "evaluation because stable allocation decisions can still trade off quality.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--left", required=True)
    parser.add_argument("--left-method", default="loss_sensitive_4to8")
    parser.add_argument("--right", required=True)
    parser.add_argument("--right-method", default="loss_sensitive_4to8")
    parser.add_argument("--base-bits", type=int, default=4)
    parser.add_argument("--high-bits", type=int, default=8)
    parser.add_argument("--budget-avg-bits", type=float, default=4.5)
    parser.add_argument("--policy", choices=["mean_consensus", "robust_lcb"], default="mean_consensus")
    parser.add_argument("--robust-gamma", type=float, default=1.0)
    parser.add_argument("--selected-limit", type=int, default=30)
    parser.add_argument("--out-json", default="outputs/qwen25_0p5b_loss_sensitive_consensus_alloc_4to8_group128_summary.json")
    parser.add_argument("--out-md", default="outputs/qwen25_0p5b_loss_sensitive_consensus_alloc_4to8_group128_report.md")
    args = parser.parse_args()

    left_groups, left_bits, left_data = load_allocation(args.left, args.left_method)
    right_groups, right_bits, right_data = load_allocation(args.right, args.right_method)
    if len(left_groups) != len(right_groups):
        raise SystemExit("allocation group counts differ")
    if len(left_bits) != len(right_bits):
        raise SystemExit("allocation bit counts differ")

    groups = consensus_groups(left_groups, right_groups, robust_gamma=args.robust_gamma)
    uniform = [args.base_bits] * len(groups)
    score_key = "robust_lcb_score_delta_per_cost" if args.policy == "robust_lcb" else "consensus_score_delta_per_cost"
    policy_name = "loss_sensitive_robust_lcb_consensus_4to8" if args.policy == "robust_lcb" else "loss_sensitive_consensus_4to8"
    consensus, meta = build_consensus(
        groups,
        left_bits,
        right_bits,
        args.budget_avg_bits,
        args.base_bits,
        args.high_bits,
        score_key=score_key,
    )

    left_high = module_set(groups, left_bits, args.high_bits)
    right_high = module_set(groups, right_bits, args.high_bits)
    consensus_high = module_set(groups, consensus, args.high_bits)
    result = {
        "left_path": args.left,
        "right_path": args.right,
        "left_method": args.left_method,
        "right_method": args.right_method,
        "model": right_data.get("model") or left_data.get("model", ""),
        "base_bits": args.base_bits,
        "high_bits": args.high_bits,
        "budget_avg_bits": args.budget_avg_bits,
        "policy": args.policy,
        "policy_name": policy_name,
        "score_key": score_key,
        "robust_gamma": args.robust_gamma,
        "groups": groups,
        "allocations": {
            f"uniform_int{args.base_bits}": uniform,
            policy_name: consensus,
        },
        "summaries": [
            summarize(f"uniform_int{args.base_bits}", groups, uniform, args.budget_avg_bits, args.base_bits),
            summarize(policy_name, groups, consensus, args.budget_avg_bits, args.base_bits),
        ],
        "consensus_meta": meta,
        "overlap": {
            "left_high_count": len(left_high),
            "right_high_count": len(right_high),
            "consensus_high_count": len(consensus_high),
            "left_high_overlap": len(left_high & consensus_high),
            "right_high_overlap": len(right_high & consensus_high),
            "left_high_jaccard": len(left_high & consensus_high) / max(len(left_high | consensus_high), 1),
            "right_high_jaccard": len(right_high & consensus_high) / max(len(right_high | consensus_high), 1),
        },
        "selected_modules": selected_rows(groups, consensus, args.high_bits, args.selected_limit, score_key=score_key),
    }

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "summary": result["summaries"][1], "overlap": result["overlap"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
