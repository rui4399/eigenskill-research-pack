# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T22:39:08Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 27]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 5 / 6 |
| exact match rate | 0.8333 |
| mean char edit similarity | 0.9223 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 0.8845 |
| mean baseline tokens/s | 21.0276 |
| mean fused tokens/s | 22.8787 |
| mean fused/baseline speed | 1.0880x |
| median baseline TTFT s | 0.048283 |
| median fused TTFT s | 0.042070 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1728 / 576`
- Cache hits / misses: `1152 / 576`
- Fused CUDA event sum: `680.7968 ms`
- Peak CUDA memory: `1164.55 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 20.9045 | 15.8995 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` |
| 1 | True | 1.0000 | 1.0000 | 18.4287 | 22.5880 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | True | 1.0000 | 1.0000 | 20.3733 | 27.2655 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | True | 1.0000 | 1.0000 | 22.7608 | 20.6927 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` |
| 4 | True | 1.0000 | 1.0000 | 20.7907 | 25.8794 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` |
| 5 | False | 0.5337 | 0.3067 | 22.9073 | 24.9469 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a key part of the transformer architecture, but it's not the only part of the model. What is` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
