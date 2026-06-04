# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\qwen25_0p5b_loss_sensitive_alloc_4to8_limit2_group128_summary.json`
Right allocation: `outputs\qwen25_0p5b_loss_sensitive_alloc_4to8_limit8_group128_summary.json`

## Summary

| metric | value |
|---|---:|
| modules | 169 |
| average bits | 4.4997 |
| budget used | 0.9999 |
| bit histogram | {'4': 109, '8': 60} |
| 2p 8-bit overlap | 49 |
| 8p 8-bit overlap | 49 |
| locked intersection modules | 38 |
| ranked additions | 22 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | 2p delta | 8p delta | score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.16.self_attn.v_proj` | 114816 | 0.013645 | 0.018912 | 0.008378 | 1.188e-07 | 1 | 3 |
| `model.layers.3.self_attn.v_proj` | 114816 | 0.013584 | 0.015033 | 0.012135 | 1.183e-07 | 2 | 1 |
| `model.layers.8.self_attn.v_proj` | 114816 | 0.010387 | 0.010710 | 0.010064 | 9.047e-08 | 3 | 2 |
| `model.layers.6.self_attn.v_proj` | 114816 | 0.005939 | 0.006699 | 0.005180 | 5.173e-08 | 4 | 5 |
| `model.layers.2.self_attn.v_proj` | 114816 | 0.003810 | 0.003008 | 0.004612 | 3.318e-08 | 11 | 7 |
| `model.layers.17.self_attn.v_proj` | 114816 | 0.003578 | 0.004184 | 0.002972 | 3.116e-08 | 8 | 8 |
| `model.layers.19.self_attn.k_proj` | 114816 | 0.003478 | 0.004997 | 0.001958 | 3.029e-08 | 6 | 14 |
| `model.layers.19.self_attn.v_proj` | 114816 | 0.003109 | 0.003275 | 0.002944 | 2.708e-08 | 9 | 9 |
| `model.layers.11.self_attn.v_proj` | 114816 | 0.003073 | 0.000897 | 0.005249 | 2.676e-08 | 28 | 4 |
| `model.layers.20.self_attn.k_proj` | 114816 | 0.002962 | 0.004636 | 0.001288 | 2.580e-08 | 7 | 19 |
| `model.layers.0.self_attn.v_proj` | 114816 | 0.002610 | 0.005219 | 0.000000 | 2.273e-08 | 5 | 116 |
| `model.layers.2.mlp.down_proj` | 4358144 | 0.091151 | 0.099780 | 0.082522 | 2.092e-08 | 12 | 12 |
| `model.layers.12.self_attn.v_proj` | 114816 | 0.002328 | 0.000000 | 0.004656 | 2.028e-08 | 143 | 6 |
| `model.layers.10.self_attn.v_proj` | 114816 | 0.002327 | 0.003028 | 0.001627 | 2.027e-08 | 10 | 18 |
| `model.layers.9.self_attn.k_proj` | 114816 | 0.002265 | 0.001930 | 0.002599 | 1.973e-08 | 18 | 10 |
| `model.layers.10.self_attn.k_proj` | 114816 | 0.002152 | 0.002332 | 0.001971 | 1.874e-08 | 14 | 13 |
| `model.layers.8.self_attn.k_proj` | 114816 | 0.002125 | 0.002452 | 0.001797 | 1.851e-08 | 13 | 15 |
| `model.layers.22.self_attn.v_proj` | 114816 | 0.001980 | 0.001597 | 0.002363 | 1.724e-08 | 20 | 11 |
| `model.layers.2.self_attn.k_proj` | 114816 | 0.001583 | 0.001380 | 0.001786 | 1.378e-08 | 21 | 16 |
| `model.layers.23.self_attn.k_proj` | 114816 | 0.001515 | 0.001301 | 0.001729 | 1.320e-08 | 22 | 17 |
| `model.layers.6.self_attn.k_proj` | 114816 | 0.001297 | 0.001851 | 0.000743 | 1.129e-08 | 19 | 25 |
| `model.layers.4.self_attn.k_proj` | 114816 | 0.001275 | 0.002323 | 0.000226 | 1.110e-08 | 15 | 50 |
| `model.layers.13.self_attn.k_proj` | 114816 | 0.001173 | 0.002177 | 0.000168 | 1.021e-08 | 16 | 61 |
| `model.layers.2.self_attn.o_proj` | 802816 | 0.008022 | 0.013980 | 0.002063 | 9.992e-09 | 17 | 41 |
| `model.layers.21.mlp.down_proj` | 4358144 | 0.042108 | 0.044720 | 0.039495 | 9.662e-09 | 25 | 20 |
| `model.layers.23.self_attn.v_proj` | 114816 | 0.001042 | 0.001183 | 0.000901 | 9.075e-09 | 24 | 23 |
| `model.layers.22.self_attn.k_proj` | 114816 | 0.000799 | 0.001194 | 0.000404 | 6.958e-09 | 23 | 34 |
| `model.layers.1.self_attn.k_proj` | 114816 | 0.000710 | 0.000593 | 0.000827 | 6.186e-09 | 33 | 24 |
| `model.layers.22.self_attn.o_proj` | 802816 | 0.004791 | 0.005715 | 0.003867 | 5.968e-09 | 29 | 27 |
| `model.layers.10.self_attn.q_proj` | 803712 | 0.004462 | 0.006395 | 0.002529 | 5.551e-09 | 27 | 37 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
