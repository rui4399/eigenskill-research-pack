# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs/olmo2_0425_1b_loss_sensitive_alloc_4to8_limit2_group128_summary.json`
Right allocation: `outputs/olmo2_0425_1b_loss_sensitive_alloc_4to8_c4_limit2_group128_summary.json`

## Summary

| metric | value |
|---|---:|
| modules | 113 |
| average bits | 4.7475 |
| budget used | 0.9995 |
| bit histogram | {'8': 33, '4': 80} |
| 2p 8-bit overlap | 22 |
| 8p 8-bit overlap | 15 |
| locked intersection modules | 6 |
| ranked additions | 27 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | 2p delta | 8p delta | score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.11.self_attn.o_proj` | 4194304 | 0.006724 | 0.009849 | 0.003600 | 1.603e-09 | 1 | 10 |
| `model.layers.7.self_attn.o_proj` | 4194304 | 0.004759 | 0.005084 | 0.004435 | 1.135e-09 | 5 | 5 |
| `model.layers.13.self_attn.o_proj` | 4194304 | 0.004659 | 0.002826 | 0.006492 | 1.111e-09 | 18 | 3 |
| `model.layers.0.self_attn.v_proj` | 4194304 | 0.004280 | 0.000000 | 0.008561 | 1.021e-09 | 69 | 1 |
| `model.layers.12.self_attn.o_proj` | 4194304 | 0.004193 | 0.006464 | 0.001921 | 9.996e-10 | 3 | 16 |
| `model.layers.2.self_attn.o_proj` | 4194304 | 0.003602 | 0.006829 | 0.000375 | 8.587e-10 | 2 | 43 |
| `model.layers.8.self_attn.v_proj` | 4194304 | 0.003493 | 0.000266 | 0.006720 | 8.328e-10 | 65 | 2 |
| `model.layers.5.self_attn.q_proj` | 4194304 | 0.003168 | 0.000366 | 0.005971 | 7.554e-10 | 60 | 4 |
| `model.layers.9.self_attn.o_proj` | 4194304 | 0.003126 | 0.005595 | 0.000656 | 7.452e-10 | 4 | 37 |
| `model.layers.15.self_attn.v_proj` | 4194304 | 0.002977 | 0.002305 | 0.003650 | 7.098e-10 | 26 | 9 |
| `model.layers.0.self_attn.q_proj` | 4194304 | 0.002833 | 0.004368 | 0.001297 | 6.753e-10 | 9 | 23 |
| `model.layers.6.mlp.down_proj` | 16777216 | 0.010849 | 0.010601 | 0.011097 | 6.467e-10 | 21 | 13 |
| `model.layers.14.mlp.down_proj` | 16777216 | 0.010025 | 0.020051 | 0.000000 | 5.976e-10 | 6 | 112 |
| `model.layers.2.self_attn.v_proj` | 4194304 | 0.002422 | 0.004080 | 0.000763 | 5.774e-10 | 11 | 34 |
| `model.layers.15.self_attn.k_proj` | 4194304 | 0.002384 | 0.002412 | 0.002356 | 5.684e-10 | 24 | 14 |
| `model.layers.5.self_attn.o_proj` | 4194304 | 0.002320 | 0.004641 | 0.000000 | 5.532e-10 | 7 | 73 |
| `model.layers.7.self_attn.v_proj` | 4194304 | 0.002248 | 0.004496 | 0.000000 | 5.359e-10 | 8 | 81 |
| `model.layers.11.mlp.down_proj` | 16777216 | 0.008721 | 0.013808 | 0.003633 | 5.198e-10 | 14 | 28 |
| `model.layers.14.self_attn.v_proj` | 4194304 | 0.002136 | 0.000000 | 0.004272 | 5.092e-10 | 109 | 6 |
| `model.layers.7.self_attn.q_proj` | 4194304 | 0.002076 | 0.004153 | 0.000000 | 4.951e-10 | 10 | 80 |
| `model.layers.15.mlp.down_proj` | 16777216 | 0.008270 | 0.000000 | 0.016541 | 4.930e-10 | 113 | 7 |
| `model.layers.7.self_attn.k_proj` | 4194304 | 0.002050 | 0.003955 | 0.000144 | 4.887e-10 | 13 | 49 |
| `model.layers.12.self_attn.k_proj` | 4194304 | 0.002040 | 0.004079 | 0.000000 | 4.863e-10 | 12 | 103 |
| `model.layers.3.self_attn.k_proj` | 4194304 | 0.002002 | 0.001140 | 0.002865 | 4.774e-10 | 43 | 12 |
| `model.layers.3.self_attn.o_proj` | 4194304 | 0.001944 | 0.002799 | 0.001089 | 4.634e-10 | 19 | 25 |
| `model.layers.4.self_attn.o_proj` | 4194304 | 0.001942 | 0.000000 | 0.003885 | 4.631e-10 | 82 | 8 |
| `model.layers.5.mlp.gate_proj` | 16777216 | 0.006512 | 0.010122 | 0.002902 | 3.881e-10 | 22 | 35 |
| `model.layers.12.mlp.down_proj` | 16777216 | 0.006142 | 0.000000 | 0.012284 | 3.661e-10 | 105 | 11 |
| `model.layers.14.mlp.up_proj` | 16777216 | 0.006033 | 0.012066 | 0.000000 | 3.596e-10 | 15 | 111 |
| `model.layers.2.mlp.gate_proj` | 16777216 | 0.005900 | 0.011800 | 0.000000 | 3.517e-10 | 16 | 63 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
