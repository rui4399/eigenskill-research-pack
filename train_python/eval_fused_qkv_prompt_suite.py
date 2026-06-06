#!/usr/bin/env python3
from __future__ import annotations

"""Compare baseline vs fused ESMP QKV replacement on a small prompt suite."""

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
from eval_esmp_module_reconstruction import DEFAULT_MODEL, DEFAULT_PACKAGE_SUMMARY, load_package_modules, resolve_path, repo_root
from measure_esmp_fused_qkv_generation import install_fused_qkv, summarize_ms
from measure_esmp_generation_latency import run_generation, parse_layers


DEFAULT_PROMPTS = [
    "Explain mixed-precision quantization in one concise paragraph.",
    "Give a short JSON object with fields task, risk, and next_step for model quantization.",
    "Solve briefly: if an INT4 row stores 1024 weights, how many packed bytes are needed?",
    "Write a compact C++ function signature for a mixed INT4/INT8 GEMV kernel.",
    "List two reasons calibration data can make quantization unstable.",
    "In one sentence, explain why replacing QKV projections can change generated text.",
]


def load_prompts(path: str) -> list[str]:
    if not path:
        return DEFAULT_PROMPTS
    text = Path(path).read_text(encoding="utf-8")
    prompts = [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    if not prompts:
        raise SystemExit(f"no prompts found in {path}")
    return prompts


def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        cur = [i]
        for j, cb in enumerate(b, start=1):
            cur.append(min(prev[j] + 1, cur[-1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def common_prefix_len(a: str, b: str) -> int:
    limit = min(len(a), len(b))
    for idx in range(limit):
        if a[idx] != b[idx]:
            return idx
    return limit


def compare_text(baseline: str, fused: str) -> dict[str, Any]:
    dist = levenshtein(baseline, fused)
    denom = max(len(baseline), len(fused), 1)
    prefix = common_prefix_len(baseline, fused)
    return {
        "exact_match": baseline == fused,
        "baseline_chars": len(baseline),
        "fused_chars": len(fused),
        "common_prefix_chars": prefix,
        "common_prefix_ratio": float(prefix / max(len(baseline), 1)),
        "char_edit_distance": dist,
        "char_edit_similarity": float(1.0 - dist / denom),
    }


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    exact = [row["comparison"]["exact_match"] for row in rows]
    similarities = [float(row["comparison"]["char_edit_similarity"]) for row in rows]
    prefix_ratios = [float(row["comparison"]["common_prefix_ratio"]) for row in rows]
    baseline_tps = [float(row["baseline"]["tokens_per_second"] or 0.0) for row in rows]
    fused_tps = [float(row["fused"]["tokens_per_second"] or 0.0) for row in rows]
    baseline_ttft = [float(row["baseline"]["ttft_seconds"] or 0.0) for row in rows]
    fused_ttft = [float(row["fused"]["ttft_seconds"] or 0.0) for row in rows]
    return {
        "prompts": len(rows),
        "exact_matches": int(sum(1 for value in exact if value)),
        "exact_match_rate": float(sum(1 for value in exact if value) / max(len(rows), 1)),
        "mean_char_edit_similarity": float(mean(similarities)) if similarities else 0.0,
        "median_char_edit_similarity": float(median(similarities)) if similarities else 0.0,
        "mean_common_prefix_ratio": float(mean(prefix_ratios)) if prefix_ratios else 0.0,
        "median_common_prefix_ratio": float(median(prefix_ratios)) if prefix_ratios else 0.0,
        "mean_baseline_tokens_per_second": float(mean(baseline_tps)) if baseline_tps else 0.0,
        "mean_fused_tokens_per_second": float(mean(fused_tps)) if fused_tps else 0.0,
        "mean_speedup_fused_vs_baseline": float(mean(fused_tps) / max(mean(baseline_tps), 1.0e-12)) if baseline_tps else 0.0,
        "median_baseline_ttft_seconds": float(median(baseline_ttft)) if baseline_ttft else 0.0,
        "median_fused_ttft_seconds": float(median(fused_ttft)) if fused_ttft else 0.0,
    }


def write_report(path: Path, result: dict[str, Any]) -> None:
    agg = result["aggregate"]
    lines = [
        "# Fused ESMP QKV Prompt-Suite Comparison",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Layers: `{result['layers']}`",
        f"Dense roles: `{result['dense_roles']}`",
        f"Chat template: `{result.get('chat_template', False)}`",
        f"Max new tokens: `{result['max_new_tokens']}`",
        f"Sync mode: `{result['sync_mode']}`",
        f"Prompts: `{agg['prompts']}`",
        "",
        "## Aggregate",
        "",
        "| metric | value |",
        "|---|---:|",
        f"| exact matches | {agg['exact_matches']} / {agg['prompts']} |",
        f"| exact match rate | {agg['exact_match_rate']:.4f} |",
        f"| mean char edit similarity | {agg['mean_char_edit_similarity']:.4f} |",
        f"| median char edit similarity | {agg['median_char_edit_similarity']:.4f} |",
        f"| mean common prefix ratio | {agg['mean_common_prefix_ratio']:.4f} |",
        f"| mean baseline tokens/s | {agg['mean_baseline_tokens_per_second']:.4f} |",
        f"| mean fused tokens/s | {agg['mean_fused_tokens_per_second']:.4f} |",
        f"| mean fused/baseline speed | {agg['mean_speedup_fused_vs_baseline']:.4f}x |",
        f"| median baseline TTFT s | {agg['median_baseline_ttft_seconds']:.6f} |",
        f"| median fused TTFT s | {agg['median_fused_ttft_seconds']:.6f} |",
        "",
        "## Replacement Runtime",
        "",
        f"- Replacement compression vs FP32: `{result['replacement_compression_vs_fp32']:.4f}x`",
        f"- Dense role calls: `{result['replacement_dense_role_calls']}`",
        f"- Wrapper calls / fused compute calls: `{result['replacement_wrapper_calls']} / {result['replacement_fused_compute_calls']}`",
        f"- Cache hits / misses: `{result['replacement_cache_hits']} / {result['replacement_cache_misses']}`",
        f"- Fused CUDA event sum: `{result['replacement_cuda_event_ms']['sum']:.4f} ms`",
        f"- Peak CUDA memory: `{result['peak_gpu_memory_mib']:.2f} MiB`",
        "",
        "## Per-Prompt",
        "",
        "| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |",
        "|---:|---|---:|---:|---:|---:|---|---|",
    ]
    for row in result["rows"]:
        base_text = row["baseline"]["generated_text"].replace("|", "\\|").replace("\n", " ")[:100]
        fused_text = row["fused"]["generated_text"].replace("|", "\\|").replace("\n", " ")[:100]
        lines.append(
            f"| {row['id']} | {row['comparison']['exact_match']} | "
            f"{row['comparison']['char_edit_similarity']:.4f} | "
            f"{row['comparison']['common_prefix_ratio']:.4f} | "
            f"{float(row['baseline']['tokens_per_second'] or 0.0):.4f} | "
            f"{float(row['fused']['tokens_per_second'] or 0.0):.4f} | "
            f"`{base_text}` | `{fused_text}` |"
        )
    lines.extend(
        [
            "",
            "## Guardrail",
            "",
            "This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare baseline and fused QKV replacement on prompt suite.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--package-summary", default=DEFAULT_PACKAGE_SUMMARY)
    parser.add_argument("--prompt-file", default="")
    parser.add_argument("--max-new-tokens", type=int, default=32)
    parser.add_argument("--warmup-runs", type=int, default=1)
    parser.add_argument("--chat-template", action="store_true", help="Format prompts as single user chat messages.")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--layers", default="0")
    parser.add_argument("--suffixes", default="q_proj,k_proj,v_proj")
    parser.add_argument("--dense-roles", default="", help="Comma-separated suffixes or exact module names to keep as dense guards.")
    parser.add_argument("--block-m", type=int, default=32)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=64)
    parser.add_argument("--sync-mode", choices=["per_call", "end"], default="end")
    parser.add_argument("--out-json", default="outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite.json")
    parser.add_argument("--out-md", default="outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE.md")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None or AutoTokenizer is None:
        raise SystemExit("missing dependencies: install torch and transformers")
    if args.device.startswith("cuda") and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")

    prompts = load_prompts(args.prompt_file)
    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
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

    for _ in range(args.warmup_runs):
        run_generation(model, tokenizer, prompts[0], min(args.max_new_tokens, 8), use_chat_template=args.chat_template)
    baseline_metrics = [
        run_generation(model, tokenizer, prompt, args.max_new_tokens, use_chat_template=args.chat_template) for prompt in prompts
    ]

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
    fused_metrics = [
        run_generation(model, tokenizer, prompt, args.max_new_tokens, use_chat_template=args.chat_template) for prompt in prompts
    ]
    for runtime in fused_runtimes:
        runtime.finalize_pending()

    rows = []
    for idx, (prompt, baseline, fused) in enumerate(zip(prompts, baseline_metrics, fused_metrics, strict=True)):
        rows.append(
            {
                "id": idx,
                "prompt": prompt,
                "baseline": baseline,
                "fused": fused,
                "comparison": compare_text(baseline["generated_text"], fused["generated_text"]),
            }
        )

    all_ms = [value for runtime in fused_runtimes for value in runtime.stats.cuda_event_ms]
    result = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "model": args.model,
        "device": args.device,
        "dtype": args.dtype,
        "package_summary": str(package_summary),
        "layers": layers,
        "suffixes": suffixes,
        "dense_roles": sorted(dense_roles),
        "chat_template": bool(args.chat_template),
        "max_new_tokens": int(args.max_new_tokens),
        "sync_mode": args.sync_mode,
        "prompts": prompts,
        "rows": rows,
        "aggregate": aggregate(rows),
        "replacement_raw_fp32_bytes": int(sum(runtime.raw_fp32_bytes for runtime in fused_runtimes)),
        "replacement_package_bytes": int(sum(runtime.package_bytes for runtime in fused_runtimes)),
        "replacement_compression_vs_fp32": float(
            sum(runtime.raw_fp32_bytes for runtime in fused_runtimes)
            / max(sum(runtime.package_bytes for runtime in fused_runtimes), 1)
        ),
        "replacement_dense_role_calls": int(sum(runtime.stats.dense_role_calls for runtime in fused_runtimes)),
        "replacement_wrapper_calls": int(sum(runtime.stats.wrapper_calls for runtime in fused_runtimes)),
        "replacement_fused_compute_calls": int(sum(runtime.stats.fused_compute_calls for runtime in fused_runtimes)),
        "replacement_cache_hits": int(sum(runtime.stats.cache_hits for runtime in fused_runtimes)),
        "replacement_cache_misses": int(sum(runtime.stats.cache_misses for runtime in fused_runtimes)),
        "replacement_cuda_event_ms": summarize_ms(all_ms),
        "peak_gpu_memory_mib": float(torch.cuda.max_memory_allocated() / (1024 * 1024)) if args.device.startswith("cuda") else 0.0,
    }
    out_json = resolve_path(args.out_json, root)
    out_md = resolve_path(args.out_md, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    write_report(out_md, result)
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "aggregate": result["aggregate"]}, indent=2, ensure_ascii=False))

    del model
    if args.device.startswith("cuda"):
        torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
