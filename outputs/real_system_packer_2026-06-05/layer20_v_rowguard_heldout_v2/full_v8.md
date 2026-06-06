# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-06T01:17:51Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `12`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 12 / 12 |
| exact match rate | 1.0000 |
| mean char edit similarity | 1.0000 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 1.0000 |
| mean baseline tokens/s | 27.3189 |
| mean fused tokens/s | 22.8611 |
| mean fused/baseline speed | 0.8368x |
| median baseline TTFT s | 0.037552 |
| median fused TTFT s | 0.047235 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `3456 / 1152`
- Cache hits / misses: `2304 / 1152`
- Fused CUDA event sum: `873.8921 ms`
- Peak CUDA memory: `1164.55 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 20.4663 | 14.6820 | ` Also, explain the role of the calibration set in the process of quantization. Additionally, explain` | ` Also, explain the role of the calibration set in the process of quantization. Additionally, explain` |
| 1 | True | 1.0000 | 1.0000 | 27.7728 | 26.6171 | ` The JSON should have a key-value pair for each of the three keys, and the values should be the corr` | ` The JSON should have a key-value pair for each of the three keys, and the values should be the corr` |
| 2 | True | 1.0000 | 1.0000 | 26.9128 | 20.2532 | ` The weights are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1` | ` The weights are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1` |
| 3 | True | 1.0000 | 1.0000 | 31.5237 | 24.8074 | ` The function should be named `multiply` and have parameters `input` and `output`, each of which is ` | ` The function should be named `multiply` and have parameters `input` and `output`, each of which is ` |
| 4 | True | 1.0000 | 1.0000 | 23.8396 | 22.0533 | ` One of the ways is to use a **search engine**. The other is to use a **search engine**. Also, provi` | ` One of the ways is to use a **search engine**. The other is to use a **search engine**. Also, provi` |
| 5 | True | 1.0000 | 1.0000 | 26.9434 | 21.7933 | ` What is the relationship between the attention value projection and the attention value in the mode` | ` What is the relationship between the attention value projection and the attention value in the mode` |
| 6 | True | 1.0000 | 1.0000 | 28.9217 | 24.1153 | ` The ablation plan should include the following: 1) the baseline, 2) the first ablation, 3) the seco` | ` The ablation plan should include the following: 1) the baseline, 2) the first ablation, 3) the seco` |
| 7 | True | 1.0000 | 1.0000 | 27.1835 | 25.2023 | ` The answer is in Chinese. The answer is in Chinese. The answer is in Chinese. The answer is in Chin` | ` The answer is in Chinese. The answer is in Chinese. The answer is in Chinese. The answer is in Chin` |
| 8 | True | 1.0000 | 1.0000 | 29.5821 | 22.1959 | ` Also, explain what each metric means. Answer: The question asks for **two deployment metrics** for ` | ` Also, explain what each metric means. Answer: The question asks for **two deployment metrics** for ` |
| 9 | True | 1.0000 | 1.0000 | 33.6953 | 23.8377 | ` Also, provide a list of 10 key points that should be included in the README for the project. The RE` | ` Also, provide a list of 10 key points that should be included in the README for the project. The RE` |
| 10 | True | 1.0000 | 1.0000 | 23.3898 | 21.4929 | ` Additionally, what are the implications of this approach on the data processing pipeline and the da` | ` Additionally, what are the implications of this approach on the data processing pipeline and the da` |
| 11 | True | 1.0000 | 1.0000 | 27.5960 | 27.2833 | ` What is the difference between the quantization policy and the quantization method? What is the dif` | ` What is the difference between the quantization policy and the quantization method? What is the dif` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
