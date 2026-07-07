# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\aaai_sprint_2026_07_07\qwen25_3b_wikitext2_n64_seed0_alloc_3to4_budget3p5.json`
Right allocation: `outputs\aaai_sprint_2026_07_07\qwen25_3b_wikitext2_n64_seed1_alloc_3to4_budget3p5.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 253 |
| average bits | 3.5000 |
| budget used | 1.0000 |
| bit histogram | {'4': 124, '3': 129} |
| 2p 8-bit overlap | 113 |
| 8p 8-bit overlap | 111 |
| locked intersection modules | 103 |
| ranked additions | 21 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.v_proj` | 524544 | 0.003918 | 0.003828 | 0.9770 | 0.003828 | 0.004009 | 7.298e-09 | 2 | 2 |
| `model.layers.1.mlp.gate_proj` | 22544384 | 0.170506 | 0.152363 | 0.8936 | 0.188649 | 0.152363 | 6.758e-09 | 1 | 3 |
| `model.layers.25.self_attn.v_proj` | 524544 | 0.003635 | 0.003169 | 0.8718 | 0.003169 | 0.004101 | 6.042e-09 | 3 | 1 |
| `model.layers.4.self_attn.v_proj` | 524544 | 0.001958 | 0.001953 | 0.9977 | 0.001962 | 0.001953 | 3.724e-09 | 4 | 5 |
| `model.layers.32.self_attn.k_proj` | 524544 | 0.001866 | 0.001818 | 0.9743 | 0.001914 | 0.001818 | 3.467e-09 | 5 | 6 |
| `model.layers.33.self_attn.v_proj` | 524544 | 0.001843 | 0.001702 | 0.9237 | 0.001702 | 0.001983 | 3.245e-09 | 6 | 4 |
| `model.layers.30.mlp.down_proj` | 22544384 | 0.063127 | 0.061981 | 0.9819 | 0.064272 | 0.061981 | 2.749e-09 | 8 | 10 |
| `model.layers.27.self_attn.v_proj` | 524544 | 0.001495 | 0.001268 | 0.8481 | 0.001268 | 0.001722 | 2.417e-09 | 11 | 7 |
| `model.layers.12.self_attn.v_proj` | 524544 | 0.001372 | 0.001225 | 0.8927 | 0.001225 | 0.001519 | 2.334e-09 | 12 | 9 |
| `model.layers.0.self_attn.k_proj` | 524544 | 0.001240 | 0.001204 | 0.9715 | 0.001275 | 0.001204 | 2.296e-09 | 10 | 14 |
| `model.layers.18.self_attn.v_proj` | 524544 | 0.001161 | 0.001088 | 0.9376 | 0.001088 | 0.001233 | 2.075e-09 | 14 | 12 |
| `model.layers.29.self_attn.v_proj` | 524544 | 0.001141 | 0.001056 | 0.9253 | 0.001056 | 0.001226 | 2.013e-09 | 15 | 13 |
| `model.layers.8.self_attn.k_proj` | 524544 | 0.001362 | 0.001052 | 0.7722 | 0.001052 | 0.001673 | 2.006e-09 | 16 | 8 |
| `model.layers.33.self_attn.k_proj` | 524544 | 0.001246 | 0.000972 | 0.7805 | 0.001519 | 0.000972 | 1.854e-09 | 7 | 16 |
| `model.layers.13.self_attn.k_proj` | 524544 | 0.001132 | 0.000958 | 0.8459 | 0.000958 | 0.001307 | 1.826e-09 | 19 | 11 |
| `model.layers.2.mlp.down_proj` | 22544384 | 0.040957 | 0.035914 | 0.8769 | 0.035914 | 0.046001 | 1.593e-09 | 20 | 15 |
| `model.layers.23.self_attn.v_proj` | 524544 | 0.001083 | 0.000772 | 0.7125 | 0.001395 | 0.000772 | 1.471e-09 | 9 | 18 |
| `model.layers.10.self_attn.v_proj` | 524544 | 0.000872 | 0.000764 | 0.8765 | 0.000979 | 0.000764 | 1.456e-09 | 18 | 19 |
| `model.layers.5.self_attn.k_proj` | 524544 | 0.000678 | 0.000643 | 0.9475 | 0.000643 | 0.000714 | 1.225e-09 | 24 | 20 |
| `model.layers.30.self_attn.k_proj` | 524544 | 0.000602 | 0.000571 | 0.9489 | 0.000633 | 0.000571 | 1.089e-09 | 25 | 21 |
| `model.layers.6.self_attn.v_proj` | 524544 | 0.000671 | 0.000571 | 0.8510 | 0.000771 | 0.000571 | 1.088e-09 | 21 | 22 |
| `model.layers.28.self_attn.v_proj` | 524544 | 0.000552 | 0.000537 | 0.9733 | 0.000567 | 0.000537 | 1.024e-09 | 26 | 24 |
| `model.layers.27.self_attn.k_proj` | 524544 | 0.000570 | 0.000465 | 0.8162 | 0.000675 | 0.000465 | 8.868e-10 | 22 | 26 |
| `model.layers.16.self_attn.v_proj` | 524544 | 0.000685 | 0.000372 | 0.5429 | 0.000999 | 0.000372 | 7.093e-10 | 17 | 29 |
| `model.layers.2.self_attn.v_proj` | 524544 | 0.000374 | 0.000347 | 0.9284 | 0.000347 | 0.000401 | 6.623e-10 | 29 | 28 |
| `model.layers.35.self_attn.v_proj` | 524544 | 0.000447 | 0.000336 | 0.7499 | 0.000336 | 0.000559 | 6.397e-10 | 31 | 23 |
| `model.layers.16.self_attn.k_proj` | 524544 | 0.000327 | 0.000317 | 0.9688 | 0.000337 | 0.000317 | 6.041e-10 | 30 | 32 |
| `model.layers.1.self_attn.o_proj` | 4194304 | 0.002832 | 0.002353 | 0.8311 | 0.003310 | 0.002353 | 5.611e-10 | 27 | 34 |
| `model.layers.0.self_attn.o_proj` | 4194304 | 0.002793 | 0.002153 | 0.7709 | 0.002153 | 0.003434 | 5.134e-10 | 34 | 27 |
| `model.layers.2.self_attn.k_proj` | 524544 | 0.000287 | 0.000265 | 0.9239 | 0.000265 | 0.000309 | 5.059e-10 | 35 | 33 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
