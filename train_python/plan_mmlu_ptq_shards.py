#!/usr/bin/env python3
from __future__ import annotations

"""Plan guarded MMLU shard runs for matched FP16/AutoAWQ/GPTQModel PTQ rows.

This script does not run inference. It writes a reproducible command plan that
turns a broad/full MMLU fixture into guarded shard evaluations, per-variant
merges, and the three paper-facing gates: task retention, runtime, and paired
statistics.
"""

import argparse
import json
import shlex
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


MMLU_SUBJECTS: tuple[str, ...] = (
    "abstract_algebra",
    "anatomy",
    "astronomy",
    "business_ethics",
    "clinical_knowledge",
    "college_biology",
    "college_chemistry",
    "college_computer_science",
    "college_mathematics",
    "college_medicine",
    "college_physics",
    "computer_security",
    "conceptual_physics",
    "econometrics",
    "electrical_engineering",
    "elementary_mathematics",
    "formal_logic",
    "global_facts",
    "high_school_biology",
    "high_school_chemistry",
    "high_school_computer_science",
    "high_school_european_history",
    "high_school_geography",
    "high_school_government_and_politics",
    "high_school_macroeconomics",
    "high_school_mathematics",
    "high_school_microeconomics",
    "high_school_physics",
    "high_school_psychology",
    "high_school_statistics",
    "high_school_us_history",
    "high_school_world_history",
    "human_aging",
    "human_sexuality",
    "international_law",
    "jurisprudence",
    "logical_fallacies",
    "machine_learning",
    "management",
    "marketing",
    "medical_genetics",
    "miscellaneous",
    "moral_disputes",
    "moral_scenarios",
    "nutrition",
    "philosophy",
    "prehistory",
    "professional_accounting",
    "professional_law",
    "professional_medicine",
    "professional_psychology",
    "public_relations",
    "security_studies",
    "sociology",
    "us_foreign_policy",
    "virology",
    "world_religions",
)

MMLU_TEST_ROWS: dict[str, int] = {
    "abstract_algebra": 100,
    "anatomy": 135,
    "astronomy": 152,
    "business_ethics": 100,
    "clinical_knowledge": 265,
    "college_biology": 144,
    "college_chemistry": 100,
    "college_computer_science": 100,
    "college_mathematics": 100,
    "college_medicine": 173,
    "college_physics": 102,
    "computer_security": 100,
    "conceptual_physics": 235,
    "econometrics": 114,
    "electrical_engineering": 145,
    "elementary_mathematics": 378,
    "formal_logic": 126,
    "global_facts": 100,
    "high_school_biology": 310,
    "high_school_chemistry": 203,
    "high_school_computer_science": 100,
    "high_school_european_history": 165,
    "high_school_geography": 198,
    "high_school_government_and_politics": 193,
    "high_school_macroeconomics": 390,
    "high_school_mathematics": 270,
    "high_school_microeconomics": 238,
    "high_school_physics": 151,
    "high_school_psychology": 545,
    "high_school_statistics": 216,
    "high_school_us_history": 204,
    "high_school_world_history": 237,
    "human_aging": 223,
    "human_sexuality": 131,
    "international_law": 121,
    "jurisprudence": 108,
    "logical_fallacies": 163,
    "machine_learning": 112,
    "management": 103,
    "marketing": 234,
    "medical_genetics": 100,
    "miscellaneous": 783,
    "moral_disputes": 346,
    "moral_scenarios": 895,
    "nutrition": 306,
    "philosophy": 311,
    "prehistory": 324,
    "professional_accounting": 282,
    "professional_law": 1534,
    "professional_medicine": 272,
    "professional_psychology": 612,
    "public_relations": 110,
    "security_studies": 245,
    "sociology": 201,
    "us_foreign_policy": 100,
    "virology": 166,
    "world_religions": 171,
}

BROAD10_SUBJECTS: tuple[str, ...] = (
    "abstract_algebra",
    "anatomy",
    "business_ethics",
    "clinical_knowledge",
    "college_computer_science",
    "computer_security",
    "high_school_mathematics",
    "high_school_us_history",
    "machine_learning",
    "professional_law",
)

