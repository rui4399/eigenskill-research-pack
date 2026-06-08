# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix10000 task matrix

Date: `2026-06-08T06:25:28+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `30000`
- total passes across cases: `17421`
- max accuracy drop vs `fp16`: `0.0501`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8794`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 10000 | 6054 | 0.6054 | 4.9898 | 0.406312 | 0.8794 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix10000_2026_06_08.json` |
| `autoawq` | `mmlu` | 10000 | 5814 | 0.5814 | 11.0766 | 0.155344 | 0.8138 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix10000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 10000 | 5553 | 0.5553 | 9.1207 | 0.186622 | 0.7566 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix10000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.6054 | 0.5814 | 0.0240 |
| `gptqmodel` | `mmlu` | 0.6054 | 0.5553 | 0.0501 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix10000 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
