#!/usr/bin/env python3
from __future__ import annotations

"""Run a minimal public-calibration GPTQModel baseline smoke.

This script is intentionally parallel to the AutoAWQ readiness probe, but it
uses GPTQModel instead of AWQ. The saved quantized model directory is a local
artifact and should not be committed. The JSON/Markdown summaries are the
paper-facing readiness evidence.
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


DEFAULT_CALIBRATION_TEXTS = [
    "Calibration split instability can change mixed precision bit allocation decisions.",
    "A public GPTQ baseline should report calibration data, quantization config, and matched eval slices.",
    "Short public prompt slices are readiness evidence, not leaderboard-scale quality claims.",
    "GPTQ quantization uses calibration activations to solve local weight reconstruction problems.",
]

DEFAULT_EVAL_PROMPTS = [
    "Calibration robustness matters because small splits can overfit sensitivity estimates.",
    "Mixed precision quantization must protect important modules while respecting a bit budget.",
    "A matched PPL probe compares the same tokenizer and prompt slice before and after quantization.",
    "Official PTQ baselines should remain separated from proxy fake-quant diagnostics.",
]


def load_texts(paths: list[Path]) -> list[str]:
    if not paths:
        return list(DEFAULT_CALIBRATION_TEXTS)
    texts: list[str] = []
    seen: set[str] = set()
    for path in paths:
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            text = raw_line.strip()
            if not text or text in seen:
                continue
            seen.add(text)
            texts.append(text)
    return texts


def load_eval_prompts(path: Path | None, limit: int) -> list[str]:
    prompts = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] if path else list(DEFAULT_EVAL_PROMPTS)
    return prompts[:limit] if limit else prompts


def finite(value: Any) -> bool:
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def gptq_device(device: str) -> str:
    return "cuda:0" if device == "cuda" else device


def hf_kwargs(*, local_files_only: bool) -> dict[str, bool]:
    return {"local_files_only": True} if local_files_only else {}


def artifact_summary(path: Path) -> dict[str, Any]:
    files = [item for item in path.rglob("*") if item.is_file()] if path.exists() else []
    suffix_counts: dict[str, int] = {}
    total = 0
    for item in files:
        total += item.stat().st_size
        suffix = item.suffix.lower() or "<none>"
        suffix_counts[suffix] = suffix_counts.get(suffix, 0) + 1
    return {
        "path": str(path),
        "file_count": len(files),
        "total_bytes": total,
        "suffix_counts": suffix_counts,
        "sample_files": [str(item.relative_to(path)) for item in files[:20]],
    }


def should_quantize(save_dir: Path, *, reuse_existing_artifact: bool) -> bool:
    if not reuse_existing_artifact:
        return True
    return int(artifact_summary(save_dir).get("file_count") or 0) <= 0


def select_loss_model(model_obj: Any, *, unwrap: bool = False) -> Any:
    return getattr(model_obj, "model", model_obj) if unwrap else model_obj


def move_wrapped_model_to_device(model_obj: Any, device: str) -> Any:
    target = getattr(model_obj, "model", model_obj)
    if hasattr(target, "to"):
        target.to(device)
    return model_obj


def load_saved_gptq_model(gptq_cls: Any, save_dir: Path, device: str, backend: str) -> Any:
    return gptq_cls.from_quantized(
        str(save_dir),
        device=device,
        backend=backend,
        trust_remote_code=True,
    )


def output_loss(out: Any, input_ids: Any) -> Any:
    if hasattr(out, "loss"):
        return out.loss
    if not hasattr(out, "logits"):
        raise AttributeError("model output has neither loss nor logits")

    import torch.nn.functional as F

    logits = out.logits
    shift_logits = logits[..., :-1, :].contiguous()
    shift_labels = input_ids[..., 1:].contiguous()
    return F.cross_entropy(
        shift_logits.view(-1, shift_logits.size(-1)).float(),
        shift_labels.view(-1),
        reduction="mean",
    )


def eval_ppl(
    model_obj: Any,
    tokenizer: Any,
    prompts: list[str],
    device: str,
    max_length: int,
    *,
    unwrap: bool = False,
) -> dict[str, Any]:
    import torch

    model = select_loss_model(model_obj, unwrap=unwrap)
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
            loss_tensor = output_loss(out, input_ids)
            loss = float(loss_tensor.detach().float().item())
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


def build_summary(
    *,
    model: str,
    artifact: str,
    calibration_source: list[str],
    calibration_count: int,
    quant_config: dict[str, Any],
    fp16_metrics: dict[str, Any],
    gptq_metrics: dict[str, Any],
    artifact_summary: dict[str, Any],
    package: dict[str, str],
    elapsed_seconds: float,
    artifact_reused: bool = False,
) -> dict[str, Any]:
    failures: list[str] = []
    fp16_ppl = float(fp16_metrics.get("ppl", float("inf")))
    gptq_ppl = float(gptq_metrics.get("ppl", float("inf")))
    fp16_nll = float(fp16_metrics.get("mean_nll", float("inf")))
    gptq_nll = float(gptq_metrics.get("mean_nll", float("inf")))
    fp16_prompts = int(fp16_metrics.get("prompt_count") or 0)
    gptq_prompts = int(gptq_metrics.get("prompt_count") or 0)
    fp16_tokens = int(fp16_metrics.get("tokens") or 0)
    gptq_tokens = int(gptq_metrics.get("tokens") or 0)

    if fp16_prompts != gptq_prompts or fp16_tokens != gptq_tokens:
        failures.append("prompt/token counts differ")
    if not finite(fp16_ppl) or not finite(gptq_ppl):
        failures.append("non-finite ppl")
    if fp16_tokens <= 0 or gptq_tokens <= 0:
        failures.append("no evaluated tokens")
    if int(artifact_summary.get("file_count") or 0) <= 0:
        failures.append("no saved GPTQ artifact files")
    if not calibration_source:
        failures.append("no public calibration source")
    if calibration_count <= 0:
        failures.append("no calibration texts")

    ratio = gptq_ppl / fp16_ppl if fp16_ppl > 0 and finite(fp16_ppl) and finite(gptq_ppl) else float("inf")
    delta_nll = gptq_nll - fp16_nll if finite(fp16_nll) and finite(gptq_nll) else float("inf")
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "model": model,
        "gptq_artifact": artifact,
        "calibration_source": calibration_source,
        "calibration_count": calibration_count,
        "quant_config": quant_config,
        "prompt_count": min(fp16_prompts, gptq_prompts),
        "tokens": min(fp16_tokens, gptq_tokens),
        "package": package,
        "artifact": artifact_summary,
        "artifact_reused": artifact_reused,
        "fp16": fp16_metrics,
        "gptq": gptq_metrics,
        "comparison": {
            "delta_nll_gptq_minus_fp16": delta_nll,
            "ppl_ratio_gptq_vs_fp16": ratio,
        },
        "elapsed_seconds": elapsed_seconds,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: GPTQModel ran a public-calibration W4 group-128 smoke "
            "and produced a matched tiny-slice FP16-vs-GPTQ PPL diagnostic. "
            "Invalid claim: this is a complete GPTQ/AWQ competitive baseline, "
            "SOTA PTQ result, task-retention proof, or production runtime."
        ),
    }


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    comparison = payload.get("comparison", {})
    artifact = payload.get("artifact", {})
    lines = [
        "# Official GPTQModel Public-Calibration Summary",
        "",
        f"Date: `{payload['date']}`",
        f"Status: **{'PASS' if payload['passed'] else 'FAIL'}**",
        f"Model: `{payload['model']}`",
        f"Package: `{payload['package'].get('name')} {payload['package'].get('version')}`",
        f"Quant config: `{payload['quant_config']}`",
        f"Calibration sources: `{payload['calibration_source']}`",
        f"Calibration texts: `{payload['calibration_count']}`",
        f"Artifact: `{payload['gptq_artifact']}`",
        f"Artifact reused: `{payload.get('artifact_reused', False)}`",
        f"Artifact files: `{artifact.get('file_count')}`",
        f"Artifact bytes: `{artifact.get('total_bytes')}`",
        f"Prompts: `{payload['prompt_count']}`",
        f"Tokens: `{payload['tokens']}`",
        f"Elapsed seconds: `{payload['elapsed_seconds']:.3f}`",
        "",
        "## Metrics",
        "",
        "| run | mean_nll | ppl |",
        "|---|---:|---:|",
        f"| `fp16` | {payload['fp16'].get('mean_nll', 0.0):.6f} | {payload['fp16'].get('ppl', 0.0):.6f} |",
        f"| `gptqmodel_w4g128` | {payload['gptq'].get('mean_nll', 0.0):.6f} | {payload['gptq'].get('ppl', 0.0):.6f} |",
        "",
        "## Comparison",
        "",
        f"- delta NLL GPTQ-FP16: `{comparison.get('delta_nll_gptq_minus_fp16', float('nan')):.6f}`",
        f"- PPL ratio GPTQ/FP16: `{comparison.get('ppl_ratio_gptq_vs_fp16', float('nan')):.6f}`",
        "",
        "## Failures",
        "",
    ]
    if payload.get("failures"):
        lines.extend(f"- {failure}" for failure in payload["failures"])
    else:
        lines.append("- none")
    if payload.get("error"):
        lines.extend(["", "## Error", "", "```text", str(payload["error"]), "```"])
    lines.extend(["", "## Claim Boundary", "", f"- {payload['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a public-calibration GPTQModel smoke.")
    parser.add_argument("--model", default="Qwen/Qwen2.5-0.5B-Instruct")
    parser.add_argument("--save-dir", type=Path, default=Path("outputs/official_gptqmodel_smoke_2026_06_07/qwen25_0p5b_public_calib_gptq_model"))
    parser.add_argument("--out-json", type=Path, default=Path("outputs/official_gptqmodel_public_calib_qwen25_0p5b_summary_2026_06_07.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_2026_06_07.md"))
    parser.add_argument("--calibration-prompts", type=Path, action="append", default=[])
    parser.add_argument("--prompts", type=Path)
    parser.add_argument("--limit-prompts", type=int, default=4)
    parser.add_argument("--max-calib-samples", type=int, default=8)
    parser.add_argument("--calibration-data-min-length", type=int, default=4)
    parser.add_argument("--max-length", type=int, default=96)
    parser.add_argument("--bits", type=int, default=4)
    parser.add_argument("--group-size", type=int, default=128)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--backend", default="gptq_torch")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--reuse-existing-artifact", action="store_true")
    args = parser.parse_args()

    started = time.time()
    try:
        import torch
        from gptqmodel import GPTQModel, QuantizeConfig
        from transformers import AutoModelForCausalLM, AutoTokenizer

        device = gptq_device(args.device)
        if device.startswith("cuda") and not torch.cuda.is_available():
            raise RuntimeError("CUDA requested but unavailable")
        dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
        calibration_texts = load_texts(args.calibration_prompts)[: args.max_calib_samples]
        eval_prompts = load_eval_prompts(args.prompts, args.limit_prompts)
        common_hf_kwargs = hf_kwargs(local_files_only=args.local_files_only)
        tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True, **common_hf_kwargs)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        fp16_model = AutoModelForCausalLM.from_pretrained(
            args.model,
            torch_dtype=dtype,
            trust_remote_code=True,
            **common_hf_kwargs,
        )
        fp16_model.to(device)
        fp16_metrics = eval_ppl(fp16_model, tokenizer, eval_prompts, device, args.max_length)
        del fp16_model
        if device.startswith("cuda"):
            torch.cuda.empty_cache()
        gc.collect()

        quant_config = {"bits": args.bits, "group_size": args.group_size}
        artifact_reused = not should_quantize(args.save_dir, reuse_existing_artifact=args.reuse_existing_artifact)
        if not artifact_reused:
            gptq_model = GPTQModel.load(
                args.model,
                quantize_config=QuantizeConfig(bits=args.bits, group_size=args.group_size),
                device=device,
                trust_remote_code=True,
            )
            gptq_model.quantize(
                calibration=calibration_texts,
                tokenizer=tokenizer,
                batch_size=1,
                calibration_data_min_length=args.calibration_data_min_length,
            )
            args.save_dir.mkdir(parents=True, exist_ok=True)
            gptq_model.save(str(args.save_dir))
            tokenizer.save_pretrained(str(args.save_dir))
            del gptq_model
            if device.startswith("cuda"):
                torch.cuda.empty_cache()
            gc.collect()
        art = artifact_summary(args.save_dir)

        reloaded_gptq_model = load_saved_gptq_model(GPTQModel, args.save_dir, device, args.backend)
        gptq_metrics = eval_ppl(reloaded_gptq_model, tokenizer, eval_prompts, device, args.max_length)
        payload = build_summary(
            model=args.model,
            artifact=str(args.save_dir),
            calibration_source=[str(path) for path in args.calibration_prompts],
            calibration_count=len(calibration_texts),
            quant_config=quant_config,
            fp16_metrics=fp16_metrics,
            gptq_metrics=gptq_metrics,
            artifact_summary=art,
            package={"name": "gptqmodel", "version": importlib.metadata.version("gptqmodel")},
            elapsed_seconds=time.time() - started,
            artifact_reused=artifact_reused,
        )
        del reloaded_gptq_model
        if device.startswith("cuda"):
            torch.cuda.empty_cache()
        gc.collect()
    except Exception as exc:  # pragma: no cover - runtime diagnostic path
        payload = {
            "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "passed": False,
            "model": args.model,
            "gptq_artifact": str(args.save_dir),
            "calibration_source": [str(path) for path in args.calibration_prompts],
            "calibration_count": 0,
            "quant_config": {"bits": args.bits, "group_size": args.group_size},
            "prompt_count": 0,
            "tokens": 0,
            "package": {"name": "gptqmodel", "version": ""},
            "artifact": artifact_summary(args.save_dir),
            "fp16": {},
            "gptq": {},
            "comparison": {},
            "elapsed_seconds": time.time() - started,
            "failures": [repr(exc)],
            "error": repr(exc),
            "traceback": traceback.format_exc(),
            "claim_boundary": "Failed diagnostic run; no paper-facing GPTQ baseline claim.",
        }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, payload)
    print(json.dumps({"passed": payload["passed"], "out_json": str(args.out_json), "failures": payload.get("failures", [])}, indent=2))
    raise SystemExit(0 if payload["passed"] else 1)


if __name__ == "__main__":
    main()
