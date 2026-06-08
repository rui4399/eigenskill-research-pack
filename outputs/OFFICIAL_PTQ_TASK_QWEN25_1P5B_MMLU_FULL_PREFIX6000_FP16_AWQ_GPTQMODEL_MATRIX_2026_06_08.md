# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix6000 task matrix

Date: `2026-06-08T04:24:18+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `18000`
- total passes across cases: `10413`
- max accuracy drop vs `fp16`: `0.0517`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 6000 | 3630 | 0.6050 | 4.8318 | 0.417520 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix6000_2026_06_08.json` |
| `autoawq` | `mmlu` | 6000 | 3463 | 0.5772 | 10.7409 | 0.161641 | 0.7890 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix6000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 6000 | 3320 | 0.5533 | 8.8492 | 0.188530 | 0.7352 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix6000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.6050 | 0.5772 | 0.0278 |
| `gptqmodel` | `mmlu` | 0.6050 | 0.5533 | 0.0517 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix6000 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
