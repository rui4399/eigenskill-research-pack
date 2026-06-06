# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\olmo2_0425_1b_loss_sensitive_alloc_4to8_limit2_group128_summary.json`
Right allocation: `outputs\olmo2_0425_1b_loss_sensitive_alloc_4to8_c4_limit2_group128_summary.json`
Policy: `robust_lcb`
Score key: `robust_lcb_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 113 |
| average bits | 4.4984 |
| budget used | 0.9996 |
| bit histogram | {'8': 20, '4': 93} |
| 2p 8-bit overlap | 10 |
| 8p 8-bit overlap | 10 |
| locked intersection modules | 6 |
| ranked additions | 14 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.7.self_attn.o_proj` | 4194304 | 0.004759 | 0.004435 | 0.9318 | 0.005084 | 0.004435 | 1.057e-09 | 5 | 5 |
| `model.layers.11.self_attn.o_proj` | 4194304 | 0.006724 | 0.003600 | 0.5353 | 0.009849 | 0.003600 | 8.583e-10 | 1 | 10 |
| `model.layers.13.self_attn.o_proj` | 4194304 | 0.004659 | 0.002826 | 0.6066 | 0.002826 | 0.006492 | 6.738e-10 | 18 | 3 |
| `model.layers.6.mlp.down_proj` | 16777216 | 0.010849 | 0.010601 | 0.9772 | 0.010601 | 0.011097 | 6.319e-10 | 21 | 13 |
| `model.layers.15.self_attn.k_proj` | 4194304 | 0.002384 | 0.002356 | 0.9881 | 0.002412 | 0.002356 | 5.616e-10 | 24 | 14 |
| `model.layers.15.self_attn.v_proj` | 4194304 | 0.002977 | 0.002305 | 0.7740 | 0.002305 | 0.003650 | 5.494e-10 | 26 | 9 |
| `model.layers.12.self_attn.o_proj` | 4194304 | 0.004193 | 0.001921 | 0.4583 | 0.006464 | 0.001921 | 4.581e-10 | 3 | 16 |
| `model.layers.13.self_attn.q_proj` | 4194304 | 0.001459 | 0.001440 | 0.9869 | 0.001440 | 0.001478 | 3.433e-10 | 36 | 21 |
| `model.layers.4.mlp.down_proj` | 16777216 | 0.005371 | 0.005315 | 0.9895 | 0.005428 | 0.005315 | 3.168e-10 | 39 | 22 |
| `model.layers.0.self_attn.q_proj` | 4194304 | 0.002833 | 0.001297 | 0.4580 | 0.004368 | 0.001297 | 3.093e-10 | 9 | 23 |
| `model.layers.3.self_attn.k_proj` | 4194304 | 0.002002 | 0.001140 | 0.5692 | 0.001140 | 0.002865 | 2.718e-10 | 43 | 12 |
| `model.layers.3.self_attn.o_proj` | 4194304 | 0.001944 | 0.001089 | 0.5600 | 0.002799 | 0.001089 | 2.595e-10 | 19 | 25 |
| `model.layers.3.mlp.up_proj` | 16777216 | 0.005771 | 0.003825 | 0.6629 | 0.007716 | 0.003825 | 2.280e-10 | 29 | 27 |
| `model.layers.11.mlp.down_proj` | 16777216 | 0.008721 | 0.003633 | 0.4166 | 0.013808 | 0.003633 | 2.166e-10 | 14 | 28 |
| `model.layers.8.self_attn.o_proj` | 4194304 | 0.001118 | 0.000853 | 0.7626 | 0.001383 | 0.000853 | 2.033e-10 | 38 | 30 |
| `model.layers.13.mlp.down_proj` | 16777216 | 0.004748 | 0.003397 | 0.7154 | 0.003397 | 0.006100 | 2.025e-10 | 51 | 20 |
| `model.layers.4.self_attn.q_proj` | 4194304 | 0.000848 | 0.000830 | 0.9792 | 0.000830 | 0.000865 | 1.979e-10 | 52 | 29 |
| `model.layers.2.self_attn.v_proj` | 4194304 | 0.002422 | 0.000763 | 0.3150 | 0.004080 | 0.000763 | 1.818e-10 | 11 | 34 |
| `model.layers.5.self_attn.k_proj` | 4194304 | 0.001251 | 0.000761 | 0.6085 | 0.000761 | 0.001741 | 1.815e-10 | 53 | 17 |
| `model.layers.5.mlp.gate_proj` | 16777216 | 0.006512 | 0.002902 | 0.4456 | 0.010122 | 0.002902 | 1.730e-10 | 22 | 35 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
