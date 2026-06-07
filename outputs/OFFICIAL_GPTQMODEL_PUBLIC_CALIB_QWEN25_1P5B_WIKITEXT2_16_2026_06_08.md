# Official GPTQModel Public-Calibration Summary

Date: `2026-06-07T18:29:30+00:00`
Status: **PASS**
Model: `Qwen/Qwen2.5-1.5B-Instruct`
Package: `gptqmodel 7.0.0`
Quant config: `{'bits': 4, 'group_size': 128}`
Calibration sources: `['data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt', 'data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt']`
Calibration texts: `4`
Artifact: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Artifact reused: `True`
Artifact files: `8`
Artifact bytes: `1161301069`
Prompts: `16`
Tokens: `1413`
Elapsed seconds: `26.469`

## Metrics

| run | mean_nll | ppl |
|---|---:|---:|
| `fp16` | 2.832280 | 16.984146 |
| `gptqmodel_w4g128` | 2.960006 | 19.298090 |

## Comparison

- delta NLL GPTQ-FP16: `0.127726`
- PPL ratio GPTQ/FP16: `1.136241`

## Failures

- none

## Claim Boundary

- Valid claim: GPTQModel ran a public-calibration W4 group-128 smoke and produced a matched tiny-slice FP16-vs-GPTQ PPL diagnostic. Invalid claim: this is a complete GPTQ/AWQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime.
