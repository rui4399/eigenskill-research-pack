#!/usr/bin/env python3
from __future__ import annotations

"""Measure per-module fake-quant loss sensitivity for EigenSkill-Q.

The earlier EigenSkill-Q allocator used activation statistics as a cheap
sensitivity proxy. This script measures a stronger signal directly: quantize
one Linear module at a time, evaluate the short-prompt next-token loss increase,
restore the original weight, and rank modules by loss increase per extra bit
cost.

It emits an allocation JSON compatible with eval_weight_quant_ppl.py:

    python train_python/eval_weight_quant_ppl.py \
      --allocation outputs/smollm2_loss_sensitive_alloc_4to8_summary.json \
      --allocation-method loss_sensitive_4to8

This remains a fake-quant diagnostic. It does not prove compressed runtime
memory, latency, or edge-board energy savings.
"""

import argparse
import gc
import json
import math
import time
from pathlib import Path

try:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
except ModuleNotFoundError:
    torch = None
    AutoModelForCausalLM = None
    AutoTokenizer = None


DEFAULT_PROMPTS = [
    "Explain why mixed-precision quantization can preserve model quality better than uniform quantization.",
    "A transformer layer has high activation outliers and high Hessian sensitivity. Which quantization policy is safer?",
    "Reason step by step: if memory budget is tight, should a sensitive attention projection use 2-bit or 4-bit weights?",
    "Write compact JSON for a quantization policy that protects outlier channels.",
    "Summarize the relation between rate-distortion theory and LLM bit allocation.",
    "If KV cache context length grows to 8192 tokens, what compression risks should be checked?",
    "Compute a qualitative tradeoff between latency, memory, and perplexity for edge LLM inference.",
    "Why can a deterministic policy kernel be safer than asking a small model to emit numeric JSON?",
]


def load_prompts(path: str, limit: int) -> list[str]:
    if path:
        prompts = [line.strip() for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]
    else:
        prompts = list(DEFAULT_PROMPTS)
    return prompts[:limit] if limit else prompts


def quantize_weight(weight: torch.Tensor, bits: int, group_size: int = 0) -> torch.Tensor:
    if bits >= 16:
        return weight
    qmax = (2 ** (bits - 1)) - 1
    if qmax <= 0:
        raise ValueError(f"unsupported bits: {bits}")
    w = weight.detach().float()
    flat = w.reshape(w.shape[0], -1)
    if group_size and group_size > 0 and group_size < flat.shape[1]:
        pieces = []
        for start in range(0, flat.shape[1], group_size):
            chunk = flat[:, start : start + group_size]
            scale = chunk.abs().amax(dim=1, keepdim=True).clamp_min(1.0e-8) / qmax
            q = torch.round(chunk / scale).clamp(-qmax, qmax)
            pieces.append(q * scale)
        deq = torch.cat(pieces, dim=1).reshape_as(w)
    else:
        scale = flat.abs().amax(dim=1, keepdim=True).clamp_min(1.0e-8) / qmax
        q = torch.round(flat / scale).clamp(-qmax, qmax)
        deq = (q * scale).reshape_as(w)
    return deq.to(dtype=weight.dtype, device=weight.device)


def tokenize_prompts(tokenizer, prompts: list[str], device: str, max_length: int) -> list[dict]:
    batches = []
    for prompt in prompts:
        batch = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
        input_ids = batch["input_ids"].to(device)
        if input_ids.shape[1] < 2:
            continue
        item = {"input_ids": input_ids}
        if "attention_mask" in batch:
            item["attention_mask"] = batch["attention_mask"].to(device)
        batches.append(item)
    return batches


