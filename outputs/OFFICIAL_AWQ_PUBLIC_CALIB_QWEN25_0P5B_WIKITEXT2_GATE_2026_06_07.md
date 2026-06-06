# Official AutoAWQ Matched PPL Gate

Date: `2026-06-06T21:46:24+00:00`
Status: **PASS**

## Summary

- model: `Qwen/Qwen2.5-0.5B-Instruct`
- package: `autoawq 0.2.9`
- prompts: `8`
- tokens: `760`
- FP16 PPL: `24.675866135712827`
- AutoAWQ PPL: `29.080631395938298`
- PPL ratio AWQ/FP16: `1.1785049909089331`
- delta NLL AWQ-FP16: `0.16424667835235596`
- peak guard VRAM ratio: `0.6116`

## Failures

- none

## Claim Boundary

- Valid claim: a minimal matched FP16-vs-AutoAWQ PPL comparison completed under guard. Invalid claim: this is a complete official AWQ/GPTQ baseline, SOTA comparison, or broad task-retention result.
