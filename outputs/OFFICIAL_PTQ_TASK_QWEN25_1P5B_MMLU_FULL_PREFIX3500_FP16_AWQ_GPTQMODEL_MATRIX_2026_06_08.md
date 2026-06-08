# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix3500 task matrix

Date: `2026-06-08T02:24:05+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `10500`
- total passes across cases: `5725`
- max accuracy drop vs `fp16`: `0.0500`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 3500 | 1999 | 0.5711 | 4.8743 | 0.419125 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix3500_2026_06_08.json` |
| `autoawq` | `mmlu` | 3500 | 1902 | 0.5434 | 10.8438 | 0.160563 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix3500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 3500 | 1824 | 0.5211 | 8.9205 | 0.188762 | 0.7232 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix3500_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5711 | 0.5434 | 0.0277 |
| `gptqmodel` | `mmlu` | 0.5711 | 0.5211 | 0.0500 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix3500 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
