# Official GPTQModel Public-Calibration Gate

Date: `2026-06-07T18:30:56+00:00`
Status: **PASS**

## Summary

- model: `Qwen/Qwen2.5-1.5B-Instruct`
- package: `gptqmodel 7.0.0`
- quant config: `{'bits': 4, 'group_size': 128}`
- calibration sources: `['data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt', 'data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt']`
- calibration texts: `4`
- artifact files: `8`
- artifact bytes: `1161301069`
- artifact reused: `False`
- eval slices: `2`
- total eval tokens: `2857`
- peak VRAM ratio: `0.854251012145749`

## Evaluation Slices

| slice | prompts | tokens | FP16 PPL | GPTQ PPL | ratio | artifact reused | peak VRAM |
|---|---:|---:|---:|---:|---:|---|---:|
| `wikitext2` | 16 | 1413 | 16.984146 | 19.298090 | 1.136241 | `True` | 0.769844 |
| `c4` | 16 | 1444 | 21.405532 | 23.381530 | 1.092312 | `True` | 0.826647 |

## Metrics

| run | PPL |
|---|---:|
| `fp16` | 16.984146 |
| `gptqmodel_w4g128` | 19.298090 |

## Comparison

- PPL ratio GPTQ/FP16: `1.136241`
- delta NLL GPTQ-FP16: `0.127726`

## Failures

- none

## Claim Boundary

- Valid claim: one fresh public-calibration GPTQModel W4 group-128 smoke ran under guard, saved/reloaded a local artifact, and produced tiny labeled FP16-vs-GPTQ PPL diagnostics. Invalid claim: this is a complete official AWQ/GPTQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime.
