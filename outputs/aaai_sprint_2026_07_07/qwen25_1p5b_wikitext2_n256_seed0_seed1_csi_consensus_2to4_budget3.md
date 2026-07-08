# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n256_seed0_alloc_2to4_budget3.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n256_seed1_alloc_2to4_budget3.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 2.9999 |
| budget used | 1.0000 |
| bit histogram | {'2': 98, '4': 99} |
| 2p 8-bit overlap | 95 |
| 8p 8-bit overlap | 92 |
| locked intersection modules | 88 |
| ranked additions | 11 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.v_proj` | 393472 | 0.006037 | 0.005686 | 0.9419 | 0.005686 | 0.006387 | 1.445e-08 | 1 | 1 |
| `model.layers.17.self_attn.v_proj` | 393472 | 0.002161 | 0.002136 | 0.9885 | 0.002136 | 0.002185 | 5.428e-09 | 4 | 2 |
| `model.layers.25.self_attn.v_proj` | 393472 | 0.002085 | 0.001851 | 0.8875 | 0.002320 | 0.001851 | 4.704e-09 | 3 | 4 |
| `model.layers.1.mlp.down_proj` | 13762560 | 0.061790 | 0.061353 | 0.9929 | 0.061353 | 0.062228 | 4.458e-09 | 6 | 5 |
| `model.layers.20.self_attn.v_proj` | 393472 | 0.001865 | 0.001752 | 0.9393 | 0.001752 | 0.001978 | 4.451e-09 | 7 | 3 |
| `model.layers.18.self_attn.v_proj` | 393472 | 0.001732 | 0.001625 | 0.9377 | 0.001840 | 0.001625 | 4.129e-09 | 5 | 6 |
| `model.layers.4.self_attn.v_proj` | 393472 | 0.001944 | 0.001341 | 0.6898 | 0.002548 | 0.001341 | 3.409e-09 | 2 | 9 |
| `model.layers.23.self_attn.v_proj` | 393472 | 0.001394 | 0.001303 | 0.9347 | 0.001303 | 0.001485 | 3.312e-09 | 10 | 7 |
| `model.layers.21.self_attn.v_proj` | 393472 | 0.001351 | 0.001289 | 0.9542 | 0.001289 | 0.001413 | 3.276e-09 | 11 | 8 |
| `model.layers.17.self_attn.k_proj` | 393472 | 0.001248 | 0.001230 | 0.9858 | 0.001266 | 0.001230 | 3.126e-09 | 12 | 11 |
| `model.layers.22.self_attn.v_proj` | 393472 | 0.001248 | 0.001158 | 0.9278 | 0.001158 | 0.001339 | 2.944e-09 | 14 | 10 |
| `model.layers.19.self_attn.v_proj` | 393472 | 0.001063 | 0.001026 | 0.9650 | 0.001026 | 0.001100 | 2.606e-09 | 15 | 13 |
| `model.layers.4.self_attn.k_proj` | 393472 | 0.001135 | 0.000960 | 0.8463 | 0.001309 | 0.000960 | 2.441e-09 | 8 | 17 |
| `model.layers.2.mlp.down_proj` | 13762560 | 0.034055 | 0.032432 | 0.9523 | 0.032432 | 0.035678 | 2.357e-09 | 17 | 14 |
| `model.layers.16.self_attn.v_proj` | 393472 | 0.000929 | 0.000925 | 0.9953 | 0.000934 | 0.000925 | 2.351e-09 | 16 | 18 |
| `model.layers.26.mlp.down_proj` | 13762560 | 0.033207 | 0.031192 | 0.9393 | 0.031192 | 0.035222 | 2.266e-09 | 18 | 15 |
| `model.layers.10.self_attn.v_proj` | 393472 | 0.001087 | 0.000864 | 0.7955 | 0.001309 | 0.000864 | 2.197e-09 | 9 | 20 |
| `model.layers.2.self_attn.k_proj` | 393472 | 0.000986 | 0.000861 | 0.8733 | 0.000861 | 0.001110 | 2.187e-09 | 19 | 12 |
| `model.layers.15.self_attn.v_proj` | 393472 | 0.001037 | 0.000818 | 0.7888 | 0.001256 | 0.000818 | 2.079e-09 | 13 | 21 |
| `model.layers.14.self_attn.k_proj` | 393472 | 0.000750 | 0.000734 | 0.9793 | 0.000734 | 0.000765 | 1.866e-09 | 23 | 23 |
| `model.layers.24.self_attn.v_proj` | 393472 | 0.000842 | 0.000708 | 0.8417 | 0.000708 | 0.000975 | 1.801e-09 | 24 | 16 |
| `model.layers.5.self_attn.k_proj` | 393472 | 0.000718 | 0.000661 | 0.9205 | 0.000661 | 0.000775 | 1.680e-09 | 25 | 22 |
| `model.layers.0.self_attn.o_proj` | 2359296 | 0.004164 | 0.003685 | 0.8851 | 0.004642 | 0.003685 | 1.562e-09 | 21 | 24 |
| `model.layers.1.self_attn.o_proj` | 2359296 | 0.004132 | 0.003509 | 0.8493 | 0.004754 | 0.003509 | 1.487e-09 | 20 | 25 |
| `model.layers.9.self_attn.v_proj` | 393472 | 0.000508 | 0.000465 | 0.9161 | 0.000550 | 0.000465 | 1.182e-09 | 26 | 27 |
| `model.layers.11.self_attn.v_proj` | 393472 | 0.000437 | 0.000418 | 0.9558 | 0.000456 | 0.000418 | 1.061e-09 | 28 | 28 |
| `model.layers.8.self_attn.v_proj` | 393472 | 0.000582 | 0.000406 | 0.6973 | 0.000759 | 0.000406 | 1.032e-09 | 22 | 29 |
| `model.layers.13.self_attn.k_proj` | 393472 | 0.000452 | 0.000405 | 0.8954 | 0.000405 | 0.000499 | 1.029e-09 | 29 | 26 |
| `model.layers.9.self_attn.k_proj` | 393472 | 0.000435 | 0.000344 | 0.7903 | 0.000526 | 0.000344 | 8.737e-10 | 27 | 33 |
| `model.layers.25.self_attn.o_proj` | 2359296 | 0.002108 | 0.001980 | 0.9394 | 0.001980 | 0.002236 | 8.393e-10 | 32 | 31 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
