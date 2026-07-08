#!/usr/bin/env python3
from __future__ import annotations

"""Build an AWQ-aware calibration-stability proxy for quantized 14B checkpoints.

This script does not fake-quantize AWQ weights. It hooks AutoAWQ
``WQLinear_GEMM`` modules, measures calibration activation magnitude, combines
it with AWQ scale magnitude, and reports split agreement plus an equal-budget
proxy allocation. It is evidence for AWQ-aware calibration stability, not a
replacement for full FP16 fake-quant CSI.
"""

import argparse
import json
import math
import random
import time
from pathlib import Path
from typing import Any

try:
    import torch
    from transformers import AutoTokenizer
except ModuleNotFoundError:  # pragma: no cover - exercised by runtime env
    torch = None
    AutoTokenizer = None


def normalize_stats(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized = []
    for row in rows:
        in_features = int(row.get("in_features") or 0)
        out_features = int(row.get("out_features") or 0)
        param_count = int(row.get("param_count") or (in_features * out_features))
        mean_abs_input = float(row.get("mean_abs_input") or 0.0)
        mean_abs_scale = float(row.get("mean_abs_scale") or 0.0)
        score = mean_abs_input * mean_abs_scale
        normalized.append(
            {
                **row,
                "in_features": in_features,
                "out_features": out_features,
                "param_count": param_count,
                "cost": float(param_count),
                "mean_abs_input": mean_abs_input,
                "mean_abs_scale": mean_abs_scale,
                "score": score,
                "score_per_cost": score / max(float(param_count), 1.0),
            }
        )
    normalized.sort(key=lambda item: (-float(item["score"]), str(item["module"])))
    for rank, row in enumerate(normalized, start=1):
        row["rank"] = rank
    return normalized


def _rank_map(rows: list[dict[str, Any]]) -> dict[str, int]:
    return {str(row["module"]): int(row["rank"]) for row in rows}


def _spearman_from_ranks(left: dict[str, int], right: dict[str, int]) -> float:
    common = sorted(set(left) & set(right))
    n = len(common)
    if n < 2:
        return 0.0
    d2 = sum((left[name] - right[name]) ** 2 for name in common)
    return 1.0 - (6.0 * d2) / (n * ((n * n) - 1))


def compare_splits(left: list[dict[str, Any]], right: list[dict[str, Any]], top_fraction: float = 0.25) -> dict[str, Any]:
    left_ranks = _rank_map(left)
    right_ranks = _rank_map(right)
    common = sorted(set(left_ranks) & set(right_ranks))
    top_k = max(1, int(math.ceil(len(common) * float(top_fraction))))
    left_top = {str(row["module"]) for row in left[:top_k]}
    right_top = {str(row["module"]) for row in right[:top_k]}
    union = left_top | right_top
    return {
        "shared_modules": len(common),
        "top_fraction": top_fraction,
        "top_k": top_k,
        "top_intersection": len(left_top & right_top),
        "top_union": len(union),
        "top_jaccard": len(left_top & right_top) / max(len(union), 1),
        "spearman": _spearman_from_ranks(left_ranks, right_ranks),
    }


def build_allocation(rows: list[dict[str, Any]], base_bits: int, high_bits: int, budget_avg_bits: float) -> dict[str, Any]:
    total_cost = sum(float(row["cost"]) for row in rows)
    target = float(budget_avg_bits) * total_cost
    memory = float(base_bits) * total_cost
    bits_by_module = {str(row["module"]): int(base_bits) for row in rows}
    ranked = sorted(rows, key=lambda row: (-float(row["score_per_cost"]), -float(row["score"]), str(row["module"])))
    for row in ranked:
        extra = float(high_bits - base_bits) * float(row["cost"])
        if memory + extra <= target + 1.0e-9:
            bits_by_module[str(row["module"])] = int(high_bits)
            memory += extra
    hist: dict[str, int] = {}
    for bits in bits_by_module.values():
        hist[str(bits)] = hist.get(str(bits), 0) + 1
    selected = [row for row in rows if bits_by_module[str(row["module"])] == high_bits]
    return {
        "base_bits": base_bits,
        "high_bits": high_bits,
        "budget_avg_bits": budget_avg_bits,
        "memory": memory,
        "target_memory": target,
        "budget_used": memory / max(target, 1.0e-12),
        "avg_bits": memory / max(total_cost, 1.0e-12),
        "bit_hist": hist,
        "bits_by_module": bits_by_module,
        "selected_high_modules": [str(row["module"]) for row in selected],
    }


def patch_autoawq_activation_compat() -> None:
    import transformers.activations as activations

    if not hasattr(activations, "PytorchGELUTanh") and hasattr(activations, "GELUActivation"):
        activations.PytorchGELUTanh = activations.GELUActivation


def load_prompts(path: Path, sample_size: int, seed: int) -> list[str]:
    prompts = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if sample_size and sample_size < len(prompts):
        rng = random.Random(seed)
        indices = sorted(rng.sample(range(len(prompts)), sample_size))
        prompts = [prompts[i] for i in indices]
    return prompts


def collect_awq_modules(model: Any, max_modules: int = 0) -> list[tuple[str, Any]]:
    inner = getattr(model, "model", model)
    modules = []
    for name, module in inner.named_modules():
        if module.__class__.__name__ != "WQLinear_GEMM":
            continue
        modules.append((name, module))
        if max_modules and len(modules) >= max_modules:
            break
    return modules


def collect_split_stats(model: Any, tokenizer: Any, prompts: list[str], max_length: int, max_modules: int = 0) -> list[dict[str, Any]]:
    modules = collect_awq_modules(model, max_modules=max_modules)
    stats = {
        name: {
            "abs_sum": 0.0,
            "sq_sum": 0.0,
            "numel": 0,
            "in_features": int(getattr(module, "in_features", 0) or 0),
            "out_features": int(getattr(module, "out_features", 0) or 0),
            "w_bit": int(getattr(module, "w_bit", 0) or 0),
            "group_size": int(getattr(module, "group_size", 0) or 0),
            "mean_abs_scale": float(module.scales.detach().abs().float().mean().cpu().item()) if hasattr(module, "scales") else 0.0,
        }
        for name, module in modules
    }
    handles = []

    def make_hook(module_name: str):
        def hook(_module: Any, inputs: tuple[Any, ...], _output: Any) -> None:
            if not inputs:
                return
            x = inputs[0]
            if not torch.is_tensor(x):
                return
            xf = x.detach().float()
            item = stats[module_name]
            item["abs_sum"] += float(xf.abs().sum().cpu().item())
            item["sq_sum"] += float((xf * xf).sum().cpu().item())
            item["numel"] += int(xf.numel())

        return hook

    for name, module in modules:
        handles.append(module.register_forward_hook(make_hook(name)))
    try:
        with torch.inference_mode():
            for prompt in prompts:
                batch = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
                batch = {key: value.to("cuda") for key, value in batch.items()}
                model(**batch)
    finally:
        for handle in handles:
            handle.remove()
    rows = []
    for name, item in stats.items():
        numel = max(int(item["numel"]), 1)
        in_features = int(item["in_features"])
        out_features = int(item["out_features"])
        rows.append(
            {
                "module": name,
                "in_features": in_features,
                "out_features": out_features,
                "param_count": in_features * out_features,
                "w_bit": int(item["w_bit"]),
                "group_size": int(item["group_size"]),
                "mean_abs_input": float(item["abs_sum"]) / numel,
                "rms_input": math.sqrt(float(item["sq_sum"]) / numel),
                "mean_abs_scale": float(item["mean_abs_scale"]),
                "observed_elements": int(item["numel"]),
            }
        )
    return normalize_stats(rows)


def markdown_report(result: dict[str, Any]) -> str:
    comparison = result["comparison"]
    allocation = result["allocation"]
    lines = [
        "# Qwen2.5-14B AWQ Activation CSI Proxy",
        "",
        f"Model: `{result['model']}`",
        f"Prompt file: `{result['prompt_file']}`",
        f"Prompt sample size: `{result['prompt_sample_size']}`",
        f"Seeds: `{result['seeds']}`",
        "",
        "## Split Agreement",
        "",
        "| metric | value |",
        "|---|---:|",
        f"| shared WQLinear modules | {comparison['shared_modules']} |",
        f"| top-k | {comparison['top_k']} |",
        f"| top-k Jaccard | {comparison['top_jaccard']:.4f} |",
        f"| Spearman rank correlation | {comparison['spearman']:.4f} |",
        "",
        "## Proxy Allocation",
        "",
        "| metric | value |",
        "|---|---:|",
        f"| average bits | {allocation['avg_bits']:.4f} |",
        f"| budget used | {allocation['budget_used']:.4f} |",
        f"| bit histogram | {allocation['bit_hist']} |",
        "",
        "## Scope",
        "",
        "This is an AWQ-aware calibration-stability proxy over `WQLinear_GEMM` modules.",
        "It does not dequantize or re-quantize 14B weights and should not be claimed as full 14B fake-quant CSI downstream evidence.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--prompt-file", type=Path, required=True)
    parser.add_argument("--prompt-sample-size", type=int, default=64)
    parser.add_argument("--seeds", default="0,1")
    parser.add_argument("--max-length", type=int, default=128)
    parser.add_argument("--max-modules", type=int, default=0)
    parser.add_argument("--base-bits", type=int, default=2)
    parser.add_argument("--high-bits", type=int, default=4)
    parser.add_argument("--budget-avg-bits", type=float, default=3.0)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    if torch is None or AutoTokenizer is None:
        raise SystemExit("This script requires torch, transformers, and autoawq.")
    patch_autoawq_activation_compat()
    from awq import AutoAWQForCausalLM

    seeds = [int(item.strip()) for item in args.seeds.split(",") if item.strip()]
    if len(seeds) != 2:
        raise SystemExit("--seeds must contain exactly two comma-separated integers")
    start = time.time()
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoAWQForCausalLM.from_quantized(
        args.model,
        trust_remote_code=True,
        fuse_layers=False,
        safetensors=True,
        device_map={"": "cuda:0"},
    )
    split_rows = []
    for seed in seeds:
        prompts = load_prompts(args.prompt_file, args.prompt_sample_size, seed)
        split_rows.append(
            {
                "seed": seed,
                "prompt_count": len(prompts),
                "rows": collect_split_stats(model, tokenizer, prompts, args.max_length, args.max_modules),
            }
        )
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    comparison = compare_splits(split_rows[0]["rows"], split_rows[1]["rows"])
    left_by_name = {str(row["module"]): row for row in split_rows[0]["rows"]}
    right_by_name = {str(row["module"]): row for row in split_rows[1]["rows"]}
    consensus_rows = []
    for name in sorted(set(left_by_name) & set(right_by_name)):
        left = left_by_name[name]
        right = right_by_name[name]
        consensus_rows.append(
            {
                **right,
                "mean_abs_input": 0.5 * (float(left["mean_abs_input"]) + float(right["mean_abs_input"])),
                "mean_abs_scale": 0.5 * (float(left["mean_abs_scale"]) + float(right["mean_abs_scale"])),
                "left_rank": int(left["rank"]),
                "right_rank": int(right["rank"]),
            }
        )
    consensus_rows = normalize_stats(consensus_rows)
    allocation = build_allocation(consensus_rows, args.base_bits, args.high_bits, args.budget_avg_bits)
    result = {
        "date": time.strftime("%Y-%m-%d"),
        "model": args.model,
        "prompt_file": str(args.prompt_file),
        "prompt_sample_size": args.prompt_sample_size,
        "seeds": seeds,
        "max_length": args.max_length,
        "max_modules": args.max_modules,
        "module_class": "WQLinear_GEMM",
        "elapsed_sec": time.time() - start,
        "split_summaries": [
            {"seed": item["seed"], "prompt_count": item["prompt_count"], "module_count": len(item["rows"])}
            for item in split_rows
        ],
        "comparison": comparison,
        "allocation": allocation,
        "top_consensus_modules": consensus_rows[:40],
        "claim_boundary": "AWQ-aware activation/scale CSI proxy only; not full 14B fake-quant downstream CSI.",
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps({"out_json": str(args.out_json), "out_md": str(args.out_md), "comparison": comparison, "allocation": {k: allocation[k] for k in ["avg_bits", "budget_used", "bit_hist"]}}, indent=2))


if __name__ == "__main__":
    main()
