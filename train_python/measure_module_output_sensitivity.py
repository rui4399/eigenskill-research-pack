#!/usr/bin/env python3
from __future__ import annotations

"""Measure per-module output reconstruction sensitivity after fake quantization.

This is a cheaper proxy than one-module full-model loss probing. It samples the
inputs to each Linear module on calibration prompts and scores the module by the
normalized output perturbation caused by quantizing that module's weight:

    E ||x(W - Q(W))^T||^2 / E ||xW^T||^2

The output is an allocation JSON compatible with eval_weight_quant_ppl.py.
"""

import argparse
import gc
import json
import math
import time
from pathlib import Path

try:
    import torch
    import torch.nn.functional as F
    from transformers import AutoModelForCausalLM, AutoTokenizer
except ModuleNotFoundError:
    torch = None
    F = None
    AutoModelForCausalLM = None
    AutoTokenizer = None


DEFAULT_PROMPTS = [
    "Explain why mixed-precision quantization can preserve model quality better than uniform quantization.",
    "A transformer layer has high activation outliers and high Hessian sensitivity. Which quantization policy is safer?",
    "Summarize the relation between rate-distortion theory and LLM bit allocation.",
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


def collect_module_inputs(
    model: torch.nn.Module,
    tokenizer,
    prompts: list[str],
    modules: list[dict],
    device: str,
    max_length: int,
    sample_rows_per_module: int,
) -> tuple[dict[str, list[torch.Tensor]], dict[str, int]]:
    inputs: dict[str, list[torch.Tensor]] = {item["module"]: [] for item in modules}
    row_counts: dict[str, int] = {item["module"]: 0 for item in modules}
    hooks = []

    def make_hook(name: str):
        def hook(_module, args):
            if row_counts[name] >= sample_rows_per_module:
                return
            if not args:
                return
            x = args[0].detach()
            if x.numel() == 0:
                return
            flat = x.reshape(-1, x.shape[-1])
            remaining = sample_rows_per_module - row_counts[name]
            take = min(int(flat.shape[0]), remaining)
            if take <= 0:
                return
            inputs[name].append(flat[:take].to("cpu", dtype=torch.float32))
            row_counts[name] += take

        return hook

    for item in modules:
        hooks.append(item["_module_ref"].register_forward_pre_hook(make_hook(item["module"])))

    try:
        with torch.inference_mode():
            for prompt in prompts:
                batch = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
                input_ids = batch["input_ids"].to(device)
                if input_ids.shape[1] < 2:
                    continue
                attention_mask = batch.get("attention_mask")
                if attention_mask is not None:
                    attention_mask = attention_mask.to(device)
                model(input_ids=input_ids, attention_mask=attention_mask)
    finally:
        for hook in hooks:
            hook.remove()

    return inputs, row_counts


def score_module_outputs(
    modules: list[dict],
    sampled_inputs: dict[str, list[torch.Tensor]],
    bits: int,
    group_size: int,
    device: str,
    chunk_rows: int,
    progress_every: int,
) -> list[dict]:
    measured = []
    start_time = time.time()
    with torch.inference_mode():
        for idx, item in enumerate(modules, start=1):
            name = item["module"]
            rows = sampled_inputs.get(name, [])
            record = {k: v for k, v in item.items() if not k.startswith("_")}
            if not rows:
                record.update(
                    {
                        "quant_bits": bits,
                        "group_size": group_size,
                        "sample_rows": 0,
                        "output_mse": 0.0,
                        "output_signal": 0.0,
                        "normalized_output_mse": 0.0,
                        "score_per_param": 0.0,
                    }
                )
                measured.append(record)
                continue

            x_cpu = torch.cat(rows, dim=0)
            module = item["_module_ref"]
            weight = module.weight.detach().float()
            qweight = quantize_weight(module.weight.detach(), bits, group_size=group_size).float()
            delta = weight - qweight
            sum_sq = 0.0
            signal_sq = 0.0
            count = 0
            for start in range(0, int(x_cpu.shape[0]), chunk_rows):
                x = x_cpu[start : start + chunk_rows].to(device=device, dtype=torch.float32)
                diff = F.linear(x, delta)
                base = F.linear(x, weight)
                sum_sq += float(diff.pow(2).sum().detach().cpu().item())
                signal_sq += float(base.pow(2).sum().detach().cpu().item())
                count += int(diff.numel())
                del x, diff, base
            del weight, qweight, delta
            if device == "cuda":
                torch.cuda.empty_cache()
            gc.collect()

            mse = sum_sq / max(count, 1)
            signal = signal_sq / max(count, 1)
            norm = mse / max(signal, 1.0e-12)
            record.update(
                {
                    "quant_bits": bits,
                    "group_size": group_size,
                    "sample_rows": int(x_cpu.shape[0]),
                    "output_mse": mse,
                    "output_signal": signal,
                    "normalized_output_mse": norm,
                    "score_per_param": norm / max(float(item["cost"]), 1.0e-12),
                }
            )
            measured.append(record)

            if progress_every and (idx == 1 or idx % progress_every == 0 or idx == len(modules)):
                print(
                    json.dumps(
                        {
                            "progress": f"{idx}/{len(modules)}",
                            "module": name,
                            "normalized_output_mse": norm,
                            "elapsed_sec": round(time.time() - start_time, 2),
                        },
                        ensure_ascii=False,
                    ),
                    flush=True,
                )
    return measured


def proxy_sensitive_4to8(groups: list[dict], budget_avg_bits: float, base_bits: int, high_bits: int) -> list[int]:
    total_cost = sum(float(g["cost"]) for g in groups)
    base_memory = base_bits * total_cost
    budget = budget_avg_bits * total_cost
    remaining = max(budget - base_memory, 0.0)
    alloc = [base_bits] * len(groups)
    ranked = sorted(
        range(len(groups)),
        key=lambda idx: (
            float(groups[idx].get("normalized_output_mse", 0.0)) / max((high_bits - base_bits) * float(groups[idx]["cost"]), 1.0e-12),
            float(groups[idx].get("normalized_output_mse", 0.0)),
        ),
        reverse=True,
    )
    for idx in ranked:
        extra = (high_bits - base_bits) * float(groups[idx]["cost"])
        if extra <= remaining + 1.0e-9 and float(groups[idx].get("normalized_output_mse", 0.0)) > 0.0:
            alloc[idx] = high_bits
            remaining -= extra
    return alloc


def summarize_allocation(name: str, groups: list[dict], alloc: list[int], budget_avg_bits: float) -> dict:
    total_cost = sum(float(g["cost"]) for g in groups)
    memory = sum(float(g["cost"]) * bits for g, bits in zip(groups, alloc))
    budget = budget_avg_bits * total_cost
    proxy_total = sum(float(g.get("normalized_output_mse", 0.0)) for g in groups)
    proxy_protected = sum(float(g.get("normalized_output_mse", 0.0)) for g, bits in zip(groups, alloc) if bits > min(alloc))
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
        "normalized_output_mse_total": proxy_total,
        "normalized_output_mse_protected": proxy_protected,
        "normalized_output_mse_protected_ratio": proxy_protected / max(proxy_total, 1.0e-12),
    }


