# Module Loss Sensitivity Report

Date: `2026-06-05`
Model: `Qwen/Qwen3-0.6B`
Prompts: `4`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `5.614949`
- FP16 PPL: `274.499495`
- Tokens: `73`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 153, '8': 44} | 0.6472 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 101 | `lm_head` | 155582464 | 0.082455 | 0.000000000530 |
| 6 | `model.layers.1.mlp.gate_proj` | 3145728 | 0.045120 | 0.000000014343 |
| 8 | `model.layers.26.mlp.up_proj` | 3145728 | 0.040325 | 0.000000012819 |
| 9 | `model.layers.26.mlp.gate_proj` | 3145728 | 0.039616 | 0.000000012593 |
| 14 | `model.layers.2.mlp.up_proj` | 3145728 | 0.033632 | 0.000000010691 |
| 18 | `model.layers.0.mlp.up_proj` | 3145728 | 0.023861 | 0.000000007585 |
| 1 | `model.layers.20.self_attn.v_proj` | 1048576 | 0.023840 | 0.000000022735 |
| 2 | `model.layers.21.self_attn.v_proj` | 1048576 | 0.022708 | 0.000000021656 |
| 3 | `model.layers.18.self_attn.v_proj` | 1048576 | 0.019195 | 0.000000018306 |
| 4 | `model.layers.4.self_attn.v_proj` | 1048576 | 0.019027 | 0.000000018146 |
| 27 | `model.layers.3.mlp.up_proj` | 3145728 | 0.017317 | 0.000000005505 |
| 28 | `model.layers.26.mlp.down_proj` | 3145728 | 0.017301 | 0.000000005500 |
| 5 | `model.layers.10.self_attn.k_proj` | 1048576 | 0.016393 | 0.000000015633 |
| 20 | `model.layers.11.self_attn.o_proj` | 2097152 | 0.015073 | 0.000000007187 |
| 22 | `model.layers.23.self_attn.q_proj` | 2097152 | 0.014886 | 0.000000007098 |
| 23 | `model.layers.25.self_attn.o_proj` | 2097152 | 0.014598 | 0.000000006961 |
| 7 | `model.layers.17.self_attn.v_proj` | 1048576 | 0.014515 | 0.000000013843 |
| 25 | `model.layers.2.self_attn.o_proj` | 2097152 | 0.013719 | 0.000000006542 |
| 10 | `model.layers.23.self_attn.k_proj` | 1048576 | 0.013164 | 0.000000012554 |
| 11 | `model.layers.16.self_attn.v_proj` | 1048576 | 0.012621 | 0.000000012036 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
