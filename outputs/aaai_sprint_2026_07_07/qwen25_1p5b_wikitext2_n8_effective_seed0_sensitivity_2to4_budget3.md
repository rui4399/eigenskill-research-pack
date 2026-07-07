# Module Loss Sensitivity Report

Date: `2026-07-07`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `8`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `3.201212`
- FP16 PPL: `24.562270`
- Tokens: `745`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9999 | 1.0000 | {'2': 104, '4': 93} | 0.9620 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 46 | `lm_head` | 233373696 | 0.131738 | 0.000000000564 |
| 17 | `model.layers.1.mlp.down_proj` | 13762560 | 0.037001 | 0.000000002689 |
| 19 | `model.layers.2.mlp.down_proj` | 13762560 | 0.032674 | 0.000000002374 |
| 22 | `model.layers.26.mlp.down_proj` | 13762560 | 0.029871 | 0.000000002170 |
| 28 | `model.layers.27.mlp.down_proj` | 13762560 | 0.019755 | 0.000000001435 |
| 38 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.009494 | 0.000000000690 |
| 42 | `model.layers.4.mlp.down_proj` | 13762560 | 0.008673 | 0.000000000630 |
| 43 | `model.layers.6.mlp.up_proj` | 13762560 | 0.008582 | 0.000000000624 |
| 48 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.007588 | 0.000000000551 |
| 49 | `model.layers.1.mlp.up_proj` | 13762560 | 0.007262 | 0.000000000528 |
| 51 | `model.layers.21.mlp.down_proj` | 13762560 | 0.006785 | 0.000000000493 |
| 52 | `model.layers.3.mlp.down_proj` | 13762560 | 0.006518 | 0.000000000474 |
| 54 | `model.layers.27.mlp.up_proj` | 13762560 | 0.005952 | 0.000000000432 |
| 57 | `model.layers.23.mlp.gate_proj` | 13762560 | 0.005529 | 0.000000000402 |
| 59 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.005129 | 0.000000000373 |
| 23 | `model.layers.25.self_attn.o_proj` | 2359296 | 0.004972 | 0.000000002108 |
| 62 | `model.layers.16.mlp.down_proj` | 13762560 | 0.004751 | 0.000000000345 |
| 1 | `model.layers.17.self_attn.v_proj` | 393472 | 0.004637 | 0.000000011785 |
| 24 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.004618 | 0.000000001957 |
| 2 | `model.layers.3.self_attn.v_proj` | 393472 | 0.004448 | 0.000000011306 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
