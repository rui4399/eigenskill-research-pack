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

- FP16 mean NLL: `2.586432`
- FP16 PPL: `13.282299`
- Tokens: `7141`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9999 | 1.0000 | {'2': 99, '4': 98} | 0.9298 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 48 | `lm_head` | 233373696 | 0.091017 | 0.000000000390 |
| 3 | `model.layers.1.mlp.down_proj` | 13762560 | 0.052417 | 0.000000003809 |
| 12 | `model.layers.2.mlp.down_proj` | 13762560 | 0.034709 | 0.000000002522 |
| 13 | `model.layers.26.mlp.down_proj` | 13762560 | 0.031259 | 0.000000002271 |
| 32 | `model.layers.27.mlp.down_proj` | 13762560 | 0.010855 | 0.000000000789 |
| 34 | `model.layers.26.mlp.up_proj` | 13762560 | 0.008861 | 0.000000000644 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.007319 | 0.000000018602 |
| 40 | `model.layers.27.mlp.up_proj` | 13762560 | 0.006796 | 0.000000000494 |
| 45 | `model.layers.3.mlp.up_proj` | 13762560 | 0.006133 | 0.000000000446 |
| 49 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.005243 | 0.000000000381 |
| 54 | `model.layers.3.mlp.down_proj` | 13762560 | 0.004174 | 0.000000000303 |
| 56 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.004065 | 0.000000000295 |
| 60 | `model.layers.2.mlp.up_proj` | 13762560 | 0.003702 | 0.000000000269 |
| 22 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.003207 | 0.000000001359 |
| 61 | `model.layers.9.mlp.up_proj` | 13762560 | 0.003186 | 0.000000000231 |
| 24 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.002950 | 0.000000001250 |
| 65 | `model.layers.23.mlp.gate_proj` | 13762560 | 0.002707 | 0.000000000197 |
| 25 | `model.layers.26.self_attn.o_proj` | 2359296 | 0.002630 | 0.000000001115 |
| 67 | `model.layers.1.mlp.up_proj` | 13762560 | 0.002630 | 0.000000000191 |
| 68 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.002575 | 0.000000000187 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
