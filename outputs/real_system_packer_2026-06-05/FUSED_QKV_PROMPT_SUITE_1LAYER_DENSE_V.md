# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T21:56:28Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[0]`
Dense roles: `['v_proj']`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 1 / 6 |
| exact match rate | 0.1667 |
| mean char edit similarity | 0.6051 |
| median char edit similarity | 0.5635 |
| mean common prefix ratio | 0.3470 |
| mean baseline tokens/s | 21.8351 |
| mean fused tokens/s | 21.9541 |
| mean fused/baseline speed | 1.0054x |
| median baseline TTFT s | 0.057506 |
| median fused TTFT s | 0.049431 |

## Replacement Runtime

- Replacement compression vs FP32: `6.1682x`
- Dense role calls: `192`
- Wrapper calls / fused compute calls: `384 / 192`
- Cache hits / misses: `192 / 192`
- Fused CUDA event sum: `640.9969 ms`
- Peak CUDA memory: `1173.43 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 24.3146 | 16.8602 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` |
| 1 | False | 0.4025 | 0.1006 | 20.0977 | 22.7009 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to quantize a model. The risk is the probability that the model is not quantized. The n` |
| 2 | False | 0.7455 | 0.2941 | 20.1841 | 24.6383 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-byte row, and that the row is packed in 16-bit chunks, and that the row` |
| 3 | False | 0.7121 | 0.3607 | 23.3738 | 20.3547 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both 4 and 8-bit integers, and the function should be able to` |
| 4 | False | 0.4149 | 0.2653 | 24.2594 | 24.5631 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main reason for the instability of quantization when using calibra` |
| 5 | False | 0.3558 | 0.0613 | 18.7811 | 22.6073 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a type of neural network architecture used in deep learning. The QKV projections are used to` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
