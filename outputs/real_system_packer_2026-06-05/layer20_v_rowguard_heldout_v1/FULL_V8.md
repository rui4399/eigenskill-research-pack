# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-06T00:23:08Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `12`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 11 / 12 |
| exact match rate | 0.9167 |
| mean char edit similarity | 0.9398 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 0.9172 |
| mean baseline tokens/s | 25.9967 |
| mean fused tokens/s | 24.5068 |
| mean fused/baseline speed | 0.9427x |
| median baseline TTFT s | 0.035161 |
| median fused TTFT s | 0.046972 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `3456 / 1152`
- Cache hits / misses: `2304 / 1152`
- Fused CUDA event sum: `771.9539 ms`
- Peak CUDA memory: `1164.55 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 25.4700 | 17.4093 | ` The summary should include the following points: 1) the use of mixed-precision in the training phas` | ` The summary should include the following points: 1) the use of mixed-precision in the training phas` |
| 1 | True | 1.0000 | 1.0000 | 24.5583 | 23.5547 | ` The JSON should be valid and have the correct syntax. Answer:  ```json {   "method": "calibration",` | ` The JSON should be valid and have the correct syntax. Answer:  ```json {   "method": "calibration",` |
| 2 | True | 1.0000 | 1.0000 | 27.6465 | 24.7170 | ` The answer is 1000. So, the answer is 1000. Answer: 1000  The question asks how many` | ` The answer is 1000. So, the answer is 1000. Answer: 1000  The question asks how many` |
| 3 | True | 1.0000 | 1.0000 | 28.6289 | 22.1128 | ` The function should take a 2D array of integers, and return a 2D array of integers. The function sh` | ` The function should take a 2D array of integers, and return a 2D array of integers. The function sh` |
| 4 | False | 0.2771 | 0.0060 | 25.1612 | 27.1392 | ` The answer should be in a sentence. Answer: The prompt-conditioned precision guard might overfit a ` | ` What are the two reasons? What are the two reasons for overfitting a large prompt suite? What is th` |
| 5 | True | 1.0000 | 1.0000 | 26.1442 | 25.7259 | ` Also, explain in one sentence why higher precision can sometimes make a quantized replacement more ` | ` Also, explain in one sentence why higher precision can sometimes make a quantized replacement more ` |
| 6 | True | 1.0000 | 1.0000 | 29.6002 | 21.3862 | ` The experiment should include a control group and a test group, and the results should be analyzed ` | ` The experiment should include a control group and a test group, and the results should be analyzed ` |
| 7 | True | 1.0000 | 1.0000 | 25.3564 | 27.4234 | ` Also, explain what each term means. Use the example of a specific case where the local reconstructi` | ` Also, explain what each term means. Use the example of a specific case where the local reconstructi` |
| 8 | True | 1.0000 | 1.0000 | 25.5721 | 28.1055 | ` Also, explain what each metric represents.  **A.** **Perplexity**   **B.** **Accuracy**   **C.** **` | ` Also, explain what each metric represents.  **A.** **Perplexity**   **B.** **Accuracy**   **C.** **` |
| 9 | True | 1.0000 | 1.0000 | 26.2506 | 26.1065 | ` The label should be in a formal tone, and include the following elements: 1) a title, 2) a descript` | ` The label should be in a formal tone, and include the following elements: 1) a title, 2) a descript` |
| 10 | True | 1.0000 | 1.0000 | 23.8979 | 28.9398 | ` What is the purpose of the KV-cache in the attention projection replacement? What is the purpose of` | ` What is the purpose of the KV-cache in the attention projection replacement? What is the purpose of` |
| 11 | True | 1.0000 | 1.0000 | 23.6735 | 21.4614 | ` Also, explain why layer 1 may need separate treatment in QKV replacement. Additionally, explain why` | ` Also, explain why layer 1 may need separate treatment in QKV replacement. Additionally, explain why` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
