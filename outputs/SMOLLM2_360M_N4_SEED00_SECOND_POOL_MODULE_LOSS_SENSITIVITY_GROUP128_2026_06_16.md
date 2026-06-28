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

- FP16 mean NLL: `3.181801`
- FP16 PPL: `24.090092`
- Tokens: `315`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 172, '8': 53} | 0.5871 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 41 | `lm_head` | 47185920 | 0.173285 | 0.000000003672 |
| 1 | `model.layers.31.mlp.down_proj` | 2457600 | 0.096571 | 0.000000039295 |
| 4 | `model.layers.30.mlp.up_proj` | 2457600 | 0.077892 | 0.000000031695 |
| 7 | `model.layers.31.mlp.up_proj` | 2457600 | 0.040040 | 0.000000016292 |
| 8 | `model.layers.3.mlp.down_proj` | 2457600 | 0.038505 | 0.000000015668 |
| 22 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.020585 | 0.000000008376 |
| 27 | `model.layers.2.mlp.gate_proj` | 2457600 | 0.017441 | 0.000000007097 |
| 33 | `model.layers.1.mlp.down_proj` | 2457600 | 0.016256 | 0.000000006614 |
| 2 | `model.layers.14.self_attn.v_proj` | 307200 | 0.010122 | 0.000000032949 |
| 3 | `model.layers.24.self_attn.v_proj` | 307200 | 0.009800 | 0.000000031900 |
| 18 | `model.layers.12.self_attn.q_proj` | 921600 | 0.008513 | 0.000000009238 |
| 44 | `model.layers.22.mlp.down_proj` | 2457600 | 0.008401 | 0.000000003418 |
| 5 | `model.layers.7.self_attn.v_proj` | 307200 | 0.008019 | 0.000000026103 |
| 49 | `model.layers.11.mlp.up_proj` | 2457600 | 0.007545 | 0.000000003070 |
| 52 | `model.layers.29.mlp.up_proj` | 2457600 | 0.007257 | 0.000000002953 |
| 54 | `model.layers.29.mlp.down_proj` | 2457600 | 0.006749 | 0.000000002746 |
| 56 | `model.layers.19.mlp.gate_proj` | 2457600 | 0.006620 | 0.000000002694 |
| 57 | `model.layers.25.mlp.gate_proj` | 2457600 | 0.006585 | 0.000000002680 |
| 29 | `model.layers.22.self_attn.o_proj` | 921600 | 0.006501 | 0.000000007054 |
| 6 | `model.layers.17.self_attn.v_proj` | 307200 | 0.006402 | 0.000000020839 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
