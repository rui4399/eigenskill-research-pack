# Module Loss Sensitivity Report

Date: `2026-06-05`
Model: `Qwen/Qwen3-0.6B`
Prompts: `4`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`

## Baseline

- FP16 mean NLL: `3.059937`
- FP16 PPL: `21.326212`
- Tokens: `401`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 158, '8': 39} | 0.5787 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 1 | `model.layers.27.mlp.down_proj` | 3145728 | 0.035792 | 0.000000011378 |
| 8 | `model.layers.2.mlp.gate_proj` | 3145728 | 0.024472 | 0.000000007779 |
| 9 | `model.layers.18.mlp.up_proj` | 3145728 | 0.021587 | 0.000000006862 |
| 13 | `model.layers.17.mlp.up_proj` | 3145728 | 0.018535 | 0.000000005892 |
| 14 | `model.layers.0.mlp.down_proj` | 3145728 | 0.017831 | 0.000000005668 |
| 15 | `model.layers.1.mlp.down_proj` | 3145728 | 0.017605 | 0.000000005597 |
| 17 | `model.layers.26.mlp.up_proj` | 3145728 | 0.017270 | 0.000000005490 |
| 18 | `model.layers.16.mlp.down_proj` | 3145728 | 0.016733 | 0.000000005319 |
| 20 | `model.layers.2.mlp.up_proj` | 3145728 | 0.016251 | 0.000000005166 |
| 25 | `model.layers.1.mlp.gate_proj` | 3145728 | 0.014043 | 0.000000004464 |
| 32 | `model.layers.8.mlp.up_proj` | 3145728 | 0.012911 | 0.000000004104 |
| 2 | `model.layers.17.self_attn.v_proj` | 1048576 | 0.011632 | 0.000000011093 |
| 36 | `model.layers.2.mlp.down_proj` | 3145728 | 0.011591 | 0.000000003685 |
| 3 | `model.layers.0.self_attn.v_proj` | 1048576 | 0.011557 | 0.000000011021 |
| 37 | `model.layers.24.mlp.up_proj` | 3145728 | 0.011412 | 0.000000003628 |
| 38 | `model.layers.26.mlp.down_proj` | 3145728 | 0.011257 | 0.000000003578 |
| 44 | `model.layers.3.mlp.up_proj` | 3145728 | 0.010030 | 0.000000003189 |
| 4 | `model.layers.4.self_attn.k_proj` | 1048576 | 0.010023 | 0.000000009559 |
| 23 | `model.layers.20.self_attn.q_proj` | 2097152 | 0.009702 | 0.000000004627 |
| 5 | `model.layers.11.self_attn.v_proj` | 1048576 | 0.009675 | 0.000000009227 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
