# Lagrangian Loss-Sensitivity Allocation

Formula: `b_i = 0.5 * log2((S_i * sigma_i^2 * ln2) / (lambda * c_i))`
Target average bits: `4.5`
Solved lambda: `3.746141399727346e-13`
Actual average bits: `4.499918`
Budget satisfied: `True`
Bit histogram: `{'2': 60, '3': 2, '4': 34, '8': 73}`

## Top Protected Records

| rank | name | bits | continuous_bits | sensitivity | variance | cost |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `model.layers.16.self_attn.v_proj` | 8 | 8.000 | 0.018912 | 1 | 114816 |
| 2 | `model.layers.3.self_attn.v_proj` | 8 | 8.000 | 0.0150332 | 1 | 114816 |
| 3 | `model.layers.8.self_attn.v_proj` | 8 | 8.000 | 0.0107104 | 1 | 114816 |
| 4 | `model.layers.6.self_attn.v_proj` | 8 | 8.000 | 0.00669903 | 1 | 114816 |
| 5 | `model.layers.0.self_attn.v_proj` | 8 | 8.000 | 0.00521934 | 1 | 114816 |
| 6 | `model.layers.19.self_attn.k_proj` | 8 | 8.000 | 0.00499749 | 1 | 114816 |
| 7 | `model.layers.20.self_attn.k_proj` | 8 | 8.000 | 0.00463593 | 1 | 114816 |
| 8 | `model.layers.17.self_attn.v_proj` | 8 | 8.000 | 0.00418359 | 1 | 114816 |
| 9 | `model.layers.19.self_attn.v_proj` | 8 | 7.844 | 0.00327468 | 1 | 114816 |
| 10 | `model.layers.10.self_attn.v_proj` | 8 | 7.787 | 0.00302798 | 1 | 114816 |
| 11 | `model.layers.2.self_attn.v_proj` | 8 | 7.783 | 0.00300813 | 1 | 114816 |
| 12 | `model.layers.2.mlp.down_proj` | 8 | 7.685 | 0.0997796 | 1 | 4358144 |
| 13 | `model.layers.8.self_attn.k_proj` | 8 | 7.635 | 0.00245208 | 1 | 114816 |
| 14 | `model.layers.10.self_attn.k_proj` | 8 | 7.599 | 0.00233227 | 1 | 114816 |
| 15 | `model.layers.4.self_attn.k_proj` | 8 | 7.596 | 0.00232291 | 1 | 114816 |
| 16 | `model.layers.13.self_attn.k_proj` | 8 | 7.549 | 0.00217736 | 1 | 114816 |
| 17 | `model.layers.2.self_attn.o_proj` | 8 | 7.488 | 0.0139802 | 1 | 802816 |
| 18 | `model.layers.9.self_attn.k_proj` | 8 | 7.463 | 0.00193036 | 1 | 114816 |
| 19 | `model.layers.6.self_attn.k_proj` | 8 | 7.432 | 0.00185096 | 1 | 114816 |
| 20 | `model.layers.22.self_attn.v_proj` | 8 | 7.326 | 0.00159711 | 1 | 114816 |
| 21 | `model.layers.2.self_attn.k_proj` | 8 | 7.220 | 0.00137961 | 1 | 114816 |
| 22 | `model.layers.23.self_attn.k_proj` | 8 | 7.178 | 0.00130141 | 1 | 114816 |
| 23 | `model.layers.22.self_attn.k_proj` | 8 | 7.116 | 0.00119376 | 1 | 114816 |
| 24 | `model.layers.23.self_attn.v_proj` | 8 | 7.109 | 0.00118327 | 1 | 114816 |
| 25 | `model.layers.21.mlp.down_proj` | 8 | 7.106 | 0.0447204 | 1 | 4358144 |
| 26 | `model.layers.5.self_attn.v_proj` | 8 | 7.023 | 0.0010491 | 1 | 114816 |
| 27 | `model.layers.10.self_attn.q_proj` | 8 | 6.923 | 0.00639486 | 1 | 803712 |
| 28 | `model.layers.11.self_attn.v_proj` | 8 | 6.910 | 0.000896931 | 1 | 114816 |
| 29 | `model.layers.22.self_attn.o_proj` | 8 | 6.843 | 0.00571549 | 1 | 802816 |
| 30 | `model.layers.15.self_attn.o_proj` | 8 | 6.782 | 0.00525814 | 1 | 802816 |
| 31 | `model.layers.23.mlp.down_proj` | 8 | 6.717 | 0.0260571 | 1 | 4358144 |
| 32 | `model.layers.12.self_attn.o_proj` | 8 | 6.670 | 0.00450116 | 1 | 802816 |

## Claim Boundary

This allocator uses measured per-module loss sensitivity. It is still a
budgeted allocation proxy; model quality must be validated by downstream
PPL and task-retention runs.
