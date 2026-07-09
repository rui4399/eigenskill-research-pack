# Module Loss Sensitivity Report

Date: `2026-07-09`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `512`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.904368`
- FP16 PPL: `18.253712`
- Tokens: `48478`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9988 | 0.9996 | {'2': 100, '4': 97} | 0.9136 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 53 | `lm_head` | 233373696 | 0.090609 | 0.000000000388 |
| 5 | `model.layers.1.mlp.down_proj` | 13762560 | 0.063650 | 0.000000004625 |
| 15 | `model.layers.2.mlp.down_proj` | 13762560 | 0.033499 | 0.000000002434 |
| 17 | `model.layers.26.mlp.down_proj` | 13762560 | 0.032845 | 0.000000002387 |
| 37 | `model.layers.27.mlp.down_proj` | 13762560 | 0.009651 | 0.000000000701 |
| 47 | `model.layers.26.mlp.up_proj` | 13762560 | 0.006131 | 0.000000000445 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.005887 | 0.000000014962 |
| 50 | `model.layers.27.mlp.up_proj` | 13762560 | 0.005752 | 0.000000000418 |
| 51 | `model.layers.1.mlp.up_proj` | 13762560 | 0.005717 | 0.000000000415 |
| 54 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.005311 | 0.000000000386 |
| 57 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.004109 | 0.000000000299 |
| 24 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.003997 | 0.000000001694 |
| 25 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.003717 | 0.000000001576 |
| 61 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.003533 | 0.000000000257 |
| 65 | `model.layers.3.mlp.up_proj` | 13762560 | 0.003463 | 0.000000000252 |
| 67 | `model.layers.24.mlp.down_proj` | 13762560 | 0.003258 | 0.000000000237 |
| 68 | `model.layers.6.mlp.up_proj` | 13762560 | 0.003102 | 0.000000000225 |
| 69 | `model.layers.3.mlp.down_proj` | 13762560 | 0.002921 | 0.000000000212 |
| 72 | `model.layers.21.mlp.down_proj` | 13762560 | 0.002649 | 0.000000000192 |
| 74 | `model.layers.20.mlp.down_proj` | 13762560 | 0.002410 | 0.000000000175 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
