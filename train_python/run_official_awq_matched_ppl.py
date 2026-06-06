#!/usr/bin/env python3
from __future__ import annotations

"""Run a minimal matched FP16-vs-AutoAWQ PPL comparison.

This is the next step after the AutoAWQ execution smoke: the same model family
and prompt slice are evaluated in FP16 and from a local AutoAWQ artifact. It is
still a small readiness baseline, not a leaderboard-scale AWQ comparison.
"""

import argparse
import gc
import importlib.metadata
import json
import math
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_PROMPTS = [
    "Calibration robustness matters because a tiny calibration split can overfit bit allocation decisions.",
    "Mixed precision quantization should protect sensitive transformer modules while staying within a memory budget.",
    "A matched baseline must use the same prompts and tokenization when comparing FP16 and quantized models.",
    "Perplexity is not a full benchmark, but it can reveal large quality regressions after post-training quantization.",
]


def load_prompts(path: Path | None, limit: int) -> list[str]:
    if path:
        prompts = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    else:
        prompts = list(DEFAULT_PROMPTS)
    return prompts[:limit] if limit else prompts


def finite(value: Any) -> bool:
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def build_summary(
    *,
    model: str,
    awq_artifact: str,
    prompt_source: str,
    fp16_metrics: dict[str, Any],
    awq_metrics: dict[str, Any],
    elapsed_seconds: float,
    package: dict[str, str],
) -> dict[str, Any]:
    failures: list[str] = []
    fp16_ppl = float(fp16_metrics.get("ppl", float("inf")))
    awq_ppl = float(awq_metrics.get("ppl", float("inf")))
    fp16_nll = float(fp16_metrics.get("mean_nll", float("inf")))
    awq_nll = float(awq_metrics.get("mean_nll", float("inf")))
    fp16_prompts = int(fp16_metrics.get("prompt_count") or 0)
    awq_prompts = int(awq_metrics.get("prompt_count") or 0)
    fp16_tokens = int(fp16_metrics.get("tokens") or 0)
    awq_tokens = int(awq_metrics.get("tokens") or 0)

    if fp16_prompts != awq_prompts or fp16_tokens != awq_tokens:
        failures.append("prompt/token counts differ")
    if not finite(fp16_ppl) or not finite(awq_ppl):
        failures.append("non-finite ppl")
    if fp16_tokens <= 0 or awq_tokens <= 0:
        failures.append("no evaluated tokens")

    ratio = awq_ppl / fp16_ppl if fp16_ppl > 0 and finite(fp16_ppl) and finite(awq_ppl) else float("inf")
    delta_nll = awq_nll - fp16_nll if finite(fp16_nll) and finite(awq_nll) else float("inf")
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "model": model,
        "awq_artifact": awq_artifact,
        "prompt_source": prompt_source,
        "prompt_count": min(fp16_prompts, awq_prompts),
        "tokens": min(fp16_tokens, awq_tokens),
        "package": package,
        "fp16": fp16_metrics,
        "awq": awq_metrics,
        "comparison": {
            "delta_nll_awq_minus_fp16": delta_nll,
            "ppl_ratio_awq_vs_fp16": ratio,
        },
        "elapsed_seconds": elapsed_seconds,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: a minimal matched FP16-vs-AutoAWQ PPL comparison ran on the same prompt slice. "
            "Invalid claim: this is a competitive AWQ/GPTQ baseline, leaderboard result, or broad task-retention proof."
        ),
    }


def select_loss_model(model_obj: Any, *, unwrap_awq: bool) -> Any:
    if unwrap_awq and hasattr(model_obj, "model"):
        return model_obj.model
    return model_obj


def awq_device_map(device: str) -> dict[str, str]:
    if device == "cuda":
        return {"": "cuda:0"}
    return {"": device}


