# Official GPTQModel Public-Calibration Summary

Date: `2026-06-07T05:12:29+00:00`
Status: **PASS**
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Package: `gptqmodel 7.0.0`
Quant config: `{'bits': 4, 'group_size': 128}`
Calibration sources: `['data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt', 'data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt']`
Calibration texts: `12`
Artifact: `outputs/official_gptqmodel_smoke_2026_06_07/qwen25_0p5b_public_calib_gptq_model`
Artifact reused: `True`
Artifact files: `8`
Artifact bytes: `470821016`
Prompts: `16`
Tokens: `1413`
Elapsed seconds: `34.037`

## Metrics

| run | mean_nll | ppl |
|---|---:|---:|
| `fp16` | 3.202370 | 24.590745 |
| `gptqmodel_w4g128` | 3.431066 | 30.909568 |

## Comparison

- delta NLL GPTQ-FP16: `0.228696`
- PPL ratio GPTQ/FP16: `1.256959`

## Failures

- none

## Claim Boundary

- Valid claim: GPTQModel ran a public-calibration W4 group-128 smoke and produced a matched tiny-slice FP16-vs-GPTQ PPL diagnostic. Invalid claim: this is a complete GPTQ/AWQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime.
