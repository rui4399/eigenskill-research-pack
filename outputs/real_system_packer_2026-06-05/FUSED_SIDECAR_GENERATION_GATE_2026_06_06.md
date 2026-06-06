# Fused Sidecar Generation Gate

Status: **PASS**

## Summary

- model: `Qwen/Qwen3-0.6B`
- layers: `[0, 1, 7]`
- sidecars: 3
- sidecar calls: 48
- sync mode: `end`
- generated tokens: 16
- TTFT: 0.043812 s
- tokens/s: 23.8078
- baseline tokens/s: 29.4639
- tokens/s ratio vs baseline: 0.8080
- generated text matches baseline: True
- sidecar CUDA sum/median/max ms: 10.218592 / 0.206160 / 0.440736
- observed input shapes: `['1x12x1024', '1x1x1024']`
- guard peak memory: 3583 / 8151 MiB (0.4396)

## Sidecars

| layer | calls | selected rows | low rows | high rows | median ms | max ms | shapes | errors |
|---:|---:|---:|---:|---:|---:|---:|---|---|
| 0 | 16 | 192 | 128 | 64 | 0.268032 | 0.440736 | `['1x12x1024', '1x1x1024']` | 0 |
| 1 | 16 | 192 | 192 | 0 | 0.157360 | 0.289728 | `['1x12x1024', '1x1x1024']` | 0 |
| 7 | 16 | 192 | 192 | 0 | 0.174736 | 0.313056 | `['1x12x1024', '1x1x1024']` | 0 |

## Failures

- none

## Claim Boundary

- Valid claim: fused selected-row ESMP kernels execute inside real HF generation hooks with bounded measured overhead and guard-limited VRAM.
- Invalid claim: this sidecar run proves end-to-end LLM acceleration, because dense QKV is still executed.
