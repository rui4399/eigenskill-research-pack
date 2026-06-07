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

- FP16 mean NLL: `3.448577`
- FP16 PPL: `31.455608`
- Tokens: `344`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4988 | 0.9997 | {'8': 59, '4': 110} | 0.7028 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 19 | `model.layers.2.mlp.down_proj` | 4358144 | 0.108660 | 0.000000024933 |
| 77 | `lm_head` | 136134656 | 0.096369 | 0.000000000708 |
| 22 | `model.layers.3.mlp.down_proj` | 4358144 | 0.096083 | 0.000000022047 |
| 25 | `model.layers.21.mlp.down_proj` | 4358144 | 0.085046 | 0.000000019514 |
| 32 | `model.layers.23.mlp.down_proj` | 4358144 | 0.046588 | 0.000000010690 |
| 43 | `model.layers.23.mlp.up_proj` | 4358144 | 0.015151 | 0.000000003477 |
| 44 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.014852 | 0.000000003408 |
| 1 | `model.layers.8.self_attn.v_proj` | 114816 | 0.012095 | 0.000000105347 |
| 47 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.012089 | 0.000000002774 |
| 49 | `model.layers.14.mlp.up_proj` | 4358144 | 0.011056 | 0.000000002537 |
| 2 | `model.layers.12.self_attn.v_proj` | 114816 | 0.010759 | 0.000000093703 |
| 52 | `model.layers.22.mlp.down_proj` | 4358144 | 0.009870 | 0.000000002265 |
| 3 | `model.layers.16.self_attn.v_proj` | 114816 | 0.009217 | 0.000000080276 |
| 53 | `model.layers.7.mlp.up_proj` | 4358144 | 0.009100 | 0.000000002088 |
| 55 | `model.layers.1.mlp.down_proj` | 4358144 | 0.008598 | 0.000000001973 |
| 4 | `model.layers.10.self_attn.v_proj` | 114816 | 0.008595 | 0.000000074860 |
| 56 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.008095 | 0.000000001857 |
| 5 | `model.layers.4.self_attn.v_proj` | 114816 | 0.007811 | 0.000000068034 |
| 57 | `model.layers.8.mlp.gate_proj` | 4358144 | 0.007781 | 0.000000001785 |
| 58 | `model.layers.21.mlp.up_proj` | 4358144 | 0.007298 | 0.000000001675 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
