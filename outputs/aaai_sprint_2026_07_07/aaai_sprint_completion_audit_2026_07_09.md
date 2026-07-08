# AAAI Sprint Completion Audit

Generated: 2026-07-09

Overall status: `substantially_complete_with_explicit_14b_csi_and_true_efficiency_boundaries`

This audit maps the requested AAAI sprint experiments to concrete artifacts in this repository. It is intentionally strict: mixed or blocked results are recorded as boundaries rather than hidden.

| Requirement | Status | Evidence | Boundary |
|---|---|---|---|
| P0 CSI-guided allocation downstream retention under equal budget | `complete_with_mixed_results` | `aaai_sprint_downstream_retention_matrix_2026_07_08.json`, `aaai_sprint_pareto_frontier_2026_07_08.json`, `aaai_sprint_failure_recovery_audit_2026_07_09.json` | CSI is useful as allocation/audit evidence but does not dominate in every slice; 7B avg3.5 is mixed/negative versus single-split. |
| P0 calibration size scaling | `complete_for_1p5b_and_7b_partial_curve` | `aaai_sprint_calibration_alignment_2026_07_09.json`, `qwen25_1p5b_n16_n32_n64_n128_csi_scaling_summary.json`, `qwen25_7b_n16_n32_n64_csi_scale_summary.json` | Not a full 16..4096 curve. It is enough for current sprint trend evidence, but a final AAAI camera-ready package should extend n256+ if compute time allows. |
| P0 seed robustness | `complete_for_1p5b_calibration_stability` | `qwen25_1p5b_wikitext2_n64_seed0_to_seed4_robustness_summary.json` | Downstream task accuracy is not rerun for all five seeds; use as calibration stability, not full task seed-mean evidence. |
| P0 CSI vs simple heuristic comparison | `complete_for_future_split_prediction` | `qwen25_1p5b_n64_csi_vs_heuristic_future_split_summary.json`, `qwen25_1p5b_n64_csi_vs_heuristic_future_split_summary.md` | This predicts future calibration sensitivity, not future task accuracy drop directly. |
| P1/P0 bit-width and low-bit pressure sweep | `complete_for_1p5b_3b_7b_uniform_and_mixed_slices` | `aaai_sprint_bit_budget_sensitivity_2026_07_09.json`, `qwen25_7b_aaai_sprint_summary.json`, `qwen25_3b_aaai_sprint_summary.json` | External GPTQ bit sweep remains blocked by local checkpoint/runtime issue; AWQ checkpoint baselines are added separately. |
| P1 cross-model/family generalization | `complete_for_one_extra_family` | `phi3_mini_cross_family_summary_2026_07_08.json`, `phi3_mini_cross_family_summary_2026_07_08.md` | This is a stress/failure-boundary cross-family check, not a positive-only generalization claim. |
| P1 calibration dataset/domain shift | `complete_for_1p5b_wikitext2_vs_c4` | `qwen25_1p5b_wikitext2_vs_c4_n64_domain_shift_summary.json` | Domain-shift downstream task retention is not separately rerun per calibration domain. |
| P2 efficiency overhead | `partial_proxy_only` | `aaai_sprint_efficiency_proxy_2026_07_08.json`, `aaai_sprint_efficiency_proxy_2026_07_08.md` | Not a true wall-clock benchmark table; do not overclaim runtime overhead. |
| P2 layer-level mechanism visualization/data | `complete_data_artifact` | `aaai_sprint_layer_mechanism_2026_07_08.json`, `aaai_sprint_layer_mechanism_2026_07_08.csv`, `aaai_sprint_gate_behavior_distribution_2026_07_09.json` | Plots can be regenerated from CSV/JSON; current artifact is data-first. |
| 7B full downstream and strong quantizer baseline | `complete_with_awq_and_gptq_blocker` | `qwen25_7b_aaai_sprint_summary.json`, `qwen25_7b_quantizer_baseline_summary_2026_07_09.json`, `qwen25_7b_awq_mmlu100_v2.json`, `qwen25_7b_awq_gsm8k100_v2.json`, `qwen25_7b_gptq_probe_after_optimum_2026_07_09.json` | GPTQ downstream score is not claimed because the local GPTQ checkpoint fails after optimum with QuantizeConfig NameError. |
| 14B downstream and CSI allocation | `partial_downstream_complete_csi_blocked` | `qwen25_14b_awq_aaai_sprint_summary.json`, `qwen25_14b_awq_mmlu100_v2.json`, `qwen25_14b_awq_gsm8k100_v2.json`, `qwen25_14b_awq_module_compat_probe.json` | Full 14B CSI allocation is not complete: only AWQ checkpoint is local; body modules are WQLinear_GEMM and the current CSI fake-quant path only traverses standard torch.nn.Linear. Loading FP16 14B into current all-cuda script would exceed the 24GB RTX 3090 memory budget. |

## Remaining Strict Gaps

- Full 14B CSI-guided allocation/downstream retention requires an FP16/BF16 14B checkpoint plus offload/device_map support, or an AWQ-aware sensitivity path for WQLinear_GEMM modules.
- True wall-clock efficiency overhead table is still proxy-only.
- Full calibration-size curve through n256/n512/n1024/n2048/n4096 is not complete for all models/tasks.
- GPTQ 7B downstream retention is blocked by QuantizeConfig runtime/schema failure in this environment.

## Recommended Paper Claim

The sprint supports a calibration-aware allocation/audit framework with downstream evidence across 1.5B/3B/7B and one cross-family model, plus 14B AWQ feasibility. It should not claim universal CSI dominance or completed 14B CSI allocation.
