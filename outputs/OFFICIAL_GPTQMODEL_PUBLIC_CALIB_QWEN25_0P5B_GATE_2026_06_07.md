# Official GPTQModel Public-Calibration Gate

Date: `2026-06-07T00:15:05+00:00`
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
- eval slices: `2`
- total eval tokens: `760`
- peak VRAM ratio: `0.6233590970433076`

## Evaluation Slices

| slice | prompts | tokens | FP16 PPL | GPTQ PPL | ratio | artifact reused | peak VRAM |
|---|---:|---:|---:|---:|---:|---|---:|
| `wikitext2` | 4 | 380 | 19.381307 | 25.677339 | 1.324851 | `False` | 0.623359 |
| `c4` | 4 | 380 | 24.665276 | 31.397740 | 1.272953 | `True` | 0.631456 |

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

- Valid claim: one fresh public-calibration GPTQModel W4 group-128 smoke ran under guard, saved/reloaded a local artifact, and produced tiny labeled FP16-vs-GPTQ PPL diagnostics. Invalid claim: this is a complete official AWQ/GPTQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime.
