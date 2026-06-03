#!/usr/bin/env python3
"""Sensitivity-rate-distortion bit allocation scaffold.

This is a small, dependency-free experiment that turns the EigenSkill-Q math
story into an executable baseline. It uses synthetic layer/group statistics by
default; later calibration code can replace `make_synthetic_groups` with real
activation/Hessian/Fisher statistics while keeping the same allocator API.
"""

import argparse
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path


BITS = [2, 3, 4, 8]


@dataclass(frozen=True)
class GroupStat:
    layer: int
    group: int
    sensitivity: float
    variance: float
    cost: float
    outlier: float


def distortion(group: GroupStat, bits: int) -> float:
    return group.sensitivity * group.variance * (2.0 ** (-2.0 * bits))


def memory(groups: list[GroupStat], alloc: list[int]) -> float:
    return sum(g.cost * b for g, b in zip(groups, alloc))


def total_distortion(groups: list[GroupStat], alloc: list[int]) -> float:
    return sum(distortion(g, b) for g, b in zip(groups, alloc))


def make_synthetic_groups(layers: int, groups_per_layer: int, seed: int) -> list[GroupStat]:
    rng = random.Random(seed)
    groups: list[GroupStat] = []
    for layer in range(layers):
        depth = 1.0 + 0.035 * layer
        # Add a middle-layer sensitivity ridge so the allocation is non-trivial.
        ridge = 1.0 + 1.15 * math.exp(-((layer - 0.58 * layers) ** 2) / (2 * (0.16 * layers) ** 2))
        for group in range(groups_per_layer):
            phase = 0.5 + 0.5 * math.sin((layer + 1) * (group + 3) * 0.37)
            outlier = rng.betavariate(1.5, 5.5)
            if rng.random() < 0.08:
                outlier += rng.uniform(0.35, 1.2)
            outlier = min(outlier, 1.6)
            sensitivity = depth * ridge * (0.55 + 1.7 * phase) * (1.0 + 1.15 * outlier)
            variance = math.exp(rng.gauss(-0.1 + 0.15 * phase, 0.55)) * (1.0 + 0.8 * outlier)
            cost = rng.uniform(0.82, 1.18) * (1.0 + 0.10 * (group % 4 == 0))
            groups.append(
                GroupStat(
                    layer=layer,
                    group=group,
                    sensitivity=round(sensitivity, 6),
                    variance=round(variance, 6),
                    cost=round(cost, 6),
                    outlier=round(outlier, 6),
                )
            )
    return groups


def load_groups(path: str) -> list[GroupStat]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    raw_groups = data["groups"] if isinstance(data, dict) and "groups" in data else data
    groups = []
    for idx, item in enumerate(raw_groups):
        groups.append(
            GroupStat(
                layer=int(item.get("layer", idx)),
                group=int(item.get("group", 0)),
                sensitivity=float(item["sensitivity"]),
                variance=float(item["variance"]),
                cost=float(item.get("cost", 1.0)),
                outlier=float(item.get("outlier", 0.0)),
            )
        )
    return groups


def uniform_alloc(n: int, bits: int) -> list[int]:
    return [bits] * n


def random_alloc(groups: list[GroupStat], budget: float, seed: int) -> list[int]:
    rng = random.Random(seed)
    alloc = [2] * len(groups)
    order = list(range(len(groups)))
    rng.shuffle(order)
    for idx in order:
        candidates = [b for b in BITS if b >= alloc[idx]]
        rng.shuffle(candidates)
        for b in candidates:
            trial = list(alloc)
            trial[idx] = b
            if memory(groups, trial) <= budget:
                alloc = trial
                break
    return alloc


def greedy_margin_alloc(groups: list[GroupStat], budget: float) -> list[int]:
    alloc = [2] * len(groups)
    if memory(groups, alloc) > budget:
        return alloc
    while True:
        best = None
        for idx, group in enumerate(groups):
            current = alloc[idx]
            next_bits = next((b for b in BITS if b > current), None)
            if next_bits is None:
                continue
            extra_cost = group.cost * (next_bits - current)
            if memory(groups, alloc) + extra_cost > budget:
                continue
            gain = distortion(group, current) - distortion(group, next_bits)
            score = gain / max(extra_cost, 1.0e-12)
            if best is None or score > best[0]:
                best = (score, idx, next_bits)
        if best is None:
            return alloc
        _, idx, next_bits = best
        alloc[idx] = next_bits


def continuous_bits(group: GroupStat, lam: float) -> float:
    # From minimizing S*sigma^2*2^(-2b) + lambda*c*b.
    numerator = 2.0 * math.log(2.0) * group.sensitivity * group.variance
    raw = 0.5 * math.log2(max(numerator / max(lam * group.cost, 1.0e-30), 1.0e-30))
    return min(8.0, max(2.0, raw))


def rate_distortion_alloc(groups: list[GroupStat], budget: float) -> list[int]:
    lo, hi = 1.0e-12, 1.0e6
    for _ in range(100):
        mid = (lo + hi) / 2.0
        cont = [continuous_bits(g, mid) for g in groups]
        mem = sum(g.cost * b for g, b in zip(groups, cont))
        if mem > budget:
            lo = mid
        else:
            hi = mid

    # Discretize downward first, then spend remaining budget greedily.
    cont = [continuous_bits(g, hi) for g in groups]
    alloc = []
    for b in cont:
        candidates = [x for x in BITS if x <= b]
        alloc.append(max(candidates) if candidates else 2)
    return greedy_from_alloc(groups, alloc, budget)


