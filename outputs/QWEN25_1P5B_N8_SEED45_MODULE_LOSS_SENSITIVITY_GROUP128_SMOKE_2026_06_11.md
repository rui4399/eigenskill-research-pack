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

- FP16 mean NLL: `2.979903`
- FP16 PPL: `19.685912`
- Tokens: `715`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 142, '8': 55} | 0.5959 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 4 | `model.layers.1.mlp.down_proj` | 13762560 | 0.099596 | 0.000000007237 |
| 56 | `lm_head` | 233373696 | 0.082512 | 0.000000000354 |
| 14 | `model.layers.26.mlp.down_proj` | 13762560 | 0.043453 | 0.000000003157 |
| 27 | `model.layers.2.mlp.down_proj` | 13762560 | 0.017199 | 0.000000001250 |
| 32 | `model.layers.27.mlp.down_proj` | 13762560 | 0.014632 | 0.000000001063 |
| 36 | `model.layers.4.mlp.up_proj` | 13762560 | 0.010067 | 0.000000000731 |
| 46 | `model.layers.3.mlp.down_proj` | 13762560 | 0.006435 | 0.000000000468 |
| 48 | `model.layers.23.mlp.down_proj` | 13762560 | 0.006253 | 0.000000000454 |
| 50 | `model.layers.20.mlp.up_proj` | 13762560 | 0.005990 | 0.000000000435 |
| 51 | `model.layers.5.mlp.up_proj` | 13762560 | 0.005645 | 0.000000000410 |
| 52 | `model.layers.22.mlp.down_proj` | 13762560 | 0.005477 | 0.000000000398 |
| 59 | `model.layers.14.mlp.up_proj` | 13762560 | 0.004427 | 0.000000000322 |
| 20 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.004234 | 0.000000001795 |
| 61 | `model.layers.8.mlp.up_proj` | 13762560 | 0.004097 | 0.000000000298 |
| 62 | `model.layers.12.mlp.down_proj` | 13762560 | 0.004030 | 0.000000000293 |
| 63 | `model.layers.3.mlp.up_proj` | 13762560 | 0.003915 | 0.000000000284 |
| 64 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.003834 | 0.000000000279 |
| 65 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.003798 | 0.000000000276 |
| 66 | `model.layers.15.mlp.up_proj` | 13762560 | 0.003742 | 0.000000000272 |
| 67 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.003581 | 0.000000000260 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
