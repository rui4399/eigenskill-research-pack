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

- FP16 mean NLL: `3.001283`
- FP16 PPL: `20.111321`
- Tokens: `49966`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9999 | 1.0000 | {'4': 103, '2': 94} | 0.9238 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 42 | `lm_head` | 233373696 | 0.097591 | 0.000000000418 |
| 2 | `model.layers.1.mlp.down_proj` | 13762560 | 0.071658 | 0.000000005207 |
| 8 | `model.layers.26.mlp.down_proj` | 13762560 | 0.038836 | 0.000000002822 |
| 12 | `model.layers.2.mlp.down_proj` | 13762560 | 0.033759 | 0.000000002453 |
| 34 | `model.layers.26.mlp.up_proj` | 13762560 | 0.007898 | 0.000000000574 |
| 37 | `model.layers.27.mlp.down_proj` | 13762560 | 0.006757 | 0.000000000491 |
| 45 | `model.layers.27.mlp.up_proj` | 13762560 | 0.005182 | 0.000000000377 |
| 46 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.005106 | 0.000000000371 |
| 50 | `model.layers.1.mlp.up_proj` | 13762560 | 0.004210 | 0.000000000306 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.003787 | 0.000000009624 |
| 22 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.002532 | 0.000000001073 |
| 63 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.002423 | 0.000000000176 |
| 65 | `model.layers.23.mlp.down_proj` | 13762560 | 0.002325 | 0.000000000169 |
| 66 | `model.layers.3.mlp.up_proj` | 13762560 | 0.002227 | 0.000000000162 |
| 67 | `model.layers.24.mlp.down_proj` | 13762560 | 0.002189 | 0.000000000159 |
| 26 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.002161 | 0.000000000916 |
| 70 | `model.layers.21.mlp.down_proj` | 13762560 | 0.002036 | 0.000000000148 |
| 72 | `model.layers.5.mlp.up_proj` | 13762560 | 0.002001 | 0.000000000145 |
| 74 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.001938 | 0.000000000141 |
| 75 | `model.layers.23.mlp.up_proj` | 13762560 | 0.001926 | 0.000000000140 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
