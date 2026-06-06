# Official AutoAWQ Matched PPL Summary

Date: `2026-06-06T21:45:42+00:00`
Status: **PASS**
Model: `Qwen/Qwen2.5-0.5B-Instruct`
AWQ artifact: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model`
Package: `autoawq 0.2.9`
Prompts: `8`
Tokens: `727`
Elapsed seconds: `23.030`

## Metrics

| run | mean_nll | ppl |
|---|---:|---:|
| `fp16` | 3.495042 | 32.951664 |
| `autoawq_w4g128` | 3.642121 | 38.172702 |

## Comparison

- delta NLL AWQ-FP16: `0.147079`
- PPL ratio AWQ/FP16: `1.158445`

## Failures

- none

## Claim Boundary

- Valid claim: a minimal matched FP16-vs-AutoAWQ PPL comparison ran on the same prompt slice. Invalid claim: this is a competitive AWQ/GPTQ baseline, leaderboard result, or broad task-retention proof.
