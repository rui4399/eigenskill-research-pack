# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix5500 task matrix

Date: `2026-06-08T04:00:32+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `16500`
- total passes across cases: `9429`
- max accuracy drop vs `fp16`: `0.0536`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 5500 | 3295 | 0.5991 | 4.8459 | 0.417699 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix5500_2026_06_08.json` |
| `autoawq` | `mmlu` | 5500 | 3134 | 0.5698 | 10.9050 | 0.157035 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix5500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 5500 | 3000 | 0.5455 | 8.7836 | 0.189041 | 0.7232 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix5500_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5991 | 0.5698 | 0.0293 |
| `gptqmodel` | `mmlu` | 0.5991 | 0.5455 | 0.0536 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix5500 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
