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
