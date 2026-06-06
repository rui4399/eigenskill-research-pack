# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T23:00:30Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 1 / 6 |
| exact match rate | 0.1667 |
| mean char edit similarity | 0.6365 |
| median char edit similarity | 0.6011 |
| mean common prefix ratio | 0.5181 |
| mean baseline tokens/s | 26.5422 |
| mean fused tokens/s | 25.5309 |
| mean fused/baseline speed | 0.9619x |
| median baseline TTFT s | 0.033719 |
| median fused TTFT s | 0.049337 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9894x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1728 / 576`
- Cache hits / misses: `1152 / 576`
- Fused CUDA event sum: `743.4440 ms`
- Peak CUDA memory: `1164.30 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | False | 0.3614 | 0.0904 | 22.0720 | 17.5248 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain why it's important to use mixed-precision in machine learning models, and give an exa` |
| 1 | False | 0.8198 | 0.7673 | 25.0872 | 25.3368 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | False | 0.6903 | 0.6176 | 27.2250 | 26.8670 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is packed in 4 bytes per row) Answer: Th` |
| 3 | True | 1.0000 | 1.0000 | 24.2135 | 28.1921 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` |
| 4 | False | 0.5119 | 0.3265 | 29.6319 | 26.0028 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main idea is to explain two reasons why calibration data can make ` |
| 5 | False | 0.4356 | 0.3067 | 31.0237 | 29.2620 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a key part of the transformer architecture, and it's used to do the following: a. __________` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
