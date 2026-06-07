# Module Loss Sensitivity Report

Date: `2026-06-07`
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Prompts: `2`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `169 / 169`

## Baseline

- FP16 mean NLL: `3.556081`
- FP16 PPL: `35.025656`
- Tokens: `190`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4988 | 0.9997 | {'4': 110, '8': 59} | 0.6107 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 86 | `lm_head` | 136134656 | 0.142262 | 0.000000001045 |
| 21 | `model.layers.2.mlp.down_proj` | 4358144 | 0.087737 | 0.000000020132 |
| 22 | `model.layers.21.mlp.down_proj` | 4358144 | 0.087391 | 0.000000020052 |
| 32 | `model.layers.3.mlp.down_proj` | 4358144 | 0.033568 | 0.000000007702 |
| 37 | `model.layers.23.mlp.down_proj` | 4358144 | 0.020193 | 0.000000004633 |
| 42 | `model.layers.1.mlp.gate_proj` | 4358144 | 0.016739 | 0.000000003841 |
| 20 | `model.layers.23.self_attn.o_proj` | 802816 | 0.016435 | 0.000000020471 |
| 1 | `model.layers.4.self_attn.v_proj` | 114816 | 0.013974 | 0.000000121708 |
| 44 | `model.layers.11.mlp.up_proj` | 4358144 | 0.013915 | 0.000000003193 |
| 48 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.013355 | 0.000000003064 |
| 49 | `model.layers.18.mlp.gate_proj` | 4358144 | 0.013280 | 0.000000003047 |
| 50 | `model.layers.6.mlp.down_proj` | 4358144 | 0.013202 | 0.000000003029 |
| 53 | `model.layers.22.mlp.down_proj` | 4358144 | 0.012583 | 0.000000002887 |
| 2 | `model.layers.0.self_attn.v_proj` | 114816 | 0.012105 | 0.000000105434 |
| 3 | `model.layers.16.self_attn.v_proj` | 114816 | 0.012016 | 0.000000104656 |
| 56 | `model.layers.1.mlp.up_proj` | 4358144 | 0.011911 | 0.000000002733 |
| 4 | `model.layers.3.self_attn.v_proj` | 114816 | 0.011475 | 0.000000099943 |
| 58 | `model.layers.20.mlp.up_proj` | 4358144 | 0.010777 | 0.000000002473 |
| 59 | `model.layers.18.mlp.up_proj` | 4358144 | 0.010302 | 0.000000002364 |
| 5 | `model.layers.15.self_attn.v_proj` | 114816 | 0.010113 | 0.000000088082 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
