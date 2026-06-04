# Module Loss Sensitivity Report

Date: `2026-06-04`
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Prompts: `2`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`

## Baseline

- FP16 mean NLL: `2.054525`
- FP16 PPL: `7.803130`
- Tokens: `254`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4951 | 0.9989 | {'4': 114, '8': 55} | 0.6336 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 12 | `model.layers.2.mlp.down_proj` | 4358144 | 0.099780 | 0.000000022895 |
| 87 | `lm_head` | 136134656 | 0.073352 | 0.000000000539 |
| 25 | `model.layers.21.mlp.down_proj` | 4358144 | 0.044720 | 0.000000010261 |
| 31 | `model.layers.23.mlp.down_proj` | 4358144 | 0.026057 | 0.000000005979 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.018912 | 0.000000164715 |
| 37 | `model.layers.3.mlp.down_proj` | 4358144 | 0.018363 | 0.000000004214 |
| 40 | `model.layers.2.mlp.up_proj` | 4358144 | 0.016088 | 0.000000003691 |
| 41 | `model.layers.3.mlp.up_proj` | 4358144 | 0.015792 | 0.000000003624 |
| 42 | `model.layers.7.mlp.up_proj` | 4358144 | 0.015246 | 0.000000003498 |
| 2 | `model.layers.3.self_attn.v_proj` | 114816 | 0.015033 | 0.000000130933 |
| 17 | `model.layers.2.self_attn.o_proj` | 802816 | 0.013980 | 0.000000017414 |
| 47 | `model.layers.4.mlp.down_proj` | 4358144 | 0.012906 | 0.000000002961 |
| 50 | `model.layers.15.mlp.down_proj` | 4358144 | 0.011618 | 0.000000002666 |
| 3 | `model.layers.8.self_attn.v_proj` | 114816 | 0.010710 | 0.000000093283 |
| 52 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.010479 | 0.000000002405 |
| 53 | `model.layers.13.mlp.up_proj` | 4358144 | 0.010170 | 0.000000002334 |
| 54 | `model.layers.21.mlp.up_proj` | 4358144 | 0.009726 | 0.000000002232 |
| 55 | `model.layers.6.mlp.down_proj` | 4358144 | 0.009598 | 0.000000002202 |
| 56 | `model.layers.15.mlp.up_proj` | 4358144 | 0.009223 | 0.000000002116 |
| 58 | `model.layers.20.mlp.up_proj` | 4358144 | 0.008922 | 0.000000002047 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
