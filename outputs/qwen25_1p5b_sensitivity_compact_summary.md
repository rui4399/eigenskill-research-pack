# Sensitivity Compact Summary

Source: `outputs\qwen25_1p5b_module_loss_sensitivity_limit2_group128.json`
Allocation: `outputs\qwen25_1p5b_loss_sensitive_alloc_4to8_limit2_group128_summary.json`
Method: `loss_sensitive_4to8`

## Overview

| metric | value |
|---|---:|
| modules | 197 |
| selected 8-bit modules | 60 |
| selected positive delta ratio | 0.6020 |

## Category Histogram

| category | all modules | selected 8-bit |
|---|---:|---:|
| attn.k_proj | 28 | 17 |
| attn.o_proj | 28 | 9 |
| attn.q_proj | 28 | 9 |
| attn.v_proj | 28 | 15 |
| lm_head | 1 | 0 |
| mlp.down_proj | 28 | 4 |
| mlp.gate_proj | 28 | 3 |
| mlp.up_proj | 28 | 3 |

## Top Absolute Positive Delta

| rank | bits | module | category | params | delta NLL | delta/param |
|---:|---:|---|---|---:|---:|---:|
| 75 | 4 | `lm_head` | lm_head | 233373696 | 0.093741 | 4.017e-10 |
| 21 | 8 | `model.layers.26.mlp.down_proj` | mlp.down_proj | 13762560 | 0.047007 | 3.416e-09 |
| 29 | 8 | `model.layers.2.mlp.down_proj` | mlp.down_proj | 13762560 | 0.034742 | 2.524e-09 |
| 1 | 8 | `model.layers.0.self_attn.v_proj` | attn.v_proj | 393472 | 0.032466 | 8.251e-08 |
| 38 | 8 | `model.layers.3.mlp.up_proj` | mlp.up_proj | 13762560 | 0.022985 | 1.670e-09 |
| 39 | 8 | `model.layers.3.mlp.down_proj` | mlp.down_proj | 13762560 | 0.022533 | 1.637e-09 |
| 40 | 8 | `model.layers.3.mlp.gate_proj` | mlp.gate_proj | 13762560 | 0.022066 | 1.603e-09 |
| 41 | 8 | `model.layers.2.mlp.gate_proj` | mlp.gate_proj | 13762560 | 0.020737 | 1.507e-09 |
| 46 | 8 | `model.layers.27.mlp.down_proj` | mlp.down_proj | 13762560 | 0.017165 | 1.247e-09 |
| 47 | 8 | `model.layers.2.mlp.up_proj` | mlp.up_proj | 13762560 | 0.016813 | 1.222e-09 |
| 2 | 8 | `model.layers.2.self_attn.v_proj` | attn.v_proj | 393472 | 0.016008 | 4.069e-08 |
| 53 | 8 | `model.layers.1.mlp.up_proj` | mlp.up_proj | 13762560 | 0.014961 | 1.087e-09 |
| 60 | 8 | `model.layers.1.mlp.gate_proj` | mlp.gate_proj | 13762560 | 0.010606 | 7.706e-10 |
| 61 | 4 | `model.layers.26.mlp.up_proj` | mlp.up_proj | 13762560 | 0.010263 | 7.457e-10 |
| 3 | 8 | `model.layers.3.self_attn.v_proj` | attn.v_proj | 393472 | 0.009128 | 2.320e-08 |
| 66 | 4 | `model.layers.0.mlp.up_proj` | mlp.up_proj | 13762560 | 0.008913 | 6.476e-10 |
| 68 | 4 | `model.layers.6.mlp.up_proj` | mlp.up_proj | 13762560 | 0.008219 | 5.972e-10 |
| 69 | 4 | `model.layers.15.mlp.up_proj` | mlp.up_proj | 13762560 | 0.007246 | 5.265e-10 |
| 70 | 4 | `model.layers.21.mlp.gate_proj` | mlp.gate_proj | 13762560 | 0.007181 | 5.218e-10 |
| 71 | 4 | `model.layers.19.mlp.down_proj` | mlp.down_proj | 13762560 | 0.006916 | 5.025e-10 |

## Top Cost-Normalized Delta

