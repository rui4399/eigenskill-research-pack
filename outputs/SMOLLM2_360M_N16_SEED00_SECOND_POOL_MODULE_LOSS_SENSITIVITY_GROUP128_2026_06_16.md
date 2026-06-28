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

- FP16 mean NLL: `2.894530`
- FP16 PPL: `18.075012`
- Tokens: `1357`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 164, '8': 61} | 0.5348 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 46 | `lm_head` | 47185920 | 0.157027 | 0.000000003328 |
| 2 | `model.layers.31.mlp.down_proj` | 2457600 | 0.064560 | 0.000000026270 |
| 3 | `model.layers.30.mlp.up_proj` | 2457600 | 0.052404 | 0.000000021323 |
| 5 | `model.layers.3.mlp.down_proj` | 2457600 | 0.042416 | 0.000000017259 |
| 18 | `model.layers.31.mlp.up_proj` | 2457600 | 0.020239 | 0.000000008235 |
| 28 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.013267 | 0.000000005399 |
| 1 | `model.layers.24.self_attn.v_proj` | 307200 | 0.010363 | 0.000000033734 |
| 52 | `model.layers.1.mlp.down_proj` | 2457600 | 0.006568 | 0.000000002673 |
| 54 | `model.layers.23.mlp.down_proj` | 2457600 | 0.006149 | 0.000000002502 |
| 4 | `model.layers.0.self_attn.v_proj` | 307200 | 0.005984 | 0.000000019478 |
| 56 | `model.layers.26.mlp.gate_proj` | 2457600 | 0.005813 | 0.000000002365 |
| 26 | `model.layers.12.self_attn.q_proj` | 921600 | 0.005648 | 0.000000006129 |
| 57 | `model.layers.24.mlp.gate_proj` | 2457600 | 0.005611 | 0.000000002283 |
| 58 | `model.layers.8.mlp.gate_proj` | 2457600 | 0.005471 | 0.000000002226 |
| 6 | `model.layers.2.self_attn.v_proj` | 307200 | 0.004741 | 0.000000015433 |
| 62 | `model.layers.24.mlp.down_proj` | 2457600 | 0.004726 | 0.000000001923 |
| 63 | `model.layers.27.mlp.down_proj` | 2457600 | 0.004708 | 0.000000001916 |
| 7 | `model.layers.27.self_attn.v_proj` | 307200 | 0.004576 | 0.000000014897 |
| 66 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.004493 | 0.000000001828 |
| 67 | `model.layers.22.mlp.down_proj` | 2457600 | 0.004348 | 0.000000001769 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
