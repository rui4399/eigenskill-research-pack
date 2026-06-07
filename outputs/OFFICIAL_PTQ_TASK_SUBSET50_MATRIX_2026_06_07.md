# Official PTQ Matched Task Subset50 Matrix

Date: `2026-06-07T02:42:48+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k', 'mmlu']`
- total tasks across cases: `300`
- total passes across cases: `37`
- max accuracy drop vs `fp16`: `0.0400`
- zero-accuracy baseline formats: `['gsm8k']`
- peak guard VRAM ratio: `0.6148`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 50 | 13 | 0.2600 | 30.7629 | 0.104500 | 0.6148 | `outputs/official_ptq_task_fp16_mmlu_subset50_summary_2026_06_07.json` |
| `fp16` | `gsm8k` | 50 | 0 | 0.0000 | 32.7153 | 0.104516 | 0.6142 | `outputs/official_ptq_task_fp16_gsm8k_subset50_summary_2026_06_07.json` |
| `autoawq` | `mmlu` | 50 | 11 | 0.2200 | 5.2414 | 0.306996 | 0.5539 | `outputs/official_ptq_task_awq_mmlu_subset50_summary_2026_06_07.json` |
| `autoawq` | `gsm8k` | 50 | 0 | 0.0000 | 5.0996 | 0.411649 | 0.5537 | `outputs/official_ptq_task_awq_gsm8k_subset50_summary_2026_06_07.json` |
| `gptqmodel` | `mmlu` | 50 | 13 | 0.2600 | 11.1024 | 0.205163 | 0.5489 | `outputs/official_ptq_task_gptqmodel_mmlu_subset50_summary_2026_06_07.json` |
| `gptqmodel` | `gsm8k` | 50 | 0 | 0.0000 | 9.9427 | 0.367901 | 0.5490 | `outputs/official_ptq_task_gptqmodel_gsm8k_subset50_summary_2026_06_07.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `gsm8k` | 0.0000 | 0.0000 | 0.0000 |
| `gptqmodel` | `gsm8k` | 0.0000 | 0.0000 | 0.0000 |
| `autoawq` | `mmlu` | 0.2600 | 0.2200 | 0.0400 |
| `gptqmodel` | `mmlu` | 0.2600 | 0.2600 | 0.0000 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same 50-row matched public MMLU/GSM8K subsets under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
