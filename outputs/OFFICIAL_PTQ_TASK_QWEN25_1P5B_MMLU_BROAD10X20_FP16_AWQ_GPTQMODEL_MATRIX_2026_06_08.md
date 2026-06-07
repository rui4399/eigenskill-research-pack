# Qwen2.5-1.5B Broad MMLU 10x20 PTQ Retention

Date: `2026-06-07T22:28:25+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `600`
- total passes across cases: `291`
- max accuracy drop vs `fp16`: `0.0350`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8189`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 200 | 101 | 0.5050 | 5.2627 | 0.397696 | 0.8189 | `outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad10x20_summary_2026_06_08.json` |
| `autoawq` | `mmlu` | 200 | 96 | 0.4800 | 11.7995 | 0.149837 | 0.7235 | `outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_broad10x20_summary_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 200 | 94 | 0.4700 | 9.3779 | 0.187812 | 0.6849 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad10x20_summary_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5050 | 0.4800 | 0.0250 |
| `gptqmodel` | `mmlu` | 0.5050 | 0.4700 | 0.0350 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same guarded local ten-subject 200-row MMLU retention, not full leaderboard under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
