# Official GPTQModel Public-Calibration Summary

Date: `2026-06-06T23:54:42+00:00`
Status: **PASS**
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Package: `gptqmodel 7.0.0`
Quant config: `{'bits': 4, 'group_size': 128}`
Calibration sources: `['data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt', 'data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt']`
Calibration texts: `4`
Artifact: `outputs/official_gptqmodel_smoke_2026_06_07/qwen25_0p5b_public_calib_gptq_model`
Artifact reused: `False`
Artifact files: `8`
Artifact bytes: `470821016`
Prompts: `4`
Tokens: `380`
Elapsed seconds: `209.275`

## Metrics

| run | mean_nll | ppl |
|---|---:|---:|
| `fp16` | 2.964309 | 19.381307 |
| `gptqmodel_w4g128` | 3.245609 | 25.677339 |

## Comparison

- delta NLL GPTQ-FP16: `0.281300`
- PPL ratio GPTQ/FP16: `1.324851`

## Failures

- none

## Claim Boundary

- Valid claim: GPTQModel ran a public-calibration W4 group-128 smoke and produced a matched tiny-slice FP16-vs-GPTQ PPL diagnostic. Invalid claim: this is a complete GPTQ/AWQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime.
