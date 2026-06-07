# Official AutoAWQ Matched PPL Summary

Date: `2026-06-07T04:30:21+00:00`
Status: **PASS**
Model: `Qwen/Qwen2.5-0.5B-Instruct`
AWQ artifact: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model`
Package: `autoawq 0.2.9`
Prompts: `16`
Tokens: `1444`
Elapsed seconds: `23.253`

## Metrics

| run | mean_nll | ppl |
|---|---:|---:|
| `fp16` | 3.398447 | 29.917597 |
| `autoawq_w4g128` | 3.565995 | 35.374649 |

## Comparison

- delta NLL AWQ-FP16: `0.167549`
- PPL ratio AWQ/FP16: `1.182403`

## Failures

- none

## Claim Boundary

- Valid claim: a minimal matched FP16-vs-AutoAWQ PPL comparison ran on the same prompt slice. Invalid claim: this is a competitive AWQ/GPTQ baseline, leaderboard result, or broad task-retention proof.
