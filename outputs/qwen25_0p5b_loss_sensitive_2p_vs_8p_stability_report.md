# Allocation Stability Report

Left allocation: `outputs\qwen25_0p5b_loss_sensitive_alloc_4to8_limit2_group128_summary.json`
Right allocation: `outputs\qwen25_0p5b_loss_sensitive_alloc_4to8_limit8_group128_summary.json`

## Summary

| metric | value |
|---|---:|
| modules | 169 |
| left high-bit modules | 55 |
| right high-bit modules | 57 |
| overlap high-bit modules | 38 |
| Jaccard | 0.5135 |
| unchanged bit decisions | 133 |
| changed bit decisions | 36 |

## PPL

| split | fp16 | uniform int4 | left allocation | right allocation | right vs left |
|---|---:|---:|---:|---:|---:|
| WikiText2-128 | 17.4294 | 27.7411 | 22.4605 | 21.9762 | -0.4843 |
| C4-64 | 23.9539 | 36.5128 | 31.2151 | 30.7970 | -0.4181 |

## Changed Modules

| module | from | to | params | positive delta NLL | rank |
|---|---:|---:|---:|---:|---:|
| `model.layers.21.mlp.up_proj` | 4 | 8 | 4358144 | 0.009726 | 54 |
| `model.layers.15.mlp.up_proj` | 4 | 8 | 4358144 | 0.009223 | 56 |
| `model.layers.1.mlp.gate_proj` | 4 | 8 | 4358144 | 0.008422 | 61 |
| `model.layers.8.mlp.up_proj` | 4 | 8 | 4358144 | 0.007088 | 66 |
| `model.layers.16.mlp.up_proj` | 4 | 8 | 4358144 | 0.001633 | 93 |
| `model.layers.4.self_attn.q_proj` | 4 | 8 | 803712 | 0.001272 | 67 |
| `model.layers.3.self_attn.o_proj` | 4 | 8 | 802816 | 0.001155 | 71 |
| `model.layers.2.self_attn.q_proj` | 4 | 8 | 803712 | 0.000565 | 85 |
| `model.layers.23.self_attn.o_proj` | 4 | 8 | 802816 | 0.000523 | 86 |
| `model.layers.12.self_attn.q_proj` | 4 | 8 | 803712 | 0.000398 | 88 |
| `model.layers.1.self_attn.q_proj` | 4 | 8 | 803712 | 0.000000 | 114 |
| `model.layers.12.self_attn.k_proj` | 4 | 8 | 114816 | 0.000000 | 142 |
| `model.layers.12.self_attn.v_proj` | 4 | 8 | 114816 | 0.000000 | 143 |
| `model.layers.20.self_attn.v_proj` | 4 | 8 | 114816 | 0.000000 | 166 |
| `model.layers.3.self_attn.k_proj` | 4 | 8 | 114816 | 0.000000 | 120 |
| `model.layers.4.self_attn.o_proj` | 4 | 8 | 802816 | 0.000000 | 122 |
| `model.layers.5.self_attn.k_proj` | 4 | 8 | 114816 | 0.000000 | 125 |
| `model.layers.5.self_attn.o_proj` | 4 | 8 | 802816 | 0.000000 | 126 |
| `model.layers.7.self_attn.k_proj` | 4 | 8 | 114816 | 0.000000 | 129 |
| `model.layers.2.mlp.up_proj` | 8 | 4 | 4358144 | 0.016088 | 40 |
| `model.layers.3.mlp.up_proj` | 8 | 4 | 4358144 | 0.015792 | 41 |
| `model.layers.7.mlp.up_proj` | 8 | 4 | 4358144 | 0.015246 | 42 |
| `model.layers.4.mlp.down_proj` | 8 | 4 | 4358144 | 0.012906 | 47 |
| `model.layers.15.mlp.down_proj` | 8 | 4 | 4358144 | 0.011618 | 50 |
| `model.layers.0.self_attn.v_proj` | 8 | 4 | 114816 | 0.005219 | 5 |
| `model.layers.12.self_attn.o_proj` | 8 | 4 | 802816 | 0.004501 | 32 |
| `model.layers.22.self_attn.q_proj` | 8 | 4 | 803712 | 0.003458 | 36 |
| `model.layers.23.self_attn.q_proj` | 8 | 4 | 803712 | 0.002323 | 48 |
| `model.layers.6.self_attn.o_proj` | 8 | 4 | 802816 | 0.002239 | 49 |
| `model.layers.16.self_attn.q_proj` | 8 | 4 | 803712 | 0.002079 | 51 |

## Interpretation

The comparison measures whether the selected 8-bit module set is stable when
the calibration probe changes. PPL is reported separately because a lower
Jaccard does not necessarily mean worse downstream quality.
