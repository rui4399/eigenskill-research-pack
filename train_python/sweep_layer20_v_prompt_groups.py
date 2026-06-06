#!/usr/bin/env python3
from __future__ import annotations

"""Prompt-suite ablation sweep for layer-20 V row-group precision guards."""

import argparse
import csv
import itertools
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from eval_esmp_module_reconstruction import DEFAULT_MODEL, repo_root, resolve_path


DEFAULT_BASE_SUMMARY = "outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers017_qkv8_guard/pack_summary.json"
DEFAULT_OUT_DIR = "outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sweep"
DEFAULT_MODULE = "model.layers.20.self_attn.v_proj"


def parse_groups(text: str, rows: int, group_size: int) -> list[int]:
    if text.strip().lower() in ("", "all"):
        return list(range((rows + group_size - 1) // group_size))
    groups = []
    for part in text.replace(";", ",").split(","):
        part = part.strip()
        if part:
            groups.append(int(part))
    if not groups:
        raise ValueError("no groups selected")
    return sorted(dict.fromkeys(groups))


def parse_group_combos(text: str, rows: int, group_size: int) -> list[tuple[int, ...]]:
    combos: list[tuple[int, ...]] = []
    max_group = (rows + group_size - 1) // group_size
    for part in text.replace(";", ",").split(","):
        part = part.strip()
        if not part:
            continue
        combo = tuple(sorted(dict.fromkeys(int(item.strip()) for item in part.replace("+", ":").split(":") if item.strip())))
        if not combo:
            continue
        for group in combo:
            if group < 0 or group >= max_group:
                raise ValueError(f"group {group} out of range for rows={rows}, group_size={group_size}")
        combos.append(combo)
    if not combos:
        raise ValueError("no group combinations selected")
    return sorted(dict.fromkeys(combos))


def run_checked(cmd: list[str], cwd: Path) -> None:
    print(json.dumps({"running": cmd}, ensure_ascii=False), flush=True)
    subprocess.run(cmd, cwd=str(cwd), check=True)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        "# Layer-20 V Prompt-Conditioned Row-Group Sweep",
        "",
        f"Date: `{result['date']}`",
        f"Model: `{result['model']}`",
        f"Base summary: `{result['base_summary']}`",
        f"Module: `{result['module']}`",
        f"Layers evaluated: `{result['layers']}`",
        f"Group size: `{result['group_size']}`",
        f"Prompt file: `{result['prompt_file'] or 'default'}`",
        "",
        "## Results",
        "",
        "| group(s) | rows | exact | edit | prefix | speed | package compression | guard peak MiB |",
        "|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in result["results"]:
        row_ranges = row.get("row_ranges", f"{row['start']}:{row['end']}")
        lines.append(
            f"| {row['group']} | `{row_ranges}` | {row['exact_matches']} / {row['prompts']} | "
            f"{row['mean_char_edit_similarity']:.4f} | {row['mean_common_prefix_ratio']:.4f} | "
            f"{row['mean_speedup_fused_vs_baseline']:.4f}x | {row['package_compression_vs_fp32']:.4f}x | "
            f"{row['guard_peak_mib']} |"
        )
    best_exact = max(result["results"], key=lambda item: (item["exact_matches"], item["mean_common_prefix_ratio"]))
    best_prefix = max(result["results"], key=lambda item: item["mean_common_prefix_ratio"])
    best_exact_rows = best_exact.get("row_ranges", f"{best_exact['start']}:{best_exact['end']}")
    best_prefix_rows = best_prefix.get("row_ranges", f"{best_prefix['start']}:{best_prefix['end']}")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            f"- Best exact/prefix candidate: group(s) `{best_exact['group']}` rows `{best_exact_rows}` with `{best_exact['exact_matches']}/{best_exact['prompts']}` exact and prefix `{best_exact['mean_common_prefix_ratio']:.4f}`.",
            f"- Highest prefix candidate: group(s) `{best_prefix['group']}` rows `{best_prefix_rows}` with prefix `{best_prefix['mean_common_prefix_ratio']:.4f}`.",
            "- This sweep is prompt-conditioned: each row group or group combination is selected by measured generation behavior on the fixed prompt suite, not by local reconstruction error alone.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sweep layer-20 V row-group guards through the prompt suite.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--base-summary", default=DEFAULT_BASE_SUMMARY)
    parser.add_argument("--module", default=DEFAULT_MODULE)
    parser.add_argument("--rows", type=int, default=1024)
    parser.add_argument("--group-size", type=int, default=128)
    parser.add_argument("--groups", default="all")
    parser.add_argument("--combo-size", type=int, default=1, help="Generate combinations of this size from --groups.")
    parser.add_argument("--group-combos", default="", help="Explicit combos such as 0+4,0+4+6; overrides --combo-size.")
    parser.add_argument("--layers", default="1,7,20")
    parser.add_argument("--suffixes", default="q_proj,k_proj,v_proj")
    parser.add_argument("--prompt-file", default="", help="Optional prompt file passed to eval_fused_qkv_prompt_suite.py.")
    parser.add_argument("--max-new-tokens", type=int, default=32)
    parser.add_argument("--warmup-runs", type=int, default=1)
    parser.add_argument("--block-m", type=int, default=32)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=64)
    parser.add_argument("--sync-mode", choices=["per_call", "end"], default="end")
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--out-dir", default=DEFAULT_OUT_DIR)
    parser.add_argument("--rerun", action="store_true")
    args = parser.parse_args()

    root = repo_root()
    out_dir = resolve_path(args.out_dir, root)
    out_dir.mkdir(parents=True, exist_ok=True)
    if args.group_combos.strip():
        combos = parse_group_combos(args.group_combos, args.rows, args.group_size)
    else:
        groups = parse_groups(args.groups, args.rows, args.group_size)
        if args.combo_size <= 0:
            raise SystemExit("--combo-size must be positive")
        if args.combo_size > len(groups):
            raise SystemExit(f"--combo-size {args.combo_size} exceeds selected group count {len(groups)}")
        combos = [tuple(combo) for combo in itertools.combinations(groups, args.combo_size)]
    python = "python3"

    rows: list[dict[str, Any]] = []
    for combo in combos:
        ranges: list[tuple[int, int]] = []
        for group in combo:
            start = group * args.group_size
            end = min(start + args.group_size, args.rows)
            if start >= args.rows:
                raise SystemExit(f"group {group} out of range for rows={args.rows}")
            ranges.append((start, end))
        group_label = "+".join(str(group) for group in combo)
        file_label = f"group_{group_label}" if len(combo) == 1 else f"groups_{group_label.replace('+', '_')}"
        row_ranges = ",".join(f"{start}:{end}" for start, end in ranges)
        row_overrides = ";".join(f"{args.module}:{start}:{end}=8" for start, end in ranges)
        package_dir = out_dir / f"{file_label}_8bit_package"
        repack_guard = out_dir / f"{file_label}_repack_gpu_guard.json"
        eval_json = out_dir / f"{file_label}_prompt_suite.json"
        eval_md = out_dir / f"{file_label.upper()}_PROMPT_SUITE.md"
        eval_guard = out_dir / f"{file_label}_prompt_suite_gpu_guard.json"
        if args.rerun or not (package_dir / "pack_summary.json").exists():
            repack_cmd = [
                python,
                "train_python/run_with_gpu_guard.py",
                "--max-memory-ratio",
                str(args.max_memory_ratio),
                "--out",
                str(repack_guard),
                python,
                "train_python/repack_qkv_precision_guard.py",
                "--model",
                args.model,
                "--base-summary",
                args.base_summary,
                "--row-overrides",
                row_overrides,
                "--out-dir",
                str(package_dir),
                "--verify",
            ]
            if args.local_files_only:
                repack_cmd.append("--local-files-only")
            run_checked(repack_cmd, root)
        if args.rerun or not eval_json.exists():
            eval_cmd = [
                python,
                "train_python/run_with_gpu_guard.py",
                "--max-memory-ratio",
                str(args.max_memory_ratio),
                "--out",
                str(eval_guard),
                python,
                "train_python/eval_fused_qkv_prompt_suite.py",
                "--model",
                args.model,
                "--package-summary",
                str(package_dir / "pack_summary.json"),
                "--layers",
                args.layers,
                "--suffixes",
                args.suffixes,
                "--max-new-tokens",
                str(args.max_new_tokens),
                "--warmup-runs",
                str(args.warmup_runs),
                "--block-m",
                str(args.block_m),
                "--block-n",
                str(args.block_n),
                "--block-k",
                str(args.block_k),
                "--sync-mode",
                args.sync_mode,
                "--out-json",
                str(eval_json),
                "--out-md",
                str(eval_md),
            ]
            if args.prompt_file:
                eval_cmd.extend(["--prompt-file", args.prompt_file])
            if args.local_files_only:
                eval_cmd.append("--local-files-only")
            run_checked(eval_cmd, root)

        summary = load_json(package_dir / "pack_summary.json")
        eval_result = load_json(eval_json)
        guard = load_json(eval_guard) if eval_guard.exists() else {}
        agg = eval_result["aggregate"]
        rows.append(
            {
                "group": group_label,
                "groups": ",".join(str(group) for group in combo),
                "row_ranges": row_ranges,
                "start": ranges[0][0],
                "end": ranges[-1][1],
                "prompts": int(agg["prompts"]),
                "exact_matches": int(agg["exact_matches"]),
                "exact_match_rate": float(agg["exact_match_rate"]),
                "mean_char_edit_similarity": float(agg["mean_char_edit_similarity"]),
                "mean_common_prefix_ratio": float(agg["mean_common_prefix_ratio"]),
                "mean_speedup_fused_vs_baseline": float(agg["mean_speedup_fused_vs_baseline"]),
                "package_compression_vs_fp32": float(summary["compression_ratio_vs_fp32"]),
                "guard_peak_mib": int(guard.get("max_memory_used_mib", 0)),
                "package_summary": str(package_dir / "pack_summary.json"),
                "eval_json": str(eval_json),
            }
        )

    result = {
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "model": args.model,
        "base_summary": args.base_summary,
        "module": args.module,
        "layers": args.layers,
        "suffixes": args.suffixes,
        "group_size": int(args.group_size),
        "prompt_file": args.prompt_file,
        "results": rows,
    }
    out_json = out_dir / "layer20_v_prompt_group_sweep.json"
    out_csv = out_dir / "layer20_v_prompt_group_sweep.csv"
    out_md = out_dir / "LAYER20_V_PROMPT_GROUP_SWEEP.md"
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with out_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)
    write_markdown(out_md, result)
    print(json.dumps({"out_json": str(out_json), "out_csv": str(out_csv), "out_md": str(out_md), "results": rows}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
