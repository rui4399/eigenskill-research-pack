# AAAI Sprint Win/Loss and Average Rank

Generated: 2026-07-09

Regenerated from downstream retention matrix after adding Qwen2.5-7B AWQ checkpoint rows.

## Average Rank

| Method | Average rank |
|---|---:|
| awq_checkpoint/csi_guided | 1.00 |
| awq_int4_checkpoint/awq_int4_checkpoint | 1.00 |
| fp16/csi_guided | 1.38 |
| uniform_int4/csi_guided | 2.38 |
| uniform_int8/csi_guided | 2.83 |
| allocation/loss_sensitive_4to8 | 4.70 |
| allocation/loss_sensitive_robust_lcb_consensus_4to8 | 4.90 |
| uniform_int3/csi_guided | 6.17 |
| uniform_int2/csi_guided | 7.00 |

## CSI Win/Loss Audit

| Comparison | Wins | Losses | Ties |
|---|---:|---:|---:|
| csi_guided_vs_allocation/loss_sensitive_4to8 | 5 | 4 | 1 |
| csi_guided_vs_allocation/loss_sensitive_robust_lcb_consensus_4to8 | 2 | 0 | 0 |
| csi_guided_vs_fp16/csi_guided | 0 | 8 | 0 |
| csi_guided_vs_uniform_int2/csi_guided | 5 | 0 | 1 |
| csi_guided_vs_uniform_int3/csi_guided | 4 | 1 | 1 |
| csi_guided_vs_uniform_int4/csi_guided | 0 | 8 | 0 |
| csi_guided_vs_uniform_int8/csi_guided | 0 | 5 | 1 |

## Rank Rows

