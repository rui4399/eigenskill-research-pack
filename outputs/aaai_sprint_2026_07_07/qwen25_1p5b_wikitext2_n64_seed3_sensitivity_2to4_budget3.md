# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `64`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.608150`
- FP16 PPL: `13.573915`
- Tokens: `6958`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9994 | 0.9998 | {'2': 95, '4': 102} | 0.9244 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 56 | `lm_head` | 233373696 | 0.083919 | 0.000000000360 |
| 7 | `model.layers.1.mlp.down_proj` | 13762560 | 0.060991 | 0.000000004432 |
| 17 | `model.layers.2.mlp.down_proj` | 13762560 | 0.037438 | 0.000000002720 |
| 20 | `model.layers.26.mlp.down_proj` | 13762560 | 0.026469 | 0.000000001923 |
| 35 | `model.layers.27.mlp.down_proj` | 13762560 | 0.011590 | 0.000000000842 |
| 45 | `model.layers.27.mlp.up_proj` | 13762560 | 0.007552 | 0.000000000549 |
| 51 | `model.layers.26.mlp.up_proj` | 13762560 | 0.005829 | 0.000000000424 |
| 54 | `model.layers.1.mlp.up_proj` | 13762560 | 0.005411 | 0.000000000393 |
| 59 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.004699 | 0.000000000341 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.004665 | 0.000000011857 |
| 60 | `model.layers.3.mlp.up_proj` | 13762560 | 0.004443 | 0.000000000323 |
| 64 | `model.layers.3.mlp.down_proj` | 13762560 | 0.004027 | 0.000000000293 |
| 66 | `model.layers.9.mlp.up_proj` | 13762560 | 0.003946 | 0.000000000287 |
| 69 | `model.layers.2.mlp.up_proj` | 13762560 | 0.003746 | 0.000000000272 |
| 71 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.003503 | 0.000000000255 |
| 72 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.003319 | 0.000000000241 |
| 74 | `model.layers.23.mlp.up_proj` | 13762560 | 0.003115 | 0.000000000226 |
| 75 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.003106 | 0.000000000226 |
| 78 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.002885 | 0.000000000210 |
| 79 | `model.layers.21.mlp.down_proj` | 13762560 | 0.002743 | 0.000000000199 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
