# RTX3090 Completion Audit - 2026-06-16

## Objective

Finish the reserved RTX3090 experiments, try a larger model and broader comparisons where practical, keep writes off C: as much as possible, and produce a report plus a paper-draft artifact.

## Verified Complete

| Requirement | Evidence | Status |
|---|---|---|
| Keep model/cache/temp outputs on E: | Models under `/mnt/e/models`; deps under `/mnt/e/python_deps/quant`; temp/cache under `/mnt/e/tmp`, `/mnt/e/hf_cache`, `/mnt/e/cache`; toolchain under `/mnt/e/conda_envs/rtx3090_toolchain` | PASS |
| RTX3090 env guard | `outputs/RTX3090_ENV_GUARD_2026_06_16.md` | PASS |
| 7B FP16 p1/p2 MMLU/GSM8K | `outputs/RTX3090_FP16_QWEN25_7B_MMLU_25_2026_06_16.md`, `outputs/RTX3090_FP16_QWEN25_7B_GSM8K_25_2026_06_16.md`, `outputs/RTX3090_FP16_QWEN25_7B_MMLU_100_2026_06_16.md`, `outputs/RTX3090_FP16_QWEN25_7B_GSM8K_100_2026_06_16.md` | PASS |
| 7B AWQ matched MMLU/GSM8K | `outputs/RTX3090_AWQ_QWEN25_7B_MMLU_25_2026_06_16.md`, `outputs/RTX3090_AWQ_QWEN25_7B_GSM8K_25_2026_06_16.md`, `outputs/RTX3090_AWQ_QWEN25_7B_MMLU_100_2026_06_16.md`, `outputs/RTX3090_AWQ_QWEN25_7B_GSM8K_100_2026_06_16.md` | PASS |
| 7B GPTQ matched MMLU/GSM8K | `outputs/RTX3090_GPTQMODEL_QWEN25_7B_MMLU_25_2026_06_16.md`, `outputs/RTX3090_GPTQMODEL_QWEN25_7B_GSM8K_25_2026_06_16.md`, `outputs/RTX3090_GPTQMODEL_QWEN25_7B_MMLU_100_2026_06_16.md`, `outputs/RTX3090_GPTQMODEL_QWEN25_7B_GSM8K_100_2026_06_16.md` | PASS |
| Larger-model experiment | `outputs/RTX3090_AWQ14B_QWEN25_14B_MMLU_10_2026_06_16.md` | PASS |
| P3 CSI gates from available seed-stability artifacts | `outputs/CSI_VS_N_CURVE_QWEN25_1P5B_RTX3090_REPRISE_2026_06_16.md`, `outputs/CSI_TREND_SIGNIFICANCE_QWEN25_1P5B_RTX3090_REPRISE_2026_06_16.md`, `outputs/CSI_NULL_PERMUTATION_QWEN25_1P5B_RTX3090_REPRISE_2026_06_16.md` | PASS for n=2/4/8 reprise |
| Strict P3 n=4/8/16 second-pool closure | `outputs/calibration_seed_stability_smollm2_360m_n4_second_pool_2026_06_16.json`, `outputs/calibration_seed_stability_smollm2_360m_n8_second_pool_2026_06_16.json`, `outputs/calibration_seed_stability_smollm2_360m_n16_second_pool_2026_06_16.json`, `outputs/csi_vs_n_curve_smollm2_360m_second_pool_2026_06_16.json`, `outputs/csi_trend_significance_smollm2_360m_second_pool_2026_06_16.json`, `outputs/csi_null_permutation_smollm2_360m_second_pool_2026_06_16.json` | PASS |
| More skill experiments | `outputs/QUANT_SKILL_DETERMINISTIC_BYPASS_2026_06_16.json`; LoRA adapter under `/mnt/e/skill_runs/quant_lora_smoke_2026_06_16` | PASS |
| Report deliverable | `outputs/RTX3090_EXPERIMENT_REPORT_2026_06_16.md` | PASS |
| Paper draft deliverable | `paper_drafts/eigenskill_q_rtx3090_extended_draft_2026_06_16.md` | PASS |

## Current Boundary

The deliverables are complete for the additional experiments run on the RTX3090. The strict n=4/8/16 P3 gap was closed with a SmolLM2-360M second-pool run over a 32-prompt pool, 6 seeds per calibration size, and passing CSI curve/trend/null gates. The Qwen2.5-1.5B reprise remains documented separately as an n=2/4/8 historical-artifact reprise, not as a Qwen n=16 claim.
