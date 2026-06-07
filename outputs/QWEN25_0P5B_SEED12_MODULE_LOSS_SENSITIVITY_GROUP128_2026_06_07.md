# Module Loss Sensitivity Report

Date: `2026-06-07`
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Prompts: `4`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `169 / 169`

## Baseline

- FP16 mean NLL: `3.216732`
- FP16 PPL: `24.946465`
- Tokens: `380`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 115, '8': 54} | 0.6334 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 80 | `lm_head` | 136134656 | 0.116478 | 0.000000000856 |
| 16 | `model.layers.21.mlp.down_proj` | 4358144 | 0.078442 | 0.000000017999 |
| 17 | `model.layers.2.mlp.down_proj` | 4358144 | 0.072935 | 0.000000016735 |
| 21 | `model.layers.3.mlp.down_proj` | 4358144 | 0.057166 | 0.000000013117 |
| 30 | `model.layers.23.mlp.down_proj` | 4358144 | 0.028856 | 0.000000006621 |
| 15 | `model.layers.23.self_attn.o_proj` | 802816 | 0.017565 | 0.000000021879 |
| 37 | `model.layers.23.mlp.up_proj` | 4358144 | 0.016945 | 0.000000003888 |
| 45 | `model.layers.1.mlp.up_proj` | 4358144 | 0.011694 | 0.000000002683 |
| 46 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.011226 | 0.000000002576 |
| 48 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.009508 | 0.000000002182 |
| 49 | `model.layers.8.mlp.up_proj` | 4358144 | 0.009094 | 0.000000002087 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.008835 | 0.000000076945 |
| 2 | `model.layers.15.self_attn.v_proj` | 114816 | 0.008274 | 0.000000072060 |
| 52 | `model.layers.20.mlp.up_proj` | 4358144 | 0.008187 | 0.000000001879 |
| 25 | `model.layers.0.self_attn.o_proj` | 802816 | 0.007728 | 0.000000009626 |
| 54 | `model.layers.19.mlp.gate_proj` | 4358144 | 0.007724 | 0.000000001772 |
| 55 | `model.layers.0.mlp.gate_proj` | 4358144 | 0.007580 | 0.000000001739 |
| 56 | `model.layers.14.mlp.gate_proj` | 4358144 | 0.007288 | 0.000000001672 |
| 3 | `model.layers.3.self_attn.v_proj` | 114816 | 0.006971 | 0.000000060712 |
| 57 | `model.layers.1.mlp.gate_proj` | 4358144 | 0.006909 | 0.000000001585 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
