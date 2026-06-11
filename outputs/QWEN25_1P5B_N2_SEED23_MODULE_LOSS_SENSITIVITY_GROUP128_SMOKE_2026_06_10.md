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

- FP16 mean NLL: `2.434680`
- FP16 PPL: `11.412161`
- Tokens: `153`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4952 | 0.9989 | {'4': 141, '8': 56} | 0.7117 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 11 | `model.layers.1.mlp.down_proj` | 13762560 | 0.143611 | 0.000000010435 |
| 17 | `model.layers.26.mlp.down_proj` | 13762560 | 0.071343 | 0.000000005184 |
| 89 | `lm_head` | 233373696 | 0.051382 | 0.000000000220 |
| 44 | `model.layers.2.mlp.down_proj` | 13762560 | 0.018742 | 0.000000001362 |
| 45 | `model.layers.4.mlp.up_proj` | 13762560 | 0.017068 | 0.000000001240 |
| 47 | `model.layers.27.mlp.down_proj` | 13762560 | 0.014399 | 0.000000001046 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.014328 | 0.000000036415 |
| 48 | `model.layers.3.mlp.up_proj` | 13762560 | 0.014053 | 0.000000001021 |
| 49 | `model.layers.27.mlp.up_proj` | 13762560 | 0.013661 | 0.000000000993 |
| 50 | `model.layers.1.mlp.up_proj` | 13762560 | 0.013073 | 0.000000000950 |
| 52 | `model.layers.23.mlp.down_proj` | 13762560 | 0.011281 | 0.000000000820 |
| 20 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.011075 | 0.000000004694 |
| 53 | `model.layers.22.mlp.down_proj` | 13762560 | 0.010339 | 0.000000000751 |
| 54 | `model.layers.6.mlp.gate_proj` | 13762560 | 0.010192 | 0.000000000741 |
| 2 | `model.layers.20.self_attn.v_proj` | 393472 | 0.009622 | 0.000000024454 |
| 57 | `model.layers.21.mlp.down_proj` | 13762560 | 0.009217 | 0.000000000670 |
| 58 | `model.layers.6.mlp.down_proj` | 13762560 | 0.009155 | 0.000000000665 |
| 3 | `model.layers.2.self_attn.k_proj` | 393472 | 0.009145 | 0.000000023241 |
| 26 | `model.layers.20.self_attn.o_proj` | 2359296 | 0.008323 | 0.000000003528 |
| 27 | `model.layers.2.self_attn.o_proj` | 2359296 | 0.008318 | 0.000000003526 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
