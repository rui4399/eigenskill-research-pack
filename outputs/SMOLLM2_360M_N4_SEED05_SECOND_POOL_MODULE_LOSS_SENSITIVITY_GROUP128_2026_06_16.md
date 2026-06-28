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

- FP16 mean NLL: `2.491700`
- FP16 PPL: `12.081801`
- Tokens: `359`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 169, '8': 56} | 0.5833 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 52 | `lm_head` | 47185920 | 0.142054 | 0.000000003011 |
| 4 | `model.layers.30.mlp.up_proj` | 2457600 | 0.060403 | 0.000000024578 |
| 6 | `model.layers.3.mlp.down_proj` | 2457600 | 0.058406 | 0.000000023765 |
| 12 | `model.layers.31.mlp.down_proj` | 2457600 | 0.041458 | 0.000000016869 |
| 22 | `model.layers.31.mlp.up_proj` | 2457600 | 0.027061 | 0.000000011011 |
| 26 | `model.layers.1.mlp.down_proj` | 2457600 | 0.021603 | 0.000000008790 |
| 27 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.019988 | 0.000000008133 |
| 33 | `model.layers.2.mlp.gate_proj` | 2457600 | 0.016300 | 0.000000006633 |
| 34 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.014909 | 0.000000006067 |
| 39 | `model.layers.0.mlp.up_proj` | 2457600 | 0.013212 | 0.000000005376 |
| 1 | `model.layers.24.self_attn.v_proj` | 307200 | 0.011767 | 0.000000038305 |
| 2 | `model.layers.14.self_attn.v_proj` | 307200 | 0.008447 | 0.000000027497 |
| 3 | `model.layers.23.self_attn.v_proj` | 307200 | 0.008087 | 0.000000026325 |
| 50 | `model.layers.30.mlp.gate_proj` | 2457600 | 0.007769 | 0.000000003161 |
| 5 | `model.layers.7.self_attn.v_proj` | 307200 | 0.007448 | 0.000000024246 |
| 51 | `model.layers.10.mlp.down_proj` | 2457600 | 0.007403 | 0.000000003012 |
| 55 | `model.layers.11.mlp.up_proj` | 2457600 | 0.006999 | 0.000000002848 |
| 7 | `model.layers.3.self_attn.v_proj` | 307200 | 0.006671 | 0.000000021715 |
| 59 | `model.layers.22.mlp.gate_proj` | 2457600 | 0.006552 | 0.000000002666 |
| 8 | `model.layers.28.self_attn.v_proj` | 307200 | 0.006503 | 0.000000021170 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
