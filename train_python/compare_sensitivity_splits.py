#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def load_groups(path: str) -> list[dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    groups = data.get("groups", [])
    if not isinstance(groups, list) or not groups:
        raise ValueError(f"{path}: missing non-empty groups array")
    return groups


def module_map(groups: list[dict]) -> dict[str, dict]:
    out = {}
    for item in groups:
        module = str(item.get("module", ""))
        if not module:
            raise ValueError("group missing module")
        out[module] = item
    return out


def positive_delta(item: dict) -> float:
    return max(float(item.get("positive_delta_nll", 0.0)), 0.0)


def signed_delta(item: dict) -> float:
    return float(item.get("delta_nll", item.get("positive_delta_nll", 0.0)))


def cost(item: dict) -> float:
    return max(float(item.get("cost", item.get("param_count", 1.0))), 1.0e-12)


def score(item: dict) -> float:
    return positive_delta(item) / cost(item)


def average_ranks(values: list[float], *, descending: bool) -> list[float]:
    indexed = list(enumerate(values))
    indexed.sort(key=lambda pair: pair[1], reverse=descending)
    ranks = [0.0] * len(values)
    pos = 0
    while pos < len(indexed):
        end = pos + 1
        while end < len(indexed) and indexed[end][1] == indexed[pos][1]:
            end += 1
        avg_rank = 0.5 * (pos + 1 + end)
        for idx in range(pos, end):
            ranks[indexed[idx][0]] = avg_rank
        pos = end
    return ranks


def pearson(xs: list[float], ys: list[float]) -> float:
    if len(xs) != len(ys) or not xs:
        return float("nan")
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    den_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    den_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    if den_x <= 0.0 or den_y <= 0.0:
        return float("nan")
    return num / (den_x * den_y)


def spearman(xs: list[float], ys: list[float], *, descending: bool = True) -> float:
    return pearson(average_ranks(xs, descending=descending), average_ranks(ys, descending=descending))


def kendall_tau_a(xs: list[float], ys: list[float]) -> float:
    concordant = 0
    discordant = 0
    n = len(xs)
    for i in range(n):
        for j in range(i + 1, n):
            dx = xs[i] - xs[j]
            dy = ys[i] - ys[j]
            prod = dx * dy
            if prod > 0:
                concordant += 1
            elif prod < 0:
                discordant += 1
    total = concordant + discordant
    if total == 0:
        return float("nan")
    return (concordant - discordant) / total


def sign_bucket(value: float, eps: float) -> str:
    if value > eps:
        return "positive"
    if value < -eps:
        return "negative"
    return "near_zero"


def top_modules(modules: list[str], values: list[float], k: int) -> set[str]:
    pairs = sorted(zip(modules, values), key=lambda pair: (pair[1], pair[0]), reverse=True)
    return {module for module, _value in pairs[: min(k, len(pairs))]}


def top_overlap_rows(modules: list[str], left_scores: list[float], right_scores: list[float], top_ks: list[int]) -> list[dict]:
    rows = []
    for k in top_ks:
        left_top = top_modules(modules, left_scores, k)
        right_top = top_modules(modules, right_scores, k)
        union = left_top | right_top
        overlap = left_top & right_top
        rows.append(
            {
                "k": k,
                "left_count": len(left_top),
                "right_count": len(right_top),
                "overlap": len(overlap),
                "union": len(union),
                "jaccard": len(overlap) / max(len(union), 1),
            }
        )
    return rows


