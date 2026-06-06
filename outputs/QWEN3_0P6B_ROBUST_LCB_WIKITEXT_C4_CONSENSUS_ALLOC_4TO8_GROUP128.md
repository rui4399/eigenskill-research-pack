# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\qwen3_0p6b_loss_sensitive_alloc_4to8_limit4_group128_summary.json`
Right allocation: `outputs\qwen3_0p6b_c4_loss_sensitive_alloc_4to8_limit4_group128_summary.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 4.4997 |
| budget used | 0.9999 |
| bit histogram | {'4': 159, '8': 38} |
| 2p 8-bit overlap | 20 |
| 8p 8-bit overlap | 20 |
| locked intersection modules | 14 |
| ranked additions | 24 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.20.self_attn.q_proj` | 2097152 | 0.011903 | 0.010649 | 0.8947 | 0.010649 | 0.013157 | 5.078e-09 | 30 | 5 |
| `model.layers.16.self_attn.v_proj` | 1048576 | 0.008685 | 0.004749 | 0.5468 | 0.012621 | 0.004749 | 4.529e-09 | 11 | 9 |
| `model.layers.19.self_attn.k_proj` | 1048576 | 0.005304 | 0.004290 | 0.8088 | 0.006318 | 0.004290 | 4.091e-09 | 26 | 11 |
| `model.layers.12.self_attn.v_proj` | 1048576 | 0.004323 | 0.004096 | 0.9474 | 0.004096 | 0.004551 | 3.906e-09 | 39 | 10 |
| `model.layers.26.mlp.up_proj` | 3145728 | 0.026239 | 0.012153 | 0.4632 | 0.040325 | 0.012153 | 3.863e-09 | 8 | 13 |
| `model.layers.7.self_attn.v_proj` | 1048576 | 0.004481 | 0.003604 | 0.8042 | 0.005358 | 0.003604 | 3.437e-09 | 29 | 16 |
| `model.layers.26.mlp.down_proj` | 3145728 | 0.013497 | 0.009693 | 0.7182 | 0.017301 | 0.009693 | 3.081e-09 | 28 | 19 |
| `model.layers.15.self_attn.k_proj` | 1048576 | 0.003465 | 0.002950 | 0.8515 | 0.002950 | 0.003980 | 2.814e-09 | 51 | 14 |
| `model.layers.20.self_attn.k_proj` | 1048576 | 0.006289 | 0.002744 | 0.4363 | 0.009834 | 0.002744 | 2.617e-09 | 16 | 28 |
| `model.layers.24.self_attn.v_proj` | 1048576 | 0.003280 | 0.002684 | 0.8182 | 0.003876 | 0.002684 | 2.559e-09 | 44 | 29 |
| `model.layers.21.self_attn.k_proj` | 1048576 | 0.007388 | 0.002677 | 0.3624 | 0.012098 | 0.002677 | 2.553e-09 | 13 | 30 |
| `model.layers.4.self_attn.v_proj` | 1048576 | 0.010845 | 0.002664 | 0.2456 | 0.019027 | 0.002664 | 2.540e-09 | 4 | 31 |
| `model.layers.3.mlp.up_proj` | 3145728 | 0.012598 | 0.007879 | 0.6254 | 0.017317 | 0.007879 | 2.505e-09 | 27 | 33 |
| `model.layers.9.self_attn.k_proj` | 1048576 | 0.002667 | 0.002454 | 0.9204 | 0.002454 | 0.002879 | 2.341e-09 | 61 | 24 |
| `model.layers.2.self_attn.k_proj` | 1048576 | 0.003647 | 0.002239 | 0.6138 | 0.005056 | 0.002239 | 2.135e-09 | 32 | 39 |
| `model.layers.1.mlp.gate_proj` | 3145728 | 0.025899 | 0.006678 | 0.2578 | 0.045120 | 0.006678 | 2.123e-09 | 6 | 40 |
| `model.layers.16.self_attn.k_proj` | 1048576 | 0.004817 | 0.002142 | 0.4447 | 0.007492 | 0.002142 | 2.043e-09 | 21 | 41 |
| `model.layers.27.self_attn.k_proj` | 1048576 | 0.002448 | 0.001983 | 0.8101 | 0.001983 | 0.002913 | 1.891e-09 | 69 | 22 |
| `model.layers.23.mlp.up_proj` | 3145728 | 0.007353 | 0.005907 | 0.8033 | 0.005907 | 0.008799 | 1.878e-09 | 70 | 21 |
| `model.layers.3.self_attn.k_proj` | 1048576 | 0.002280 | 0.001882 | 0.8255 | 0.002678 | 0.001882 | 1.795e-09 | 54 | 47 |
| `model.layers.26.self_attn.k_proj` | 1048576 | 0.007012 | 0.001814 | 0.2588 | 0.012209 | 0.001814 | 1.730e-09 | 12 | 48 |
| `model.layers.10.mlp.down_proj` | 3145728 | 0.006634 | 0.005381 | 0.8112 | 0.007887 | 0.005381 | 1.711e-09 | 57 | 49 |
| `model.layers.22.self_attn.k_proj` | 1048576 | 0.002172 | 0.001701 | 0.7835 | 0.001701 | 0.002642 | 1.623e-09 | 74 | 32 |
| `model.layers.11.self_attn.o_proj` | 2097152 | 0.009008 | 0.002943 | 0.3267 | 0.015073 | 0.002943 | 1.403e-09 | 20 | 57 |
| `model.layers.12.mlp.down_proj` | 3145728 | 0.005701 | 0.004395 | 0.7709 | 0.007007 | 0.004395 | 1.397e-09 | 64 | 58 |
| `model.layers.2.self_attn.o_proj` | 2097152 | 0.008291 | 0.002863 | 0.3454 | 0.013719 | 0.002863 | 1.365e-09 | 25 | 61 |
| `model.layers.22.mlp.down_proj` | 3145728 | 0.005722 | 0.004159 | 0.7269 | 0.007285 | 0.004159 | 1.322e-09 | 63 | 63 |
| `model.layers.1.self_attn.q_proj` | 2097152 | 0.002728 | 0.002543 | 0.9321 | 0.002543 | 0.002914 | 1.213e-09 | 84 | 60 |
| `model.layers.26.mlp.gate_proj` | 3145728 | 0.021650 | 0.003684 | 0.1702 | 0.039616 | 0.003684 | 1.171e-09 | 9 | 68 |
| `model.layers.13.self_attn.q_proj` | 2097152 | 0.003283 | 0.002360 | 0.7190 | 0.004205 | 0.002360 | 1.126e-09 | 67 | 70 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
