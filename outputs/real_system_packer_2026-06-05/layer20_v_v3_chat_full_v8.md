# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-06T02:19:38Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Dense roles: `[]`
Chat template: `True`
Max new tokens: `32`
Sync mode: `end`
Prompts: `24`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 23 / 24 |
| exact match rate | 0.9583 |
| mean char edit similarity | 0.9978 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 0.9824 |
| mean baseline tokens/s | 25.4481 |
| mean fused tokens/s | 26.2037 |
| mean fused/baseline speed | 1.0297x |
| median baseline TTFT s | 0.075710 |
| median fused TTFT s | 0.072025 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `6912 / 2304`
- Cache hits / misses: `4608 / 2304`
- Fused CUDA event sum: `777.0112 ms`
- Peak CUDA memory: `1165.75 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 21.1575 | 20.4333 | `<think> Okay, so the user is asking why calibration prompts might bias a mixed-precision row search.` | `<think> Okay, so the user is asking why calibration prompts might bias a mixed-precision row search.` |
| 1 | False | 0.9483 | 0.5776 | 24.7546 | 26.1170 | `<think> Okay, the user wants me to write a minified JSON with keys "hypothesis", "proxy", and "risk"` | `<think> Okay, the user wants me to write a minified JSON with keys 'hypothesis', 'proxy', and 'risk'` |
| 2 | True | 1.0000 | 1.0000 | 26.1143 | 26.6180 | `<think> Okay, so I need to figure out the packed byte count for 8192 signed 4-bit values. Hmm, let m` | `<think> Okay, so I need to figure out the packed byte count for 8192 signed 4-bit values. Hmm, let m` |
| 3 | True | 1.0000 | 1.0000 | 21.3355 | 28.6927 | `<think> Okay, I need to figure out how to create a C++ function signature for loading a row-wise mix` | `<think> Okay, I need to figure out how to create a C++ function signature for loading a row-wise mix` |
| 4 | True | 1.0000 | 1.0000 | 24.1492 | 25.0209 | `<think> Okay, so I need to figure out two reasons why a selected-row kernel might be fast in a micro` | `<think> Okay, so I need to figure out two reasons why a selected-row kernel might be fast in a micro` |
| 5 | True | 1.0000 | 1.0000 | 23.9765 | 21.1148 | `<think> Okay, so the user wants me to explain why KV-cache drift might reveal quantization damage be` | `<think> Okay, so the user wants me to explain why KV-cache drift might reveal quantization damage be` |
| 6 | True | 1.0000 | 1.0000 | 27.7185 | 26.7987 | `<think> Okay, the user is asking for three ablations needed before claiming a rowguard generalizes a` | `<think> Okay, the user is asking for three ablations needed before claiming a rowguard generalizes a` |
| 7 | True | 1.0000 | 1.0000 | 26.0228 | 22.6175 | `<think> Okay, the user wants me to compare exact match and logit relative L2 as evaluation signals i` | `<think> Okay, the user wants me to compare exact match and logit relative L2 as evaluation signals i` |
| 8 | True | 1.0000 | 1.0000 | 26.3741 | 24.6032 | `<think> Okay, the user is asking for two physical deployment metrics for an edge LLM besides tokens ` | `<think> Okay, the user is asking for two physical deployment metrics for an edge LLM besides tokens ` |
| 9 | True | 1.0000 | 1.0000 | 24.6437 | 27.9835 | `<think> Okay, the user wants a conservative paper title and subtitle for a study on calibration spli` | `<think> Okay, the user wants a conservative paper title and subtitle for a study on calibration spli` |
| 10 | True | 1.0000 | 1.0000 | 30.0083 | 28.1555 | `<think> Okay, so I need to figure out how a dense fallback for layer 0 in QKV replacement could impr` | `<think> Okay, so I need to figure out how a dense fallback for layer 0 in QKV replacement could impr` |
| 11 | True | 1.0000 | 1.0000 | 21.3448 | 27.6754 | `<think> Okay, so the user is asking for a failure case where increasing a row group from INT4 to INT` | `<think> Okay, so the user is asking for a failure case where increasing a row group from INT4 to INT` |
| 12 | True | 1.0000 | 1.0000 | 23.1632 | 26.4604 | `<think> Okay, the user wants a short README caveat that clarifies the difference between packed memo` | `<think> Okay, the user wants a short README caveat that clarifies the difference between packed memo` |
| 13 | True | 1.0000 | 1.0000 | 28.1174 | 29.7354 | `<think> Okay, so the user is asking why local reconstruction error might fail to rank attention rows` | `<think> Okay, so the user is asking why local reconstruction error might fail to rank attention rows` |
| 14 | True | 1.0000 | 1.0000 | 23.8548 | 28.6829 | `<think> Okay, the user wants a YAML snippet with specific fields: model, policy, prompt_splits, and ` | `<think> Okay, the user wants a YAML snippet with specific fields: model, policy, prompt_splits, and ` |
| 15 | True | 1.0000 | 1.0000 | 23.3602 | 29.1163 | `<think> Okay, so I need to find the average bit width for a given set of row bit widths. The problem` | `<think> Okay, so I need to find the average bit width for a given set of row bit widths. The problem` |
| 16 | True | 1.0000 | 1.0000 | 27.6803 | 29.4835 | `<think> Okay, the user is asking for two task-style benchmarks that are stronger than perplexity for` | `<think> Okay, the user is asking for two task-style benchmarks that are stronger than perplexity for` |
| 17 | True | 1.0000 | 1.0000 | 28.7937 | 29.9074 | `<think> Okay, the user wants a one-line warning against tuning precision policies on test prompts. L` | `<think> Okay, the user wants a one-line warning against tuning precision policies on test prompts. L` |
| 18 | True | 1.0000 | 1.0000 | 25.2267 | 18.8115 | `<think> Okay, so I need to explain why a proxy selector should penalize large hidden-state drift eve` | `<think> Okay, so I need to explain why a proxy selector should penalize large hidden-state drift eve` |
| 19 | True | 1.0000 | 1.0000 | 28.3944 | 24.2756 | `<think> Okay, the user wants three bullet points for an experiment plan that separates speed evidenc` | `<think> Okay, the user wants three bullet points for an experiment plan that separates speed evidenc` |
| 20 | True | 1.0000 | 1.0000 | 26.1329 | 27.1083 | `<think> Okay, so I need to figure out why Triton kernels might lose to dense GEMM on tiny batch-one ` | `<think> Okay, so I need to figure out why Triton kernels might lose to dense GEMM on tiny batch-one ` |
| 21 | True | 1.0000 | 1.0000 | 29.6337 | 25.4022 | `<think> Okay, the user wants a compact JSON object describing a failed rowguard with keys 'symptom' ` | `<think> Okay, the user wants a compact JSON object describing a failed rowguard with keys 'symptom' ` |
| 22 | True | 1.0000 | 1.0000 | 19.5222 | 27.8294 | `<think> Okay, so I need to define prompt-split instability in the context of precision-policy search` | `<think> Okay, so I need to define prompt-split instability in the context of precision-policy search` |
| 23 | True | 1.0000 | 1.0000 | 29.2746 | 26.2443 | `<think> Okay, the user wants to choose between baseline, full-V8, and rowguard candidates. Let me st` | `<think> Okay, the user wants to choose between baseline, full-V8, and rowguard candidates. Let me st` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
