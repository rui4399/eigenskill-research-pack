# Official GPTQModel Public-Calibration Gate

Date: `2026-06-07T05:15:04+00:00`
Status: **PASS**

## Summary

- model: `Qwen/Qwen2.5-0.5B-Instruct`
- package: `gptqmodel 7.0.0`
- quant config: `{'bits': 4, 'group_size': 128}`
- calibration sources: `['data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt', 'data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt']`
- calibration texts: `12`
- artifact files: `8`
- artifact bytes: `470821016`
- artifact reused: `False`
- eval slices: `2`
- total eval tokens: `2857`
- peak VRAM ratio: `0.6110906637222426`

## Evaluation Slices

| slice | prompts | tokens | FP16 PPL | GPTQ PPL | ratio | artifact reused | peak VRAM |
|---|---:|---:|---:|---:|---:|---|---:|
| `wikitext2` | 16 | 1413 | 24.590745 | 30.909568 | 1.256959 | `True` | 0.574653 |
| `c4` | 16 | 1444 | 29.917597 | 36.362052 | 1.215407 | `True` | 0.556619 |

## Metrics

| run | PPL |
|---|---:|
| `fp16` | 24.590745 |
| `gptqmodel_w4g128` | 30.909568 |

## Comparison

- PPL ratio GPTQ/FP16: `1.256959`
- delta NLL GPTQ-FP16: `0.228696`

## Failures

- none

## Claim Boundary

- Valid claim: one fresh public-calibration GPTQModel W4 group-128 smoke ran under guard, saved/reloaded a local artifact, and produced tiny labeled FP16-vs-GPTQ PPL diagnostics. Invalid claim: this is a complete official AWQ/GPTQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime.
