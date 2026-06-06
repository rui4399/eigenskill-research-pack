# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T23:16:08Z`
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
| mean char edit similarity | 0.5498 |
| median char edit similarity | 0.5063 |
| mean common prefix ratio | 0.3569 |
| mean baseline tokens/s | 25.0950 |
| mean fused tokens/s | 21.7252 |
| mean fused/baseline speed | 0.8657x |
| median baseline TTFT s | 0.038704 |
| median fused TTFT s | 0.045537 |

## Replacement Runtime

- Replacement compression vs FP32: `4.0526x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `1728 / 576`
- Cache hits / misses: `1152 / 576`
- Fused CUDA event sum: `413.6699 ms`
- Peak CUDA memory: `1164.11 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | False | 0.3614 | 0.0904 | 25.0076 | 18.8249 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain why it's important to use mixed-precision in machine learning models, and give an exa` |
| 1 | False | 0.2893 | 0.1006 | 23.2686 | 23.8174 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to create a JSON object with the fields task, risk, and next_step for a model quantizat` |
| 2 | False | 0.6903 | 0.6176 | 26.7436 | 20.7792 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-bit wide row, and that the row is packed in 4 bytes per row) Answer: Th` |
| 3 | True | 1.0000 | 1.0000 | 24.2537 | 21.9812 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` |
| 4 | False | 0.6512 | 0.3265 | 25.5491 | 20.7931 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main idea is to explain why calibration data can affect the quanti` |
| 5 | False | 0.3067 | 0.0061 | 25.7474 | 24.1555 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` What is the role of QKV in the model? What is the role of the model in generating text? What is the` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
