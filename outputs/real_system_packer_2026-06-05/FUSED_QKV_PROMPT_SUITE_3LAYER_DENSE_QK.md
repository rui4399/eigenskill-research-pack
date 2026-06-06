# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T21:58:18Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[0, 1, 7]`
Dense roles: `['k_proj', 'q_proj']`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 0 / 6 |
| exact match rate | 0.0000 |
| mean char edit similarity | 0.5347 |
| median char edit similarity | 0.5127 |
| mean common prefix ratio | 0.3397 |
| mean baseline tokens/s | 21.7755 |
| mean fused tokens/s | 20.7822 |
| mean fused/baseline speed | 0.9544x |
| median baseline TTFT s | 0.060755 |
| median fused TTFT s | 0.208382 |

## Replacement Runtime

- Replacement compression vs FP32: `7.0778x`
- Dense role calls: `1152`
- Wrapper calls / fused compute calls: `576 / 576`
- Cache hits / misses: `0 / 576`
- Fused CUDA event sum: `1891.0566 ms`
- Peak CUDA memory: `1177.55 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | False | 0.3675 | 0.0904 | 21.2980 | 13.8008 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain why it's important to use mixed-precision in deep learning models, and give an exampl` |
| 1 | False | 0.7530 | 0.6981 | 19.4823 | 21.1224 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to implement a model quantization strategy that reduces the model's computational compl` |
| 2 | False | 0.6698 | 0.6176 | 24.8847 | 19.3985 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is packed in 4 bytes per row) Answer: An` |
| 3 | False | 0.5854 | 0.3607 | 21.8398 | 24.2933 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both types of data types and should be efficient. The functio` |
| 4 | False | 0.4400 | 0.2653 | 19.4101 | 23.2315 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main reason for the instability of quantization due to calibration` |
| 5 | False | 0.3926 | 0.0061 | 23.7379 | 22.8467 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` What is the role of QKV in the model? What is the role of the attention mechanism in the model? Wha` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
