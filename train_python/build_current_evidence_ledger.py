#!/usr/bin/env python3
from __future__ import annotations

"""Build the current paper-facing evidence ledger from the committed gate set.

This wrapper keeps the public reproducibility entry point stable. The lower
level ``build_evidence_ledger.py`` still accepts arbitrary ``--gate`` values for
experiments, but the paper-facing branch should use this fixed manifest.
"""

import argparse
import json
import os
from pathlib import Path

import build_evidence_ledger as ledger


DEFAULT_OUT_JSON = Path("outputs/real_system_packer_2026-06-05/evidence_ledger_2026_06_06.json")
DEFAULT_OUT_MD = Path("outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md")

CURRENT_GATE_SPECS: tuple[tuple[str, str], ...] = (
    ("public_hygiene", "outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json"),
    ("calibration_instability", "outputs/calibration_instability_benchmark_2026_06_06.json"),
    ("sensitivity_perturbation_matrix", "outputs/sensitivity_perturbation_matrix_qwen25_2026_06_07.json"),
    ("calibration_seed_stability", "outputs/calibration_seed_stability_qwen25_0p5b_2026_06_07.json"),
    ("csi_vs_n_curve", "outputs/csi_vs_n_curve_qwen25_0p5b_2026_06_07.json"),
    ("csi_trend_significance", "outputs/csi_trend_significance_qwen25_0p5b_2026_06_07.json"),
    ("csi_null_permutation", "outputs/csi_null_permutation_qwen25_0p5b_2026_06_07.json"),
    ("csi_vs_n_curve_qwen25_1p5b", "outputs/csi_vs_n_curve_qwen25_1p5b_2026_06_11.json"),
    ("csi_trend_significance_qwen25_1p5b", "outputs/csi_trend_significance_qwen25_1p5b_2026_06_11.json"),
    ("csi_null_permutation_qwen25_1p5b", "outputs/csi_null_permutation_qwen25_1p5b_2026_06_11.json"),
    ("csi_cross_scale_qwen25", "outputs/csi_cross_scale_qwen25_0p5b_vs_1p5b_2026_06_11.json"),
    (
        "csi_cross_scale_paper_artifacts_qwen25",
        "outputs/csi_cross_scale_paper_artifacts_qwen25_0p5b_vs_1p5b_2026_06_12.json",
    ),
    ("rank_inversion_theory", "outputs/rank_inversion_theory_qwen25_0p5b_2026_06_07.json"),
    ("calibration_robustness_stress", "outputs/calibration_robustness_stress_gate_2026_06_07.json"),
    ("consensus_transfer_boundary", "outputs/consensus_transfer_boundary_gate_2026_06_07.json"),
    ("interaction_swap_boundary", "outputs/interaction_swap_boundary_gate_2026_06_07.json"),
    ("paper_evidence_alignment", "outputs/paper_evidence_alignment_gate_2026_06_08.json"),
    ("esmp_package", "outputs/real_system_packer_2026-06-05/esmp_package_verify_qwen3_0p6b_limit8_2026_06_06.json"),
    ("triton_shape_family", "outputs/real_system_packer_2026-06-05/triton_qwen_shape_family_gate_2026_06_06.json"),
    ("w4a8_activation_reconstruction", "outputs/w4a8_activation_reconstruction_2026_06_08/w4a8_activation_reconstruction_gate.json"),
    ("w4a8_activation_reconstruction_extended", "outputs/w4a8_activation_reconstruction_extended_2026_06_08/w4a8_activation_reconstruction_extended_gate.json"),
    ("selector_runtime", "outputs/real_system_packer_2026-06-05/selector_runtime_smoke_gate_2026_06_06.json"),
    ("selected_row", "outputs/real_system_packer_2026-06-05/selected_row_benchmark_gate_2026_06_06.json"),
    ("cpp_runtime", "outputs/real_system_packer_2026-06-05/cpp_runtime_sweep_gate_2026_06_06.json"),
    ("fused_sidecar", "outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate_2026_06_06.json"),
    ("fused_qkv_speed", "outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate_2026_06_06.json"),
    ("fused_qkv_quality", "outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate_2026_06_06.json"),
    ("chat_task_stress", "outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_gate_2026_06_06.json"),
    (
        "public_task_benchmark",
        "outputs/public_task_benchmark_ollama_qwen25_abliterate_7b_gsm8k200_mmlu100_gate_2026_06_08.json",
    ),
    (
        "public_task_gsm8k_full_7b",
        "outputs/public_task_benchmark_gsm8kfull_ollama_qwen25_abliterate_7b_gate_2026_06_08.json",
    ),
    ("public_task_model_ladder", "outputs/public_task_model_ladder_gate_2026_06_07.json"),
    ("official_ptq_task_retention", "outputs/official_ptq_task_retention_smoke_matrix_2026_06_07.json"),
    ("official_ptq_runtime_profile", "outputs/official_ptq_runtime_profile_2026_06_07.json"),
    ("official_ptq_task_subset50", "outputs/official_ptq_task_subset50_matrix_2026_06_07.json"),
    ("official_ptq_subset50_runtime_profile", "outputs/official_ptq_subset50_runtime_profile_2026_06_07.json"),
    ("official_ptq_task_subset100", "outputs/official_ptq_task_subset100_matrix_2026_06_07.json"),
    ("official_ptq_subset100_runtime_profile", "outputs/official_ptq_subset100_runtime_profile_2026_06_07.json"),
    ("official_ptq_ifeval_v2", "outputs/official_ptq_task_ifeval_v2_matrix_2026_06_07.json"),
    ("official_ptq_ifeval_v2_runtime_profile", "outputs/official_ptq_runtime_ifeval_v2_profile_2026_06_07.json"),
    ("official_ptq_matched_baseline_pack", "outputs/official_ptq_matched_baseline_pack_qwen25_0p5b_2026_06_07.json"),
    ("official_awq_public_calib_16_eval", "outputs/official_awq_public_calib_qwen25_0p5b_bundle_16_gate_2026_06_07.json"),
    ("official_awq_public_calib_1p5b_16_eval", "outputs/official_awq_public_calib_qwen25_1p5b_bundle_16_gate_2026_06_07.json"),
    ("official_gptqmodel_public_calib_1p5b_16_eval", "outputs/official_gptqmodel_public_calib_qwen25_1p5b_16_gate_2026_06_08.json"),
    ("official_gptqmodel_task_execution_qwen25_1p5b_subset100", "outputs/official_gptqmodel_task_execution_qwen25_1p5b_subset100_matrix_2026_06_08.json"),
    ("official_ptq_task_qwen25_1p5b_subset100_fp16_awq_gptqmodel", "outputs/official_ptq_task_qwen25_1p5b_subset100_fp16_awq_gptqmodel_matrix_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_subset100_fp16_awq_gptqmodel_runtime_profile", "outputs/official_ptq_qwen25_1p5b_subset100_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json"),
    ("official_ptq_task_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel", "outputs/official_ptq_task_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_matrix_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_runtime_profile", "outputs/official_ptq_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_statistics", "outputs/official_ptq_task_qwen25_1p5b_gsm8k200_mmlu100_fp16_awq_gptqmodel_statistics_2026_06_08.json"),
    ("official_ptq_task_qwen25_1p5b_gsm8k500_fp16_awq_gptqmodel", "outputs/official_ptq_task_qwen25_1p5b_gsm8k500_fp16_awq_gptqmodel_matrix_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_gsm8k500_fp16_awq_gptqmodel_runtime_profile", "outputs/official_ptq_qwen25_1p5b_gsm8k500_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_gsm8k500_fp16_awq_gptqmodel_statistics", "outputs/official_ptq_task_qwen25_1p5b_gsm8k500_fp16_awq_gptqmodel_statistics_2026_06_08.json"),
    ("official_ptq_task_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel", "outputs/official_ptq_task_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel_matrix_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel_runtime_profile", "outputs/official_ptq_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel_statistics", "outputs/official_ptq_task_qwen25_1p5b_gsm8kfull_fp16_awq_gptqmodel_statistics_2026_06_08.json"),
    ("official_ptq_task_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel", "outputs/official_ptq_task_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel_matrix_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel_runtime_profile", "outputs/official_ptq_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel_statistics", "outputs/official_ptq_task_qwen25_1p5b_mmlu_broad5x20_fp16_awq_gptqmodel_statistics_2026_06_08.json"),
    ("official_ptq_task_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel", "outputs/official_ptq_task_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel_matrix_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel_runtime_profile", "outputs/official_ptq_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel_statistics", "outputs/official_ptq_task_qwen25_1p5b_mmlu_broad10x20_fp16_awq_gptqmodel_statistics_2026_06_08.json"),
    ("official_ptq_task_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel", "outputs/official_ptq_task_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_matrix_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_runtime_profile", "outputs/official_ptq_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_statistics", "outputs/official_ptq_task_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_statistics_2026_06_08.json"),
    ("official_ptq_task_qwen25_1p5b_mmlu_full_prefix12000_fp16_awq_gptqmodel", "outputs/official_ptq_task_qwen25_1p5b_mmlu_full_prefix12000_fp16_awq_gptqmodel_matrix_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_mmlu_full_prefix12000_fp16_awq_gptqmodel_runtime_profile", "outputs/official_ptq_qwen25_1p5b_mmlu_full_prefix12000_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_mmlu_full_prefix12000_fp16_awq_gptqmodel_statistics", "outputs/official_ptq_task_qwen25_1p5b_mmlu_full_prefix12000_fp16_awq_gptqmodel_statistics_2026_06_08.json"),
    ("official_ptq_task_qwen25_1p5b_mmlu_full_prefix14042_fp16_awq_gptqmodel", "outputs/official_ptq_task_qwen25_1p5b_mmlu_full_prefix14042_fp16_awq_gptqmodel_matrix_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_mmlu_full_prefix14042_fp16_awq_gptqmodel_runtime_profile", "outputs/official_ptq_qwen25_1p5b_mmlu_full_prefix14042_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json"),
    ("official_ptq_qwen25_1p5b_mmlu_full_prefix14042_fp16_awq_gptqmodel_statistics", "outputs/official_ptq_task_qwen25_1p5b_mmlu_full_prefix14042_fp16_awq_gptqmodel_statistics_2026_06_08.json"),
    ("allocation_family_proxy", "outputs/q_palette_style_allocation_family_gate_2026_06_06.json"),
    ("robust_lcb_consensus", "outputs/robust_lcb_consensus_family_gate_2026_06_06.json"),
    ("robust_lcb_quality", "outputs/qwen3_0p6b_robust_lcb_quality_gate_2026_06_07.json"),
    ("rotation_family_proxy", "outputs/quarot_spinquant_rotation_family_gate_2026_06_06.json"),
    ("awq_gptq_proxy", "outputs/awq_gptq_proxy_gate_2026_06_06.json"),
)


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def current_gates() -> list[tuple[str, Path]]:
    return [(label, Path(raw_path)) for label, raw_path in CURRENT_GATE_SPECS]


def build_current_ledger(repo_root: Path, out_json: Path, out_md: Path) -> dict:
    previous_cwd = Path.cwd()
    try:
        os.chdir(repo_root)
        result = ledger.build_ledger(current_gates())
    finally:
        os.chdir(previous_cwd)
    out_json = repo_root / out_json if not out_json.is_absolute() else out_json
    out_md = repo_root / out_md if not out_md.is_absolute() else out_md
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ledger.write_markdown(out_md, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the current paper-facing evidence ledger.")
    parser.add_argument("--repo-root", type=Path, default=repo_root_from_script())
    parser.add_argument("--out-json", type=Path, default=DEFAULT_OUT_JSON)
    parser.add_argument("--out-md", type=Path, default=DEFAULT_OUT_MD)
    parser.add_argument("--expected-gate-count", type=int, default=len(CURRENT_GATE_SPECS))
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    result = build_current_ledger(repo_root, args.out_json, args.out_md)
    payload = {
        "passed": result["passed"],
        "gate_count": result["gate_count"],
        "out_json": str(args.out_json),
        "out_md": str(args.out_md),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if result["gate_count"] != args.expected_gate_count:
        raise SystemExit(f"expected {args.expected_gate_count} gates, got {result['gate_count']}")
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
