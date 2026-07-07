# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_7b_wikitext2_n32_seed0_sensitivity_2to4_budget3.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_7b_wikitext2_n32_seed1_sensitivity_2to4_budget3.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 2.9997 |
| budget used | 0.9999 |
| bit histogram | {'2': 115, '4': 82} |
| 2p 8-bit overlap | 70 |
| 8p 8-bit overlap | 72 |
| locked intersection modules | 63 |
| ranked additions | 19 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.27.self_attn.v_proj` | 1835520 | 0.003269 | 0.002850 | 0.8718 | 0.002850 | 0.003688 | 1.553e-09 | 1 | 1 |
| `model.layers.6.self_attn.v_proj` | 1835520 | 0.001991 | 0.001894 | 0.9512 | 0.001894 | 0.002088 | 1.032e-09 | 2 | 3 |
| `model.layers.5.self_attn.v_proj` | 1835520 | 0.001578 | 0.001508 | 0.9557 | 0.001648 | 0.001508 | 8.218e-10 | 4 | 6 |
| `model.layers.26.self_attn.v_proj` | 1835520 | 0.001689 | 0.001494 | 0.8849 | 0.001883 | 0.001494 | 8.142e-10 | 3 | 7 |
| `model.layers.13.self_attn.v_proj` | 1835520 | 0.001534 | 0.001468 | 0.9570 | 0.001468 | 0.001600 | 7.997e-10 | 6 | 5 |
| `model.layers.8.self_attn.v_proj` | 1835520 | 0.001233 | 0.001193 | 0.9675 | 0.001273 | 0.001193 | 6.500e-10 | 7 | 9 |
| `model.layers.24.self_attn.k_proj` | 1835520 | 0.001438 | 0.001167 | 0.8115 | 0.001167 | 0.001708 | 6.356e-10 | 8 | 4 |
| `model.layers.24.self_attn.v_proj` | 1835520 | 0.001330 | 0.001099 | 0.8263 | 0.001561 | 0.001099 | 5.988e-10 | 5 | 11 |
| `model.layers.13.self_attn.k_proj` | 1835520 | 0.000926 | 0.000777 | 0.8392 | 0.001075 | 0.000777 | 4.233e-10 | 10 | 15 |
| `model.layers.7.self_attn.v_proj` | 1835520 | 0.000893 | 0.000757 | 0.8481 | 0.000757 | 0.001028 | 4.125e-10 | 12 | 12 |
| `model.layers.11.self_attn.v_proj` | 1835520 | 0.000817 | 0.000542 | 0.6634 | 0.001092 | 0.000542 | 2.953e-10 | 9 | 19 |
| `model.layers.20.self_attn.v_proj` | 1835520 | 0.000763 | 0.000525 | 0.6877 | 0.000525 | 0.001001 | 2.859e-10 | 15 | 13 |
| `model.layers.15.self_attn.v_proj` | 1835520 | 0.001327 | 0.000488 | 0.3678 | 0.000488 | 0.002167 | 2.660e-10 | 16 | 2 |
| `model.layers.6.self_attn.k_proj` | 1835520 | 0.000646 | 0.000484 | 0.7486 | 0.000484 | 0.000809 | 2.635e-10 | 17 | 14 |
| `model.layers.19.self_attn.o_proj` | 12845056 | 0.002423 | 0.002083 | 0.8596 | 0.002083 | 0.002763 | 1.622e-10 | 20 | 22 |
| `model.layers.12.self_attn.k_proj` | 1835520 | 0.000314 | 0.000288 | 0.9175 | 0.000288 | 0.000340 | 1.571e-10 | 21 | 23 |
| `lm_head` | 544997376 | 0.082783 | 0.081331 | 0.9825 | 0.084234 | 0.081331 | 1.492e-10 | 22 | 27 |
| `model.layers.26.mlp.down_proj` | 67895296 | 0.012622 | 0.008727 | 0.6914 | 0.008727 | 0.016517 | 1.285e-10 | 23 | 21 |
| `model.layers.26.mlp.up_proj` | 67895296 | 0.004314 | 0.004125 | 0.9562 | 0.004503 | 0.004125 | 6.075e-11 | 30 | 37 |
| `model.layers.27.mlp.gate_proj` | 67895296 | 0.004094 | 0.003621 | 0.8844 | 0.003621 | 0.004568 | 5.333e-11 | 32 | 34 |
| `model.layers.9.mlp.down_proj` | 67895296 | 0.004284 | 0.003478 | 0.8118 | 0.005090 | 0.003478 | 5.122e-11 | 28 | 39 |
| `model.layers.11.self_attn.o_proj` | 12845056 | 0.001114 | 0.000627 | 0.5625 | 0.000627 | 0.001602 | 4.880e-11 | 35 | 30 |
| `model.layers.20.self_attn.o_proj` | 12845056 | 0.000807 | 0.000613 | 0.7601 | 0.001000 | 0.000613 | 4.774e-11 | 27 | 44 |
| `model.layers.10.mlp.gate_proj` | 67895296 | 0.003229 | 0.003105 | 0.9618 | 0.003352 | 0.003105 | 4.574e-11 | 34 | 46 |
| `model.layers.27.mlp.up_proj` | 67895296 | 0.003632 | 0.003067 | 0.8444 | 0.003067 | 0.004197 | 4.517e-11 | 38 | 36 |
| `model.layers.10.self_attn.k_proj` | 1835520 | 0.000310 | 0.000083 | 0.2672 | 0.000536 | 0.000083 | 4.507e-11 | 14 | 48 |
| `model.layers.10.self_attn.o_proj` | 12845056 | 0.000697 | 0.000577 | 0.8280 | 0.000577 | 0.000817 | 4.494e-11 | 39 | 35 |
| `model.layers.9.self_attn.v_proj` | 1835520 | 0.000426 | 0.000082 | 0.1924 | 0.000082 | 0.000771 | 4.469e-11 | 40 | 16 |
| `model.layers.23.self_attn.k_proj` | 1835520 | 0.000136 | 0.000074 | 0.5448 | 0.000197 | 0.000074 | 4.025e-11 | 24 | 50 |
| `model.layers.1.mlp.up_proj` | 67895296 | 0.002607 | 0.002575 | 0.9874 | 0.002575 | 0.002640 | 3.792e-11 | 44 | 51 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
