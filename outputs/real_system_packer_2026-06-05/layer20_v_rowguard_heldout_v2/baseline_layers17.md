# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-06T01:16:41Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7]`
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
| mean baseline tokens/s | 26.9589 |
| mean fused tokens/s | 24.6618 |
| mean fused/baseline speed | 0.9148x |
| median baseline TTFT s | 0.036310 |
| median fused TTFT s | 0.046244 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `2304 / 768`
- Cache hits / misses: `1536 / 768`
- Fused CUDA event sum: `1127.1578 ms`
- Peak CUDA memory: `1168.49 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 26.5173 | 18.1110 | ` Also, explain the role of the calibration set in the process of quantization. Additionally, explain` | ` Also, explain the role of the calibration set in the process of quantization. Additionally, explain` |
| 1 | True | 1.0000 | 1.0000 | 23.0564 | 26.4455 | ` The JSON should have a key-value pair for each of the three keys, and the values should be the corr` | ` The JSON should have a key-value pair for each of the three keys, and the values should be the corr` |
| 2 | True | 1.0000 | 1.0000 | 30.8638 | 25.7262 | ` The weights are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1` | ` The weights are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1` |
| 3 | True | 1.0000 | 1.0000 | 23.1344 | 23.4528 | ` The function should be named `multiply` and have parameters `input` and `output`, each of which is ` | ` The function should be named `multiply` and have parameters `input` and `output`, each of which is ` |
| 4 | True | 1.0000 | 1.0000 | 28.7866 | 27.8795 | ` One of the ways is to use a **search engine**. The other is to use a **search engine**. Also, provi` | ` One of the ways is to use a **search engine**. The other is to use a **search engine**. Also, provi` |
| 5 | True | 1.0000 | 1.0000 | 30.4862 | 20.1543 | ` What is the relationship between the attention value projection and the attention value in the mode` | ` What is the relationship between the attention value projection and the attention value in the mode` |
| 6 | True | 1.0000 | 1.0000 | 29.5109 | 25.7428 | ` The ablation plan should include the following: 1) the baseline, 2) the first ablation, 3) the seco` | ` The ablation plan should include the following: 1) the baseline, 2) the first ablation, 3) the seco` |
| 7 | True | 1.0000 | 1.0000 | 27.2694 | 20.8928 | ` The answer is in Chinese. The answer is in Chinese. The answer is in Chinese. The answer is in Chin` | ` The answer is in Chinese. The answer is in Chinese. The answer is in Chinese. The answer is in Chin` |
| 8 | True | 1.0000 | 1.0000 | 23.2578 | 29.4063 | ` Also, explain what each metric means. Answer: The question asks for **two deployment metrics** for ` | ` Also, explain what each metric means. Answer: The question asks for **two deployment metrics** for ` |
| 9 | True | 1.0000 | 1.0000 | 27.4521 | 21.8119 | ` Also, provide a list of 10 key points that should be included in the README for the project. The RE` | ` Also, provide a list of 10 key points that should be included in the README for the project. The RE` |
| 10 | True | 1.0000 | 1.0000 | 26.0669 | 27.5615 | ` Additionally, what are the implications of this approach on the data processing pipeline and the da` | ` Additionally, what are the implications of this approach on the data processing pipeline and the da` |
| 11 | True | 1.0000 | 1.0000 | 27.1049 | 28.7571 | ` What is the difference between the quantization policy and the quantization method? What is the dif` | ` What is the difference between the quantization policy and the quantization method? What is the dif` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
