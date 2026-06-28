# Module Loss Sensitivity Report

Date: `2026-06-16`
Model: `/mnt/e/hf_cache/hub/models--HuggingFaceTB--SmolLM2-360M-Instruct/snapshots/a10cc1512eabd3dde888204e902eca88bddb4951`
Prompts: `4`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `225 / 225`

## Baseline

- FP16 mean NLL: `2.851233`
- FP16 PPL: `17.309103`
- Tokens: `359`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 168, '8': 57} | 0.4526 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 35 | `lm_head` | 47185920 | 0.223525 | 0.000000004737 |
| 7 | `model.layers.31.mlp.down_proj` | 2457600 | 0.047691 | 0.000000019405 |
| 11 | `model.layers.3.mlp.down_proj` | 2457600 | 0.042244 | 0.000000017189 |
| 18 | `model.layers.30.mlp.up_proj` | 2457600 | 0.028502 | 0.000000011598 |
| 1 | `model.layers.0.self_attn.v_proj` | 307200 | 0.018137 | 0.000000059040 |
| 2 | `model.layers.14.self_attn.v_proj` | 307200 | 0.012021 | 0.000000039130 |
| 34 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.011765 | 0.000000004787 |
| 41 | `model.layers.3.mlp.up_proj` | 2457600 | 0.009686 | 0.000000003941 |
| 3 | `model.layers.27.self_attn.v_proj` | 307200 | 0.009278 | 0.000000030203 |
| 4 | `model.layers.6.self_attn.v_proj` | 307200 | 0.008803 | 0.000000028656 |
| 47 | `model.layers.28.mlp.gate_proj` | 2457600 | 0.008485 | 0.000000003453 |
| 21 | `model.layers.18.self_attn.o_proj` | 921600 | 0.007308 | 0.000000007930 |
| 52 | `model.layers.29.mlp.down_proj` | 2457600 | 0.007217 | 0.000000002937 |
| 22 | `model.layers.13.self_attn.q_proj` | 921600 | 0.007045 | 0.000000007645 |
| 5 | `model.layers.23.self_attn.v_proj` | 307200 | 0.006940 | 0.000000022592 |
| 55 | `model.layers.11.mlp.up_proj` | 2457600 | 0.006935 | 0.000000002822 |
| 57 | `model.layers.29.mlp.up_proj` | 2457600 | 0.006815 | 0.000000002773 |
| 6 | `model.layers.29.self_attn.v_proj` | 307200 | 0.006746 | 0.000000021961 |
| 63 | `model.layers.10.mlp.down_proj` | 2457600 | 0.006108 | 0.000000002486 |
| 8 | `model.layers.24.self_attn.v_proj` | 307200 | 0.005880 | 0.000000019142 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
