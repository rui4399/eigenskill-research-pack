# Module Loss Sensitivity Report

Date: `2026-06-11`
Model: `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct`
Prompts: `4`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.722318`
- FP16 PPL: `15.215553`
- Tokens: `344`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 147, '8': 50} | 0.6594 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 2 | `model.layers.1.mlp.down_proj` | 13762560 | 0.093206 | 0.000000006772 |
| 10 | `model.layers.2.mlp.down_proj` | 13762560 | 0.055650 | 0.000000004044 |
| 74 | `lm_head` | 233373696 | 0.052510 | 0.000000000225 |
| 11 | `model.layers.26.mlp.down_proj` | 13762560 | 0.045575 | 0.000000003312 |
| 23 | `model.layers.27.mlp.down_proj` | 13762560 | 0.023931 | 0.000000001739 |
| 40 | `model.layers.9.mlp.up_proj` | 13762560 | 0.009293 | 0.000000000675 |
| 42 | `model.layers.19.mlp.down_proj` | 13762560 | 0.008045 | 0.000000000585 |
| 45 | `model.layers.3.mlp.down_proj` | 13762560 | 0.007285 | 0.000000000529 |
| 47 | `model.layers.5.mlp.up_proj` | 13762560 | 0.006539 | 0.000000000475 |
| 18 | `model.layers.26.self_attn.o_proj` | 2359296 | 0.006538 | 0.000000002771 |
| 49 | `model.layers.26.mlp.up_proj` | 13762560 | 0.006140 | 0.000000000446 |
| 1 | `model.layers.24.self_attn.v_proj` | 393472 | 0.005839 | 0.000000014840 |
| 50 | `model.layers.20.mlp.up_proj` | 13762560 | 0.005073 | 0.000000000369 |
| 52 | `model.layers.23.mlp.gate_proj` | 13762560 | 0.004605 | 0.000000000335 |
| 53 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.004562 | 0.000000000331 |
| 22 | `model.layers.21.self_attn.o_proj` | 2359296 | 0.004523 | 0.000000001917 |
| 54 | `model.layers.4.mlp.down_proj` | 13762560 | 0.004403 | 0.000000000320 |
| 55 | `model.layers.18.mlp.up_proj` | 13762560 | 0.004280 | 0.000000000311 |
| 56 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.004209 | 0.000000000306 |
| 58 | `model.layers.7.mlp.down_proj` | 13762560 | 0.004160 | 0.000000000302 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