def eval_ppl(
    model_obj: Any,
    tokenizer: Any,
    prompts: list[str],
    device: str,
    max_length: int,
    *,
    unwrap_awq: bool = False,
) -> dict[str, Any]:
    import torch

    model = select_loss_model(model_obj, unwrap_awq=unwrap_awq)
    model.eval()
    total_nll = 0.0
    total_tokens = 0
    per_prompt: list[dict[str, Any]] = []
    with torch.inference_mode():
        for prompt in prompts:
            batch = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
            input_ids = batch["input_ids"].to(device)
            if input_ids.shape[1] < 2:
                continue
            attention_mask = batch.get("attention_mask")
            if attention_mask is not None:
                attention_mask = attention_mask.to(device)
            out = model(input_ids=input_ids, attention_mask=attention_mask, labels=input_ids)
            tokens = int(input_ids.shape[1] - 1)
            loss = float(out.loss.detach().float().item())
            total_nll += loss * tokens
            total_tokens += tokens
            per_prompt.append(
                {
                    "tokens": tokens,
                    "loss": loss,
                    "ppl": math.exp(loss) if loss < 50 else float("inf"),
                }
            )
            del out, input_ids
    mean_nll = total_nll / max(total_tokens, 1)
    return {
        "prompt_count": len(per_prompt),
        "tokens": total_tokens,
        "mean_nll": mean_nll,
        "ppl": math.exp(mean_nll) if mean_nll < 50 else float("inf"),
        "per_prompt": per_prompt,
    }


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    comparison = payload.get("comparison", {})
    lines = [
        "# Official AutoAWQ Matched PPL Summary",
        "",
        f"Date: `{payload['date']}`",
        f"Status: **{'PASS' if payload['passed'] else 'FAIL'}**",
        f"Model: `{payload['model']}`",
        f"AWQ artifact: `{payload['awq_artifact']}`",
        f"Package: `{payload['package'].get('name')} {payload['package'].get('version')}`",
        f"Prompts: `{payload['prompt_count']}`",
        f"Tokens: `{payload['tokens']}`",
        f"Elapsed seconds: `{payload['elapsed_seconds']:.3f}`",
        "",
        "## Metrics",
        "",
        "| run | mean_nll | ppl |",
        "|---|---:|---:|",
        f"| `fp16` | {payload['fp16'].get('mean_nll', 0.0):.6f} | {payload['fp16'].get('ppl', 0.0):.6f} |",
        f"| `autoawq_w4g128` | {payload['awq'].get('mean_nll', 0.0):.6f} | {payload['awq'].get('ppl', 0.0):.6f} |",
        "",
        "## Comparison",
        "",
        f"- delta NLL AWQ-FP16: `{comparison.get('delta_nll_awq_minus_fp16', float('nan')):.6f}`",
        f"- PPL ratio AWQ/FP16: `{comparison.get('ppl_ratio_awq_vs_fp16', float('nan')):.6f}`",
        "",
        "## Failures",
        "",
    ]
    lines.extend(f"- {failure}" for failure in payload.get("failures", [])) if payload.get("failures") else lines.append("- none")
    lines.extend(["", "## Claim Boundary", "", f"- {payload['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a matched FP16-vs-AutoAWQ PPL comparison.")
    parser.add_argument("--model", default="Qwen/Qwen2.5-0.5B-Instruct")
    parser.add_argument("--awq-artifact", type=Path, default=Path("outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_awq_model"))
    parser.add_argument("--prompts", type=Path)
    parser.add_argument("--limit-prompts", type=int, default=4)
    parser.add_argument("--max-length", type=int, default=96)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--out-json", type=Path, default=Path("outputs/official_awq_matched_ppl_qwen25_0p5b_summary_2026_06_07.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/OFFICIAL_AWQ_MATCHED_PPL_QWEN25_0P5B_2026_06_07.md"))
    args = parser.parse_args()

    started = time.time()
    payload: dict[str, Any]
    try:
        import torch
        from awq import AutoAWQForCausalLM
        from transformers import AutoModelForCausalLM, AutoTokenizer

        if args.device == "cuda" and not torch.cuda.is_available():
            raise RuntimeError("CUDA requested but unavailable")
        if not args.awq_artifact.exists():
            raise FileNotFoundError(f"AWQ artifact not found: {args.awq_artifact}")
        dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
        prompt_source = str(args.prompts) if args.prompts else "default"
        prompts = load_prompts(args.prompts, args.limit_prompts)
        tokenizer = AutoTokenizer.from_pretrained(str(args.awq_artifact), trust_remote_code=True)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        fp16_model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=dtype, trust_remote_code=True)
        fp16_model.to(args.device)
        fp16_metrics = eval_ppl(fp16_model, tokenizer, prompts, args.device, args.max_length)
        del fp16_model
        if args.device == "cuda":
            torch.cuda.empty_cache()
        gc.collect()

        awq_model = AutoAWQForCausalLM.from_quantized(
            str(args.awq_artifact),
            trust_remote_code=True,
            fuse_layers=False,
            use_exllama=False,
            use_exllama_v2=False,
            safetensors=True,
            device_map=awq_device_map(args.device),
            max_seq_len=args.max_length,
        )
        if hasattr(awq_model, "model"):
            awq_model.model.to(args.device)
        awq_metrics = eval_ppl(awq_model, tokenizer, prompts, args.device, args.max_length, unwrap_awq=True)
        payload = build_summary(
            model=args.model,
            awq_artifact=str(args.awq_artifact),
            prompt_source=prompt_source,
            fp16_metrics=fp16_metrics,
            awq_metrics=awq_metrics,
            elapsed_seconds=time.time() - started,
            package={"name": "autoawq", "version": importlib.metadata.version("autoawq")},
        )
        del awq_model
        if args.device == "cuda":
            torch.cuda.empty_cache()
        gc.collect()
    except Exception as exc:  # pragma: no cover - runtime diagnostic path
        payload = {
            "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "passed": False,
            "model": args.model,
            "awq_artifact": str(args.awq_artifact),
            "prompt_source": str(args.prompts) if args.prompts else "default",
            "prompt_count": 0,
            "tokens": 0,
            "package": {"name": "autoawq", "version": ""},
            "fp16": {},
            "awq": {},
            "comparison": {},
            "elapsed_seconds": time.time() - started,
            "failures": [repr(exc)],
            "error": repr(exc),
            "traceback": traceback.format_exc(),
            "claim_boundary": "Failed diagnostic run; no paper-facing baseline claim.",
        }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, payload)
    print(
        json.dumps(
            {
                "passed": payload["passed"],
                "out_json": str(args.out_json),
                "fp16_ppl": payload.get("fp16", {}).get("ppl"),
                "awq_ppl": payload.get("awq", {}).get("ppl"),
                "failures": payload.get("failures", []),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    raise SystemExit(0 if payload["passed"] else 1)


if __name__ == "__main__":
    main()
