# Lagrangian Loss-Sensitivity Allocation

Formula: `b_i = 0.5 * log2((S_i * sigma_i^2 * ln2) / (lambda * c_i))`
Target average bits: `4.5`
Solved lambda: `5.665460628521507e-13`
Actual average bits: `4.499670`
Budget satisfied: `True`
Bit histogram: `{'3': 87, '4': 45, '8': 65}`

## Top Protected Records

| rank | name | bits | continuous_bits | sensitivity | variance | cost |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `model.layers.20.self_attn.v_proj` | 8 | 7.382 | 0.0238397 | 1 | 1048576 |
| 2 | `model.layers.21.self_attn.v_proj` | 8 | 7.347 | 0.0227079 | 1 | 1048576 |
| 3 | `model.layers.18.self_attn.v_proj` | 8 | 7.225 | 0.019195 | 1 | 1048576 |
| 4 | `model.layers.4.self_attn.v_proj` | 8 | 7.219 | 0.0190271 | 1 | 1048576 |
| 5 | `model.layers.10.self_attn.k_proj` | 8 | 7.112 | 0.0163927 | 1 | 1048576 |
| 6 | `model.layers.1.mlp.gate_proj` | 8 | 7.050 | 0.0451198 | 1 | 3145728 |
| 7 | `model.layers.17.self_attn.v_proj` | 8 | 7.024 | 0.014515 | 1 | 1048576 |
| 8 | `model.layers.26.mlp.up_proj` | 8 | 6.968 | 0.0403252 | 1 | 3145728 |
| 9 | `model.layers.26.mlp.gate_proj` | 8 | 6.956 | 0.0396156 | 1 | 3145728 |
| 10 | `model.layers.23.self_attn.k_proj` | 8 | 6.953 | 0.0131642 | 1 | 1048576 |
| 11 | `model.layers.16.self_attn.v_proj` | 8 | 6.923 | 0.012621 | 1 | 1048576 |
| 12 | `model.layers.26.self_attn.k_proj` | 8 | 6.899 | 0.0122093 | 1 | 1048576 |
| 13 | `model.layers.21.self_attn.k_proj` | 8 | 6.893 | 0.012098 | 1 | 1048576 |
| 14 | `model.layers.2.mlp.up_proj` | 8 | 6.838 | 0.033632 | 1 | 3145728 |
| 15 | `model.layers.1.self_attn.v_proj` | 8 | 6.777 | 0.0103117 | 1 | 1048576 |
| 16 | `model.layers.20.self_attn.k_proj` | 8 | 6.743 | 0.00983407 | 1 | 1048576 |
| 17 | `model.layers.4.self_attn.k_proj` | 8 | 6.613 | 0.00821507 | 1 | 1048576 |
| 18 | `model.layers.0.mlp.up_proj` | 8 | 6.590 | 0.023861 | 1 | 3145728 |
| 19 | `model.layers.22.self_attn.v_proj` | 8 | 6.553 | 0.00755615 | 1 | 1048576 |
| 20 | `model.layers.11.self_attn.o_proj` | 8 | 6.551 | 0.0150729 | 1 | 2097152 |
| 21 | `model.layers.16.self_attn.k_proj` | 8 | 6.547 | 0.0074922 | 1 | 1048576 |
| 22 | `model.layers.23.self_attn.q_proj` | 8 | 6.542 | 0.014886 | 1 | 2097152 |
| 23 | `model.layers.25.self_attn.o_proj` | 8 | 6.528 | 0.0145978 | 1 | 2097152 |
| 24 | `model.layers.15.self_attn.v_proj` | 8 | 6.515 | 0.00716607 | 1 | 1048576 |
| 25 | `model.layers.2.self_attn.o_proj` | 8 | 6.483 | 0.0137187 | 1 | 2097152 |
| 26 | `model.layers.19.self_attn.k_proj` | 8 | 6.424 | 0.00631821 | 1 | 1048576 |
| 27 | `model.layers.3.mlp.up_proj` | 8 | 6.359 | 0.0173165 | 1 | 3145728 |
| 28 | `model.layers.26.mlp.down_proj` | 8 | 6.358 | 0.0173013 | 1 | 3145728 |
| 29 | `model.layers.7.self_attn.v_proj` | 8 | 6.305 | 0.005358 | 1 | 1048576 |
| 30 | `model.layers.20.self_attn.q_proj` | 8 | 6.301 | 0.0106494 | 1 | 2097152 |
| 31 | `model.layers.0.self_attn.k_proj` | 8 | 6.268 | 0.00508988 | 1 | 1048576 |
| 32 | `model.layers.2.self_attn.k_proj` | 8 | 6.263 | 0.00505564 | 1 | 1048576 |

## Claim Boundary

This allocator uses measured per-module loss sensitivity. It is still a
budgeted allocation proxy; model quality must be validated by downstream
PPL and task-retention runs.