def markdown_report(result: dict) -> str:
    lines = [
        "# Sensitivity Split Stability",
        "",
        f"Left: `{result['left_path']}`",
        f"Right: `{result['right_path']}`",
        "",
        "## Summary",
        "",
        "| metric | value |",
        "|---|---:|",
        f"| shared modules | {result['shared_modules']} |",
        f"| left positive modules | {result['left_positive_count']} |",
        f"| right positive modules | {result['right_positive_count']} |",
        f"| both positive modules | {result['both_positive_count']} |",
        f"| either positive modules | {result['either_positive_count']} |",
        f"| positive-set Jaccard | {result['positive_jaccard']:.4f} |",
        f"| signed-delta sign agreement | {result['sign_agreement_ratio']:.4f} |",
        f"| positive-delta Pearson | {result['positive_delta_pearson']:.4f} |",
        f"| positive-delta Spearman | {result['positive_delta_spearman']:.4f} |",
        f"| score/cost Pearson | {result['score_pearson']:.4f} |",
        f"| score/cost Spearman | {result['score_spearman']:.4f} |",
        f"| score/cost Kendall tau-a | {result['score_kendall_tau_a']:.4f} |",
        "",
        "## Top-K Score Overlap",
        "",
        "| k | left top-k | right top-k | overlap | union | Jaccard |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in result["top_overlap"]:
        lines.append(
            f"| {row['k']} | {row['left_count']} | {row['right_count']} | {row['overlap']} | "
            f"{row['union']} | {row['jaccard']:.4f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Low rank correlation or low top-k overlap means the calibration split is",
            "noisy; it does not by itself prove poor downstream PPL. The consensus",
            "allocation should therefore be judged by both this stability audit and",
            "the downstream PPL evidence matrix.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_result(args) -> dict:
    left = module_map(load_groups(args.left))
    right = module_map(load_groups(args.right))
    modules = sorted(set(left) & set(right))
    if not modules:
        raise ValueError("no shared modules")
    missing = (set(left) ^ set(right))
    if missing:
        print(f"warning: ignoring {len(missing)} non-shared modules", flush=True)

    left_pos = [positive_delta(left[module]) for module in modules]
    right_pos = [positive_delta(right[module]) for module in modules]
    left_score = [score(left[module]) for module in modules]
    right_score = [score(right[module]) for module in modules]
    left_signed = [signed_delta(left[module]) for module in modules]
    right_signed = [signed_delta(right[module]) for module in modules]

    left_positive_set = {module for module, value in zip(modules, left_pos) if value > args.epsilon}
    right_positive_set = {module for module, value in zip(modules, right_pos) if value > args.epsilon}
    positive_overlap = left_positive_set & right_positive_set
    positive_union = left_positive_set | right_positive_set
    sign_agree = sum(
        1
        for l_value, r_value in zip(left_signed, right_signed)
        if sign_bucket(l_value, args.epsilon) == sign_bucket(r_value, args.epsilon)
    )

    top_ks = [int(item) for item in args.top_k.split(",") if item.strip()]
    result = {
        "left_path": args.left,
        "right_path": args.right,
        "left_name": args.left_name,
        "right_name": args.right_name,
        "epsilon": args.epsilon,
        "shared_modules": len(modules),
        "left_positive_count": len(left_positive_set),
        "right_positive_count": len(right_positive_set),
        "both_positive_count": len(positive_overlap),
        "either_positive_count": len(positive_union),
        "positive_jaccard": len(positive_overlap) / max(len(positive_union), 1),
        "sign_agreement_count": sign_agree,
        "sign_agreement_ratio": sign_agree / len(modules),
        "positive_delta_pearson": pearson(left_pos, right_pos),
        "positive_delta_spearman": spearman(left_pos, right_pos),
        "score_pearson": pearson(left_score, right_score),
        "score_spearman": spearman(left_score, right_score),
        "score_kendall_tau_a": kendall_tau_a(left_score, right_score),
        "top_overlap": top_overlap_rows(modules, left_score, right_score, top_ks),
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--left", required=True)
    parser.add_argument("--right", required=True)
    parser.add_argument("--left-name", default="left")
    parser.add_argument("--right-name", default="right")
    parser.add_argument("--top-k", default="10,20,40")
    parser.add_argument("--epsilon", type=float, default=1.0e-12)
    parser.add_argument("--out-json", default="outputs/sensitivity_split_stability_summary.json")
    parser.add_argument("--out-md", default="outputs/sensitivity_split_stability_report.md")
    args = parser.parse_args()

    result = build_result(args)
    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "score_spearman": result["score_spearman"]}, indent=2))


if __name__ == "__main__":
    main()