def eval_nll(model: torch.nn.Module, batches: list[dict]) -> dict:
    total_nll = 0.0
    total_tokens = 0
    per_prompt = []
    with torch.inference_mode():
        for batch in batches:
            input_ids = batch["input_ids"]
            tokens = input_ids.shape[1] - 1
            out = model(
                input_ids=input_ids,
                attention_mask=batch.get("attention_mask"),
                labels=input_ids,
            )
            loss = float(out.loss.detach().float().item())
            total_nll += loss * tokens
            total_tokens += tokens
            per_prompt.append({"tokens": tokens, "loss": loss, "ppl": math.exp(loss) if loss < 50 else float("inf")})
            del out
    mean_nll = total_nll / max(total_tokens, 1)
    return {
        "prompt_count": len(per_prompt),
        "tokens": total_tokens,
        "mean_nll": mean_nll,
        "ppl": math.exp(mean_nll) if mean_nll < 50 else float("inf"),
        "per_prompt": per_prompt,
    }


def collect_linear_modules(model: torch.nn.Module, max_modules: int) -> list[dict]:
    modules = []
    for name, module in model.named_modules():
        if not isinstance(module, torch.nn.Linear):
            continue
        weight_params = int(module.weight.numel())
        bias_params = int(module.bias.numel()) if module.bias is not None else 0
        modules.append(
            {
                "index": len(modules),
                "module": name,
                "name": name,
                "layer": len(modules),
                "group": len(modules),
                "shape": list(module.weight.shape),
                "param_count": weight_params + bias_params,
                "weight_params": weight_params,
                "bias_params": bias_params,
                "cost": float(weight_params + bias_params),
                "_module_ref": module,
            }
        )
        if max_modules and len(modules) >= max_modules:
            break
    return modules


def measure_modules(
    model: torch.nn.Module,
    batches: list[dict],
    modules: list[dict],
    bits: int,
    group_size: int,
    progress_every: int,
    device: str,
) -> tuple[dict, list[dict]]:
    baseline = eval_nll(model, batches)
    base_nll = baseline["mean_nll"]
    measured = []
    start_time = time.time()

    for idx, item in enumerate(modules, start=1):
        module = item["_module_ref"]
        with torch.no_grad():
            original = module.weight.detach().clone()
            module.weight.data.copy_(quantize_weight(module.weight.data, bits, group_size=group_size))
        metrics = eval_nll(model, batches)
        with torch.no_grad():
            module.weight.data.copy_(original)
        del original
        if device == "cuda":
            torch.cuda.empty_cache()
        gc.collect()

        delta_nll = metrics["mean_nll"] - base_nll
        positive_delta = max(delta_nll, 0.0)
        extra_cost_fp16 = item["cost"] * max(16 - bits, 1)
        score_per_param = positive_delta / max(item["cost"], 1.0e-12)
        score_fp16 = positive_delta / max(extra_cost_fp16, 1.0e-12)
        record = {k: v for k, v in item.items() if not k.startswith("_")}
        record.update(
            {
                "quant_bits": bits,
                "group_size": group_size,
                "quantized_mean_nll": metrics["mean_nll"],
                "quantized_ppl": metrics["ppl"],
                "delta_nll": delta_nll,
                "positive_delta_nll": positive_delta,
                "extra_cost_to_keep_fp16": extra_cost_fp16,
                "score_delta_per_param": score_per_param,
                "score_delta_per_extra_fp16_cost": score_fp16,
            }
        )
        measured.append(record)

        if progress_every and (idx == 1 or idx % progress_every == 0 or idx == len(modules)):
            elapsed = time.time() - start_time
            print(
                json.dumps(
                    {
                        "progress": f"{idx}/{len(modules)}",
                        "module": item["module"],
                        "delta_nll": delta_nll,
                        "elapsed_sec": round(elapsed, 2),
                    },
                    ensure_ascii=False,
                ),
                flush=True,
            )

    return baseline, measured


