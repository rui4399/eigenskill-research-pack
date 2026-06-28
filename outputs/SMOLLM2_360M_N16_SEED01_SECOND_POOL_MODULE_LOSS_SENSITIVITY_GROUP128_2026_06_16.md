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

- FP16 mean NLL: `2.977983`
- FP16 PPL: `19.648139`
- Tokens: `1325`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 167, '8': 58} | 0.4911 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 30 | `lm_head` | 47185920 | 0.200642 | 0.000000004252 |
| 5 | `model.layers.31.mlp.down_proj` | 2457600 | 0.053551 | 0.000000021790 |
| 7 | `model.layers.30.mlp.up_proj` | 2457600 | 0.051606 | 0.000000020999 |
| 9 | `model.layers.3.mlp.down_proj` | 2457600 | 0.039920 | 0.000000016243 |
| 23 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.014178 | 0.000000005769 |
| 27 | `model.layers.31.mlp.up_proj` | 2457600 | 0.012588 | 0.000000005122 |
| 1 | `model.layers.24.self_attn.v_proj` | 307200 | 0.009632 | 0.000000031354 |
| 2 | `model.layers.23.self_attn.v_proj` | 307200 | 0.008026 | 0.000000026127 |
| 3 | `model.layers.0.self_attn.v_proj` | 307200 | 0.008013 | 0.000000026083 |
| 4 | `model.layers.2.self_attn.v_proj` | 307200 | 0.006823 | 0.000000022211 |
| 6 | `model.layers.1.self_attn.v_proj` | 307200 | 0.006679 | 0.000000021743 |
| 8 | `model.layers.14.self_attn.v_proj` | 307200 | 0.005304 | 0.000000017267 |
| 46 | `model.layers.28.mlp.gate_proj` | 2457600 | 0.004873 | 0.000000001983 |
| 48 | `model.layers.13.mlp.down_proj` | 2457600 | 0.004768 | 0.000000001940 |
| 10 | `model.layers.28.self_attn.v_proj` | 307200 | 0.004680 | 0.000000015234 |
| 11 | `model.layers.22.self_attn.v_proj` | 307200 | 0.004492 | 0.000000014623 |
| 12 | `model.layers.29.self_attn.v_proj` | 307200 | 0.004459 | 0.000000014515 |
| 29 | `model.layers.12.self_attn.q_proj` | 921600 | 0.004434 | 0.000000004812 |
| 52 | `model.layers.24.mlp.gate_proj` | 2457600 | 0.004319 | 0.000000001757 |
| 13 | `model.layers.27.self_attn.v_proj` | 307200 | 0.003946 | 0.000000012846 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
