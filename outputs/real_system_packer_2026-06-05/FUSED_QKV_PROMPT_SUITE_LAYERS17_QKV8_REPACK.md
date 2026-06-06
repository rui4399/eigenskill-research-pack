# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T22:18:38Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 6 / 6 |
| exact match rate | 1.0000 |
| mean char edit similarity | 1.0000 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 1.0000 |
| mean baseline tokens/s | 27.1231 |
| mean fused tokens/s | 24.2953 |
| mean fused/baseline speed | 0.8957x |
| median baseline TTFT s | 0.034487 |
| median fused TTFT s | 0.037703 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1152 / 384`
- Cache hits / misses: `768 / 384`
- Fused CUDA event sum: `650.8291 ms`
- Peak CUDA memory: `1168.49 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 25.0208 | 18.3631 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` |
| 1 | True | 1.0000 | 1.0000 | 29.0371 | 29.6642 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | True | 1.0000 | 1.0000 | 30.2654 | 26.4286 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | True | 1.0000 | 1.0000 | 27.1629 | 22.8005 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` |
| 4 | True | 1.0000 | 1.0000 | 24.7379 | 23.1162 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` |
| 5 | True | 1.0000 | 1.0000 | 26.5145 | 25.3993 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
