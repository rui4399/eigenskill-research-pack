# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-06T02:20:56Z`
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
| exact matches | 22 / 24 |
| exact match rate | 0.9167 |
| mean char edit similarity | 0.9890 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 0.9469 |
| mean baseline tokens/s | 24.9605 |
| mean fused tokens/s | 22.8044 |
| mean fused/baseline speed | 0.9136x |
| median baseline TTFT s | 0.083215 |
| median fused TTFT s | 0.118279 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9282x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `6912 / 2304`
- Cache hits / misses: `4608 / 2304`
- Fused CUDA event sum: `2291.9845 ms`
- Peak CUDA memory: `1165.69 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 23.4617 | 19.0768 | `<think> Okay, so the user is asking why calibration prompts might bias a mixed-precision row search.` | `<think> Okay, so the user is asking why calibration prompts might bias a mixed-precision row search.` |
| 1 | False | 0.9483 | 0.5776 | 25.6267 | 24.2484 | `<think> Okay, the user wants me to write a minified JSON with keys "hypothesis", "proxy", and "risk"` | `<think> Okay, the user wants me to write a minified JSON with keys 'hypothesis', 'proxy', and 'risk'` |
| 2 | True | 1.0000 | 1.0000 | 26.6829 | 18.9618 | `<think> Okay, so I need to figure out the packed byte count for 8192 signed 4-bit values. Hmm, let m` | `<think> Okay, so I need to figure out the packed byte count for 8192 signed 4-bit values. Hmm, let m` |
| 3 | True | 1.0000 | 1.0000 | 24.3510 | 19.2480 | `<think> Okay, I need to figure out how to create a C++ function signature for loading a row-wise mix` | `<think> Okay, I need to figure out how to create a C++ function signature for loading a row-wise mix` |
| 4 | True | 1.0000 | 1.0000 | 24.7215 | 20.4101 | `<think> Okay, so I need to figure out two reasons why a selected-row kernel might be fast in a micro` | `<think> Okay, so I need to figure out two reasons why a selected-row kernel might be fast in a micro` |
| 5 | True | 1.0000 | 1.0000 | 24.8025 | 24.1459 | `<think> Okay, so the user wants me to explain why KV-cache drift might reveal quantization damage be` | `<think> Okay, so the user wants me to explain why KV-cache drift might reveal quantization damage be` |
| 6 | True | 1.0000 | 1.0000 | 22.1239 | 19.6534 | `<think> Okay, the user is asking for three ablations needed before claiming a rowguard generalizes a` | `<think> Okay, the user is asking for three ablations needed before claiming a rowguard generalizes a` |
| 7 | True | 1.0000 | 1.0000 | 19.2208 | 27.8696 | `<think> Okay, the user wants me to compare exact match and logit relative L2 as evaluation signals i` | `<think> Okay, the user wants me to compare exact match and logit relative L2 as evaluation signals i` |
| 8 | True | 1.0000 | 1.0000 | 23.4485 | 16.6461 | `<think> Okay, the user is asking for two physical deployment metrics for an edge LLM besides tokens ` | `<think> Okay, the user is asking for two physical deployment metrics for an edge LLM besides tokens ` |
| 9 | True | 1.0000 | 1.0000 | 28.3166 | 24.3620 | `<think> Okay, the user wants a conservative paper title and subtitle for a study on calibration spli` | `<think> Okay, the user wants a conservative paper title and subtitle for a study on calibration spli` |
| 10 | True | 1.0000 | 1.0000 | 20.5508 | 25.7931 | `<think> Okay, so I need to figure out how a dense fallback for layer 0 in QKV replacement could impr` | `<think> Okay, so I need to figure out how a dense fallback for layer 0 in QKV replacement could impr` |
| 11 | True | 1.0000 | 1.0000 | 23.1487 | 23.9862 | `<think> Okay, so the user is asking for a failure case where increasing a row group from INT4 to INT` | `<think> Okay, so the user is asking for a failure case where increasing a row group from INT4 to INT` |
| 12 | True | 1.0000 | 1.0000 | 24.1772 | 20.1438 | `<think> Okay, the user wants a short README caveat that clarifies the difference between packed memo` | `<think> Okay, the user wants a short README caveat that clarifies the difference between packed memo` |
| 13 | False | 0.7886 | 0.1486 | 29.1607 | 20.6169 | `<think> Okay, so the user is asking why local reconstruction error might fail to rank attention rows` | `<think> Okay, so the user wants me to explain why local reconstruction error might fail to rank atte` |
| 14 | True | 1.0000 | 1.0000 | 29.6815 | 26.2449 | `<think> Okay, the user wants a YAML snippet with specific fields: model, policy, prompt_splits, and ` | `<think> Okay, the user wants a YAML snippet with specific fields: model, policy, prompt_splits, and ` |
| 15 | True | 1.0000 | 1.0000 | 25.6783 | 18.0890 | `<think> Okay, so I need to find the average bit width for a given set of row bit widths. The problem` | `<think> Okay, so I need to find the average bit width for a given set of row bit widths. The problem` |
| 16 | True | 1.0000 | 1.0000 | 30.5152 | 23.6708 | `<think> Okay, the user is asking for two task-style benchmarks that are stronger than perplexity for` | `<think> Okay, the user is asking for two task-style benchmarks that are stronger than perplexity for` |
| 17 | True | 1.0000 | 1.0000 | 28.4803 | 30.0688 | `<think> Okay, the user wants a one-line warning against tuning precision policies on test prompts. L` | `<think> Okay, the user wants a one-line warning against tuning precision policies on test prompts. L` |
| 18 | True | 1.0000 | 1.0000 | 21.5490 | 25.5079 | `<think> Okay, so I need to explain why a proxy selector should penalize large hidden-state drift eve` | `<think> Okay, so I need to explain why a proxy selector should penalize large hidden-state drift eve` |
| 19 | True | 1.0000 | 1.0000 | 24.2096 | 24.5203 | `<think> Okay, the user wants three bullet points for an experiment plan that separates speed evidenc` | `<think> Okay, the user wants three bullet points for an experiment plan that separates speed evidenc` |
| 20 | True | 1.0000 | 1.0000 | 21.7107 | 21.4086 | `<think> Okay, so I need to figure out why Triton kernels might lose to dense GEMM on tiny batch-one ` | `<think> Okay, so I need to figure out why Triton kernels might lose to dense GEMM on tiny batch-one ` |
| 21 | True | 1.0000 | 1.0000 | 21.8378 | 20.0938 | `<think> Okay, the user wants a compact JSON object describing a failed rowguard with keys 'symptom' ` | `<think> Okay, the user wants a compact JSON object describing a failed rowguard with keys 'symptom' ` |
| 22 | True | 1.0000 | 1.0000 | 28.3428 | 23.8864 | `<think> Okay, so I need to define prompt-split instability in the context of precision-policy search` | `<think> Okay, so I need to define prompt-split instability in the context of precision-policy search` |
| 23 | True | 1.0000 | 1.0000 | 27.2540 | 28.6532 | `<think> Okay, the user wants to choose between baseline, full-V8, and rowguard candidates. Let me st` | `<think> Okay, the user wants to choose between baseline, full-V8, and rowguard candidates. Let me st` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
