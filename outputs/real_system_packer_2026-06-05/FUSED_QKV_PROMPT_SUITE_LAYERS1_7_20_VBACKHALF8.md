# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T22:51:17Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 1 / 6 |
| exact match rate | 0.1667 |
| mean char edit similarity | 0.6741 |
| median char edit similarity | 0.7026 |
| mean common prefix ratio | 0.4753 |
| mean baseline tokens/s | 23.0612 |
| mean fused tokens/s | 21.4421 |
| mean fused/baseline speed | 0.9298x |
| median baseline TTFT s | 0.044759 |
| median fused TTFT s | 0.063073 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9894x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1728 / 576`
- Cache hits / misses: `1152 / 576`
- Fused CUDA event sum: `782.8300 ms`
- Peak CUDA memory: `1164.30 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | False | 0.3434 | 0.0904 | 25.3411 | 15.6550 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain why it's important to use mixed-precision in machine learning models, and give an exa` |
| 1 | False | 0.8113 | 0.7673 | 19.3570 | 22.3345 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | True | 1.0000 | 1.0000 | 23.2251 | 22.1314 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | False | 0.7541 | 0.3607 | 21.2936 | 24.5878 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both 4-byte and 8-byte integers, and should be able to handle` |
| 4 | False | 0.6512 | 0.3265 | 22.4645 | 20.4650 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main idea is to explain why calibration data can affect the quanti` |
| 5 | False | 0.4847 | 0.3067 | 26.6858 | 23.4788 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a key part of the transformer architecture, but it's not used in the standard transformer. S` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
