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

- FP16 mean NLL: `2.989692`
- FP16 PPL: `19.879559`
- Tokens: `1397`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 160, '8': 65} | 0.5330 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 42 | `lm_head` | 47185920 | 0.174384 | 0.000000003696 |
| 2 | `model.layers.31.mlp.down_proj` | 2457600 | 0.058140 | 0.000000023657 |
| 3 | `model.layers.3.mlp.down_proj` | 2457600 | 0.056574 | 0.000000023020 |
| 5 | `model.layers.30.mlp.up_proj` | 2457600 | 0.050787 | 0.000000020665 |
| 13 | `model.layers.31.mlp.up_proj` | 2457600 | 0.025199 | 0.000000010254 |
| 19 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.020519 | 0.000000008349 |
| 36 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.010838 | 0.000000004410 |
| 1 | `model.layers.0.self_attn.v_proj` | 307200 | 0.008642 | 0.000000028131 |
| 49 | `model.layers.1.mlp.down_proj` | 2457600 | 0.007760 | 0.000000003157 |
| 51 | `model.layers.8.mlp.gate_proj` | 2457600 | 0.006964 | 0.000000002833 |
| 20 | `model.layers.1.self_attn.q_proj` | 921600 | 0.006832 | 0.000000007413 |
| 4 | `model.layers.24.self_attn.v_proj` | 307200 | 0.006607 | 0.000000021507 |
| 25 | `model.layers.12.self_attn.q_proj` | 921600 | 0.005402 | 0.000000005861 |
| 6 | `model.layers.23.self_attn.v_proj` | 307200 | 0.005286 | 0.000000017208 |
| 64 | `model.layers.24.mlp.gate_proj` | 2457600 | 0.005105 | 0.000000002077 |
| 7 | `model.layers.29.self_attn.v_proj` | 307200 | 0.004829 | 0.000000015719 |
| 67 | `model.layers.21.mlp.up_proj` | 2457600 | 0.004802 | 0.000000001954 |
| 68 | `model.layers.23.mlp.down_proj` | 2457600 | 0.004692 | 0.000000001909 |
| 8 | `model.layers.28.self_attn.v_proj` | 307200 | 0.004539 | 0.000000014774 |
| 35 | `model.layers.22.self_attn.q_proj` | 921600 | 0.004135 | 0.000000004487 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
