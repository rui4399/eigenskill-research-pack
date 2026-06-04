# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs/olmo2_0425_1b_loss_sensitive_alloc_4to8_limit2_group128_summary.json`
Right allocation: `outputs/olmo2_0425_1b_loss_sensitive_alloc_4to8_c4_limit2_group128_summary.json`

## Summary

| metric | value |
|---|---:|
| modules | 113 |
| average bits | 4.2492 |
| budget used | 0.9998 |
| bit histogram | {'8': 16, '4': 97} |
| 2p 8-bit overlap | 12 |
| 8p 8-bit overlap | 10 |
| locked intersection modules | 6 |
| ranked additions | 10 |

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
| `model.layers.2.self_attn.v_proj` | 4194304 | 0.002422 | 0.004080 | 0.000763 | 5.774e-10 | 11 | 34 |
| `model.layers.15.self_attn.k_proj` | 4194304 | 0.002384 | 0.002412 | 0.002356 | 5.684e-10 | 24 | 14 |
| `model.layers.5.self_attn.o_proj` | 4194304 | 0.002320 | 0.004641 | 0.000000 | 5.532e-10 | 7 | 73 |
| `model.layers.7.self_attn.v_proj` | 4194304 | 0.002248 | 0.004496 | 0.000000 | 5.359e-10 | 8 | 81 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
