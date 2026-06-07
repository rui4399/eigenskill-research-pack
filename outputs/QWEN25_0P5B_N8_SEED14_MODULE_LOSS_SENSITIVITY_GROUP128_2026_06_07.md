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

- FP16 mean NLL: `3.360604`
- FP16 PPL: `28.806587`
- Tokens: `724`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4951 | 0.9989 | {'4': 108, '8': 61} | 0.6851 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 19 | `model.layers.21.mlp.down_proj` | 4358144 | 0.089446 | 0.000000020524 |
| 92 | `lm_head` | 136134656 | 0.079647 | 0.000000000585 |
| 20 | `model.layers.2.mlp.down_proj` | 4358144 | 0.078904 | 0.000000018105 |
| 24 | `model.layers.3.mlp.down_proj` | 4358144 | 0.059016 | 0.000000013541 |
| 29 | `model.layers.23.mlp.down_proj` | 4358144 | 0.038791 | 0.000000008901 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.014572 | 0.000000126913 |
| 47 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.010845 | 0.000000002488 |
| 48 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.010332 | 0.000000002371 |
| 51 | `model.layers.1.mlp.up_proj` | 4358144 | 0.008902 | 0.000000002043 |
| 54 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.008488 | 0.000000001948 |
| 2 | `model.layers.0.self_attn.v_proj` | 114816 | 0.008420 | 0.000000073339 |
| 3 | `model.layers.15.self_attn.v_proj` | 114816 | 0.007965 | 0.000000069373 |
| 4 | `model.layers.12.self_attn.v_proj` | 114816 | 0.007353 | 0.000000064045 |
| 5 | `model.layers.3.self_attn.v_proj` | 114816 | 0.007085 | 0.000000061709 |
| 56 | `model.layers.16.mlp.down_proj` | 4358144 | 0.006800 | 0.000000001560 |
| 57 | `model.layers.22.mlp.down_proj` | 4358144 | 0.006609 | 0.000000001516 |
| 58 | `model.layers.11.mlp.up_proj` | 4358144 | 0.006410 | 0.000000001471 |
| 59 | `model.layers.1.mlp.gate_proj` | 4358144 | 0.006401 | 0.000000001469 |
| 6 | `model.layers.21.self_attn.v_proj` | 114816 | 0.006193 | 0.000000053939 |
| 61 | `model.layers.22.mlp.up_proj` | 4358144 | 0.006176 | 0.000000001417 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
