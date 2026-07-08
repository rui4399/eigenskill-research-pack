# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_7b_wikitext2_n64_seed0_alloc_3to4_budget3p5.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_7b_wikitext2_n64_seed1_alloc_3to4_budget3p5.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 3.4999 |
| budget used | 1.0000 |
| bit histogram | {'3': 103, '4': 94} |
| 2p 8-bit overlap | 86 |
| 8p 8-bit overlap | 84 |
| locked intersection modules | 80 |
| ranked additions | 14 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.27.self_attn.v_proj` | 1835520 | 0.003928 | 0.003626 | 0.9230 | 0.003626 | 0.004231 | 1.975e-09 | 1 | 1 |
| `model.layers.26.self_attn.v_proj` | 1835520 | 0.002276 | 0.002169 | 0.9533 | 0.002169 | 0.002382 | 1.182e-09 | 2 | 2 |
| `model.layers.13.self_attn.v_proj` | 1835520 | 0.001946 | 0.001626 | 0.8357 | 0.001626 | 0.002265 | 8.858e-10 | 4 | 3 |
| `model.layers.15.self_attn.v_proj` | 1835520 | 0.001335 | 0.001213 | 0.9082 | 0.001213 | 0.001458 | 6.607e-10 | 6 | 6 |
| `model.layers.6.self_attn.v_proj` | 1835520 | 0.001396 | 0.001152 | 0.8251 | 0.001640 | 0.001152 | 6.276e-10 | 3 | 9 |
| `model.layers.5.self_attn.v_proj` | 1835520 | 0.001211 | 0.001132 | 0.9344 | 0.001291 | 0.001132 | 6.167e-10 | 5 | 10 |
| `model.layers.11.self_attn.v_proj` | 1835520 | 0.001097 | 0.001089 | 0.9920 | 0.001089 | 0.001106 | 5.931e-10 | 7 | 11 |
| `model.layers.7.self_attn.v_proj` | 1835520 | 0.001145 | 0.001047 | 0.9144 | 0.001047 | 0.001243 | 5.702e-10 | 9 | 8 |
| `model.layers.24.self_attn.k_proj` | 1835520 | 0.001166 | 0.001008 | 0.8646 | 0.001008 | 0.001324 | 5.494e-10 | 10 | 7 |
| `model.layers.20.self_attn.v_proj` | 1835520 | 0.001027 | 0.000990 | 0.9635 | 0.001064 | 0.000990 | 5.391e-10 | 8 | 12 |
| `model.layers.24.self_attn.v_proj` | 1835520 | 0.000934 | 0.000912 | 0.9759 | 0.000957 | 0.000912 | 4.969e-10 | 11 | 13 |
| `model.layers.13.self_attn.k_proj` | 1835520 | 0.001172 | 0.000834 | 0.7113 | 0.000834 | 0.001510 | 4.541e-10 | 13 | 5 |
| `model.layers.6.self_attn.k_proj` | 1835520 | 0.000723 | 0.000677 | 0.9360 | 0.000677 | 0.000769 | 3.687e-10 | 15 | 15 |
| `model.layers.8.self_attn.v_proj` | 1835520 | 0.000643 | 0.000636 | 0.9886 | 0.000650 | 0.000636 | 3.463e-10 | 16 | 18 |
| `model.layers.14.self_attn.v_proj` | 1835520 | 0.001071 | 0.000630 | 0.5888 | 0.000630 | 0.001511 | 3.435e-10 | 17 | 4 |
| `model.layers.26.self_attn.k_proj` | 1835520 | 0.000575 | 0.000492 | 0.8561 | 0.000492 | 0.000658 | 2.682e-10 | 18 | 17 |
| `model.layers.3.self_attn.k_proj` | 1835520 | 0.000475 | 0.000419 | 0.8826 | 0.000419 | 0.000531 | 2.285e-10 | 20 | 19 |
| `model.layers.26.mlp.down_proj` | 67895296 | 0.015594 | 0.014008 | 0.8983 | 0.014008 | 0.017180 | 2.063e-10 | 21 | 21 |
| `lm_head` | 544997376 | 0.083366 | 0.081905 | 0.9825 | 0.081905 | 0.084827 | 1.503e-10 | 23 | 26 |
| `model.layers.10.self_attn.k_proj` | 1835520 | 0.000370 | 0.000276 | 0.7448 | 0.000464 | 0.000276 | 1.501e-10 | 19 | 27 |
| `model.layers.19.self_attn.k_proj` | 1835520 | 0.000300 | 0.000252 | 0.8415 | 0.000252 | 0.000347 | 1.375e-10 | 24 | 23 |
| `model.layers.19.self_attn.o_proj` | 12845056 | 0.001898 | 0.001664 | 0.8764 | 0.001664 | 0.002133 | 1.295e-10 | 25 | 24 |
| `model.layers.25.self_attn.k_proj` | 1835520 | 0.000263 | 0.000227 | 0.8615 | 0.000227 | 0.000300 | 1.235e-10 | 26 | 25 |
| `model.layers.3.self_attn.v_proj` | 1835520 | 0.000483 | 0.000185 | 0.3832 | 0.000185 | 0.000781 | 1.008e-10 | 29 | 14 |
| `model.layers.16.self_attn.k_proj` | 1835520 | 0.000289 | 0.000174 | 0.6007 | 0.000174 | 0.000405 | 9.465e-11 | 30 | 22 |
| `model.layers.2.self_attn.v_proj` | 1835520 | 0.000158 | 0.000149 | 0.9478 | 0.000166 | 0.000149 | 8.134e-11 | 31 | 33 |
| `model.layers.3.self_attn.o_proj` | 12845056 | 0.001083 | 0.001020 | 0.9422 | 0.001145 | 0.001020 | 7.943e-11 | 32 | 34 |
| `model.layers.8.self_attn.k_proj` | 1835520 | 0.000299 | 0.000109 | 0.3660 | 0.000109 | 0.000488 | 5.955e-11 | 36 | 20 |
| `model.layers.27.mlp.gate_proj` | 67895296 | 0.003805 | 0.003721 | 0.9780 | 0.003889 | 0.003721 | 5.481e-11 | 37 | 40 |
| `model.layers.27.mlp.up_proj` | 67895296 | 0.003869 | 0.003469 | 0.8966 | 0.003469 | 0.004269 | 5.110e-11 | 39 | 37 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
