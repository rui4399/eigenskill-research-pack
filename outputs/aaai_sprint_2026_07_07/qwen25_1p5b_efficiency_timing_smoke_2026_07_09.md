# Module Loss Sensitivity Report

Date: `2026-07-09`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `4`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `1 / 1`

## Baseline

- FP16 mean NLL: `2.127065`
- FP16 PPL: `8.390202`
- Tokens: `401`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 1} | 0.0000 |
| loss_sensitive_4to8 | 2.0000 | 0.6667 | {'2': 1} | 0.0000 |

## Top 1 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 1 | `model.layers.0.self_attn.q_proj` | 2360832 | 0.000426 | 0.000000000181 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
