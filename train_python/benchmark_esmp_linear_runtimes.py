#!/usr/bin/env python3
from __future__ import annotations

"""Microbenchmark real ESMP Linear runtimes on generation-like shapes."""

import argparse
import csv
import json
import math
import statistics
import time
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

from eval_esmp_module_reconstruction import DEFAULT_MODEL, DEFAULT_PACKAGE_SUMMARY, load_package_modules, resolve_path, repo_root
from measure_esmp_generation_latency import EsmpLinear, parse_layers, select_modules
from triton_config_selector import load_kernel_configs


def synchronize() -> None:
    if torch is not None and torch.cuda.is_available():
        torch.cuda.synchronize()


def time_ms(fn, warmup: int, iters: int) -> float:
    for _ in range(warmup):
        fn()
    synchronize()
    start = time.perf_counter()
    for _ in range(iters):
        fn()
    synchronize()
    return (time.perf_counter() - start) * 1000.0 / max(iters, 1)


def rel_l2(lhs: torch.Tensor, rhs: torch.Tensor) -> float:
    num = torch.linalg.vector_norm((lhs.float() - rhs.float()).reshape(-1))
    den = torch.linalg.vector_norm(rhs.float().reshape(-1)).clamp_min(1.0e-12)
    return float((num / den).detach().cpu().item())


def parse_ints(text: str) -> list[int]:
    return [int(part.strip()) for part in text.replace(";", ",").split(",") if part.strip()]


