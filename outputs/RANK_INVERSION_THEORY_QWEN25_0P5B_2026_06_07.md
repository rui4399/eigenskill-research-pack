# Rank-Inversion Theory Gate

Date: `2026-06-07T10:02:06+00:00`
Status: **PASS**

## Summary

- n range: `2 -> 8`
- curve points: `3`
- margin quantile: `0.75`
- mean empirical inversion rate: `0.2418 -> 0.1442`
- mean Chebyshev proxy bound: `0.8473 -> 0.6097`
- margin empirical inversion rate: `0.0969 -> 0.0427`
- margin Chebyshev proxy bound: `0.5974 -> 0.2713`
- mean empirical inversion decreasing: `True`
- mean Chebyshev proxy decreasing: `True`
- margin empirical inversion decreasing: `True`
- margin Chebyshev proxy decreasing: `True`

## Theory Note

For two unbiased sensitivity estimators with true gap Delta_ij, Chebyshev gives P[(hat{s}_i - hat{s}_j) changes sign] <= (Var[hat{s}_i] + Var[hat{s}_j]) / Delta_ij^2. This gate uses seed-level sample means and variances as a diagnostic plug-in estimator.

## Curve Points

| n | artifacts | modules | pairs | margin pairs | margin gap | mean inversion | mean bound | margin inversion | margin bound |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 6 | 169 | 14193 | 3549 | 1.575e-08 | 0.2418 | 0.8473 | 0.0969 | 0.5974 |
| 4 | 6 | 169 | 14168 | 3542 | 1.457e-08 | 0.2114 | 0.7825 | 0.0774 | 0.4701 |
| 8 | 6 | 169 | 14043 | 3511 | 1.317e-08 | 0.1442 | 0.6097 | 0.0427 | 0.2713 |

## Representative High-Risk Pairs

### n=2

| left | right | gap | variance sum | empirical inversion | bound |
|---|---|---:|---:|---:|---:|
| `model.layers.14.mlp.down_proj` | `model.layers.5.self_attn.k_proj` | 5.454e-09 | 2.251e-16 | 0.8333 | 1.0000 |
| `model.layers.5.self_attn.k_proj` | `model.layers.9.mlp.gate_proj` | 5.373e-09 | 2.249e-16 | 0.8333 | 1.0000 |
| `lm_head` | `model.layers.5.self_attn.k_proj` | 5.212e-09 | 2.249e-16 | 0.8333 | 1.0000 |
| `model.layers.20.mlp.up_proj` | `model.layers.5.self_attn.k_proj` | 5.185e-09 | 2.255e-16 | 0.8333 | 1.0000 |
| `model.layers.18.mlp.down_proj` | `model.layers.5.self_attn.k_proj` | 5.075e-09 | 2.251e-16 | 0.8333 | 1.0000 |

### n=4

| left | right | gap | variance sum | empirical inversion | bound |
|---|---|---:|---:|---:|---:|
| `model.layers.13.self_attn.v_proj` | `model.layers.5.mlp.up_proj` | 9.907e-09 | 6.506e-16 | 0.8333 | 1.0000 |
| `model.layers.13.self_attn.v_proj` | `model.layers.19.mlp.up_proj` | 9.704e-09 | 6.500e-16 | 0.8333 | 1.0000 |
| `model.layers.13.self_attn.v_proj` | `model.layers.17.mlp.down_proj` | 9.616e-09 | 6.500e-16 | 0.8333 | 1.0000 |
| `model.layers.13.self_attn.v_proj` | `model.layers.15.mlp.up_proj` | 9.565e-09 | 6.501e-16 | 0.8333 | 1.0000 |
| `model.layers.13.self_attn.v_proj` | `model.layers.20.mlp.up_proj` | 9.522e-09 | 6.502e-16 | 0.8333 | 1.0000 |

### n=8

| left | right | gap | variance sum | empirical inversion | bound |
|---|---|---:|---:|---:|---:|
| `model.layers.21.self_attn.q_proj` | `model.layers.9.self_attn.v_proj` | 1.831e-09 | 9.145e-17 | 0.8333 | 1.0000 |
| `model.layers.19.self_attn.o_proj` | `model.layers.9.self_attn.k_proj` | 7.163e-10 | 2.748e-17 | 0.8333 | 1.0000 |
| `model.layers.20.self_attn.q_proj` | `model.layers.9.self_attn.k_proj` | 6.648e-10 | 2.706e-17 | 0.8333 | 1.0000 |
| `model.layers.0.self_attn.o_proj` | `model.layers.9.self_attn.v_proj` | 4.151e-10 | 9.674e-17 | 0.8333 | 1.0000 |
| `model.layers.1.self_attn.v_proj` | `model.layers.11.mlp.down_proj` | 3.970e-10 | 4.540e-18 | 0.8333 | 1.0000 |

## Claim Boundary

Valid claim: a Chebyshev-style plug-in rank-inversion analysis over the committed Qwen2.5-0.5B prompt-seed sensitivity artifacts shows decreasing empirical inversion risk and decreasing variance/gap^2 upper-bound proxies as calibration size increases. Invalid claim: this proves a tight theoretical bound, downstream task retention, large-model universality, or production quantization quality.

## Failures

- none
