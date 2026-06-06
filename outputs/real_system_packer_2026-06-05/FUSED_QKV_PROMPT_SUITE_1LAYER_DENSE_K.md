# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T21:55:37Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[0]`
Dense roles: `['k_proj']`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 1 / 6 |
| exact match rate | 0.1667 |
| mean char edit similarity | 0.5911 |
| median char edit similarity | 0.5635 |
| mean common prefix ratio | 0.3519 |
| mean baseline tokens/s | 26.0799 |
| mean fused tokens/s | 25.2282 |
| mean fused/baseline speed | 0.9673x |
| median baseline TTFT s | 0.049421 |
| median fused TTFT s | 0.048342 |

## Replacement Runtime

- Replacement compression vs FP32: `6.1682x`
- Dense role calls: `192`
- Wrapper calls / fused compute calls: `384 / 192`
- Cache hits / misses: `192 / 192`
- Fused CUDA event sum: `636.4455 ms`
- Peak CUDA memory: `1173.42 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 24.4323 | 19.0463 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` |
| 1 | False | 0.3899 | 0.1006 | 31.0774 | 30.6135 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to quantize a model. The risk is that the model might not be able to run on a GPU. The ` |
| 2 | False | 0.7290 | 0.3235 | 26.6703 | 25.2612 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit row, and that the row is packed in 4 bytes, and that the row is pac` |
| 3 | False | 0.7121 | 0.3607 | 29.4710 | 20.9483 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both 4 and 8-bit integers, and the function should be able to` |
| 4 | False | 0.4149 | 0.2653 | 21.7151 | 31.0243 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main reason for the instability of quantization when using calibra` |
| 5 | False | 0.3006 | 0.0613 | 23.1134 | 24.4754 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a type of projection that is used in the training of neural networks. The QKV projections ar` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
