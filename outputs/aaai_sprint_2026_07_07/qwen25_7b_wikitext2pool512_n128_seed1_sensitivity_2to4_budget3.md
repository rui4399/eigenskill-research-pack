# Module Loss Sensitivity Report

Date: `2026-07-10`
Model: `E:\models\Qwen2.5-7B-Instruct`
Prompts: `128`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.683618`
- FP16 PPL: `14.637952`
- Tokens: `11368`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9997 | 0.9999 | {'2': 97, '4': 100} | 0.9586 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 26 | `lm_head` | 544997376 | 0.076000 | 0.000000000139 |
| 18 | `model.layers.26.mlp.down_proj` | 67895296 | 0.016341 | 0.000000000241 |
| 35 | `model.layers.1.mlp.up_proj` | 67895296 | 0.004641 | 0.000000000068 |
| 37 | `model.layers.9.mlp.down_proj` | 67895296 | 0.004430 | 0.000000000065 |
| 40 | `model.layers.27.mlp.gate_proj` | 67895296 | 0.004352 | 0.000000000064 |
| 41 | `model.layers.25.mlp.up_proj` | 67895296 | 0.004292 | 0.000000000063 |
| 43 | `model.layers.26.mlp.up_proj` | 67895296 | 0.004123 | 0.000000000061 |
| 44 | `model.layers.9.mlp.up_proj` | 67895296 | 0.004115 | 0.000000000061 |
| 50 | `model.layers.10.mlp.gate_proj` | 67895296 | 0.003721 | 0.000000000055 |
| 52 | `model.layers.5.mlp.up_proj` | 67895296 | 0.003381 | 0.000000000050 |
| 1 | `model.layers.27.self_attn.v_proj` | 1835520 | 0.003250 | 0.000000001771 |
| 54 | `model.layers.24.mlp.gate_proj` | 67895296 | 0.003207 | 0.000000000047 |
| 55 | `model.layers.10.mlp.up_proj` | 67895296 | 0.003183 | 0.000000000047 |
| 56 | `model.layers.4.mlp.up_proj` | 67895296 | 0.002920 | 0.000000000043 |
| 58 | `model.layers.3.mlp.down_proj` | 67895296 | 0.002460 | 0.000000000036 |
| 59 | `model.layers.16.mlp.down_proj` | 67895296 | 0.002418 | 0.000000000036 |
| 2 | `model.layers.9.self_attn.v_proj` | 1835520 | 0.002326 | 0.000000001267 |
| 62 | `model.layers.21.mlp.up_proj` | 67895296 | 0.002051 | 0.000000000030 |
| 63 | `model.layers.8.mlp.down_proj` | 67895296 | 0.002045 | 0.000000000030 |
| 67 | `model.layers.14.mlp.down_proj` | 67895296 | 0.001780 | 0.000000000026 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
