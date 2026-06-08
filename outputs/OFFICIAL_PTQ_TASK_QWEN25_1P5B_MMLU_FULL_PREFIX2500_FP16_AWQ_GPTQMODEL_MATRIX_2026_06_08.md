# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix2500 task matrix

Date: `2026-06-08T01:37:50+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `7500`
- total passes across cases: `3950`
- max accuracy drop vs `fp16`: `0.0540`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 2500 | 1387 | 0.5548 | 4.9436 | 0.423534 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix2500_2026_06_08.json` |
| `autoawq` | `mmlu` | 2500 | 1311 | 0.5244 | 11.2880 | 0.154709 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix2500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 2500 | 1252 | 0.5008 | 8.9728 | 0.190026 | 0.7232 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix2500_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5548 | 0.5244 | 0.0304 |
| `gptqmodel` | `mmlu` | 0.5548 | 0.5008 | 0.0540 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix2500 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
