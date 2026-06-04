# Module Loss Sensitivity Report

Date: `2026-06-05`
Model: `Qwen/Qwen3-1.7B`
Prompts: `2`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.308958`
- FP16 PPL: `10.063937`
- Tokens: `254`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4973 | 0.9994 | {'4': 153, '8': 44} | 0.6048 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 107 | `lm_head` | 311164928 | 0.038784 | 0.000000000125 |
| 21 | `model.layers.7.mlp.gate_proj` | 12582912 | 0.021073 | 0.000000001675 |
| 1 | `model.layers.20.self_attn.k_proj` | 2097152 | 0.020324 | 0.000000009691 |
| 25 | `model.layers.4.mlp.down_proj` | 12582912 | 0.019855 | 0.000000001578 |
| 26 | `model.layers.6.mlp.up_proj` | 12582912 | 0.019579 | 0.000000001556 |
| 28 | `model.layers.2.mlp.gate_proj` | 12582912 | 0.018229 | 0.000000001449 |
| 30 | `model.layers.7.mlp.up_proj` | 12582912 | 0.017087 | 0.000000001358 |
| 31 | `model.layers.20.mlp.up_proj` | 12582912 | 0.016948 | 0.000000001347 |
| 2 | `model.layers.16.self_attn.v_proj` | 2097152 | 0.015543 | 0.000000007412 |
| 35 | `model.layers.17.mlp.up_proj` | 12582912 | 0.014162 | 0.000000001126 |
| 3 | `model.layers.9.self_attn.v_proj` | 2097152 | 0.013018 | 0.000000006208 |
| 38 | `model.layers.4.mlp.gate_proj` | 12582912 | 0.012813 | 0.000000001018 |
| 39 | `model.layers.19.mlp.gate_proj` | 12582912 | 0.012740 | 0.000000001012 |
| 4 | `model.layers.6.self_attn.v_proj` | 2097152 | 0.012337 | 0.000000005883 |
| 41 | `model.layers.8.mlp.down_proj` | 12582912 | 0.011888 | 0.000000000945 |
| 13 | `model.layers.6.self_attn.o_proj` | 4194304 | 0.009570 | 0.000000002282 |
| 5 | `model.layers.17.self_attn.v_proj` | 2097152 | 0.009556 | 0.000000004557 |
| 14 | `model.layers.1.self_attn.o_proj` | 4194304 | 0.009535 | 0.000000002273 |
| 47 | `model.layers.23.mlp.down_proj` | 12582912 | 0.008884 | 0.000000000706 |
| 48 | `model.layers.11.mlp.down_proj` | 12582912 | 0.008724 | 0.000000000693 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
