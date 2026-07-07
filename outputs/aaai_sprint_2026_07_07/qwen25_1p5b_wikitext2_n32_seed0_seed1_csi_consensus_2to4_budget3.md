# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n32_seed0_alloc_2to4_budget3.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n32_seed1_alloc_2to4_budget3.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 2.9999 |
| budget used | 1.0000 |
| bit histogram | {'2': 108, '4': 89} |
| 2p 8-bit overlap | 79 |
| 8p 8-bit overlap | 80 |
| locked intersection modules | 71 |
| ranked additions | 18 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.v_proj` | 393472 | 0.006708 | 0.005170 | 0.7707 | 0.005170 | 0.008246 | 1.314e-08 | 1 | 1 |
| `model.layers.17.self_attn.v_proj` | 393472 | 0.001950 | 0.001887 | 0.9674 | 0.002014 | 0.001887 | 4.795e-09 | 3 | 2 |
| `model.layers.1.mlp.down_proj` | 13762560 | 0.051647 | 0.051163 | 0.9906 | 0.051163 | 0.052131 | 3.718e-09 | 8 | 7 |
| `model.layers.18.self_attn.v_proj` | 393472 | 0.001673 | 0.001402 | 0.8382 | 0.001944 | 0.001402 | 3.564e-09 | 4 | 8 |
| `model.layers.3.self_attn.v_proj` | 393472 | 0.001583 | 0.001285 | 0.8113 | 0.001285 | 0.001882 | 3.265e-09 | 11 | 3 |
| `model.layers.21.self_attn.v_proj` | 393472 | 0.001448 | 0.001279 | 0.8832 | 0.001279 | 0.001617 | 3.250e-09 | 12 | 6 |
| `model.layers.10.self_attn.v_proj` | 393472 | 0.001442 | 0.001230 | 0.8535 | 0.001230 | 0.001653 | 3.127e-09 | 13 | 5 |
| `model.layers.4.self_attn.v_proj` | 393472 | 0.001253 | 0.001216 | 0.9703 | 0.001290 | 0.001216 | 3.089e-09 | 10 | 11 |
| `model.layers.17.self_attn.k_proj` | 393472 | 0.001460 | 0.001213 | 0.8308 | 0.001213 | 0.001707 | 3.084e-09 | 14 | 4 |
| `model.layers.14.self_attn.k_proj` | 393472 | 0.001229 | 0.001059 | 0.8622 | 0.001059 | 0.001398 | 2.693e-09 | 15 | 9 |
| `model.layers.9.self_attn.v_proj` | 393472 | 0.001029 | 0.000968 | 0.9405 | 0.000968 | 0.001090 | 2.459e-09 | 16 | 12 |
| `model.layers.26.mlp.down_proj` | 13762560 | 0.032387 | 0.030754 | 0.9496 | 0.030754 | 0.034020 | 2.235e-09 | 18 | 14 |
| `model.layers.2.mlp.down_proj` | 13762560 | 0.029887 | 0.028850 | 0.9653 | 0.028850 | 0.030924 | 2.096e-09 | 21 | 17 |
| `model.layers.10.self_attn.k_proj` | 393472 | 0.000800 | 0.000706 | 0.8824 | 0.000894 | 0.000706 | 1.795e-09 | 17 | 18 |
| `model.layers.23.self_attn.k_proj` | 393472 | 0.001040 | 0.000644 | 0.6197 | 0.001436 | 0.000644 | 1.638e-09 | 9 | 19 |
| `model.layers.16.self_attn.v_proj` | 393472 | 0.000733 | 0.000589 | 0.8041 | 0.000877 | 0.000589 | 1.498e-09 | 19 | 22 |
| `model.layers.24.self_attn.v_proj` | 393472 | 0.000918 | 0.000503 | 0.5474 | 0.000503 | 0.001334 | 1.277e-09 | 23 | 10 |
| `model.layers.2.self_attn.k_proj` | 393472 | 0.000544 | 0.000494 | 0.9077 | 0.000494 | 0.000594 | 1.255e-09 | 24 | 20 |
| `model.layers.24.self_attn.k_proj` | 393472 | 0.000680 | 0.000491 | 0.7222 | 0.000870 | 0.000491 | 1.249e-09 | 20 | 25 |
| `model.layers.3.self_attn.k_proj` | 393472 | 0.000507 | 0.000452 | 0.8911 | 0.000452 | 0.000562 | 1.148e-09 | 27 | 23 |
| `model.layers.0.self_attn.o_proj` | 2359296 | 0.002570 | 0.002452 | 0.9541 | 0.002452 | 0.002688 | 1.039e-09 | 28 | 27 |
| `model.layers.1.self_attn.o_proj` | 2359296 | 0.003819 | 0.002109 | 0.5521 | 0.002109 | 0.005530 | 8.937e-10 | 29 | 15 |
| `model.layers.27.mlp.down_proj` | 13762560 | 0.011500 | 0.010543 | 0.9168 | 0.010543 | 0.012456 | 7.660e-10 | 30 | 30 |
| `model.layers.26.self_attn.k_proj` | 393472 | 0.000503 | 0.000286 | 0.5680 | 0.000721 | 0.000286 | 7.268e-10 | 22 | 33 |
| `model.layers.26.self_attn.o_proj` | 2359296 | 0.002224 | 0.001704 | 0.7663 | 0.001704 | 0.002743 | 7.223e-10 | 32 | 26 |
| `model.layers.22.self_attn.v_proj` | 393472 | 0.001535 | 0.000268 | 0.1743 | 0.002802 | 0.000268 | 6.800e-10 | 2 | 36 |
| `model.layers.19.self_attn.o_proj` | 2359296 | 0.001741 | 0.001552 | 0.8914 | 0.001552 | 0.001930 | 6.578e-10 | 33 | 31 |
| `model.layers.11.self_attn.k_proj` | 393472 | 0.000580 | 0.000259 | 0.4460 | 0.000259 | 0.000901 | 6.574e-10 | 34 | 16 |
| `model.layers.5.self_attn.o_proj` | 2359296 | 0.001513 | 0.001379 | 0.9113 | 0.001379 | 0.001647 | 5.845e-10 | 35 | 34 |
| `model.layers.25.self_attn.o_proj` | 2359296 | 0.001952 | 0.001336 | 0.6846 | 0.001336 | 0.002568 | 5.665e-10 | 37 | 28 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
