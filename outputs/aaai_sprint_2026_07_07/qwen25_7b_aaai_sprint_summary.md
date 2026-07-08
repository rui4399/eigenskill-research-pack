# Qwen2.5-7B AAAI Sprint Summary

Generated: 2026-07-08

7B extension covers MMLU bit sweep plus MMLU/GSM8K equal-budget allocation slices. Results are mixed: CSI does not dominate single-split at 7B in this slice, so this should be framed as scale/failure-boundary evidence rather than a positive-only claim.

## MMLU100

| Method | Exact / 100 | Accuracy | Role |
|---|---:|---:|---|
| FP16 | 65 | 0.65 | upper reference |
| Uniform INT2 | 0 | 0.00 | bit sweep |
| Uniform INT3 | 8 | 0.08 | bit sweep |
| Uniform INT4 | 63 | 0.63 | bit sweep |
| Uniform INT8 | 65 | 0.65 | bit sweep |
| Single split 2-to-4 avg3 | 0 | 0.00 | collapse-boundary allocation |
| CSI consensus 2-to-4 avg3 | 1 | 0.01 | collapse-boundary allocation |
| Single split 3-to-4 avg3.5 | 55 | 0.55 | equal-budget allocation |
| CSI consensus 3-to-4 avg3.5 | 53 | 0.53 | equal-budget allocation |

Key result: Uniform INT4 retains 63/100 vs FP16 65/100. At 3-to-4 avg 3.5-bit, single-split allocation reaches 55/100 while CSI consensus reaches 53/100; this is scale evidence plus a failure/limitation case, not CSI dominance.

## GSM8K100

| Method | Exact / 100 | Accuracy | Role |
|---|---:|---:|---|
| FP16 | 4 | 0.04 | upper reference |
| Uniform INT4 | 5 | 0.05 | bit sweep |
| Single split 3-to-4 avg3.5 | 3 | 0.03 | equal-budget allocation |
| CSI consensus 3-to-4 avg3.5 | 2 | 0.02 | equal-budget allocation |

GSM8K100 is weak under the current simple generation and first-number scoring protocol; CSI is 2/100 vs single 3/100 at the 3.5-bit budget.

## Allocation Consistency

- 2-to-4 avg3: consensus_high_count=94, left_high_jaccard=0.8431, right_high_jaccard=0.8077
- 3-to-4 avg3.5: consensus_high_count=94, left_high_jaccard=0.8431, right_high_jaccard=0.8077

## Artifacts

- `outputs/aaai_sprint_2026_07_07/qwen25_7b_mmlu100_fp16_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_mmlu100_uniform_int2_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_mmlu100_uniform_int3_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_mmlu100_uniform_int4_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_mmlu100_uniform_int8_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_mmlu100_single_n64_budget3_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_mmlu100_csi_n64_budget3_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_mmlu100_single_n64_3to4_budget3p5_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_mmlu100_csi_n64_3to4_budget3p5_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_gsm8k100_fp16_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_gsm8k100_uniform_int4_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_gsm8k100_single_n64_3to4_budget3p5_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_7b_gsm8k100_csi_n64_3to4_budget3p5_v2.json`
