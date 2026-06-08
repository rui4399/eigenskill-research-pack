#!/usr/bin/env python3
from __future__ import annotations

"""Materialize a guarded full-MMLU PTQ prefix from an existing shard plan.

The full-MMLU run is intentionally sharded. This helper does not run model
inference; it consumes completed shard summaries from the generated plan,
merges the first N rows per variant, and emits the three paper-facing gates:
task retention, runtime profile, and paired statistics.
"""

import argparse
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_VARIANTS = ("fp16", "autoawq", "gptqmodel")


@dataclass(frozen=True)
class PrefixPaths:
    variant: str
    summary_json: Path
    summary_md: Path
    guard_json: Path


@dataclass(frozen=True)
class PrefixPlan:
    commands: list[list[str]]
    variant_paths: dict[str, PrefixPaths]
    matrix_json: Path
    matrix_md: Path
    runtime_json: Path
    runtime_md: Path
    statistics_json: Path
    statistics_md: Path


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _variant_lookup(plan: dict[str, Any]) -> dict[str, dict[str, Any]]:
    variants = plan.get("variants", [])
    if not isinstance(variants, list):
        raise ValueError("plan variants must be a list")
    result: dict[str, dict[str, Any]] = {}
    for variant in variants:
        if not isinstance(variant, dict):
            continue
        name = str(variant.get("variant", ""))
        if name:
            result[name] = variant
    return result


def _selected_shards(variant: dict[str, Any], prefix_rows: int) -> list[dict[str, Any]]:
    shards = variant.get("shards", [])
    if not isinstance(shards, list):
        raise ValueError("variant shards must be a list")
    selected: list[dict[str, Any]] = []
    covered = 0
    for shard in shards:
        if not isinstance(shard, dict):
            continue
        offset = int(shard.get("offset", -1))
        limit = int(shard.get("limit", 0))
        if offset != covered:
            raise ValueError(f"non-contiguous shard offset: {offset} != {covered}")
        if covered + limit > prefix_rows:
            break
        selected.append(shard)
        covered += limit
        if covered == prefix_rows:
            break
    if covered != prefix_rows:
        raise ValueError(f"prefix {prefix_rows} is not exactly covered by completed shard plan")
    return selected


