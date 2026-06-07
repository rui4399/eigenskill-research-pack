# Official PTQ Matched Task Subset100 Matrix

Date: `2026-06-07T09:26:53+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k', 'mmlu']`
- total tasks across cases: `600`
- total passes across cases: `75`
- max accuracy drop vs `fp16`: `0.0300`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.5210`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 100 | 25 | 0.2500 | 31.0716 | 0.088620 | 0.5118 | `outputs/official_ptq_task_fp16_mmlu_subset100_summary_2026_06_07.json` |
| `fp16` | `gsm8k` | 100 | 2 | 0.0200 | 27.7082 | 0.106440 | 0.5210 | `outputs/official_ptq_task_fp16_gsm8k_subset100_summary_2026_06_07.json` |
| `autoawq` | `mmlu` | 100 | 23 | 0.2300 | 4.8842 | 0.326504 | 0.4527 | `outputs/official_ptq_task_awq_mmlu_subset100_summary_2026_06_07.json` |
| `autoawq` | `gsm8k` | 100 | 1 | 0.0100 | 5.1528 | 0.385639 | 0.4530 | `outputs/official_ptq_task_awq_gsm8k_subset100_summary_2026_06_07.json` |
| `gptqmodel` | `mmlu` | 100 | 22 | 0.2200 | 10.7656 | 0.202465 | 0.4514 | `outputs/official_ptq_task_gptqmodel_mmlu_subset100_summary_2026_06_07.json` |
| `gptqmodel` | `gsm8k` | 100 | 2 | 0.0200 | 9.6759 | 0.400023 | 0.4512 | `outputs/official_ptq_task_gptqmodel_gsm8k_subset100_summary_2026_06_07.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `gsm8k` | 0.0200 | 0.0100 | 0.0100 |
| `gptqmodel` | `gsm8k` | 0.0200 | 0.0200 | 0.0000 |
| `autoawq` | `mmlu` | 0.2500 | 0.2300 | 0.0200 |
| `gptqmodel` | `mmlu` | 0.2500 | 0.2200 | 0.0300 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same 100-row matched public MMLU/GSM8K subsets under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