BROAD20_SUBJECTS: tuple[str, ...] = BROAD10_SUBJECTS + (
    "astronomy",
    "college_biology",
    "college_chemistry",
    "college_mathematics",
    "college_medicine",
    "conceptual_physics",
    "econometrics",
    "electrical_engineering",
    "formal_logic",
    "global_facts",
)


@dataclass(frozen=True)
class VariantSpec:
    name: str
    loader: str
    model: str
    extra_args: tuple[str, ...] = ()


DEFAULT_VARIANTS: tuple[VariantSpec, ...] = (
    VariantSpec(
        "fp16",
        "hf",
        "Qwen/Qwen2.5-1.5B-Instruct",
        ("--hf-device-map", "auto", "--hf-max-gpu-memory-mib", "2400"),
    ),
    VariantSpec("autoawq", "autoawq", "/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07"),
    VariantSpec("gptqmodel", "gptqmodel", "/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08"),
)


def shell_join(parts: list[str]) -> str:
    return shlex.join([str(part) for part in parts])


def normalize_suite(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "_" for ch in value.strip())
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    cleaned = cleaned.strip("_")
    if not cleaned:
        raise ValueError("suite name must not be empty")
    return cleaned


def select_subjects(preset: str, explicit_subjects: list[str]) -> tuple[str, ...]:
    if explicit_subjects:
        subjects = tuple(dict.fromkeys(subject.strip() for subject in explicit_subjects if subject.strip()))
    elif preset == "broad10":
        subjects = BROAD10_SUBJECTS
    elif preset == "broad20":
        subjects = BROAD20_SUBJECTS
    elif preset == "full":
        subjects = MMLU_SUBJECTS
    else:
        raise ValueError(f"unsupported preset: {preset}")
    unknown = [subject for subject in subjects if subject not in MMLU_SUBJECTS]
    if unknown:
        raise ValueError(f"unknown MMLU subjects: {unknown}")
    return subjects


def shard_ranges(total_rows: int, shard_size: int) -> list[tuple[int, int]]:
    if total_rows <= 0:
        raise ValueError("total_rows must be positive")
    if shard_size <= 0:
        raise ValueError("shard_size must be positive")
    ranges: list[tuple[int, int]] = []
    for offset in range(0, total_rows, shard_size):
        limit = min(shard_size, total_rows - offset)
        ranges.append((offset, limit))
    return ranges


def subject_row_counts(subjects: tuple[str, ...], rows_per_subject: int, full_test_split: bool) -> dict[str, int]:
    if full_test_split:
        missing = [subject for subject in subjects if subject not in MMLU_TEST_ROWS]
        if missing:
            raise ValueError(f"missing MMLU test row counts for subjects: {missing}")
        return {subject: MMLU_TEST_ROWS[subject] for subject in subjects}
    if rows_per_subject <= 0:
        raise ValueError("rows_per_subject must be positive unless --full-test-split is set")
    return {subject: rows_per_subject for subject in subjects}


def output_paths(suite: str, date_tag: str) -> dict[str, str]:
    upper_suite = suite.upper()
    return {
        "fixture": f"data_eval/public_task_benchmark_v1/mmlu_{suite}_test.jsonl",
        "manifest_json": f"outputs/public_task_benchmark_mmlu_{suite}_manifest_{date_tag}.json",
        "manifest_md": f"outputs/PUBLIC_TASK_BENCHMARK_MMLU_{upper_suite}_MANIFEST_{date_tag}.md",
        "matrix_json": f"outputs/official_ptq_task_qwen25_1p5b_mmlu_{suite}_fp16_awq_gptqmodel_matrix_{date_tag}.json",
        "matrix_md": f"outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_MMLU_{upper_suite}_FP16_AWQ_GPTQMODEL_MATRIX_{date_tag}.md",
        "runtime_json": f"outputs/official_ptq_qwen25_1p5b_mmlu_{suite}_fp16_awq_gptqmodel_runtime_profile_{date_tag}.json",
        "runtime_md": f"outputs/OFFICIAL_PTQ_QWEN25_1P5B_MMLU_{upper_suite}_FP16_AWQ_GPTQMODEL_RUNTIME_PROFILE_{date_tag}.md",
        "statistics_json": f"outputs/official_ptq_task_qwen25_1p5b_mmlu_{suite}_fp16_awq_gptqmodel_statistics_{date_tag}.json",
        "statistics_md": f"outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_MMLU_{upper_suite}_FP16_AWQ_GPTQMODEL_STATISTICS_{date_tag}.md",
    }


