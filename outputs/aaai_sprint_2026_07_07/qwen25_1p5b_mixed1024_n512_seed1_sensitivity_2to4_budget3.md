# Module Loss Sensitivity Report

Date: `2026-07-10`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `512`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `3.019570`
- FP16 PPL: `20.482481`
- Tokens: `49404`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9999 | 1.0000 | {'4': 103, '2': 94} | 0.9224 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 42 | `lm_head` | 233373696 | 0.097618 | 0.000000000418 |
| 2 | `model.layers.1.mlp.down_proj` | 13762560 | 0.067338 | 0.000000004893 |
| 8 | `model.layers.26.mlp.down_proj` | 13762560 | 0.040327 | 0.000000002930 |
| 13 | `model.layers.2.mlp.down_proj` | 13762560 | 0.034206 | 0.000000002485 |
| 37 | `model.layers.26.mlp.up_proj` | 13762560 | 0.007927 | 0.000000000576 |
| 39 | `model.layers.27.mlp.down_proj` | 13762560 | 0.007662 | 0.000000000557 |
| 46 | `model.layers.27.mlp.up_proj` | 13762560 | 0.005357 | 0.000000000389 |
| 51 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.004310 | 0.000000000313 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.004072 | 0.000000010349 |
| 53 | `model.layers.1.mlp.up_proj` | 13762560 | 0.004053 | 0.000000000294 |
| 59 | `model.layers.3.mlp.up_proj` | 13762560 | 0.003067 | 0.000000000223 |
| 23 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.002953 | 0.000000001252 |
| 24 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.002882 | 0.000000001222 |
| 61 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.002562 | 0.000000000186 |
| 64 | `model.layers.24.mlp.down_proj` | 13762560 | 0.002268 | 0.000000000165 |
| 65 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.002254 | 0.000000000164 |
| 66 | `model.layers.6.mlp.up_proj` | 13762560 | 0.002184 | 0.000000000159 |
| 68 | `model.layers.23.mlp.down_proj` | 13762560 | 0.002131 | 0.000000000155 |
| 72 | `model.layers.5.mlp.up_proj` | 13762560 | 0.001943 | 0.000000000141 |
| 73 | `model.layers.22.mlp.up_proj` | 13762560 | 0.001911 | 0.000000000139 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
