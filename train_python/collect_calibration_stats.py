#!/usr/bin/env python3
"""Collect lightweight activation statistics for EigenSkill-Q allocation.

This script is intentionally conservative: it does not quantize the model and
does not need GPTQ/AWQ/bitsandbytes. It loads a small causal LM, records inputs
to Linear modules on a small prompt set, and emits allocator-compatible group
statistics:

    GroupStat(layer, group, sensitivity, variance, cost, outlier)

The output can be passed to:

    python train_python/rate_distortion_allocator.py --stats-json <stats.json>
"""

import argparse
import json
import math
from collections import OrderedDict
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


DEFAULT_PROMPTS = [
    "Explain why low-bit quantization can fail on outlier channels.",
    "Compute the safest bit width when sensitivity is high and memory is tight.",
    "Write a compact JSON policy for KV cache compression under long context.",
    "A model layer has high activation variance; decide whether rotation helps.",
    "Summarize rate-distortion guided mixed precision for small language models.",
    "Reason step by step about preserving math accuracy after quantization.",
    "Classify whether a residual low-rank patch is needed for a sensitive layer.",
    "Describe how Hessian or Fisher scores can guide bit allocation.",
]


class RunningStat:
    def __init__(self, layer: int, name: str, param_count: int):
        self.layer = layer
        self.name = name
        self.param_count = param_count
        self.count = 0
        self.sum_abs = 0.0
        self.sum_sq = 0.0
        self.max_abs = 0.0

    def update(self, tensor: torch.Tensor) -> None:
        x = tensor.detach().float()
        if x.numel() == 0:
            return
        abs_x = x.abs()
        self.count += x.numel()
        self.sum_abs += float(abs_x.sum().item())
        self.sum_sq += float((x * x).sum().item())
        self.max_abs = max(self.max_abs, float(abs_x.max().item()))

    def to_group(self, group: int) -> dict:
        mean_abs = self.sum_abs / max(self.count, 1)
        variance = self.sum_sq / max(self.count, 1)
        rms = math.sqrt(max(variance, 1.0e-12))
        outlier = self.max_abs / max(rms, 1.0e-12)
        # This is a proxy, not a Hessian score. It gives the allocator a stable
        # first signal until real Fisher/Hessian statistics are added.
        sensitivity = mean_abs * math.log1p(self.param_count) * (1.0 + 0.04 * outlier)
        cost = max(self.param_count / 1_000_000.0, 1.0e-4)
        return {
            "layer": self.layer,
            "group": group,
            "module": self.name,
            "sensitivity": round(sensitivity, 8),
            "variance": round(variance, 8),
            "cost": round(cost, 8),
            "outlier": round(outlier, 8),
            "count": self.count,
            "param_count": self.param_count,
            "mean_abs": round(mean_abs, 8),
            "max_abs": round(self.max_abs, 8),
        }


def load_prompts(path: str, limit: int) -> list[str]:
    if path:
        prompts = [line.strip() for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]
    else:
        prompts = list(DEFAULT_PROMPTS)
    return prompts[:limit] if limit else prompts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="HuggingFaceTB/SmolLM2-360M-Instruct")
    parser.add_argument("--prompts", default="")
    parser.add_argument("--limit-prompts", type=int, default=8)
    parser.add_argument("--max-length", type=int, default=160)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["auto", "float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--max-modules", type=int, default=0, help="0 means all Linear modules")
    parser.add_argument("--out", default="outputs/calibration_stats_smollm2_360m.json")
    args = parser.parse_args()

    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")

    dtype = {
        "auto": "auto",
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
        "float32": torch.float32,
    }[args.dtype]

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=dtype)
    model.eval()
    model.to(args.device)

    stats: OrderedDict[str, RunningStat] = OrderedDict()
    handles = []
    layer_index = 0
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            param_count = sum(p.numel() for p in module.parameters(recurse=False))
            stats[name] = RunningStat(layer=layer_index, name=name, param_count=param_count)
            layer_index += 1
            if args.max_modules and layer_index >= args.max_modules:
                break

    def make_hook(key: str):
        def hook(_module, inputs, _output):
            if inputs:
                stats[key].update(inputs[0])
        return hook

    for key, module in model.named_modules():
        if key in stats:
            handles.append(module.register_forward_hook(make_hook(key)))

    prompts = load_prompts(args.prompts, args.limit_prompts)
    with torch.no_grad():
        for prompt in prompts:
            batch = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=args.max_length).to(args.device)
            model(**batch)

    for handle in handles:
        handle.remove()

    groups = [value.to_group(group=i) for i, value in enumerate(stats.values()) if value.count > 0]
    result = {
        "model": args.model,
        "prompt_count": len(prompts),
        "max_length": args.max_length,
        "device": args.device,
        "dtype": args.dtype,
        "linear_modules": len(groups),
        "groups": groups,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["model", "prompt_count", "linear_modules"]} | {"out": str(out)}, indent=2))


if __name__ == "__main__":
    main()
