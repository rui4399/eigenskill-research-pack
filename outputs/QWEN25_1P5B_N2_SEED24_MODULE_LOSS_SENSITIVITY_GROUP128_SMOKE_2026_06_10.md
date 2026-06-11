# Module Loss Sensitivity Report

Date: `2026-06-10`
Model: `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct`
Prompts: `2`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `3.104323`
- FP16 PPL: `22.294113`
- Tokens: `190`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4983 | 0.9996 | {'8': 54, '4': 143} | 0.5721 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 3 | `model.layers.1.mlp.down_proj` | 13762560 | 0.133132 | 0.000000009673 |
| 44 | `lm_head` | 233373696 | 0.122476 | 0.000000000525 |
| 19 | `model.layers.26.mlp.down_proj` | 13762560 | 0.022617 | 0.000000001643 |
| 30 | `model.layers.4.mlp.up_proj` | 13762560 | 0.012534 | 0.000000000911 |
| 35 | `model.layers.27.mlp.down_proj` | 13762560 | 0.010234 | 0.000000000744 |
| 37 | `model.layers.24.mlp.gate_proj` | 13762560 | 0.009799 | 0.000000000712 |
| 12 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.009191 | 0.000000003896 |
| 41 | `model.layers.5.mlp.up_proj` | 13762560 | 0.008809 | 0.000000000640 |
| 43 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.007779 | 0.000000000565 |
| 48 | `model.layers.11.mlp.up_proj` | 13762560 | 0.006835 | 0.000000000497 |
| 49 | `model.layers.0.mlp.down_proj` | 13762560 | 0.006826 | 0.000000000496 |
| 50 | `model.layers.23.mlp.down_proj` | 13762560 | 0.006500 | 0.000000000472 |
| 51 | `model.layers.14.mlp.down_proj` | 13762560 | 0.006453 | 0.000000000469 |
| 52 | `model.layers.3.mlp.down_proj` | 13762560 | 0.005832 | 0.000000000424 |
| 53 | `model.layers.21.mlp.up_proj` | 13762560 | 0.005728 | 0.000000000416 |
| 1 | `model.layers.17.self_attn.v_proj` | 393472 | 0.005533 | 0.000000014063 |
| 55 | `model.layers.22.mlp.down_proj` | 13762560 | 0.005324 | 0.000000000387 |
| 2 | `model.layers.21.self_attn.v_proj` | 393472 | 0.005166 | 0.000000013129 |
| 59 | `model.layers.20.mlp.up_proj` | 13762560 | 0.005068 | 0.000000000368 |
| 60 | `model.layers.26.mlp.gate_proj` | 13762560 | 0.004863 | 0.000000000353 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
