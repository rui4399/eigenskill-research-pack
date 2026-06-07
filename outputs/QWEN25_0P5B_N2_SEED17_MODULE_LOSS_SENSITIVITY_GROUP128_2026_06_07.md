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

- FP16 mean NLL: `3.314442`
- FP16 PPL: `27.507039`
- Tokens: `190`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4969 | 0.9993 | {'4': 113, '8': 56} | 0.6045 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 79 | `lm_head` | 136134656 | 0.177090 | 0.000000001301 |
| 18 | `model.layers.21.mlp.down_proj` | 4358144 | 0.104687 | 0.000000024021 |
| 21 | `model.layers.3.mlp.down_proj` | 4358144 | 0.083264 | 0.000000019105 |
| 26 | `model.layers.2.mlp.down_proj` | 4358144 | 0.060485 | 0.000000013879 |
| 34 | `model.layers.23.mlp.down_proj` | 4358144 | 0.038841 | 0.000000008912 |
| 41 | `model.layers.23.mlp.up_proj` | 4358144 | 0.020392 | 0.000000004679 |
| 1 | `model.layers.0.self_attn.v_proj` | 114816 | 0.019817 | 0.000000172597 |
| 42 | `model.layers.7.mlp.up_proj` | 4358144 | 0.016615 | 0.000000003812 |
| 43 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.016436 | 0.000000003771 |
| 46 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.013781 | 0.000000003162 |
| 47 | `model.layers.8.mlp.up_proj` | 4358144 | 0.013395 | 0.000000003074 |
| 52 | `model.layers.16.mlp.down_proj` | 4358144 | 0.011316 | 0.000000002596 |
| 53 | `model.layers.19.mlp.gate_proj` | 4358144 | 0.011083 | 0.000000002543 |
| 2 | `model.layers.15.self_attn.v_proj` | 114816 | 0.010814 | 0.000000094186 |
| 56 | `model.layers.22.mlp.gate_proj` | 4358144 | 0.010104 | 0.000000002319 |
| 3 | `model.layers.12.self_attn.v_proj` | 114816 | 0.009995 | 0.000000087055 |
| 57 | `model.layers.2.mlp.gate_proj` | 4358144 | 0.009956 | 0.000000002284 |
| 58 | `model.layers.1.mlp.down_proj` | 4358144 | 0.009837 | 0.000000002257 |
| 59 | `model.layers.11.mlp.up_proj` | 4358144 | 0.009618 | 0.000000002207 |
| 60 | `model.layers.0.mlp.gate_proj` | 4358144 | 0.009390 | 0.000000002155 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
