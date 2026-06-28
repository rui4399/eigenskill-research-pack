# Module Loss Sensitivity Report

Date: `2026-06-28`
Model: `/mnt/e/hf_cache/hub/models--HuggingFaceTB--SmolLM2-360M-Instruct/snapshots/a10cc1512eabd3dde888204e902eca88bddb4951`
Prompts: `16`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `225 / 225`

## Baseline

- FP16 mean NLL: `3.063194`
- FP16 PPL: `21.395781`
- Tokens: `1309`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 164, '8': 61} | 0.4843 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 28 | `lm_head` | 47185920 | 0.228469 | 0.000000004842 |
| 4 | `model.layers.31.mlp.down_proj` | 2457600 | 0.055261 | 0.000000022486 |
| 5 | `model.layers.30.mlp.up_proj` | 2457600 | 0.053823 | 0.000000021901 |
| 6 | `model.layers.3.mlp.down_proj` | 2457600 | 0.042030 | 0.000000017102 |
| 13 | `model.layers.31.mlp.up_proj` | 2457600 | 0.023721 | 0.000000009652 |
| 23 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.014966 | 0.000000006090 |
| 1 | `model.layers.24.self_attn.v_proj` | 307200 | 0.007744 | 0.000000025210 |
| 43 | `model.layers.2.mlp.down_proj` | 2457600 | 0.007358 | 0.000000002994 |
| 2 | `model.layers.23.self_attn.v_proj` | 307200 | 0.007279 | 0.000000023696 |
| 3 | `model.layers.0.self_attn.v_proj` | 307200 | 0.007140 | 0.000000023243 |
| 45 | `model.layers.27.mlp.down_proj` | 2457600 | 0.006825 | 0.000000002777 |
| 58 | `model.layers.24.mlp.gate_proj` | 2457600 | 0.005254 | 0.000000002138 |
| 25 | `model.layers.12.self_attn.q_proj` | 921600 | 0.004896 | 0.000000005312 |
| 7 | `model.layers.14.self_attn.v_proj` | 307200 | 0.004867 | 0.000000015844 |
| 61 | `model.layers.11.mlp.up_proj` | 2457600 | 0.004708 | 0.000000001916 |
| 65 | `model.layers.9.mlp.gate_proj` | 2457600 | 0.004390 | 0.000000001786 |
| 66 | `model.layers.12.mlp.up_proj` | 2457600 | 0.004352 | 0.000000001771 |
| 67 | `model.layers.8.mlp.gate_proj` | 2457600 | 0.004152 | 0.000000001689 |
| 8 | `model.layers.28.self_attn.v_proj` | 307200 | 0.003991 | 0.000000012992 |
| 70 | `model.layers.1.mlp.down_proj` | 2457600 | 0.003694 | 0.000000001503 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
