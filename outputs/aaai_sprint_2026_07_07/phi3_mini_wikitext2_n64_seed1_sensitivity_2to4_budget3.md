# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `microsoft/Phi-3-mini-4k-instruct`
Prompts: `64`
Max length: `128`
Quantized bits during probing: `2`
Group size: `128`
Status: `complete`
Measured modules: `129 / 129`

## Baseline

- FP16 mean NLL: `2.219588`
- FP16 PPL: `9.203539`
- Tokens: `7336`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 129} | 0.0000 |
| loss_sensitive_4to8 | 2.9994 | 0.9998 | {'2': 61, '4': 68} | 0.8815 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 1 | `lm_head` | 98500608 | 5.109147 | 0.000000051869 |
| 2 | `model.layers.31.mlp.down_proj` | 25165824 | 0.910613 | 0.000000036185 |
| 3 | `model.layers.31.mlp.gate_up_proj` | 50331648 | 0.527681 | 0.000000010484 |
| 6 | `model.layers.30.mlp.gate_up_proj` | 50331648 | 0.206618 | 0.000000004105 |
| 10 | `model.layers.29.mlp.gate_up_proj` | 50331648 | 0.162709 | 0.000000003233 |
| 7 | `model.layers.29.mlp.down_proj` | 25165824 | 0.101386 | 0.000000004029 |
| 23 | `model.layers.28.mlp.gate_up_proj` | 50331648 | 0.094133 | 0.000000001870 |
| 8 | `model.layers.30.mlp.down_proj` | 25165824 | 0.087964 | 0.000000003495 |
| 27 | `model.layers.7.mlp.gate_up_proj` | 50331648 | 0.087563 | 0.000000001740 |
| 9 | `model.layers.2.mlp.down_proj` | 25165824 | 0.084137 | 0.000000003343 |
| 37 | `model.layers.25.mlp.gate_up_proj` | 50331648 | 0.077518 | 0.000000001540 |
| 4 | `model.layers.31.self_attn.o_proj` | 9437184 | 0.072050 | 0.000000007635 |
| 46 | `model.layers.6.mlp.gate_up_proj` | 50331648 | 0.067154 | 0.000000001334 |
| 12 | `model.layers.4.mlp.down_proj` | 25165824 | 0.066418 | 0.000000002639 |
| 48 | `model.layers.26.mlp.gate_up_proj` | 50331648 | 0.065828 | 0.000000001308 |
| 50 | `model.layers.2.mlp.gate_up_proj` | 50331648 | 0.063407 | 0.000000001260 |
| 13 | `model.layers.25.mlp.down_proj` | 25165824 | 0.063159 | 0.000000002510 |
| 52 | `model.layers.4.mlp.gate_up_proj` | 50331648 | 0.061487 | 0.000000001222 |
| 54 | `model.layers.21.mlp.gate_up_proj` | 50331648 | 0.060882 | 0.000000001210 |
| 55 | `model.layers.27.mlp.gate_up_proj` | 50331648 | 0.060608 | 0.000000001204 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
