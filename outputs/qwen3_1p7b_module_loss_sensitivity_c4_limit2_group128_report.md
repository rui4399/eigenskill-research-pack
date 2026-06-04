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

- FP16 mean NLL: `3.349737`
- FP16 PPL: `28.495250`
- Tokens: `254`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4973 | 0.9994 | {'8': 40, '4': 157} | 0.5099 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 102 | `lm_head` | 311164928 | 0.041510 | 0.000000000133 |
| 4 | `model.layers.27.mlp.down_proj` | 12582912 | 0.033298 | 0.000000002646 |
| 16 | `model.layers.1.mlp.down_proj` | 12582912 | 0.016134 | 0.000000001282 |
| 17 | `model.layers.16.mlp.up_proj` | 12582912 | 0.016128 | 0.000000001282 |
| 25 | `model.layers.6.mlp.up_proj` | 12582912 | 0.014021 | 0.000000001114 |
| 28 | `model.layers.15.mlp.up_proj` | 12582912 | 0.011510 | 0.000000000915 |
| 31 | `model.layers.23.mlp.up_proj` | 12582912 | 0.011206 | 0.000000000891 |
| 34 | `model.layers.11.mlp.up_proj` | 12582912 | 0.010763 | 0.000000000855 |
| 36 | `model.layers.21.mlp.down_proj` | 12582912 | 0.009757 | 0.000000000775 |
| 39 | `model.layers.14.mlp.up_proj` | 12582912 | 0.009389 | 0.000000000746 |
| 40 | `model.layers.21.mlp.gate_proj` | 12582912 | 0.009279 | 0.000000000737 |
| 43 | `model.layers.3.mlp.down_proj` | 12582912 | 0.008582 | 0.000000000682 |
| 47 | `model.layers.16.mlp.gate_proj` | 12582912 | 0.008326 | 0.000000000662 |
| 1 | `model.layers.5.self_attn.v_proj` | 2097152 | 0.008163 | 0.000000003892 |
| 49 | `model.layers.8.mlp.gate_proj` | 12582912 | 0.008127 | 0.000000000646 |
| 2 | `model.layers.20.self_attn.k_proj` | 2097152 | 0.008067 | 0.000000003847 |
| 3 | `model.layers.20.self_attn.v_proj` | 2097152 | 0.008005 | 0.000000003817 |
| 10 | `model.layers.16.self_attn.o_proj` | 4194304 | 0.007481 | 0.000000001784 |
| 11 | `model.layers.9.self_attn.o_proj` | 4194304 | 0.007198 | 0.000000001716 |
| 53 | `model.layers.11.mlp.gate_proj` | 12582912 | 0.007156 | 0.000000000569 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
