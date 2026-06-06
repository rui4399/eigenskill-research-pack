from __future__ import annotations

"""Sweep Triton block sizes for selected-row ESMP execution.

The selected-row benchmark establishes correctness and first latency numbers.
This script keeps the model loaded once and sweeps a compact block grid to see
whether the current bottleneck is simply tile choice or deeper launch/fusion
overhead.
"""

import argparse
import csv
import json
import statistics
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


def parse_block_configs(text: str) -> list[tuple[int, int, int]]:
    configs: list[tuple[int, int, int]] = []
    for part in text.replace(";", ",").split(","):
        item = part.strip().lower().replace(" ", "")
        if not item:
            continue
        pieces = item.split("x")
        if len(pieces) != 3:
            raise ValueError(f"bad block config {part!r}; expected MxNxK")
        configs.append((int(pieces[0]), int(pieces[1]), int(pieces[2])))
    return configs


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    pos = (len(ordered) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(ordered) - 1)
    frac = pos - lo
    return float(ordered[lo] * (1.0 - frac) + ordered[hi] * frac)


def config_key(row: dict[str, Any]) -> str:
    return f"{row['block_m']}x{row['block_n']}x{row['block_k']}"


def write_report(path: Path, result: dict[str, Any]) -> None:
    rows = [row for row in result["rows"] if row.get("ok")]
    lines = [
        "# ESMP Selected-Row Block Sweep",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Modules: `{result['module_count']}`",
        f"Batch shapes: `{result['batches']}`",
        f"Selected rows: `{result['selected_rows']}`",
        f"Block configs: `{result['block_configs']}`",
        f"Warmup/iters: `{result['warmup']}/{result['iters']}`",
        "",
        "## Summary By Block Config",
        "",
        "| block | cases | median ms | p90 ms | median speedup vs dense full | median speedup vs dense selected | wins vs dense full | wins vs dense selected | best full speedup |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for block in sorted({config_key(row) for row in rows}):
        bucket = [row for row in rows if config_key(row) == block]
        lat = [float(row["latency_ms"]) for row in bucket]
        full = [float(row["speedup_vs_dense_full"]) for row in bucket]
        selected = [float(row["speedup_vs_dense_selected"]) for row in bucket]
        lines.append(
            f"| {block} | {len(bucket)} | {median(lat):.6f} | {percentile(lat, 0.9):.6f} | "
            f"{median(full):.4f} | {median(selected):.4f} | "
            f"{sum(1 for value in full if value > 1.0)} | {sum(1 for value in selected if value > 1.0)} | {max(full):.4f} |"
        )

    lines.extend(
        [
            "",
            "## Best Config Per Shape",
            "",
            "| module | batch | selected rows | best block | latency ms | speedup vs dense full | speedup vs dense selected | rel-L2 |",
            "|---|---:|---:|---|---:|---:|---:|---:|",
        ]
    )
    shape_keys = sorted({(row["module"], int(row["batch"]), int(row["selected_rows"])) for row in rows})
    for module, batch, selected_rows in shape_keys:
        bucket = [row for row in rows if row["module"] == module and int(row["batch"]) == batch and int(row["selected_rows"]) == selected_rows]
        best = max(bucket, key=lambda row: float(row["speedup_vs_dense_selected"]))
        lines.append(
            f"| `{module}` | {batch} | {selected_rows} | {config_key(best)} | {float(best['latency_ms']):.6f} | "
            f"{float(best['speedup_vs_dense_full']):.4f} | {float(best['speedup_vs_dense_selected']):.4f} | "
            f"{float(best['rel_l2_vs_dense_selected']):.6f} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation Guardrails",
            "",
            "- This sweep keeps the model loaded once and varies Triton block sizes only.",
            "- A config with isolated wins but weak median performance indicates launch/fusion overhead, not a complete hardware win.",
            "- Use this to choose the next kernel target; do not report it as end-to-end LLM acceleration.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sweep selected-row ESMP Triton block configs.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--package-summary", default=DEFAULT_PACKAGE_SUMMARY)
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float16", "bfloat16", "float32"], default="float16")
    parser.add_argument("--module", action="append", default=[])
    parser.add_argument("--module-filter", action="append", default=[])
    parser.add_argument("--layers", default="")
    parser.add_argument("--max-modules", type=int, default=3)
    parser.add_argument("--batches", default="1,12")
    parser.add_argument("--selected-rows", default="64,256")
    parser.add_argument("--block-configs", default="16x8x64,16x16x64,32x8x64,32x16x64,32x16x128,64x16x128")
    parser.add_argument("--warmup", type=int, default=5)
    parser.add_argument("--iters", type=int, default=40)
    parser.add_argument("--out-json", default="outputs/real_system_packer_2026-06-05/esmp_selected_row_block_sweep.json")
    parser.add_argument("--out-jsonl", default="outputs/real_system_packer_2026-06-05/esmp_selected_row_block_sweep.jsonl")
    parser.add_argument("--out-csv", default="outputs/real_system_packer_2026-06-05/esmp_selected_row_block_sweep.csv")
    parser.add_argument("--out-md", default="outputs/real_system_packer_2026-06-05/ESMP_SELECTED_ROW_BLOCK_SWEEP.md")
    args = parser.parse_args()

    if torch is None or AutoModelForCausalLM is None:
        raise SystemExit("missing dependencies: install torch and transformers")
    if args.device == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is false")

    root = repo_root()
    package_summary = resolve_path(args.package_summary, root)
    dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}[args.dtype]
    device = torch.device(args.device)
    block_configs = parse_block_configs(args.block_configs)
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

    rows: list[dict[str, Any]] = []
    torch.manual_seed(20260606)
    for item in selected_modules:
        name = item["module"]
        source = model_modules[name]
        source.eval()
        packed = EsmpLinear(source, item["out"], "triton_grouped", device, dtype, 32, 16, 128)
        for batch in batches:
            x = torch.randn(batch, int(source.in_features), device=device, dtype=dtype)
            dense_full_ms = time_ms(lambda: source(x), args.warmup, args.iters)
            for count in selected_counts:
                selected_rows = select_even_rows(int(source.out_features), count, device)
                groups = build_selected_groups(packed, selected_rows)
                source_weight_selected = source.weight.index_select(0, selected_rows).contiguous()
                bias_selected = source.bias.index_select(0, selected_rows).contiguous() if source.bias is not None else None
                with torch.inference_mode():
                    dense_selected_out = F.linear(x, source_weight_selected, bias_selected)
                dense_selected_ms = time_ms(lambda: F.linear(x, source_weight_selected, bias_selected), args.warmup, args.iters)
                for block_m, block_n, block_k in block_configs:
                    record = {
                        "ok": False,
                        "model": args.model,
                        "module": name,
                        "bits": int(item.get("bits", 0)),
                        "rows": int(item.get("rows", 0)),
                        "cols": int(item.get("cols", 0)),
                        "batch": int(batch),
                        "selected_rows": int(selected_rows.numel()),
                        "low_rows": int(groups["low_slots"].numel()),
                        "high_rows": int(groups["high_slots"].numel()),
                        "block_m": int(block_m),
                        "block_n": int(block_n),
                        "block_k": int(block_k),
                        "dense_full_ms": dense_full_ms,
                        "dense_selected_ms": dense_selected_ms,
                    }
                    try:
                        with torch.inference_mode():
                            latency = time_ms(
                                lambda: triton_selected_forward(packed, x, selected_rows, groups, block_m, block_n, block_k),
                                args.warmup,
                                args.iters,
                            )
                            out = triton_selected_forward(packed, x, selected_rows, groups, block_m, block_n, block_k)
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
        "block_configs": [f"{m}x{n}x{k}" for m, n, k in block_configs],
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