def greedy_from_alloc(groups: list[GroupStat], alloc: list[int], budget: float) -> list[int]:
    alloc = list(alloc)
    while memory(groups, alloc) > budget:
        best = None
        for idx, group in enumerate(groups):
            current = alloc[idx]
            prev_bits = next((b for b in reversed(BITS) if b < current), None)
            if prev_bits is None:
                continue
            saved = group.cost * (current - prev_bits)
            penalty = distortion(group, prev_bits) - distortion(group, current)
            score = penalty / max(saved, 1.0e-12)
            if best is None or score < best[0]:
                best = (score, idx, prev_bits)
        if best is None:
            break
        _, idx, prev_bits = best
        alloc[idx] = prev_bits

    while True:
        best = None
        base_mem = memory(groups, alloc)
        for idx, group in enumerate(groups):
            current = alloc[idx]
            next_bits = next((b for b in BITS if b > current), None)
            if next_bits is None:
                continue
            extra = group.cost * (next_bits - current)
            if base_mem + extra > budget:
                continue
            gain = distortion(group, current) - distortion(group, next_bits)
            score = gain / max(extra, 1.0e-12)
            if best is None or score > best[0]:
                best = (score, idx, next_bits)
        if best is None:
            return alloc
        _, idx, next_bits = best
        alloc[idx] = next_bits


def summarize(name: str, groups: list[GroupStat], alloc: list[int], budget: float) -> dict:
    bit_hist = {str(b): alloc.count(b) for b in BITS}
    mem = memory(groups, alloc)
    dist = total_distortion(groups, alloc)
    avg_bits = mem / max(sum(g.cost for g in groups), 1.0e-12)
    return {
        "name": name,
        "groups": len(groups),
        "budget": budget,
        "memory": mem,
        "budget_used": mem / max(budget, 1.0e-12),
        "avg_bits": avg_bits,
        "distortion": dist,
        "bit_hist": bit_hist,
    }


def markdown_report(result: dict) -> str:
    lines = [
        "# Sensitivity-Rate-Distortion Allocation Report",
        "",
        f"Seed: `{result['seed']}`",
        f"Layers: `{result['layers']}`",
        f"Groups per layer: `{result['groups_per_layer']}`",
        f"Budget average bits: `{result['budget_avg_bits']}`",
        "",
        "## Results",
        "",
        "| method | avg_bits | budget_used | distortion | bit_hist |",
        "|---|---:|---:|---:|---|",
    ]
    base = next(item for item in result["summaries"] if item["name"] == "uniform_int4")
    for item in result["summaries"]:
        rel = item["distortion"] / max(base["distortion"], 1.0e-30)
        lines.append(
            f"| {item['name']} | {item['avg_bits']:.3f} | {item['budget_used']:.3f} | "
            f"{item['distortion']:.8f} ({rel:.3f}x uniform4) | {item['bit_hist']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This scaffold validates the allocation objective, not real model quality.",
            "The next step is to replace synthetic statistics with calibration-derived",
            "activation, Hessian/Fisher, outlier, and hardware-cost statistics.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--layers", type=int, default=24)
    parser.add_argument("--groups-per-layer", type=int, default=16)
    parser.add_argument("--stats-json", default="", help="Optional calibration stats JSON with a groups array")
    parser.add_argument("--budget-avg-bits", type=float, default=3.2)
    parser.add_argument("--seed", type=int, default=20260604)
    parser.add_argument("--out-json", default="outputs/rate_distortion_allocation_summary.json")
    parser.add_argument("--out-md", default="outputs/rate_distortion_allocation_report.md")
    args = parser.parse_args()

    groups = load_groups(args.stats_json) if args.stats_json else make_synthetic_groups(args.layers, args.groups_per_layer, args.seed)
    budget = args.budget_avg_bits * sum(g.cost for g in groups)
    allocs = {
        "uniform_int2": uniform_alloc(len(groups), 2),
        "uniform_int3": uniform_alloc(len(groups), 3),
        "uniform_int4": uniform_alloc(len(groups), 4),
        "random_budgeted": random_alloc(groups, budget, args.seed + 17),
        "greedy_margin": greedy_margin_alloc(groups, budget),
        "rate_distortion": rate_distortion_alloc(groups, budget),
    }
    summaries = [summarize(name, groups, alloc, budget) for name, alloc in allocs.items()]
    result = {
        "seed": args.seed,
        "stats_json": args.stats_json,
        "layers": args.layers if not args.stats_json else len({g.layer for g in groups}),
        "groups_per_layer": args.groups_per_layer if not args.stats_json else None,
        "budget_avg_bits": args.budget_avg_bits,
        "bits": BITS,
        "groups": [asdict(g) for g in groups],
        "summaries": summaries,
        "allocations": allocs,
    }

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "summaries": summaries}, indent=2))


if __name__ == "__main__":
    main()