def variant_shard_paths(variant: str, suite: str, offset: int, limit: int, date_tag: str) -> dict[str, str]:
    end = offset + limit
    upper_variant = variant.upper()
    upper_suite = suite.upper()
    stem = f"outputs/shards/official_ptq_task_{variant}_qwen25_1p5b_mmlu_{suite}_{offset}_{end}_{date_tag}"
    return {
        "summary_json": f"{stem}.json",
        "summary_md": f"{stem}.md",
        "guard_json": f"{stem}_gpu_guard.json",
        "title": f"{upper_variant} Qwen2.5-1.5B MMLU {upper_suite} shard {offset}-{end}",
    }


def variant_merged_paths(variant: str, suite: str, date_tag: str) -> dict[str, str]:
    upper_variant = variant.upper()
    upper_suite = suite.upper()
    stem = f"outputs/official_ptq_task_{variant}_qwen25_1p5b_mmlu_{suite}_summary_{date_tag}"
    return {
        "summary_json": f"{stem}.json",
        "summary_md": f"outputs/OFFICIAL_PTQ_TASK_{upper_variant}_QWEN25_1P5B_MMLU_{upper_suite}_{date_tag}.md",
        "guard_json": f"{stem}_gpu_guard.json",
    }


def build_fixture_command(
    subjects: tuple[str, ...],
    args: argparse.Namespace,
    paths: dict[str, str],
    row_counts: dict[str, int],
) -> list[str]:
    command = [
        "python3",
        "train_python/build_public_task_smoke.py",
        "--out-dir",
        "data_eval/public_task_benchmark_v1",
        "--gsm8k-count",
        "0",
        "--mmlu-count",
        "0",
        "--mmlu-count-per-subject",
        str(args.rows_per_subject),
        "--file-tag",
        args.suite,
        "--mmlu-combined-file",
        Path(paths["fixture"]).name,
        "--title",
        f"Public Task Benchmark MMLU {args.suite} Manifest",
        "--claim-boundary",
        args.claim_boundary,
        "--source",
        args.source,
        "--out-json",
        paths["manifest_json"],
        "--out-md",
        paths["manifest_md"],
    ]
    for subject in subjects:
        command.extend(["--mmlu-subject", subject])
    if args.full_test_split:
        for subject in subjects:
            command.extend(["--mmlu-subject-count", f"{subject}={row_counts[subject]}"])
    return command


def eval_command_for_shard(variant: VariantSpec, args: argparse.Namespace, paths: dict[str, str], shard: dict[str, Any]) -> list[str]:
    eval_args = [
        "python3",
        "train_python/eval_chat_task_benchmark.py",
        "--tasks-jsonl",
        paths["fixture"],
        "--task-format",
        "mmlu",
        "--model",
        variant.model,
        "--loader",
        variant.loader,
        "--max-new-tokens",
        str(args.max_new_tokens),
        "--limit",
        str(shard["limit"]),
        "--offset",
        str(shard["offset"]),
        "--chat-template",
        "--no-think",
        "--out-json",
        shard["summary_json"],
        "--out-md",
        shard["summary_md"],
    ]
    eval_args.extend(variant.extra_args)
    return [
        "python3",
        "train_python/run_with_gpu_guard.py",
        "--max-memory-ratio",
        f"{args.max_memory_ratio:.2f}",
        "--max-start-memory-ratio",
        f"{args.max_start_memory_ratio:.2f}",
        "--min-disk-free-gb",
        str(args.min_disk_free_gb),
        "--disk-check-path",
        args.disk_check_path,
        "--timeout-sec",
        str(args.timeout_sec),
        "--out",
        shard["guard_json"],
        "--",
        *eval_args,
    ]


