# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `microsoft/Phi-3-mini-4k-instruct`
Prompts: `64`
Max length: `128`
Quantized bits during probing: `2`
Group size: `128`
Status: `complete`
Measured modules: `129 / 129`

## Baseline

- FP16 mean NLL: `2.169101`
- FP16 PPL: `8.750411`
- Tokens: `7229`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 129} | 0.0000 |
| loss_sensitive_4to8 | 2.9960 | 0.9987 | {'2': 64, '4': 65} | 0.8750 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 1 | `lm_head` | 98500608 | 5.021623 | 0.000000050981 |
| 2 | `model.layers.31.mlp.down_proj` | 25165824 | 0.893282 | 0.000000035496 |
| 3 | `model.layers.31.mlp.gate_up_proj` | 50331648 | 0.526306 | 0.000000010457 |
| 6 | `model.layers.30.mlp.gate_up_proj` | 50331648 | 0.211808 | 0.000000004208 |
| 10 | `model.layers.29.mlp.gate_up_proj` | 50331648 | 0.171495 | 0.000000003407 |
| 5 | `model.layers.29.mlp.down_proj` | 25165824 | 0.106224 | 0.000000004221 |
| 24 | `model.layers.28.mlp.gate_up_proj` | 50331648 | 0.097693 | 0.000000001941 |
| 8 | `model.layers.2.mlp.down_proj` | 25165824 | 0.094014 | 0.000000003736 |
| 29 | `model.layers.7.mlp.gate_up_proj` | 50331648 | 0.091755 | 0.000000001823 |
| 9 | `model.layers.30.mlp.down_proj` | 25165824 | 0.088928 | 0.000000003534 |
| 4 | `model.layers.31.self_attn.o_proj` | 9437184 | 0.079664 | 0.000000008441 |
| 39 | `model.layers.25.mlp.gate_up_proj` | 50331648 | 0.076991 | 0.000000001530 |
| 13 | `model.layers.4.mlp.down_proj` | 25165824 | 0.073951 | 0.000000002939 |
| 48 | `model.layers.4.mlp.gate_up_proj` | 50331648 | 0.070820 | 0.000000001407 |
| 49 | `model.layers.2.mlp.gate_up_proj` | 50331648 | 0.070688 | 0.000000001404 |
| 14 | `model.layers.25.mlp.down_proj` | 25165824 | 0.067219 | 0.000000002671 |
| 52 | `model.layers.3.mlp.gate_up_proj` | 50331648 | 0.066515 | 0.000000001322 |
| 53 | `model.layers.26.mlp.gate_up_proj` | 50331648 | 0.066057 | 0.000000001312 |
| 56 | `model.layers.27.mlp.gate_up_proj` | 50331648 | 0.063715 | 0.000000001266 |
| 19 | `model.layers.30.self_attn.qkv_proj` | 28311552 | 0.060616 | 0.000000002141 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
