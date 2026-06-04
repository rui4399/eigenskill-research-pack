# SmolLM2 Module Output-Reconstruction Sensitivity Report

Date: `2026-06-04`
Model: `HuggingFaceTB/SmolLM2-360M-Instruct`
Prompts: `4`
Max length: `128`
Sample rows per module: `128`
Quantized bits during proxy measurement: `4`
Group size: `128`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected proxy |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| output_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 135, '8': 90} | 0.5450 |

## Top 20 Output-Sensitive Modules

| rank | module | params | normalized output MSE | output MSE / param | sample rows |
|---:|---|---:|---:|---:|---:|
| 33 | `model.layers.0.mlp.up_proj` | 2457600 | 0.09169908 | 0.000000037312 | 128 |
| 1 | `model.layers.0.self_attn.v_proj` | 307200 | 0.06423615 | 0.000000209102 | 128 |
| 224 | `lm_head` | 47185920 | 0.05605614 | 0.000000001188 | 128 |
| 2 | `model.layers.20.self_attn.v_proj` | 307200 | 0.04434513 | 0.000000144353 | 128 |
| 3 | `model.layers.25.self_attn.v_proj` | 307200 | 0.04039045 | 0.000000131479 | 128 |
| 4 | `model.layers.23.self_attn.v_proj` | 307200 | 0.04017792 | 0.000000130788 | 128 |
| 5 | `model.layers.13.self_attn.v_proj` | 307200 | 0.04010892 | 0.000000130563 | 128 |
| 6 | `model.layers.14.self_attn.v_proj` | 307200 | 0.03962396 | 0.000000128984 | 128 |
| 7 | `model.layers.22.self_attn.v_proj` | 307200 | 0.03839472 | 0.000000124983 | 128 |
| 8 | `model.layers.19.self_attn.v_proj` | 307200 | 0.03808744 | 0.000000123983 | 128 |
| 9 | `model.layers.9.self_attn.v_proj` | 307200 | 0.03791795 | 0.000000123431 | 128 |
| 10 | `model.layers.16.self_attn.v_proj` | 307200 | 0.03690541 | 0.000000120135 | 128 |
| 11 | `model.layers.24.self_attn.v_proj` | 307200 | 0.03639115 | 0.000000118461 | 128 |
| 12 | `model.layers.21.self_attn.v_proj` | 307200 | 0.03619604 | 0.000000117826 | 128 |
| 13 | `model.layers.26.self_attn.v_proj` | 307200 | 0.03476219 | 0.000000113158 | 128 |
| 14 | `model.layers.10.self_attn.v_proj` | 307200 | 0.03448243 | 0.000000112247 | 128 |
| 15 | `model.layers.18.self_attn.v_proj` | 307200 | 0.03351786 | 0.000000109108 | 128 |
| 16 | `model.layers.30.self_attn.v_proj` | 307200 | 0.03246976 | 0.000000105696 | 128 |
| 17 | `model.layers.11.self_attn.v_proj` | 307200 | 0.03202062 | 0.000000104234 | 128 |
| 18 | `model.layers.7.self_attn.v_proj` | 307200 | 0.03107107 | 0.000000101143 | 128 |

## Scope

- This is an activation/output reconstruction proxy, not a full loss probe.
- It is cheaper than per-module PPL probing but may mis-rank modules whose
  local output error is not aligned with global language-model loss.
- The generated allocation should be evaluated with `eval_weight_quant_ppl.py`.
