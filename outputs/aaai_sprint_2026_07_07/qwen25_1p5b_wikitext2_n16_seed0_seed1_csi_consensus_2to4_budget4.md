# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n16_seed0_alloc_2to4_budget4.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_1p5b_wikitext2_n16_seed1_alloc_2to4_budget4.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 4.0000 |
| budget used | 1.0000 |
| bit histogram | {'4': 197} |
| 2p 8-bit overlap | 134 |
| 8p 8-bit overlap | 124 |
| locked intersection modules | 99 |
| ranked additions | 98 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.3.self_attn.v_proj` | 393472 | 0.002567 | 0.002223 | 0.8661 | 0.002223 | 0.002911 | 5.651e-09 | 6 | 3 |
| `model.layers.4.self_attn.v_proj` | 393472 | 0.002568 | 0.001744 | 0.6790 | 0.003392 | 0.001744 | 4.432e-09 | 1 | 6 |
| `model.layers.22.self_attn.v_proj` | 393472 | 0.001722 | 0.001463 | 0.8492 | 0.001463 | 0.001982 | 3.717e-09 | 9 | 4 |
| `model.layers.21.self_attn.v_proj` | 393472 | 0.001802 | 0.001371 | 0.7610 | 0.002232 | 0.001371 | 3.485e-09 | 4 | 8 |
| `model.layers.16.self_attn.v_proj` | 393472 | 0.002149 | 0.001292 | 0.6011 | 0.001292 | 0.003006 | 3.283e-09 | 11 | 2 |
| `model.layers.17.self_attn.v_proj` | 393472 | 0.001591 | 0.001287 | 0.8093 | 0.001894 | 0.001287 | 3.272e-09 | 7 | 9 |
| `model.layers.18.self_attn.v_proj` | 393472 | 0.001829 | 0.001256 | 0.6867 | 0.002402 | 0.001256 | 3.193e-09 | 3 | 10 |
| `model.layers.1.mlp.down_proj` | 13762560 | 0.060289 | 0.042577 | 0.7062 | 0.078001 | 0.042577 | 3.094e-09 | 5 | 13 |
| `model.layers.24.self_attn.v_proj` | 393472 | 0.000961 | 0.000889 | 0.9247 | 0.000889 | 0.001033 | 2.258e-09 | 19 | 16 |
| `model.layers.15.self_attn.v_proj` | 393472 | 0.001271 | 0.000887 | 0.6982 | 0.000887 | 0.001654 | 2.254e-09 | 20 | 7 |
| `model.layers.25.self_attn.v_proj` | 393472 | 0.001040 | 0.000838 | 0.8058 | 0.000838 | 0.001242 | 2.129e-09 | 21 | 12 |
| `model.layers.26.mlp.down_proj` | 13762560 | 0.032516 | 0.026430 | 0.8128 | 0.026430 | 0.038602 | 1.920e-09 | 24 | 15 |
| `model.layers.2.mlp.down_proj` | 13762560 | 0.033105 | 0.024998 | 0.7551 | 0.024998 | 0.041212 | 1.816e-09 | 25 | 14 |
| `model.layers.10.self_attn.k_proj` | 393472 | 0.000891 | 0.000688 | 0.7722 | 0.001095 | 0.000688 | 1.749e-09 | 12 | 19 |
| `model.layers.14.self_attn.k_proj` | 393472 | 0.000835 | 0.000638 | 0.7641 | 0.001032 | 0.000638 | 1.621e-09 | 14 | 20 |
| `model.layers.9.self_attn.v_proj` | 393472 | 0.001027 | 0.000624 | 0.6078 | 0.001430 | 0.000624 | 1.587e-09 | 10 | 21 |
| `model.layers.8.self_attn.v_proj` | 393472 | 0.000727 | 0.000618 | 0.8506 | 0.000835 | 0.000618 | 1.571e-09 | 22 | 22 |
| `model.layers.27.self_attn.k_proj` | 393472 | 0.000738 | 0.000571 | 0.7746 | 0.000904 | 0.000571 | 1.452e-09 | 18 | 23 |
| `model.layers.2.self_attn.k_proj` | 393472 | 0.001557 | 0.000548 | 0.3516 | 0.002567 | 0.000548 | 1.392e-09 | 2 | 24 |
| `model.layers.15.self_attn.k_proj` | 393472 | 0.000511 | 0.000487 | 0.9517 | 0.000536 | 0.000487 | 1.237e-09 | 32 | 26 |
| `model.layers.0.self_attn.k_proj` | 393472 | 0.001100 | 0.000449 | 0.4086 | 0.000449 | 0.001750 | 1.142e-09 | 34 | 5 |
| `model.layers.26.self_attn.o_proj` | 2359296 | 0.002997 | 0.002682 | 0.8948 | 0.003313 | 0.002682 | 1.137e-09 | 31 | 29 |
| `model.layers.17.self_attn.k_proj` | 393472 | 0.000460 | 0.000421 | 0.9162 | 0.000498 | 0.000421 | 1.071e-09 | 33 | 32 |
| `model.layers.18.self_attn.o_proj` | 2359296 | 0.002688 | 0.002299 | 0.8552 | 0.002299 | 0.003078 | 9.744e-10 | 36 | 25 |
| `model.layers.27.mlp.down_proj` | 13762560 | 0.013676 | 0.012587 | 0.9204 | 0.012587 | 0.014766 | 9.146e-10 | 37 | 31 |
| `model.layers.25.self_attn.o_proj` | 2359296 | 0.001483 | 0.001447 | 0.9754 | 0.001520 | 0.001447 | 6.133e-10 | 42 | 43 |
| `model.layers.3.self_attn.k_proj` | 393472 | 0.000725 | 0.000204 | 0.2808 | 0.000204 | 0.001247 | 5.175e-10 | 48 | 11 |
| `model.layers.1.self_attn.o_proj` | 2359296 | 0.002788 | 0.000984 | 0.3528 | 0.000984 | 0.004593 | 4.170e-10 | 52 | 18 |
| `model.layers.6.self_attn.o_proj` | 2359296 | 0.001019 | 0.000944 | 0.9257 | 0.000944 | 0.001095 | 3.999e-10 | 54 | 48 |
| `model.layers.19.self_attn.k_proj` | 393472 | 0.000428 | 0.000154 | 0.3591 | 0.000703 | 0.000154 | 3.910e-10 | 26 | 50 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
