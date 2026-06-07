# Module Loss Sensitivity Report

Date: `2026-06-07`
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Prompts: `8`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `169 / 169`

## Baseline

- FP16 mean NLL: `3.469590`
- FP16 PPL: `32.123579`
- Tokens: `687`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 103, '8': 66} | 0.6889 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 18 | `model.layers.2.mlp.down_proj` | 4358144 | 0.086748 | 0.000000019905 |
| 86 | `lm_head` | 136134656 | 0.086621 | 0.000000000636 |
| 20 | `model.layers.21.mlp.down_proj` | 4358144 | 0.081887 | 0.000000018789 |
| 24 | `model.layers.3.mlp.down_proj` | 4358144 | 0.054160 | 0.000000012427 |
| 28 | `model.layers.23.mlp.down_proj` | 4358144 | 0.042417 | 0.000000009733 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.011820 | 0.000000102951 |
| 48 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.011296 | 0.000000002592 |
| 49 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.010515 | 0.000000002413 |
| 51 | `model.layers.1.mlp.up_proj` | 4358144 | 0.010266 | 0.000000002356 |
| 2 | `model.layers.8.self_attn.v_proj` | 114816 | 0.009721 | 0.000000084664 |
| 54 | `model.layers.22.mlp.down_proj` | 4358144 | 0.009439 | 0.000000002166 |
| 3 | `model.layers.12.self_attn.v_proj` | 114816 | 0.008812 | 0.000000076745 |
| 58 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.008567 | 0.000000001966 |
| 4 | `model.layers.21.self_attn.v_proj` | 114816 | 0.007844 | 0.000000068320 |
| 59 | `model.layers.23.mlp.up_proj` | 4358144 | 0.007661 | 0.000000001758 |
| 30 | `model.layers.1.self_attn.o_proj` | 802816 | 0.007626 | 0.000000009500 |
| 33 | `model.layers.23.self_attn.o_proj` | 802816 | 0.006883 | 0.000000008574 |
| 5 | `model.layers.15.self_attn.v_proj` | 114816 | 0.006772 | 0.000000058982 |
| 60 | `model.layers.1.mlp.down_proj` | 4358144 | 0.006382 | 0.000000001464 |
| 6 | `model.layers.6.self_attn.v_proj` | 114816 | 0.006271 | 0.000000054616 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
