# Qwen2.5-14B AWQ Activation CSI Proxy

Model: `E:\models\Qwen2.5-14B-Instruct-AWQ`
Prompt file: `data_eval\text_prompts\aaai_scaling_512_2026_07_09\wikitext2_test_ppl_prompts.txt`
Prompt sample size: `64`
Seeds: `[0, 1]`

## Split Agreement

| metric | value |
|---|---:|
| shared WQLinear modules | 336 |
| top-k | 84 |
| top-k Jaccard | 0.9765 |
| Spearman rank correlation | 0.9998 |

## Proxy Allocation

| metric | value |
|---|---:|
| average bits | 2.9996 |
| budget used | 0.9999 |
| bit histogram | {'4': 220, '2': 116} |

## Scope

This is an AWQ-aware calibration-stability proxy over `WQLinear_GEMM` modules.
It does not dequantize or re-quantize 14B weights and should not be claimed as full 14B fake-quant CSI downstream evidence.
