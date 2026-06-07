# Lagrangian Loss-Sensitivity Allocation

Formula: `b_i = 0.5 * log2((S_i * sigma_i^2 * ln2) / (lambda * c_i))`
Target average bits: `4.5`
Solved lambda: `3.9534494921989976e-13`
Actual average bits: `4.499912`
Budget satisfied: `True`
Bit histogram: `{'2': 54, '3': 3, '4': 37, '8': 75}`

## Top Protected Records

| rank | name | bits | continuous_bits | sensitivity | variance | cost |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `model.layers.3.self_attn.v_proj` | 8 | 8.000 | 0.0121354 | 1 | 114816 |
| 2 | `model.layers.8.self_attn.v_proj` | 8 | 8.000 | 0.010064 | 1 | 114816 |
| 3 | `model.layers.16.self_attn.v_proj` | 8 | 8.000 | 0.0083776 | 1 | 114816 |
| 4 | `model.layers.11.self_attn.v_proj` | 8 | 8.000 | 0.00524879 | 1 | 114816 |
| 5 | `model.layers.6.self_attn.v_proj` | 8 | 8.000 | 0.00517965 | 1 | 114816 |
| 6 | `model.layers.12.self_attn.v_proj` | 8 | 8.000 | 0.00465637 | 1 | 114816 |
| 7 | `model.layers.2.self_attn.v_proj` | 8 | 8.000 | 0.00461204 | 1 | 114816 |
| 8 | `model.layers.17.self_attn.v_proj` | 8 | 7.735 | 0.00297169 | 1 | 114816 |
| 9 | `model.layers.19.self_attn.v_proj` | 8 | 7.728 | 0.00294364 | 1 | 114816 |
| 10 | `model.layers.9.self_attn.k_proj` | 8 | 7.638 | 0.00259931 | 1 | 114816 |
| 11 | `model.layers.22.self_attn.v_proj` | 8 | 7.569 | 0.00236279 | 1 | 114816 |
| 12 | `model.layers.2.mlp.down_proj` | 8 | 7.509 | 0.0825218 | 1 | 4358144 |
| 13 | `model.layers.10.self_attn.k_proj` | 8 | 7.439 | 0.00197116 | 1 | 114816 |
| 14 | `model.layers.19.self_attn.k_proj` | 8 | 7.434 | 0.00195767 | 1 | 114816 |
| 15 | `model.layers.8.self_attn.k_proj` | 8 | 7.372 | 0.00179747 | 1 | 114816 |
| 16 | `model.layers.2.self_attn.k_proj` | 8 | 7.367 | 0.00178565 | 1 | 114816 |
| 17 | `model.layers.23.self_attn.k_proj` | 8 | 7.344 | 0.00172933 | 1 | 114816 |
| 18 | `model.layers.10.self_attn.v_proj` | 8 | 7.300 | 0.00162657 | 1 | 114816 |
| 19 | `model.layers.20.self_attn.k_proj` | 8 | 7.132 | 0.00128837 | 1 | 114816 |
| 20 | `model.layers.21.mlp.down_proj` | 8 | 6.978 | 0.0394947 | 1 | 4358144 |
| 21 | `model.layers.7.self_attn.k_proj` | 8 | 6.967 | 0.00102544 | 1 | 114816 |
| 22 | `model.layers.12.self_attn.k_proj` | 8 | 6.911 | 0.000948735 | 1 | 114816 |
| 23 | `model.layers.23.self_attn.v_proj` | 8 | 6.874 | 0.000900635 | 1 | 114816 |
| 24 | `model.layers.1.self_attn.k_proj` | 8 | 6.812 | 0.000827286 | 1 | 114816 |
| 25 | `model.layers.6.self_attn.k_proj` | 8 | 6.735 | 0.00074268 | 1 | 114816 |
| 26 | `model.layers.3.mlp.down_proj` | 8 | 6.705 | 0.0270637 | 1 | 4358144 |
| 27 | `model.layers.22.self_attn.o_proj` | 8 | 6.522 | 0.00386693 | 1 | 802816 |
| 28 | `model.layers.23.self_attn.o_proj` | 8 | 6.520 | 0.00385507 | 1 | 802816 |
| 29 | `model.layers.20.self_attn.v_proj` | 8 | 6.478 | 0.000520492 | 1 | 114816 |
| 30 | `model.layers.23.mlp.down_proj` | 8 | 6.440 | 0.0187342 | 1 | 4358144 |
| 31 | `model.layers.5.self_attn.k_proj` | 8 | 6.409 | 0.000473077 | 1 | 114816 |
| 32 | `model.layers.20.self_attn.o_proj` | 8 | 6.343 | 0.00301923 | 1 | 802816 |

## Claim Boundary

This allocator uses measured per-module loss sensitivity. It is still a
budgeted allocation proxy; model quality must be validated by downstream
PPL and task-retention runs.
