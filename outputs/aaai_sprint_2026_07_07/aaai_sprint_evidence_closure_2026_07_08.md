# AAAI Sprint Evidence Closure

Generated: 2026-07-08

This file maps the AAAI reviewer-risk checklist to concrete artifacts already produced in this sprint.

## P0 Evidence

| Reviewer risk | Evidence artifact | Status |
|---|---|---|
| CSI is only an observation, not a downstream allocation decision. | `aaai_sprint_downstream_retention_matrix_2026_07_08.{json,md}` plus Qwen2.5 1.5B/3B/7B MMLU100 and GSM8K100 retention JSON files. | Covered for 1.5B/3B/7B with equal-budget uniform, single-split, and CSI allocation slices. |
| Calibration-size stability is not shown. | `qwen25_1p5b_n16_n32_n64_n128_csi_scaling_summary.json`; `qwen25_7b_n16_n32_n64_csi_scale_summary.json`. | Covered for 1.5B and 7B. |
| Result may be seed luck. | `qwen25_1p5b_wikitext2_n64_seed0_to_seed4_robustness_summary.json`. | Covered for 1.5B n64 sensitivity/allocation stability. |
| CSI may be no better than simple heuristics. | `qwen25_1p5b_n64_csi_vs_heuristic_future_split_summary.{json,md}`. | Covered as a calibration-sensitivity prediction check; not downstream task prediction. |
| Domain shift may break calibration. | `qwen25_1p5b_wikitext2_vs_c4_n64_domain_shift_summary.json`. | Covered for WikiText2 vs C4 calibration stability. |

## Scale Evidence

| Scale | Evidence artifact | Boundary |
|---|---|---|
| 3B | `qwen25_3b_aaai_sprint_summary.{json,md}` and downstream matrix rows. | CSI helps at 3-to-4 avg 3.5-bit in the measured MMLU/GSM8K slices. |
| 7B | `qwen25_7b_aaai_sprint_summary.{json,md}` and downstream matrix rows. | Mixed/negative: CSI does not beat single split in the measured 3.5-bit 7B slice. Use as scale and failure-boundary evidence. |
| 14B | `qwen25_14b_awq_aaai_sprint_summary.{json,md}` and `qwen25_14b_awq_module_compat_probe.json`. | AWQ retention feasibility only. Full 14B CSI allocation is blocked by AWQ `WQLinear_GEMM` modules not exposing standard Linear weights to the current fake-quant sensitivity path. |

## Downstream Matrix Highlights

| Model | Task | Key retained evidence |
|---|---|---|
| Qwen2.5-1.5B | MMLU100 | FP16 54/100, INT4 41/100, INT8 55/100, avg3 CSI 1/100 vs single 0/100. |
| Qwen2.5-1.5B | GSM8K100 | FP16 3/100, INT4 2/100, avg3 CSI 0/100 vs single 2/100. |
| Qwen2.5-3B | MMLU100 | FP16 52/100, INT4 42/100, avg3.5 CSI 36/100 vs single 30/100. |
| Qwen2.5-3B | GSM8K100 | FP16 6/100, INT4 5/100, avg3.5 CSI 3/100 vs single 2/100. |
| Qwen2.5-7B | MMLU100 | FP16 65/100, INT4 63/100, avg3.5 CSI 53/100 vs single 55/100. |
| Qwen2.5-7B | GSM8K100 | FP16 4/100, INT4 5/100, avg3.5 CSI 2/100 vs single 3/100. |
| Qwen2.5-14B-AWQ | MMLU100/GSM8K100 | AWQ checkpoint: MMLU100 65/100, GSM8K100 13/100. |

## Claim Boundary

The sprint now supports a stricter paper narrative: CSI can be used as an allocation decision framework and exposes both gains and failure boundaries under equal-budget quantization. The current evidence should not claim universal CSI dominance, especially at 7B and 14B. The strongest defensible claim is calibration-aware allocation with measured scale limits and explicit failure cases.

## Cross-Family Evidence

Phi-3-mini evidence is recorded in `phi3_mini_cross_family_summary_2026_07_08.{json,md}`. The model exposes 129 standard Linear modules, supports the existing sensitivity path, and provides MMLU/GSM8K FP16, INT4, single-split avg3, and CSI avg3 downstream slices. Results are a stress/failure-boundary case: INT4 retains while avg3 allocation collapses.

## Final Reviewer Tables

Additional reviewer-facing closure artifacts generated on 2026-07-09:

- Win/loss and average rank: `aaai_sprint_win_loss_average_rank_2026_07_09.{json,md}`.
- Failure recovery audit: `aaai_sprint_failure_recovery_audit_2026_07_09.{json,md}`.
- Gate behavior distribution: `aaai_sprint_gate_behavior_distribution_2026_07_09.{json,md}`.

These tables should be used as audit/positioning evidence rather than as new positive-only claims; they explicitly preserve loss cases and rejection boundaries.

## Bit/Budget Sensitivity and Alignment

- Bit/budget sensitivity source: `aaai_sprint_bit_budget_sensitivity_2026_07_09.{json,md}`.
- Calibration-size-to-retention alignment source: `aaai_sprint_calibration_alignment_2026_07_09.{json,md}`.
## 7B Strong Quantizer Baseline Update

Added on 2026-07-09: `qwen25_7b_quantizer_baseline_summary_2026_07_09.{json,md}` records AWQ checkpoint downstream retention for Qwen2.5-7B. MMLU100 is 64/100, compared with FP16 65/100 and local uniform INT4 63/100. GSM8K100 is 2/100, compared with FP16 4/100 and local uniform INT4 5/100 under the current first-number scoring protocol. GPTQ is explicitly blocked in this environment after `optimum` installation by `NameError("name 'QuantizeConfig' is not defined")`, so no GPTQ downstream score is claimed.
## Completion Audit

