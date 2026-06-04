#!/usr/bin/env python3
from __future__ import annotations

"""Interaction-aware swap search for mixed-precision fake-quant allocation.

This is a small policy-improvement experiment. It starts from an allocation
file, proposes budget-feasible one-out/one-in swaps among 8-bit modules, and
evaluates the resulting global PPL on a prompt slice. The goal is to test
whether direct global feedback can improve over additive one-module sensitivity.

The script is intentionally bounded by `--max-swaps`; it is not an efficient
production quantizer.
"""

import argparse
import copy
import gc
import json
import math
from pathlib import Path

try:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
except ModuleNotFoundError:
    torch = None
    AutoModelForCausalLM = None
    AutoTokenizer = None


def load_prompts(path: str, limit: int) -> list[str]:
    prompts = [line.strip() for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]
    return prompts[:limit] if limit else prompts


def quantize_weight(weight: torch.Tensor, bits: int, group_size: int) -> torch.Tensor:
    if bits >= 16:
        return weight
    qmax = (2 ** (bits - 1)) - 1
    w = weight.detach().float()
    flat = w.reshape(w.shape[0], -1)
    if group_size and group_size > 0 and group_size < flat.shape[1]:
        chunks = []
        for start in range(0, flat.shape[1], group_size):
            chunk = flat[:, start : start + group_size]
            scale = chunk.abs().amax(dim=1, keepdim=True).clamp_min(1.0e-8) / qmax
            q = torch.round(chunk / scale).clamp(-qmax, qmax)
            chunks.append(q * scale)
        deq = torch.cat(chunks, dim=1).reshape_as(w)
    else:
        scale = flat.abs().amax(dim=1, keepdim=True).clamp_min(1.0e-8) / qmax
        q = torch.round(flat / scale).clamp(-qmax, qmax)
        deq = (q * scale).reshape_as(w)
    return deq.to(dtype=weight.dtype, device=weight.device)


def eval_ppl(model: torch.nn.Module, tokenizer, prompts: list[str], device: str, max_length: int) -> dict:
    total_nll = 0.0
    total_tokens = 0
    with torch.no_grad():
        for prompt in prompts:
            batch = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
            input_ids = batch["input_ids"].to(device)
            if input_ids.shape[1] < 2:
                continue
            out = model(input_ids=input_ids, labels=input_ids)
            tokens = input_ids.shape[1] - 1
            loss = float(out.loss.item())
            total_nll += loss * tokens
            total_tokens += tokens
            del out
    mean_nll = total_nll / max(total_tokens, 1)
    return {"tokens": total_tokens, "mean_nll": mean_nll, "ppl": math.exp(mean_nll) if mean_nll < 50 else float("inf")}


def load_allocation(path: str, method: str) -> tuple[list[dict], list[int], dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data["groups"], [int(x) for x in data["allocations"][method]], data


def write_allocation(base_meta: dict, groups: list[dict], alloc: list[int], method: str, out: Path) -> None:
    bit_hist: dict[str, int] = {}
    for bits in alloc:
        bit_hist[str(bits)] = bit_hist.get(str(bits), 0) + 1
    total_cost = sum(float(g["cost"]) for g in groups)
    memory = sum(float(g["cost"]) * bits for g, bits in zip(groups, alloc))
    budget_avg_bits = memory / max(total_cost, 1.0e-12)
    positive_total = sum(float(g.get("positive_delta_nll", 0.0)) for g in groups)
    positive_protected = sum(float(g.get("positive_delta_nll", 0.0)) for g, bits in zip(groups, alloc) if bits > min(alloc))
    result = copy.deepcopy(base_meta)
    result["groups"] = groups
    result["allocations"] = {method: alloc}
    result["summaries"] = [
        {
            "name": method,
            "groups": len(groups),
            "budget_avg_bits": budget_avg_bits,
            "memory": memory,
            "budget": memory,
            "budget_used": 1.0,
            "avg_bits": budget_avg_bits,
            "bit_hist": bit_hist,
            "positive_delta_nll_total": positive_total,
            "positive_delta_nll_protected": positive_protected,
            "positive_delta_nll_protected_ratio": positive_protected / max(positive_total, 1.0e-12),
        }
    ]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


def apply_allocation(model: torch.nn.Module, groups: list[dict], alloc: list[int], group_size: int) -> None:
    module_map = dict(model.named_modules())
    with torch.no_grad():
        for group, bits in zip(groups, alloc):
            module = module_map.get(group.get("module", ""))
            if module is None or not isinstance(module, torch.nn.Linear):
                continue
            if bits < 16:
                module.weight.data.copy_(quantize_weight(module.weight.data, bits, group_size=group_size))


def evaluate_allocation(args, tokenizer, prompts: list[str], groups: list[dict], alloc: list[int]) -> dict:
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=dtype)
    model.eval()
    model.to(args.device)
    apply_allocation(model, groups, alloc, args.group_size)
    metrics = eval_ppl(model, tokenizer, prompts, args.device, args.max_length)
    del model
    if args.device == "cuda":
        torch.cuda.empty_cache()
    gc.collect()
    return metrics


