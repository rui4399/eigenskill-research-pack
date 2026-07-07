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

- FP16 mean NLL: `2.650781`
- FP16 PPL: `14.165098`
- Tokens: `1731`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9988 | 0.9996 | {'4': 92, '2': 105} | 0.9336 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 62 | `lm_head` | 233373696 | 0.064563 | 0.000000000277 |
| 13 | `model.layers.1.mlp.down_proj` | 13762560 | 0.042577 | 0.000000003094 |
| 14 | `model.layers.2.mlp.down_proj` | 13762560 | 0.041212 | 0.000000002994 |
| 15 | `model.layers.26.mlp.down_proj` | 13762560 | 0.038602 | 0.000000002805 |
| 31 | `model.layers.27.mlp.down_proj` | 13762560 | 0.014766 | 0.000000001073 |
| 44 | `model.layers.26.mlp.up_proj` | 13762560 | 0.008297 | 0.000000000603 |
| 46 | `model.layers.1.mlp.up_proj` | 13762560 | 0.007035 | 0.000000000511 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.006030 | 0.000000015325 |
| 49 | `model.layers.3.mlp.up_proj` | 13762560 | 0.006019 | 0.000000000437 |
| 53 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.004800 | 0.000000000349 |
| 54 | `model.layers.25.mlp.down_proj` | 13762560 | 0.004656 | 0.000000000338 |
| 18 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.004593 | 0.000000001947 |
| 55 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.004227 | 0.000000000307 |
| 57 | `model.layers.11.mlp.up_proj` | 13762560 | 0.004055 | 0.000000000295 |
| 58 | `model.layers.5.mlp.up_proj` | 13762560 | 0.004001 | 0.000000000291 |
| 60 | `model.layers.20.mlp.up_proj` | 13762560 | 0.003945 | 0.000000000287 |
| 61 | `model.layers.4.mlp.up_proj` | 13762560 | 0.003837 | 0.000000000279 |
| 63 | `model.layers.23.mlp.up_proj` | 13762560 | 0.003504 | 0.000000000255 |
| 64 | `model.layers.9.mlp.up_proj` | 13762560 | 0.003449 | 0.000000000251 |
| 65 | `model.layers.0.mlp.up_proj` | 13762560 | 0.003182 | 0.000000000231 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
