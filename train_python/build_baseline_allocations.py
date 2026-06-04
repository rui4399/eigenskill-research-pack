#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path


def bit_hist(alloc: list[int]) -> dict[str, int]:
    hist: dict[str, int] = {}
    for bits in alloc:
        hist[str(bits)] = hist.get(str(bits), 0) + 1
    return hist


def avg_bits(groups: list[dict], alloc: list[int]) -> float:
    total_cost = sum(float(group["cost"]) for group in groups)
    memory = sum(float(group["cost"]) * bits for group, bits in zip(groups, alloc))
    return memory / max(total_cost, 1.0e-12)


def summarize(groups: list[dict], alloc: list[int], name: str) -> dict:
    total_cost = sum(float(group["cost"]) for group in groups)
    memory = sum(float(group["cost"]) * bits for group, bits in zip(groups, alloc))
    positive_total = sum(float(group.get("positive_delta_nll", 0.0)) for group in groups)
    positive_protected = sum(
        float(group.get("positive_delta_nll", 0.0)) for group, bits in zip(groups, alloc) if bits > min(alloc)
    )
    return {
        "name": name,
        "groups": len(groups),
        "memory": memory,
        "budget": memory,
        "budget_used": 1.0,
        "avg_bits": memory / max(total_cost, 1.0e-12),
        "budget_avg_bits": memory / max(total_cost, 1.0e-12),
        "bit_hist": bit_hist(alloc),
        "positive_delta_nll_total": positive_total,
        "positive_delta_nll_protected": positive_protected,
        "positive_delta_nll_protected_ratio": positive_protected / max(positive_total, 1.0e-12),
    }


def same_hist_random(reference: list[int], seed: int) -> list[int]:
    alloc = list(reference)
    rng = random.Random(seed)
    rng.shuffle(alloc)
    return alloc


def category(group: dict) -> str:
    value = group.get("category")
    if value:
        return str(value)
    module = str(group.get("module", ""))
    if module == "lm_head":
        return "lm_head"
    if ".self_attn." in module:
        return "attn." + module.rsplit(".", 1)[-1]
    if ".mlp." in module:
        return "mlp." + module.rsplit(".", 1)[-1]
    return "other"


def heuristic_by_category(groups: list[dict], reference: list[int]) -> list[int]:
    high_count = sum(1 for bits in reference if bits > min(reference))
    scored: list[tuple[float, int]] = []
    for idx, group in enumerate(groups):
        cat = category(group)
        module = str(group.get("module", ""))
        score = 0.0
        if cat in {"attn.k_proj", "attn.v_proj"}:
            score += 100.0
        elif cat in {"attn.q_proj", "attn.o_proj"}:
            score += 50.0
        elif cat == "mlp.down_proj":
            score += 20.0
        elif cat == "lm_head":
            score -= 100.0
        # Slightly prefer earlier layers; it is a common but intentionally naive baseline.
        if "model.layers." in module:
            try:
                layer = int(module.split("model.layers.", 1)[1].split(".", 1)[0])
                score += max(0, 32 - layer) / 32.0
            except ValueError:
                pass
        scored.append((score, idx))
    selected = {idx for _score, idx in sorted(scored, reverse=True)[:high_count]}
    low = min(reference)
    high = max(reference)
    return [high if idx in selected else low for idx in range(len(groups))]


def heuristic_by_size(groups: list[dict], reference: list[int]) -> list[int]:
    high_count = sum(1 for bits in reference if bits > min(reference))
    selected = {
        idx
        for _cost, idx in sorted(
            ((float(group.get("cost", group.get("params", 0.0))), idx) for idx, group in enumerate(groups))
        )[:high_count]
    }
    low = min(reference)
    high = max(reference)
    return [high if idx in selected else low for idx in range(len(groups))]


def target_memory(groups: list[dict], reference: list[int]) -> float:
    return sum(float(group["cost"]) * bits for group, bits in zip(groups, reference))


