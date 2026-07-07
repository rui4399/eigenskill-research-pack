# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n128_seed0_alloc_2to4_budget3.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n128_seed1_alloc_2to4_budget3.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 2.9999 |
| budget used | 1.0000 |
| bit histogram | {'2': 94, '4': 103} |
| 2p 8-bit overlap | 102 |
| 8p 8-bit overlap | 102 |
| locked intersection modules | 102 |
| ranked additions | 1 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.v_proj` | 393472 | 0.006237 | 0.006237 | 1.0000 | 0.006237 | 0.006237 | 1.585e-08 | 1 | 1 |
| `model.layers.17.self_attn.v_proj` | 393472 | 0.001938 | 0.001938 | 1.0000 | 0.001938 | 0.001938 | 4.926e-09 | 2 | 2 |
| `model.layers.1.mlp.down_proj` | 13762560 | 0.055863 | 0.055863 | 1.0000 | 0.055863 | 0.055863 | 4.059e-09 | 3 | 3 |
| `model.layers.21.self_attn.v_proj` | 393472 | 0.001515 | 0.001515 | 1.0000 | 0.001515 | 0.001515 | 3.851e-09 | 4 | 4 |
| `model.layers.22.self_attn.v_proj` | 393472 | 0.001478 | 0.001478 | 1.0000 | 0.001478 | 0.001478 | 3.755e-09 | 5 | 5 |
| `model.layers.4.self_attn.v_proj` | 393472 | 0.001315 | 0.001315 | 1.0000 | 0.001315 | 0.001315 | 3.342e-09 | 6 | 6 |
| `model.layers.16.self_attn.v_proj` | 393472 | 0.001185 | 0.001185 | 1.0000 | 0.001185 | 0.001185 | 3.013e-09 | 7 | 7 |
| `model.layers.18.self_attn.v_proj` | 393472 | 0.001100 | 0.001100 | 1.0000 | 0.001100 | 0.001100 | 2.796e-09 | 8 | 8 |
| `model.layers.3.self_attn.v_proj` | 393472 | 0.001095 | 0.001095 | 1.0000 | 0.001095 | 0.001095 | 2.783e-09 | 9 | 9 |
| `model.layers.4.self_attn.k_proj` | 393472 | 0.001052 | 0.001052 | 1.0000 | 0.001052 | 0.001052 | 2.674e-09 | 10 | 10 |
| `model.layers.17.self_attn.k_proj` | 393472 | 0.001031 | 0.001031 | 1.0000 | 0.001031 | 0.001031 | 2.621e-09 | 11 | 11 |
| `model.layers.15.self_attn.v_proj` | 393472 | 0.001020 | 0.001020 | 1.0000 | 0.001020 | 0.001020 | 2.593e-09 | 12 | 12 |
| `model.layers.9.self_attn.v_proj` | 393472 | 0.000989 | 0.000989 | 1.0000 | 0.000989 | 0.000989 | 2.514e-09 | 13 | 13 |
| `model.layers.2.mlp.down_proj` | 13762560 | 0.034037 | 0.034037 | 1.0000 | 0.034037 | 0.034037 | 2.473e-09 | 14 | 14 |
| `model.layers.10.self_attn.v_proj` | 393472 | 0.000944 | 0.000944 | 1.0000 | 0.000944 | 0.000944 | 2.400e-09 | 15 | 15 |
| `model.layers.14.self_attn.k_proj` | 393472 | 0.000899 | 0.000899 | 1.0000 | 0.000899 | 0.000899 | 2.284e-09 | 16 | 16 |
| `model.layers.26.mlp.down_proj` | 13762560 | 0.030078 | 0.030078 | 1.0000 | 0.030078 | 0.030078 | 2.186e-09 | 17 | 17 |
| `model.layers.23.self_attn.k_proj` | 393472 | 0.000829 | 0.000829 | 1.0000 | 0.000829 | 0.000829 | 2.106e-09 | 18 | 18 |
| `model.layers.10.self_attn.k_proj` | 393472 | 0.000821 | 0.000821 | 1.0000 | 0.000821 | 0.000821 | 2.087e-09 | 19 | 19 |
| `model.layers.25.self_attn.v_proj` | 393472 | 0.000773 | 0.000773 | 1.0000 | 0.000773 | 0.000773 | 1.964e-09 | 20 | 20 |
| `model.layers.20.self_attn.v_proj` | 393472 | 0.000748 | 0.000748 | 1.0000 | 0.000748 | 0.000748 | 1.901e-09 | 21 | 21 |
| `model.layers.24.self_attn.v_proj` | 393472 | 0.000748 | 0.000748 | 1.0000 | 0.000748 | 0.000748 | 1.901e-09 | 22 | 22 |
| `model.layers.1.self_attn.o_proj` | 2359296 | 0.003074 | 0.003074 | 1.0000 | 0.003074 | 0.003074 | 1.303e-09 | 23 | 23 |
| `model.layers.12.self_attn.v_proj` | 393472 | 0.000484 | 0.000484 | 1.0000 | 0.000484 | 0.000484 | 1.230e-09 | 24 | 24 |
| `model.layers.2.self_attn.k_proj` | 393472 | 0.000478 | 0.000478 | 1.0000 | 0.000478 | 0.000478 | 1.216e-09 | 25 | 25 |
| `model.layers.0.self_attn.k_proj` | 393472 | 0.000466 | 0.000466 | 1.0000 | 0.000466 | 0.000466 | 1.184e-09 | 26 | 26 |
| `model.layers.0.self_attn.o_proj` | 2359296 | 0.002686 | 0.002686 | 1.0000 | 0.002686 | 0.002686 | 1.138e-09 | 27 | 27 |
| `model.layers.24.self_attn.k_proj` | 393472 | 0.000417 | 0.000417 | 1.0000 | 0.000417 | 0.000417 | 1.060e-09 | 28 | 28 |
| `model.layers.11.self_attn.v_proj` | 393472 | 0.000383 | 0.000383 | 1.0000 | 0.000383 | 0.000383 | 9.731e-10 | 29 | 29 |
| `model.layers.26.self_attn.o_proj` | 2359296 | 0.002109 | 0.002109 | 1.0000 | 0.002109 | 0.002109 | 8.941e-10 | 30 | 30 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
