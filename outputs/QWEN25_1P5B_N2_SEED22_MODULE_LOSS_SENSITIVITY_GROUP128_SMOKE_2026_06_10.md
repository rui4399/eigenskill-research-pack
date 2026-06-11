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

- FP16 mean NLL: `2.988486`
- FP16 PPL: `19.855595`
- Tokens: `162`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9999 | {'4': 142, '8': 55} | 0.6802 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 5 | `model.layers.1.mlp.down_proj` | 13762560 | 0.124479 | 0.000000009045 |
| 10 | `model.layers.2.mlp.down_proj` | 13762560 | 0.089681 | 0.000000006516 |
| 57 | `lm_head` | 233373696 | 0.089317 | 0.000000000383 |
| 22 | `model.layers.26.mlp.down_proj` | 13762560 | 0.041009 | 0.000000002980 |
| 29 | `model.layers.26.mlp.up_proj` | 13762560 | 0.015561 | 0.000000001131 |
| 39 | `model.layers.3.mlp.down_proj` | 13762560 | 0.012376 | 0.000000000899 |
| 43 | `model.layers.1.mlp.up_proj` | 13762560 | 0.009713 | 0.000000000706 |
| 44 | `model.layers.25.mlp.down_proj` | 13762560 | 0.009343 | 0.000000000679 |
| 47 | `model.layers.19.mlp.down_proj` | 13762560 | 0.007933 | 0.000000000576 |
| 49 | `model.layers.27.mlp.up_proj` | 13762560 | 0.007311 | 0.000000000531 |
| 21 | `model.layers.19.self_attn.o_proj` | 2359296 | 0.007129 | 0.000000003022 |
| 53 | `model.layers.17.mlp.down_proj` | 13762560 | 0.006145 | 0.000000000446 |
| 23 | `model.layers.25.self_attn.o_proj` | 2359296 | 0.006126 | 0.000000002597 |
| 24 | `model.layers.16.self_attn.o_proj` | 2359296 | 0.006063 | 0.000000002570 |
| 54 | `model.layers.8.mlp.gate_proj` | 13762560 | 0.005853 | 0.000000000425 |
| 55 | `model.layers.18.mlp.gate_proj` | 13762560 | 0.005307 | 0.000000000386 |
| 58 | `model.layers.15.mlp.down_proj` | 13762560 | 0.005255 | 0.000000000382 |
| 59 | `model.layers.23.mlp.gate_proj` | 13762560 | 0.005110 | 0.000000000371 |
| 1 | `model.layers.21.self_attn.v_proj` | 393472 | 0.004533 | 0.000000011521 |
| 2 | `model.layers.9.self_attn.v_proj` | 393472 | 0.004438 | 0.000000011279 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
