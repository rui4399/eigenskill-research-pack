# Fused QKV Replacement Generation Gate

Status: **PASS**

## Summary

- model: `Qwen/Qwen3-0.6B`
- layers: `[0]`
- replacements: 1
- generated tokens: 64
- TTFT: 0.032971 s
- baseline TTFT: 0.048212 s
- TTFT ratio vs baseline: 0.6839
- tokens/s: 30.2441
- baseline tokens/s: 26.7642
- tokens/s ratio vs baseline: 1.1300
- exact text match: False
- common prefix chars: 210
- compression vs FP32: 6.1682x
- wrapper/fused/cache-hit/cache-miss calls: 192 / 64 / 128 / 64
- replacement CUDA median/max ms: 0.192896 / 0.508544
- guard peak memory: 3587 / 8151 MiB (0.4401)

## Replacements

| index | modules | wrapper | fused | hits | misses | compression | median ms | max ms | shapes |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 0 | `q_proj, k_proj, v_proj` | 192 | 64 | 128 | 64 | 6.1682x | 0.192896 | 0.508544 | `['1x12x1024', '1x1x1024']` |

## Failures

- none

## Claim Boundary

- Valid claim: selected QKV projections can be replaced by the fused ESMP runtime in a guarded HF generation smoke, with measured compression, QKV cache reuse, TTFT, and throughput.
- Invalid claim: this is a quality-preserving full-model quantizer or a production Tensor Core runtime.
