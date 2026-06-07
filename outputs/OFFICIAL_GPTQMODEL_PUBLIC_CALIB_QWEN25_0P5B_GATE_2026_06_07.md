# Official GPTQModel Public-Calibration Gate

Date: `2026-06-07T00:03:10+00:00`
Status: **PASS**

## Summary

- model: `Qwen/Qwen2.5-0.5B-Instruct`
- package: `gptqmodel 7.0.0`
- quant config: `{'bits': 4, 'group_size': 128}`
- calibration sources: `['data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt', 'data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt']`
- calibration texts: `4`
- artifact files: `8`
- artifact bytes: `470821016`
- artifact reused: `False`
- prompts: `4`
- tokens: `380`
- peak VRAM ratio: `0.6233590970433076`

## Metrics

| run | PPL |
|---|---:|
| `fp16` | 19.381307 |
| `gptqmodel_w4g128` | 25.677339 |

## Comparison

- PPL ratio GPTQ/FP16: `1.324851`
- delta NLL GPTQ-FP16: `0.281300`

## Failures

- none

## Claim Boundary

- Valid claim: one public-calibration GPTQModel W4 group-128 smoke ran under guard, saved/reloaded a local artifact, and produced a tiny matched FP16-vs-GPTQ PPL diagnostic. Invalid claim: this is a complete official AWQ/GPTQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime.
