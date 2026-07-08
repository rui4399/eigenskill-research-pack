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

- FP16 mean NLL: `2.873024`
- FP16 PPL: `17.690441`
- Tokens: `24604`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9994 | 0.9998 | {'2': 99, '4': 98} | 0.9126 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 45 | `lm_head` | 233373696 | 0.088325 | 0.000000000378 |
| 6 | `model.layers.1.mlp.down_proj` | 13762560 | 0.061353 | 0.000000004458 |
| 17 | `model.layers.2.mlp.down_proj` | 13762560 | 0.032432 | 0.000000002357 |
| 18 | `model.layers.26.mlp.down_proj` | 13762560 | 0.031192 | 0.000000002266 |
| 37 | `model.layers.27.mlp.down_proj` | 13762560 | 0.009204 | 0.000000000669 |
| 42 | `model.layers.27.mlp.up_proj` | 13762560 | 0.005694 | 0.000000000414 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.005686 | 0.000000014451 |
| 43 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.005372 | 0.000000000390 |
| 44 | `model.layers.1.mlp.up_proj` | 13762560 | 0.005220 | 0.000000000379 |
| 20 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.004754 | 0.000000002015 |
| 21 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.004642 | 0.000000001968 |
| 53 | `model.layers.26.mlp.up_proj` | 13762560 | 0.004528 | 0.000000000329 |
| 55 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.004239 | 0.000000000308 |
| 56 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.003963 | 0.000000000288 |
| 57 | `model.layers.3.mlp.up_proj` | 13762560 | 0.003866 | 0.000000000281 |
| 58 | `model.layers.24.mlp.down_proj` | 13762560 | 0.003833 | 0.000000000278 |
| 63 | `model.layers.6.mlp.up_proj` | 13762560 | 0.003323 | 0.000000000241 |
| 65 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.002980 | 0.000000000217 |
| 66 | `model.layers.21.mlp.down_proj` | 13762560 | 0.002970 | 0.000000000216 |
| 68 | `model.layers.20.mlp.down_proj` | 13762560 | 0.002795 | 0.000000000203 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