def build_prefix_plan(
    plan: dict[str, Any],
    prefix_rows: int,
    *,
    variants: tuple[str, ...] = DEFAULT_VARIANTS,
    date_tag: str = "2026_06_08",
    max_memory_ratio: float = 0.90,
    max_accuracy_drop: float = 0.15,
    max_ci_accuracy_drop: float = 0.15,
    bootstrap_samples: int = 4000,
) -> PrefixPlan:
    if prefix_rows <= 0:
        raise ValueError("prefix_rows must be positive")
    lookup = _variant_lookup(plan)
    missing = [variant for variant in variants if variant not in lookup]
    if missing:
        raise ValueError(f"missing variants in plan: {missing}")

    commands: list[list[str]] = []
    variant_paths: dict[str, PrefixPaths] = {}

    for variant_name in variants:
        selected = _selected_shards(lookup[variant_name], prefix_rows)
        summary_json = Path(
            f"outputs/shards/official_ptq_task_{variant_name}_"
            f"qwen25_1p5b_mmlu_mmlu_full_prefix{prefix_rows}_{date_tag}.json"
        )
        summary_md = Path(
            f"outputs/OFFICIAL_PTQ_TASK_{variant_name.upper()}_"
            f"QWEN25_1P5B_MMLU_MMLU_FULL_PREFIX{prefix_rows}_{date_tag}.md"
        )
        guard_json = Path(
            f"outputs/shards/official_ptq_task_{variant_name}_"
            f"qwen25_1p5b_mmlu_mmlu_full_prefix{prefix_rows}_{date_tag}_gpu_guard.json"
        )
        merge_cmd = [
            "python",
            "train_python/merge_chat_task_shards.py",
            "--out-json",
            str(summary_json),
            "--out-md",
            str(summary_md),
            "--out-guard-json",
            str(guard_json),
        ]
        for shard in selected:
            merge_cmd.extend(["--shard", f"{shard['summary_json']}={shard['guard_json']}"])
        commands.append(merge_cmd)
        variant_paths[variant_name] = PrefixPaths(variant_name, summary_json, summary_md, guard_json)

    matrix_json = Path(
        f"outputs/official_ptq_task_qwen25_1p5b_mmlu_full_prefix{prefix_rows}_"
        f"fp16_awq_gptqmodel_matrix_{date_tag}.json"
    )
    matrix_md = Path(
        f"outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_MMLU_FULL_PREFIX{prefix_rows}_"
        f"FP16_AWQ_GPTQMODEL_MATRIX_{date_tag}.md"
    )
    retention_cmd = [
        "python",
        "train_python/gate_official_ptq_task_retention.py",
        "--baseline-variant",
        "fp16",
        "--required-format",
        "mmlu",
        "--min-tasks-per-case",
        str(prefix_rows),
        "--max-memory-ratio",
        f"{max_memory_ratio:.2f}",
        "--max-accuracy-drop",
        f"{max_accuracy_drop:.4f}",
        "--matrix-title",
        f"Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix{prefix_rows} task matrix",
        "--evidence-label",
        f"matched Qwen2.5-1.5B local full-MMLU prefix{prefix_rows} task evidence for FP16, AutoAWQ, and GPTQModel",
        "--out-json",
        str(matrix_json),
        "--out-md",
        str(matrix_md),
    ]
    for variant_name in variants:
        retention_cmd.extend(["--required-variant", variant_name])
    for variant_name in variants:
        paths = variant_paths[variant_name]
        retention_cmd.extend(["--case", f"{variant_name}:mmlu={paths.summary_json}={paths.guard_json}"])
    commands.append(retention_cmd)

    runtime_json = Path(
        f"outputs/official_ptq_qwen25_1p5b_mmlu_full_prefix{prefix_rows}_"
        f"fp16_awq_gptqmodel_runtime_profile_{date_tag}.json"
    )
    runtime_md = Path(
        f"outputs/OFFICIAL_PTQ_QWEN25_1P5B_MMLU_FULL_PREFIX{prefix_rows}_"
        f"FP16_AWQ_GPTQMODEL_RUNTIME_PROFILE_{date_tag}.md"
    )
    runtime_cmd = [
        "python",
        "train_python/gate_official_ptq_runtime_profile.py",
        "--matrix-json",
        str(matrix_json),
        "--baseline-variant",
        "fp16",
        "--min-cases-per-variant",
        "1",
        "--max-memory-ratio",
        f"{max_memory_ratio:.2f}",
        "--out-json",
        str(runtime_json),
        "--out-md",
        str(runtime_md),
    ]
    for variant_name in variants:
        runtime_cmd.extend(["--required-variant", variant_name])
    commands.append(runtime_cmd)

    statistics_json = Path(
        f"outputs/official_ptq_task_qwen25_1p5b_mmlu_full_prefix{prefix_rows}_"
        f"fp16_awq_gptqmodel_statistics_{date_tag}.json"
    )
    statistics_md = Path(
        f"outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_MMLU_FULL_PREFIX{prefix_rows}_"
        f"FP16_AWQ_GPTQMODEL_STATISTICS_{date_tag}.md"
    )
    statistics_cmd = [
        "python",
        "train_python/gate_official_ptq_task_statistics.py",
        "--baseline-variant",
        "fp16",
        "--min-tasks-per-case",
        str(prefix_rows),
        "--min-shared-tasks",
        str(prefix_rows),
        "--max-ci-accuracy-drop",
        f"{max_ci_accuracy_drop:.4f}",
        "--bootstrap-samples",
        str(bootstrap_samples),
        "--matrix-title",
        f"Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix{prefix_rows} task statistics",
        "--out-json",
        str(statistics_json),
        "--out-md",
        str(statistics_md),
    ]
    for variant_name in variants:
        paths = variant_paths[variant_name]
        statistics_cmd.extend(["--case", f"{variant_name}:mmlu={paths.summary_json}"])
    commands.append(statistics_cmd)

    return PrefixPlan(
        commands=commands,
        variant_paths=variant_paths,
        matrix_json=matrix_json,
        matrix_md=matrix_md,
        runtime_json=runtime_json,
        runtime_md=runtime_md,
        statistics_json=statistics_json,
        statistics_md=statistics_md,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Materialize full-MMLU PTQ prefix gates.")
    parser.add_argument("--plan-json", type=Path, default=Path("outputs/mmlu_ptq_shard_plan_mmlu_full_2026_06_08.json"))
    parser.add_argument("--prefix-rows", type=int, required=True)
    parser.add_argument("--date-tag", default="2026_06_08")
    parser.add_argument("--variant", action="append", default=None)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--max-accuracy-drop", type=float, default=0.15)
    parser.add_argument("--max-ci-accuracy-drop", type=float, default=0.15)
    parser.add_argument("--bootstrap-samples", type=int, default=4000)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    variants = tuple(args.variant) if args.variant else DEFAULT_VARIANTS
    prefix_plan = build_prefix_plan(
        load_json(args.plan_json),
        args.prefix_rows,
        variants=variants,
        date_tag=args.date_tag,
        max_memory_ratio=args.max_memory_ratio,
        max_accuracy_drop=args.max_accuracy_drop,
        max_ci_accuracy_drop=args.max_ci_accuracy_drop,
        bootstrap_samples=args.bootstrap_samples,
    )
    if args.dry_run:
        print(json.dumps({"commands": prefix_plan.commands}, indent=2, ensure_ascii=False))
        return
    for command in prefix_plan.commands:
        subprocess.run(command, check=True)
    print(
        json.dumps(
            {
                "prefix_rows": args.prefix_rows,
                "matrix_md": str(prefix_plan.matrix_md),
                "runtime_md": str(prefix_plan.runtime_md),
                "statistics_md": str(prefix_plan.statistics_md),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
