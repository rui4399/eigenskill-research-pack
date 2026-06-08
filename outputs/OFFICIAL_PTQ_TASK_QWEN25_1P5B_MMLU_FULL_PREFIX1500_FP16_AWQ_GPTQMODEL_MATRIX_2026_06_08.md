# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix1500 task matrix

Date: `2026-06-08T00:50:09+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `4500`
- total passes across cases: `2420`
- max accuracy drop vs `fp16`: `0.0480`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 1500 | 848 | 0.5653 | 4.8378 | 0.415698 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix1500_2026_06_08.json` |
| `autoawq` | `mmlu` | 1500 | 796 | 0.5307 | 10.6969 | 0.152438 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix1500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 1500 | 776 | 0.5173 | 8.5655 | 0.186657 | 0.7232 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix1500_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5653 | 0.5307 | 0.0347 |
| `gptqmodel` | `mmlu` | 0.5653 | 0.5173 | 0.0480 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same local full-MMLU first 1500-row task evidence under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