def summarize_allocation(name: str, groups: list[dict], alloc: list[int], budget_avg_bits: float) -> dict:
    total_cost = sum(float(g["cost"]) for g in groups)
    memory = sum(float(g["cost"]) * bits for g, bits in zip(groups, alloc))
    budget = budget_avg_bits * total_cost
    positive_total = sum(float(g.get("positive_delta_nll", 0.0)) for g in groups)
    positive_protected = sum(float(g.get("positive_delta_nll", 0.0)) for g, bits in zip(groups, alloc) if bits > min(alloc))
    bit_hist: dict[str, int] = {}
    for bits in alloc:
        bit_hist[str(bits)] = bit_hist.get(str(bits), 0) + 1
    return {
        "name": name,
        "groups": len(groups),
        "budget_avg_bits": budget_avg_bits,
        "memory": memory,
        "budget": budget,
        "budget_used": memory / max(budget, 1.0e-12),
        "avg_bits": memory / max(total_cost, 1.0e-12),
        "bit_hist": bit_hist,
        "positive_delta_nll_total": positive_total,
        "positive_delta_nll_protected": positive_protected,
        "positive_delta_nll_protected_ratio": positive_protected / max(positive_total, 1.0e-12),
    }


def loss_sensitive_4to8(groups: list[dict], budget_avg_bits: float, base_bits: int, high_bits: int) -> list[int]:
    if high_bits <= base_bits:
        raise ValueError("--high-bits must be greater than --base-bits")
    total_cost = sum(float(g["cost"]) for g in groups)
    base_memory = base_bits * total_cost
    budget = budget_avg_bits * total_cost
    remaining = max(budget - base_memory, 0.0)
    alloc = [base_bits] * len(groups)
    ranked = sorted(
        range(len(groups)),
        key=lambda idx: (
            float(groups[idx].get("positive_delta_nll", 0.0)) / max((high_bits - base_bits) * float(groups[idx]["cost"]), 1.0e-12),
            float(groups[idx].get("positive_delta_nll", 0.0)),
        ),
        reverse=True,
    )
    for idx in ranked:
        extra = (high_bits - base_bits) * float(groups[idx]["cost"])
        if extra <= remaining + 1.0e-9 and float(groups[idx].get("positive_delta_nll", 0.0)) > 0.0:
            alloc[idx] = high_bits
            remaining -= extra
    return alloc


def rank_groups(groups: list[dict]) -> list[dict]:
    order = sorted(
        range(len(groups)),
        key=lambda idx: (
            float(groups[idx].get("positive_delta_nll", 0.0)) / max(float(groups[idx]["cost"]), 1.0e-12),
            float(groups[idx].get("positive_delta_nll", 0.0)),
        ),
        reverse=True,
    )
    ranks = {idx: rank + 1 for rank, idx in enumerate(order)}
    ranked = []
    for idx, group in enumerate(groups):
        item = dict(group)
        item["sensitivity_rank"] = ranks[idx]
        # Compatibility with rate_distortion_allocator.py's GroupStat schema.
        item["sensitivity"] = float(item.get("positive_delta_nll", 0.0))
        item["variance"] = 1.0
        item["outlier"] = float(item.get("quantized_ppl", 0.0))
        ranked.append(item)
    return ranked


