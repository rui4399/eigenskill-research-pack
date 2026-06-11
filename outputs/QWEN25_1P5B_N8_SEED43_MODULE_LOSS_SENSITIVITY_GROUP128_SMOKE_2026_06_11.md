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

- FP16 mean NLL: `2.992768`
- FP16 PPL: `19.940812`
- Tokens: `724`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4983 | 0.9996 | {'4': 129, '8': 68} | 0.6596 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 3 | `model.layers.1.mlp.down_proj` | 13762560 | 0.117576 | 0.000000008543 |
| 76 | `lm_head` | 233373696 | 0.064537 | 0.000000000277 |
| 16 | `model.layers.26.mlp.down_proj` | 13762560 | 0.044516 | 0.000000003235 |
| 24 | `model.layers.2.mlp.down_proj` | 13762560 | 0.030505 | 0.000000002216 |
| 51 | `model.layers.27.mlp.down_proj` | 13762560 | 0.008291 | 0.000000000602 |
| 55 | `model.layers.4.mlp.up_proj` | 13762560 | 0.007361 | 0.000000000535 |
| 56 | `model.layers.1.mlp.up_proj` | 13762560 | 0.007176 | 0.000000000521 |
| 57 | `model.layers.5.mlp.up_proj` | 13762560 | 0.007077 | 0.000000000514 |
| 58 | `model.layers.23.mlp.down_proj` | 13762560 | 0.007058 | 0.000000000513 |
| 17 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.006814 | 0.000000002888 |
| 59 | `model.layers.6.mlp.gate_proj` | 13762560 | 0.006570 | 0.000000000477 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.005838 | 0.000000014837 |
| 62 | `model.layers.4.mlp.gate_proj` | 13762560 | 0.005464 | 0.000000000397 |
| 63 | `model.layers.20.mlp.up_proj` | 13762560 | 0.005387 | 0.000000000391 |
| 64 | `model.layers.12.mlp.down_proj` | 13762560 | 0.005233 | 0.000000000380 |
| 68 | `model.layers.22.mlp.down_proj` | 13762560 | 0.004501 | 0.000000000327 |
| 69 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.004425 | 0.000000000322 |
| 75 | `model.layers.14.mlp.down_proj` | 13762560 | 0.003985 | 0.000000000290 |
| 29 | `model.layers.21.self_attn.o_proj` | 2359296 | 0.003912 | 0.000000001658 |
| 77 | `model.layers.7.mlp.down_proj` | 13762560 | 0.003797 | 0.000000000276 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
