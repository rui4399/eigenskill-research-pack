# Sensitivity Compact Summary

Source: `outputs\qwen25_1p5b_module_loss_sensitivity_limit8_group128.json`
Allocation: `outputs\qwen25_1p5b_loss_sensitive_alloc_4to8_limit8_group128_summary.json`
Method: `loss_sensitive_4to8`

## Overview

| metric | value |
|---|---:|
| modules | 197 |
| selected 8-bit modules | 61 |
| selected positive delta ratio | 0.5445 |

## Category Histogram

| category | all modules | selected 8-bit |
|---|---:|---:|
| attn.k_proj | 28 | 17 |
| attn.o_proj | 28 | 9 |
| attn.q_proj | 28 | 8 |
| attn.v_proj | 28 | 17 |
| lm_head | 1 | 0 |
| mlp.down_proj | 28 | 5 |
| mlp.gate_proj | 28 | 2 |
| mlp.up_proj | 28 | 3 |

## Top Absolute Positive Delta

| rank | bits | module | category | params | delta NLL | delta/param |
|---:|---:|---|---|---:|---:|---:|
| 73 | 4 | `lm_head` | lm_head | 233373696 | 0.087258 | 3.739e-10 |
| 25 | 8 | `model.layers.26.mlp.down_proj` | mlp.down_proj | 13762560 | 0.030113 | 2.188e-09 |
| 27 | 8 | `model.layers.2.mlp.down_proj` | mlp.down_proj | 13762560 | 0.021759 | 1.581e-09 |
| 1 | 8 | `model.layers.0.self_attn.v_proj` | attn.v_proj | 393472 | 0.019994 | 5.081e-08 |
| 28 | 8 | `model.layers.1.mlp.down_proj` | mlp.down_proj | 13762560 | 0.018669 | 1.357e-09 |
| 31 | 8 | `model.layers.27.mlp.down_proj` | mlp.down_proj | 13762560 | 0.016632 | 1.208e-09 |
| 33 | 8 | `model.layers.3.mlp.down_proj` | mlp.down_proj | 13762560 | 0.015931 | 1.158e-09 |
| 35 | 8 | `model.layers.2.mlp.gate_proj` | mlp.gate_proj | 13762560 | 0.014477 | 1.052e-09 |
| 38 | 8 | `model.layers.3.mlp.up_proj` | mlp.up_proj | 13762560 | 0.013873 | 1.008e-09 |
| 42 | 8 | `model.layers.2.mlp.up_proj` | mlp.up_proj | 13762560 | 0.011403 | 8.286e-10 |
| 57 | 8 | `model.layers.1.mlp.up_proj` | mlp.up_proj | 13762560 | 0.008115 | 5.896e-10 |
| 19 | 8 | `model.layers.0.self_attn.o_proj` | attn.o_proj | 2359296 | 0.007883 | 3.341e-09 |
| 58 | 8 | `model.layers.27.mlp.gate_proj` | mlp.gate_proj | 13762560 | 0.007838 | 5.695e-10 |
| 61 | 4 | `model.layers.3.mlp.gate_proj` | mlp.gate_proj | 13762560 | 0.007165 | 5.206e-10 |
| 2 | 8 | `model.layers.2.self_attn.v_proj` | attn.v_proj | 393472 | 0.007072 | 1.797e-08 |
| 63 | 4 | `model.layers.0.mlp.up_proj` | mlp.up_proj | 13762560 | 0.006831 | 4.963e-10 |
| 68 | 4 | `model.layers.1.mlp.gate_proj` | mlp.gate_proj | 13762560 | 0.005979 | 4.345e-10 |
| 3 | 8 | `model.layers.17.self_attn.v_proj` | attn.v_proj | 393472 | 0.005770 | 1.466e-08 |
| 69 | 4 | `model.layers.27.mlp.up_proj` | mlp.up_proj | 13762560 | 0.005661 | 4.114e-10 |
| 75 | 4 | `model.layers.26.mlp.up_proj` | mlp.up_proj | 13762560 | 0.005076 | 3.689e-10 |

## Top Cost-Normalized Delta

