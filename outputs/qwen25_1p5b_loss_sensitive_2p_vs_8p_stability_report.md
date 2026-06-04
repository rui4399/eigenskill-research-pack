# Allocation Stability Report

Left allocation: `outputs\qwen25_1p5b_loss_sensitive_alloc_4to8_limit2_group128_summary.json`
Right allocation: `outputs\qwen25_1p5b_loss_sensitive_alloc_4to8_limit8_group128_summary.json`

## Summary

| metric | value |
|---|---:|
| modules | 197 |
| left high-bit modules | 60 |
| right high-bit modules | 61 |
| overlap high-bit modules | 47 |
| Jaccard | 0.6351 |
| unchanged bit decisions | 170 |
| changed bit decisions | 27 |

## PPL

| split | fp16 | uniform int4 | left allocation | right allocation | right vs left |
|---|---:|---:|---:|---:|---:|
| WikiText2-16 | 11.2830 | 15.8383 | 13.7652 | 13.7622 | -0.0030 |
| C4-32 | 17.8832 | 23.5711 | 22.8859 | 21.9642 | -0.9217 |

## Changed Modules

| module | from | to | params | positive delta NLL | rank |
|---|---:|---:|---:|---:|---:|
| `model.layers.27.mlp.gate_proj` | 4 | 8 | 13762560 | 0.002997 | 95 |
| `model.layers.18.self_attn.o_proj` | 4 | 8 | 2359296 | 0.000595 | 90 |
| `model.layers.0.self_attn.q_proj` | 4 | 8 | 2360832 | 0.000406 | 102 |
| `model.layers.23.self_attn.k_proj` | 4 | 8 | 393472 | 0.000289 | 62 |
| `model.layers.1.self_attn.k_proj` | 4 | 8 | 393472 | 0.000262 | 64 |
| `model.layers.0.self_attn.o_proj` | 4 | 8 | 2359296 | 0.000000 | 132 |
| `model.layers.1.mlp.down_proj` | 4 | 8 | 13762560 | 0.000000 | 134 |
| `model.layers.21.self_attn.v_proj` | 4 | 8 | 393472 | 0.000000 | 183 |
| `model.layers.25.self_attn.v_proj` | 4 | 8 | 393472 | 0.000000 | 193 |
| `model.layers.26.self_attn.k_proj` | 4 | 8 | 393472 | 0.000000 | 195 |
| `model.layers.4.self_attn.k_proj` | 4 | 8 | 393472 | 0.000000 | 140 |
| `model.layers.4.self_attn.v_proj` | 4 | 8 | 393472 | 0.000000 | 141 |
| `model.layers.5.self_attn.k_proj` | 4 | 8 | 393472 | 0.000000 | 145 |
| `model.layers.9.self_attn.q_proj` | 4 | 8 | 2360832 | 0.000000 | 158 |
| `model.layers.3.mlp.gate_proj` | 8 | 4 | 13762560 | 0.022066 | 40 |
| `model.layers.1.mlp.gate_proj` | 8 | 4 | 13762560 | 0.010606 | 60 |
| `model.layers.12.self_attn.q_proj` | 8 | 4 | 2360832 | 0.004068 | 36 |
| `model.layers.12.self_attn.v_proj` | 8 | 4 | 393472 | 0.002858 | 11 |
| `model.layers.2.self_attn.o_proj` | 8 | 4 | 2359296 | 0.002573 | 52 |
| `model.layers.16.self_attn.q_proj` | 8 | 4 | 2360832 | 0.002484 | 55 |
| `model.layers.15.self_attn.q_proj` | 8 | 4 | 2360832 | 0.002144 | 57 |
| `model.layers.22.self_attn.o_proj` | 8 | 4 | 2359296 | 0.001849 | 59 |
| `model.layers.11.self_attn.k_proj` | 8 | 4 | 393472 | 0.001234 | 23 |
| `model.layers.25.self_attn.k_proj` | 8 | 4 | 393472 | 0.001151 | 24 |
| `model.layers.27.self_attn.k_proj` | 8 | 4 | 393472 | 0.000975 | 30 |
| `model.layers.8.self_attn.k_proj` | 8 | 4 | 393472 | 0.000675 | 37 |
| `model.layers.10.self_attn.k_proj` | 8 | 4 | 393472 | 0.000450 | 51 |

## Interpretation

The comparison measures whether the selected 8-bit module set is stable when
the calibration probe changes. PPL is reported separately because a lower
Jaccard does not necessarily mean worse downstream quality.
