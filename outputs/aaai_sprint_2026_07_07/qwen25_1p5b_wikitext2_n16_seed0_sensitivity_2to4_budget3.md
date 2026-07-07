# Module Loss Sensitivity Report

Date: `2026-07-07`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `16`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.583625`
- FP16 PPL: `13.245068`
- Tokens: `1866`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9984 | 0.9995 | {'2': 93, '4': 104} | 0.9292 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 5 | `model.layers.1.mlp.down_proj` | 13762560 | 0.078001 | 0.000000005668 |
| 58 | `lm_head` | 233373696 | 0.075081 | 0.000000000322 |
| 24 | `model.layers.26.mlp.down_proj` | 13762560 | 0.026430 | 0.000000001920 |
| 25 | `model.layers.2.mlp.down_proj` | 13762560 | 0.024998 | 0.000000001816 |
| 37 | `model.layers.27.mlp.down_proj` | 13762560 | 0.012587 | 0.000000000915 |
| 43 | `model.layers.27.mlp.up_proj` | 13762560 | 0.008483 | 0.000000000616 |
| 63 | `model.layers.26.mlp.up_proj` | 13762560 | 0.003629 | 0.000000000264 |
| 1 | `model.layers.4.self_attn.v_proj` | 393472 | 0.003392 | 0.000000008621 |
| 64 | `model.layers.9.mlp.up_proj` | 13762560 | 0.003351 | 0.000000000244 |
| 31 | `model.layers.26.self_attn.o_proj` | 2359296 | 0.003313 | 0.000000001404 |
| 65 | `model.layers.9.mlp.down_proj` | 13762560 | 0.003287 | 0.000000000239 |
| 68 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.003153 | 0.000000000229 |
| 70 | `model.layers.5.mlp.up_proj` | 13762560 | 0.003075 | 0.000000000223 |
| 72 | `model.layers.3.mlp.down_proj` | 13762560 | 0.002922 | 0.000000000212 |
| 73 | `model.layers.23.mlp.up_proj` | 13762560 | 0.002920 | 0.000000000212 |
| 74 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.002905 | 0.000000000211 |
| 75 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.002855 | 0.000000000207 |
| 78 | `model.layers.20.mlp.up_proj` | 13762560 | 0.002710 | 0.000000000197 |
| 79 | `model.layers.21.mlp.down_proj` | 13762560 | 0.002658 | 0.000000000193 |
| 2 | `model.layers.2.self_attn.k_proj` | 393472 | 0.002567 | 0.000000006524 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