| rank | bits | module | category | params | delta NLL | delta/param |
|---:|---:|---|---|---:|---:|---:|
| 1 | 8 | `model.layers.0.self_attn.v_proj` | attn.v_proj | 393472 | 0.019994 | 5.081e-08 |
| 2 | 8 | `model.layers.2.self_attn.v_proj` | attn.v_proj | 393472 | 0.007072 | 1.797e-08 |
| 3 | 8 | `model.layers.17.self_attn.v_proj` | attn.v_proj | 393472 | 0.005770 | 1.466e-08 |
| 4 | 8 | `model.layers.1.self_attn.v_proj` | attn.v_proj | 393472 | 0.004760 | 1.210e-08 |
| 5 | 8 | `model.layers.3.self_attn.v_proj` | attn.v_proj | 393472 | 0.003848 | 9.779e-09 |
| 6 | 8 | `model.layers.4.self_attn.k_proj` | attn.k_proj | 393472 | 0.003761 | 9.558e-09 |
| 7 | 8 | `model.layers.4.self_attn.v_proj` | attn.v_proj | 393472 | 0.003547 | 9.015e-09 |
| 8 | 8 | `model.layers.22.self_attn.v_proj` | attn.v_proj | 393472 | 0.003139 | 7.977e-09 |
| 9 | 8 | `model.layers.15.self_attn.v_proj` | attn.v_proj | 393472 | 0.002680 | 6.810e-09 |
| 10 | 8 | `model.layers.13.self_attn.k_proj` | attn.k_proj | 393472 | 0.002547 | 6.473e-09 |
| 11 | 8 | `model.layers.8.self_attn.v_proj` | attn.v_proj | 393472 | 0.002344 | 5.958e-09 |
| 12 | 8 | `model.layers.11.self_attn.v_proj` | attn.v_proj | 393472 | 0.001839 | 4.674e-09 |
| 13 | 8 | `model.layers.10.self_attn.v_proj` | attn.v_proj | 393472 | 0.001629 | 4.141e-09 |
| 14 | 8 | `model.layers.15.self_attn.k_proj` | attn.k_proj | 393472 | 0.001568 | 3.984e-09 |
| 15 | 8 | `model.layers.19.self_attn.k_proj` | attn.k_proj | 393472 | 0.001564 | 3.974e-09 |
| 16 | 8 | `model.layers.13.self_attn.v_proj` | attn.v_proj | 393472 | 0.001444 | 3.670e-09 |
| 17 | 8 | `model.layers.23.self_attn.k_proj` | attn.k_proj | 393472 | 0.001389 | 3.530e-09 |
| 18 | 8 | `model.layers.14.self_attn.k_proj` | attn.k_proj | 393472 | 0.001315 | 3.342e-09 |
| 19 | 8 | `model.layers.0.self_attn.o_proj` | attn.o_proj | 2359296 | 0.007883 | 3.341e-09 |
| 20 | 8 | `model.layers.24.self_attn.v_proj` | attn.v_proj | 393472 | 0.001128 | 2.867e-09 |

## Selected 8-bit Modules By Rank

| rank | bits | module | category | params | delta NLL | delta/param |
|---:|---:|---|---|---:|---:|---:|
| 1 | 8 | `model.layers.0.self_attn.v_proj` | attn.v_proj | 393472 | 0.019994 | 5.081e-08 |
| 2 | 8 | `model.layers.2.self_attn.v_proj` | attn.v_proj | 393472 | 0.007072 | 1.797e-08 |
| 3 | 8 | `model.layers.17.self_attn.v_proj` | attn.v_proj | 393472 | 0.005770 | 1.466e-08 |
| 4 | 8 | `model.layers.1.self_attn.v_proj` | attn.v_proj | 393472 | 0.004760 | 1.210e-08 |
| 5 | 8 | `model.layers.3.self_attn.v_proj` | attn.v_proj | 393472 | 0.003848 | 9.779e-09 |
| 6 | 8 | `model.layers.4.self_attn.k_proj` | attn.k_proj | 393472 | 0.003761 | 9.558e-09 |
| 7 | 8 | `model.layers.4.self_attn.v_proj` | attn.v_proj | 393472 | 0.003547 | 9.015e-09 |
| 8 | 8 | `model.layers.22.self_attn.v_proj` | attn.v_proj | 393472 | 0.003139 | 7.977e-09 |
| 9 | 8 | `model.layers.15.self_attn.v_proj` | attn.v_proj | 393472 | 0.002680 | 6.810e-09 |
| 10 | 8 | `model.layers.13.self_attn.k_proj` | attn.k_proj | 393472 | 0.002547 | 6.473e-09 |
| 11 | 8 | `model.layers.8.self_attn.v_proj` | attn.v_proj | 393472 | 0.002344 | 5.958e-09 |
| 12 | 8 | `model.layers.11.self_attn.v_proj` | attn.v_proj | 393472 | 0.001839 | 4.674e-09 |
| 13 | 8 | `model.layers.10.self_attn.v_proj` | attn.v_proj | 393472 | 0.001629 | 4.141e-09 |
| 14 | 8 | `model.layers.15.self_attn.k_proj` | attn.k_proj | 393472 | 0.001568 | 3.984e-09 |
| 15 | 8 | `model.layers.19.self_attn.k_proj` | attn.k_proj | 393472 | 0.001564 | 3.974e-09 |
| 16 | 8 | `model.layers.13.self_attn.v_proj` | attn.v_proj | 393472 | 0.001444 | 3.670e-09 |
| 17 | 8 | `model.layers.23.self_attn.k_proj` | attn.k_proj | 393472 | 0.001389 | 3.530e-09 |
| 18 | 8 | `model.layers.14.self_attn.k_proj` | attn.k_proj | 393472 | 0.001315 | 3.342e-09 |
| 19 | 8 | `model.layers.0.self_attn.o_proj` | attn.o_proj | 2359296 | 0.007883 | 3.341e-09 |
| 20 | 8 | `model.layers.24.self_attn.v_proj` | attn.v_proj | 393472 | 0.001128 | 2.867e-09 |

## Note

Absolute loss increase and cost-normalized loss increase can disagree.
The allocation is budget-constrained, so small but highly sensitive
projection matrices can outrank very large modules with bigger absolute
delta but lower delta per parameter.
