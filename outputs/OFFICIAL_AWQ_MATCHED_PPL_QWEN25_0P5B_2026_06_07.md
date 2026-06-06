# Official AutoAWQ Matched PPL Summary

Date: `2026-06-06T21:06:31+00:00`
Status: **PASS**
Model: `Qwen/Qwen2.5-0.5B-Instruct`
AWQ artifact: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_awq_model`
Package: `autoawq 0.2.9`
Prompts: `4`
Tokens: `73`
Elapsed seconds: `22.504`

## Metrics

| run | mean_nll | ppl |
|---|---:|---:|
| `fp16` | 5.285900 | 197.531963 |
| `autoawq_w4g128` | 5.450449 | 232.862636 |

## Comparison

- delta NLL AWQ-FP16: `0.164548`
- PPL ratio AWQ/FP16: `1.178861`

## Failures

- none

## Claim Boundary

- Valid claim: a minimal matched FP16-vs-AutoAWQ PPL comparison ran on the same prompt slice. Invalid claim: this is a competitive AWQ/GPTQ baseline, leaderboard result, or broad task-retention proof.
