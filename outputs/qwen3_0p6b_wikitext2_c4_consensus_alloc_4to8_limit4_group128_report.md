# Consensus Loss-Sensitive Allocation

Left allocation: `outputs/qwen3_0p6b_module_loss_sensitivity_limit4_group128.json`
Right allocation: `outputs/qwen3_0p6b_c4_module_loss_sensitivity_limit4_group128.json`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 4.4997 |
| budget used | 0.9999 |
| bit histogram | {"4": 151, "8": 46} |
| locked intersection modules | 14 |
| ranked additions | 32 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | left delta | right delta | score/cost | left rank | right rank |
|---|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.v_proj` | 1048576 | 0.012516 | 0.000000 | 0.025032 | 1.194e-08 | 112 | 1 |
| `model.layers.20.self_attn.v_proj` | 1048576 | 0.011920 | 0.023840 | 0.000000 | 1.137e-08 | 1 | 180 |
| `model.layers.21.self_attn.v_proj` | 1048576 | 0.011560 | 0.022708 | 0.000413 | 1.102e-08 | 2 | 101 |
| `model.layers.4.self_attn.v_proj` | 1048576 | 0.010845 | 0.019027 | 0.002664 | 1.034e-08 | 4 | 31 |
| `model.layers.18.self_attn.v_proj` | 1048576 | 0.009597 | 0.019195 | 0.000000 | 9.153e-09 | 3 | 177 |
| `model.layers.26.mlp.up_proj` | 3145728 | 0.026239 | 0.040325 | 0.012153 | 8.341e-09 | 8 | 13 |
| `model.layers.16.self_attn.v_proj` | 1048576 | 0.008685 | 0.012621 | 0.004749 | 8.283e-09 | 11 | 9 |
| `model.layers.1.mlp.gate_proj` | 3145728 | 0.025899 | 0.045120 | 0.006678 | 8.233e-09 | 6 | 40 |
| `model.layers.10.self_attn.k_proj` | 1048576 | 0.008196 | 0.016393 | 0.000000 | 7.817e-09 | 5 | 154 |
| `model.layers.21.self_attn.k_proj` | 1048576 | 0.007388 | 0.012098 | 0.002677 | 7.045e-09 | 13 | 30 |
| `model.layers.17.self_attn.v_proj` | 1048576 | 0.007258 | 0.014515 | 0.000000 | 6.921e-09 | 7 | 174 |
| `model.layers.26.mlp.gate_proj` | 3145728 | 0.021650 | 0.039616 | 0.003684 | 6.882e-09 | 9 | 68 |
| `model.layers.26.self_attn.k_proj` | 1048576 | 0.007012 | 0.012209 | 0.001814 | 6.687e-09 | 12 | 48 |
| `model.layers.2.self_attn.v_proj` | 1048576 | 0.006906 | 0.000000 | 0.013811 | 6.586e-09 | 118 | 2 |
| `model.layers.23.self_attn.k_proj` | 1048576 | 0.006823 | 0.013164 | 0.000482 | 6.507e-09 | 10 | 94 |
| `model.layers.20.self_attn.k_proj` | 1048576 | 0.006289 | 0.009834 | 0.002744 | 5.998e-09 | 16 | 28 |
| `model.layers.20.self_attn.q_proj` | 2097152 | 0.011903 | 0.010649 | 0.013157 | 5.676e-09 | 30 | 5 |
| `model.layers.2.mlp.up_proj` | 3145728 | 0.017001 | 0.033632 | 0.000369 | 5.404e-09 | 14 | 124 |
| `model.layers.19.self_attn.k_proj` | 1048576 | 0.005304 | 0.006318 | 0.004290 | 5.058e-09 | 26 | 11 |
| `model.layers.1.self_attn.v_proj` | 1048576 | 0.005156 | 0.010312 | 0.000000 | 4.917e-09 | 15 | 131 |
| `model.layers.16.self_attn.k_proj` | 1048576 | 0.004817 | 0.007492 | 0.002142 | 4.594e-09 | 21 | 41 |
| `model.layers.2.mlp.down_proj` | 3145728 | 0.013716 | 0.000000 | 0.027432 | 4.360e-09 | 120 | 3 |
| `model.layers.11.self_attn.o_proj` | 2097152 | 0.009008 | 0.015073 | 0.002943 | 4.295e-09 | 20 | 57 |
| `model.layers.26.mlp.down_proj` | 3145728 | 0.013497 | 0.017301 | 0.009693 | 4.291e-09 | 28 | 19 |
| `model.layers.7.self_attn.v_proj` | 1048576 | 0.004481 | 0.005358 | 0.003604 | 4.273e-09 | 29 | 16 |
| `model.layers.12.self_attn.v_proj` | 1048576 | 0.004323 | 0.004096 | 0.004551 | 4.123e-09 | 39 | 10 |
| `model.layers.3.mlp.up_proj` | 3145728 | 0.012598 | 0.017317 | 0.007879 | 4.005e-09 | 27 | 33 |
| `model.layers.0.mlp.up_proj` | 3145728 | 0.012501 | 0.023861 | 0.001142 | 3.974e-09 | 18 | 104 |
| `model.layers.2.self_attn.o_proj` | 2097152 | 0.008291 | 0.013719 | 0.002863 | 3.953e-09 | 25 | 61 |
| `model.layers.4.self_attn.k_proj` | 1048576 | 0.004108 | 0.008215 | 0.000000 | 3.917e-09 | 17 | 137 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
loss-per-cost score. It should be read together with downstream PPL
evaluation because stable allocation decisions can still trade off quality.
