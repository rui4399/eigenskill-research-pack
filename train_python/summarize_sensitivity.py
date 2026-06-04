#!/usr/bin/env python3
from __future__ import annotations

"""Create compact summaries from module loss-sensitivity artifacts."""

import argparse
import json
from pathlib import Path


def category(module: str) -> str:
    if module == "lm_head":
        return "lm_head"
    if ".self_attn.q_proj" in module:
        return "attn.q_proj"
    if ".self_attn.k_proj" in module:
        return "attn.k_proj"
    if ".self_attn.v_proj" in module:
        return "attn.v_proj"
    if ".self_attn.o_proj" in module:
        return "attn.o_proj"
    if ".mlp.gate_proj" in module:
        return "mlp.gate_proj"
    if ".mlp.up_proj" in module:
        return "mlp.up_proj"
    if ".mlp.down_proj" in module:
        return "mlp.down_proj"
    return "other"


def load_allocation(path: str, method: str) -> dict[str, int]:
    if not path:
        return {}
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    groups = data["groups"]
    bits = data["allocations"][method]
    return {group["module"]: int(bit) for group, bit in zip(groups, bits)}


def slim(group: dict, allocation: dict[str, int]) -> dict:
    module = group["module"]
    return {
        "rank": int(group.get("sensitivity_rank", 0)),
        "module": module,
        "category": category(module),
        "bits": allocation.get(module),
        "params": int(group.get("param_count", group.get("weight_params", 0))),
        "shape": group.get("shape", []),
        "delta_nll": float(group.get("delta_nll", 0.0)),
        "positive_delta_nll": float(group.get("positive_delta_nll", 0.0)),
        "delta_per_param": float(group.get("score_delta_per_param", 0.0)),
    }


def histogram(rows: list[dict], key: str) -> dict[str, int]:
    hist: dict[str, int] = {}
    for row in rows:
        value = str(row.get(key))
        hist[value] = hist.get(value, 0) + 1
    return dict(sorted(hist.items()))


def markdown(result: dict) -> str:
    lines = [
        "# Sensitivity Compact Summary",
        "",
        f"Source: `{result['source_json']}`",
        f"Allocation: `{result.get('allocation_json', '')}`",
        f"Method: `{result.get('allocation_method', '')}`",
        "",
        "## Overview",
        "",
        "| metric | value |",
        "|---|---:|",
        f"| modules | {result['module_count']} |",
        f"| selected 8-bit modules | {result['selected_count']} |",
        f"| selected positive delta ratio | {result['selected_positive_delta_ratio']:.4f} |",
        "",
        "## Category Histogram",
        "",
        "| category | all modules | selected 8-bit |",
        "|---|---:|---:|",
    ]
    all_hist = result["category_hist"]
    selected_hist = result["selected_category_hist"]
    for cat in sorted(all_hist):
        lines.append(f"| {cat} | {all_hist.get(cat, 0)} | {selected_hist.get(cat, 0)} |")

    def add_table(title: str, rows: list[dict]) -> None:
        lines.extend(
            [
                "",
                f"## {title}",
                "",
                "| rank | bits | module | category | params | delta NLL | delta/param |",
                "|---:|---:|---|---|---:|---:|---:|",
            ]
        )
        for row in rows:
            bits = "" if row["bits"] is None else row["bits"]
            lines.append(
                f"| {row['rank']} | {bits} | `{row['module']}` | {row['category']} | "
                f"{row['params']} | {row['positive_delta_nll']:.6f} | {row['delta_per_param']:.3e} |"
            )

    add_table("Top Absolute Positive Delta", result["top_absolute"])
    add_table("Top Cost-Normalized Delta", result["top_normalized"])
    add_table("Selected 8-bit Modules By Rank", result["selected_by_rank"])

    lines.extend(
        [
            "",
            "## Note",
            "",
            "Absolute loss increase and cost-normalized loss increase can disagree.",
            "The allocation is budget-constrained, so small but highly sensitive",
            "projection matrices can outrank very large modules with bigger absolute",
            "delta but lower delta per parameter.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-json", required=True)
    parser.add_argument("--allocation-json", default="")
    parser.add_argument("--allocation-method", default="loss_sensitive_4to8")
    parser.add_argument("--top-k", type=int, default=20)
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    source = json.loads(Path(args.source_json).read_text(encoding="utf-8"))
    allocation = load_allocation(args.allocation_json, args.allocation_method)
    rows = [slim(group, allocation) for group in source["groups"]]
    selected = [row for row in rows if row["bits"] == 8]
    positive_total = sum(row["positive_delta_nll"] for row in rows)
    selected_positive = sum(row["positive_delta_nll"] for row in selected)

    result = {
        "source_json": args.source_json,
        "allocation_json": args.allocation_json,
        "allocation_method": args.allocation_method,
        "module_count": len(rows),
        "selected_count": len(selected),
        "selected_positive_delta_ratio": selected_positive / max(positive_total, 1.0e-12),
        "category_hist": histogram(rows, "category"),
        "selected_category_hist": histogram(selected, "category"),
        "top_absolute": sorted(rows, key=lambda row: (row["positive_delta_nll"], row["delta_per_param"]), reverse=True)[: args.top_k],
        "top_normalized": sorted(rows, key=lambda row: (row["delta_per_param"], row["positive_delta_nll"]), reverse=True)[: args.top_k],
        "selected_by_rank": sorted(selected, key=lambda row: row["rank"])[: args.top_k],
    }

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "selected_count": result["selected_count"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
