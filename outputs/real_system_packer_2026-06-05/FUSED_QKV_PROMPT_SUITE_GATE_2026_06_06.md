# Fused QKV Prompt-Suite Gate

Status: **PASS**

## Summary

- model: `Qwen/Qwen3-0.6B`
- layers: `[1, 7]`
- prompts: 6
- exact matches: 6 / 6
- exact match rate: 1.0000
- mean / median edit similarity: 1.0000 / 1.0000
- mean common prefix ratio: 1.0000
- mean speed ratio fused/baseline: 0.8957x
- median TTFT ratio fused/baseline: 1.0933x
- compression vs FP32: 3.9082x
- replacement median CUDA ms: 0.141008
- wrapper/fused/cache-hit/cache-miss calls: 1152 / 384 / 768 / 384
- guard peak memory: 3553 / 8151 MiB (0.4359)

## Rule Score

- scored prompts: 6
- baseline passes: 5
- fused passes: 5
- fused pass rate: 0.8333
- regressions: 0
- improvements: 0
- rule count: 2

## Failures

- none

## Claim Boundary

- Valid claim: this candidate preserves the measured prompt-suite outputs under deterministic text and shallow rule checks.
- Invalid claim: this proves broad semantic quality, task accuracy, or SOTA quantization quality.
