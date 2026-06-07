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

- FP16 mean NLL: `3.261722`
- FP16 PPL: `26.094420`
- Tokens: `724`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4960 | 0.9991 | {'4': 107, '8': 62} | 0.7236 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 18 | `model.layers.2.mlp.down_proj` | 4358144 | 0.098798 | 0.000000022670 |
| 20 | `model.layers.21.mlp.down_proj` | 4358144 | 0.085842 | 0.000000019697 |
| 22 | `model.layers.3.mlp.down_proj` | 4358144 | 0.079033 | 0.000000018135 |
| 95 | `lm_head` | 136134656 | 0.076096 | 0.000000000559 |
| 29 | `model.layers.23.mlp.down_proj` | 4358144 | 0.045812 | 0.000000010512 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.013139 | 0.000000114435 |
| 45 | `model.layers.22.mlp.down_proj` | 4358144 | 0.012051 | 0.000000002765 |
| 2 | `model.layers.12.self_attn.v_proj` | 114816 | 0.011561 | 0.000000100690 |
| 49 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.010815 | 0.000000002482 |
| 50 | `model.layers.23.mlp.up_proj` | 4358144 | 0.010531 | 0.000000002416 |
| 27 | `model.layers.1.self_attn.o_proj` | 802816 | 0.010200 | 0.000000012705 |
| 52 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.009634 | 0.000000002211 |
| 3 | `model.layers.10.self_attn.v_proj` | 114816 | 0.008898 | 0.000000077499 |
| 54 | `model.layers.14.mlp.up_proj` | 4358144 | 0.008049 | 0.000000001847 |
| 4 | `model.layers.21.self_attn.v_proj` | 114816 | 0.007550 | 0.000000065753 |
| 57 | `model.layers.1.mlp.up_proj` | 4358144 | 0.006942 | 0.000000001593 |
| 5 | `model.layers.4.self_attn.v_proj` | 114816 | 0.006916 | 0.000000060233 |
| 59 | `model.layers.6.mlp.gate_proj` | 4358144 | 0.006708 | 0.000000001539 |
| 6 | `model.layers.8.self_attn.v_proj` | 114816 | 0.006359 | 0.000000055381 |
| 62 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.006021 | 0.000000001381 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
