# Module Loss Sensitivity Report

Date: `2026-06-05`
Model: `allenai/OLMo-2-0425-1B-Instruct`
Prompts: `2`
Max length: `160`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `113 / 113`

## Baseline

- FP16 mean NLL: `3.233390`
- FP16 PPL: `25.365509`
- Tokens: `318`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 113} | 0.0000 |
| loss_sensitive_4to8 | 4.4984 | 0.9996 | {'4': 93, '8': 20} | 0.5879 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 36 | `lm_head` | 205520896 | 0.033888 | 0.000000000165 |
| 7 | `model.layers.15.mlp.down_proj` | 16777216 | 0.016541 | 0.000000000986 |
| 11 | `model.layers.12.mlp.down_proj` | 16777216 | 0.012284 | 0.000000000732 |
| 13 | `model.layers.6.mlp.down_proj` | 16777216 | 0.011097 | 0.000000000661 |
| 1 | `model.layers.0.self_attn.v_proj` | 4194304 | 0.008561 | 0.000000002041 |
| 18 | `model.layers.15.mlp.gate_proj` | 16777216 | 0.006884 | 0.000000000410 |
| 2 | `model.layers.8.self_attn.v_proj` | 4194304 | 0.006720 | 0.000000001602 |
| 3 | `model.layers.13.self_attn.o_proj` | 4194304 | 0.006492 | 0.000000001548 |
| 19 | `model.layers.1.mlp.up_proj` | 16777216 | 0.006325 | 0.000000000377 |
| 20 | `model.layers.13.mlp.down_proj` | 16777216 | 0.006100 | 0.000000000364 |
| 4 | `model.layers.5.self_attn.q_proj` | 4194304 | 0.005971 | 0.000000001424 |
| 22 | `model.layers.4.mlp.down_proj` | 16777216 | 0.005315 | 0.000000000317 |
| 5 | `model.layers.7.self_attn.o_proj` | 4194304 | 0.004435 | 0.000000001057 |
| 6 | `model.layers.14.self_attn.v_proj` | 4194304 | 0.004272 | 0.000000001018 |
| 26 | `model.layers.11.mlp.gate_proj` | 16777216 | 0.004236 | 0.000000000253 |
| 8 | `model.layers.4.self_attn.o_proj` | 4194304 | 0.003885 | 0.000000000926 |
| 27 | `model.layers.3.mlp.up_proj` | 16777216 | 0.003825 | 0.000000000228 |
| 9 | `model.layers.15.self_attn.v_proj` | 4194304 | 0.003650 | 0.000000000870 |
| 28 | `model.layers.11.mlp.down_proj` | 16777216 | 0.003633 | 0.000000000217 |
| 10 | `model.layers.11.self_attn.o_proj` | 4194304 | 0.003600 | 0.000000000858 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