def mean(values: list[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def median(values: list[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    keys = sorted({key for row in rows for key in row.keys()})
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, result: dict[str, Any]) -> None:
    rows = result["rows"]
    ok = [row for row in rows if row.get("ok")]
    lines = [
        "# ESMP Linear Runtime Shape Benchmark",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Modules: `{result['module_count']}`",
        f"Batch shapes: `{result['batches']}`",
        f"Warmup/iters: `{result['warmup']}/{result['iters']}`",
        "",
        "## Summary By Runtime",
        "",
        "| runtime | cases | median ms | mean ms | median speedup vs dense | median rel-L2 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for runtime in ["dense", "cached", "python_on_demand", "triton_grouped"]:
        bucket = [row for row in ok if row["runtime"] == runtime]
        if not bucket:
            continue
        lines.append(
            f"| {runtime} | {len(bucket)} | {median([float(r['latency_ms']) for r in bucket]):.6f} | "
            f"{mean([float(r['latency_ms']) for r in bucket]):.6f} | "
            f"{median([float(r.get('speedup_vs_dense', 1.0)) for r in bucket]):.4f} | "
            f"{median([float(r.get('rel_l2_vs_dense', 0.0)) for r in bucket]):.6f} |"
        )

    lines.extend(
        [
            "",
            "## Per-Case Results",
            "",
            "| module | batch | runtime | latency ms | speedup vs dense | rel-L2 vs dense | selector calls |",
            "|---|---:|---|---:|---:|---:|---:|",
        ]
    )
    for row in sorted(ok, key=lambda r: (r["module"], int(r["batch"]), r["runtime"])):
        lines.append(
            f"| `{row['module']}` | {row['batch']} | {row['runtime']} | {row['latency_ms']:.6f} | "
            f"{float(row.get('speedup_vs_dense', 1.0)):.4f} | {float(row.get('rel_l2_vs_dense', 0.0)):.6f} | "
            f"{int(row.get('selector_call_count', 0) or 0)} |"
        )
    failures = [row for row in rows if not row.get("ok")]
    if failures:
        lines.extend(["", "## Failures", ""])
        for row in failures:
            lines.append(f"- `{row.get('module')}` batch={row.get('batch')} runtime={row.get('runtime')}: {row.get('error')}")
    lines.extend(
        [
            "",
            "## Interpretation Guardrails",
            "",
            "- This is a real ESMP module-runtime benchmark, not an end-to-end LLM claim.",
            "- Batch `1` approximates decode-step Linear calls; batch `12` approximates the current short-prompt prefill; batch `64` tests amortization.",
            "- Triton speedups below dense mean the current grouped kernel needs fusion, shape-specific tuning, or a lower-launch-overhead path.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark dense/cached/on-demand/Triton ESMP Linear runtimes.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--package-summary", default=DEFAULT_PACKAGE_SUMMARY)
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--module", action="append", default=[])
    parser.add_argument("--module-filter", action="append", default=[])
    parser.add_argument("--layers", default="")
    parser.add_argument("--max-modules", type=int, default=3)
    parser.add_argument("--batches", default="1,12,64")
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--iters", type=int, default=80)
    parser.add_argument("--block-m", type=int, default=32)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=128)
    parser.add_argument("--kernel-config-selector", default="", help="Optional JSON output from select_triton_kernel_configs.py.")
    parser.add_argument("--prefer-selector-fp16-win", action="store_true", help="Prefer FP16-winning selector rows after batch/shape matching.")
    parser.add_argument("--out-json", default="outputs/real_system_packer_2026-06-05/esmp_linear_runtime_shapes.json")
    parser.add_argument("--out-jsonl", default="outputs/real_system_packer_2026-06-05/esmp_linear_runtime_shapes.jsonl")
    parser.add_argument("--out-csv", default="outputs/real_system_packer_2026-06-05/esmp_linear_runtime_shapes.csv")
    parser.add_argument("--out-md", default="outputs/real_system_packer_2026-06-05/ESMP_LINEAR_RUNTIME_SHAPES.md")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None:
        raise SystemExit("missing dependencies: install torch and transformers")
    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")

    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
    kernel_config_selector = resolve_path(args.kernel_config_selector, root) if args.kernel_config_selector else None
    kernel_configs = load_kernel_configs(kernel_config_selector) if kernel_config_selector else []
    if kernel_config_selector and not kernel_configs:
        raise SystemExit(f"No usable kernel configs in selector: {kernel_config_selector}")
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    if args.device == "cuda":
        torch.cuda.reset_peak_memory_stats()

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        local_files_only=args.local_files_only,
        trust_remote_code=True,
    )
    model.eval()
    model.to(args.device)
    model_modules = {name: module for name, module in model.named_modules() if isinstance(module, torch.nn.Linear)}
    selected = select_modules(
        load_package_modules(package_summary),
        model_modules=model_modules,
        exact_modules=args.module,
        filters=args.module_filter,
        layers=parse_layers(args.layers),
        include_lm_head=False,
        max_modules=args.max_modules,
    )
    if not selected:
        raise SystemExit("No modules selected.")

    batches = parse_ints(args.batches)
    rows: list[dict[str, Any]] = []
    torch.manual_seed(20260606)
    for item in selected:
        name = item["module"]
        source = model_modules[name]
        source.eval()
        runtimes: dict[str, Any] = {
            "dense": source,
            "cached": EsmpLinear(source, item["out"], "cached", torch.device(args.device), dtype, args.block_m, args.block_n, args.block_k),
            "python_on_demand": EsmpLinear(source, item["out"], "python_on_demand", torch.device(args.device), dtype, args.block_m, args.block_n, args.block_k),
            "triton_grouped": EsmpLinear(
                source,
                item["out"],
                "triton_grouped",
                torch.device(args.device),
                dtype,
                args.block_m,
                args.block_n,
                args.block_k,
                kernel_configs=kernel_configs,
                prefer_selector_fp16_win=args.prefer_selector_fp16_win,
            ),
        }
        for batch in batches:
            x = torch.randn(batch, int(source.in_features), device=args.device, dtype=dtype)
            with torch.inference_mode():
                dense_out = source(x)
            dense_ms = None
            for runtime, module in runtimes.items():
                record = {
                    "ok": False,
                    "model": args.model,
                    "module": name,
                    "bits": int(item.get("bits", 0)),
                    "rows": int(item.get("rows", 0)),
                    "cols": int(item.get("cols", 0)),
                    "batch": int(batch),
                    "runtime": runtime,
                    "block_m": args.block_m if runtime == "triton_grouped" else None,
                    "block_n": args.block_n if runtime == "triton_grouped" else None,
                    "block_k": args.block_k if runtime == "triton_grouped" else None,
                }
                try:
                    with torch.inference_mode():
                        if hasattr(module, "clear_runtime_config_summary"):
                            module.clear_runtime_config_summary()
                        latency = time_ms(lambda: module(x), args.warmup, args.iters)
                        out = module(x)
                    if runtime == "dense":
                        dense_ms = latency
                    speedup = (dense_ms / latency) if dense_ms and latency > 0 else 1.0
                    runtime_config_summary = module.runtime_config_summary() if hasattr(module, "runtime_config_summary") else []
                    selector_call_count = sum(
                        int(event.get("count", 0))
                        for event in runtime_config_summary
                        if event.get("selection") == "selector"
                    )
                    record.update(
                        {
                            "ok": True,
                            "latency_ms": latency,
                            "speedup_vs_dense": speedup,
                            "rel_l2_vs_dense": 0.0 if runtime == "dense" else rel_l2(out, dense_out),
                            "runtime_config_summary": runtime_config_summary if runtime_config_summary else None,
                            "selector_call_count": selector_call_count,
                        }
                    )
                except Exception as exc:  # keep benchmark going across runtimes
                    record["error"] = repr(exc)
                rows.append(record)
                print(json.dumps(record, ensure_ascii=False), flush=True)
            del x, dense_out
        del runtimes

    result = {
        "date": time.strftime("%Y-%m-%d"),
        "model": args.model,
        "package_summary": str(package_summary),
        "kernel_config_selector": str(kernel_config_selector) if kernel_config_selector else None,
        "kernel_config_count": len(kernel_configs),
        "module_count": len(selected),
        "modules": [item["module"] for item in selected],
        "batches": batches,
        "warmup": args.warmup,
        "iters": args.iters,
        "block_m": args.block_m,
        "block_n": args.block_n,
        "block_k": args.block_k,
        "rows": rows,
        "peak_cuda_memory_mib": float(torch.cuda.max_memory_allocated() / (1024**2)) if args.device == "cuda" else 0.0,
    }
    out_json = resolve_path(args.out_json, root)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_jsonl(resolve_path(args.out_jsonl, root), rows)
    write_csv(resolve_path(args.out_csv, root), rows)
    write_report(resolve_path(args.out_md, root), result)
    print(
        json.dumps(
            {
                "out_json": str(out_json),
                "out_jsonl": str(resolve_path(args.out_jsonl, root)),
                "out_csv": str(resolve_path(args.out_csv, root)),
                "out_md": str(resolve_path(args.out_md, root)),
                "peak_cuda_memory_mib": result["peak_cuda_memory_mib"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
