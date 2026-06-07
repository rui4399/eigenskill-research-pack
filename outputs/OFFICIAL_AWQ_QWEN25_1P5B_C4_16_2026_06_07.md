# Official AutoAWQ Matched PPL Summary

Date: `2026-06-07T11:59:00+00:00`
Status: **PASS**
Model: `Qwen/Qwen2.5-1.5B-Instruct`
AWQ artifact: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Package: `autoawq 0.2.9`
Prompts: `16`
Tokens: `1444`
Elapsed seconds: `30.106`

## Metrics

| run | mean_nll | ppl |
|---|---:|---:|
| `fp16` | 3.063649 | 21.405532 |
| `autoawq_w4g128` | 3.143249 | 23.179046 |

## Comparison

- delta NLL AWQ-FP16: `0.079599`
- PPL ratio AWQ/FP16: `1.082853`

## Failures

- none

## Claim Boundary

- Valid claim: a minimal matched FP16-vs-AutoAWQ PPL comparison ran on the same prompt slice. Invalid claim: this is a competitive AWQ/GPTQ baseline, leaderboard result, or broad task-retention proof.