| Model | Task | Method | Accuracy | Rank | Artifact |
|---|---|---|---:|---:|---|
| 14b_awq | gsm8k100 | awq_checkpoint/csi_guided | 0.13 | 1 | `qwen25_14b_awq_gsm8k100_v2.json` |
| 14b_awq | mmlu100 | awq_checkpoint/csi_guided | 0.65 | 1 | `qwen25_14b_awq_mmlu100_v2.json` |
| 1p5b | gsm8k100 | fp16/csi_guided | 0.03 | 1 | `qwen25_1p5b_gsm8k100_fp16_v2.json` |
| 1p5b | gsm8k100 | allocation/loss_sensitive_4to8 | 0.02 | 2 | `qwen25_1p5b_gsm8k100_single_n64_budget3_v2.json` |
| 1p5b | gsm8k100 | uniform_int4/csi_guided | 0.02 | 3 | `qwen25_1p5b_gsm8k100_uniform_int4_v2.json` |
| 1p5b | gsm8k100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0.00 | 4 | `qwen25_1p5b_gsm8k100_csi_n64_budget3_v2.json` |
| 1p5b | gsm8k100 | uniform_int2/csi_guided | 0.00 | 5 | `qwen25_1p5b_gsm8k100_uniform_int2_v2.json` |
| 1p5b | gsm8k100 | uniform_int3/csi_guided | 0.00 | 6 | `qwen25_1p5b_gsm8k100_uniform_int3_v2.json` |
| 1p5b | gsm8k100 | uniform_int8/csi_guided | 0.00 | 7 | `qwen25_1p5b_gsm8k100_uniform_int8_v2.json` |
| 1p5b | mmlu100 | uniform_int8/csi_guided | 0.55 | 1 | `qwen25_1p5b_mmlu100_uniform_int8_v2.json` |
| 1p5b | mmlu100 | fp16/csi_guided | 0.54 | 2 | `qwen25_1p5b_mmlu100_fp16_v2.json` |
| 1p5b | mmlu100 | uniform_int4/csi_guided | 0.41 | 3 | `qwen25_1p5b_mmlu100_uniform_int4_v2.json` |
| 1p5b | mmlu100 | uniform_int3/csi_guided | 0.04 | 4 | `qwen25_1p5b_mmlu100_uniform_int3_v2.json` |
| 1p5b | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0.01 | 5 | `qwen25_1p5b_mmlu100_csi_n64_budget3_v2.json` |
| 1p5b | mmlu100 | allocation/loss_sensitive_4to8 | 0.00 | 6 | `qwen25_1p5b_mmlu100_single_n64_budget3_v2.json` |
| 1p5b | mmlu100 | uniform_int2/csi_guided | 0.00 | 7 | `qwen25_1p5b_mmlu100_uniform_int2_v2.json` |
| 3b | gsm8k100 | fp16/csi_guided | 0.06 | 1 | `qwen25_3b_gsm8k100_fp16_v2.json` |
| 3b | gsm8k100 | uniform_int8/csi_guided | 0.06 | 2 | `qwen25_3b_gsm8k100_uniform_int8_v2.json` |
| 3b | gsm8k100 | uniform_int4/csi_guided | 0.05 | 3 | `qwen25_3b_gsm8k100_uniform_int4_v2.json` |
| 3b | gsm8k100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0.03 | 4 | `qwen25_3b_gsm8k100_csi_n64_3to4_budget3p5_v2.json` |
| 3b | gsm8k100 | allocation/loss_sensitive_4to8 | 0.02 | 5 | `qwen25_3b_gsm8k100_single_n64_3to4_budget3p5_v2.json` |
| 3b | gsm8k100 | uniform_int2/csi_guided | 0.00 | 6 | `qwen25_3b_gsm8k100_uniform_int2_v2.json` |
| 3b | gsm8k100 | uniform_int3/csi_guided | 0.00 | 7 | `qwen25_3b_gsm8k100_uniform_int3_v2.json` |
| 3b | mmlu100 | fp16/csi_guided | 0.52 | 1 | `qwen25_3b_mmlu100_fp16_v2.json` |
| 3b | mmlu100 | uniform_int8/csi_guided | 0.52 | 2 | `qwen25_3b_mmlu100_uniform_int8_v2.json` |
| 3b | mmlu100 | uniform_int4/csi_guided | 0.42 | 3 | `qwen25_3b_mmlu100_uniform_int4_v2.json` |
| 3b | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0.36 | 4 | `qwen25_3b_mmlu100_csi_n64_3to4_budget3p5_v2.json` |
| 3b | mmlu100 | allocation/loss_sensitive_4to8 | 0.30 | 5 | `qwen25_3b_mmlu100_single_n64_3to4_budget3p5_v2.json` |
| 3b | mmlu100 | allocation/loss_sensitive_4to8 | 0.04 | 6 | `qwen25_3b_mmlu100_single_n64_budget3_v2.json` |
| 3b | mmlu100 | uniform_int3/csi_guided | 0.02 | 7 | `qwen25_3b_mmlu100_uniform_int3_v2.json` |
| 3b | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0.01 | 8 | `qwen25_3b_mmlu100_csi_n64_budget3_v2.json` |
| 3b | mmlu100 | uniform_int2/csi_guided | 0.00 | 9 | `qwen25_3b_mmlu100_uniform_int2_v2.json` |
| 7b | gsm8k100 | uniform_int4/csi_guided | 0.05 | 1 | `qwen25_7b_gsm8k100_uniform_int4_v2.json` |
| 7b | gsm8k100 | fp16/csi_guided | 0.04 | 2 | `qwen25_7b_gsm8k100_fp16_v2.json` |
| 7b | gsm8k100 | uniform_int8/csi_guided | 0.04 | 3 | `qwen25_7b_gsm8k100_uniform_int8_v2.json` |
| 7b | gsm8k100 | allocation/loss_sensitive_4to8 | 0.03 | 4 | `qwen25_7b_gsm8k100_single_n64_3to4_budget3p5_v2.json` |
| 7b | gsm8k100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0.02 | 5 | `qwen25_7b_gsm8k100_csi_n64_3to4_budget3p5_v2.json` |
| 7b | gsm8k100 | uniform_int2/csi_guided | 0.00 | 6 | `qwen25_7b_gsm8k100_uniform_int2_v2.json` |
| 7b | gsm8k100 | uniform_int3/csi_guided | 0.00 | 7 | `qwen25_7b_gsm8k100_uniform_int3_v2.json` |
| 7b | mmlu100 | fp16/csi_guided | 0.65 | 1 | `qwen25_7b_mmlu100_fp16_v2.json` |
| 7b | mmlu100 | uniform_int8/csi_guided | 0.65 | 2 | `qwen25_7b_mmlu100_uniform_int8_v2.json` |
| 7b | mmlu100 | uniform_int4/csi_guided | 0.63 | 3 | `qwen25_7b_mmlu100_uniform_int4_v2.json` |
| 7b | mmlu100 | allocation/loss_sensitive_4to8 | 0.55 | 4 | `qwen25_7b_mmlu100_single_n64_3to4_budget3p5_v2.json` |
| 7b | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0.53 | 5 | `qwen25_7b_mmlu100_csi_n64_3to4_budget3p5_v2.json` |
| 7b | mmlu100 | uniform_int3/csi_guided | 0.08 | 6 | `qwen25_7b_mmlu100_uniform_int3_v2.json` |
| 7b | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0.01 | 7 | `qwen25_7b_mmlu100_csi_n64_budget3_v2.json` |
| 7b | mmlu100 | allocation/loss_sensitive_4to8 | 0.00 | 8 | `qwen25_7b_mmlu100_single_n64_budget3_v2.json` |
| 7b | mmlu100 | uniform_int2/csi_guided | 0.00 | 9 | `qwen25_7b_mmlu100_uniform_int2_v2.json` |
| 7b_awq | gsm8k100 | awq_int4_checkpoint/awq_int4_checkpoint | 0.02 | 1 | `qwen25_7b_awq_gsm8k100_v2.json` |
| 7b_awq | mmlu100 | awq_int4_checkpoint/awq_int4_checkpoint | 0.64 | 1 | `qwen25_7b_awq_mmlu100_v2.json` |
| phi3_mini | gsm8k100 | fp16/csi_guided | 0.02 | 1 | `phi3_mini_gsm8k100_fp16_v2.json` |
| phi3_mini | gsm8k100 | uniform_int4/csi_guided | 0.02 | 2 | `phi3_mini_gsm8k100_uniform_int4_v2.json` |
| phi3_mini | gsm8k100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0.00 | 3 | `phi3_mini_gsm8k100_csi_n64_budget3_v2.json` |
| phi3_mini | gsm8k100 | allocation/loss_sensitive_4to8 | 0.00 | 4 | `phi3_mini_gsm8k100_single_n64_budget3_v2.json` |
| phi3_mini | mmlu100 | uniform_int4/csi_guided | 0.42 | 1 | `phi3_mini_mmlu100_uniform_int4_v2.json` |
| phi3_mini | mmlu100 | fp16/csi_guided | 0.41 | 2 | `phi3_mini_mmlu100_fp16_v2.json` |
| phi3_mini | mmlu100 | allocation/loss_sensitive_4to8 | 0.09 | 3 | `phi3_mini_mmlu100_single_n64_budget3_v2.json` |
| phi3_mini | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0.08 | 4 | `phi3_mini_mmlu100_csi_n64_budget3_v2.json` |
