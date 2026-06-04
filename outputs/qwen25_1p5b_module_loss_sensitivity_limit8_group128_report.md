# Module Loss Sensitivity Report

Date: `2026-06-04`
Model: `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct`
Prompts: `8`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`

## Baseline

- FP16 mean NLL: `2.319380`
- FP16 PPL: `10.169370`
- Tokens: `807`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4953 | 0.9989 | {'8': 61, '4': 136} | 0.5445 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 73 | `lm_head` | 233373696 | 0.087258 | 0.000000000374 |
| 25 | `model.layers.26.mlp.down_proj` | 13762560 | 0.030113 | 0.000000002188 |
| 27 | `model.layers.2.mlp.down_proj` | 13762560 | 0.021759 | 0.000000001581 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.019994 | 0.000000050814 |
| 28 | `model.layers.1.mlp.down_proj` | 13762560 | 0.018669 | 0.000000001357 |
| 31 | `model.layers.27.mlp.down_proj` | 13762560 | 0.016632 | 0.000000001208 |
| 33 | `model.layers.3.mlp.down_proj` | 13762560 | 0.015931 | 0.000000001158 |
| 35 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.014477 | 0.000000001052 |
| 38 | `model.layers.3.mlp.up_proj` | 13762560 | 0.013873 | 0.000000001008 |
| 42 | `model.layers.2.mlp.up_proj` | 13762560 | 0.011403 | 0.000000000829 |
| 57 | `model.layers.1.mlp.up_proj` | 13762560 | 0.008115 | 0.000000000590 |
| 19 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.007883 | 0.000000003341 |
| 58 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.007838 | 0.000000000570 |
| 61 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.007165 | 0.000000000521 |
| 2 | `model.layers.2.self_attn.v_proj` | 393472 | 0.007072 | 0.000000017973 |
| 63 | `model.layers.0.mlp.up_proj` | 13762560 | 0.006831 | 0.000000000496 |
| 68 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.005979 | 0.000000000434 |
| 3 | `model.layers.17.self_attn.v_proj` | 393472 | 0.005770 | 0.000000014664 |
| 69 | `model.layers.27.mlp.up_proj` | 13762560 | 0.005661 | 0.000000000411 |
| 75 | `model.layers.26.mlp.up_proj` | 13762560 | 0.005076 | 0.000000000369 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
