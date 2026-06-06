from __future__ import annotations

"""Benchmark fused selected-row ESMP execution across same-input modules.

The existing selected-row benchmark launches the packed INT4/INT8 kernels per
Linear module. For QKV-style routing, those modules share the same input, so a
deterministic skill slice can concatenate the selected packed rows and execute
them as one fused selected-row payload. This script measures that lower-launch
overhead path against strong dense concat baselines.
"""

import argparse
import csv
import json
import statistics
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import torch
    import torch.nn.functional as F
    from transformers import AutoModelForCausalLM
except ModuleNotFoundError:  # pragma: no cover
    torch = None
    F = None
    AutoModelForCausalLM = None

try:
    import triton
    from triton_mixed_gemm import _int4_selected_matmul_kernel, _int8_selected_matmul_kernel
except ModuleNotFoundError:  # pragma: no cover
    triton = None
    _int4_selected_matmul_kernel = None
    _int8_selected_matmul_kernel = None

from benchmark_esmp_selected_rows import (
    build_selected_groups,
    mean,
    median,
    parse_ints,
    rel_l2,
    select_even_rows,
    time_ms,
    triton_selected_forward,
    write_csv,
    write_jsonl,
)
from eval_esmp_module_reconstruction import DEFAULT_MODEL, DEFAULT_PACKAGE_SUMMARY, load_package_modules, resolve_path, repo_root
from measure_esmp_generation_latency import EsmpLinear, parse_layers, select_modules


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    pos = (len(ordered) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(ordered) - 1)
    frac = pos - lo
    return float(ordered[lo] * (1.0 - frac) + ordered[hi] * frac)


def parse_suffixes(text: str) -> list[str]:
    values = [part.strip() for part in text.replace(";", ",").split(",") if part.strip()]
    if not values:
        raise ValueError("at least one suffix is required")
    return values


def build_exact_modules_for_layer(layer: int, suffixes: list[str]) -> list[str]:
    return [f"model.layers.{layer}.self_attn.{suffix}" for suffix in suffixes]


def concat_bias(modules: list[torch.nn.Linear], selected: list[torch.Tensor] | None = None) -> torch.Tensor | None:
    chunks: list[torch.Tensor] = []
    for idx, module in enumerate(modules):
        if module.bias is None:
            return None
        bias = module.bias
        if selected is not None:
            bias = bias.index_select(0, selected[idx])
        chunks.append(bias)
    return torch.cat(chunks, dim=0).contiguous()


def concat_weight(modules: list[torch.nn.Linear], selected: list[torch.Tensor] | None = None) -> torch.Tensor:
    chunks: list[torch.Tensor] = []
    for idx, module in enumerate(modules):
        weight = module.weight
        if selected is not None:
            weight = weight.index_select(0, selected[idx])
        chunks.append(weight)
    return torch.cat(chunks, dim=0).contiguous()


