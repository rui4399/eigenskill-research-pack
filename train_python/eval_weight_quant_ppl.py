#!/usr/bin/env python3
from __future__ import annotations

"""Evaluate short-prompt perplexity after simple fake weight quantization.

This is a first quality-signal scaffold, not a production quantizer. It applies
per-output-channel symmetric fake quantization to Linear weights, dequantizes
back to floating point, and evaluates next-token loss on a small prompt set.

Use it to compare:
  - fp16
  - uniform INT3/INT4
  - an allocation from rate_distortion_allocator.py

The script intentionally avoids GPTQ/AWQ/bitsandbytes dependencies.
"""

import argparse
import copy
import json
import math
import gc
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


def load_allocation(path: str, method: str) -> tuple[dict[str, int], dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    groups = data["groups"]
    if groups and "module" not in groups[0] and data.get("stats_json"):
        stats_ref = str(data["stats_json"]).replace("\\", "/")
        stats_path = Path(stats_ref)
        if not stats_path.is_absolute():
            stats_path = Path(path).parent.parent / stats_path
            if not stats_path.exists():
                stats_path = Path(stats_ref)
        stats_data = json.loads(stats_path.read_text(encoding="utf-8"))
        stats_groups = stats_data.get("groups", [])
        if len(stats_groups) == len(groups):
            groups = [{**group, "module": stats_group.get("module", "")} for group, stats_group in zip(groups, stats_groups)]
    alloc = data["allocations"][method]
    module_bits = {}
    for item, bits in zip(groups, alloc):
        module = item.get("module")
        if module:
            module_bits[module] = int(bits)
    return module_bits, data


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


def apply_fake_quant(model: torch.nn.Module, mode: str, module_bits: dict[str, int] | None = None, group_size: int = 0) -> dict:
    bit_hist: dict[str, int] = {}
    touched = 0
    with torch.no_grad():
        for name, module in model.named_modules():
            if not isinstance(module, torch.nn.Linear):
                continue
            if mode == "fp16":
                bits = 16
            elif mode.startswith("uniform_int"):
                bits = int(mode.replace("uniform_int", ""))
            elif mode == "allocation":
                if module_bits is None or name not in module_bits:
                    continue
                bits = int(module_bits[name])
            else:
                raise ValueError(f"unknown quant mode: {mode}")
            if bits < 16:
                module.weight.data.copy_(quantize_weight(module.weight.data, bits, group_size=group_size))
            bit_hist[str(bits)] = bit_hist.get(str(bits), 0) + 1
            touched += 1
    return {"linear_modules_touched": touched, "bit_hist": bit_hist, "group_size": group_size}


def capture_linear_weights(model: torch.nn.Module) -> dict[str, torch.Tensor]:
    weights = {}
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            weights[name] = module.weight.detach().cpu().clone()
    return weights


def restore_linear_weights(model: torch.nn.Module, weights: dict[str, torch.Tensor]) -> None:
    with torch.no_grad():
        for name, module in model.named_modules():
            if not isinstance(module, torch.nn.Linear):
                continue
            original = weights.get(name)
            if original is None:
                continue
            module.weight.data.copy_(original.to(device=module.weight.device, dtype=module.weight.dtype))


def eval_ppl(model: torch.nn.Module, tokenizer, prompts: list[str], device: str, max_length: int) -> dict:
    total_nll = 0.0
    total_tokens = 0
    per_prompt = []
    with torch.no_grad():
        for prompt in prompts:
            batch = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
            input_ids = batch["input_ids"].to(device)
            if input_ids.shape[1] < 2:
                continue
            out = model(input_ids=input_ids, labels=input_ids)
            tokens = input_ids.shape[1] - 1
            nll = float(out.loss.item()) * tokens
            total_nll += nll
            total_tokens += tokens
            per_prompt.append({"tokens": tokens, "loss": float(out.loss.item()), "ppl": math.exp(float(out.loss.item()))})
    mean_nll = total_nll / max(total_tokens, 1)
    return {
        "prompt_count": len(per_prompt),
        "tokens": total_tokens,
        "mean_nll": mean_nll,
        "ppl": math.exp(mean_nll) if mean_nll < 50 else float("inf"),
        "per_prompt": per_prompt,
    }


def run_config(args, tokenizer, config: dict, prompts: list[str]) -> dict:
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=dtype)
    model.eval()
    model.to(args.device)

    module_bits = None
    allocation_meta = None
    if config["mode"] == "allocation":
        module_bits, allocation_meta = load_allocation(config["allocation"], config["method"])
    quant_meta = apply_fake_quant(model, config["mode"], module_bits, group_size=args.group_size)
    metrics = eval_ppl(model, tokenizer, prompts, args.device, args.max_length)
    result = {
        "name": config["name"],
        "mode": config["mode"],
        "allocation": config.get("allocation", ""),
        "method": config.get("method", ""),
        "quant_meta": quant_meta,
        "metrics": metrics,
    }
    if allocation_meta:
        result["allocation_summary"] = next(
            (item for item in allocation_meta["summaries"] if item["name"] == config["method"]),
            None,
        )
    del model
    if args.device == "cuda":
        torch.cuda.empty_cache()
    gc.collect()
    return result


