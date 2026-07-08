# AAAI Sprint Win/Loss and Average Rank

Generated: 2026-07-09

## Average Rank

| Method | Average rank | N |
|---|---:|---:|
| awq_checkpoint/csi_guided | 1.00 | 2 |
| fp16/csi_guided | 1.38 | 8 |
| uniform_int4/csi_guided | 2.38 | 8 |
| uniform_int8/csi_guided | 2.83 | 6 |
| allocation/loss_sensitive_4to8 | 4.70 | 10 |
| allocation/loss_sensitive_robust_lcb_consensus_4to8 | 4.90 | 10 |
| uniform_int3/csi_guided | 6.17 | 6 |
| uniform_int2/csi_guided | 7.00 | 6 |

## CSI Win/Loss vs Available Baselines

Counts: win `19`, lose `39`, tie `4`.

| Model | Task | Baseline | Result | Ours | Baseline |
|---|---|---|---|---:|---:|
| 1p5b | gsm8k100 | `qwen25_1p5b_gsm8k100_fp16_v2.json` | lose | 0.00 | 0.03 |
| 1p5b | gsm8k100 | `qwen25_1p5b_gsm8k100_single_n64_budget3_v2.json` | lose | 0.00 | 0.02 |
| 1p5b | gsm8k100 | `qwen25_1p5b_gsm8k100_uniform_int2_v2.json` | tie | 0.00 | 0.00 |
| 1p5b | gsm8k100 | `qwen25_1p5b_gsm8k100_uniform_int3_v2.json` | tie | 0.00 | 0.00 |
| 1p5b | gsm8k100 | `qwen25_1p5b_gsm8k100_uniform_int4_v2.json` | lose | 0.00 | 0.02 |
| 1p5b | gsm8k100 | `qwen25_1p5b_gsm8k100_uniform_int8_v2.json` | tie | 0.00 | 0.00 |
| 1p5b | mmlu100 | `qwen25_1p5b_mmlu100_fp16_v2.json` | lose | 0.01 | 0.54 |
| 1p5b | mmlu100 | `qwen25_1p5b_mmlu100_single_n64_budget3_v2.json` | win | 0.01 | 0.00 |
| 1p5b | mmlu100 | `qwen25_1p5b_mmlu100_uniform_int2_v2.json` | win | 0.01 | 0.00 |
| 1p5b | mmlu100 | `qwen25_1p5b_mmlu100_uniform_int3_v2.json` | lose | 0.01 | 0.04 |
| 1p5b | mmlu100 | `qwen25_1p5b_mmlu100_uniform_int4_v2.json` | lose | 0.01 | 0.41 |
| 1p5b | mmlu100 | `qwen25_1p5b_mmlu100_uniform_int8_v2.json` | lose | 0.01 | 0.55 |
| 3b | gsm8k100 | `qwen25_3b_gsm8k100_fp16_v2.json` | lose | 0.03 | 0.06 |
| 3b | gsm8k100 | `qwen25_3b_gsm8k100_single_n64_3to4_budget3p5_v2.json` | win | 0.03 | 0.02 |
| 3b | gsm8k100 | `qwen25_3b_gsm8k100_uniform_int2_v2.json` | win | 0.03 | 0.00 |
| 3b | gsm8k100 | `qwen25_3b_gsm8k100_uniform_int3_v2.json` | win | 0.03 | 0.00 |
| 3b | gsm8k100 | `qwen25_3b_gsm8k100_uniform_int4_v2.json` | lose | 0.03 | 0.05 |
| 3b | gsm8k100 | `qwen25_3b_gsm8k100_uniform_int8_v2.json` | lose | 0.03 | 0.06 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_csi_n64_budget3_v2.json` | win | 0.36 | 0.01 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_fp16_v2.json` | lose | 0.36 | 0.52 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_single_n64_3to4_budget3p5_v2.json` | win | 0.36 | 0.30 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_single_n64_budget3_v2.json` | win | 0.36 | 0.04 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_uniform_int2_v2.json` | win | 0.36 | 0.00 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_uniform_int3_v2.json` | win | 0.36 | 0.02 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_uniform_int4_v2.json` | lose | 0.36 | 0.42 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_uniform_int8_v2.json` | lose | 0.36 | 0.52 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_csi_n64_3to4_budget3p5_v2.json` | lose | 0.01 | 0.36 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_fp16_v2.json` | lose | 0.01 | 0.52 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_single_n64_3to4_budget3p5_v2.json` | lose | 0.01 | 0.30 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_single_n64_budget3_v2.json` | lose | 0.01 | 0.04 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_uniform_int2_v2.json` | win | 0.01 | 0.00 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_uniform_int3_v2.json` | lose | 0.01 | 0.02 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_uniform_int4_v2.json` | lose | 0.01 | 0.42 |
| 3b | mmlu100 | `qwen25_3b_mmlu100_uniform_int8_v2.json` | lose | 0.01 | 0.52 |
| 7b | gsm8k100 | `qwen25_7b_gsm8k100_fp16_v2.json` | lose | 0.02 | 0.04 |
| 7b | gsm8k100 | `qwen25_7b_gsm8k100_single_n64_3to4_budget3p5_v2.json` | lose | 0.02 | 0.03 |
| 7b | gsm8k100 | `qwen25_7b_gsm8k100_uniform_int2_v2.json` | win | 0.02 | 0.00 |
| 7b | gsm8k100 | `qwen25_7b_gsm8k100_uniform_int3_v2.json` | win | 0.02 | 0.00 |
| 7b | gsm8k100 | `qwen25_7b_gsm8k100_uniform_int4_v2.json` | lose | 0.02 | 0.05 |
| 7b | gsm8k100 | `qwen25_7b_gsm8k100_uniform_int8_v2.json` | lose | 0.02 | 0.04 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_csi_n64_budget3_v2.json` | win | 0.53 | 0.01 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_fp16_v2.json` | lose | 0.53 | 0.65 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_single_n64_3to4_budget3p5_v2.json` | lose | 0.53 | 0.55 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_single_n64_budget3_v2.json` | win | 0.53 | 0.00 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_uniform_int2_v2.json` | win | 0.53 | 0.00 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_uniform_int3_v2.json` | win | 0.53 | 0.08 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_uniform_int4_v2.json` | lose | 0.53 | 0.63 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_uniform_int8_v2.json` | lose | 0.53 | 0.65 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_csi_n64_3to4_budget3p5_v2.json` | lose | 0.01 | 0.53 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_fp16_v2.json` | lose | 0.01 | 0.65 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_single_n64_3to4_budget3p5_v2.json` | lose | 0.01 | 0.55 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_single_n64_budget3_v2.json` | win | 0.01 | 0.00 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_uniform_int2_v2.json` | win | 0.01 | 0.00 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_uniform_int3_v2.json` | lose | 0.01 | 0.08 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_uniform_int4_v2.json` | lose | 0.01 | 0.63 |
| 7b | mmlu100 | `qwen25_7b_mmlu100_uniform_int8_v2.json` | lose | 0.01 | 0.65 |
| phi3_mini | gsm8k100 | `phi3_mini_gsm8k100_fp16_v2.json` | lose | 0.00 | 0.02 |
| phi3_mini | gsm8k100 | `phi3_mini_gsm8k100_single_n64_budget3_v2.json` | tie | 0.00 | 0.00 |
| phi3_mini | gsm8k100 | `phi3_mini_gsm8k100_uniform_int4_v2.json` | lose | 0.00 | 0.02 |
| phi3_mini | mmlu100 | `phi3_mini_mmlu100_fp16_v2.json` | lose | 0.08 | 0.41 |
| phi3_mini | mmlu100 | `phi3_mini_mmlu100_single_n64_budget3_v2.json` | lose | 0.08 | 0.09 |
| phi3_mini | mmlu100 | `phi3_mini_mmlu100_uniform_int4_v2.json` | lose | 0.08 | 0.42 |
