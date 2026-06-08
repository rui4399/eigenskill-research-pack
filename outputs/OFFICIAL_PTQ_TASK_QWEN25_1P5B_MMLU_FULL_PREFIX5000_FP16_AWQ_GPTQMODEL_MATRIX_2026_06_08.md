# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix5000 task matrix

Date: `2026-06-08T03:39:22+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `15000`
- total passes across cases: `8346`
- max accuracy drop vs `fp16`: `0.0548`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 5000 | 2921 | 0.5842 | 4.8454 | 0.417038 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix5000_2026_06_08.json` |
| `autoawq` | `mmlu` | 5000 | 2778 | 0.5556 | 10.8964 | 0.157726 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix5000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 5000 | 2647 | 0.5294 | 8.7835 | 0.189247 | 0.7232 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix5000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5842 | 0.5556 | 0.0286 |
| `gptqmodel` | `mmlu` | 0.5842 | 0.5294 | 0.0548 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix5000 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
