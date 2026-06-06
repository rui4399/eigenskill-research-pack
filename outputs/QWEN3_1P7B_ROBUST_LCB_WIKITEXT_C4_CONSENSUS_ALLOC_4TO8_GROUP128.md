# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\qwen3_1p7b_loss_sensitive_alloc_4to8_limit2_group128_summary.json`
Right allocation: `outputs\qwen3_1p7b_loss_sensitive_alloc_4to8_c4_limit2_group128_summary.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 4.4973 |
| budget used | 0.9994 |
| bit histogram | {'8': 41, '4': 156} |
| 2p 8-bit overlap | 19 |
| 8p 8-bit overlap | 23 |
| locked intersection modules | 10 |
| ranked additions | 31 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.20.self_attn.k_proj` | 2097152 | 0.014196 | 0.008067 | 0.5683 | 0.020324 | 0.008067 | 3.847e-09 | 1 | 2 |
| `model.layers.20.self_attn.v_proj` | 2097152 | 0.006978 | 0.005952 | 0.8529 | 0.005952 | 0.008005 | 2.838e-09 | 11 | 3 |
| `model.layers.13.self_attn.v_proj` | 2097152 | 0.004238 | 0.004175 | 0.9851 | 0.004175 | 0.004301 | 1.991e-09 | 17 | 7 |
| `model.layers.4.self_attn.v_proj` | 2097152 | 0.003932 | 0.003627 | 0.9225 | 0.003627 | 0.004237 | 1.730e-09 | 19 | 8 |
| `model.layers.26.self_attn.k_proj` | 2097152 | 0.003646 | 0.003525 | 0.9667 | 0.003525 | 0.003767 | 1.681e-09 | 20 | 9 |
| `model.layers.18.self_attn.k_proj` | 2097152 | 0.003240 | 0.003043 | 0.9393 | 0.003437 | 0.003043 | 1.451e-09 | 24 | 13 |
| `model.layers.6.mlp.up_proj` | 12582912 | 0.016800 | 0.014021 | 0.8346 | 0.019579 | 0.014021 | 1.114e-09 | 26 | 25 |
| `model.layers.9.self_attn.o_proj` | 4194304 | 0.005837 | 0.004477 | 0.7669 | 0.004477 | 0.007198 | 1.067e-09 | 36 | 11 |
| `model.layers.21.self_attn.k_proj` | 2097152 | 0.003723 | 0.002180 | 0.5855 | 0.002180 | 0.005266 | 1.039e-09 | 37 | 5 |
| `model.layers.14.self_attn.k_proj` | 2097152 | 0.003621 | 0.002082 | 0.5748 | 0.002082 | 0.005161 | 9.927e-10 | 40 | 6 |
| `model.layers.25.self_attn.q_proj` | 4194304 | 0.004092 | 0.002950 | 0.7210 | 0.005234 | 0.002950 | 7.034e-10 | 33 | 41 |
| `model.layers.14.mlp.up_proj` | 12582912 | 0.008957 | 0.008524 | 0.9517 | 0.008524 | 0.009389 | 6.774e-10 | 51 | 39 |
| `model.layers.18.self_attn.q_proj` | 4194304 | 0.002831 | 0.002814 | 0.9941 | 0.002848 | 0.002814 | 6.710e-10 | 50 | 46 |
| `model.layers.7.self_attn.k_proj` | 2097152 | 0.001911 | 0.001374 | 0.7189 | 0.001374 | 0.002448 | 6.550e-10 | 53 | 21 |
| `model.layers.9.self_attn.k_proj` | 2097152 | 0.001479 | 0.001355 | 0.9164 | 0.001602 | 0.001355 | 6.463e-10 | 46 | 48 |
| `model.layers.21.self_attn.v_proj` | 2097152 | 0.003798 | 0.001354 | 0.3565 | 0.006242 | 0.001354 | 6.457e-10 | 10 | 50 |
| `model.layers.7.self_attn.o_proj` | 4194304 | 0.003153 | 0.002660 | 0.8436 | 0.003646 | 0.002660 | 6.342e-10 | 44 | 51 |
| `model.layers.6.self_attn.v_proj` | 2097152 | 0.006760 | 0.001182 | 0.1748 | 0.012337 | 0.001182 | 5.635e-10 | 4 | 54 |
| `model.layers.9.self_attn.v_proj` | 2097152 | 0.007065 | 0.001111 | 0.1573 | 0.013018 | 0.001111 | 5.300e-10 | 3 | 57 |
| `model.layers.15.self_attn.k_proj` | 2097152 | 0.001704 | 0.001089 | 0.6392 | 0.001089 | 0.002319 | 5.193e-10 | 59 | 26 |
| `model.layers.0.self_attn.q_proj` | 4194304 | 0.002646 | 0.002066 | 0.7809 | 0.002066 | 0.003226 | 4.926e-10 | 61 | 37 |
| `model.layers.27.self_attn.k_proj` | 2097152 | 0.002660 | 0.001015 | 0.3817 | 0.004304 | 0.001015 | 4.840e-10 | 16 | 63 |
| `model.layers.1.self_attn.k_proj` | 2097152 | 0.001199 | 0.000980 | 0.8175 | 0.000980 | 0.001418 | 4.675e-10 | 63 | 45 |
| `model.layers.19.self_attn.q_proj` | 4194304 | 0.002835 | 0.001930 | 0.6808 | 0.001930 | 0.003739 | 4.601e-10 | 64 | 30 |
| `model.layers.21.self_attn.q_proj` | 4194304 | 0.003278 | 0.001820 | 0.5552 | 0.001820 | 0.004736 | 4.339e-10 | 67 | 24 |
| `model.layers.5.self_attn.k_proj` | 2097152 | 0.001749 | 0.000901 | 0.5154 | 0.000901 | 0.002597 | 4.298e-10 | 68 | 19 |
| `model.layers.8.mlp.down_proj` | 12582912 | 0.008615 | 0.005342 | 0.6201 | 0.011888 | 0.005342 | 4.246e-10 | 41 | 69 |
| `model.layers.25.mlp.gate_proj` | 12582912 | 0.005465 | 0.005307 | 0.9711 | 0.005307 | 0.005623 | 4.217e-10 | 70 | 66 |
| `model.layers.25.self_attn.k_proj` | 2097152 | 0.001337 | 0.000860 | 0.6435 | 0.000860 | 0.001813 | 4.102e-10 | 72 | 32 |
| `model.layers.17.self_attn.o_proj` | 4194304 | 0.003297 | 0.001713 | 0.5196 | 0.001713 | 0.004881 | 4.084e-10 | 73 | 22 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
