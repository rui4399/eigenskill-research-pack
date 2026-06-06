# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-06T02:18:26Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7]`
Dense roles: `[]`
Chat template: `True`
Max new tokens: `32`
Sync mode: `end`
Prompts: `24`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 24 / 24 |
| exact match rate | 1.0000 |
| mean char edit similarity | 1.0000 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 1.0000 |
| mean baseline tokens/s | 26.0407 |
| mean fused tokens/s | 23.4792 |
| mean fused/baseline speed | 0.9016x |
| median baseline TTFT s | 0.077250 |
| median fused TTFT s | 0.089299 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `4608 / 1536`
- Cache hits / misses: `3072 / 1536`
- Fused CUDA event sum: `1505.3792 ms`
- Peak CUDA memory: `1169.69 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 23.6042 | 16.6275 | `<think> Okay, so the user is asking why calibration prompts might bias a mixed-precision row search.` | `<think> Okay, so the user is asking why calibration prompts might bias a mixed-precision row search.` |
| 1 | True | 1.0000 | 1.0000 | 25.0632 | 25.9415 | `<think> Okay, the user wants me to write a minified JSON with keys "hypothesis", "proxy", and "risk"` | `<think> Okay, the user wants me to write a minified JSON with keys "hypothesis", "proxy", and "risk"` |
| 2 | True | 1.0000 | 1.0000 | 28.0407 | 17.1476 | `<think> Okay, so I need to figure out the packed byte count for 8192 signed 4-bit values. Hmm, let m` | `<think> Okay, so I need to figure out the packed byte count for 8192 signed 4-bit values. Hmm, let m` |
| 3 | True | 1.0000 | 1.0000 | 25.3184 | 19.5195 | `<think> Okay, I need to figure out how to create a C++ function signature for loading a row-wise mix` | `<think> Okay, I need to figure out how to create a C++ function signature for loading a row-wise mix` |
| 4 | True | 1.0000 | 1.0000 | 29.9228 | 18.1912 | `<think> Okay, so I need to figure out two reasons why a selected-row kernel might be fast in a micro` | `<think> Okay, so I need to figure out two reasons why a selected-row kernel might be fast in a micro` |
| 5 | True | 1.0000 | 1.0000 | 21.0668 | 25.2509 | `<think> Okay, so the user wants me to explain why KV-cache drift might reveal quantization damage be` | `<think> Okay, so the user wants me to explain why KV-cache drift might reveal quantization damage be` |
| 6 | True | 1.0000 | 1.0000 | 24.7211 | 26.1477 | `<think> Okay, the user is asking for three ablations needed before claiming a rowguard generalizes a` | `<think> Okay, the user is asking for three ablations needed before claiming a rowguard generalizes a` |
| 7 | True | 1.0000 | 1.0000 | 26.4914 | 22.9668 | `<think> Okay, the user wants me to compare exact match and logit relative L2 as evaluation signals i` | `<think> Okay, the user wants me to compare exact match and logit relative L2 as evaluation signals i` |
| 8 | True | 1.0000 | 1.0000 | 26.3796 | 22.2114 | `<think> Okay, the user is asking for two physical deployment metrics for an edge LLM besides tokens ` | `<think> Okay, the user is asking for two physical deployment metrics for an edge LLM besides tokens ` |
| 9 | True | 1.0000 | 1.0000 | 24.5155 | 24.8386 | `<think> Okay, the user wants a conservative paper title and subtitle for a study on calibration spli` | `<think> Okay, the user wants a conservative paper title and subtitle for a study on calibration spli` |
| 10 | True | 1.0000 | 1.0000 | 23.0193 | 27.2402 | `<think> Okay, so I need to figure out how a dense fallback for layer 0 in QKV replacement could impr` | `<think> Okay, so I need to figure out how a dense fallback for layer 0 in QKV replacement could impr` |
| 11 | True | 1.0000 | 1.0000 | 24.7760 | 24.2375 | `<think> Okay, so the user is asking for a failure case where increasing a row group from INT4 to INT` | `<think> Okay, so the user is asking for a failure case where increasing a row group from INT4 to INT` |
| 12 | True | 1.0000 | 1.0000 | 25.2590 | 27.9621 | `<think> Okay, the user wants a short README caveat that clarifies the difference between packed memo` | `<think> Okay, the user wants a short README caveat that clarifies the difference between packed memo` |
| 13 | True | 1.0000 | 1.0000 | 27.0987 | 23.0363 | `<think> Okay, so the user is asking why local reconstruction error might fail to rank attention rows` | `<think> Okay, so the user is asking why local reconstruction error might fail to rank attention rows` |
| 14 | True | 1.0000 | 1.0000 | 24.7485 | 23.9331 | `<think> Okay, the user wants a YAML snippet with specific fields: model, policy, prompt_splits, and ` | `<think> Okay, the user wants a YAML snippet with specific fields: model, policy, prompt_splits, and ` |
| 15 | True | 1.0000 | 1.0000 | 25.1786 | 20.6227 | `<think> Okay, so I need to find the average bit width for a given set of row bit widths. The problem` | `<think> Okay, so I need to find the average bit width for a given set of row bit widths. The problem` |
| 16 | True | 1.0000 | 1.0000 | 28.1372 | 26.7691 | `<think> Okay, the user is asking for two task-style benchmarks that are stronger than perplexity for` | `<think> Okay, the user is asking for two task-style benchmarks that are stronger than perplexity for` |
| 17 | True | 1.0000 | 1.0000 | 23.3866 | 22.1714 | `<think> Okay, the user wants a one-line warning against tuning precision policies on test prompts. L` | `<think> Okay, the user wants a one-line warning against tuning precision policies on test prompts. L` |
| 18 | True | 1.0000 | 1.0000 | 31.1894 | 22.1420 | `<think> Okay, so I need to explain why a proxy selector should penalize large hidden-state drift eve` | `<think> Okay, so I need to explain why a proxy selector should penalize large hidden-state drift eve` |
| 19 | True | 1.0000 | 1.0000 | 26.3042 | 27.7472 | `<think> Okay, the user wants three bullet points for an experiment plan that separates speed evidenc` | `<think> Okay, the user wants three bullet points for an experiment plan that separates speed evidenc` |
| 20 | True | 1.0000 | 1.0000 | 31.1194 | 21.0274 | `<think> Okay, so I need to figure out why Triton kernels might lose to dense GEMM on tiny batch-one ` | `<think> Okay, so I need to figure out why Triton kernels might lose to dense GEMM on tiny batch-one ` |
| 21 | True | 1.0000 | 1.0000 | 26.6587 | 25.9908 | `<think> Okay, the user wants a compact JSON object describing a failed rowguard with keys 'symptom' ` | `<think> Okay, the user wants a compact JSON object describing a failed rowguard with keys 'symptom' ` |
| 22 | True | 1.0000 | 1.0000 | 27.3076 | 25.6140 | `<think> Okay, so I need to define prompt-split instability in the context of precision-policy search` | `<think> Okay, so I need to define prompt-split instability in the context of precision-policy search` |
| 23 | True | 1.0000 | 1.0000 | 25.6698 | 26.1639 | `<think> Okay, the user wants to choose between baseline, full-V8, and rowguard candidates. Let me st` | `<think> Okay, the user wants to choose between baseline, full-V8, and rowguard candidates. Let me st` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
