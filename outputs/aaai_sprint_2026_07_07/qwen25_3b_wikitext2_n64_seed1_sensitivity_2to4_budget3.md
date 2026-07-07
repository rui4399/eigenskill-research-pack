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

- FP16 mean NLL: `2.505868`
- FP16 PPL: `12.254187`
- Tokens: `7141`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 253} | 0.0000 |
| loss_sensitive_4to8 | 2.9996 | 0.9999 | {'4': 130, '2': 123} | 0.9471 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 3 | `model.layers.1.mlp.gate_proj` | 22544384 | 0.152363 | 0.000000006758 |
| 10 | `model.layers.30.mlp.down_proj` | 22544384 | 0.061981 | 0.000000002749 |
| 62 | `lm_head` | 311164928 | 0.060343 | 0.000000000194 |
| 15 | `model.layers.2.mlp.down_proj` | 22544384 | 0.046001 | 0.000000002040 |
| 41 | `model.layers.35.mlp.down_proj` | 22544384 | 0.009128 | 0.000000000405 |
| 50 | `model.layers.3.mlp.down_proj` | 22544384 | 0.006786 | 0.000000000301 |
| 55 | `model.layers.30.mlp.up_proj` | 22544384 | 0.005365 | 0.000000000238 |
| 59 | `model.layers.8.mlp.down_proj` | 22544384 | 0.004631 | 0.000000000205 |
| 61 | `model.layers.35.mlp.gate_proj` | 22544384 | 0.004377 | 0.000000000194 |
| 65 | `model.layers.35.mlp.up_proj` | 22544384 | 0.004153 | 0.000000000184 |
| 1 | `model.layers.25.self_attn.v_proj` | 524544 | 0.004101 | 0.000000007819 |
| 2 | `model.layers.0.self_attn.v_proj` | 524544 | 0.004009 | 0.000000007642 |
| 66 | `model.layers.7.mlp.up_proj` | 22544384 | 0.003945 | 0.000000000175 |
| 69 | `model.layers.11.mlp.down_proj` | 22544384 | 0.003824 | 0.000000000170 |
| 71 | `model.layers.30.mlp.gate_proj` | 22544384 | 0.003507 | 0.000000000156 |
| 27 | `model.layers.0.self_attn.o_proj` | 4194304 | 0.003434 | 0.000000000819 |
| 72 | `model.layers.3.mlp.up_proj` | 22544384 | 0.003376 | 0.000000000150 |
| 76 | `model.layers.15.mlp.down_proj` | 22544384 | 0.003261 | 0.000000000145 |
| 78 | `model.layers.5.mlp.up_proj` | 22544384 | 0.003189 | 0.000000000141 |
| 80 | `model.layers.9.mlp.down_proj` | 22544384 | 0.002907 | 0.000000000129 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