| rank | bits | module | category | params | delta NLL | delta/param |
|---:|---:|---|---|---:|---:|---:|
| 1 | 8 | `model.layers.0.self_attn.v_proj` | attn.v_proj | 393472 | 0.032466 | 8.251e-08 |
| 2 | 8 | `model.layers.2.self_attn.v_proj` | attn.v_proj | 393472 | 0.016008 | 4.069e-08 |
| 3 | 8 | `model.layers.3.self_attn.v_proj` | attn.v_proj | 393472 | 0.009128 | 2.320e-08 |
| 4 | 8 | `model.layers.17.self_attn.v_proj` | attn.v_proj | 393472 | 0.006238 | 1.585e-08 |
| 5 | 8 | `model.layers.11.self_attn.v_proj` | attn.v_proj | 393472 | 0.005505 | 1.399e-08 |
| 6 | 8 | `model.layers.7.self_attn.v_proj` | attn.v_proj | 393472 | 0.004792 | 1.218e-08 |
| 7 | 8 | `model.layers.6.self_attn.k_proj` | attn.k_proj | 393472 | 0.003820 | 9.708e-09 |
| 8 | 8 | `model.layers.21.self_attn.k_proj` | attn.k_proj | 393472 | 0.002970 | 7.547e-09 |
| 9 | 8 | `model.layers.22.self_attn.k_proj` | attn.k_proj | 393472 | 0.002927 | 7.440e-09 |
| 10 | 8 | `model.layers.1.self_attn.v_proj` | attn.v_proj | 393472 | 0.002873 | 7.301e-09 |
| 11 | 8 | `model.layers.12.self_attn.v_proj` | attn.v_proj | 393472 | 0.002858 | 7.264e-09 |
| 12 | 8 | `model.layers.22.self_attn.v_proj` | attn.v_proj | 393472 | 0.002821 | 7.170e-09 |
| 13 | 8 | `model.layers.10.self_attn.v_proj` | attn.v_proj | 393472 | 0.002720 | 6.914e-09 |
| 14 | 8 | `model.layers.13.self_attn.k_proj` | attn.k_proj | 393472 | 0.002491 | 6.332e-09 |
| 15 | 8 | `model.layers.8.self_attn.v_proj` | attn.v_proj | 393472 | 0.002470 | 6.276e-09 |
| 16 | 8 | `model.layers.16.self_attn.k_proj` | attn.k_proj | 393472 | 0.002047 | 5.202e-09 |
| 17 | 8 | `model.layers.24.self_attn.v_proj` | attn.v_proj | 393472 | 0.002027 | 5.153e-09 |
| 18 | 8 | `model.layers.13.self_attn.v_proj` | attn.v_proj | 393472 | 0.001978 | 5.026e-09 |
| 19 | 8 | `model.layers.14.self_attn.k_proj` | attn.k_proj | 393472 | 0.001960 | 4.981e-09 |
| 20 | 8 | `model.layers.17.self_attn.k_proj` | attn.k_proj | 393472 | 0.001633 | 4.151e-09 |

## Selected 8-bit Modules By Rank

| rank | bits | module | category | params | delta NLL | delta/param |
|---:|---:|---|---|---:|---:|---:|
| 1 | 8 | `model.layers.0.self_attn.v_proj` | attn.v_proj | 393472 | 0.032466 | 8.251e-08 |
| 2 | 8 | `model.layers.2.self_attn.v_proj` | attn.v_proj | 393472 | 0.016008 | 4.069e-08 |
| 3 | 8 | `model.layers.3.self_attn.v_proj` | attn.v_proj | 393472 | 0.009128 | 2.320e-08 |
| 4 | 8 | `model.layers.17.self_attn.v_proj` | attn.v_proj | 393472 | 0.006238 | 1.585e-08 |
| 5 | 8 | `model.layers.11.self_attn.v_proj` | attn.v_proj | 393472 | 0.005505 | 1.399e-08 |
| 6 | 8 | `model.layers.7.self_attn.v_proj` | attn.v_proj | 393472 | 0.004792 | 1.218e-08 |
| 7 | 8 | `model.layers.6.self_attn.k_proj` | attn.k_proj | 393472 | 0.003820 | 9.708e-09 |
| 8 | 8 | `model.layers.21.self_attn.k_proj` | attn.k_proj | 393472 | 0.002970 | 7.547e-09 |
| 9 | 8 | `model.layers.22.self_attn.k_proj` | attn.k_proj | 393472 | 0.002927 | 7.440e-09 |
| 10 | 8 | `model.layers.1.self_attn.v_proj` | attn.v_proj | 393472 | 0.002873 | 7.301e-09 |
| 11 | 8 | `model.layers.12.self_attn.v_proj` | attn.v_proj | 393472 | 0.002858 | 7.264e-09 |
| 12 | 8 | `model.layers.22.self_attn.v_proj` | attn.v_proj | 393472 | 0.002821 | 7.170e-09 |
| 13 | 8 | `model.layers.10.self_attn.v_proj` | attn.v_proj | 393472 | 0.002720 | 6.914e-09 |
| 14 | 8 | `model.layers.13.self_attn.k_proj` | attn.k_proj | 393472 | 0.002491 | 6.332e-09 |
| 15 | 8 | `model.layers.8.self_attn.v_proj` | attn.v_proj | 393472 | 0.002470 | 6.276e-09 |
| 16 | 8 | `model.layers.16.self_attn.k_proj` | attn.k_proj | 393472 | 0.002047 | 5.202e-09 |
| 17 | 8 | `model.layers.24.self_attn.v_proj` | attn.v_proj | 393472 | 0.002027 | 5.153e-09 |
| 18 | 8 | `model.layers.13.self_attn.v_proj` | attn.v_proj | 393472 | 0.001978 | 5.026e-09 |
| 19 | 8 | `model.layers.14.self_attn.k_proj` | attn.k_proj | 393472 | 0.001960 | 4.981e-09 |
| 20 | 8 | `model.layers.17.self_attn.k_proj` | attn.k_proj | 393472 | 0.001633 | 4.151e-09 |

## Note

Absolute loss increase and cost-normalized loss increase can disagree.
The allocation is budget-constrained, so small but highly sensitive
projection matrices can outrank very large modules with bigger absolute
delta but lower delta per parameter.
