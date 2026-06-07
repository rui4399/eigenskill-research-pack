# Lagrangian Loss-Sensitivity Allocation

Formula: `b_i = 0.5 * log2((S_i * sigma_i^2 * ln2) / (lambda * c_i))`
Target average bits: `4.5`
Solved lambda: `1.1915107645845237e-13`
Actual average bits: `4.499844`
Budget satisfied: `True`
Bit histogram: `{'2': 67, '3': 2, '4': 45, '8': 83}`

## Top Protected Records

| rank | name | bits | continuous_bits | sensitivity | variance | cost |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `model.layers.0.self_attn.v_proj` | 8 | 8.000 | 0.0324664 | 1 | 393472 |
| 2 | `model.layers.2.self_attn.v_proj` | 8 | 8.000 | 0.0160085 | 1 | 393472 |
| 3 | `model.layers.3.self_attn.v_proj` | 8 | 8.000 | 0.00912791 | 1 | 393472 |
| 4 | `model.layers.17.self_attn.v_proj` | 8 | 8.000 | 0.0062381 | 1 | 393472 |
| 5 | `model.layers.11.self_attn.v_proj` | 8 | 8.000 | 0.0055052 | 1 | 393472 |
| 6 | `model.layers.7.self_attn.v_proj` | 8 | 8.000 | 0.00479168 | 1 | 393472 |
| 7 | `model.layers.6.self_attn.k_proj` | 8 | 7.893 | 0.00382 | 1 | 393472 |
| 8 | `model.layers.21.self_attn.k_proj` | 8 | 7.711 | 0.00296962 | 1 | 393472 |
| 9 | `model.layers.22.self_attn.k_proj` | 8 | 7.701 | 0.00292736 | 1 | 393472 |
| 10 | `model.layers.1.self_attn.v_proj` | 8 | 7.687 | 0.00287265 | 1 | 393472 |
| 11 | `model.layers.12.self_attn.v_proj` | 8 | 7.683 | 0.00285804 | 1 | 393472 |
| 12 | `model.layers.22.self_attn.v_proj` | 8 | 7.674 | 0.00282133 | 1 | 393472 |
| 13 | `model.layers.10.self_attn.v_proj` | 8 | 7.648 | 0.0027203 | 1 | 393472 |
| 14 | `model.layers.13.self_attn.k_proj` | 8 | 7.584 | 0.00249135 | 1 | 393472 |
| 15 | `model.layers.8.self_attn.v_proj` | 8 | 7.578 | 0.0024696 | 1 | 393472 |
| 16 | `model.layers.16.self_attn.k_proj` | 8 | 7.443 | 0.00204664 | 1 | 393472 |
| 17 | `model.layers.24.self_attn.v_proj` | 8 | 7.436 | 0.00202745 | 1 | 393472 |
| 18 | `model.layers.13.self_attn.v_proj` | 8 | 7.418 | 0.0019775 | 1 | 393472 |
| 19 | `model.layers.14.self_attn.k_proj` | 8 | 7.411 | 0.00195998 | 1 | 393472 |
| 20 | `model.layers.17.self_attn.k_proj` | 8 | 7.280 | 0.00163323 | 1 | 393472 |
| 21 | `model.layers.26.mlp.down_proj` | 8 | 7.139 | 0.0470073 | 1 | 13762560 |
| 22 | `model.layers.15.self_attn.v_proj` | 8 | 7.107 | 0.00128549 | 1 | 393472 |
| 23 | `model.layers.11.self_attn.k_proj` | 8 | 7.078 | 0.00123399 | 1 | 393472 |
| 24 | `model.layers.25.self_attn.k_proj` | 8 | 7.027 | 0.0011512 | 1 | 393472 |
| 25 | `model.layers.24.self_attn.k_proj` | 8 | 7.023 | 0.00114459 | 1 | 393472 |
| 26 | `model.layers.3.self_attn.q_proj` | 8 | 6.987 | 0.0065316 | 1 | 2360832 |
| 27 | `model.layers.12.self_attn.k_proj` | 8 | 6.987 | 0.00108838 | 1 | 393472 |
| 28 | `model.layers.15.self_attn.k_proj` | 8 | 6.944 | 0.00102472 | 1 | 393472 |
| 29 | `model.layers.2.mlp.down_proj` | 8 | 6.921 | 0.0347419 | 1 | 13762560 |
| 30 | `model.layers.27.self_attn.k_proj` | 8 | 6.908 | 0.00097537 | 1 | 393472 |
| 31 | `model.layers.10.self_attn.o_proj` | 8 | 6.861 | 0.00548142 | 1 | 2359296 |
| 32 | `model.layers.20.self_attn.o_proj` | 8 | 6.832 | 0.00526613 | 1 | 2359296 |

## Claim Boundary

This allocator uses measured per-module loss sensitivity. It is still a
budgeted allocation proxy; model quality must be validated by downstream
PPL and task-retention runs.
