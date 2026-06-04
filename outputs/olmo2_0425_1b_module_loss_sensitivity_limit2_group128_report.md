# Module Loss Sensitivity Report

Date: `2026-06-05`
Model: `allenai/OLMo-2-0425-1B-Instruct`
Prompts: `2`
Max length: `160`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `113 / 113`

## Baseline

- FP16 mean NLL: `2.092133`
- FP16 PPL: `8.102182`
- Tokens: `317`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 113} | 0.0000 |
| loss_sensitive_4to8 | 4.4984 | 0.9996 | {'8': 23, '4': 90} | 0.4837 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 57 | `lm_head` | 205520896 | 0.026611 | 0.000000000129 |
| 6 | `model.layers.14.mlp.down_proj` | 16777216 | 0.020051 | 0.000000001195 |
| 14 | `model.layers.11.mlp.down_proj` | 16777216 | 0.013808 | 0.000000000823 |
| 15 | `model.layers.14.mlp.up_proj` | 16777216 | 0.012066 | 0.000000000719 |
| 16 | `model.layers.2.mlp.gate_proj` | 16777216 | 0.011800 | 0.000000000703 |
| 21 | `model.layers.6.mlp.down_proj` | 16777216 | 0.010601 | 0.000000000632 |
| 22 | `model.layers.5.mlp.gate_proj` | 16777216 | 0.010122 | 0.000000000603 |
| 1 | `model.layers.11.self_attn.o_proj` | 4194304 | 0.009849 | 0.000000002348 |
| 27 | `model.layers.12.mlp.gate_proj` | 16777216 | 0.008996 | 0.000000000536 |
| 29 | `model.layers.3.mlp.up_proj` | 16777216 | 0.007716 | 0.000000000460 |
| 30 | `model.layers.4.mlp.gate_proj` | 16777216 | 0.007224 | 0.000000000431 |
| 31 | `model.layers.10.mlp.down_proj` | 16777216 | 0.006966 | 0.000000000415 |
| 2 | `model.layers.2.self_attn.o_proj` | 4194304 | 0.006829 | 0.000000001628 |
| 3 | `model.layers.12.self_attn.o_proj` | 4194304 | 0.006464 | 0.000000001541 |
| 33 | `model.layers.4.mlp.up_proj` | 16777216 | 0.006051 | 0.000000000361 |
| 34 | `model.layers.14.mlp.gate_proj` | 16777216 | 0.005927 | 0.000000000353 |
| 35 | `model.layers.3.mlp.gate_proj` | 16777216 | 0.005850 | 0.000000000349 |
| 37 | `model.layers.12.mlp.up_proj` | 16777216 | 0.005640 | 0.000000000336 |
| 4 | `model.layers.9.self_attn.o_proj` | 4194304 | 0.005595 | 0.000000001334 |
| 39 | `model.layers.4.mlp.down_proj` | 16777216 | 0.005428 | 0.000000000324 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
