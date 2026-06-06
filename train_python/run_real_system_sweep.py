#!/usr/bin/env python3
from __future__ import annotations

"""Run reproducible real-system sweeps for EigenSkill-Q artifacts.

The script keeps the raw command outputs as JSON and also writes compact JSONL
and Markdown summaries. It is intentionally small: no hidden framework, no
silent retries, and no claims beyond the measured numbers.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


TRITON_CONFIGS = [
    {"rows": 2048, "cols": 1024, "batch": 1, "high_every": 16},
    {"rows": 2048, "cols": 1024, "batch": 4, "high_every": 16},
    {"rows": 2048, "cols": 1024, "batch": 16, "high_every": 16},
    {"rows": 2048, "cols": 1024, "batch": 16, "high_every": 8},
    {"rows": 3072, "cols": 1024, "batch": 8, "high_every": 16},
    {"rows": 1024, "cols": 3072, "batch": 8, "high_every": 16},
]

CPU_MODULE_PATTERNS = [
    "model__layers__0__self_attn__q_proj.esmp",
    "model__layers__0__self_attn__v_proj.esmp",
    "model__layers__0__mlp__gate_proj.esmp",
    "model__layers__0__mlp__down_proj.esmp",
    "model__layers__10__self_attn__q_proj.esmp",
    "model__layers__10__mlp__gate_proj.esmp",
]


def run_command(command: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(command, text=True, encoding="utf-8", errors="replace", capture_output=True)
    return proc.returncode, proc.stdout, proc.stderr


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def scalar(value: Any, digits: int = 4) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def write_markdown(path: Path, triton_rows: list[dict[str, Any]], cpu_rows: list[dict[str, Any]]) -> None:
    lines = [
        "# Real-System Sweep Summary",
        "",
        "All rows are produced by local scripts on the current machine. Speedups below 1.0 mean the low-bit path is slower than the baseline.",
        "",
        "## Triton GPU Mixed GEMM",
        "",
        "| rows | cols | batch | high_every | compression vs FP16 | rowwise ms | grouped ms | torch FP16 ms | grouped/FP16 | grouped/rowwise | grouped rel-L2 | max VRAM MiB |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in triton_rows:
        lines.append(
            "| {rows} | {cols} | {batch} | {high_every} | {comp} | {row_ms} | {grp_ms} | {fp16_ms} | {grp_spd} | {grp_row_spd} | {rel} | {vram} |".format(
                rows=row.get("rows"),
                cols=row.get("cols"),
                batch=row.get("batch"),
                high_every=row.get("high_every"),
                comp=scalar(row.get("compression_ratio_vs_fp16")),
                row_ms=scalar(row.get("rowwise_mixed_ms"), 6),
                grp_ms=scalar(row.get("grouped_mixed_ms"), 6),
                fp16_ms=scalar(row.get("torch_fp16_ms"), 6),
                grp_spd=scalar(row.get("grouped_speedup_vs_torch_fp16")),
                grp_row_spd=scalar(row.get("grouped_speedup_vs_rowwise")),
                rel=scalar(row.get("grouped_rel_l2")),
                vram=scalar(row.get("guard_max_memory_used_mib"), 0),
            )
        )

    lines.extend(
        [
            "",
            "## C++ ESMP Runtime",
            "",
            "| module file | rows | cols | avg bits | compression vs FP32 | full ms | active rows | selected ms |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in cpu_rows:
        lines.append(
            "| {name} | {rows} | {cols} | {bits} | {comp} | {full_ms} | {active_rows} | {selected_ms} |".format(
                name=Path(str(row.get("input", ""))).name,
                rows=row.get("rows"),
                cols=row.get("cols"),
                bits=scalar(row.get("avg_bits")),
                comp=scalar(row.get("compression_ratio_vs_fp32")),
                full_ms=scalar(row.get("full_mixed_gemv_ms"), 6),
                active_rows=row.get("active_rows"),
                selected_ms=scalar(row.get("selected_mixed_gemv_ms"), 6),
            )
        )

    lines.extend(
        [
            "",
            "## Interpretation Guardrails",
            "",
            "- Triton grouped kernels measure packed-storage execution, but are still prototype kernels, not fused transformer runtime.",
            "- ESMP C++ runtime numbers are CPU module-level GEMV numbers, not end-to-end LLM token latency.",
            "- These results are valid evidence for systems bottleneck analysis and follow-up kernel design, not yet a SOTA quantization claim.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_triton_sweep(args: argparse.Namespace) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for cfg in TRITON_CONFIGS:
        stem = f"triton_mixed_gemm_{cfg['rows']}x{cfg['cols']}_b{cfg['batch']}_h{cfg['high_every']}"
        result_path = args.out_dir / f"{stem}.json"
        guard_path = args.out_dir / f"{stem}_guard.json"
        command = [
            sys.executable,
            str(args.gpu_guard),
            "--max-memory-ratio",
            str(args.max_memory_ratio),
            "--poll-seconds",
            "1",
            "--out",
            str(guard_path),
            "--",
            sys.executable,
            str(args.triton_script),
            "--rows",
            str(cfg["rows"]),
            "--cols",
            str(cfg["cols"]),
            "--batch",
            str(cfg["batch"]),
            "--high-every",
            str(cfg["high_every"]),
            "--iters",
            str(args.triton_iters),
            "--warmup",
            str(args.triton_warmup),
            "--block-m",
            str(args.block_m),
            "--block-n",
            str(args.block_n),
            "--block-k",
            str(args.block_k),
            "--out",
            str(result_path),
        ]
        code, stdout, stderr = run_command(command)
        row = {
            "kind": "triton",
            "config": cfg,
            "returncode": code,
            "stdout_tail": stdout[-2000:],
            "stderr_tail": stderr[-2000:],
            "result_path": str(result_path),
            "guard_path": str(guard_path),
        }
        if result_path.exists():
            row.update(read_json(result_path))
        if guard_path.exists():
            guard = read_json(guard_path)
            row["guard_killed"] = guard.get("killed_by_guard")
            row["guard_max_memory_used_mib"] = guard.get("max_memory_used_mib")
            row["guard_max_memory_used_ratio"] = guard.get("max_memory_used_ratio")
            row["guard_max_utilization_gpu_pct"] = guard.get("max_utilization_gpu_pct")
        rows.append(row)
        if code != 0:
            break
    return rows


def run_cpu_sweep(args: argparse.Namespace) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for pattern in CPU_MODULE_PATTERNS:
        input_path = args.esmp_dir / pattern
        if not input_path.exists():
            rows.append({"kind": "cpu_esmp", "input": str(input_path), "returncode": -1, "error": "missing input"})
            continue
        command = [
            str(args.runtime_bench),
            "--input",
            str(input_path),
            "--iters",
            str(args.cpu_iters),
            "--warmup",
            str(args.cpu_warmup),
            "--active-rows",
            str(args.active_rows),
        ]
        code, stdout, stderr = run_command(command)
        row: dict[str, Any] = {
            "kind": "cpu_esmp",
            "input": str(input_path),
            "returncode": code,
            "stderr_tail": stderr[-2000:],
        }
        try:
            row.update(json.loads(stdout))
        except json.JSONDecodeError:
            row["stdout_tail"] = stdout[-2000:]
        rows.append(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Run real-system EigenSkill-Q sweep.")
    parser.add_argument("--out-dir", type=Path, default=Path("outputs/real_system_packer_2026-06-05/sweeps"))
    parser.add_argument("--triton-script", type=Path, default=Path("train_python/triton_mixed_gemm.py"))
    parser.add_argument("--gpu-guard", type=Path, default=Path("train_python/run_with_gpu_guard.py"))
    parser.add_argument("--runtime-bench", type=Path, default=Path("build/cpp-wsl/mixed_precision_runtime_bench"))
    parser.add_argument("--esmp-dir", type=Path, default=Path("outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp"))
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--triton-iters", type=int, default=80)
    parser.add_argument("--triton-warmup", type=int, default=20)
    parser.add_argument("--block-m", type=int, default=16)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=64)
    parser.add_argument("--cpu-iters", type=int, default=200)
    parser.add_argument("--cpu-warmup", type=int, default=20)
    parser.add_argument("--active-rows", type=int, default=64)
    parser.add_argument("--skip-triton", action="store_true")
    parser.add_argument("--skip-cpu", action="store_true")
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    triton_rows = [] if args.skip_triton else run_triton_sweep(args)
    cpu_rows = [] if args.skip_cpu else run_cpu_sweep(args)
    write_jsonl(args.out_dir / "triton_sweep.jsonl", triton_rows)
    write_jsonl(args.out_dir / "cpu_esmp_sweep.jsonl", cpu_rows)
    summary = {
        "ok": all(row.get("returncode") == 0 for row in triton_rows + cpu_rows),
        "triton_count": len(triton_rows),
        "cpu_count": len(cpu_rows),
        "triton_jsonl": str(args.out_dir / "triton_sweep.jsonl"),
        "cpu_jsonl": str(args.out_dir / "cpu_esmp_sweep.jsonl"),
        "markdown": str(args.out_dir / "REAL_SYSTEM_SWEEP_SUMMARY.md"),
    }
    (args.out_dir / "sweep_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_dir / "REAL_SYSTEM_SWEEP_SUMMARY.md", triton_rows, cpu_rows)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    raise SystemExit(0 if summary["ok"] else 2)


if __name__ == "__main__":
    main()
