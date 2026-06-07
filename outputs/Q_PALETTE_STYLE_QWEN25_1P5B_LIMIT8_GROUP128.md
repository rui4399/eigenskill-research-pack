# Lagrangian Loss-Sensitivity Allocation

Formula: `b_i = 0.5 * log2((S_i * sigma_i^2 * ln2) / (lambda * c_i))`
Target average bits: `4.5`
Solved lambda: `1.1803986628379084e-13`
Actual average bits: `4.499854`
Budget satisfied: `True`
Bit histogram: `{'2': 58, '3': 3, '4': 51, '8': 85}`

## Top Protected Records

| rank | name | bits | continuous_bits | sensitivity | variance | cost |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `model.layers.0.self_attn.v_proj` | 8 | 8.000 | 0.0199938 | 1 | 393472 |
| 2 | `model.layers.2.self_attn.v_proj` | 8 | 8.000 | 0.007072 | 1 | 393472 |
| 3 | `model.layers.17.self_attn.v_proj` | 8 | 8.000 | 0.00576969 | 1 | 393472 |
| 4 | `model.layers.1.self_attn.v_proj` | 8 | 8.000 | 0.00475977 | 1 | 393472 |
| 5 | `model.layers.3.self_attn.v_proj` | 8 | 7.905 | 0.00384783 | 1 | 393472 |
| 6 | `model.layers.4.self_attn.k_proj` | 8 | 7.888 | 0.00376099 | 1 | 393472 |
| 7 | `model.layers.4.self_attn.v_proj` | 8 | 7.846 | 0.0035471 | 1 | 393472 |
| 8 | `model.layers.22.self_attn.v_proj` | 8 | 7.758 | 0.00313879 | 1 | 393472 |
| 9 | `model.layers.15.self_attn.v_proj` | 8 | 7.644 | 0.0026796 | 1 | 393472 |
| 10 | `model.layers.13.self_attn.k_proj` | 8 | 7.607 | 0.00254678 | 1 | 393472 |
| 11 | `model.layers.8.self_attn.v_proj` | 8 | 7.547 | 0.0023443 | 1 | 393472 |
| 12 | `model.layers.11.self_attn.v_proj` | 8 | 7.372 | 0.00183909 | 1 | 393472 |
| 13 | `model.layers.10.self_attn.v_proj` | 8 | 7.285 | 0.00162949 | 1 | 393472 |
| 14 | `model.layers.15.self_attn.k_proj` | 8 | 7.257 | 0.00156766 | 1 | 393472 |
| 15 | `model.layers.19.self_attn.k_proj` | 8 | 7.255 | 0.00156382 | 1 | 393472 |
| 16 | `model.layers.13.self_attn.v_proj` | 8 | 7.198 | 0.00144394 | 1 | 393472 |
| 17 | `model.layers.23.self_attn.k_proj` | 8 | 7.170 | 0.00138906 | 1 | 393472 |
| 18 | `model.layers.14.self_attn.k_proj` | 8 | 7.130 | 0.00131491 | 1 | 393472 |
| 19 | `model.layers.0.self_attn.o_proj` | 8 | 7.130 | 0.00788315 | 1 | 2359296 |
| 20 | `model.layers.24.self_attn.v_proj` | 8 | 7.019 | 0.0011279 | 1 | 393472 |
| 21 | `model.layers.18.self_attn.k_proj` | 8 | 6.978 | 0.00106533 | 1 | 393472 |
| 22 | `model.layers.17.self_attn.k_proj` | 8 | 6.960 | 0.00103873 | 1 | 393472 |
| 23 | `model.layers.24.self_attn.k_proj` | 8 | 6.875 | 0.00092379 | 1 | 393472 |
| 24 | `model.layers.6.self_attn.k_proj` | 8 | 6.837 | 0.000875222 | 1 | 393472 |
| 25 | `model.layers.26.mlp.down_proj` | 8 | 6.825 | 0.0301132 | 1 | 13762560 |
| 26 | `model.layers.21.self_attn.k_proj` | 8 | 6.774 | 0.000802813 | 1 | 393472 |
| 27 | `model.layers.2.mlp.down_proj` | 8 | 6.590 | 0.0217587 | 1 | 13762560 |
| 28 | `model.layers.1.mlp.down_proj` | 8 | 6.480 | 0.018669 | 1 | 13762560 |
| 29 | `model.layers.26.self_attn.k_proj` | 8 | 6.480 | 0.000533738 | 1 | 393472 |
| 30 | `model.layers.12.self_attn.k_proj` | 8 | 6.467 | 0.000524095 | 1 | 393472 |
| 31 | `model.layers.27.mlp.down_proj` | 8 | 6.396 | 0.0166315 | 1 | 13762560 |
| 32 | `model.layers.16.self_attn.k_proj` | 8 | 6.389 | 0.000470449 | 1 | 393472 |

## Claim Boundary

This allocator uses measured per-module loss sensitivity. It is still a
budgeted allocation proxy; model quality must be validated by downstream
PPL and task-retention runs.
