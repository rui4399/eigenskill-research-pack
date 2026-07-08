# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\phi3_mini_wikitext2_n64_seed0_sensitivity_2to4_budget3.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\phi3_mini_wikitext2_n64_seed1_sensitivity_2to4_budget3.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 129 |
| average bits | 2.9977 |
| budget used | 0.9992 |
| bit histogram | {'2': 63, '4': 66} |
| 2p 8-bit overlap | 62 |
| 8p 8-bit overlap | 64 |
| locked intersection modules | 60 |
| ranked additions | 6 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `lm_head` | 98500608 | 5.065385 | 5.043504 | 0.9957 | 5.021623 | 5.109147 | 5.120e-08 | 1 | 1 |
| `model.layers.31.mlp.down_proj` | 25165824 | 0.901948 | 0.897615 | 0.9952 | 0.893282 | 0.910613 | 3.567e-08 | 2 | 2 |
| `model.layers.31.mlp.gate_up_proj` | 50331648 | 0.526994 | 0.526650 | 0.9993 | 0.526306 | 0.527681 | 1.046e-08 | 3 | 3 |
| `model.layers.31.self_attn.o_proj` | 9437184 | 0.075857 | 0.073953 | 0.9749 | 0.079664 | 0.072050 | 7.836e-09 | 4 | 4 |
| `model.layers.30.self_attn.o_proj` | 9437184 | 0.040417 | 0.039742 | 0.9833 | 0.039067 | 0.041766 | 4.211e-09 | 7 | 5 |
| `model.layers.30.mlp.gate_up_proj` | 50331648 | 0.209213 | 0.207915 | 0.9938 | 0.211808 | 0.206618 | 4.131e-09 | 6 | 6 |
| `model.layers.29.mlp.down_proj` | 25165824 | 0.103805 | 0.102595 | 0.9883 | 0.106224 | 0.101386 | 4.077e-09 | 5 | 7 |
| `model.layers.30.mlp.down_proj` | 25165824 | 0.088446 | 0.088205 | 0.9973 | 0.088928 | 0.087964 | 3.505e-09 | 9 | 8 |
| `model.layers.2.mlp.down_proj` | 25165824 | 0.089076 | 0.086606 | 0.9723 | 0.094014 | 0.084137 | 3.441e-09 | 8 | 9 |
| `model.layers.29.mlp.gate_up_proj` | 50331648 | 0.167102 | 0.164905 | 0.9869 | 0.171495 | 0.162709 | 3.276e-09 | 10 | 10 |
| `model.layers.29.self_attn.o_proj` | 9437184 | 0.029916 | 0.029688 | 0.9924 | 0.030372 | 0.029460 | 3.146e-09 | 11 | 11 |
| `model.layers.4.mlp.down_proj` | 25165824 | 0.070185 | 0.068302 | 0.9732 | 0.073951 | 0.066418 | 2.714e-09 | 13 | 12 |
| `model.layers.7.self_attn.o_proj` | 9437184 | 0.025571 | 0.024380 | 0.9534 | 0.027953 | 0.023189 | 2.583e-09 | 12 | 14 |
| `model.layers.25.mlp.down_proj` | 25165824 | 0.065189 | 0.064174 | 0.9844 | 0.067219 | 0.063159 | 2.550e-09 | 14 | 13 |
| `model.layers.2.self_attn.o_proj` | 9437184 | 0.022176 | 0.021420 | 0.9659 | 0.023686 | 0.020665 | 2.270e-09 | 16 | 16 |
| `model.layers.7.mlp.down_proj` | 25165824 | 0.056737 | 0.055479 | 0.9778 | 0.054222 | 0.059252 | 2.205e-09 | 18 | 15 |
| `model.layers.30.self_attn.qkv_proj` | 28311552 | 0.058391 | 0.057278 | 0.9809 | 0.060616 | 0.056165 | 2.023e-09 | 19 | 17 |
| `model.layers.10.self_attn.o_proj` | 9437184 | 0.020750 | 0.018788 | 0.9054 | 0.024676 | 0.016825 | 1.991e-09 | 15 | 25 |
| `model.layers.1.self_attn.qkv_proj` | 28311552 | 0.057068 | 0.055835 | 0.9784 | 0.059534 | 0.054602 | 1.972e-09 | 21 | 20 |
| `model.layers.27.mlp.down_proj` | 25165824 | 0.049700 | 0.049198 | 0.9899 | 0.050706 | 0.048695 | 1.955e-09 | 23 | 19 |
| `model.layers.10.self_attn.qkv_proj` | 28311552 | 0.055903 | 0.055100 | 0.9856 | 0.057509 | 0.054297 | 1.946e-09 | 22 | 21 |
| `model.layers.3.mlp.down_proj` | 25165824 | 0.050411 | 0.048976 | 0.9715 | 0.053282 | 0.047540 | 1.946e-09 | 20 | 22 |
| `model.layers.21.mlp.down_proj` | 25165824 | 0.049087 | 0.048932 | 0.9968 | 0.048776 | 0.049399 | 1.944e-09 | 25 | 18 |
| `model.layers.28.mlp.gate_up_proj` | 50331648 | 0.095913 | 0.095023 | 0.9907 | 0.097693 | 0.094133 | 1.888e-09 | 24 | 23 |
| `model.layers.9.self_attn.o_proj` | 9437184 | 0.019113 | 0.017813 | 0.9320 | 0.021713 | 0.016513 | 1.888e-09 | 17 | 26 |
| `model.layers.7.mlp.gate_up_proj` | 50331648 | 0.089659 | 0.088611 | 0.9883 | 0.091755 | 0.087563 | 1.761e-09 | 29 | 27 |
| `model.layers.6.mlp.down_proj` | 25165824 | 0.044813 | 0.044253 | 0.9875 | 0.045931 | 0.043694 | 1.758e-09 | 27 | 28 |
| `model.layers.1.mlp.down_proj` | 25165824 | 0.044134 | 0.043576 | 0.9873 | 0.043017 | 0.045251 | 1.732e-09 | 31 | 24 |
| `model.layers.22.mlp.down_proj` | 25165824 | 0.043886 | 0.042887 | 0.9772 | 0.045884 | 0.041889 | 1.704e-09 | 28 | 32 |
| `model.layers.20.self_attn.o_proj` | 9437184 | 0.016472 | 0.015941 | 0.9678 | 0.017534 | 0.015411 | 1.689e-09 | 26 | 34 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
