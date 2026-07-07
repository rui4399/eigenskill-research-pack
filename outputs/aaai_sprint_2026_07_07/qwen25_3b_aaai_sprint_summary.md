# Qwen2.5-3B AAAI Sprint Summary

Generated: 2026-07-08

Note: GPU was intentionally run with concurrent jobs to use remaining RTX 3090 memory. Use these runs for accuracy/retention evidence, not clean efficiency timing claims.

## MMLU100

| Method | Exact / 100 | Accuracy | Role |
|---|---:|---:|---|
| FP16 | 52 | 0.52 | upper reference |
| Uniform INT2 | 0 | 0.00 | bit sweep |
| Uniform INT3 | 2 | 0.02 | bit sweep |
| Uniform INT4 | 42 | 0.42 | bit sweep |
| Uniform INT8 | 52 | 0.52 | bit sweep |
| Single split 2-to-4 avg3 | 4 | 0.04 | collapse-boundary allocation |
| CSI consensus 2-to-4 avg3 | 1 | 0.01 | collapse-boundary allocation |
| Single split 3-to-4 avg3.5 | 30 | 0.30 | equal-budget allocation |
| CSI consensus 3-to-4 avg3.5 | 36 | 0.36 | equal-budget allocation |

Key pressure-budget result: at 3-to-4 avg 3.5-bit, CSI consensus improves MMLU100 from 30/100 to 36/100 over single-split allocation under the same budget. At 2-to-4 avg 3-bit, both policies are at the collapse boundary.

## GSM8K100

| Method | Exact / 100 | Accuracy | Role |
|---|---:|---:|---|
| FP16 | 6 | 0.06 | upper reference |
| Uniform INT3 | 0 | 0.00 | bit sweep |
| Uniform INT4 | 5 | 0.05 | bit sweep |
| Single split 3-to-4 avg3.5 | 2 | 0.02 | equal-budget allocation |
| CSI consensus 3-to-4 avg3.5 | 3 | 0.03 | equal-budget allocation |

GSM8K remains a weak-task slice for this simple generation/evaluation setup, but CSI still improves the 3.5-bit allocation from 2/100 to 3/100 under equal budget.

## Allocation Consistency

- 2-to-4 avg3: consensus_high_count=124, left_high_jaccard=0.8014, right_high_jaccard=0.7762
- 3-to-4 avg3.5: consensus_high_count=124, left_high_jaccard=0.8014, right_high_jaccard=0.7762

## Artifacts

- `outputs/aaai_sprint_2026_07_07/qwen25_3b_mmlu100_fp16_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_mmlu100_uniform_int2_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_mmlu100_uniform_int3_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_mmlu100_uniform_int4_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_mmlu100_uniform_int8_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_mmlu100_single_n64_budget3_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_mmlu100_csi_n64_budget3_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_mmlu100_single_n64_3to4_budget3p5_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_mmlu100_csi_n64_3to4_budget3p5_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_gsm8k100_fp16_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_gsm8k100_uniform_int3_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_gsm8k100_uniform_int4_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_gsm8k100_single_n64_3to4_budget3p5_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_3b_gsm8k100_csi_n64_3to4_budget3p5_v2.json`
