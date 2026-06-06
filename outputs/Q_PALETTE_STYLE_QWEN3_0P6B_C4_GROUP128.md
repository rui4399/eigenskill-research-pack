# Lagrangian Loss-Sensitivity Allocation

Formula: `b_i = 0.5 * log2((S_i * sigma_i^2 * ln2) / (lambda * c_i))`
Target average bits: `4.5`
Solved lambda: `3.646024502837154e-13`
Actual average bits: `4.499670`
Budget satisfied: `True`
Bit histogram: `{'3': 73, '4': 63, '8': 61}`

## Top Protected Records

| rank | name | bits | continuous_bits | sensitivity | variance | cost |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `model.layers.0.self_attn.v_proj` | 8 | 7.735 | 0.0250319 | 1 | 1048576 |
| 2 | `model.layers.2.self_attn.v_proj` | 8 | 7.306 | 0.0138115 | 1 | 1048576 |
| 3 | `model.layers.2.mlp.down_proj` | 8 | 7.009 | 0.0274324 | 1 | 3145728 |
| 4 | `model.layers.11.self_attn.k_proj` | 8 | 6.802 | 0.00687188 | 1 | 1048576 |
| 5 | `model.layers.20.self_attn.q_proj` | 8 | 6.771 | 0.0131571 | 1 | 2097152 |
| 6 | `model.layers.27.mlp.down_proj` | 8 | 6.652 | 0.0167437 | 1 | 3145728 |
| 7 | `model.layers.10.self_attn.v_proj` | 8 | 6.632 | 0.00542295 | 1 | 1048576 |
| 8 | `model.layers.12.self_attn.k_proj` | 8 | 6.618 | 0.00532085 | 1 | 1048576 |
| 9 | `model.layers.16.self_attn.v_proj` | 8 | 6.536 | 0.00474918 | 1 | 1048576 |
| 10 | `model.layers.12.self_attn.v_proj` | 8 | 6.505 | 0.00455087 | 1 | 1048576 |
| 11 | `model.layers.19.self_attn.k_proj` | 8 | 6.463 | 0.00428963 | 1 | 1048576 |
| 12 | `model.layers.20.mlp.up_proj` | 8 | 6.441 | 0.0124919 | 1 | 3145728 |
| 13 | `model.layers.26.mlp.up_proj` | 8 | 6.421 | 0.0121527 | 1 | 3145728 |
| 14 | `model.layers.15.self_attn.k_proj` | 8 | 6.408 | 0.0039798 | 1 | 1048576 |
| 15 | `model.layers.26.self_attn.q_proj` | 8 | 6.374 | 0.00758612 | 1 | 2097152 |
| 16 | `model.layers.7.self_attn.v_proj` | 8 | 6.337 | 0.00360358 | 1 | 1048576 |
| 17 | `model.layers.4.mlp.gate_proj` | 8 | 6.295 | 0.0102023 | 1 | 3145728 |
| 18 | `model.layers.25.self_attn.v_proj` | 8 | 6.289 | 0.00337374 | 1 | 1048576 |
| 19 | `model.layers.26.mlp.down_proj` | 8 | 6.258 | 0.00969297 | 1 | 3145728 |
| 20 | `model.layers.14.self_attn.v_proj` | 8 | 6.219 | 0.00305885 | 1 | 1048576 |
| 21 | `model.layers.23.mlp.up_proj` | 8 | 6.188 | 0.00879908 | 1 | 3145728 |
| 22 | `model.layers.27.self_attn.k_proj` | 8 | 6.183 | 0.00291276 | 1 | 1048576 |
| 23 | `model.layers.27.mlp.up_proj` | 8 | 6.180 | 0.00870341 | 1 | 3145728 |
| 24 | `model.layers.9.self_attn.k_proj` | 8 | 6.175 | 0.0028792 | 1 | 1048576 |
| 25 | `model.layers.3.self_attn.q_proj` | 8 | 6.167 | 0.00569373 | 1 | 2097152 |
| 26 | `model.layers.3.mlp.gate_proj` | 8 | 6.163 | 0.0084933 | 1 | 3145728 |
| 27 | `model.layers.7.mlp.up_proj` | 8 | 6.143 | 0.0082649 | 1 | 3145728 |
| 28 | `model.layers.20.self_attn.k_proj` | 8 | 6.140 | 0.00274414 | 1 | 1048576 |
| 29 | `model.layers.24.self_attn.v_proj` | 8 | 6.124 | 0.00268352 | 1 | 1048576 |
| 30 | `model.layers.21.self_attn.k_proj` | 8 | 6.122 | 0.0026772 | 1 | 1048576 |
| 31 | `model.layers.4.self_attn.v_proj` | 8 | 6.119 | 0.00266373 | 1 | 1048576 |
| 32 | `model.layers.22.self_attn.k_proj` | 8 | 6.113 | 0.00264174 | 1 | 1048576 |

## Claim Boundary

This allocator uses measured per-module loss sensitivity. It is still a
budgeted allocation proxy; model quality must be validated by downstream
PPL and task-retention runs.
