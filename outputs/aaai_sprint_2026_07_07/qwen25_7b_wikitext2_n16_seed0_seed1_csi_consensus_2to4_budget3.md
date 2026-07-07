# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_7b_wikitext2_n16_seed0_alloc_2to4_budget3.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_7b_wikitext2_n16_seed1_alloc_2to4_budget3.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 2.9997 |
| budget used | 0.9999 |
| bit histogram | {'2': 115, '4': 82} |
| 2p 8-bit overlap | 69 |
| 8p 8-bit overlap | 73 |
| locked intersection modules | 64 |
| ranked additions | 18 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.27.self_attn.v_proj` | 1835520 | 0.004298 | 0.003131 | 0.7285 | 0.005465 | 0.003131 | 1.706e-09 | 1 | 1 |
| `model.layers.5.self_attn.v_proj` | 1835520 | 0.002777 | 0.002360 | 0.8498 | 0.003194 | 0.002360 | 1.286e-09 | 2 | 3 |
| `model.layers.26.self_attn.v_proj` | 1835520 | 0.001871 | 0.001500 | 0.8015 | 0.002243 | 0.001500 | 8.172e-10 | 3 | 6 |
| `model.layers.13.self_attn.v_proj` | 1835520 | 0.001721 | 0.001463 | 0.8498 | 0.001463 | 0.001980 | 7.969e-10 | 6 | 5 |
| `model.layers.24.self_attn.v_proj` | 1835520 | 0.001046 | 0.001027 | 0.9815 | 0.001027 | 0.001066 | 5.595e-10 | 9 | 9 |
| `model.layers.8.self_attn.v_proj` | 1835520 | 0.001374 | 0.000977 | 0.7106 | 0.001772 | 0.000977 | 5.320e-10 | 4 | 10 |
| `model.layers.20.self_attn.v_proj` | 1835520 | 0.001443 | 0.000763 | 0.5287 | 0.000763 | 0.002123 | 4.157e-10 | 12 | 4 |
| `model.layers.26.self_attn.k_proj` | 1835520 | 0.000797 | 0.000699 | 0.8763 | 0.000699 | 0.000896 | 3.807e-10 | 16 | 11 |
| `model.layers.11.self_attn.v_proj` | 1835520 | 0.001095 | 0.000658 | 0.6009 | 0.001533 | 0.000658 | 3.586e-10 | 5 | 15 |
| `model.layers.12.self_attn.k_proj` | 1835520 | 0.000795 | 0.000648 | 0.8141 | 0.000943 | 0.000648 | 3.528e-10 | 11 | 16 |
| `model.layers.16.self_attn.k_proj` | 1835520 | 0.000595 | 0.000514 | 0.8634 | 0.000514 | 0.000677 | 2.801e-10 | 19 | 14 |
| `model.layers.13.self_attn.k_proj` | 1835520 | 0.000681 | 0.000493 | 0.7241 | 0.000493 | 0.000869 | 2.687e-10 | 20 | 12 |
| `model.layers.8.self_attn.k_proj` | 1835520 | 0.000559 | 0.000491 | 0.8784 | 0.000627 | 0.000491 | 2.675e-10 | 17 | 20 |
| `model.layers.7.self_attn.v_proj` | 1835520 | 0.000720 | 0.000409 | 0.5680 | 0.001032 | 0.000409 | 2.229e-10 | 8 | 22 |
| `model.layers.26.mlp.down_proj` | 67895296 | 0.015867 | 0.015074 | 0.9500 | 0.015074 | 0.016660 | 2.220e-10 | 24 | 21 |
| `model.layers.15.self_attn.v_proj` | 1835520 | 0.000856 | 0.000314 | 0.3666 | 0.000314 | 0.001399 | 1.710e-10 | 28 | 7 |
| `model.layers.6.self_attn.v_proj` | 1835520 | 0.001328 | 0.000291 | 0.2191 | 0.000291 | 0.002366 | 1.586e-10 | 31 | 2 |
| `lm_head` | 544997376 | 0.093000 | 0.085384 | 0.9181 | 0.100616 | 0.085384 | 1.567e-10 | 27 | 24 |
| `model.layers.15.self_attn.o_proj` | 12845056 | 0.001887 | 0.001886 | 0.9990 | 0.001889 | 0.001886 | 1.468e-10 | 32 | 25 |
| `model.layers.0.self_attn.o_proj` | 12845056 | 0.002008 | 0.001414 | 0.7043 | 0.002601 | 0.001414 | 1.101e-10 | 25 | 27 |
| `model.layers.22.self_attn.q_proj` | 12848640 | 0.001408 | 0.001348 | 0.9569 | 0.001348 | 0.001469 | 1.049e-10 | 35 | 26 |
| `model.layers.14.self_attn.k_proj` | 1835520 | 0.000311 | 0.000173 | 0.5559 | 0.000449 | 0.000173 | 9.425e-11 | 23 | 29 |
| `model.layers.9.mlp.down_proj` | 67895296 | 0.005850 | 0.005481 | 0.9369 | 0.006220 | 0.005481 | 8.073e-11 | 37 | 35 |
| `model.layers.3.self_attn.o_proj` | 12845056 | 0.001285 | 0.000804 | 0.6254 | 0.001767 | 0.000804 | 6.259e-11 | 33 | 41 |
| `model.layers.4.self_attn.v_proj` | 1835520 | 0.000376 | 0.000111 | 0.2958 | 0.000111 | 0.000641 | 6.062e-11 | 42 | 17 |
| `model.layers.5.self_attn.q_proj` | 12848640 | 0.000911 | 0.000778 | 0.8548 | 0.000778 | 0.001043 | 6.058e-11 | 43 | 34 |
| `model.layers.19.self_attn.o_proj` | 12845056 | 0.000885 | 0.000742 | 0.8389 | 0.001027 | 0.000742 | 5.779e-11 | 39 | 42 |
| `model.layers.27.mlp.gate_proj` | 67895296 | 0.005135 | 0.003893 | 0.7583 | 0.003893 | 0.006376 | 5.735e-11 | 45 | 30 |
| `model.layers.26.mlp.up_proj` | 67895296 | 0.005088 | 0.003823 | 0.7515 | 0.003823 | 0.006352 | 5.631e-11 | 46 | 31 |
| `model.layers.20.self_attn.o_proj` | 12845056 | 0.000927 | 0.000670 | 0.7228 | 0.000670 | 0.001184 | 5.216e-11 | 47 | 32 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
