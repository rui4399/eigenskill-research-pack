# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T22:11:05Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[0, 1, 7]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 3 / 6 |
| exact match rate | 0.5000 |
| mean char edit similarity | 0.7692 |
| median char edit similarity | 0.8333 |
| mean common prefix ratio | 0.6555 |
| mean baseline tokens/s | 24.0200 |
| mean fused tokens/s | 24.6225 |
| mean fused/baseline speed | 1.0251x |
| median baseline TTFT s | 0.042094 |
| median fused TTFT s | 0.045148 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1728 / 576`
- Cache hits / misses: `1152 / 576`
- Fused CUDA event sum: `793.7528 ms`
- Peak CUDA memory: `1164.55 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 21.9408 | 15.7196 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` |
| 1 | True | 1.0000 | 1.0000 | 27.0095 | 27.4546 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | True | 1.0000 | 1.0000 | 24.6334 | 26.9759 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | False | 0.6667 | 0.3607 | 24.2984 | 25.2729 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both 4-byte and 8-byte integers. The function should be able ` |
| 4 | False | 0.4149 | 0.2653 | 22.4361 | 27.8029 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main reason for the instability of quantization when using calibra` |
| 5 | False | 0.5337 | 0.3067 | 23.8019 | 24.5093 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a key part of the transformer architecture, but it's not the only part of the model. What is` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
