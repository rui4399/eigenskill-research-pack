# Official AutoAWQ Public-Calibration Baseline Gate

Date: `2026-06-07T11:59:29+00:00`
Status: **PASS**

## Summary

- model: `Qwen/Qwen2.5-1.5B-Instruct`
- package: `autoawq 0.2.9`
- quant config: `{'zero_point': True, 'q_group_size': 128, 'w_bit': 4, 'version': 'GEMM'}`
- calibration sources: `['data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt', 'data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt']`
- calibration samples: `4`
- expected AWQ calibration blocks: `2`
- artifact files: `6`
- artifact bytes: `1159233350`
- quantization peak VRAM ratio: `0.8234572445098761`
- eval slices: `2`
- total eval tokens: `2857`

## Eval Slices

| label | prompts | tokens | FP16 PPL | AutoAWQ PPL | ratio | peak VRAM |
|---|---:|---:|---:|---:|---:|---:|
| `wikitext2` | 16 | 1413 | 16.984146 | 19.266930 | 1.134407 | 0.6543 |
| `c4` | 16 | 1444 | 21.405532 | 23.179046 | 1.082853 | 0.4641 |

## Failures

- none

## Claim Boundary

- Valid claim: one public-calibration AutoAWQ W4 group-128 baseline bundle ran under guard and was evaluated on tiny public WikiText2/C4 PPL slices. Invalid claim: this is a complete official AWQ/GPTQ competitive baseline, SOTA PTQ result, task-retention proof, or production runtime.