Added on 2026-07-09: `aaai_sprint_completion_audit_2026_07_09.{json,md}` maps the full AAAI sprint checklist to concrete artifacts and explicitly records remaining strict boundaries: full 14B CSI allocation, true wall-clock efficiency, extended n256+ calibration scaling, and GPTQ runtime compatibility.
## Efficiency Timing Smoke

Added on 2026-07-09: `qwen25_1p5b_efficiency_timing_smoke_2026_07_09.{json,md}` and `qwen25_1p5b_efficiency_timing_smoke_wallclock_2026_07_09.json` record a reproducible wall-clock smoke for the sensitivity path: Qwen2.5-1.5B, 4 prompts, 1 Linear module, RTX 3090, 12.931 seconds end-to-end. This upgrades the efficiency evidence from proxy-only to proxy-plus-smoke, but it is still not a full timing table across all scales.
## GPTQ Dependency Blocker Follow-up

Added on 2026-07-09: `qwen25_7b_gptq_dependency_blocker_2026_07_09.{json,md}` records a stronger GPTQ blocker. Installing `gptqmodel 2.2.0+cu121torch2.5` moves past the missing `QuantizeConfig` error, but the current Windows Python 3.9 runtime fails importing `gptqmodel` with a PEP-604 type-union/EnumMeta error. The project test subset still passes after restoring numpy/pytest/setuptools/wheel to project-compatible versions.
## Multi-scale Efficiency Timing Smoke

Added on 2026-07-09: `aaai_sprint_efficiency_timing_smoke_2026_07_09.{json,md}` aggregates reproducible 1.5B/3B/7B timing smokes under the same 4-prompt/1-module sensitivity protocol. Wall-clock times are 12.931s, 15.102s, and 37.691s respectively. This remains a smoke/protocol timing table, not a full all-module benchmark.
## Calibration Scaling 512 Prompt Readiness

Added on 2026-07-09: `aaai_scaling_512_prompt_manifest_2026_07_09.{json,md}` and `aaai_scaling_512_readiness_audit_2026_07_09.{json,md}` materialize public WikiText2/C4 prompt pools with 512 usable prompts each. This closes the prompt-pool preparation gap for n256/n512 scaling, but the expensive sensitivity/downstream runs for those sizes are still not claimed complete.
## Calibration Scaling n256 Evidence

Added on 2026-07-09: `qwen25_1p5b_wikitext2_n256_seed0_seed1_csi_consensus_2to4_budget3.{json,md}` and `qwen25_1p5b_n16_n32_n64_n128_n256_csi_scaling_summary.{json,md}` record completed Qwen2.5-1.5B n256 sensitivity/consensus scaling from the 512-prompt WikiText2 pool. The n256 mean high-bit Jaccard is 0.908, with avg bits 2.9999 and 98/99 split across 2-bit/4-bit modules. This upgrades calibration scaling from readiness-only to completed n256 calibration evidence; n256 downstream retention and n512 remain unclaimed.
## 14B AWQ-Aware CSI Proxy

Added on 2026-07-09: `qwen25_14b_awq_activation_csi_proxy_n64_seed0_seed1_2026_07_09.{json,md}` records an AWQ-aware calibration-stability proxy over all 336 `WQLinear_GEMM` modules in the local Qwen2.5-14B-Instruct-AWQ checkpoint. At n64, seed0/seed1 top-25% Jaccard is 0.9765 and Spearman rank correlation is 0.9998; the proxy 2/4-bit allocation uses avg 2.9996 bits. This strengthens the 14B scale evidence while preserving the boundary that full 14B fake-quant downstream CSI remains unclaimed.
## Calibration Scaling n512 Evidence

Added on 2026-07-09: `qwen25_1p5b_wikitext2_n512_seed0_sensitivity_2to4_budget3.{json,md}` and `qwen25_1p5b_n16_n32_n64_n128_n256_n512_csi_scaling_summary.{json,md}` record completed Qwen2.5-1.5B n512 full-pool sensitivity/allocation evidence. The run uses 512 prompts and covers 197/197 modules; avg bits is 2.9988 and protected positive-delta ratio is 0.9136. This closes the sensitivity side of the calibration-size curve through n512, while explicitly not claiming n512 two-split consensus.

## 1.5B n256/n512 Downstream Scaling Update

Added on 2026-07-09: `qwen25_1p5b_n64_n256_n512_downstream_scaling_summary_2026_07_09.{json,md}` records downstream retention for the extended calibration-size evidence. Under the average ~3-bit 2/4-bit budget, n256 CSI consensus reaches MMLU100 5/100 and GSM8K100 0/100; the true n512 full-pool single sensitivity allocation reaches MMLU100 5/100 and GSM8K100 0/100. This closes the n256 downstream gap and adds n512 downstream evidence, while preserving the boundary that n512 two-split CSI consensus remains unclaimed.

## Mixed-Domain n512 Split-Consensus Closure

Added on 2026-07-09: `aaai_mixed_1024_prompt_manifest_2026_07_09.{json,md}` and `qwen25_1p5b_mixed1024_n512_csi_consensus_downstream_summary_2026_07_09.{json,md}` record a true n512 two-split CSI consensus run using two independent 512-sample draws from a mixed public 1024-prompt pool (512 WikiText2 + 512 C4). Both seed runs cover 197/197 modules. The consensus allocation uses avg 2.9999 bits with 103 4-bit and 94 2-bit modules; left/right high-bit Jaccard is 0.8727/0.8899. Downstream retention is MMLU100 4/100 and GSM8K100 0/100. This closes the n512 split-consensus method gap for mixed-domain public calibration while preserving the boundary that pure WikiText2 n512 remains full-pool single-run evidence only.

