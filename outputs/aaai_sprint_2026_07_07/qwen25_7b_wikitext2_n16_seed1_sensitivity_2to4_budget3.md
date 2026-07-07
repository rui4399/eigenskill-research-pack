# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-7B-Instruct`
Prompts: `16`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.436589`
- FP16 PPL: `11.433976`
- Tokens: `1731`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9977 | 0.9992 | {'2': 107, '4': 90} | 0.9767 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 24 | `lm_head` | 544997376 | 0.085384 | 0.000000000157 |
| 21 | `model.layers.26.mlp.down_proj` | 67895296 | 0.016660 | 0.000000000245 |
| 30 | `model.layers.27.mlp.gate_proj` | 67895296 | 0.006376 | 0.000000000094 |
| 31 | `model.layers.26.mlp.up_proj` | 67895296 | 0.006352 | 0.000000000094 |
| 35 | `model.layers.9.mlp.down_proj` | 67895296 | 0.005481 | 0.000000000081 |
| 38 | `model.layers.9.mlp.gate_proj` | 67895296 | 0.005084 | 0.000000000075 |
| 39 | `model.layers.1.mlp.up_proj` | 67895296 | 0.004399 | 0.000000000065 |
| 40 | `model.layers.9.mlp.up_proj` | 67895296 | 0.004312 | 0.000000000064 |
| 44 | `model.layers.7.mlp.down_proj` | 67895296 | 0.003727 | 0.000000000055 |
| 1 | `model.layers.27.self_attn.v_proj` | 1835520 | 0.003131 | 0.000000001706 |
| 46 | `model.layers.7.mlp.gate_proj` | 67895296 | 0.003008 | 0.000000000044 |
| 47 | `model.layers.10.mlp.gate_proj` | 67895296 | 0.002951 | 0.000000000043 |
| 49 | `model.layers.27.mlp.down_proj` | 67895296 | 0.002842 | 0.000000000042 |
| 50 | `model.layers.2.mlp.gate_proj` | 67895296 | 0.002648 | 0.000000000039 |
| 51 | `model.layers.27.mlp.up_proj` | 67895296 | 0.002631 | 0.000000000039 |
| 53 | `model.layers.16.mlp.up_proj` | 67895296 | 0.002503 | 0.000000000037 |
| 54 | `model.layers.12.mlp.up_proj` | 67895296 | 0.002448 | 0.000000000036 |
| 55 | `model.layers.16.mlp.down_proj` | 67895296 | 0.002446 | 0.000000000036 |
| 2 | `model.layers.6.self_attn.v_proj` | 1835520 | 0.002366 | 0.000000001289 |
| 3 | `model.layers.5.self_attn.v_proj` | 1835520 | 0.002360 | 0.000000001286 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