def build_plan(args: argparse.Namespace) -> dict[str, Any]:
    args.suite = normalize_suite(args.suite)
    subjects = select_subjects(args.preset, args.mmlu_subject)
    row_counts = subject_row_counts(subjects, args.rows_per_subject, args.full_test_split)
    total_rows = args.total_rows or sum(row_counts.values())
    paths = output_paths(args.suite, args.date_tag)
    variants = DEFAULT_VARIANTS
    ranges = shard_ranges(total_rows, args.shard_size)
    variant_plans: list[dict[str, Any]] = []
    for variant in variants:
        shards: list[dict[str, Any]] = []
        for offset, limit in ranges:
            shard = variant_shard_paths(variant.name, args.suite, offset, limit, args.date_tag)
            shard.update({"offset": offset, "limit": limit, "command": ""})
            shard["command"] = shell_join(eval_command_for_shard(variant, args, paths, shard))
            shards.append(shard)
        merged = variant_merged_paths(variant.name, args.suite, args.date_tag)
        merge_command = [
            "python3",
            "train_python/merge_chat_task_shards.py",
            "--out-json",
            merged["summary_json"],
            "--out-md",
            merged["summary_md"],
            "--out-guard-json",
            merged["guard_json"],
        ]
        for shard in shards:
            merge_command.extend(["--shard", f"{shard['summary_json']}={shard['guard_json']}"])
        variant_plans.append(
            {
                "variant": variant.name,
                "loader": variant.loader,
                "model": variant.model,
                "merged": merged,
                "shards": shards,
                "merge_command": shell_join(merge_command),
            }
        )

    case_specs = [
        f"{plan['variant']}:mmlu={plan['merged']['summary_json']}={plan['merged']['guard_json']}"
        for plan in variant_plans
    ]
    stat_case_specs = [f"{plan['variant']}:mmlu={plan['merged']['summary_json']}" for plan in variant_plans]
    retention_command = [
        "python3",
        "train_python/gate_official_ptq_task_retention.py",
        "--baseline-variant",
        "fp16",
        "--required-variant",
        "fp16",
        "--required-variant",
        "autoawq",
        "--required-variant",
        "gptqmodel",
        "--required-format",
        "mmlu",
        "--min-tasks-per-case",
        str(total_rows),
        "--max-memory-ratio",
        f"{args.max_memory_ratio:.2f}",
        "--max-accuracy-drop",
        f"{args.max_accuracy_drop:.4f}",
        "--matrix-title",
        f"Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel MMLU {args.suite} task matrix",
        "--evidence-label",
        f"matched Qwen2.5-1.5B local MMLU {args.suite} task evidence for FP16, AutoAWQ, and GPTQModel",
        "--out-json",
        paths["matrix_json"],
        "--out-md",
        paths["matrix_md"],
    ]
    for case in case_specs:
        retention_command.extend(["--case", case])

    runtime_command = [
        "python3",
        "train_python/gate_official_ptq_runtime_profile.py",
        "--matrix-json",
        paths["matrix_json"],
        "--baseline-variant",
        "fp16",
        "--required-variant",
        "fp16",
        "--required-variant",
        "autoawq",
        "--required-variant",
        "gptqmodel",
        "--min-cases-per-variant",
        "1",
        "--max-memory-ratio",
        f"{args.max_memory_ratio:.2f}",
        "--out-json",
        paths["runtime_json"],
        "--out-md",
        paths["runtime_md"],
    ]

    statistics_command = [
        "python3",
        "train_python/gate_official_ptq_task_statistics.py",
        "--baseline-variant",
        "fp16",
        "--min-tasks-per-case",
        str(total_rows),
        "--min-shared-tasks",
        str(total_rows),
        "--max-ci-accuracy-drop",
        f"{args.max_ci_accuracy_drop:.4f}",
        "--bootstrap-samples",
        str(args.bootstrap_samples),
        "--matrix-title",
        f"Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel MMLU {args.suite} task statistics",
        "--out-json",
        paths["statistics_json"],
        "--out-md",
        paths["statistics_md"],
    ]
    for case in stat_case_specs:
        statistics_command.extend(["--case", case])

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "suite": args.suite,
        "preset": args.preset,
        "subjects": list(subjects),
        "rows_per_subject": args.rows_per_subject,
        "full_test_split": args.full_test_split,
        "subject_row_counts": row_counts,
        "total_rows_planned": total_rows,
        "shard_size": args.shard_size,
        "paths": paths,
        "fixture_command": shell_join(build_fixture_command(subjects, args, paths, row_counts)),
        "variants": variant_plans,
        "gate_commands": {
            "task_retention": shell_join(retention_command),
            "runtime_profile": shell_join(runtime_command),
            "task_statistics": shell_join(statistics_command),
        },
        "claim_boundary": (
            "This is a command plan only. It proves no model quality until the fixture, shard summaries, "
            "merged summaries, GPU guard logs, and gates are produced and committed."
        ),
    }


