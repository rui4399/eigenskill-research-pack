# Module Loss Sensitivity Report

Date: `2026-07-07`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `64`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.522085`
- FP16 PPL: `12.454538`
- Tokens: `6986`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9999 | 1.0000 | {'2': 99, '4': 98} | 0.9217 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 49 | `lm_head` | 233373696 | 0.088720 | 0.000000000380 |
| 4 | `model.layers.1.mlp.down_proj` | 13762560 | 0.051770 | 0.000000003762 |
| 11 | `model.layers.26.mlp.down_proj` | 13762560 | 0.033434 | 0.000000002429 |
| 15 | `model.layers.2.mlp.down_proj` | 13762560 | 0.031078 | 0.000000002258 |
| 34 | `model.layers.27.mlp.down_proj` | 13762560 | 0.010134 | 0.000000000736 |
| 39 | `model.layers.26.mlp.up_proj` | 13762560 | 0.008129 | 0.000000000591 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.007413 | 0.000000018840 |
| 50 | `model.layers.1.mlp.up_proj` | 13762560 | 0.005226 | 0.000000000380 |
| 51 | `model.layers.27.mlp.up_proj` | 13762560 | 0.005107 | 0.000000000371 |
| 52 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.004695 | 0.000000000341 |
| 53 | `model.layers.3.mlp.up_proj` | 13762560 | 0.004664 | 0.000000000339 |
| 55 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.004496 | 0.000000000327 |
| 58 | `model.layers.3.mlp.down_proj` | 13762560 | 0.003759 | 0.000000000273 |
| 64 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.003324 | 0.000000000242 |
| 65 | `model.layers.23.mlp.gate_proj` | 13762560 | 0.003297 | 0.000000000240 |
| 26 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.002960 | 0.000000001255 |
| 70 | `model.layers.11.mlp.down_proj` | 13762560 | 0.002666 | 0.000000000194 |
| 71 | `model.layers.23.mlp.up_proj` | 13762560 | 0.002641 | 0.000000000192 |
| 29 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.002557 | 0.000000001084 |
| 73 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.002438 | 0.000000000177 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
