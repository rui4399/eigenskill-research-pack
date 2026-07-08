# Module Loss Sensitivity Report

Date: `2026-07-09`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `256`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.869138`
- FP16 PPL: `17.621815`
- Tokens: `23924`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9988 | 0.9996 | {'2': 100, '4': 97} | 0.9140 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 48 | `lm_head` | 233373696 | 0.091062 | 0.000000000390 |
| 5 | `model.layers.1.mlp.down_proj` | 13762560 | 0.062228 | 0.000000004522 |
| 14 | `model.layers.2.mlp.down_proj` | 13762560 | 0.035678 | 0.000000002592 |
| 15 | `model.layers.26.mlp.down_proj` | 13762560 | 0.035222 | 0.000000002559 |
| 37 | `model.layers.27.mlp.down_proj` | 13762560 | 0.010405 | 0.000000000756 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.006387 | 0.000000016234 |
| 46 | `model.layers.27.mlp.up_proj` | 13762560 | 0.005518 | 0.000000000401 |
| 47 | `model.layers.26.mlp.up_proj` | 13762560 | 0.005510 | 0.000000000400 |
| 51 | `model.layers.1.mlp.up_proj` | 13762560 | 0.005207 | 0.000000000378 |
| 54 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.005119 | 0.000000000372 |
| 55 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.005104 | 0.000000000371 |
| 24 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.003685 | 0.000000001562 |
| 25 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.003509 | 0.000000001487 |
| 63 | `model.layers.6.mlp.up_proj` | 13762560 | 0.003180 | 0.000000000231 |
| 64 | `model.layers.24.mlp.down_proj` | 13762560 | 0.003110 | 0.000000000226 |
| 66 | `model.layers.5.mlp.up_proj` | 13762560 | 0.002973 | 0.000000000216 |
| 69 | `model.layers.21.mlp.down_proj` | 13762560 | 0.002800 | 0.000000000203 |
| 70 | `model.layers.3.mlp.up_proj` | 13762560 | 0.002728 | 0.000000000198 |
| 71 | `model.layers.0.mlp.down_proj` | 13762560 | 0.002724 | 0.000000000198 |
| 72 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.002693 | 0.000000000196 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
