# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs/qwen25_1p5b_baseline_allocations_4to8_limit8_group128_summary.json`
Right allocation: `outputs/qwen25_1p5b_baseline_allocations_4to8_limit8_group128_summary.json`
Policy: `mean_consensus`
Score key: `consensus_score_delta_per_cost`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 4.4993 |
| budget used | 0.9999 |
| bit histogram | {'8': 65, '4': 132} |
| 2p 8-bit overlap | 61 |
| 8p 8-bit overlap | 13 |
| locked intersection modules | 13 |
| ranked additions | 52 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | robust LCB | consistency | 2p delta | 8p delta | policy score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.v_proj` | 393472 | 0.019994 | 0.019994 | 1.0000 | 0.019994 | 0.019994 | 5.081e-08 | 1 | 1 |
| `model.layers.2.self_attn.v_proj` | 393472 | 0.007072 | 0.007072 | 1.0000 | 0.007072 | 0.007072 | 1.797e-08 | 2 | 2 |
| `model.layers.17.self_attn.v_proj` | 393472 | 0.005770 | 0.005770 | 1.0000 | 0.005770 | 0.005770 | 1.466e-08 | 3 | 3 |
| `model.layers.1.self_attn.v_proj` | 393472 | 0.004760 | 0.004760 | 1.0000 | 0.004760 | 0.004760 | 1.210e-08 | 4 | 4 |
| `model.layers.3.self_attn.v_proj` | 393472 | 0.003848 | 0.003848 | 1.0000 | 0.003848 | 0.003848 | 9.779e-09 | 5 | 5 |
| `model.layers.4.self_attn.k_proj` | 393472 | 0.003761 | 0.003761 | 1.0000 | 0.003761 | 0.003761 | 9.558e-09 | 6 | 6 |
| `model.layers.4.self_attn.v_proj` | 393472 | 0.003547 | 0.003547 | 1.0000 | 0.003547 | 0.003547 | 9.015e-09 | 7 | 7 |
| `model.layers.22.self_attn.v_proj` | 393472 | 0.003139 | 0.003139 | 1.0000 | 0.003139 | 0.003139 | 7.977e-09 | 8 | 8 |
| `model.layers.15.self_attn.v_proj` | 393472 | 0.002680 | 0.002680 | 1.0000 | 0.002680 | 0.002680 | 6.810e-09 | 9 | 9 |
| `model.layers.13.self_attn.k_proj` | 393472 | 0.002547 | 0.002547 | 1.0000 | 0.002547 | 0.002547 | 6.473e-09 | 10 | 10 |
| `model.layers.8.self_attn.v_proj` | 393472 | 0.002344 | 0.002344 | 1.0000 | 0.002344 | 0.002344 | 5.958e-09 | 11 | 11 |
| `model.layers.11.self_attn.v_proj` | 393472 | 0.001839 | 0.001839 | 1.0000 | 0.001839 | 0.001839 | 4.674e-09 | 12 | 12 |
| `model.layers.10.self_attn.v_proj` | 393472 | 0.001629 | 0.001629 | 1.0000 | 0.001629 | 0.001629 | 4.141e-09 | 13 | 13 |
| `model.layers.15.self_attn.k_proj` | 393472 | 0.001568 | 0.001568 | 1.0000 | 0.001568 | 0.001568 | 3.984e-09 | 14 | 14 |
| `model.layers.19.self_attn.k_proj` | 393472 | 0.001564 | 0.001564 | 1.0000 | 0.001564 | 0.001564 | 3.974e-09 | 15 | 15 |
| `model.layers.13.self_attn.v_proj` | 393472 | 0.001444 | 0.001444 | 1.0000 | 0.001444 | 0.001444 | 3.670e-09 | 16 | 16 |
| `model.layers.23.self_attn.k_proj` | 393472 | 0.001389 | 0.001389 | 1.0000 | 0.001389 | 0.001389 | 3.530e-09 | 17 | 17 |
| `model.layers.14.self_attn.k_proj` | 393472 | 0.001315 | 0.001315 | 1.0000 | 0.001315 | 0.001315 | 3.342e-09 | 18 | 18 |
| `model.layers.0.self_attn.o_proj` | 2359296 | 0.007883 | 0.007883 | 1.0000 | 0.007883 | 0.007883 | 3.341e-09 | 19 | 19 |
| `model.layers.24.self_attn.v_proj` | 393472 | 0.001128 | 0.001128 | 1.0000 | 0.001128 | 0.001128 | 2.867e-09 | 20 | 20 |
| `model.layers.18.self_attn.k_proj` | 393472 | 0.001065 | 0.001065 | 1.0000 | 0.001065 | 0.001065 | 2.708e-09 | 21 | 21 |
| `model.layers.17.self_attn.k_proj` | 393472 | 0.001039 | 0.001039 | 1.0000 | 0.001039 | 0.001039 | 2.640e-09 | 22 | 22 |
| `model.layers.24.self_attn.k_proj` | 393472 | 0.000924 | 0.000924 | 1.0000 | 0.000924 | 0.000924 | 2.348e-09 | 23 | 23 |
| `model.layers.6.self_attn.k_proj` | 393472 | 0.000875 | 0.000875 | 1.0000 | 0.000875 | 0.000875 | 2.224e-09 | 24 | 24 |
| `model.layers.26.mlp.down_proj` | 13762560 | 0.030113 | 0.030113 | 1.0000 | 0.030113 | 0.030113 | 2.188e-09 | 25 | 25 |
| `model.layers.21.self_attn.k_proj` | 393472 | 0.000803 | 0.000803 | 1.0000 | 0.000803 | 0.000803 | 2.040e-09 | 26 | 26 |
| `model.layers.2.mlp.down_proj` | 13762560 | 0.021759 | 0.021759 | 1.0000 | 0.021759 | 0.021759 | 1.581e-09 | 27 | 27 |
| `model.layers.1.mlp.down_proj` | 13762560 | 0.018669 | 0.018669 | 1.0000 | 0.018669 | 0.018669 | 1.357e-09 | 28 | 28 |
| `model.layers.26.self_attn.k_proj` | 393472 | 0.000534 | 0.000534 | 1.0000 | 0.000534 | 0.000534 | 1.356e-09 | 29 | 29 |
| `model.layers.12.self_attn.k_proj` | 393472 | 0.000524 | 0.000524 | 1.0000 | 0.000524 | 0.000524 | 1.332e-09 | 30 | 30 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
or robust lower-confidence loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
