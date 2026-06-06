# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T22:38:13Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 5 / 6 |
| exact match rate | 0.8333 |
| mean char edit similarity | 0.9383 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 0.9096 |
| mean baseline tokens/s | 26.8500 |
| mean fused tokens/s | 22.7600 |
| mean fused/baseline speed | 0.8477x |
| median baseline TTFT s | 0.040277 |
| median fused TTFT s | 0.048184 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1728 / 576`
- Cache hits / misses: `1152 / 576`
- Fused CUDA event sum: `670.2291 ms`
- Peak CUDA memory: `1164.55 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | False | 0.6301 | 0.4578 | 25.7864 | 12.6793 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision. Please provide an exampl` |
| 1 | True | 1.0000 | 1.0000 | 31.4342 | 23.4372 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | True | 1.0000 | 1.0000 | 22.2939 | 21.2127 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | True | 1.0000 | 1.0000 | 28.6320 | 27.9907 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` |
| 4 | True | 1.0000 | 1.0000 | 20.7022 | 25.5459 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` |
| 5 | True | 1.0000 | 1.0000 | 32.2512 | 25.6944 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
