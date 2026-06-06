# Triton Kernel Config Selector

Status: **PASS**

This selector chooses one grouped packed INT4/INT8 Triton block config per measured shape/batch/high_every group.
It is a deployment-planning artifact for the prototype kernel, not an end-to-end runtime claim.

## Summary

- total groups: 8
- valid groups: 8
- FP16-winning groups: 6
- row-wise-winning groups: 7
- selected grouped/FP16 speedup median: 1.8305
- selected grouped/FP16 speedup max: 2.7647
- selected grouped/row-wise speedup median: 2.2330
- selected grouped/row-wise speedup max: 5.1794

## Selected Configs

| shape | batch | high_every | status | BM | BN | BK | grouped/FP16 | grouped/row-wise | rel-L2 | VRAM ratio |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1024x1024 | 8 | 16 | fp16_win | 32 | 32 | 64 | 2.3350 | 0.9238 | 0.1372 | 0.4314 |
| 1024x1024 | 16 | 16 | fallback_best_available | 32 | 32 | 128 | 0.5394 | 1.7205 | 0.1389 | 0.4318 |
| 1024x3072 | 8 | 16 | fp16_win | 16 | 16 | 128 | 2.0627 | 2.1480 | 0.1491 | 0.4369 |
| 1024x3072 | 16 | 16 | fallback_best_available | 32 | 32 | 128 | 0.5302 | 2.3180 | 0.1492 | 0.4361 |
| 2048x1024 | 8 | 16 | fp16_win | 32 | 8 | 128 | 1.3194 | 1.6097 | 0.1382 | 0.4336 |
| 2048x1024 | 16 | 16 | fp16_win | 16 | 8 | 128 | 1.6543 | 3.1602 | 0.1373 | 0.4430 |
| 3072x1024 | 8 | 16 | fp16_win | 32 | 32 | 64 | 2.7647 | 2.6601 | 0.1376 | 0.4366 |
| 3072x1024 | 16 | 16 | fp16_win | 16 | 16 | 128 | 2.0067 | 5.1794 | 0.1379 | 0.4366 |

## Failures

- none

## Claim Boundary

- Valid claim: the measured tuning sweep can be converted into a deterministic per-shape kernel config policy.
- Invalid claim: unmeasured shapes, mobile kernels, or end-to-end LLM acceleration are covered by this selector.