def propose_swaps(groups: list[dict], alloc: list[int], max_swaps: int, out_pool: int, in_pool: int) -> list[tuple[int, int]]:
    selected = [idx for idx, bits in enumerate(alloc) if bits == 8]
    unselected = [idx for idx, bits in enumerate(alloc) if bits == 4 and float(groups[idx].get("positive_delta_nll", 0.0)) > 0.0]
    selected_ranked = sorted(selected, key=lambda idx: float(groups[idx].get("positive_delta_nll", 0.0)))[:out_pool]
    unselected_ranked = sorted(unselected, key=lambda idx: float(groups[idx].get("positive_delta_nll", 0.0)), reverse=True)[:in_pool]
    scored = []
    for out_idx in selected_ranked:
        out_cost = float(groups[out_idx]["cost"])
        out_delta = float(groups[out_idx].get("positive_delta_nll", 0.0))
        for in_idx in unselected_ranked:
            in_cost = float(groups[in_idx]["cost"])
            if in_cost <= out_cost + 1.0e-9:
                in_delta = float(groups[in_idx].get("positive_delta_nll", 0.0))
                local_gain = in_delta - out_delta
                # Prefer swaps that improve the local proxy, but still allow
                # a few near-neutral candidates because global PPL can disagree
                # with the additive proxy.
                scored.append((local_gain, in_delta, -out_delta, out_idx, in_idx))
    scored.sort(reverse=True)
    return [(out_idx, in_idx) for _gain, _in_delta, _neg_out_delta, out_idx, in_idx in scored[:max_swaps]]


def markdown_report(result: dict) -> str:
    lines = [
        "# Allocation Swap Search Report",
        "",
        f"Base allocation: `{result['base_allocation']}`",
        f"Method: `{result['base_method']}`",
        f"Prompts: `{result['prompt_count']}`",
        f"Evaluated swaps: `{len(result['trials'])}`",
        "",
        "## Result",
        "",
        "| method | PPL | mean NLL | swap |",
        "|---|---:|---:|---|",
        f"| base | {result['base_metrics']['ppl']:.4f} | {result['base_metrics']['mean_nll']:.6f} | - |",
    ]
    best = result["best"]
    swap = best.get("swap")
    lines.append(
        f"| best | {best['metrics']['ppl']:.4f} | {best['metrics']['mean_nll']:.6f} | "
        f"{swap['out_module']} -> {swap['in_module']} |"
    )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This is a bounded one-step policy-improvement search using global PPL",
            "feedback. It tests interaction-aware allocation beyond additive",
            "one-module sensitivity, but it is still a fake-quant diagnostic.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="HuggingFaceTB/SmolLM2-360M-Instruct")
    parser.add_argument("--prompts", default="data_eval/text_prompts/wikitext2_validation_128.txt")
    parser.add_argument("--limit-prompts", type=int, default=128)
    parser.add_argument("--max-length", type=int, default=160)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--group-size", type=int, default=128)
    parser.add_argument("--base-allocation", default="outputs/smollm2_loss_sensitive_alloc_4to8_limit4_group128_summary.json")
    parser.add_argument("--base-method", default="loss_sensitive_4to8")
    parser.add_argument("--max-swaps", type=int, default=8)
    parser.add_argument("--out-pool", type=int, default=12)
    parser.add_argument("--in-pool", type=int, default=16)
    parser.add_argument("--out-json", default="outputs/smollm2_allocation_swap_search_group128_wikitext2_128_summary.json")
    parser.add_argument("--out-md", default="outputs/smollm2_allocation_swap_search_group128_wikitext2_128_report.md")
    parser.add_argument("--out-allocation", default="outputs/smollm2_loss_sensitive_swap_search_alloc_4to8_group128_summary.json")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("This script requires torch and transformers.")
    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")

    groups, base_alloc, base_meta = load_allocation(args.base_allocation, args.base_method)
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    prompts = load_prompts(args.prompts, args.limit_prompts)

    base_metrics = evaluate_allocation(args, tokenizer, prompts, groups, base_alloc)
    best_alloc = list(base_alloc)
    best = {"metrics": base_metrics, "swap": {"out_module": "-", "in_module": "-", "out_index": -1, "in_index": -1}}
    trials = []
    for out_idx, in_idx in propose_swaps(groups, base_alloc, args.max_swaps, args.out_pool, args.in_pool):
        trial_alloc = list(base_alloc)
        trial_alloc[out_idx] = 4
        trial_alloc[in_idx] = 8
        metrics = evaluate_allocation(args, tokenizer, prompts, groups, trial_alloc)
        swap = {
            "out_index": out_idx,
            "in_index": in_idx,
            "out_module": groups[out_idx]["module"],
            "in_module": groups[in_idx]["module"],
            "out_delta": groups[out_idx].get("positive_delta_nll", 0.0),
            "in_delta": groups[in_idx].get("positive_delta_nll", 0.0),
        }
        item = {"swap": swap, "metrics": metrics}
        trials.append(item)
        if metrics["mean_nll"] < best["metrics"]["mean_nll"]:
            best = item
            best_alloc = trial_alloc
        print(json.dumps({"trial": len(trials), "ppl": metrics["ppl"], "swap": swap}, ensure_ascii=False), flush=True)

    result = {
        "model": args.model,
        "prompts": args.prompts,
        "prompt_count": len(prompts),
        "max_length": args.max_length,
        "group_size": args.group_size,
        "base_allocation": args.base_allocation,
        "base_method": args.base_method,
        "base_metrics": base_metrics,
        "trials": trials,
        "best": best,
    }
    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_report(result), encoding="utf-8")
    write_allocation(base_meta, groups, best_alloc, "loss_sensitive_swap_search_4to8", Path(args.out_allocation))
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "out_allocation": args.out_allocation, "base_ppl": base_metrics["ppl"], "best_ppl": best["metrics"]["ppl"], "trials": len(trials)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