def build_fused_selected_groups(
    runtimes: list[EsmpLinear],
    selected_by_module: list[torch.Tensor],
) -> dict[str, Any]:
    if not runtimes:
        raise ValueError("no runtimes")
    device = selected_by_module[0].device
    cols = int(runtimes[0].in_features)
    q4_stride = int(runtimes[0].triton_q4.shape[1]) if runtimes[0].triton_q4.ndim == 2 else (cols + 1) // 2
    q4_chunks: list[torch.Tensor] = []
    q8_chunks: list[torch.Tensor] = []
    low_slots: list[torch.Tensor] = []
    low_row_ids: list[torch.Tensor] = []
    low_out_pos: list[torch.Tensor] = []
    high_slots: list[torch.Tensor] = []
    high_row_ids: list[torch.Tensor] = []
    high_out_pos: list[torch.Tensor] = []
    scale_chunks: list[torch.Tensor] = []
    bias_chunks: list[torch.Tensor] = []
    module_offsets: list[int] = []
    total_selected = 0
    total_low = 0
    total_high = 0

    for runtime, selected_rows in zip(runtimes, selected_by_module, strict=True):
        if int(runtime.in_features) != cols:
            raise ValueError("fused selected rows require matching input feature dimensions")
        groups = build_selected_groups(runtime, selected_rows)
        module_offsets.append(total_selected)
        selected_count = int(selected_rows.numel())
        scale_chunks.append(runtime.triton_scales.index_select(0, selected_rows.long()).float().contiguous())
        if runtime.bias is not None:
            bias_chunks.append(runtime.bias.index_select(0, selected_rows.long()).float().contiguous())
        else:
            bias_chunks.append(torch.zeros(selected_count, device=device, dtype=torch.float32))

        low_count = int(groups["low_slots"].numel())
        if low_count:
            q4_chunks.append(runtime.triton_q4.index_select(0, groups["low_slots"].long()).contiguous())
            slots = torch.arange(total_low, total_low + low_count, device=device, dtype=torch.long)
            out_pos = groups["low_out_pos"].long() + total_selected
            low_slots.append(slots)
            low_row_ids.append(out_pos)
            low_out_pos.append(out_pos)
            total_low += low_count

        high_count = int(groups["high_slots"].numel())
        if high_count:
            q8_chunks.append(runtime.triton_q8.index_select(0, groups["high_slots"].long()).contiguous())
            slots = torch.arange(total_high, total_high + high_count, device=device, dtype=torch.long)
            out_pos = groups["high_out_pos"].long() + total_selected
            high_slots.append(slots)
            high_row_ids.append(out_pos)
            high_out_pos.append(out_pos)
            total_high += high_count

        total_selected += selected_count

    if q4_chunks:
        q4 = torch.cat(q4_chunks, dim=0).contiguous()
    else:
        q4 = torch.empty((0, q4_stride), device=device, dtype=torch.uint8)
    if q8_chunks:
        q8 = torch.cat(q8_chunks, dim=0).contiguous()
    else:
        q8 = torch.empty((0, cols), device=device, dtype=torch.int8)

    def cat_or_empty(chunks: list[torch.Tensor]) -> torch.Tensor:
        if chunks:
            return torch.cat(chunks, dim=0).contiguous()
        return torch.empty((0,), device=device, dtype=torch.long)

    return {
        "q4": q4,
        "q8": q8,
        "low_slots": cat_or_empty(low_slots),
        "low_row_ids": cat_or_empty(low_row_ids),
        "low_out_pos": cat_or_empty(low_out_pos),
        "high_slots": cat_or_empty(high_slots),
        "high_row_ids": cat_or_empty(high_row_ids),
        "high_out_pos": cat_or_empty(high_out_pos),
        "scales": torch.cat(scale_chunks, dim=0).contiguous(),
        "bias": torch.cat(bias_chunks, dim=0).contiguous(),
        "cols": cols,
        "q4_stride": q4_stride,
        "total_selected": total_selected,
        "module_offsets": module_offsets,
        "low_rows": total_low,
        "high_rows": total_high,
    }


def triton_fused_selected_forward(
    x: torch.Tensor,
    fused: dict[str, Any],
    block_m: int,
    block_n: int,
    block_k: int,
) -> torch.Tensor:
    if triton is None or _int4_selected_matmul_kernel is None or _int8_selected_matmul_kernel is None:
        raise RuntimeError("fused selected-row runtime requires triton")
    flat = x.reshape(-1, int(fused["cols"])).contiguous()
    batch = int(flat.shape[0])
    total_selected = int(fused["total_selected"])
    y = torch.empty((batch, total_selected), device=x.device, dtype=torch.float32)
    low_count = int(fused["low_slots"].numel())
    if low_count:
        grid4 = (triton.cdiv(low_count, block_m), triton.cdiv(batch, block_n))
        _int4_selected_matmul_kernel[grid4](
            flat,
            fused["q4"],
            fused["low_slots"],
            fused["low_row_ids"],
            fused["low_out_pos"],
            fused["scales"],
            y,
            low_count,
            total_selected,
            int(fused["cols"]),
            batch,
            int(fused["q4_stride"]),
            block_m,
            block_n,
            block_k,
            num_warps=4,
        )
    high_count = int(fused["high_slots"].numel())
    if high_count:
        grid8 = (triton.cdiv(high_count, block_m), triton.cdiv(batch, block_n))
        _int8_selected_matmul_kernel[grid8](
            flat,
            fused["q8"],
            fused["high_slots"],
            fused["high_row_ids"],
            fused["high_out_pos"],
            fused["scales"],
            y,
            high_count,
            total_selected,
            int(fused["cols"]),
            batch,
            block_m,
            block_n,
            block_k,
            num_warps=4,
        )
    y = y + fused["bias"][None, :]
    return y.reshape(*x.shape[:-1], total_selected).to(dtype=x.dtype)


