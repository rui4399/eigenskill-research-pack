# Official AutoAWQ Public-Calibration Baseline Gate

Date: `2026-06-06T21:50:25+00:00`
Status: **PASS**

## Summary

- model: `Qwen/Qwen2.5-0.5B-Instruct`
- package: `autoawq 0.2.9`
- quant config: `{'zero_point': True, 'q_group_size': 128, 'w_bit': 4, 'version': 'GEMM'}`
- calibration sources: `['data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt', 'data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt']`
- calibration samples: `12`
- expected AWQ calibration blocks: `8`
- artifact files: `6`
- artifact bytes: `469809733`
- quantization peak VRAM ratio: `0.6959882223040118`
- eval slices: `2`
- total eval tokens: `1487`

## Eval Slices

| label | prompts | tokens | FP16 PPL | AutoAWQ PPL | ratio | peak VRAM |
|---|---:|---:|---:|---:|---:|---:|
| `wikitext2` | 8 | 760 | 24.675866 | 29.080631 | 1.178505 | 0.6116 |
| `c4` | 8 | 727 | 32.951664 | 38.172702 | 1.158445 | 0.6116 |

## Failures

- none

## Claim Boundary

- Valid claim: one public-calibration AutoAWQ W4 group-128 baseline bundle ran under guard and was evaluated on tiny public WikiText2/C4 PPL slices. Invalid claim: this is a complete official AWQ/GPTQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime.
