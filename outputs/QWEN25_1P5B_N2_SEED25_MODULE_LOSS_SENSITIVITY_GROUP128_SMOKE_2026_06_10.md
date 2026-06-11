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

- FP16 mean NLL: `2.978373`
- FP16 PPL: `19.655816`
- Tokens: `190`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 147, '8': 50} | 0.5885 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 63 | `lm_head` | 233373696 | 0.089391 | 0.000000000383 |
| 5 | `model.layers.1.mlp.down_proj` | 13762560 | 0.088417 | 0.000000006424 |
| 21 | `model.layers.27.mlp.down_proj` | 13762560 | 0.023341 | 0.000000001696 |
| 31 | `model.layers.26.mlp.down_proj` | 13762560 | 0.015335 | 0.000000001114 |
| 35 | `model.layers.2.mlp.down_proj` | 13762560 | 0.012596 | 0.000000000915 |
| 14 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.010310 | 0.000000004370 |
| 39 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.010048 | 0.000000000730 |
| 41 | `model.layers.5.mlp.up_proj` | 13762560 | 0.009657 | 0.000000000702 |
| 42 | `model.layers.4.mlp.up_proj` | 13762560 | 0.009462 | 0.000000000688 |
| 45 | `model.layers.4.mlp.gate_proj` | 13762560 | 0.008540 | 0.000000000621 |
| 47 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.007372 | 0.000000000536 |
| 48 | `model.layers.18.mlp.up_proj` | 13762560 | 0.007357 | 0.000000000535 |
| 52 | `model.layers.20.mlp.up_proj` | 13762560 | 0.007190 | 0.000000000522 |
| 55 | `model.layers.16.mlp.up_proj` | 13762560 | 0.006898 | 0.000000000501 |
| 56 | `model.layers.12.mlp.gate_proj` | 13762560 | 0.006884 | 0.000000000500 |
| 58 | `model.layers.14.mlp.down_proj` | 13762560 | 0.006068 | 0.000000000441 |
| 60 | `model.layers.24.mlp.down_proj` | 13762560 | 0.005995 | 0.000000000436 |
| 61 | `model.layers.9.mlp.up_proj` | 13762560 | 0.005441 | 0.000000000395 |
| 62 | `model.layers.16.mlp.down_proj` | 13762560 | 0.005352 | 0.000000000389 |
| 64 | `model.layers.23.mlp.down_proj` | 13762560 | 0.005257 | 0.000000000382 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
