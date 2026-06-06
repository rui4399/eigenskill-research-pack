from __future__ import annotations

"""Benchmark selected-row ESMP Linear execution on CUDA.

This script targets the deterministic routing/bypass case: the runtime only
needs a small subset of output rows, so it should not materialize the full
Linear output. It compares full dense, dense selected-row, cached-dequant
selected-row, and packed Triton selected-row paths on real ESMP packages.
"""

import argparse
import csv
import json
import statistics
import time
from pathlib import Path
from typing import Any

import numpy as np

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

from eval_esmp_module_reconstruction import DEFAULT_MODEL, DEFAULT_PACKAGE_SUMMARY, load_package_modules, resolve_path, repo_root
from measure_esmp_generation_latency import EsmpLinear, parse_layers, select_modules


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


def median(values: list[float]) -> float:
    return float(statistics.median(values)) if values else 0.0


def mean(values: list[float]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def select_even_rows(rows: int, count: int, device: torch.device) -> torch.Tensor:
    count = max(1, min(int(count), int(rows)))
    if count == rows:
        return torch.arange(rows, device=device, dtype=torch.long)
    values = torch.linspace(0, rows - 1, steps=count, device=device).round().long()
    values = torch.unique_consecutive(values)
    if int(values.numel()) < count:
        seen = set(int(v) for v in values.detach().cpu().tolist())
        fill = [idx for idx in range(rows) if idx not in seen]
        extra = torch.tensor(fill[: count - int(values.numel())], device=device, dtype=torch.long)
        values = torch.cat([values, extra], dim=0)
    return values[:count].sort().values


def build_selected_groups(runtime: EsmpLinear, selected_rows: torch.Tensor) -> dict[str, torch.Tensor]:
    device = selected_rows.device
    selected_np = selected_rows.detach().cpu().numpy().astype(np.int64, copy=False)
    row_bits = runtime.esmp.row_bits
    low_rows = runtime.triton_low_rows.detach().cpu().numpy().astype(np.int64, copy=False)
    high_rows = runtime.triton_high_rows.detach().cpu().numpy().astype(np.int64, copy=False)
    low_slot_by_row = {int(row): slot for slot, row in enumerate(low_rows)}
    high_slot_by_row = {int(row): slot for slot, row in enumerate(high_rows)}
    low_slots: list[int] = []
    low_row_ids: list[int] = []
    low_out_pos: list[int] = []
    high_slots: list[int] = []
    high_row_ids: list[int] = []
    high_out_pos: list[int] = []
    for out_pos, row in enumerate(selected_np.tolist()):
        bits = int(row_bits[int(row)])
        if bits == 4:
            low_slots.append(low_slot_by_row[int(row)])
            low_row_ids.append(int(row))
            low_out_pos.append(int(out_pos))
        elif bits == 8:
            high_slots.append(high_slot_by_row[int(row)])
            high_row_ids.append(int(row))
            high_out_pos.append(int(out_pos))
        else:
            raise ValueError(f"selected-row Triton path only supports INT4/INT8 rows, got {bits}")

    def tensor(values: list[int]) -> torch.Tensor:
        return torch.tensor(values, device=device, dtype=torch.long)

    return {
        "low_slots": tensor(low_slots),
        "low_row_ids": tensor(low_row_ids),
        "low_out_pos": tensor(low_out_pos),
        "high_slots": tensor(high_slots),
        "high_row_ids": tensor(high_row_ids),
        "high_out_pos": tensor(high_out_pos),
    }


def triton_selected_forward(
    runtime: EsmpLinear,
    x: torch.Tensor,
    selected_rows: torch.Tensor,
    groups: dict[str, torch.Tensor],
    block_m: int,
    block_n: int,
    block_k: int,
) -> torch.Tensor:
    if triton is None or _int4_selected_matmul_kernel is None or _int8_selected_matmul_kernel is None:
        raise RuntimeError("selected-row Triton runtime requires triton")
    flat = x.reshape(-1, runtime.in_features).contiguous()
    batch = int(flat.shape[0])
    selected_count = int(selected_rows.numel())
    y = torch.empty((batch, selected_count), device=x.device, dtype=torch.float32)
    if int(groups["low_slots"].numel()) > 0:
        grid4 = (triton.cdiv(int(groups["low_slots"].numel()), block_m), triton.cdiv(batch, block_n))
        _int4_selected_matmul_kernel[grid4](
            flat,
            runtime.triton_q4,
            groups["low_slots"],
            groups["low_row_ids"],
            groups["low_out_pos"],
            runtime.triton_scales,
            y,
            int(groups["low_slots"].numel()),
            selected_count,
            runtime.in_features,
            batch,
            int(runtime.triton_q4.shape[1]) if runtime.triton_q4.ndim == 2 else 0,
            block_m,
            block_n,
            block_k,
            num_warps=4,
        )
    if int(groups["high_slots"].numel()) > 0:
        grid8 = (triton.cdiv(int(groups["high_slots"].numel()), block_m), triton.cdiv(batch, block_n))
        _int8_selected_matmul_kernel[grid8](
            flat,
            runtime.triton_q8,
            groups["high_slots"],
            groups["high_row_ids"],
            groups["high_out_pos"],
            runtime.triton_scales,
            y,
            int(groups["high_slots"].numel()),
            selected_count,
            runtime.in_features,
            batch,
            block_m,
            block_n,
            block_k,
            num_warps=4,
        )
    if runtime.bias is not None:
        y = y + runtime.bias.index_select(0, selected_rows).float()
    return y.reshape(*x.shape[:-1], selected_count).to(dtype=x.dtype)


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
    keys = sorted({key for row in rows for key in row})
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, result: dict[str, Any]) -> None:
    rows = [row for row in result["rows"] if row.get("ok")]
    lines = [
        "# ESMP Selected-Row Runtime Benchmark",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Modules: `{result['module_count']}`",
        f"Batch shapes: `{result['batches']}`",
        f"Selected rows: `{result['selected_rows']}`",
        f"Warmup/iters: `{result['warmup']}/{result['iters']}`",
        "",
        "## Summary By Runtime",
        "",
        "| runtime | cases | median ms | mean ms | median speedup vs dense full | median speedup vs dense selected | median rel-L2 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for runtime in ["dense_full", "dense_selected", "cached_selected", "triton_selected"]:
        bucket = [row for row in rows if row["runtime"] == runtime]
        if not bucket:
            continue
        lines.append(
            f"| {runtime} | {len(bucket)} | {median([float(r['latency_ms']) for r in bucket]):.6f} | "
            f"{mean([float(r['latency_ms']) for r in bucket]):.6f} | "
            f"{median([float(r.get('speedup_vs_dense_full', 1.0)) for r in bucket]):.4f} | "
            f"{median([float(r.get('speedup_vs_dense_selected', 1.0)) for r in bucket]):.4f} | "
            f"{median([float(r.get('rel_l2_vs_dense_selected', 0.0)) for r in bucket]):.6f} |"
        )
    lines.extend(
        [
            "",
            "## Per-Case Results",
            "",
            "| module | batch | selected rows | runtime | latency ms | speedup vs dense full | speedup vs dense selected | rel-L2 |",
            "|---|---:|---:|---|---:|---:|---:|---:|",
        ]
    )
    for row in sorted(rows, key=lambda r: (r["module"], int(r["batch"]), int(r["selected_rows"]), r["runtime"])):
        lines.append(
            f"| `{row['module']}` | {row['batch']} | {row['selected_rows']} | {row['runtime']} | "
            f"{row['latency_ms']:.6f} | {float(row.get('speedup_vs_dense_full', 1.0)):.4f} | "
            f"{float(row.get('speedup_vs_dense_selected', 1.0)):.4f} | "
            f"{float(row.get('rel_l2_vs_dense_selected', 0.0)):.6f} |"
        )
    failures = [row for row in result["rows"] if not row.get("ok")]
    if failures:
        lines.extend(["", "## Failures", ""])
        for row in failures:
            lines.append(f"- `{row.get('module')}` batch={row.get('batch')} selected={row.get('selected_rows')} runtime={row.get('runtime')}: {row.get('error')}")
    lines.extend(
        [
            "",
            "## Interpretation Guardrails",
            "",
            "- This benchmark measures selected output rows only; it is a routing/bypass microbenchmark, not full generation throughput.",
            "- `speedup vs dense full` is the system-routing comparison: avoid materializing all rows when only a skill slice is needed.",
            "- `speedup vs dense selected` is the kernel comparison against torch operating on the selected FP16 rows only.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark selected-row ESMP Linear runtimes.")
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
    parser.add_argument("--selected-rows", default="16,64,256")
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--iters", type=int, default=80)
    parser.add_argument("--block-m", type=int, default=32)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=128)
    parser.add_argument("--out-json", default="outputs/real_system_packer_2026-06-05/esmp_selected_rows.json")
    parser.add_argument("--out-jsonl", default="outputs/real_system_packer_2026-06-05/esmp_selected_rows.jsonl")
    parser.add_argument("--out-csv", default="outputs/real_system_packer_2026-06-05/esmp_selected_rows.csv")
    parser.add_argument("--out-md", default="outputs/real_system_packer_2026-06-05/ESMP_SELECTED_ROWS.md")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None:
        raise SystemExit("missing dependencies: install torch and transformers")
    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")
    if triton is None:
        raise SystemExit("Triton is required for selected-row ESMP benchmark")

    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    device = torch.device(args.device)
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
    selected_modules = select_modules(
        load_package_modules(package_summary),
        model_modules=model_modules,
        exact_modules=args.module,
        filters=args.module_filter,
        layers=parse_layers(args.layers),
        include_lm_head=False,
        max_modules=args.max_modules,
    )
    if not selected_modules:
        raise SystemExit("No modules selected.")

    batches = parse_ints(args.batches)
    selected_counts = parse_ints(args.selected_rows)
    rows: list[dict[str, Any]] = []
    torch.manual_seed(20260606)

    for item in selected_modules:
        name = item["module"]
        source = model_modules[name]
        source.eval()
        cached = EsmpLinear(source, item["out"], "cached", device, dtype, args.block_m, args.block_n, args.block_k)
        packed = EsmpLinear(source, item["out"], "triton_grouped", device, dtype, args.block_m, args.block_n, args.block_k)

        for batch in batches:
            x = torch.randn(batch, int(source.in_features), device=device, dtype=dtype)
            dense_full_ms = time_ms(lambda: source(x), args.warmup, args.iters)
            for count in selected_counts:
                selected_rows = select_even_rows(int(source.out_features), count, device)
                groups = build_selected_groups(packed, selected_rows)
                source_weight_selected = source.weight.index_select(0, selected_rows).contiguous()
                bias_selected = source.bias.index_select(0, selected_rows).contiguous() if source.bias is not None else None
                cached_weight_selected = cached.weight_dequant.index_select(0, selected_rows).to(dtype=x.dtype).contiguous()
                cached_bias_selected = cached.bias.index_select(0, selected_rows).contiguous() if cached.bias is not None else None

                with torch.inference_mode():
                    dense_selected_out = F.linear(x, source_weight_selected, bias_selected)
                dense_selected_ms = time_ms(
                    lambda: F.linear(x, source_weight_selected, bias_selected),
                    args.warmup,
                    args.iters,
                )

                base_record = {
                    "ok": True,
                    "model": args.model,
                    "module": name,
                    "bits": int(item.get("bits", 0)),
                    "rows": int(item.get("rows", 0)),
                    "cols": int(item.get("cols", 0)),
                    "batch": int(batch),
                    "selected_rows": int(selected_rows.numel()),
                    "block_m": None,
                    "block_n": None,
                    "block_k": None,
                    "low_rows": int(groups["low_slots"].numel()),
                    "high_rows": int(groups["high_slots"].numel()),
                    "dense_full_ms": dense_full_ms,
                    "dense_selected_ms": dense_selected_ms,
                    "rel_l2_vs_dense_selected": 0.0,
                }
                for runtime, latency in [("dense_full", dense_full_ms), ("dense_selected", dense_selected_ms)]:
                    record = dict(base_record)
                    record.update(
                        {
                            "runtime": runtime,
                            "latency_ms": latency,
                            "speedup_vs_dense_full": dense_full_ms / latency if latency > 0 else 0.0,
                            "speedup_vs_dense_selected": dense_selected_ms / latency if latency > 0 else 0.0,
                        }
                    )
                    rows.append(record)
                    print(json.dumps(record, ensure_ascii=False))

                runtime_fns = {
                    "cached_selected": lambda: F.linear(x, cached_weight_selected, cached_bias_selected),
                    "triton_selected": lambda: triton_selected_forward(
                        packed,
                        x,
                        selected_rows,
                        groups,
                        args.block_m,
                        args.block_n,
                        args.block_k,
                    ),
                }
                for runtime, fn in runtime_fns.items():
                    record = dict(base_record)
                    record.update(
                        {
                            "ok": False,
                            "runtime": runtime,
                            "block_m": args.block_m if runtime == "triton_selected" else None,
                            "block_n": args.block_n if runtime == "triton_selected" else None,
                            "block_k": args.block_k if runtime == "triton_selected" else None,
                        }
                    )
                    try:
                        with torch.inference_mode():
                            latency = time_ms(fn, args.warmup, args.iters)
                            out = fn()
                        record.update(
                            {
                                "ok": True,
                                "latency_ms": latency,
                                "speedup_vs_dense_full": dense_full_ms / latency if latency > 0 else 0.0,
                                "speedup_vs_dense_selected": dense_selected_ms / latency if latency > 0 else 0.0,
                                "rel_l2_vs_dense_selected": rel_l2(out, dense_selected_out),
                            }
                        )
                    except Exception as exc:  # pragma: no cover
                        record["error"] = str(exc)
                    rows.append(record)
                    print(json.dumps(record, ensure_ascii=False))

    result = {
        "date": "2026-06-06",
        "model": args.model,
        "package_summary": str(package_summary),
        "module_count": len(selected_modules),
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
