# Qwen Consensus Loss-Sensitive Allocation

Left allocation: `outputs\qwen25_1p5b_loss_sensitive_alloc_4to8_limit2_group128_summary.json`
Right allocation: `outputs\qwen25_1p5b_loss_sensitive_alloc_4to8_limit8_group128_summary.json`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| average bits | 4.4993 |
| budget used | 0.9999 |
| bit histogram | {'4': 132, '8': 65} |
| 2p 8-bit overlap | 57 |
| 8p 8-bit overlap | 55 |
| locked intersection modules | 47 |
| ranked additions | 18 |

## Top Consensus 8-bit Modules

| module | params | avg delta NLL | 2p delta | 8p delta | score/cost | 2p rank | 8p rank |
|---|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.v_proj` | 393472 | 0.026230 | 0.032466 | 0.019994 | 6.666e-08 | 1 | 1 |
| `model.layers.2.self_attn.v_proj` | 393472 | 0.011540 | 0.016008 | 0.007072 | 2.933e-08 | 2 | 2 |
| `model.layers.3.self_attn.v_proj` | 393472 | 0.006488 | 0.009128 | 0.003848 | 1.649e-08 | 3 | 5 |
| `model.layers.17.self_attn.v_proj` | 393472 | 0.006004 | 0.006238 | 0.005770 | 1.526e-08 | 4 | 3 |
| `model.layers.1.self_attn.v_proj` | 393472 | 0.003816 | 0.002873 | 0.004760 | 9.699e-09 | 10 | 4 |
| `model.layers.11.self_attn.v_proj` | 393472 | 0.003672 | 0.005505 | 0.001839 | 9.333e-09 | 5 | 12 |
| `model.layers.22.self_attn.v_proj` | 393472 | 0.002980 | 0.002821 | 0.003139 | 7.574e-09 | 12 | 8 |
| `model.layers.7.self_attn.v_proj` | 393472 | 0.002602 | 0.004792 | 0.000412 | 6.612e-09 | 6 | 36 |
| `model.layers.13.self_attn.k_proj` | 393472 | 0.002519 | 0.002491 | 0.002547 | 6.402e-09 | 14 | 10 |
| `model.layers.8.self_attn.v_proj` | 393472 | 0.002407 | 0.002470 | 0.002344 | 6.117e-09 | 15 | 11 |
| `model.layers.6.self_attn.k_proj` | 393472 | 0.002348 | 0.003820 | 0.000875 | 5.966e-09 | 7 | 24 |
| `model.layers.10.self_attn.v_proj` | 393472 | 0.002175 | 0.002720 | 0.001629 | 5.527e-09 | 13 | 13 |
| `model.layers.15.self_attn.v_proj` | 393472 | 0.001983 | 0.001285 | 0.002680 | 5.039e-09 | 22 | 9 |
| `model.layers.21.self_attn.k_proj` | 393472 | 0.001886 | 0.002970 | 0.000803 | 4.794e-09 | 8 | 26 |
| `model.layers.4.self_attn.k_proj` | 393472 | 0.001880 | 0.000000 | 0.003761 | 4.779e-09 | 140 | 6 |
| `model.layers.4.self_attn.v_proj` | 393472 | 0.001774 | 0.000000 | 0.003547 | 4.507e-09 | 141 | 7 |
| `model.layers.13.self_attn.v_proj` | 393472 | 0.001711 | 0.001978 | 0.001444 | 4.348e-09 | 18 | 16 |
| `model.layers.22.self_attn.k_proj` | 393472 | 0.001660 | 0.002927 | 0.000393 | 4.219e-09 | 9 | 39 |
| `model.layers.14.self_attn.k_proj` | 393472 | 0.001637 | 0.001960 | 0.001315 | 4.162e-09 | 19 | 18 |
| `model.layers.24.self_attn.v_proj` | 393472 | 0.001578 | 0.002027 | 0.001128 | 4.010e-09 | 17 | 20 |
| `model.layers.12.self_attn.v_proj` | 393472 | 0.001429 | 0.002858 | 0.000000 | 3.632e-09 | 11 | 164 |
| `model.layers.17.self_attn.k_proj` | 393472 | 0.001336 | 0.001633 | 0.001039 | 3.395e-09 | 20 | 22 |
| `model.layers.15.self_attn.k_proj` | 393472 | 0.001296 | 0.001025 | 0.001568 | 3.294e-09 | 28 | 14 |
| `model.layers.16.self_attn.k_proj` | 393472 | 0.001259 | 0.002047 | 0.000470 | 3.199e-09 | 16 | 32 |
| `model.layers.19.self_attn.k_proj` | 393472 | 0.001215 | 0.000867 | 0.001564 | 3.089e-09 | 33 | 15 |
| `model.layers.26.mlp.down_proj` | 13762560 | 0.038560 | 0.047007 | 0.030113 | 2.802e-09 | 21 | 25 |
| `model.layers.24.self_attn.k_proj` | 393472 | 0.001034 | 0.001145 | 0.000924 | 2.628e-09 | 25 | 23 |
| `model.layers.18.self_attn.k_proj` | 393472 | 0.000948 | 0.000831 | 0.001065 | 2.409e-09 | 34 | 21 |
| `model.layers.23.self_attn.k_proj` | 393472 | 0.000839 | 0.000289 | 0.001389 | 2.132e-09 | 62 | 17 |
| `model.layers.2.mlp.down_proj` | 13762560 | 0.028250 | 0.034742 | 0.021759 | 2.053e-09 | 29 | 27 |

## Interpretation

This allocation is a stability-oriented policy: it prioritizes modules that
both calibration probes selected, then fills unused budget by average
loss-per-cost score. It should be read together with the downstream PPL
evaluation because stable allocation decisions can still trade off quality.
