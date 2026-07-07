# Module Loss Sensitivity Report

Date: `2026-07-07`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `32`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.534301`
- FP16 PPL: `12.607617`
- Tokens: `3712`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9994 | 0.9998 | {'2': 96, '4': 101} | 0.9266 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 46 | `lm_head` | 233373696 | 0.094778 | 0.000000000406 |
| 7 | `model.layers.1.mlp.down_proj` | 13762560 | 0.052131 | 0.000000003788 |
| 14 | `model.layers.26.mlp.down_proj` | 13762560 | 0.034020 | 0.000000002472 |
| 17 | `model.layers.2.mlp.down_proj` | 13762560 | 0.030924 | 0.000000002247 |
| 30 | `model.layers.27.mlp.down_proj` | 13762560 | 0.012456 | 0.000000000905 |
| 37 | `model.layers.26.mlp.up_proj` | 13762560 | 0.008958 | 0.000000000651 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.008246 | 0.000000020956 |
| 45 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.005594 | 0.000000000406 |
| 15 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.005530 | 0.000000002344 |
| 52 | `model.layers.27.mlp.up_proj` | 13762560 | 0.004495 | 0.000000000327 |
| 58 | `model.layers.3.mlp.down_proj` | 13762560 | 0.004124 | 0.000000000300 |
| 60 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.003951 | 0.000000000287 |
| 61 | `model.layers.2.mlp.up_proj` | 13762560 | 0.003876 | 0.000000000282 |
| 63 | `model.layers.9.mlp.up_proj` | 13762560 | 0.003037 | 0.000000000221 |
| 64 | `model.layers.21.mlp.down_proj` | 13762560 | 0.002983 | 0.000000000217 |
| 66 | `model.layers.1.mlp.up_proj` | 13762560 | 0.002921 | 0.000000000212 |
| 67 | `model.layers.0.mlp.gate_proj` | 13762560 | 0.002883 | 0.000000000209 |
| 26 | `model.layers.26.self_attn.o_proj` | 2359296 | 0.002743 | 0.000000001163 |
| 27 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.002688 | 0.000000001139 |
| 69 | `model.layers.22.mlp.up_proj` | 13762560 | 0.002651 | 0.000000000193 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
