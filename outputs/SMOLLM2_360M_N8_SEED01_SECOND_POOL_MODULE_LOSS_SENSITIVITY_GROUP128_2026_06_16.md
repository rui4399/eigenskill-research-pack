# Module Loss Sensitivity Report

Date: `2026-06-16`
Model: `/mnt/e/hf_cache/hub/models--HuggingFaceTB--SmolLM2-360M-Instruct/snapshots/a10cc1512eabd3dde888204e902eca88bddb4951`
Prompts: `8`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `225 / 225`

## Baseline

- FP16 mean NLL: `3.170009`
- FP16 PPL: `23.807709`
- Tokens: `668`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 171, '8': 54} | 0.5650 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 46 | `lm_head` | 47185920 | 0.180536 | 0.000000003826 |
| 2 | `model.layers.30.mlp.up_proj` | 2457600 | 0.071122 | 0.000000028940 |
| 5 | `model.layers.31.mlp.down_proj` | 2457600 | 0.063280 | 0.000000025749 |
| 6 | `model.layers.3.mlp.down_proj` | 2457600 | 0.060150 | 0.000000024475 |
| 17 | `model.layers.31.mlp.up_proj` | 2457600 | 0.029917 | 0.000000012173 |
| 33 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.013751 | 0.000000005595 |
| 34 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.013039 | 0.000000005305 |
| 1 | `model.layers.24.self_attn.v_proj` | 307200 | 0.011184 | 0.000000036405 |
| 44 | `model.layers.1.mlp.down_proj` | 2457600 | 0.010072 | 0.000000004098 |
| 3 | `model.layers.0.self_attn.v_proj` | 307200 | 0.008625 | 0.000000028075 |
| 4 | `model.layers.28.self_attn.v_proj` | 307200 | 0.008415 | 0.000000027393 |
| 50 | `model.layers.24.mlp.down_proj` | 2457600 | 0.007203 | 0.000000002931 |
| 51 | `model.layers.23.mlp.down_proj` | 2457600 | 0.006917 | 0.000000002815 |
| 52 | `model.layers.21.mlp.up_proj` | 2457600 | 0.006874 | 0.000000002797 |
| 53 | `model.layers.24.mlp.gate_proj` | 2457600 | 0.006483 | 0.000000002638 |
| 54 | `model.layers.28.mlp.gate_proj` | 2457600 | 0.006370 | 0.000000002592 |
| 56 | `model.layers.22.mlp.down_proj` | 2457600 | 0.006116 | 0.000000002489 |
| 7 | `model.layers.4.self_attn.v_proj` | 307200 | 0.005866 | 0.000000019095 |
| 8 | `model.layers.23.self_attn.v_proj` | 307200 | 0.005794 | 0.000000018862 |
| 9 | `model.layers.29.self_attn.v_proj` | 307200 | 0.005784 | 0.000000018829 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
