# Official AutoAWQ Public-Calibration Baseline Gate

Date: `2026-06-07T05:16:02+00:00`
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
- total eval tokens: `2857`

## Eval Slices

| label | prompts | tokens | FP16 PPL | AutoAWQ PPL | ratio | peak VRAM |
|---|---:|---:|---:|---:|---:|---:|
| `wikitext2` | 16 | 1413 | 24.590745 | 29.788817 | 1.211383 | 0.5493 |
| `c4` | 16 | 1444 | 29.917597 | 35.374649 | 1.182403 | 0.5678 |

## Failures

- none

## Claim Boundary

- Valid claim: one public-calibration AutoAWQ W4 group-128 baseline bundle ran under guard and was evaluated on tiny public WikiText2/C4 PPL slices. Invalid claim: this is a complete official AWQ/GPTQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime.