def write_report(path: Path, result: dict[str, Any]) -> None:
    rows = [row for row in result["rows"] if row.get("ok")]
    lines = [
        "# ESMP Fused Selected-Row Runtime Benchmark",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Layers: `{result['layers']}`",
        f"Module suffixes: `{result['suffixes']}`",
        f"Batch shapes: `{result['batches']}`",
        f"Selected rows per module: `{result['selected_rows']}`",
        f"Warmup/iters: `{result['warmup']}/{result['iters']}`",
        "",
        "## Summary By Runtime",
        "",
        "| runtime | cases | median ms | p90 ms | median speedup vs dense full concat | median speedup vs dense selected concat | median speedup vs triton separate | median rel-L2 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for runtime in [
        "dense_full_concat",
        "dense_selected_concat",
        "cached_selected_concat",
        "triton_separate_selected",
        "triton_fused_selected",
    ]:
        bucket = [row for row in rows if row["runtime"] == runtime]
        if not bucket:
            continue
        lat = [float(row["latency_ms"]) for row in bucket]
        lines.append(
            f"| {runtime} | {len(bucket)} | {median(lat):.6f} | {percentile(lat, 0.9):.6f} | "
            f"{median([float(r.get('speedup_vs_dense_full_concat', 1.0)) for r in bucket]):.4f} | "
            f"{median([float(r.get('speedup_vs_dense_selected_concat', 1.0)) for r in bucket]):.4f} | "
            f"{median([float(r.get('speedup_vs_triton_separate', 1.0)) for r in bucket]):.4f} | "
            f"{median([float(r.get('rel_l2_vs_dense_selected_concat', 0.0)) for r in bucket]):.6f} |"
        )
    fused_rows = [row for row in rows if row["runtime"] == "triton_fused_selected"]
    if fused_rows:
        lines.extend(
            [
                "",
                "## Fused Wins",
                "",
                f"- Fused faster than triton separate: `{sum(1 for row in fused_rows if float(row.get('speedup_vs_triton_separate', 0.0)) > 1.0)} / {len(fused_rows)}`",
                f"- Fused faster than dense full concat: `{sum(1 for row in fused_rows if float(row.get('speedup_vs_dense_full_concat', 0.0)) > 1.0)} / {len(fused_rows)}`",
                f"- Fused faster than dense selected concat: `{sum(1 for row in fused_rows if float(row.get('speedup_vs_dense_selected_concat', 0.0)) > 1.0)} / {len(fused_rows)}`",
                f"- Best fused speedup vs triton separate: `{max(float(row.get('speedup_vs_triton_separate', 0.0)) for row in fused_rows):.4f}x`",
                f"- Best fused speedup vs dense full concat: `{max(float(row.get('speedup_vs_dense_full_concat', 0.0)) for row in fused_rows):.4f}x`",
            ]
        )
    lines.extend(
        [
            "",
            "## Per-Case Results",
            "",
            "| layer | batch | selected/module | runtime | latency ms | speedup vs full concat | speedup vs selected concat | speedup vs triton separate | rel-L2 |",
            "|---:|---:|---:|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in sorted(rows, key=lambda r: (int(r["layer"]), int(r["batch"]), int(r["selected_rows_per_module"]), r["runtime"])):
        lines.append(
            f"| {row['layer']} | {row['batch']} | {row['selected_rows_per_module']} | {row['runtime']} | "
            f"{float(row['latency_ms']):.6f} | "
            f"{float(row.get('speedup_vs_dense_full_concat', 1.0)):.4f} | "
            f"{float(row.get('speedup_vs_dense_selected_concat', 1.0)):.4f} | "
            f"{float(row.get('speedup_vs_triton_separate', 1.0)):.4f} | "
            f"{float(row.get('rel_l2_vs_dense_selected_concat', 0.0)):.6f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation Guardrails",
            "",
            "- This is a same-input multi-module selected-row microbenchmark, not end-to-end LLM acceleration.",
            "- `dense_full_concat` and `dense_selected_concat` are strong one-launch torch baselines built from concatenated FP16 weights.",
            "- `triton_fused_selected` reduces ESMP launch count across QKV-style modules by concatenating selected packed rows ahead of time.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def add_record(
    rows: list[dict[str, Any]],
    base: dict[str, Any],
    runtime: str,
    latency_ms: float,
    dense_full_ms: float,
    dense_selected_ms: float,
    triton_separate_ms: float | None,
    rel_l2_value: float,
) -> None:
    rows.append(
        {
            **base,
            "ok": True,
            "runtime": runtime,
            "latency_ms": float(latency_ms),
            "speedup_vs_dense_full_concat": float(dense_full_ms / latency_ms) if latency_ms > 0 else 0.0,
            "speedup_vs_dense_selected_concat": float(dense_selected_ms / latency_ms) if latency_ms > 0 else 0.0,
            "speedup_vs_triton_separate": float(triton_separate_ms / latency_ms) if triton_separate_ms and latency_ms > 0 else 1.0,
            "rel_l2_vs_dense_selected_concat": float(rel_l2_value),
        }
    )
    print(json.dumps(rows[-1], ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark fused selected-row ESMP execution across QKV-style modules.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--package-summary", default=DEFAULT_PACKAGE_SUMMARY)
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--layers", default="0")
    parser.add_argument("--suffixes", default="q_proj,k_proj,v_proj")
    parser.add_argument("--batches", default="1,12,64")
    parser.add_argument("--selected-rows", default="16,64,256")
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--iters", type=int, default=80)
    parser.add_argument("--block-m", type=int, default=32)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=128)
    parser.add_argument("--out-json", default="outputs/real_system_packer_2026-06-05/esmp_fused_selected_rows.json")
    parser.add_argument("--out-jsonl", default="outputs/real_system_packer_2026-06-05/esmp_fused_selected_rows.jsonl")
    parser.add_argument("--out-csv", default="outputs/real_system_packer_2026-06-05/esmp_fused_selected_rows.csv")
    parser.add_argument("--out-md", default="outputs/real_system_packer_2026-06-05/ESMP_FUSED_SELECTED_ROWS.md")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None:
        raise SystemExit("missing dependencies: install torch and transformers")
    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")
    if triton is None:
        raise SystemExit("Triton is required for fused selected-row benchmark")

    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    device = torch.device(args.device)
    layers = sorted(parse_layers(args.layers) or set())
    suffixes = parse_suffixes(args.suffixes)
    batches = parse_ints(args.batches)
    selected_counts = parse_ints(args.selected_rows)
    if args.device == "cuda":
        torch.cuda.reset_peak_memory_stats()

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )
    model.eval()
    model.to(device)
    model_modules = {name: module for name, module in model.named_modules() if isinstance(module, torch.nn.Linear)}
    package_modules = load_package_modules(package_summary)
    rows: list[dict[str, Any]] = []
    torch.manual_seed(20260606)

    for layer in layers:
        exact_modules = build_exact_modules_for_layer(layer, suffixes)
        selected_items = select_modules(
            package_modules,
            model_modules=model_modules,
            exact_modules=exact_modules,
            filters=[],
            layers=None,
            include_lm_head=False,
            max_modules=0,
        )
        selected_by_name = {str(item["module"]): item for item in selected_items}
        if any(name not in selected_by_name for name in exact_modules):
            missing = [name for name in exact_modules if name not in selected_by_name]
            raise SystemExit(f"missing modules for layer {layer}: {missing}")

        items = [selected_by_name[name] for name in exact_modules]
        sources = [model_modules[str(item["module"])] for item in items]
        for source in sources:
            source.eval()
        packed = [EsmpLinear(source, item["out"], "triton_grouped", device, dtype, args.block_m, args.block_n, args.block_k) for source, item in zip(sources, items, strict=True)]
        cached = [EsmpLinear(source, item["out"], "cached", device, dtype, args.block_m, args.block_n, args.block_k) for source, item in zip(sources, items, strict=True)]
        if len({int(source.in_features) for source in sources}) != 1:
            raise SystemExit(f"layer {layer} modules do not share input feature dimensions")
        full_weight = concat_weight(sources).to(device=device, dtype=dtype)
        full_bias = concat_bias(sources)
        if full_bias is not None:
            full_bias = full_bias.to(device=device, dtype=dtype)

        for batch in batches:
            x = torch.randn(batch, int(sources[0].in_features), device=device, dtype=dtype)
            dense_full_ms = time_ms(lambda: F.linear(x, full_weight, full_bias), args.warmup, args.iters)
            for count in selected_counts:
                selected_by_module = [select_even_rows(int(source.out_features), count, device) for source in sources]
                selected_weight = concat_weight(sources, selected_by_module).to(device=device, dtype=dtype)
                selected_bias = concat_bias(sources, selected_by_module)
                if selected_bias is not None:
                    selected_bias = selected_bias.to(device=device, dtype=dtype)
                cached_weight = torch.cat(
                    [runtime.weight_dequant.index_select(0, selected_by_module[idx]).to(dtype=dtype) for idx, runtime in enumerate(cached)],
                    dim=0,
                ).contiguous()
                cached_bias = concat_bias(cached, selected_by_module)
                if cached_bias is not None:
                    cached_bias = cached_bias.to(device=device, dtype=dtype)
                separate_groups = [build_selected_groups(runtime, selected_by_module[idx]) for idx, runtime in enumerate(packed)]
                fused_groups = build_fused_selected_groups(packed, selected_by_module)

                with torch.inference_mode():
                    dense_selected_out = F.linear(x, selected_weight, selected_bias)

                dense_selected_ms = time_ms(lambda: F.linear(x, selected_weight, selected_bias), args.warmup, args.iters)
                cached_selected_ms = time_ms(lambda: F.linear(x, cached_weight, cached_bias), args.warmup, args.iters)

                def separate_forward() -> torch.Tensor:
                    return torch.cat(
                        [
                            triton_selected_forward(runtime, x, selected_by_module[idx], separate_groups[idx], args.block_m, args.block_n, args.block_k)
                            for idx, runtime in enumerate(packed)
                        ],
                        dim=-1,
                    )

                def fused_forward() -> torch.Tensor:
                    return triton_fused_selected_forward(x, fused_groups, args.block_m, args.block_n, args.block_k)

                triton_separate_ms = time_ms(separate_forward, args.warmup, args.iters)
                triton_fused_ms = time_ms(fused_forward, args.warmup, args.iters)
                with torch.inference_mode():
                    cached_out = F.linear(x, cached_weight, cached_bias)
                    separate_out = separate_forward()
                    fused_out = fused_forward()

                base = {
                    "model": args.model,
                    "layer": int(layer),
                    "modules": exact_modules,
                    "module_count": len(exact_modules),
                    "suffixes": suffixes,
                    "batch": int(batch),
                    "selected_rows_per_module": int(count),
                    "selected_rows_total": int(fused_groups["total_selected"]),
                    "low_rows_total": int(fused_groups["low_rows"]),
                    "high_rows_total": int(fused_groups["high_rows"]),
                    "cols": int(fused_groups["cols"]),
                    "block_m": int(args.block_m),
                    "block_n": int(args.block_n),
                    "block_k": int(args.block_k),
                    "dense_full_concat_ms": float(dense_full_ms),
                    "dense_selected_concat_ms": float(dense_selected_ms),
                    "triton_separate_selected_ms": float(triton_separate_ms),
                }
                add_record(rows, base, "dense_full_concat", dense_full_ms, dense_full_ms, dense_selected_ms, triton_separate_ms, 0.0)
                add_record(rows, base, "dense_selected_concat", dense_selected_ms, dense_full_ms, dense_selected_ms, triton_separate_ms, 0.0)
                add_record(
                    rows,
                    base,
                    "cached_selected_concat",
                    cached_selected_ms,
                    dense_full_ms,
                    dense_selected_ms,
                    triton_separate_ms,
                    rel_l2(cached_out, dense_selected_out),
                )
                add_record(
                    rows,
                    base,
                    "triton_separate_selected",
                    triton_separate_ms,
                    dense_full_ms,
                    dense_selected_ms,
                    triton_separate_ms,
                    rel_l2(separate_out, dense_selected_out),
                )
                add_record(
                    rows,
                    base,
                    "triton_fused_selected",
                    triton_fused_ms,
                    dense_full_ms,
                    dense_selected_ms,
                    triton_separate_ms,
                    rel_l2(fused_out, dense_selected_out),
                )
                rows[-1]["rel_l2_vs_triton_separate"] = rel_l2(fused_out, separate_out)

    result = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "model": args.model,
        "package_summary": str(package_summary),
        "layers": layers,
        "suffixes": suffixes,
        "batches": batches,
        "selected_rows": selected_counts,
        "warmup": args.warmup,
        "iters": args.iters,
        "rows": rows,
        "peak_cuda_memory_mib": torch.cuda.max_memory_allocated() / (1024 * 1024) if args.device == "cuda" else None,
    }
    out_json = resolve_path(args.out_json, root)
    out_jsonl = resolve_path(args.out_jsonl, root)
    out_csv = resolve_path(args.out_csv, root)
    out_md = resolve_path(args.out_md, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    write_jsonl(out_jsonl, rows)
    write_csv(out_csv, rows)
    write_report(out_md, result)
    print(
        json.dumps(
            {
                "out_json": str(out_json),
                "out_jsonl": str(out_jsonl),
                "out_csv": str(out_csv),
                "out_md": str(out_md),
                "peak_cuda_memory_mib": result["peak_cuda_memory_mib"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
