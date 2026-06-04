# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs/qwen3_1p7b_loss_sensitive_alloc_4to8_limit2_group128_summary.json`
Right allocation: `outputs/qwen3_1p7b_loss_sensitive_alloc_4to8_c4_limit2_group128_summary.json`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 4.4973 |
| budget used | 0.9994 |
| bit histogram | {'4': 147, '8': 50} |
| 2p 8-bit overlap | 36 |
| 8p 8-bit overlap | 23 |
| locked intersection modules | 10 |
| ranked additions | 40 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | 2p delta | 8p delta | score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.20.self_attn.k_proj` | 2097152 | 0.014196 | 0.020324 | 0.008067 | 6.769e-09 | 1 | 2 |
| `model.layers.16.self_attn.v_proj` | 2097152 | 0.007772 | 0.015543 | 0.000000 | 3.706e-09 | 2 | 165 |
| `model.layers.9.self_attn.v_proj` | 2097152 | 0.007065 | 0.013018 | 0.001111 | 3.369e-09 | 3 | 57 |
| `model.layers.20.self_attn.v_proj` | 2097152 | 0.006978 | 0.005952 | 0.008005 | 3.328e-09 | 11 | 3 |
| `model.layers.6.self_attn.v_proj` | 2097152 | 0.006760 | 0.012337 | 0.001182 | 3.223e-09 | 4 | 54 |
| `model.layers.17.self_attn.v_proj` | 2097152 | 0.004778 | 0.009556 | 0.000000 | 2.278e-09 | 5 | 168 |
| `model.layers.13.self_attn.v_proj` | 2097152 | 0.004238 | 0.004175 | 0.004301 | 2.021e-09 | 17 | 7 |
| `model.layers.5.self_attn.v_proj` | 2097152 | 0.004081 | 0.000000 | 0.008163 | 1.946e-09 | 132 | 1 |
| `model.layers.18.self_attn.v_proj` | 2097152 | 0.004033 | 0.008066 | 0.000000 | 1.923e-09 | 6 | 171 |
| `model.layers.4.self_attn.v_proj` | 2097152 | 0.003932 | 0.003627 | 0.004237 | 1.875e-09 | 19 | 8 |
| `model.layers.21.self_attn.v_proj` | 2097152 | 0.003798 | 0.006242 | 0.001354 | 1.811e-09 | 10 | 50 |
| `model.layers.16.self_attn.k_proj` | 2097152 | 0.003736 | 0.007472 | 0.000000 | 1.782e-09 | 7 | 164 |
| `model.layers.21.self_attn.k_proj` | 2097152 | 0.003723 | 0.002180 | 0.005266 | 1.775e-09 | 37 | 5 |
| `model.layers.26.self_attn.k_proj` | 2097152 | 0.003646 | 0.003525 | 0.003767 | 1.738e-09 | 20 | 9 |
| `model.layers.14.self_attn.k_proj` | 2097152 | 0.003621 | 0.002082 | 0.005161 | 1.727e-09 | 40 | 6 |
| `model.layers.11.self_attn.v_proj` | 2097152 | 0.003589 | 0.006665 | 0.000513 | 1.711e-09 | 9 | 86 |
| `model.layers.7.self_attn.v_proj` | 2097152 | 0.003434 | 0.006869 | 0.000000 | 1.638e-09 | 8 | 143 |
| `model.layers.18.self_attn.k_proj` | 2097152 | 0.003240 | 0.003437 | 0.003043 | 1.545e-09 | 24 | 13 |
| `model.layers.27.mlp.down_proj` | 12582912 | 0.018720 | 0.004142 | 0.033298 | 1.488e-09 | 85 | 4 |
| `model.layers.9.self_attn.o_proj` | 4194304 | 0.005837 | 0.004477 | 0.007198 | 1.392e-09 | 36 | 11 |
| `model.layers.12.self_attn.k_proj` | 2097152 | 0.002903 | 0.005806 | 0.000000 | 1.384e-09 | 12 | 153 |
| `model.layers.6.mlp.up_proj` | 12582912 | 0.016800 | 0.019579 | 0.014021 | 1.335e-09 | 26 | 25 |
| `model.layers.27.self_attn.k_proj` | 2097152 | 0.002660 | 0.004304 | 0.001015 | 1.268e-09 | 16 | 63 |
| `model.layers.6.self_attn.o_proj` | 4194304 | 0.005007 | 0.009570 | 0.000444 | 1.194e-09 | 13 | 105 |
| `model.layers.1.self_attn.o_proj` | 4194304 | 0.004768 | 0.009535 | 0.000000 | 1.137e-09 | 14 | 126 |
| `model.layers.4.self_attn.k_proj` | 2097152 | 0.002183 | 0.004365 | 0.000000 | 1.041e-09 | 15 | 134 |
| `model.layers.23.self_attn.v_proj` | 2097152 | 0.002080 | 0.004159 | 0.000000 | 9.916e-10 | 18 | 186 |
| `model.layers.25.self_attn.q_proj` | 4194304 | 0.004092 | 0.005234 | 0.002950 | 9.757e-10 | 33 | 41 |
| `model.layers.2.self_attn.k_proj` | 2097152 | 0.001986 | 0.000477 | 0.003495 | 9.470e-10 | 95 | 12 |
| `model.layers.7.mlp.gate_proj` | 12582912 | 0.011799 | 0.021073 | 0.002526 | 9.377e-10 | 21 | 93 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
