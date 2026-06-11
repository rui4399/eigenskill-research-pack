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

- FP16 mean NLL: `2.892741`
- FP16 PPL: `18.042701`
- Tokens: `380`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9999 | {'4': 133, '8': 64} | 0.6574 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 4 | `model.layers.1.mlp.down_proj` | 13762560 | 0.123273 | 0.000000008957 |
| 72 | `lm_head` | 233373696 | 0.075875 | 0.000000000325 |
| 25 | `model.layers.26.mlp.down_proj` | 13762560 | 0.039432 | 0.000000002865 |
| 29 | `model.layers.2.mlp.down_proj` | 13762560 | 0.024439 | 0.000000001776 |
| 41 | `model.layers.4.mlp.up_proj` | 13762560 | 0.013269 | 0.000000000964 |
| 50 | `model.layers.22.mlp.down_proj` | 13762560 | 0.008702 | 0.000000000632 |
| 22 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.007270 | 0.000000003081 |
| 57 | `model.layers.1.mlp.up_proj` | 13762560 | 0.006902 | 0.000000000501 |
| 58 | `model.layers.5.mlp.up_proj` | 13762560 | 0.006761 | 0.000000000491 |
| 59 | `model.layers.27.mlp.up_proj` | 13762560 | 0.006576 | 0.000000000478 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.006456 | 0.000000016408 |
| 62 | `model.layers.23.mlp.down_proj` | 13762560 | 0.006133 | 0.000000000446 |
| 64 | `model.layers.4.mlp.gate_proj` | 13762560 | 0.005880 | 0.000000000427 |
| 2 | `model.layers.17.self_attn.v_proj` | 393472 | 0.004898 | 0.000000012449 |
| 67 | `model.layers.26.mlp.gate_proj` | 13762560 | 0.004879 | 0.000000000355 |
| 68 | `model.layers.16.mlp.up_proj` | 13762560 | 0.004841 | 0.000000000352 |
| 69 | `model.layers.12.mlp.down_proj` | 13762560 | 0.004812 | 0.000000000350 |
| 71 | `model.layers.6.mlp.gate_proj` | 13762560 | 0.004605 | 0.000000000335 |
| 73 | `model.layers.23.mlp.up_proj` | 13762560 | 0.004091 | 0.000000000297 |
| 75 | `model.layers.11.mlp.down_proj` | 13762560 | 0.004011 | 0.000000000291 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
