# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_c4_n64_seed0_alloc_2to4_budget3.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_c4_n64_seed1_alloc_2to4_budget3.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 2.9999 |
| budget used | 1.0000 |
| bit histogram | {'4': 103, '2': 94} |
| 2p 8-bit overlap | 91 |
| 8p 8-bit overlap | 95 |
| locked intersection modules | 85 |
| ranked additions | 18 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.v_proj` | 393472 | 0.002649 | 0.002087 | 0.7879 | 0.002087 | 0.003212 | 5.305e-09 | 1 | 1 |
| `model.layers.1.mlp.down_proj` | 13762560 | 0.059488 | 0.054895 | 0.9228 | 0.054895 | 0.064081 | 3.989e-09 | 5 | 4 |
| `model.layers.21.self_attn.v_proj` | 393472 | 0.001916 | 0.001458 | 0.7609 | 0.001458 | 0.002375 | 3.706e-09 | 7 | 2 |
| `model.layers.25.self_attn.v_proj` | 393472 | 0.001489 | 0.001427 | 0.9583 | 0.001551 | 0.001427 | 3.627e-09 | 6 | 6 |
| `model.layers.11.self_attn.v_proj` | 393472 | 0.001720 | 0.001363 | 0.7922 | 0.001363 | 0.002078 | 3.464e-09 | 8 | 3 |
| `model.layers.23.self_attn.v_proj` | 393472 | 0.001720 | 0.001355 | 0.7877 | 0.002085 | 0.001355 | 3.443e-09 | 2 | 7 |
| `model.layers.20.self_attn.v_proj` | 393472 | 0.001467 | 0.001346 | 0.9180 | 0.001587 | 0.001346 | 3.422e-09 | 4 | 8 |
| `model.layers.3.self_attn.v_proj` | 393472 | 0.001388 | 0.001202 | 0.8656 | 0.001202 | 0.001575 | 3.054e-09 | 10 | 5 |
| `model.layers.3.self_attn.k_proj` | 393472 | 0.001248 | 0.001140 | 0.9136 | 0.001355 | 0.001140 | 2.897e-09 | 9 | 11 |
| `model.layers.26.mlp.down_proj` | 13762560 | 0.039112 | 0.034604 | 0.8847 | 0.034604 | 0.043621 | 2.514e-09 | 11 | 9 |
| `model.layers.15.self_attn.v_proj` | 393472 | 0.001049 | 0.000989 | 0.9428 | 0.000989 | 0.001109 | 2.513e-09 | 12 | 12 |
| `model.layers.2.mlp.down_proj` | 13762560 | 0.032118 | 0.030468 | 0.9486 | 0.030468 | 0.033769 | 2.214e-09 | 14 | 14 |
| `model.layers.4.self_attn.k_proj` | 393472 | 0.000852 | 0.000840 | 0.9856 | 0.000865 | 0.000840 | 2.135e-09 | 15 | 15 |
| `model.layers.7.self_attn.k_proj` | 393472 | 0.000912 | 0.000839 | 0.9192 | 0.000839 | 0.000986 | 2.131e-09 | 16 | 13 |
| `model.layers.19.self_attn.v_proj` | 393472 | 0.000814 | 0.000793 | 0.9750 | 0.000793 | 0.000834 | 2.016e-09 | 17 | 16 |
| `model.layers.22.self_attn.v_proj` | 393472 | 0.001232 | 0.000792 | 0.6427 | 0.001672 | 0.000792 | 2.012e-09 | 3 | 17 |
| `model.layers.14.self_attn.v_proj` | 393472 | 0.000732 | 0.000702 | 0.9577 | 0.000763 | 0.000702 | 1.783e-09 | 18 | 19 |
| `model.layers.8.self_attn.v_proj` | 393472 | 0.000801 | 0.000698 | 0.8712 | 0.000904 | 0.000698 | 1.773e-09 | 13 | 20 |
| `model.layers.5.self_attn.v_proj` | 393472 | 0.000862 | 0.000574 | 0.6656 | 0.000574 | 0.001151 | 1.459e-09 | 20 | 10 |
| `model.layers.1.self_attn.o_proj` | 2359296 | 0.003410 | 0.003317 | 0.9727 | 0.003317 | 0.003502 | 1.406e-09 | 21 | 22 |
| `model.layers.18.self_attn.v_proj` | 393472 | 0.000506 | 0.000504 | 0.9952 | 0.000504 | 0.000509 | 1.280e-09 | 22 | 23 |
| `model.layers.16.self_attn.v_proj` | 393472 | 0.000542 | 0.000437 | 0.8052 | 0.000648 | 0.000437 | 1.110e-09 | 19 | 26 |
| `model.layers.26.mlp.up_proj` | 13762560 | 0.011836 | 0.011444 | 0.9669 | 0.012228 | 0.011444 | 8.315e-10 | 28 | 30 |
| `model.layers.0.self_attn.k_proj` | 393472 | 0.000455 | 0.000325 | 0.7140 | 0.000325 | 0.000585 | 8.249e-10 | 29 | 21 |
| `model.layers.24.self_attn.v_proj` | 393472 | 0.000522 | 0.000309 | 0.5917 | 0.000309 | 0.000735 | 7.844e-10 | 30 | 18 |
| `model.layers.8.self_attn.k_proj` | 393472 | 0.000381 | 0.000293 | 0.7694 | 0.000293 | 0.000469 | 7.456e-10 | 31 | 24 |
| `model.layers.17.self_attn.k_proj` | 393472 | 0.000302 | 0.000291 | 0.9644 | 0.000291 | 0.000313 | 7.400e-10 | 32 | 31 |
| `model.layers.1.self_attn.v_proj` | 393472 | 0.000370 | 0.000289 | 0.7805 | 0.000289 | 0.000452 | 7.347e-10 | 33 | 25 |
| `model.layers.18.self_attn.k_proj` | 393472 | 0.000324 | 0.000286 | 0.8841 | 0.000361 | 0.000286 | 7.278e-10 | 27 | 34 |
| `model.layers.9.self_attn.k_proj` | 393472 | 0.000286 | 0.000271 | 0.9477 | 0.000271 | 0.000301 | 6.880e-10 | 35 | 32 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
