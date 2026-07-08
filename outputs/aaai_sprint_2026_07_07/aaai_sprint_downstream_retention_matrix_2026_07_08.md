# AAAI Sprint Downstream Retention Matrix

Generated: 2026-07-09

Consolidated downstream retention artifacts for AAAI sprint. GSM8K uses data_eval/public_task_benchmark_v1/gsm8k_test_subset100.jsonl; MMLU100 uses the broad 5x20 MMLU subset unless noted in artifact history. Updated 2026-07-09 with Qwen2.5-7B AWQ checkpoint baseline rows and GPTQ blocker summary.

| Model | Task | Method | Exact / Total | Accuracy | Artifact |
|---|---|---|---:|---:|---|
| 14b_awq | gsm8k100 | awq_checkpoint/csi_guided | 13 / 100 | 0.13 | `qwen25_14b_awq_gsm8k100_v2.json` |
| 14b_awq | mmlu100 | awq_checkpoint/csi_guided | 65 / 100 | 0.65 | `qwen25_14b_awq_mmlu100_v2.json` |
| 1p5b | gsm8k100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0 / 100 | 0.00 | `qwen25_1p5b_gsm8k100_csi_n64_budget3_v2.json` |
| 1p5b | gsm8k100 | allocation/loss_sensitive_4to8 | 2 / 100 | 0.02 | `qwen25_1p5b_gsm8k100_single_n64_budget3_v2.json` |
| 1p5b | gsm8k100 | fp16/csi_guided | 3 / 100 | 0.03 | `qwen25_1p5b_gsm8k100_fp16_v2.json` |
| 1p5b | gsm8k100 | uniform_int2/csi_guided | 0 / 100 | 0.00 | `qwen25_1p5b_gsm8k100_uniform_int2_v2.json` |
| 1p5b | gsm8k100 | uniform_int3/csi_guided | 0 / 100 | 0.00 | `qwen25_1p5b_gsm8k100_uniform_int3_v2.json` |
| 1p5b | gsm8k100 | uniform_int4/csi_guided | 2 / 100 | 0.02 | `qwen25_1p5b_gsm8k100_uniform_int4_v2.json` |
| 1p5b | gsm8k100 | uniform_int8/csi_guided | 0 / 100 | 0.00 | `qwen25_1p5b_gsm8k100_uniform_int8_v2.json` |
| 1p5b | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 1 / 100 | 0.01 | `qwen25_1p5b_mmlu100_csi_n64_budget3_v2.json` |
| 1p5b | mmlu100 | allocation/loss_sensitive_4to8 | 0 / 100 | 0.00 | `qwen25_1p5b_mmlu100_single_n64_budget3_v2.json` |
| 1p5b | mmlu100 | fp16/csi_guided | 54 / 100 | 0.54 | `qwen25_1p5b_mmlu100_fp16_v2.json` |
| 1p5b | mmlu100 | uniform_int2/csi_guided | 0 / 100 | 0.00 | `qwen25_1p5b_mmlu100_uniform_int2_v2.json` |
| 1p5b | mmlu100 | uniform_int3/csi_guided | 4 / 100 | 0.04 | `qwen25_1p5b_mmlu100_uniform_int3_v2.json` |
| 1p5b | mmlu100 | uniform_int4/csi_guided | 41 / 100 | 0.41 | `qwen25_1p5b_mmlu100_uniform_int4_v2.json` |
| 1p5b | mmlu100 | uniform_int8/csi_guided | 55 / 100 | 0.55 | `qwen25_1p5b_mmlu100_uniform_int8_v2.json` |
| 3b | gsm8k100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 3 / 100 | 0.03 | `qwen25_3b_gsm8k100_csi_n64_3to4_budget3p5_v2.json` |
| 3b | gsm8k100 | allocation/loss_sensitive_4to8 | 2 / 100 | 0.02 | `qwen25_3b_gsm8k100_single_n64_3to4_budget3p5_v2.json` |
| 3b | gsm8k100 | fp16/csi_guided | 6 / 100 | 0.06 | `qwen25_3b_gsm8k100_fp16_v2.json` |
| 3b | gsm8k100 | uniform_int2/csi_guided | 0 / 100 | 0.00 | `qwen25_3b_gsm8k100_uniform_int2_v2.json` |
| 3b | gsm8k100 | uniform_int3/csi_guided | 0 / 100 | 0.00 | `qwen25_3b_gsm8k100_uniform_int3_v2.json` |
| 3b | gsm8k100 | uniform_int4/csi_guided | 5 / 100 | 0.05 | `qwen25_3b_gsm8k100_uniform_int4_v2.json` |
| 3b | gsm8k100 | uniform_int8/csi_guided | 6 / 100 | 0.06 | `qwen25_3b_gsm8k100_uniform_int8_v2.json` |
| 3b | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 36 / 100 | 0.36 | `qwen25_3b_mmlu100_csi_n64_3to4_budget3p5_v2.json` |
| 3b | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 1 / 100 | 0.01 | `qwen25_3b_mmlu100_csi_n64_budget3_v2.json` |
| 3b | mmlu100 | allocation/loss_sensitive_4to8 | 30 / 100 | 0.30 | `qwen25_3b_mmlu100_single_n64_3to4_budget3p5_v2.json` |
| 3b | mmlu100 | allocation/loss_sensitive_4to8 | 4 / 100 | 0.04 | `qwen25_3b_mmlu100_single_n64_budget3_v2.json` |
| 3b | mmlu100 | fp16/csi_guided | 52 / 100 | 0.52 | `qwen25_3b_mmlu100_fp16_v2.json` |
| 3b | mmlu100 | uniform_int2/csi_guided | 0 / 100 | 0.00 | `qwen25_3b_mmlu100_uniform_int2_v2.json` |
| 3b | mmlu100 | uniform_int3/csi_guided | 2 / 100 | 0.02 | `qwen25_3b_mmlu100_uniform_int3_v2.json` |
| 3b | mmlu100 | uniform_int4/csi_guided | 42 / 100 | 0.42 | `qwen25_3b_mmlu100_uniform_int4_v2.json` |
| 3b | mmlu100 | uniform_int8/csi_guided | 52 / 100 | 0.52 | `qwen25_3b_mmlu100_uniform_int8_v2.json` |
| 7b | gsm8k100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 2 / 100 | 0.02 | `qwen25_7b_gsm8k100_csi_n64_3to4_budget3p5_v2.json` |
| 7b | gsm8k100 | allocation/loss_sensitive_4to8 | 3 / 100 | 0.03 | `qwen25_7b_gsm8k100_single_n64_3to4_budget3p5_v2.json` |
| 7b | gsm8k100 | fp16/csi_guided | 4 / 100 | 0.04 | `qwen25_7b_gsm8k100_fp16_v2.json` |
| 7b | gsm8k100 | uniform_int2/csi_guided | 0 / 100 | 0.00 | `qwen25_7b_gsm8k100_uniform_int2_v2.json` |
| 7b | gsm8k100 | uniform_int3/csi_guided | 0 / 100 | 0.00 | `qwen25_7b_gsm8k100_uniform_int3_v2.json` |
| 7b | gsm8k100 | uniform_int4/csi_guided | 5 / 100 | 0.05 | `qwen25_7b_gsm8k100_uniform_int4_v2.json` |
| 7b | gsm8k100 | uniform_int8/csi_guided | 4 / 100 | 0.04 | `qwen25_7b_gsm8k100_uniform_int8_v2.json` |
| 7b | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 53 / 100 | 0.53 | `qwen25_7b_mmlu100_csi_n64_3to4_budget3p5_v2.json` |
| 7b | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 1 / 100 | 0.01 | `qwen25_7b_mmlu100_csi_n64_budget3_v2.json` |
| 7b | mmlu100 | allocation/loss_sensitive_4to8 | 55 / 100 | 0.55 | `qwen25_7b_mmlu100_single_n64_3to4_budget3p5_v2.json` |
| 7b | mmlu100 | allocation/loss_sensitive_4to8 | 0 / 100 | 0.00 | `qwen25_7b_mmlu100_single_n64_budget3_v2.json` |
| 7b | mmlu100 | fp16/csi_guided | 65 / 100 | 0.65 | `qwen25_7b_mmlu100_fp16_v2.json` |
| 7b | mmlu100 | uniform_int2/csi_guided | 0 / 100 | 0.00 | `qwen25_7b_mmlu100_uniform_int2_v2.json` |
| 7b | mmlu100 | uniform_int3/csi_guided | 8 / 100 | 0.08 | `qwen25_7b_mmlu100_uniform_int3_v2.json` |
| 7b | mmlu100 | uniform_int4/csi_guided | 63 / 100 | 0.63 | `qwen25_7b_mmlu100_uniform_int4_v2.json` |
| 7b | mmlu100 | uniform_int8/csi_guided | 65 / 100 | 0.65 | `qwen25_7b_mmlu100_uniform_int8_v2.json` |
| 7b_awq | gsm8k100 | awq_int4_checkpoint/awq_int4_checkpoint | 2 / 100 | 0.02 | `qwen25_7b_awq_gsm8k100_v2.json` |
| 7b_awq | mmlu100 | awq_int4_checkpoint/awq_int4_checkpoint | 64 / 100 | 0.64 | `qwen25_7b_awq_mmlu100_v2.json` |
| phi3_mini | gsm8k100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 0 / 100 | 0.00 | `phi3_mini_gsm8k100_csi_n64_budget3_v2.json` |
| phi3_mini | gsm8k100 | allocation/loss_sensitive_4to8 | 0 / 100 | 0.00 | `phi3_mini_gsm8k100_single_n64_budget3_v2.json` |
| phi3_mini | gsm8k100 | fp16/csi_guided | 2 / 100 | 0.02 | `phi3_mini_gsm8k100_fp16_v2.json` |
| phi3_mini | gsm8k100 | uniform_int4/csi_guided | 2 / 100 | 0.02 | `phi3_mini_gsm8k100_uniform_int4_v2.json` |
| phi3_mini | mmlu100 | allocation/loss_sensitive_robust_lcb_consensus_4to8 | 8 / 100 | 0.08 | `phi3_mini_mmlu100_csi_n64_budget3_v2.json` |
| phi3_mini | mmlu100 | allocation/loss_sensitive_4to8 | 9 / 100 | 0.09 | `phi3_mini_mmlu100_single_n64_budget3_v2.json` |
| phi3_mini | mmlu100 | fp16/csi_guided | 41 / 100 | 0.41 | `phi3_mini_mmlu100_fp16_v2.json` |
| phi3_mini | mmlu100 | uniform_int4/csi_guided | 42 / 100 | 0.42 | `phi3_mini_mmlu100_uniform_int4_v2.json` |
