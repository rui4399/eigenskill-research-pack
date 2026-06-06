# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T22:17:33Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[0, 7]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 4 / 6 |
| exact match rate | 0.6667 |
| mean char edit similarity | 0.8469 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 0.7710 |
| mean baseline tokens/s | 26.8625 |
| mean fused tokens/s | 22.8398 |
| mean fused/baseline speed | 0.8502x |
| median baseline TTFT s | 0.037808 |
| median fused TTFT s | 0.074790 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1152 / 384`
- Cache hits / misses: `768 / 384`
- Fused CUDA event sum: `674.8617 ms`
- Peak CUDA memory: `1168.49 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 22.8888 | 18.6381 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` |
| 1 | True | 1.0000 | 1.0000 | 29.7429 | 24.7202 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | True | 1.0000 | 1.0000 | 24.2882 | 26.2712 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | False | 0.6667 | 0.3607 | 21.8795 | 24.2459 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both 4-byte and 8-byte integers. The function should be able ` |
| 4 | False | 0.4149 | 0.2653 | 31.2744 | 20.9786 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main reason for the instability of quantization when using calibra` |
| 5 | True | 1.0000 | 1.0000 | 31.1012 | 22.1847 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
