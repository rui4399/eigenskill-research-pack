# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T22:49:57Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 3 / 6 |
| exact match rate | 0.5000 |
| mean char edit similarity | 0.6960 |
| median char edit similarity | 0.7809 |
| mean common prefix ratio | 0.6013 |
| mean baseline tokens/s | 20.2451 |
| mean fused tokens/s | 16.8235 |
| mean fused/baseline speed | 0.8310x |
| median baseline TTFT s | 0.044568 |
| median fused TTFT s | 0.352044 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9894x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1728 / 576`
- Cache hits / misses: `1152 / 576`
- Fused CUDA event sum: `2762.8518 ms`
- Peak CUDA memory: `1164.30 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | False | 0.5618 | 0.4458 | 17.1551 | 12.0301 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain the difference between mixed-precision and single-precision and double-precision in o` |
| 1 | False | 0.2893 | 0.1006 | 22.2130 | 18.8541 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to create a JSON object with the fields task, risk, and next_step for a model quantizat` |
| 2 | True | 1.0000 | 1.0000 | 17.4742 | 16.1609 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` |
| 3 | True | 1.0000 | 1.0000 | 22.5023 | 17.8819 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` |
| 4 | True | 1.0000 | 1.0000 | 23.2600 | 19.6210 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` |
| 5 | False | 0.3252 | 0.0613 | 18.8659 | 16.3927 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` QKV is a type of projection that is used in the training of language models. The QKV projections ar` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
