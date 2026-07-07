# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-3B-Instruct`
Prompts: `64`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `253 / 253`

## Baseline

- FP16 mean NLL: `2.462818`
- FP16 PPL: `11.737845`
- Tokens: `6986`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int3 | 3.0000 | 0.8571 | {'3': 253} | 0.0000 |
| loss_sensitive_4to8 | 3.4998 | 0.9999 | {'4': 130, '3': 123} | 0.9467 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 1 | `model.layers.1.mlp.gate_proj` | 22544384 | 0.188649 | 0.000000008368 |
| 8 | `model.layers.30.mlp.down_proj` | 22544384 | 0.064272 | 0.000000002851 |
| 63 | `lm_head` | 311164928 | 0.060818 | 0.000000000195 |
| 20 | `model.layers.2.mlp.down_proj` | 22544384 | 0.035914 | 0.000000001593 |
| 36 | `model.layers.35.mlp.down_proj` | 22544384 | 0.011238 | 0.000000000498 |
| 46 | `model.layers.3.mlp.down_proj` | 22544384 | 0.007279 | 0.000000000323 |
| 50 | `model.layers.35.mlp.gate_proj` | 22544384 | 0.006191 | 0.000000000275 |
| 55 | `model.layers.11.mlp.down_proj` | 22544384 | 0.005264 | 0.000000000233 |
| 56 | `model.layers.7.mlp.up_proj` | 22544384 | 0.005203 | 0.000000000231 |
| 62 | `model.layers.30.mlp.gate_proj` | 22544384 | 0.004478 | 0.000000000199 |
| 64 | `model.layers.30.mlp.up_proj` | 22544384 | 0.004232 | 0.000000000188 |
| 66 | `model.layers.6.mlp.up_proj` | 22544384 | 0.003879 | 0.000000000172 |
| 2 | `model.layers.0.self_attn.v_proj` | 524544 | 0.003828 | 0.000000007298 |
| 27 | `model.layers.1.self_attn.o_proj` | 4194304 | 0.003310 | 0.000000000789 |
| 72 | `model.layers.8.mlp.down_proj` | 22544384 | 0.003287 | 0.000000000146 |
| 74 | `model.layers.8.mlp.gate_proj` | 22544384 | 0.003182 | 0.000000000141 |
| 3 | `model.layers.25.self_attn.v_proj` | 524544 | 0.003169 | 0.000000006042 |
| 75 | `model.layers.9.mlp.down_proj` | 22544384 | 0.003087 | 0.000000000137 |
| 76 | `model.layers.5.mlp.up_proj` | 22544384 | 0.003087 | 0.000000000137 |
| 77 | `model.layers.35.mlp.up_proj` | 22544384 | 0.003083 | 0.000000000137 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