def markdown_report(result: dict, top_k: int = 20) -> str:
    baseline = result["baseline"]
    lines = [
        "# SmolLM2 Module Loss Sensitivity Report",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Prompts: `{result['prompt_count']}`",
        f"Max length: `{result['max_length']}`",
        f"Quantized bits during probing: `{result['probe_bits']}`",
        f"Group size: `{result['group_size']}`",
        "",
        "## Baseline",
        "",
        f"- FP16 mean NLL: `{baseline['mean_nll']:.6f}`",
        f"- FP16 PPL: `{baseline['ppl']:.6f}`",
        f"- Tokens: `{baseline['tokens']}`",
        "",
        "## Allocation Summary",
        "",
        "| method | avg bits | budget used | bit histogram | protected positive delta |",
        "|---|---:|---:|---|---:|",
    ]
    for item in result["summaries"]:
        lines.append(
            f"| {item['name']} | {item['avg_bits']:.4f} | {item['budget_used']:.4f} | "
            f"{item['bit_hist']} | {item['positive_delta_nll_protected_ratio']:.4f} |"
        )

    top = sorted(
        result["groups"],
        key=lambda g: (float(g.get("positive_delta_nll", 0.0)), float(g.get("score_delta_per_param", 0.0))),
        reverse=True,
    )[:top_k]
    lines.extend(
        [
            "",
            f"## Top {len(top)} Sensitive Modules",
            "",
            "| rank | module | params | delta NLL | delta NLL / param |",
            "|---:|---|---:|---:|---:|",
        ]
    )
    for item in top:
        lines.append(
            f"| {item['sensitivity_rank']} | `{item['module']}` | {int(item['param_count'])} | "
            f"{float(item['delta_nll']):.6f} | {float(item['score_delta_per_param']):.12f} |"
        )

    lines.extend(
        [
            "",
            "## Scope",
            "",
            "- This is a per-module fake-quant diagnostic, not a production quantizer.",
            "- It measures short-prompt loss sensitivity and writes an allocation file",
            "  that can be evaluated by `eval_weight_quant_ppl.py`.",
            "- Memory/latency claims still require real compressed storage or a",
            "  quantized runtime.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="HuggingFaceTB/SmolLM2-360M-Instruct")
    parser.add_argument("--prompts", default="")
    parser.add_argument("--limit-prompts", type=int, default=4)
    parser.add_argument("--max-length", type=int, default=128)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--probe-bits", type=int, default=4)
    parser.add_argument("--group-size", type=int, default=128)
    parser.add_argument("--max-modules", type=int, default=0, help="0 means all Linear modules")
    parser.add_argument("--base-bits", type=int, default=4)
    parser.add_argument("--high-bits", type=int, default=8)
    parser.add_argument("--budget-avg-bits", type=float, default=4.5)
    parser.add_argument("--progress-every", type=int, default=12)
    parser.add_argument("--out-json", default="outputs/smollm2_module_loss_sensitivity.json")
    parser.add_argument("--out-md", default="outputs/smollm2_module_loss_sensitivity_report.md")
    parser.add_argument("--out-allocation", default="outputs/smollm2_loss_sensitive_alloc_4to8_summary.json")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("This script requires torch and transformers. Run it in the WSL GPU Python environment.")
    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")

    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=dtype)
    model.eval()
    model.to(args.device)

    prompts = load_prompts(args.prompts, args.limit_prompts)
    batches = tokenize_prompts(tokenizer, prompts, args.device, args.max_length)
    modules = collect_linear_modules(model, args.max_modules)
    baseline, measured = measure_modules(
        model=model,
        batches=batches,
        modules=modules,
        bits=args.probe_bits,
        group_size=args.group_size,
        progress_every=args.progress_every,
        device=args.device,
    )
    groups = rank_groups(measured)
    alloc_loss = loss_sensitive_4to8(groups, args.budget_avg_bits, args.base_bits, args.high_bits)
    alloc_uniform = [args.base_bits] * len(groups)
    summaries = [
        summarize_allocation(f"uniform_int{args.base_bits}", groups, alloc_uniform, args.budget_avg_bits),
        summarize_allocation("loss_sensitive_4to8", groups, alloc_loss, args.budget_avg_bits),
    ]
    result = {
        "date": time.strftime("%Y-%m-%d"),
        "model": args.model,
        "prompt_count": len(batches),
        "max_length": args.max_length,
        "device": args.device,
        "dtype": args.dtype,
        "probe_bits": args.probe_bits,
        "group_size": args.group_size,
        "base_bits": args.base_bits,
        "high_bits": args.high_bits,
        "budget_avg_bits": args.budget_avg_bits,
        "baseline": baseline,
        "linear_modules": len(groups),
        "groups": groups,
        "allocations": {
            f"uniform_int{args.base_bits}": alloc_uniform,
            "loss_sensitive_4to8": alloc_loss,
        },
        "summaries": summaries,
    }

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_alloc = Path(args.out_allocation)
    out_alloc.parent.mkdir(parents=True, exist_ok=True)
    out_alloc.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown_report(result), encoding="utf-8")
    print(
        json.dumps(
            {
                "out_json": str(out_json),
                "out_md": str(out_md),
                "out_allocation": str(out_alloc),
                "summaries": summaries,
            },
            ensure_ascii=False,
            indent=2,
        )
    )

    del model
    if args.device == "cuda":
        torch.cuda.empty_cache()
    gc.collect()


if __name__ == "__main__":
    main()
