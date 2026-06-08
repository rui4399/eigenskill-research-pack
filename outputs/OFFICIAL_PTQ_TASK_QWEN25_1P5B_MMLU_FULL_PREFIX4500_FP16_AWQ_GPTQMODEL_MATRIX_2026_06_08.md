# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix4500 task matrix

Date: `2026-06-08T03:16:07+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `13500`
- total passes across cases: `7469`
- max accuracy drop vs `fp16`: `0.0564`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 4500 | 2614 | 0.5809 | 4.8561 | 0.417594 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix4500_2026_06_08.json` |
| `autoawq` | `mmlu` | 4500 | 2495 | 0.5544 | 10.9480 | 0.158347 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix4500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 4500 | 2360 | 0.5244 | 8.8469 | 0.189934 | 0.7232 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix4500_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5809 | 0.5544 | 0.0264 |
| `gptqmodel` | `mmlu` | 0.5809 | 0.5244 | 0.0564 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix4500 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
