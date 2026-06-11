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

- FP16 mean NLL: `2.535273`
- FP16 PPL: `12.619870`
- Tokens: `661`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9999 | {'4': 138, '8': 59} | 0.6662 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 5 | `model.layers.1.mlp.down_proj` | 13762560 | 0.097724 | 0.000000007101 |
| 59 | `lm_head` | 233373696 | 0.072189 | 0.000000000309 |
| 13 | `model.layers.2.mlp.down_proj` | 13762560 | 0.052376 | 0.000000003806 |
| 14 | `model.layers.26.mlp.down_proj` | 13762560 | 0.036537 | 0.000000002655 |
| 29 | `model.layers.27.mlp.down_proj` | 13762560 | 0.016901 | 0.000000001228 |
| 37 | `model.layers.4.mlp.up_proj` | 13762560 | 0.011321 | 0.000000000823 |
| 45 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.008728 | 0.000000000634 |
| 46 | `model.layers.22.mlp.down_proj` | 13762560 | 0.007824 | 0.000000000568 |
| 50 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.006499 | 0.000000000472 |
| 51 | `model.layers.3.mlp.down_proj` | 13762560 | 0.006372 | 0.000000000463 |
| 1 | `model.layers.24.self_attn.v_proj` | 393472 | 0.005445 | 0.000000013839 |
| 18 | `model.layers.26.self_attn.o_proj` | 2359296 | 0.005049 | 0.000000002140 |
| 56 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.004846 | 0.000000000352 |
| 57 | `model.layers.1.mlp.up_proj` | 13762560 | 0.004839 | 0.000000000352 |
| 19 | `model.layers.21.self_attn.o_proj` | 2359296 | 0.004788 | 0.000000002029 |
| 58 | `model.layers.23.mlp.down_proj` | 13762560 | 0.004553 | 0.000000000331 |
| 21 | `model.layers.25.self_attn.o_proj` | 2359296 | 0.004399 | 0.000000001865 |
| 60 | `model.layers.13.mlp.gate_proj` | 13762560 | 0.004120 | 0.000000000299 |
| 2 | `model.layers.20.self_attn.v_proj` | 393472 | 0.004062 | 0.000000010325 |
| 61 | `model.layers.17.mlp.up_proj` | 13762560 | 0.003931 | 0.000000000286 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