def budgeted_select(groups: list[dict], reference: list[int], ordered_indices: list[int]) -> list[int]:
    low = min(reference)
    high = max(reference)
    budget = target_memory(groups, reference)
    base_memory = sum(float(group["cost"]) * low for group in groups)
    remaining = max(0.0, budget - base_memory)
    alloc = [low for _ in groups]
    selected: set[int] = set()

    for idx in ordered_indices:
        extra = float(groups[idx]["cost"]) * (high - low)
        if extra <= remaining + 1.0e-9:
            alloc[idx] = high
            selected.add(idx)
            remaining -= extra

    # Fill tiny residual budget with any still-fitting group, independent of the
    # original ranking. This keeps heuristic/random baselines close to the same
    # average-bit budget without solving another optimization problem.
    for _cost, idx in sorted((float(group["cost"]), idx) for idx, group in enumerate(groups)):
        if idx in selected:
            continue
        extra = float(groups[idx]["cost"]) * (high - low)
        if extra <= remaining + 1.0e-9:
            alloc[idx] = high
            selected.add(idx)
            remaining -= extra
    return alloc


def random_budget(groups: list[dict], reference: list[int], seed: int) -> list[int]:
    indices = list(range(len(groups)))
    rng = random.Random(seed)
    rng.shuffle(indices)
    return budgeted_select(groups, reference, indices)


def category_budget(groups: list[dict], reference: list[int]) -> list[int]:
    scored: list[tuple[float, int]] = []
    for idx, group in enumerate(groups):
        cat = category(group)
        module = str(group.get("module", ""))
        score = 0.0
        if cat in {"attn.k_proj", "attn.v_proj"}:
            score += 100.0
        elif cat in {"attn.q_proj", "attn.o_proj"}:
            score += 50.0
        elif cat == "mlp.down_proj":
            score += 20.0
        elif cat == "lm_head":
            score -= 100.0
        if "model.layers." in module:
            try:
                layer = int(module.split("model.layers.", 1)[1].split(".", 1)[0])
                score += max(0, 32 - layer) / 32.0
            except ValueError:
                pass
        scored.append((score, idx))
    return budgeted_select(groups, reference, [idx for _score, idx in sorted(scored, reverse=True)])


def small_first_budget(groups: list[dict], reference: list[int]) -> list[int]:
    ordered = [idx for _cost, idx in sorted((float(group["cost"]), idx) for idx, group in enumerate(groups))]
    return budgeted_select(groups, reference, ordered)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build random and heuristic allocation baselines from an existing allocation.")
    parser.add_argument("--base", required=True, help="Allocation summary JSON with groups/allocations.")
    parser.add_argument("--method", default="loss_sensitive_4to8")
    parser.add_argument("--seed", type=int, default=20260604)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    source = json.loads(Path(args.base).read_text(encoding="utf-8"))
    groups = source["groups"]
    reference = [int(bits) for bits in source["allocations"][args.method]]
    allocations = {
        args.method: reference,
        "random_same_hist": same_hist_random(reference, args.seed),
        "heuristic_category": heuristic_by_category(groups, reference),
        "heuristic_small_first": heuristic_by_size(groups, reference),
        "random_budget": random_budget(groups, reference, args.seed),
        "heuristic_category_budget": category_budget(groups, reference),
        "heuristic_small_first_budget": small_first_budget(groups, reference),
    }

    output = dict(source)
    output["baseline_source"] = args.base
    output["baseline_seed"] = args.seed
    output["allocations"] = allocations
    output["summaries"] = [summarize(groups, alloc, name) for name, alloc in allocations.items()]

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "out": str(out),
                "methods": list(allocations),
                "avg_bits": {name: avg_bits(groups, alloc) for name, alloc in allocations.items()},
                "bit_hist": {name: bit_hist(alloc) for name, alloc in allocations.items()},
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
