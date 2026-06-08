# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix14042 task matrix

Date: `2026-06-08T10:36:12+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `42126`
- total passes across cases: `23694`
- max accuracy drop vs `fp16`: `0.0502`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8794`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 14042 | 8234 | 0.5864 | 4.9773 | 0.396824 | 0.8794 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix14042_2026_06_08.json` |
| `autoawq` | `mmlu` | 14042 | 7931 | 0.5648 | 10.8232 | 0.153977 | 0.8138 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix14042_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 14042 | 7529 | 0.5362 | 9.1870 | 0.182449 | 0.7566 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix14042_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5864 | 0.5648 | 0.0216 |
| `gptqmodel` | `mmlu` | 0.5864 | 0.5362 | 0.0502 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix14042 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
