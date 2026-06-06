# Lagrangian Loss-Sensitivity Allocation

Formula: `b_i = 0.5 * log2((S_i * sigma_i^2 * ln2) / (lambda * c_i))`
Target average bits: `4.5`
Solved lambda: `1.188321261127239e-12`
Actual average bits: `4.499670`
Budget satisfied: `True`
Bit histogram: `{'4': 153, '8': 44}`

## Top Protected Records

| rank | name | bits | continuous_bits | sensitivity | variance | cost |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `model.layers.20.self_attn.v_proj` | 8 | 6.847 | 0.0238397 | 1 | 1048576 |
| 2 | `model.layers.21.self_attn.v_proj` | 8 | 6.812 | 0.0227079 | 1 | 1048576 |
| 3 | `model.layers.18.self_attn.v_proj` | 8 | 6.691 | 0.019195 | 1 | 1048576 |
| 4 | `model.layers.4.self_attn.v_proj` | 8 | 6.685 | 0.0190271 | 1 | 1048576 |
| 5 | `model.layers.10.self_attn.k_proj` | 8 | 6.577 | 0.0163927 | 1 | 1048576 |
| 6 | `model.layers.1.mlp.gate_proj` | 8 | 6.515 | 0.0451198 | 1 | 3145728 |
| 7 | `model.layers.17.self_attn.v_proj` | 8 | 6.490 | 0.014515 | 1 | 1048576 |
| 8 | `model.layers.26.mlp.up_proj` | 8 | 6.434 | 0.0403252 | 1 | 3145728 |
| 9 | `model.layers.26.mlp.gate_proj` | 8 | 6.421 | 0.0396156 | 1 | 3145728 |
| 10 | `model.layers.23.self_attn.k_proj` | 8 | 6.419 | 0.0131642 | 1 | 1048576 |
| 11 | `model.layers.16.self_attn.v_proj` | 8 | 6.389 | 0.012621 | 1 | 1048576 |
| 12 | `model.layers.26.self_attn.k_proj` | 8 | 6.365 | 0.0122093 | 1 | 1048576 |
| 13 | `model.layers.21.self_attn.k_proj` | 8 | 6.358 | 0.012098 | 1 | 1048576 |
| 14 | `model.layers.2.mlp.up_proj` | 8 | 6.303 | 0.033632 | 1 | 3145728 |
| 15 | `model.layers.1.self_attn.v_proj` | 8 | 6.243 | 0.0103117 | 1 | 1048576 |
| 16 | `model.layers.20.self_attn.k_proj` | 8 | 6.209 | 0.00983407 | 1 | 1048576 |
| 17 | `model.layers.4.self_attn.k_proj` | 8 | 6.079 | 0.00821507 | 1 | 1048576 |
| 18 | `model.layers.0.mlp.up_proj` | 8 | 6.056 | 0.023861 | 1 | 3145728 |
| 19 | `model.layers.22.self_attn.v_proj` | 8 | 6.019 | 0.00755615 | 1 | 1048576 |
| 20 | `model.layers.11.self_attn.o_proj` | 8 | 6.017 | 0.0150729 | 1 | 2097152 |
| 21 | `model.layers.16.self_attn.k_proj` | 8 | 6.013 | 0.0074922 | 1 | 1048576 |
| 22 | `model.layers.23.self_attn.q_proj` | 8 | 6.008 | 0.014886 | 1 | 2097152 |
| 23 | `model.layers.25.self_attn.o_proj` | 8 | 5.994 | 0.0145978 | 1 | 2097152 |
| 24 | `model.layers.15.self_attn.v_proj` | 8 | 5.980 | 0.00716607 | 1 | 1048576 |
| 25 | `model.layers.2.self_attn.o_proj` | 8 | 5.949 | 0.0137187 | 1 | 2097152 |
| 26 | `model.layers.19.self_attn.k_proj` | 8 | 5.890 | 0.00631821 | 1 | 1048576 |
| 27 | `model.layers.3.mlp.up_proj` | 8 | 5.824 | 0.0173165 | 1 | 3145728 |
| 28 | `model.layers.26.mlp.down_proj` | 8 | 5.824 | 0.0173013 | 1 | 3145728 |
| 29 | `model.layers.7.self_attn.v_proj` | 8 | 5.771 | 0.005358 | 1 | 1048576 |
| 30 | `model.layers.20.self_attn.q_proj` | 8 | 5.766 | 0.0106494 | 1 | 2097152 |
| 31 | `model.layers.0.self_attn.k_proj` | 8 | 5.734 | 0.00508988 | 1 | 1048576 |
| 32 | `model.layers.2.self_attn.k_proj` | 8 | 5.729 | 0.00505564 | 1 | 1048576 |

## Claim Boundary

This allocator uses measured per-module loss sensitivity. It is still a
budgeted allocation proxy; model quality must be validated by downstream
PPL and task-retention runs.
