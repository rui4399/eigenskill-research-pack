#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


MODELS = ["qwen25_0p5b", "qwen25_1p5b", "qwen25_3b", "qwen25_7b"]
PRIMARY_MODELS = ["qwen25_0p5b", "qwen25_1p5b"]
ALLOCATION_MODELS = ["qwen25_1p5b", "qwen25_3b", "qwen25_7b"]
SCALE_MODELS = ["qwen25_7b", "qwen25_14b_awq"]
TASKS = ["mmlu", "gsm8k"]
SEEDS = [0, 1, 2, 3, 4]
CALIBRATION_SIZES = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
BIT_WIDTHS = [2, 3, 4, 8, 16]
AVERAGE_BIT_BUDGETS = [2, 3, 4]
ALLOCATION_POLICIES = [
    "uniform",
    "single_split",
    "sensitivity_only",
    "activation_magnitude",
    "hessian_trace_proxy",
    "weight_sensitivity",
    "random",
    "csi_guided",
]
PTQ_BASELINES = ["fp16", "uniform_int4", "uniform_int3", "gptq_int4", "awq_int4", "smoothquant_int4"]
BIT_SWEEP_METHODS = ["uniform", "gptq", "awq", "csi_guided"]
HEURISTICS = ["rank_variance", "entropy", "layer_sensitivity", "calibration_loss", "random", "csi"]


def add_run(
    runs: list[dict],
    *,
    experiment_id: str,
    model: str,
    task: str,
    method: str,
    seed: int | None = None,
    calibration_size: int | None = None,
    bit_width: int | None = None,
) -> None:
    run_key = [experiment_id, model, task, method, str(seed), str(calibration_size), str(bit_width)]
    runs.append(
        {
            "experiment_id": experiment_id,
            "model": model,
            "task": task,
            "method": method,
            "seed": seed,
            "calibration_size": calibration_size,
            "bit_width": bit_width,
            "run_key": run_key,
            "status": "pending",
            "expected_summary": f"outputs/aaai_sprint_2026_07_07/{'_'.join(run_key)}.json",
        }
    )


def build_payload() -> dict:
    experiments = [
        {
            "experiment_id": "p0_csi_allocation_retention",
            "reviewer_objection": "CSI is only an observation, not an allocation decision.",
            "required_outputs": [
                "pareto_curve",
                "task_retention_table",
                "equal_budget_int2_int3_int4",
                "bits_per_weight",
                "model_size",
                "rank_agreement",
                "csi_variance",
                "full_mmlu_gsm8k_downstream_retention",
            ],
        },
        {
            "experiment_id": "p0_calibration_size_scaling",
            "reviewer_objection": "Calibration stability does not necessarily scale into downstream retention.",
            "required_outputs": [
                "dual_axis_csi_accuracy_curve",
                "split_agreement",
                "rank_correlation",
                "topk_overlap",
            ],
        },
        {
            "experiment_id": "p0_seed_robustness",
            "reviewer_objection": "The result may be a lucky seed.",
            "required_outputs": ["mean_std_worst_case", "seed_rank_correlation", "seed_accuracy"],
        },
        {
            "experiment_id": "p0_csi_vs_heuristics",
            "reviewer_objection": "A simpler variance, entropy, sensitivity, or calibration-loss heuristic may be enough.",
            "required_outputs": [
                "pearson_correlation",
                "spearman_correlation",
                "kendall_tau",
                "future_accuracy_drop_prediction",
            ],
        },
        {
            "experiment_id": "p1_bit_width_sweep",
            "reviewer_objection": "The method is not stress-tested at low bits.",
            "required_outputs": ["int2_int3_int4_int8_fp16_retention_curve", "uniform_vs_gptq_vs_awq_vs_csi"],
        },
        {
            "experiment_id": "p1_scale_support",
            "reviewer_objection": "Small-model results may not generalize to 7B/14B-class models.",
            "required_outputs": [
                "qwen25_7b_csi_curve",
                "qwen25_7b_retention",
                "qwen25_14b_csi_curve",
                "qwen25_14b_retention_or_resource_boundary",
            ],
        },
    ]
    runs: list[dict] = []
    for model in ALLOCATION_MODELS:
        for task in TASKS:
            for method in PTQ_BASELINES + ALLOCATION_POLICIES:
                for budget in AVERAGE_BIT_BUDGETS:
                    add_run(
                        runs,
                        experiment_id="p0_csi_allocation_retention",
                        model=model,
                        task=task,
                        method=method,
                        bit_width=budget,
                    )
    for model in PRIMARY_MODELS + SCALE_MODELS:
        for task in TASKS:
            for n in CALIBRATION_SIZES:
                add_run(
                    runs,
                    experiment_id="p0_calibration_size_scaling",
                    model=model,
                    task=task,
                    method="csi_guided",
                    calibration_size=n,
                )
            for method in ["uniform", "gptq_int4", "awq_int4", "single_split", "csi_guided"]:
                for seed in SEEDS:
                    add_run(runs, experiment_id="p0_seed_robustness", model=model, task=task, method=method, seed=seed)
            for heuristic in HEURISTICS:
                add_run(runs, experiment_id="p0_csi_vs_heuristics", model=model, task=task, method=heuristic)
            if model == "qwen25_1p5b":
                for method in BIT_SWEEP_METHODS:
                    for bit_width in BIT_WIDTHS:
                        add_run(
                            runs,
                            experiment_id="p1_bit_width_sweep",
                            model=model,
                            task=task,
                            method=method,
                            bit_width=bit_width,
                        )
    for model in SCALE_MODELS:
        for task in TASKS:
            for method in ["uniform", "single_split", "csi_guided"]:
                add_run(runs, experiment_id="p1_scale_support", model=model, task=task, method=method, bit_width=4)
    return {
        "schema_version": 1,
        "created_for": "AAAI experiment sprint 2026-07-07",
        "experiments": experiments,
        "runs": runs,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(build_payload(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
