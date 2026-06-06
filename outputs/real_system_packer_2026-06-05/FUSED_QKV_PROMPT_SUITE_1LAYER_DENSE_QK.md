# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T21:57:22Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[0]`
Dense roles: `['k_proj', 'q_proj']`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 4 / 6 |
| exact match rate | 0.6667 |
| mean char edit similarity | 0.8642 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 0.7722 |
| mean baseline tokens/s | 25.7962 |
| mean fused tokens/s | 23.4610 |
| mean fused/baseline speed | 0.9095x |
| median baseline TTFT s | 0.037422 |
| median fused TTFT s | 0.046399 |

## Replacement Runtime

- Replacement compression vs FP32: `6.1682x`
- Dense role calls: `384`
- Wrapper calls / fused compute calls: `192 / 192`
- Cache hits / misses: `0 / 192`
- Fused CUDA event sum: `654.2361 ms`
- Peak CUDA memory: `1177.42 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 25.9991 | 15.9303 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` |
| 1 | True | 1.0000 | 1.0000 | 26.0102 | 22.5801 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | True | 1.0000 | 1.0000 | 26.4676 | 21.7291 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | True | 1.0000 | 1.0000 | 26.3669 | 27.5874 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` |
| 4 | False | 0.6512 | 0.3265 | 27.1350 | 24.5456 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main idea is to explain why calibration data can affect the quanti` |
| 5 | False | 0.5337 | 0.3067 | 22.7981 | 28.3938 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a key part of the transformer architecture, but it's not the only part of the model. What is` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
