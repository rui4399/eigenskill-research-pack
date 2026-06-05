# Module Loss Sensitivity Report

Date: `2026-06-05`
Model: `Qwen/Qwen3-0.6B`
Prompts: `4`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `3.630492`
- FP16 PPL: `37.731388`
- Tokens: `508`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 156, '8': 41} | 0.5861 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 115 | `lm_head` | 155582464 | 0.036368 | 0.000000000234 |
| 3 | `model.layers.2.mlp.down_proj` | 3145728 | 0.027432 | 0.000000008721 |
| 1 | `model.layers.0.self_attn.v_proj` | 1048576 | 0.025032 | 0.000000023872 |
| 6 | `model.layers.27.mlp.down_proj` | 3145728 | 0.016744 | 0.000000005323 |
| 2 | `model.layers.2.self_attn.v_proj` | 1048576 | 0.013811 | 0.000000013172 |
| 5 | `model.layers.20.self_attn.q_proj` | 2097152 | 0.013157 | 0.000000006274 |
| 12 | `model.layers.20.mlp.up_proj` | 3145728 | 0.012492 | 0.000000003971 |
| 13 | `model.layers.26.mlp.up_proj` | 3145728 | 0.012153 | 0.000000003863 |
| 17 | `model.layers.4.mlp.gate_proj` | 3145728 | 0.010202 | 0.000000003243 |
| 19 | `model.layers.26.mlp.down_proj` | 3145728 | 0.009693 | 0.000000003081 |
| 21 | `model.layers.23.mlp.up_proj` | 3145728 | 0.008799 | 0.000000002797 |
| 23 | `model.layers.27.mlp.up_proj` | 3145728 | 0.008703 | 0.000000002767 |
| 26 | `model.layers.3.mlp.gate_proj` | 3145728 | 0.008493 | 0.000000002700 |
| 27 | `model.layers.7.mlp.up_proj` | 3145728 | 0.008265 | 0.000000002627 |
| 33 | `model.layers.3.mlp.up_proj` | 3145728 | 0.007879 | 0.000000002505 |
| 34 | `model.layers.7.mlp.gate_proj` | 3145728 | 0.007822 | 0.000000002486 |
| 36 | `model.layers.5.mlp.gate_proj` | 3145728 | 0.007604 | 0.000000002417 |
| 15 | `model.layers.26.self_attn.q_proj` | 2097152 | 0.007586 | 0.000000003617 |
| 4 | `model.layers.11.self_attn.k_proj` | 1048576 | 0.006872 | 0.000000006554 |
| 40 | `model.layers.1.mlp.gate_proj` | 3145728 | 0.006678 | 0.000000002123 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
