# Official PTQ Matched Task Subset20 Matrix

Date: `2026-06-07T02:13:51+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k', 'mmlu']`
- total tasks across cases: `120`
- total passes across cases: `15`
- max accuracy drop vs `fp16`: `0.0000`
- zero-accuracy baseline formats: `['gsm8k']`
- peak guard VRAM ratio: `0.6131`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 20 | 5 | 0.2500 | 31.4878 | 0.134118 | 0.6131 | `outputs/official_ptq_task_fp16_mmlu_subset20_summary_2026_06_07.json` |
| `fp16` | `gsm8k` | 20 | 0 | 0.0000 | 29.5206 | 0.157866 | 0.6116 | `outputs/official_ptq_task_fp16_gsm8k_subset20_summary_2026_06_07.json` |
| `autoawq` | `mmlu` | 20 | 5 | 0.2500 | 4.5607 | 0.342797 | 0.5543 | `outputs/official_ptq_task_awq_mmlu_subset20_summary_2026_06_07.json` |
| `autoawq` | `gsm8k` | 20 | 0 | 0.0000 | 5.0626 | 0.493040 | 0.5538 | `outputs/official_ptq_task_awq_gsm8k_subset20_summary_2026_06_07.json` |
| `gptqmodel` | `mmlu` | 20 | 5 | 0.2500 | 7.9835 | 0.272888 | 0.5504 | `outputs/official_ptq_task_gptqmodel_mmlu_subset20_summary_2026_06_07.json` |
| `gptqmodel` | `gsm8k` | 20 | 0 | 0.0000 | 9.6279 | 0.415011 | 0.5494 | `outputs/official_ptq_task_gptqmodel_gsm8k_subset20_summary_2026_06_07.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `gsm8k` | 0.0000 | 0.0000 | 0.0000 |
| `gptqmodel` | `gsm8k` | 0.0000 | 0.0000 | 0.0000 |
| `autoawq` | `mmlu` | 0.2500 | 0.2500 | 0.0000 |
| `gptqmodel` | `mmlu` | 0.2500 | 0.2500 | 0.0000 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same 20-row matched public MMLU/GSM8K subsets under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
