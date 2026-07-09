# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_7b_wikitext2pool512_n128_seed0_sensitivity_2to4_budget3.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_7b_wikitext2pool512_n128_seed1_sensitivity_2to4_budget3.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 2.9997 |
| budget used | 0.9999 |
| bit histogram | {'2': 103, '4': 94} |
| 2p 8-bit overlap | 86 |
| 8p 8-bit overlap | 86 |
| locked intersection modules | 80 |
| ranked additions | 14 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.27.self_attn.v_proj` | 1835520 | 0.003307 | 0.003250 | 0.9828 | 0.003364 | 0.003250 | 1.771e-09 | 1 | 1 |
| `model.layers.9.self_attn.v_proj` | 1835520 | 0.001989 | 0.001652 | 0.8307 | 0.001652 | 0.002326 | 9.000e-10 | 4 | 2 |
| `model.layers.26.self_attn.v_proj` | 1835520 | 0.001559 | 0.001362 | 0.8737 | 0.001362 | 0.001756 | 7.420e-10 | 5 | 3 |
| `model.layers.11.self_attn.v_proj` | 1835520 | 0.001532 | 0.001344 | 0.8770 | 0.001720 | 0.001344 | 7.320e-10 | 2 | 6 |
| `model.layers.5.self_attn.v_proj` | 1835520 | 0.001361 | 0.001038 | 0.7626 | 0.001684 | 0.001038 | 5.654e-10 | 3 | 10 |
| `model.layers.7.self_attn.v_proj` | 1835520 | 0.001173 | 0.000989 | 0.8429 | 0.000989 | 0.001358 | 5.389e-10 | 9 | 5 |
| `model.layers.24.self_attn.k_proj` | 1835520 | 0.001031 | 0.000978 | 0.9487 | 0.001084 | 0.000978 | 5.329e-10 | 8 | 11 |
| `model.layers.24.self_attn.v_proj` | 1835520 | 0.001105 | 0.000890 | 0.8059 | 0.000890 | 0.001319 | 4.850e-10 | 10 | 7 |
| `model.layers.15.self_attn.v_proj` | 1835520 | 0.000909 | 0.000873 | 0.9610 | 0.000873 | 0.000944 | 4.758e-10 | 11 | 12 |
| `model.layers.20.self_attn.v_proj` | 1835520 | 0.001060 | 0.000841 | 0.7937 | 0.000841 | 0.001278 | 4.581e-10 | 12 | 8 |
| `model.layers.12.self_attn.v_proj` | 1835520 | 0.000978 | 0.000803 | 0.8210 | 0.000803 | 0.001153 | 4.373e-10 | 13 | 9 |
| `model.layers.13.self_attn.k_proj` | 1835520 | 0.000718 | 0.000649 | 0.9045 | 0.000786 | 0.000649 | 3.536e-10 | 14 | 16 |
| `model.layers.6.self_attn.v_proj` | 1835520 | 0.001139 | 0.000545 | 0.4785 | 0.000545 | 0.001733 | 2.969e-10 | 16 | 4 |
| `model.layers.4.self_attn.k_proj` | 1835520 | 0.000656 | 0.000457 | 0.6974 | 0.000457 | 0.000854 | 2.492e-10 | 18 | 13 |
| `model.layers.8.self_attn.v_proj` | 1835520 | 0.000564 | 0.000410 | 0.7263 | 0.000410 | 0.000718 | 2.232e-10 | 19 | 15 |
| `model.layers.4.self_attn.v_proj` | 1835520 | 0.000568 | 0.000356 | 0.6261 | 0.000780 | 0.000356 | 1.937e-10 | 15 | 20 |
| `model.layers.26.mlp.down_proj` | 67895296 | 0.014515 | 0.012689 | 0.8742 | 0.012689 | 0.016341 | 1.869e-10 | 22 | 18 |
| `model.layers.12.self_attn.k_proj` | 1835520 | 0.000427 | 0.000336 | 0.7868 | 0.000518 | 0.000336 | 1.831e-10 | 17 | 21 |
| `model.layers.5.self_attn.k_proj` | 1835520 | 0.000353 | 0.000332 | 0.9417 | 0.000332 | 0.000373 | 1.811e-10 | 23 | 19 |
| `model.layers.6.self_attn.k_proj` | 1835520 | 0.000325 | 0.000259 | 0.7965 | 0.000391 | 0.000259 | 1.410e-10 | 20 | 24 |
| `lm_head` | 544997376 | 0.076325 | 0.076000 | 0.9957 | 0.076651 | 0.076000 | 1.394e-10 | 26 | 26 |
| `model.layers.3.self_attn.v_proj` | 1835520 | 0.000498 | 0.000256 | 0.5143 | 0.000256 | 0.000739 | 1.394e-10 | 27 | 14 |
| `model.layers.2.self_attn.v_proj` | 1835520 | 0.000405 | 0.000234 | 0.5779 | 0.000234 | 0.000575 | 1.274e-10 | 28 | 17 |
| `model.layers.19.self_attn.k_proj` | 1835520 | 0.000268 | 0.000212 | 0.7926 | 0.000323 | 0.000212 | 1.156e-10 | 24 | 30 |
| `model.layers.23.self_attn.v_proj` | 1835520 | 0.000220 | 0.000200 | 0.9091 | 0.000200 | 0.000240 | 1.091e-10 | 30 | 28 |
| `model.layers.26.self_attn.k_proj` | 1835520 | 0.000753 | 0.000186 | 0.2470 | 0.001319 | 0.000186 | 1.013e-10 | 6 | 32 |
| `model.layers.16.self_attn.k_proj` | 1835520 | 0.000207 | 0.000171 | 0.8247 | 0.000171 | 0.000243 | 9.291e-11 | 31 | 27 |
| `model.layers.14.self_attn.v_proj` | 1835520 | 0.000248 | 0.000162 | 0.6514 | 0.000162 | 0.000335 | 8.804e-11 | 32 | 22 |
| `model.layers.1.mlp.up_proj` | 67895296 | 0.004747 | 0.004641 | 0.9778 | 0.004852 | 0.004641 | 6.836e-11 | 34 | 35 |
| `model.layers.13.self_attn.v_proj` | 1835520 | 0.000658 | 0.000118 | 0.1792 | 0.001199 | 0.000118 | 6.428e-11 | 7 | 39 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
