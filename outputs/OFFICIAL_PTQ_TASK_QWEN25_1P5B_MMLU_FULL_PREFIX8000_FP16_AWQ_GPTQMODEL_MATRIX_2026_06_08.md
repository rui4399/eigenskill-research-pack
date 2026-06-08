# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix8000 task matrix

Date: `2026-06-08T05:25:43+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `24000`
- total passes across cases: `14582`
- max accuracy drop vs `fp16`: `0.0493`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8794`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 8000 | 5059 | 0.6324 | 4.8894 | 0.409530 | 0.8794 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix8000_2026_06_08.json` |
| `autoawq` | `mmlu` | 8000 | 4858 | 0.6072 | 10.8962 | 0.157509 | 0.8138 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix8000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 8000 | 4665 | 0.5831 | 8.9705 | 0.186147 | 0.7566 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix8000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.6324 | 0.6072 | 0.0251 |
| `gptqmodel` | `mmlu` | 0.6324 | 0.5831 | 0.0493 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix8000 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
