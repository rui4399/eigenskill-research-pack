# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T23:19:15Z`
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
| mean char edit similarity | 0.5789 |
| median char edit similarity | 0.5434 |
| mean common prefix ratio | 0.3642 |
| mean baseline tokens/s | 24.3017 |
| mean fused tokens/s | 24.2167 |
| mean fused/baseline speed | 0.9965x |
| median baseline TTFT s | 0.036829 |
| median fused TTFT s | 0.044007 |

## Replacement Runtime

- Replacement compression vs FP32: `4.0526x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1728 / 576`
- Cache hits / misses: `1152 / 576`
- Fused CUDA event sum: `400.5160 ms`
- Peak CUDA memory: `1164.11 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | False | 0.3434 | 0.0904 | 25.8919 | 20.9866 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain why it's important to use mixed-precision in machine learning models, and give an exa` |
| 1 | False | 0.2893 | 0.1006 | 24.2373 | 22.6443 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to create a JSON object with the fields task, risk, and next_step for a model quantizat` |
| 2 | True | 1.0000 | 1.0000 | 25.4004 | 28.2579 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | False | 0.7541 | 0.3607 | 23.4588 | 28.1540 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both 4-byte and 8-byte integers, and should be able to handle` |
| 4 | False | 0.6512 | 0.3265 | 23.7470 | 24.7048 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main idea is to explain why calibration data can affect the quanti` |
| 5 | False | 0.4356 | 0.3067 | 23.0750 | 20.5527 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a key part of the transformer architecture, and it's used to do the following: a. __________` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
