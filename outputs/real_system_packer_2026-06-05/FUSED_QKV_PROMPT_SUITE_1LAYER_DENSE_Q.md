# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T21:54:47Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[0]`
Dense roles: `['q_proj']`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 3 / 6 |
| exact match rate | 0.5000 |
| mean char edit similarity | 0.7448 |
| median char edit similarity | 0.8765 |
| mean common prefix ratio | 0.6708 |
| mean baseline tokens/s | 25.7508 |
| mean fused tokens/s | 19.1192 |
| mean fused/baseline speed | 0.7425x |
| median baseline TTFT s | 0.042533 |
| median fused TTFT s | 0.310986 |

## Replacement Runtime

- Replacement compression vs FP32: `6.1682x`
- Dense role calls: `192`
- Wrapper calls / fused compute calls: `384 / 192`
- Cache hits / misses: `192 / 192`
- Fused CUDA event sum: `3449.1703 ms`
- Peak CUDA memory: `1175.42 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 27.9862 | 9.1438 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` |
| 1 | False | 0.7530 | 0.6981 | 28.7270 | 20.3217 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | True | 1.0000 | 1.0000 | 22.8197 | 20.6072 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | True | 1.0000 | 1.0000 | 21.9685 | 23.1028 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` |
| 4 | False | 0.4149 | 0.2653 | 30.1725 | 20.4125 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main reason for the instability of quantization when using calibra` |
| 5 | False | 0.3006 | 0.0613 | 22.8306 | 21.1270 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a type of projection that is used in the training of neural networks. The QKV projections ar` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
