# Official AutoAWQ Matched PPL Gate

Date: `2026-06-06T21:23:04+00:00`
Status: **PASS**

## Summary

- model: `Qwen/Qwen2.5-0.5B-Instruct`
- package: `autoawq 0.2.9`
- prompts: `8`
- tokens: `760`
- FP16 PPL: `24.675866135712827`
- AutoAWQ PPL: `31.350536434424747`
- PPL ratio AWQ/FP16: `1.2704938607626752`
- delta NLL AWQ-FP16: `0.23940569162368774`
- peak guard VRAM ratio: `0.6005`

## Failures

- none

## Claim Boundary

- Valid claim: a minimal matched FP16-vs-AutoAWQ PPL comparison completed under guard. Invalid claim: this is a complete official AWQ/GPTQ baseline, SOTA comparison, or broad task-retention result.
