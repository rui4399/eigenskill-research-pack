# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_mixed1024_n512_seed0_sensitivity_2to4_budget3.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_mixed1024_n512_seed1_sensitivity_2to4_budget3.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 2.9999 |
| budget used | 1.0000 |
| bit histogram | {'4': 103, '2': 94} |
| 2p 8-bit overlap | 96 |
| 8p 8-bit overlap | 97 |
| locked intersection modules | 91 |
| ranked additions | 12 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.v_proj` | 393472 | 0.003929 | 0.003787 | 0.9637 | 0.003787 | 0.004072 | 9.624e-09 | 1 | 1 |
| `model.layers.1.mlp.down_proj` | 13762560 | 0.069498 | 0.067338 | 0.9689 | 0.071658 | 0.067338 | 4.893e-09 | 2 | 2 |
| `model.layers.25.self_attn.v_proj` | 393472 | 0.001820 | 0.001777 | 0.9767 | 0.001777 | 0.001862 | 4.517e-09 | 3 | 3 |
| `model.layers.18.self_attn.v_proj` | 393472 | 0.001328 | 0.001305 | 0.9826 | 0.001351 | 0.001305 | 3.316e-09 | 5 | 5 |
| `model.layers.21.self_attn.v_proj` | 393472 | 0.001303 | 0.001259 | 0.9668 | 0.001346 | 0.001259 | 3.200e-09 | 6 | 7 |
| `model.layers.19.self_attn.v_proj` | 393472 | 0.001326 | 0.001150 | 0.8672 | 0.001502 | 0.001150 | 2.923e-09 | 4 | 9 |
| `model.layers.26.mlp.down_proj` | 13762560 | 0.039582 | 0.038836 | 0.9812 | 0.038836 | 0.040327 | 2.822e-09 | 8 | 8 |
| `model.layers.20.self_attn.v_proj` | 393472 | 0.001265 | 0.001100 | 0.8700 | 0.001100 | 0.001429 | 2.797e-09 | 9 | 4 |
| `model.layers.11.self_attn.v_proj` | 393472 | 0.001125 | 0.001068 | 0.9493 | 0.001182 | 0.001068 | 2.714e-09 | 7 | 10 |
| `model.layers.17.self_attn.v_proj` | 393472 | 0.001058 | 0.001022 | 0.9656 | 0.001095 | 0.001022 | 2.597e-09 | 10 | 11 |
| `model.layers.23.self_attn.v_proj` | 393472 | 0.001128 | 0.000978 | 0.8666 | 0.000978 | 0.001279 | 2.484e-09 | 11 | 6 |
| `model.layers.2.mlp.down_proj` | 13762560 | 0.033983 | 0.033759 | 0.9934 | 0.033759 | 0.034206 | 2.453e-09 | 12 | 13 |
| `model.layers.10.self_attn.v_proj` | 393472 | 0.000876 | 0.000762 | 0.8694 | 0.000762 | 0.000990 | 1.935e-09 | 15 | 12 |
| `model.layers.24.self_attn.v_proj` | 393472 | 0.000825 | 0.000738 | 0.8940 | 0.000912 | 0.000738 | 1.874e-09 | 13 | 15 |
| `model.layers.17.self_attn.k_proj` | 393472 | 0.000755 | 0.000726 | 0.9623 | 0.000783 | 0.000726 | 1.846e-09 | 14 | 16 |
| `model.layers.22.self_attn.v_proj` | 393472 | 0.000711 | 0.000678 | 0.9536 | 0.000678 | 0.000744 | 1.724e-09 | 16 | 14 |
| `model.layers.16.self_attn.v_proj` | 393472 | 0.000651 | 0.000640 | 0.9844 | 0.000661 | 0.000640 | 1.627e-09 | 18 | 18 |
| `model.layers.4.self_attn.v_proj` | 393472 | 0.000644 | 0.000624 | 0.9686 | 0.000624 | 0.000665 | 1.586e-09 | 19 | 17 |
| `model.layers.4.self_attn.k_proj` | 393472 | 0.000614 | 0.000557 | 0.9065 | 0.000672 | 0.000557 | 1.415e-09 | 17 | 20 |
| `model.layers.8.self_attn.v_proj` | 393472 | 0.000517 | 0.000494 | 0.9544 | 0.000494 | 0.000541 | 1.255e-09 | 20 | 21 |
| `model.layers.1.self_attn.o_proj` | 2359296 | 0.002707 | 0.002532 | 0.9353 | 0.002532 | 0.002882 | 1.073e-09 | 22 | 24 |
| `model.layers.2.self_attn.k_proj` | 393472 | 0.000502 | 0.000393 | 0.7815 | 0.000393 | 0.000612 | 9.979e-10 | 24 | 19 |
| `model.layers.14.self_attn.k_proj` | 393472 | 0.000402 | 0.000388 | 0.9657 | 0.000416 | 0.000388 | 9.873e-10 | 23 | 30 |
| `model.layers.15.self_attn.v_proj` | 393472 | 0.000412 | 0.000365 | 0.8847 | 0.000365 | 0.000460 | 9.270e-10 | 25 | 27 |
| `model.layers.0.self_attn.o_proj` | 2359296 | 0.002557 | 0.002161 | 0.8451 | 0.002161 | 0.002953 | 9.160e-10 | 26 | 23 |
| `model.layers.7.self_attn.v_proj` | 393472 | 0.000407 | 0.000338 | 0.8302 | 0.000338 | 0.000476 | 8.587e-10 | 27 | 25 |
| `model.layers.5.self_attn.k_proj` | 393472 | 0.000398 | 0.000323 | 0.8128 | 0.000323 | 0.000472 | 8.220e-10 | 28 | 26 |
| `model.layers.23.self_attn.k_proj` | 393472 | 0.000399 | 0.000305 | 0.7638 | 0.000494 | 0.000305 | 7.749e-10 | 21 | 32 |
| `model.layers.20.self_attn.k_proj` | 393472 | 0.000348 | 0.000271 | 0.7772 | 0.000271 | 0.000426 | 6.880e-10 | 31 | 28 |
| `model.layers.25.self_attn.o_proj` | 2359296 | 0.001501 | 0.001462 | 0.9739 | 0.001462 | 0.001540 | 6.195e-10 | 32 | 34 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