def run_config_reuse(
    args,
    model: torch.nn.Module,
    base_linear_weights: dict[str, torch.Tensor],
    config: dict,
    prompts: list[str],
) -> dict:
    restore_linear_weights(model, base_linear_weights)
    module_bits = None
    allocation_meta = None
    if config["mode"] == "allocation":
        module_bits, allocation_meta = load_allocation(config["allocation"], config["method"])
    quant_meta = apply_fake_quant(model, config["mode"], module_bits, group_size=args.group_size)
    metrics = eval_ppl(model, args._tokenizer, prompts, args.device, args.max_length)
    result = {
        "name": config["name"],
        "mode": config["mode"],
        "allocation": config.get("allocation", ""),
        "method": config.get("method", ""),
        "quant_meta": quant_meta,
        "metrics": metrics,
    }
    if allocation_meta:
        result["allocation_summary"] = next(
            (item for item in allocation_meta["summaries"] if item["name"] == config["method"]),
            None,
        )
    return result


def parse_configs(args) -> list[dict]:
    configs = [
        {"name": "fp16", "mode": "fp16"},
        {"name": "uniform_int4", "mode": "uniform_int4"},
        {"name": "uniform_int3", "mode": "uniform_int3"},
    ]
    if args.allocation:
        configs.append(
            {
                "name": f"allocation_{args.allocation_method}",
                "mode": "allocation",
                "allocation": args.allocation,
                "method": args.allocation_method,
            }
        )
    if args.config_json:
        configs = json.loads(Path(args.config_json).read_text(encoding="utf-8"))
    return configs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="HuggingFaceTB/SmolLM2-360M-Instruct")
    parser.add_argument("--prompts", default="")
    parser.add_argument("--limit-prompts", type=int, default=8)
    parser.add_argument("--max-length", type=int, default=160)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--allocation", default="")
    parser.add_argument("--allocation-method", default="rate_distortion")
    parser.add_argument("--group-size", type=int, default=0, help="0 means one scale per output row")
    parser.add_argument("--config-json", default="")
    parser.add_argument(
        "--reuse-model",
        action="store_true",
        help="Load the model once and restore cached Linear weights between configs.",
    )
    parser.add_argument("--out", default="outputs/smollm2_fake_quant_ppl_summary.json")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("This script requires torch and transformers. Run it in the WSL GPU Python environment.")

    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    prompts = load_prompts(args.prompts, args.limit_prompts)
    configs = parse_configs(args)
    if args.reuse_model:
        dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
        model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=dtype)
        model.eval()
        model.to(args.device)
        args._tokenizer = tokenizer
        base_linear_weights = capture_linear_weights(model)
        results = [run_config_reuse(args, model, base_linear_weights, config, prompts) for config in configs]
        del model
        del base_linear_weights
        del args._tokenizer
        if args.device == "cuda":
            torch.cuda.empty_cache()
        gc.collect()
    else:
        results = [run_config(args, tokenizer, config, prompts) for config in configs]
    baseline = next((x for x in results if x["name"] == "fp16"), None)
    if baseline:
        base_nll = baseline["metrics"]["mean_nll"]
        for result in results:
            result["delta_nll_vs_fp16"] = result["metrics"]["mean_nll"] - base_nll
            result["ppl_ratio_vs_fp16"] = result["metrics"]["ppl"] / max(baseline["metrics"]["ppl"], 1.0e-12)

    output = {
        "model": args.model,
        "prompt_count": len(prompts),
        "max_length": args.max_length,
        "device": args.device,
        "dtype": args.dtype,
        "results": results,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"out": str(out), "results": [
        {
            "name": r["name"],
            "ppl": r["metrics"]["ppl"],
            "delta_nll_vs_fp16": r.get("delta_nll_vs_fp16", 0.0),
            "bit_hist": r["quant_meta"]["bit_hist"],
        }
        for r in results
    ]}, indent=2))


if __name__ == "__main__":
    main()
