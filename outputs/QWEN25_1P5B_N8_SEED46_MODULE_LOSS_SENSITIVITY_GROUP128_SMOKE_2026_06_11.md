# Module Loss Sensitivity Report

Date: `2026-06-11`
Model: `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct`
Prompts: `8`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.677490`
- FP16 PPL: `14.548527`
- Tokens: `689`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 142, '8': 55} | 0.6604 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 5 | `model.layers.1.mlp.down_proj` | 13762560 | 0.105784 | 0.000000007686 |
| 67 | `lm_head` | 233373696 | 0.073193 | 0.000000000314 |
| 18 | `model.layers.26.mlp.down_proj` | 13762560 | 0.033096 | 0.000000002405 |
| 19 | `model.layers.2.mlp.down_proj` | 13762560 | 0.029595 | 0.000000002150 |
| 31 | `model.layers.27.mlp.down_proj` | 13762560 | 0.013447 | 0.000000000977 |
| 35 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.011359 | 0.000000000825 |
| 38 | `model.layers.4.mlp.up_proj` | 13762560 | 0.011286 | 0.000000000820 |
| 46 | `model.layers.22.mlp.down_proj` | 13762560 | 0.007584 | 0.000000000551 |
| 48 | `model.layers.23.mlp.down_proj` | 13762560 | 0.006989 | 0.000000000508 |
| 49 | `model.layers.27.mlp.up_proj` | 13762560 | 0.006923 | 0.000000000503 |
| 51 | `model.layers.4.mlp.gate_proj` | 13762560 | 0.006568 | 0.000000000477 |
| 52 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.006375 | 0.000000000463 |
| 56 | `model.layers.20.mlp.up_proj` | 13762560 | 0.006058 | 0.000000000440 |
| 58 | `model.layers.5.mlp.up_proj` | 13762560 | 0.005496 | 0.000000000399 |
| 60 | `model.layers.6.mlp.gate_proj` | 13762560 | 0.005289 | 0.000000000384 |
| 1 | `model.layers.24.self_attn.v_proj` | 393472 | 0.004128 | 0.000000010491 |
| 23 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.004054 | 0.000000001718 |
| 24 | `model.layers.27.self_attn.o_proj` | 2359296 | 0.003630 | 0.000000001539 |
| 2 | `model.layers.17.self_attn.v_proj` | 393472 | 0.003558 | 0.000000009043 |
| 70 | `model.layers.1.mlp.up_proj` | 13762560 | 0.003403 | 0.000000000247 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
