# Qwen2.5-1.5B Broad MMLU 5x20 PTQ Retention

Date: `2026-06-07T22:05:23+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `300`
- total passes across cases: `160`
- max accuracy drop vs `fp16`: `0.0600`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8114`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 100 | 56 | 0.5600 | 5.1312 | 0.412188 | 0.8114 | `outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad5x20_summary_2026_06_08.json` |
| `autoawq` | `mmlu` | 100 | 54 | 0.5400 | 11.1998 | 0.154689 | 0.7209 | `outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_broad5x20_summary_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 100 | 50 | 0.5000 | 9.4013 | 0.191056 | 0.6819 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad5x20_summary_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5600 | 0.5400 | 0.0200 |
| `gptqmodel` | `mmlu` | 0.5600 | 0.5000 | 0.0600 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same guarded local five-subject 100-row MMLU retention, not full leaderboard under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