def write_markdown(path: Path, plan: dict[str, Any]) -> None:
    lines = [
        f"# MMLU PTQ Shard Plan: {plan['suite']}",
        "",
        f"Date: `{plan['date']}`",
        f"Subjects: `{len(plan['subjects'])}`",
        f"Full test split: `{plan.get('full_test_split', False)}`",
        f"Planned rows: `{plan['total_rows_planned']}`",
        f"Shard size: `{plan['shard_size']}`",
        "",
        "## Claim Boundary",
        "",
        f"- {plan['claim_boundary']}",
        "- Generated commands must still be run under the GPU guard before any paper-facing claim is added.",
        "",
        "## Fixture Command",
        "",
        "```bash",
        plan["fixture_command"],
        "```",
        "",
        "## Variant Shards",
    ]
    for variant in plan["variants"]:
        lines.extend(["", f"### {variant['variant']}", ""])
        for shard in variant["shards"]:
            lines.extend(
                [
                    f"Shard `{shard['offset']}` + `{shard['limit']}`:",
                    "",
                    "```bash",
                    shard["command"],
                    "```",
                    "",
                ]
            )
        lines.extend(["Merge:", "", "```bash", variant["merge_command"], "```"])
    lines.extend(["", "## Gate Commands", ""])
    for name, command in plan["gate_commands"].items():
        lines.extend([f"### {name}", "", "```bash", command, "```", ""])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Plan guarded MMLU PTQ shard commands.")
    parser.add_argument("--suite", default="broad20x20")
    parser.add_argument("--preset", choices=["broad10", "broad20", "full"], default="broad20")
    parser.add_argument("--mmlu-subject", action="append", default=[])
    parser.add_argument("--rows-per-subject", type=int, default=20)
    parser.add_argument("--full-test-split", action="store_true", help="Use static per-subject MMLU test row counts instead of a uniform row limit.")
    parser.add_argument("--total-rows", type=int, default=0, help="Override planned total rows for sharding.")
    parser.add_argument("--shard-size", type=int, default=100)
    parser.add_argument("--date-tag", default="2026_06_08")
    parser.add_argument("--source", choices=["auto", "datasets", "datasets-server"], default="datasets-server")
    parser.add_argument("--claim-boundary", default="Public MMLU fixture for guarded local PTQ retention; not full leaderboard evidence until all shards and gates pass.")
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--max-start-memory-ratio", type=float, default=0.85)
    parser.add_argument("--min-disk-free-gb", type=int, default=20)
    parser.add_argument("--disk-check-path", default="/home/rui")
    parser.add_argument("--timeout-sec", type=int, default=1800)
    parser.add_argument("--max-new-tokens", type=int, default=64)
    parser.add_argument("--max-accuracy-drop", type=float, default=0.15)
    parser.add_argument("--max-ci-accuracy-drop", type=float, default=0.15)
    parser.add_argument("--bootstrap-samples", type=int, default=4000)
    parser.add_argument("--out-json", type=Path, default=None)
    parser.add_argument("--out-md", type=Path, default=None)
    args = parser.parse_args()
    args.suite = normalize_suite(args.suite)
    if args.out_json is None:
        args.out_json = Path(f"outputs/mmlu_ptq_shard_plan_{args.suite}_{args.date_tag}.json")
    if args.out_md is None:
        args.out_md = Path(f"outputs/MMLU_PTQ_SHARD_PLAN_{args.suite.upper()}_{args.date_tag}.md")

    plan = build_plan(args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, plan)
    print(
        json.dumps(
            {
                "out_json": str(args.out_json),
                "out_md": str(args.out_md),
                "suite": plan["suite"],
                "subjects": len(plan["subjects"]),
                "planned_rows": plan["total_rows_planned"],
                "variant_count": len(plan["variants"]),
                "shards_per_variant": len(plan["variants"][0]["shards"]) if plan["variants"] else 0,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