def rank_groups(groups: list[dict]) -> list[dict]:
    order = sorted(
        range(len(groups)),
        key=lambda idx: (
            float(groups[idx].get("normalized_output_mse", 0.0)) / max(float(groups[idx]["cost"]), 1.0e-12),
            float(groups[idx].get("normalized_output_mse", 0.0)),
        ),
        reverse=True,
    )
    ranks = {idx: rank + 1 for rank, idx in enumerate(order)}
    ranked = []
    for idx, group in enumerate(groups):
        item = dict(group)
        item["output_sensitivity_rank"] = ranks[idx]
        ranked.append(item)
    return ranked


def markdown_report(result: dict, top_k: int = 20) -> str:
    lines = [
        "# SmolLM2 Module Output-Reconstruction Sensitivity Report",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Prompts: `{result['prompt_count']}`",
        f"Max length: `{result['max_length']}`",
        f"Sample rows per module: `{result['sample_rows_per_module']}`",
        f"Quantized bits during proxy measurement: `{result['probe_bits']}`",
        f"Group size: `{result['group_size']}`",
        "",
        "## Allocation Summary",
        "",
        "| method | avg bits | budget used | bit histogram | protected proxy |",
        "|---|---:|---:|---|---:|",
    ]
    for item in result["summaries"]:
        lines.append(
            f"| {item['name']} | {item['avg_bits']:.4f} | {item['budget_used']:.4f} | "
            f"{item['bit_hist']} | {item['normalized_output_mse_protected_ratio']:.4f} |"
        )

    top = sorted(
        result["groups"],
        key=lambda g: (float(g.get("normalized_output_mse", 0.0)), float(g.get("score_per_param", 0.0))),
        reverse=True,
    )[:top_k]
    lines.extend(
        [
            "",
            f"## Top {len(top)} Output-Sensitive Modules",
            "",
            "| rank | module | params | normalized output MSE | output MSE / param | sample rows |",
            "|---:|---|---:|---:|---:|---:|",
        ]
    )
    for item in top:
        lines.append(
            f"| {item['output_sensitivity_rank']} | `{item['module']}` | {int(item['param_count'])} | "
            f"{float(item['normalized_output_mse']):.8f} | {float(item['score_per_param']):.12f} | "
            f"{int(item['sample_rows'])} |"
        )

    lines.extend(
        [
            "",
            "## Scope",
            "",
            "- This is an activation/output reconstruction proxy, not a full loss probe.",
            "- It is cheaper than per-module PPL probing but may mis-rank modules whose",
            "  local output error is not aligned with global language-model loss.",
            "- The generated allocation should be evaluated with `eval_weight_quant_ppl.py`.",
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
    parser.add_argument("--sample-rows-per-module", type=int, default=128)
    parser.add_argument("--chunk-rows", type=int, default=64)
    parser.add_argument("--max-modules", type=int, default=0, help="0 means all Linear modules")
    parser.add_argument("--base-bits", type=int, default=4)
    parser.add_argument("--high-bits", type=int, default=8)
    parser.add_argument("--budget-avg-bits", type=float, default=4.5)
    parser.add_argument("--progress-every", type=int, default=24)
    parser.add_argument("--out-json", default="outputs/smollm2_module_output_sensitivity.json")
    parser.add_argument("--out-md", default="outputs/smollm2_module_output_sensitivity_report.md")
    parser.add_argument("--out-allocation", default="outputs/smollm2_output_sensitive_alloc_4to8_summary.json")
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
    modules = collect_linear_modules(model, args.max_modules)
    sampled_inputs, row_counts = collect_module_inputs(
        model=model,
        tokenizer=tokenizer,
        prompts=prompts,
        modules=modules,
        device=args.device,
        max_length=args.max_length,
        sample_rows_per_module=args.sample_rows_per_module,
    )
    measured = score_module_outputs(
        modules=modules,
        sampled_inputs=sampled_inputs,
        bits=args.probe_bits,
        group_size=args.group_size,
        device=args.device,
        chunk_rows=args.chunk_rows,
        progress_every=args.progress_every,
    )
    groups = rank_groups(measured)
    alloc_proxy = proxy_sensitive_4to8(groups, args.budget_avg_bits, args.base_bits, args.high_bits)
    alloc_uniform = [args.base_bits] * len(groups)
    summaries = [
        summarize_allocation(f"uniform_int{args.base_bits}", groups, alloc_uniform, args.budget_avg_bits),
        summarize_allocation("output_sensitive_4to8", groups, alloc_proxy, args.budget_avg_bits),
    ]
    result = {
        "date": time.strftime("%Y-%m-%d"),
        "model": args.model,
        "prompt_count": len(prompts),
        "max_length": args.max_length,
        "device": args.device,
        "dtype": args.dtype,
        "probe_bits": args.probe_bits,
        "group_size": args.group_size,
        "sample_rows_per_module": args.sample_rows_per_module,
        "row_count_min": min(row_counts.values()) if row_counts else 0,
        "row_count_max": max(row_counts.values()) if row_counts else 0,
        "base_bits": args.base_bits,
        "high_bits": args.high_bits,
        "budget_avg_bits": args.budget_avg_bits,
        "linear_modules": len(groups),
        "groups": groups,
        "allocations": {
            f"uniform_int{args.base_bits}": alloc_uniform,
            "output_sensitive_4to8": alloc_proxy,
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
                "row_count_min": result["row_count_min"],
                "row_count_max": result["row_count_max"],
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
