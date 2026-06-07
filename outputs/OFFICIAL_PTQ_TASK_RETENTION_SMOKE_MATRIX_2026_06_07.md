# Official PTQ Task-Execution Smoke Matrix

Date: `2026-06-07T01:25:41+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k', 'mmlu']`
- total tasks across cases: `24`
- total passes across cases: `2`
- max accuracy drop vs `fp16`: `0.2500`
- zero-accuracy baseline formats: `['gsm8k']`
- peak guard VRAM ratio: `0.6108`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 4 | 1 | 0.2500 | 25.2172 | 0.359683 | 0.6108 | `outputs/official_ptq_task_fp16_mmlu_smoke_summary_2026_06_07.json` |
| `fp16` | `gsm8k` | 4 | 0 | 0.0000 | 20.5511 | 0.410765 | 0.6101 | `outputs/official_ptq_task_fp16_gsm8k_smoke_summary_2026_06_07.json` |
| `autoawq` | `mmlu` | 4 | 0 | 0.0000 | 3.1810 | 0.569940 | 0.5538 | `outputs/official_ptq_task_awq_mmlu_smoke_summary_2026_06_07.json` |
| `autoawq` | `gsm8k` | 4 | 0 | 0.0000 | 4.5937 | 0.724255 | 0.5524 | `outputs/official_ptq_task_awq_gsm8k_smoke_summary_2026_06_07.json` |
| `gptqmodel` | `mmlu` | 4 | 1 | 0.2500 | 7.9229 | 0.434381 | 0.5420 | `outputs/official_ptq_task_gptqmodel_mmlu_smoke_summary_2026_06_07.json` |
| `gptqmodel` | `gsm8k` | 4 | 0 | 0.0000 | 7.2988 | 0.551946 | 0.5420 | `outputs/official_ptq_task_gptqmodel_gsm8k_smoke_summary_2026_06_07.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `gsm8k` | 0.0000 | 0.0000 | 0.0000 |
| `gptqmodel` | `gsm8k` | 0.0000 | 0.0000 | 0.0000 |
| `autoawq` | `mmlu` | 0.2500 | 0.0000 | 0.2500 |
| `gptqmodel` | `mmlu` | 0.2500 | 0.2500 | 0.0000 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same tiny public MMLU/GSM8K smoke tasks under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
