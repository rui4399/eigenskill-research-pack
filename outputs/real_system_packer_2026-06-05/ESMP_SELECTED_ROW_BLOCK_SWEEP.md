# ESMP Selected-Row Block Sweep

Date: `2026-06-06`
Model: `Qwen/Qwen3-0.6B`
Modules: `3`
Batch shapes: `[1, 12]`
Selected rows: `[64, 256]`
Block configs: `['16x8x64', '16x16x64', '32x8x64', '32x16x64', '32x16x128', '64x16x128']`
Warmup/iters: `5/40`

## Summary By Block Config

| block | cases | median ms | p90 ms | median speedup vs dense full | median speedup vs dense selected | wins vs dense full | wins vs dense selected | best full speedup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 16x16x64 | 12 | 0.044271 | 0.152287 | 0.3744 | 0.3238 | 0 | 2 | 0.4247 |
| 16x8x64 | 12 | 0.043482 | 0.048491 | 0.3860 | 0.3388 | 0 | 3 | 0.4163 |
| 32x16x128 | 12 | 0.044102 | 0.057363 | 0.3738 | 0.3917 | 0 | 2 | 0.4418 |
| 32x16x64 | 12 | 0.044807 | 0.164309 | 0.3665 | 0.3384 | 0 | 2 | 0.4455 |
| 32x8x64 | 12 | 0.044401 | 0.146651 | 0.3669 | 0.3542 | 0 | 2 | 0.4505 |
| 64x16x128 | 12 | 0.043356 | 0.083537 | 0.3797 | 0.3958 | 0 | 2 | 0.4393 |

## Best Config Per Shape

| module | batch | selected rows | best block | latency ms | speedup vs dense full | speedup vs dense selected | rel-L2 |
|---|---:|---:|---|---:|---:|---:|---:|
| `model.layers.0.self_attn.k_proj` | 1 | 64 | 32x16x64 | 0.040194 | 0.4360 | 0.3182 | 0.190756 |
| `model.layers.0.self_attn.k_proj` | 1 | 256 | 32x8x64 | 0.038902 | 0.4505 | 0.3724 | 0.146067 |
| `model.layers.0.self_attn.k_proj` | 12 | 64 | 64x16x128 | 0.042393 | 0.3886 | 0.3429 | 0.170314 |
| `model.layers.0.self_attn.k_proj` | 12 | 256 | 32x8x64 | 0.045184 | 0.3646 | 0.9396 | 0.150917 |
| `model.layers.0.self_attn.q_proj` | 1 | 64 | 32x16x128 | 0.041103 | 0.4418 | 0.4512 | 0.182233 |
| `model.layers.0.self_attn.q_proj` | 1 | 256 | 32x8x64 | 0.041621 | 0.4363 | 0.3360 | 0.143236 |
| `model.layers.0.self_attn.q_proj` | 12 | 64 | 64x16x128 | 0.043273 | 0.3704 | 2.0041 | 0.171355 |
| `model.layers.0.self_attn.q_proj` | 12 | 256 | 16x16x64 | 0.042067 | 0.3810 | 0.8316 | 0.163548 |
| `model.layers.0.self_attn.v_proj` | 1 | 64 | 32x16x64 | 0.037114 | 0.4455 | 0.3446 | 0.008019 |
| `model.layers.0.self_attn.v_proj` | 1 | 256 | 16x8x64 | 0.040343 | 0.4099 | 0.3297 | 0.007496 |
| `model.layers.0.self_attn.v_proj` | 12 | 64 | 32x16x64 | 0.038313 | 0.4198 | 1.3101 | 0.008377 |
| `model.layers.0.self_attn.v_proj` | 12 | 256 | 16x8x64 | 0.041229 | 0.3901 | 1.5914 | 0.008401 |

## Interpretation Guardrails

- This sweep keeps the model loaded once and varies Triton block sizes only.
- A config with isolated wins but weak median performance indicates launch/fusion overhead, not a complete hardware win.
- Use this to choose the next kernel target; do not report it as end-to-end LLM acceleration.
