# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T22:03:57Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[0]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 4 / 6 |
| exact match rate | 0.6667 |
| mean char edit similarity | 0.8248 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 0.7620 |
| mean baseline tokens/s | 23.0367 |
| mean fused tokens/s | 22.3332 |
| mean fused/baseline speed | 0.9695x |
| median baseline TTFT s | 0.054166 |
| median fused TTFT s | 0.199011 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `576 / 192`
- Cache hits / misses: `384 / 192`
- Fused CUDA event sum: `1477.6830 ms`
- Peak CUDA memory: `1172.42 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 20.6199 | 14.4866 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` |
| 1 | True | 1.0000 | 1.0000 | 22.1638 | 21.9426 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | True | 1.0000 | 1.0000 | 22.5767 | 24.9477 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | True | 1.0000 | 1.0000 | 22.4032 | 24.7799 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` |
| 4 | False | 0.4149 | 0.2653 | 27.4453 | 22.3264 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main reason for the instability of quantization when using calibra` |
| 5 | False | 0.5337 | 0.3067 | 23.0115 | 25.5162 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a key part of the transformer architecture, but it's not the only part of the model. What is` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
