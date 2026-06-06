# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T23:17:27Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 2 / 6 |
| exact match rate | 0.3333 |
| mean char edit similarity | 0.7169 |
| median char edit similarity | 0.7827 |
| mean common prefix ratio | 0.5374 |
| mean baseline tokens/s | 23.2054 |
| mean fused tokens/s | 22.6264 |
| mean fused/baseline speed | 0.9750x |
| median baseline TTFT s | 0.038693 |
| median fused TTFT s | 0.065643 |

## Replacement Runtime

- Replacement compression vs FP32: `4.0526x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1728 / 576`
- Cache hits / misses: `1152 / 576`
- Fused CUDA event sum: `386.8608 ms`
- Peak CUDA memory: `1164.11 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | False | 0.3434 | 0.0904 | 20.1982 | 19.8814 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain why it's important to use mixed-precision in machine learning models, and give an exa` |
| 1 | False | 0.8113 | 0.7673 | 23.9465 | 26.9104 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | True | 1.0000 | 1.0000 | 24.4665 | 23.8069 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | False | 0.7541 | 0.3607 | 25.4744 | 23.5976 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both 4-byte and 8-byte integers, and should be able to handle` |
| 4 | True | 1.0000 | 1.0000 | 20.8221 | 22.1924 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` |
| 5 | False | 0.3926 | 0.0061 | 24.3250 | 19.3696 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` What is the role of QKV in the model? What is the role of the attention mechanism in the model? Wha` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
