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

- FP16 mean NLL: `2.690920`
- FP16 PPL: `14.745241`
- Tokens: `352`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9999 | {'4': 138, '8': 59} | 0.6124 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 8 | `model.layers.1.mlp.down_proj` | 13762560 | 0.106257 | 0.000000007721 |
| 57 | `lm_head` | 233373696 | 0.102727 | 0.000000000440 |
| 13 | `model.layers.2.mlp.down_proj` | 13762560 | 0.055040 | 0.000000003999 |
| 19 | `model.layers.26.mlp.down_proj` | 13762560 | 0.035244 | 0.000000002561 |
| 34 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.013407 | 0.000000000974 |
| 43 | `model.layers.4.mlp.up_proj` | 13762560 | 0.009388 | 0.000000000682 |
| 44 | `model.layers.27.mlp.down_proj` | 13762560 | 0.009373 | 0.000000000681 |
| 46 | `model.layers.23.mlp.down_proj` | 13762560 | 0.008580 | 0.000000000623 |
| 51 | `model.layers.26.mlp.up_proj` | 13762560 | 0.007982 | 0.000000000580 |
| 52 | `model.layers.2.mlp.up_proj` | 13762560 | 0.007896 | 0.000000000574 |
| 1 | `model.layers.7.self_attn.v_proj` | 393472 | 0.006983 | 0.000000017747 |
| 55 | `model.layers.12.mlp.gate_proj` | 13762560 | 0.006716 | 0.000000000488 |
| 56 | `model.layers.5.mlp.up_proj` | 13762560 | 0.006371 | 0.000000000463 |
| 20 | `model.layers.16.self_attn.o_proj` | 2359296 | 0.005981 | 0.000000002535 |
| 59 | `model.layers.3.mlp.down_proj` | 13762560 | 0.005830 | 0.000000000424 |
| 21 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.005697 | 0.000000002415 |
| 61 | `model.layers.20.mlp.up_proj` | 13762560 | 0.005472 | 0.000000000398 |
| 63 | `model.layers.22.mlp.down_proj` | 13762560 | 0.005051 | 0.000000000367 |
| 64 | `model.layers.20.mlp.gate_proj` | 13762560 | 0.005043 | 0.000000000366 |
| 2 | `model.layers.26.self_attn.v_proj` | 393472 | 0.004867 | 0.000000012369 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
