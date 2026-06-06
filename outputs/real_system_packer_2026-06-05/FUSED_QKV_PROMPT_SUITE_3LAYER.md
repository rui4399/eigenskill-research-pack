# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-05T21:38:41Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[0, 1, 7]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `6`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 0 / 6 |
| exact match rate | 0.0000 |
| mean char edit similarity | 0.5221 |
| median char edit similarity | 0.4191 |
| mean common prefix ratio | 0.1862 |
| mean baseline tokens/s | 25.7576 |
| mean fused tokens/s | 21.8530 |
| mean fused/baseline speed | 0.8484x |
| median baseline TTFT s | 0.064350 |
| median fused TTFT s | 0.201079 |

## Replacement Runtime

- Replacement compression vs FP32: `7.0778x`
- Wrapper calls / fused compute calls: `1728 / 576`
- Cache hits / misses: `1152 / 576`
- Fused CUDA event sum: `1515.4567 ms`
- Peak CUDA memory: `1159.55 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | False | 0.4277 | 0.0904 | 29.1876 | 18.0572 | ` Also, explain the difference between mixed-precision and single-precision. \| Also, explain the dif` | ` Also, explain why it's important to use mixed-precision in neural networks, and what are the benefi` |
| 1 | False | 0.4025 | 0.1006 | 22.0770 | 24.6974 | ` The task is to implement a model quantization strategy that reduces the model's computational compl` | ` The task is to quantize a model. The risk is that the model may not be able to run on a GPU. The ne` |
| 2 | False | 0.7455 | 0.2941 | 25.2854 | 25.7169 | ` (Assume that the row is a 4-bit wide row, and that the row is a 4-bit wide row, and that the row is` | ` (Assume that the row is a 4-byte row, and that the row is packed in 16-bit chunks, and that the row` |
| 3 | False | 0.7541 | 0.3607 | 24.6253 | 20.1031 | ` The function should be able to handle both INT4 and INT8 data types, and should be able to handle b` | ` The function should be able to handle both 4-byte and 8-byte integers, and should be able to handle` |
| 4 | False | 0.4104 | 0.2653 | 22.3898 | 23.4774 | ` Explain each reason. Answer: The main idea is that **calibration data** can affect the **quantizati` | ` Explain each reason. Answer: The main reason for the instability of quantization when using calibra` |
| 5 | False | 0.3926 | 0.0061 | 30.9806 | 19.0659 | ` QKV is a key part of the transformer architecture. The key part is the attention mechanism. The att` | ` What is the role of QKV in the model? What is the role of the attention mechanism in the model? Wha` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
