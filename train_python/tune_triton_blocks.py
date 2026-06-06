#!/usr/bin/env python3
from __future__ import annotations

"""Tune Triton block sizes for the prototype mixed INT4/INT8 GEMM."""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


def run(command: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(command, text=True, encoding="utf-8", errors="replace", capture_output=True)
    return proc.returncode, proc.stdout, proc.stderr


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def fmt(value: Any, digits: int = 4) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def write_report(path: Path, rows: list[dict[str, Any]]) -> None:
    valid = [row for row in rows if row.get("returncode") == 0 and row.get("grouped_mixed_ms")]
    by_fp16 = sorted(valid, key=lambda row: row.get("grouped_speedup_vs_torch_fp16") or -1.0, reverse=True)
    by_rowwise = sorted(valid, key=lambda row: row.get("grouped_speedup_vs_rowwise") or -1.0, reverse=True)

    lines = [
        "# Triton Block Tuning Summary",
        "",
        "Speedups below 1.0 mean the grouped low-bit kernel is slower than the baseline.",
        "",
        "## Best By Torch FP16 Speedup",
        "",
        "| rank | rows | cols | batch | high_every | BM | BN | BK | grouped ms | torch FP16 ms | grouped/FP16 | grouped/rowwise | rel-L2 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for rank, row in enumerate(by_fp16[:10], start=1):
        lines.append(
            "| {rank} | {rows} | {cols} | {batch} | {high_every} | {bm} | {bn} | {bk} | {gms} | {fms} | {gfp16} | {grow} | {rel} |".format(
                rank=rank,
                rows=row.get("rows"),
                cols=row.get("cols"),
                batch=row.get("batch"),
                high_every=row.get("high_every"),
                bm=row.get("block_m"),
                bn=row.get("block_n"),
                bk=row.get("block_k"),
                gms=fmt(row.get("grouped_mixed_ms"), 6),
                fms=fmt(row.get("torch_fp16_ms"), 6),
                gfp16=fmt(row.get("grouped_speedup_vs_torch_fp16")),
                grow=fmt(row.get("grouped_speedup_vs_rowwise")),
                rel=fmt(row.get("grouped_rel_l2")),
            )
        )

    lines.extend(
        [
            "",
            "## Best By Rowwise Speedup",
            "",
            "| rank | rows | cols | batch | high_every | BM | BN | BK | rowwise ms | grouped ms | grouped/rowwise | grouped/FP16 |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for rank, row in enumerate(by_rowwise[:10], start=1):
        lines.append(
            "| {rank} | {rows} | {cols} | {batch} | {high_every} | {bm} | {bn} | {bk} | {rms} | {gms} | {grow} | {gfp16} |".format(
                rank=rank,
                rows=row.get("rows"),
                cols=row.get("cols"),
                batch=row.get("batch"),
                high_every=row.get("high_every"),
                bm=row.get("block_m"),
                bn=row.get("block_n"),
                bk=row.get("block_k"),
                rms=fmt(row.get("rowwise_mixed_ms"), 6),
                gms=fmt(row.get("grouped_mixed_ms"), 6),
                grow=fmt(row.get("grouped_speedup_vs_rowwise")),
                gfp16=fmt(row.get("grouped_speedup_vs_torch_fp16")),
            )
        )

    failures = [row for row in rows if row.get("returncode") != 0]
    if failures:
        lines.extend(["", "## Failures", ""])
        for row in failures:
            lines.append(
                f"- rows={row.get('rows')} cols={row.get('cols')} batch={row.get('batch')} high_every={row.get('high_every')} "
                f"BM/BN/BK={row.get('block_m')}/{row.get('block_n')}/{row.get('block_k')} rc={row.get('returncode')}"
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Tune Triton mixed GEMM block sizes.")
    parser.add_argument("--out-dir", type=Path, default=Path("outputs/real_system_packer_2026-06-05/triton_tuning"))
    parser.add_argument("--triton-script", type=Path, default=Path("train_python/triton_mixed_gemm.py"))
    parser.add_argument("--gpu-guard", type=Path, default=Path("train_python/run_with_gpu_guard.py"))
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--iters", type=int, default=60)
    parser.add_argument("--warmup", type=int, default=15)
    parser.add_argument("--rows", type=int, default=2048)
    parser.add_argument("--cols", type=int, default=1024)
    parser.add_argument("--batches", default="1,8,16")
    parser.add_argument("--high-every", default="8,16")
    parser.add_argument("--block-ms", default="16,32")
    parser.add_argument("--block-ns", default="8,16,32")
    parser.add_argument("--block-ks", default="64,128")
    args = parser.parse_args()

    def ints(csv: str) -> list[int]:
        return [int(item.strip()) for item in csv.split(",") if item.strip()]

    args.out_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for batch in ints(args.batches):
        for high_every in ints(args.high_every):
            for block_m in ints(args.block_ms):
                for block_n in ints(args.block_ns):
                    for block_k in ints(args.block_ks):
                        stem = f"tune_{args.rows}x{args.cols}_b{batch}_h{high_every}_bm{block_m}_bn{block_n}_bk{block_k}"
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
                            str(args.rows),
                            "--cols",
                            str(args.cols),
                            "--batch",
                            str(batch),
                            "--high-every",
                            str(high_every),
                            "--iters",
                            str(args.iters),
                            "--warmup",
                            str(args.warmup),
                            "--block-m",
                            str(block_m),
                            "--block-n",
                            str(block_n),
                            "--block-k",
                            str(block_k),
                            "--out",
                            str(result_path),
                        ]
                        code, stdout, stderr = run(command)
                        row: dict[str, Any] = {
                            "returncode": code,
                            "rows": args.rows,
                            "cols": args.cols,
                            "batch": batch,
                            "high_every": high_every,
                            "block_m": block_m,
                            "block_n": block_n,
                            "block_k": block_k,
                            "result_path": str(result_path),
                            "guard_path": str(guard_path),
                            "stdout_tail": stdout[-1200:],
                            "stderr_tail": stderr[-1200:],
                        }
                        if result_path.exists():
                            row.update(read_json(result_path))
                        if guard_path.exists():
                            guard = read_json(guard_path)
                            row["guard_killed"] = guard.get("killed_by_guard")
                            row["guard_max_memory_used_mib"] = guard.get("max_memory_used_mib")
                            row["guard_max_memory_used_ratio"] = guard.get("max_memory_used_ratio")
                        rows.append(row)
                        write_jsonl(args.out_dir / "tuning_results.jsonl", rows)
                        if code != 0:
                            write_report(args.out_dir / "TRITON_BLOCK_TUNING_SUMMARY.md", rows)
                            raise SystemExit(code)

    write_report(args.out_dir / "TRITON_BLOCK_TUNING_SUMMARY.md", rows)
    summary = {
        "ok": True,
        "result_count": len(rows),
        "jsonl": str(args.out_dir / "tuning_results.jsonl"),
        "markdown": str(args.out_dir / "TRITON_BLOCK_TUNING_SUMMARY.md"),
    }
    (args.out_dir / "tuning_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
