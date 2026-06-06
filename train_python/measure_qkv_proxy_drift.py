#!/usr/bin/env python3
from __future__ import annotations

"""Measure teacher-forced hidden/logit/KV drift for fused ESMP QKV replacement.

Unlike prompt-suite exact matching, this script does not depend on generated
text branching.  It runs the dense model and the fused-QKV replacement on the
same prompt tokens, then compares final hidden states, last-token logits, and
selected-layer KV cache tensors.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median
from typing import Any

try:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
except ModuleNotFoundError:  # pragma: no cover
    torch = None
    AutoModelForCausalLM = None
    AutoTokenizer = None

from benchmark_esmp_fused_selected_rows import parse_suffixes
from eval_esmp_module_reconstruction import DEFAULT_MODEL, DEFAULT_PACKAGE_SUMMARY, load_package_modules, repo_root, resolve_path
from measure_esmp_fused_qkv_generation import install_fused_qkv, summarize_ms
from measure_esmp_generation_latency import parse_layers


DEFAULT_PROMPTS = [
    "Explain calibration-set sensitivity in mixed-bit LLM quantization using exactly two sentences.",
    "Produce minified JSON with keys policy, evidence, and caveat for a precision-routing experiment.",
    "How many bytes store 4096 four-bit signed weights when packed densely? Give only the number and unit.",
]


def load_prompts(path: str, limit: int = 0) -> list[str]:
    if not path:
        prompts = list(DEFAULT_PROMPTS)
    else:
        text = Path(path).read_text(encoding="utf-8")
        prompts = [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    if limit > 0:
        prompts = prompts[:limit]
    if not prompts:
        raise SystemExit("no prompts found")
    return prompts


def tensor_error(name: str, reference: torch.Tensor, approximation: torch.Tensor, eps: float = 1.0e-12) -> dict[str, Any]:
    ref = reference.detach().float().cpu()
    approx = approximation.detach().float().cpu()
    diff = ref - approx
    ref_l2 = torch.linalg.vector_norm(ref).item()
    diff_l2 = torch.linalg.vector_norm(diff).item()
    ref_mse = torch.mean(ref * ref).item()
    diff_mse = torch.mean(diff * diff).item()
    return {
        "name": name,
        "shape": list(ref.shape),
        "rel_l2": float(diff_l2 / max(ref_l2, eps)),
        "normalized_mse": float(diff_mse / max(ref_mse, eps)),
        "reference_l2": float(ref_l2),
        "diff_l2": float(diff_l2),
    }


def normalize_past_key_values(past_key_values: Any) -> list[tuple[torch.Tensor, torch.Tensor]]:
    if past_key_values is None:
        return []
    if hasattr(past_key_values, "to_legacy_cache"):
        past_key_values = past_key_values.to_legacy_cache()
    elif hasattr(past_key_values, "key_cache") and hasattr(past_key_values, "value_cache"):
        return list(zip(past_key_values.key_cache, past_key_values.value_cache))

    pairs: list[tuple[torch.Tensor, torch.Tensor]] = []
    for item in past_key_values:
        if isinstance(item, (tuple, list)) and len(item) >= 2:
            key, value = item[0], item[1]
            if torch.is_tensor(key) and torch.is_tensor(value):
                pairs.append((key, value))
    return pairs


def aggregate_metric(rows: list[dict[str, Any]], key: str) -> dict[str, float]:
    values = [float(row[key]) for row in rows]
    if not values:
        return {"mean": 0.0, "median": 0.0, "max": 0.0}
    return {"mean": float(mean(values)), "median": float(median(values)), "max": float(max(values))}


def forward_probe(
    model: Any,
    tokenizer: Any,
    prompt: str,
    device: torch.device,
    max_length: int,
) -> dict[str, Any]:
    encoded = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
    encoded = {key: value.to(device) for key, value in encoded.items()}
    with torch.inference_mode():
        out = model(
            **encoded,
            use_cache=True,
            output_hidden_states=True,
            return_dict=True,
        )
    hidden_states = out.hidden_states
    final_hidden = hidden_states[-1].detach().cpu()
    last_logits = out.logits[:, -1, :].detach().cpu()
    kv_pairs = [(k.detach().cpu(), v.detach().cpu()) for k, v in normalize_past_key_values(out.past_key_values)]
    return {
        "input_length": int(encoded["input_ids"].shape[-1]),
        "final_hidden": final_hidden,
        "last_logits": last_logits,
        "kv_pairs": kv_pairs,
    }


def compare_probe(
    prompt_id: int,
    prompt: str,
    baseline: dict[str, Any],
    fused: dict[str, Any],
    layers: list[int],
) -> dict[str, Any]:
    final_hidden = tensor_error("final_hidden", baseline["final_hidden"], fused["final_hidden"])
    last_logits = tensor_error("last_logits", baseline["last_logits"], fused["last_logits"])
    kv_errors: list[dict[str, Any]] = []
    baseline_pairs = baseline["kv_pairs"]
    fused_pairs = fused["kv_pairs"]
    for layer in layers:
        if layer >= len(baseline_pairs) or layer >= len(fused_pairs):
            continue
        b_key, b_value = baseline_pairs[layer]
        f_key, f_value = fused_pairs[layer]
        kv_errors.append({"layer": layer, "kind": "key", **tensor_error(f"layer{layer}_key", b_key, f_key)})
        kv_errors.append({"layer": layer, "kind": "value", **tensor_error(f"layer{layer}_value", b_value, f_value)})
    kv_rel = [float(item["rel_l2"]) for item in kv_errors]
    kv_nmse = [float(item["normalized_mse"]) for item in kv_errors]
    return {
        "id": int(prompt_id),
        "prompt": prompt,
        "input_length": int(baseline["input_length"]),
        "final_hidden_rel_l2": float(final_hidden["rel_l2"]),
        "final_hidden_normalized_mse": float(final_hidden["normalized_mse"]),
        "last_logits_rel_l2": float(last_logits["rel_l2"]),
        "last_logits_normalized_mse": float(last_logits["normalized_mse"]),
        "kv_mean_rel_l2": float(mean(kv_rel)) if kv_rel else 0.0,
        "kv_max_rel_l2": float(max(kv_rel)) if kv_rel else 0.0,
        "kv_mean_normalized_mse": float(mean(kv_nmse)) if kv_nmse else 0.0,
        "kv_errors": kv_errors,
    }


def write_report(path: Path, result: dict[str, Any]) -> None:
    agg = result["aggregate"]
    lines = [
        "# QKV Replacement Proxy Drift",
        "",
        f"Date: `{result['date']}`",
        f"Candidate: `{result['candidate_label']}`",
        f"Model: `{result['model']}`",
        f"Layers: `{result['layers']}`",
        f"Prompt file: `{result['prompt_file'] or 'default'}`",
        f"Prompts: `{agg['prompts']}`",
        "",
        "## Aggregate",
        "",
        "| metric | mean | median | max |",
        "|---|---:|---:|---:|",
        f"| final hidden rel-L2 | {agg['final_hidden_rel_l2']['mean']:.6f} | {agg['final_hidden_rel_l2']['median']:.6f} | {agg['final_hidden_rel_l2']['max']:.6f} |",
        f"| last logits rel-L2 | {agg['last_logits_rel_l2']['mean']:.6f} | {agg['last_logits_rel_l2']['median']:.6f} | {agg['last_logits_rel_l2']['max']:.6f} |",
        f"| KV mean rel-L2 | {agg['kv_mean_rel_l2']['mean']:.6f} | {agg['kv_mean_rel_l2']['median']:.6f} | {agg['kv_mean_rel_l2']['max']:.6f} |",
        f"| KV max rel-L2 | {agg['kv_max_rel_l2']['mean']:.6f} | {agg['kv_max_rel_l2']['median']:.6f} | {agg['kv_max_rel_l2']['max']:.6f} |",
        "",
        "## Per Prompt",
        "",
        "| id | input len | final hidden rel-L2 | logits rel-L2 | KV mean rel-L2 | KV max rel-L2 | prompt |",
        "|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in result["rows"]:
        prompt = " ".join(row["prompt"].split()).replace("|", "\\|")[:96]
        lines.append(
            f"| {row['id']} | {row['input_length']} | {row['final_hidden_rel_l2']:.6f} | "
            f"{row['last_logits_rel_l2']:.6f} | {row['kv_mean_rel_l2']:.6f} | "
            f"{row['kv_max_rel_l2']:.6f} | `{prompt}` |"
        )
    lines.extend(
        [
            "",
            "## Guardrail",
            "",
            "This is a teacher-forced continuous proxy. It supports ranking and diagnostics, but it does not prove generation quality by itself.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure hidden/logit/KV drift for fused QKV replacement.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--candidate-label", default="candidate")
    parser.add_argument("--package-summary", default=DEFAULT_PACKAGE_SUMMARY)
    parser.add_argument("--prompt-file", default="")
    parser.add_argument("--limit-prompts", type=int, default=0)
    parser.add_argument("--max-length", type=int, default=96)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--layers", default="1,7,20")
    parser.add_argument("--suffixes", default="q_proj,k_proj,v_proj")
    parser.add_argument("--dense-roles", default="")
    parser.add_argument("--block-m", type=int, default=32)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=64)
    parser.add_argument("--sync-mode", choices=["per_call", "end"], default="end")
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("missing dependencies: install torch and transformers")
    if args.device.startswith("cuda") and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")

    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
    prompts = load_prompts(args.prompt_file, args.limit_prompts)
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    device = torch.device(args.device)
    layers = sorted(parse_layers(args.layers) or set())
    suffixes = parse_suffixes(args.suffixes)
    dense_roles = set(parse_suffixes(args.dense_roles)) if args.dense_roles else set()

    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=args.local_files_only, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )
    model.eval()
    model.to(device)

    baseline_probes = [forward_probe(model, tokenizer, prompt, device, args.max_length) for prompt in prompts]
    fused_runtimes = install_fused_qkv(
        model=model,
        package_modules=load_package_modules(package_summary),
        layers=layers,
        suffixes=suffixes,
        dense_roles=dense_roles,
        device=device,
        dtype=dtype,
        block_m=args.block_m,
        block_n=args.block_n,
        block_k=args.block_k,
        sync_mode=args.sync_mode,
    )
    for runtime in fused_runtimes:
        runtime.clear_stats()
    if args.device.startswith("cuda"):
        torch.cuda.reset_peak_memory_stats()

    rows: list[dict[str, Any]] = []
    for idx, prompt in enumerate(prompts):
        fused_probe = forward_probe(model, tokenizer, prompt, device, args.max_length)
        rows.append(compare_probe(idx, prompt, baseline_probes[idx], fused_probe, layers))
    for runtime in fused_runtimes:
        runtime.finalize_pending()

    all_ms = [value for runtime in fused_runtimes for value in runtime.stats.cuda_event_ms]
    result = {
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "candidate_label": args.candidate_label,
        "model": args.model,
        "dtype": args.dtype,
        "device": str(device),
        "package_summary": str(package_summary),
        "prompt_file": args.prompt_file,
        "layers": layers,
        "suffixes": suffixes,
        "dense_roles": sorted(dense_roles),
        "max_length": int(args.max_length),
        "replacement_compression_vs_fp32": float(
            sum(runtime.raw_fp32_bytes for runtime in fused_runtimes)
            / max(sum(runtime.package_bytes for runtime in fused_runtimes), 1)
        ),
        "replacement_cuda_event_ms": summarize_ms(all_ms),
        "peak_gpu_memory_mib": float(torch.cuda.max_memory_allocated() / (1024 * 1024)) if args.device.startswith("cuda") else 0.0,
        "aggregate": {
            "prompts": len(rows),
            "final_hidden_rel_l2": aggregate_metric(rows, "final_hidden_rel_l2"),
            "last_logits_rel_l2": aggregate_metric(rows, "last_logits_rel_l2"),
            "kv_mean_rel_l2": aggregate_metric(rows, "kv_mean_rel_l2"),
            "kv_max_rel_l2": aggregate_metric(rows, "kv_max_rel_l2"),
            "final_hidden_normalized_mse": aggregate_metric(rows, "final_hidden_normalized_mse"),
            "last_logits_normalized_mse": aggregate_metric(rows, "last_logits_normalized_mse"),
            "kv_mean_normalized_mse": aggregate_metric(rows, "kv_mean_normalized_mse"),
        },
        "rows": rows,
    }
    out_json = resolve_path(args.out_json, root)
    out_md = resolve_path(args.out_md, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_report(out_md, result)
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "aggregate": result["aggregate"]}, indent=2, ensure_ascii=False))

    del model
    if args.device.startswith("cuda"):
        torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
