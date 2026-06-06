# Selector Runtime Smoke Gate

Status: **PASS**

## Summary

- mode: `triton_grouped`
- kernel configs loaded: 8
- replaced modules: 1
- selector events: 2
- selector calls: 4
- selected compression vs FP32: 7.6413x
- TTFT: 2.4270 s
- tokens/s: 1.4233
- generated tokens: 4
- guard peak memory: 4663 / 8151 MiB (0.5721)

## Selector Events

| module | requested batch | selected batch | shape | BM | BN | BK | status | count |
|---|---:|---:|---|---:|---:|---:|---|---:|
| `model.layers.0.self_attn.q_proj` | 12 | 16 | `2048x1024` | 16 | 8 | 128 | `fp16_win` | 1 |
| `model.layers.0.self_attn.q_proj` | 1 | 8 | `2048x1024` | 32 | 8 | 128 | `fp16_win` | 3 |

## Failures

- none
