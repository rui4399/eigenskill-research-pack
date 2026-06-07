# Allocation Family Proxy Gate

Date: `2026-06-07T04:41:39+00:00`
Status: **PASS**
Cases: `6`
Total records: `1126`

## Cases

| case | method | records | avg bits | target bits | budget use | lambda | distinct bits | bit hist |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `qwen3_0p6b_wikitext2` | `q_palette_style_lagrangian_proxy` | 197 | 4.499670 | 4.500000 | 0.999927 | 5.66546e-13 | 3 | `{'3': 87, '4': 45, '8': 65}` |
| `qwen3_0p6b_c4` | `q_palette_style_lagrangian_proxy` | 197 | 4.499670 | 4.500000 | 0.999927 | 3.64602e-13 | 3 | `{'3': 73, '4': 63, '8': 61}` |
| `qwen25_0p5b_limit2` | `q_palette_style_lagrangian_loss_sensitivity` | 169 | 4.499918 | 4.500000 | 0.999982 | 3.74614e-13 | 4 | `{'2': 60, '3': 2, '4': 34, '8': 73}` |
| `qwen25_0p5b_limit8` | `q_palette_style_lagrangian_loss_sensitivity` | 169 | 4.499912 | 4.500000 | 0.999980 | 3.95345e-13 | 4 | `{'2': 54, '3': 3, '4': 37, '8': 75}` |
| `qwen25_1p5b_limit2` | `q_palette_style_lagrangian_loss_sensitivity` | 197 | 4.499844 | 4.500000 | 0.999965 | 1.19151e-13 | 4 | `{'2': 67, '3': 2, '4': 45, '8': 83}` |
| `qwen25_1p5b_limit8` | `q_palette_style_lagrangian_loss_sensitivity` | 197 | 4.499854 | 4.500000 | 0.999967 | 1.1804e-13 | 4 | `{'2': 58, '3': 3, '4': 51, '8': 85}` |

## Failures

- none

## Claim Boundary

- Valid claim: Q-Palette-style measured-sensitivity allocation proxy artifacts exist and satisfy budget. Invalid claim: this is a faithful official Q-Palette/IMPQ/WINDQuant reproduction.
