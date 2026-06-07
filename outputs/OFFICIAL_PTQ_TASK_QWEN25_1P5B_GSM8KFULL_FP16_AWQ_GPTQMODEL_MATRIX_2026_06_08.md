# Official PTQ task-retention gate: Qwen2.5-1.5B GSM8K full

Date: `2026-06-07T21:36:01+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k']`
- total tasks across cases: `3957`
- total passes across cases: `307`
- max accuracy drop vs `fp16`: `0.0083`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8295`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `gsm8k` | 1319 | 107 | 0.0811 | 5.1170 | 0.496028 | 0.8295 | `outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_1319_summary_2026_06_08.json` |
| `autoawq` | `gsm8k` | 1319 | 104 | 0.0788 | 13.3764 | 0.202863 | 0.7391 | `outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8kfull_1319_summary_2026_06_08.json` |
| `gptqmodel` | `gsm8k` | 1319 | 96 | 0.0728 | 10.6277 | 0.262285 | 0.6791 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8kfull_1319_summary_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `gsm8k` | 0.0811 | 0.0788 | 0.0023 |
| `gptqmodel` | `gsm8k` | 0.0811 | 0.0728 | 0.0083 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same Qwen2.5-1.5B full GSM8K PTQ retention under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
