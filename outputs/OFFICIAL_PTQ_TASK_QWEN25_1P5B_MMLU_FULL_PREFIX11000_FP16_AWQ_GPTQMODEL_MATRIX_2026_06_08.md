# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix11000 task matrix

Date: `2026-06-08T07:05:16+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `33000`
- total passes across cases: `18860`
- max accuracy drop vs `fp16`: `0.0494`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8794`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 11000 | 6554 | 0.5958 | 5.0045 | 0.403427 | 0.8794 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix11000_2026_06_08.json` |
| `autoawq` | `mmlu` | 11000 | 6295 | 0.5723 | 11.0222 | 0.155157 | 0.8138 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix11000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 11000 | 6011 | 0.5465 | 9.1480 | 0.185809 | 0.7566 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix11000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5958 | 0.5723 | 0.0235 |
| `gptqmodel` | `mmlu` | 0.5958 | 0.5465 | 0.0494 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix11000 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
