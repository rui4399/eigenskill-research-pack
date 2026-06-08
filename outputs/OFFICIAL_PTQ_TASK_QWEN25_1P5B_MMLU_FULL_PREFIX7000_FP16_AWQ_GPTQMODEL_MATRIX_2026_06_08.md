# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix7000 task matrix

Date: `2026-06-08T04:59:45+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `21000`
- total passes across cases: `12387`
- max accuracy drop vs `fp16`: `0.0491`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8794`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 7000 | 4305 | 0.6150 | 4.8377 | 0.411032 | 0.8794 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix7000_2026_06_08.json` |
| `autoawq` | `mmlu` | 7000 | 4121 | 0.5887 | 10.7648 | 0.158735 | 0.8138 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix7000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 7000 | 3961 | 0.5659 | 8.8689 | 0.186104 | 0.7566 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix7000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.6150 | 0.5887 | 0.0263 |
| `gptqmodel` | `mmlu` | 0.6150 | 0.5659 | 0.0491 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix7000 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
