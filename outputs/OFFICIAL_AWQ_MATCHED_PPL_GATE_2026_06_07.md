# Official AutoAWQ Matched PPL Gate

Date: `2026-06-06T21:06:48+00:00`
Status: **PASS**

## Summary

- model: `Qwen/Qwen2.5-0.5B-Instruct`
- package: `autoawq 0.2.9`
- prompts: `4`
- tokens: `73`
- FP16 PPL: `197.53196313550743`
- AutoAWQ PPL: `232.8626361090369`
- PPL ratio AWQ/FP16: `1.178860536860521`
- delta NLL AWQ-FP16: `0.164548325212035`
- peak guard VRAM ratio: `0.6057`

## Failures

- none

## Claim Boundary

- Valid claim: a minimal matched FP16-vs-AutoAWQ PPL comparison completed under guard. Invalid claim: this is a complete official AWQ/GPTQ baseline, SOTA comparison, or broad task-retention result.
