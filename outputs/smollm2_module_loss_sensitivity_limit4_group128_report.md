# Module Loss Sensitivity Report

Date: `2026-06-04`
Model: `HuggingFaceTB/SmolLM2-360M-Instruct`
Prompts: `4`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`

## Baseline

- FP16 mean NLL: `5.051106`
- FP16 PPL: `156.195141`
- Tokens: `75`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 172, '8': 53} | 0.5783 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 60 | `lm_head` | 47185920 | 0.283996 | 0.000000006019 |
| 1 | `model.layers.30.mlp.up_proj` | 2457600 | 0.221735 | 0.000000090224 |
| 6 | `model.layers.3.mlp.down_proj` | 2457600 | 0.106990 | 0.000000043534 |
| 17 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.045376 | 0.000000018463 |
| 22 | `model.layers.31.mlp.up_proj` | 2457600 | 0.039710 | 0.000000016158 |
| 10 | `model.layers.0.self_attn.o_proj` | 921600 | 0.034125 | 0.000000037029 |
| 30 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.029739 | 0.000000012101 |
| 40 | `model.layers.12.mlp.gate_proj` | 2457600 | 0.022786 | 0.000000009271 |
| 41 | `model.layers.31.mlp.down_proj` | 2457600 | 0.022256 | 0.000000009056 |
| 2 | `model.layers.8.self_attn.k_proj` | 307200 | 0.020574 | 0.000000066974 |
| 45 | `model.layers.3.mlp.up_proj` | 2457600 | 0.020016 | 0.000000008144 |
| 3 | `model.layers.31.self_attn.v_proj` | 307200 | 0.019166 | 0.000000062389 |
| 47 | `model.layers.13.mlp.up_proj` | 2457600 | 0.018726 | 0.000000007620 |
| 48 | `model.layers.2.mlp.gate_proj` | 2457600 | 0.018643 | 0.000000007586 |
| 51 | `model.layers.15.mlp.up_proj` | 2457600 | 0.017378 | 0.000000007071 |
| 53 | `model.layers.12.mlp.up_proj` | 2457600 | 0.016799 | 0.000000006835 |
| 4 | `model.layers.8.self_attn.v_proj` | 307200 | 0.016688 | 0.000000054323 |
| 54 | `model.layers.4.mlp.down_proj` | 2457600 | 0.016255 | 0.000000006614 |
| 5 | `model.layers.12.self_attn.v_proj` | 307200 | 0.015671 | 0.000000051014 |
| 19 | `model.layers.4.self_attn.q_proj` | 921600 | 0.015612 | 0.000000016940 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
