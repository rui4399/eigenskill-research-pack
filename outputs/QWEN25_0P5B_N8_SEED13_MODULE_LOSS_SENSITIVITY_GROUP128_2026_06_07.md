# Module Loss Sensitivity Report

Date: `2026-06-07`
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Prompts: `8`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `169 / 169`

## Baseline

- FP16 mean NLL: `3.196648`
- FP16 PPL: `24.450438`
- Tokens: `690`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 109, '8': 60} | 0.6957 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 12 | `model.layers.2.mlp.down_proj` | 4358144 | 0.105954 | 0.000000024312 |
| 15 | `model.layers.21.mlp.down_proj` | 4358144 | 0.086597 | 0.000000019870 |
| 90 | `lm_head` | 136134656 | 0.084636 | 0.000000000622 |
| 17 | `model.layers.3.mlp.down_proj` | 4358144 | 0.079927 | 0.000000018340 |
| 26 | `model.layers.23.mlp.down_proj` | 4358144 | 0.047380 | 0.000000010872 |
| 37 | `model.layers.23.mlp.up_proj` | 4358144 | 0.017914 | 0.000000004110 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.011245 | 0.000000097939 |
| 46 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.011195 | 0.000000002569 |
| 2 | `model.layers.10.self_attn.v_proj` | 114816 | 0.010705 | 0.000000093236 |
| 3 | `model.layers.12.self_attn.v_proj` | 114816 | 0.009668 | 0.000000084206 |
| 51 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.009416 | 0.000000002161 |
| 52 | `model.layers.7.mlp.up_proj` | 4358144 | 0.008548 | 0.000000001961 |
| 53 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.008447 | 0.000000001938 |
| 27 | `model.layers.23.self_attn.o_proj` | 802816 | 0.007638 | 0.000000009514 |
| 29 | `model.layers.12.self_attn.o_proj` | 802816 | 0.007461 | 0.000000009294 |
| 4 | `model.layers.8.self_attn.v_proj` | 114816 | 0.007348 | 0.000000063999 |
| 54 | `model.layers.1.mlp.up_proj` | 4358144 | 0.007197 | 0.000000001651 |
| 56 | `model.layers.20.mlp.up_proj` | 4358144 | 0.007064 | 0.000000001621 |
| 57 | `model.layers.22.mlp.down_proj` | 4358144 | 0.006650 | 0.000000001526 |
| 5 | `model.layers.3.self_attn.v_proj` | 114816 | 0.006639 | 0.000000057824 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
