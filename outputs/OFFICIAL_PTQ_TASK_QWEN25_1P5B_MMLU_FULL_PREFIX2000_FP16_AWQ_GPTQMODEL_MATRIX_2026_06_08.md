# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix2000 task matrix

Date: `2026-06-08T01:08:51+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `6000`
- total passes across cases: `3208`
- max accuracy drop vs `fp16`: `0.0540`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 2000 | 1128 | 0.5640 | 4.8733 | 0.419905 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix2000_2026_06_08.json` |
| `autoawq` | `mmlu` | 2000 | 1060 | 0.5300 | 10.8575 | 0.152379 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix2000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 2000 | 1020 | 0.5100 | 8.7780 | 0.189020 | 0.7232 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix2000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5640 | 0.5300 | 0.0340 |
| `gptqmodel` | `mmlu` | 0.5640 | 0.5100 | 0.0540 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same local full-MMLU first 2000-row task evidence under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
