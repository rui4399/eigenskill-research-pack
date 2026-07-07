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

- FP16 mean NLL: `2.599175`
- FP16 PPL: `13.452628`
- Tokens: `7093`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9994 | 0.9998 | {'4': 106, '2': 91} | 0.9369 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 52 | `lm_head` | 233373696 | 0.090107 | 0.000000000386 |
| 6 | `model.layers.1.mlp.down_proj` | 13762560 | 0.066518 | 0.000000004833 |
| 18 | `model.layers.2.mlp.down_proj` | 13762560 | 0.032662 | 0.000000002373 |
| 22 | `model.layers.26.mlp.down_proj` | 13762560 | 0.028848 | 0.000000002096 |
| 36 | `model.layers.27.mlp.down_proj` | 13762560 | 0.010471 | 0.000000000761 |
| 42 | `model.layers.27.mlp.up_proj` | 13762560 | 0.008048 | 0.000000000585 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.005586 | 0.000000014197 |
| 51 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.005326 | 0.000000000387 |
| 58 | `model.layers.9.mlp.up_proj` | 13762560 | 0.004705 | 0.000000000342 |
| 60 | `model.layers.26.mlp.up_proj` | 13762560 | 0.004255 | 0.000000000309 |
| 61 | `model.layers.1.mlp.up_proj` | 13762560 | 0.003796 | 0.000000000276 |
| 64 | `model.layers.23.mlp.up_proj` | 13762560 | 0.003684 | 0.000000000268 |
| 65 | `model.layers.23.mlp.gate_proj` | 13762560 | 0.003618 | 0.000000000263 |
| 66 | `model.layers.3.mlp.up_proj` | 13762560 | 0.003614 | 0.000000000263 |
| 67 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.003565 | 0.000000000259 |
| 27 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.003412 | 0.000000001446 |
| 75 | `model.layers.11.mlp.down_proj` | 13762560 | 0.002778 | 0.000000000202 |
| 30 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.002775 | 0.000000001176 |
| 77 | `model.layers.4.mlp.up_proj` | 13762560 | 0.002715 | 0.000000000197 |
| 78 | `model.layers.6.mlp.gate_proj` | 13762560 | 0.002676 | 0.000000000194 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
