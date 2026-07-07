# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-7B-Instruct`
Prompts: `32`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.379809`
- FP16 PPL: `10.802841`
- Tokens: `3712`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9992 | 0.9997 | {'2': 104, '4': 93} | 0.9717 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 27 | `lm_head` | 544997376 | 0.081331 | 0.000000000149 |
| 21 | `model.layers.26.mlp.down_proj` | 67895296 | 0.016517 | 0.000000000243 |
| 34 | `model.layers.27.mlp.gate_proj` | 67895296 | 0.004568 | 0.000000000067 |
| 36 | `model.layers.27.mlp.up_proj` | 67895296 | 0.004197 | 0.000000000062 |
| 37 | `model.layers.26.mlp.up_proj` | 67895296 | 0.004125 | 0.000000000061 |
| 1 | `model.layers.27.self_attn.v_proj` | 1835520 | 0.003688 | 0.000000002009 |
| 39 | `model.layers.9.mlp.down_proj` | 67895296 | 0.003478 | 0.000000000051 |
| 41 | `model.layers.8.mlp.down_proj` | 67895296 | 0.003436 | 0.000000000051 |
| 42 | `model.layers.12.mlp.up_proj` | 67895296 | 0.003335 | 0.000000000049 |
| 46 | `model.layers.10.mlp.gate_proj` | 67895296 | 0.003105 | 0.000000000046 |
| 47 | `model.layers.4.mlp.up_proj` | 67895296 | 0.003087 | 0.000000000045 |
| 22 | `model.layers.19.self_attn.o_proj` | 12845056 | 0.002763 | 0.000000000215 |
| 49 | `model.layers.16.mlp.down_proj` | 67895296 | 0.002737 | 0.000000000040 |
| 51 | `model.layers.1.mlp.up_proj` | 67895296 | 0.002640 | 0.000000000039 |
| 52 | `model.layers.10.mlp.up_proj` | 67895296 | 0.002408 | 0.000000000035 |
| 54 | `model.layers.24.mlp.gate_proj` | 67895296 | 0.002358 | 0.000000000035 |
| 55 | `model.layers.23.mlp.up_proj` | 67895296 | 0.002294 | 0.000000000034 |
| 2 | `model.layers.15.self_attn.v_proj` | 1835520 | 0.002167 | 0.000000001180 |
| 3 | `model.layers.6.self_attn.v_proj` | 1835520 | 0.002088 | 0.000000001137 |
| 61 | `model.layers.11.mlp.gate_proj` | 67895296 | 0.001811 | 0.000000000027 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
