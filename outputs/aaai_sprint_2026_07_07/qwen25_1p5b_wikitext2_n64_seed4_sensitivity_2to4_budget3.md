# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `64`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.608834`
- FP16 PPL: `13.583201`
- Tokens: `7051`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9973 | 0.9991 | {'2': 94, '4': 103} | 0.9358 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 54 | `lm_head` | 233373696 | 0.092388 | 0.000000000396 |
| 3 | `model.layers.1.mlp.down_proj` | 13762560 | 0.052768 | 0.000000003834 |
| 15 | `model.layers.2.mlp.down_proj` | 13762560 | 0.033780 | 0.000000002455 |
| 18 | `model.layers.26.mlp.down_proj` | 13762560 | 0.028889 | 0.000000002099 |
| 36 | `model.layers.27.mlp.down_proj` | 13762560 | 0.011635 | 0.000000000845 |
| 49 | `model.layers.27.mlp.up_proj` | 13762560 | 0.006944 | 0.000000000505 |
| 50 | `model.layers.26.mlp.up_proj` | 13762560 | 0.006827 | 0.000000000496 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.005933 | 0.000000015078 |
| 58 | `model.layers.1.mlp.up_proj` | 13762560 | 0.005236 | 0.000000000380 |
| 59 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.005190 | 0.000000000377 |
| 60 | `model.layers.3.mlp.up_proj` | 13762560 | 0.004835 | 0.000000000351 |
| 64 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.004293 | 0.000000000312 |
| 69 | `model.layers.9.mlp.up_proj` | 13762560 | 0.003068 | 0.000000000223 |
| 70 | `model.layers.23.mlp.up_proj` | 13762560 | 0.002920 | 0.000000000212 |
| 74 | `model.layers.4.mlp.down_proj` | 13762560 | 0.002731 | 0.000000000198 |
| 75 | `model.layers.23.mlp.gate_proj` | 13762560 | 0.002692 | 0.000000000196 |
| 26 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.002588 | 0.000000001097 |
| 76 | `model.layers.6.mlp.gate_proj` | 13762560 | 0.002544 | 0.000000000185 |
| 77 | `model.layers.3.mlp.down_proj` | 13762560 | 0.002454 | 0.000000000178 |
| 82 | `model.layers.9.mlp.down_proj` | 13762560 | 0.002303 | 0.000000000167 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
