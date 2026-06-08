# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix3000 task matrix

Date: `2026-06-08T02:02:58+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `9000`
- total passes across cases: `4816`
- max accuracy drop vs `fp16`: `0.0530`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 3000 | 1687 | 0.5623 | 4.8991 | 0.420055 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix3000_2026_06_08.json` |
| `autoawq` | `mmlu` | 3000 | 1601 | 0.5337 | 11.1693 | 0.152503 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix3000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 3000 | 1528 | 0.5093 | 8.9680 | 0.188292 | 0.7232 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix3000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5623 | 0.5337 | 0.0287 |
| `gptqmodel` | `mmlu` | 0.5623 | 0.5093 | 0.0530 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix3000 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
