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

- FP16 mean NLL: `2.788472`
- FP16 PPL: `16.256170`
- Tokens: `372`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4973 | 0.9994 | {'4': 144, '8': 53} | 0.6460 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 3 | `model.layers.1.mlp.down_proj` | 13762560 | 0.110934 | 0.000000008061 |
| 65 | `lm_head` | 233373696 | 0.063889 | 0.000000000274 |
| 12 | `model.layers.26.mlp.down_proj` | 13762560 | 0.050040 | 0.000000003636 |
| 17 | `model.layers.2.mlp.down_proj` | 13762560 | 0.034845 | 0.000000002532 |
| 29 | `model.layers.27.mlp.down_proj` | 13762560 | 0.012916 | 0.000000000938 |
| 37 | `model.layers.1.mlp.up_proj` | 13762560 | 0.009483 | 0.000000000689 |
| 38 | `model.layers.5.mlp.up_proj` | 13762560 | 0.009463 | 0.000000000688 |
| 42 | `model.layers.23.mlp.down_proj` | 13762560 | 0.008050 | 0.000000000585 |
| 44 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.007491 | 0.000000000544 |
| 16 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.006549 | 0.000000002776 |
| 46 | `model.layers.11.mlp.up_proj` | 13762560 | 0.006011 | 0.000000000437 |
| 47 | `model.layers.20.mlp.up_proj` | 13762560 | 0.005926 | 0.000000000431 |
| 49 | `model.layers.4.mlp.down_proj` | 13762560 | 0.005745 | 0.000000000417 |
| 20 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.005690 | 0.000000002412 |
| 51 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.005459 | 0.000000000397 |
| 52 | `model.layers.8.mlp.up_proj` | 13762560 | 0.005452 | 0.000000000396 |
| 21 | `model.layers.16.self_attn.o_proj` | 2359296 | 0.005057 | 0.000000002143 |
| 54 | `model.layers.12.mlp.gate_proj` | 13762560 | 0.004762 | 0.000000000346 |
| 55 | `model.layers.15.mlp.up_proj` | 13762560 | 0.004718 | 0.000000000343 |
| 23 | `model.layers.3.self_attn.o_proj` | 2359296 | 0.004521 | 0.000000001916 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
