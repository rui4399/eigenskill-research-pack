# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix12000 task matrix

Date: `2026-06-08T08:02:29+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `36000`
- total passes across cases: `20051`
- max accuracy drop vs `fp16`: `0.0483`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8794`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 12000 | 6968 | 0.5807 | 4.9771 | 0.401457 | 0.8794 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix12000_2026_06_08.json` |
| `autoawq` | `mmlu` | 12000 | 6694 | 0.5578 | 10.8106 | 0.157657 | 0.8138 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix12000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 12000 | 6389 | 0.5324 | 9.2153 | 0.185555 | 0.7566 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix12000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5807 | 0.5578 | 0.0228 |
| `gptqmodel` | `mmlu` | 0.5807 | 0.5324 | 0.0483 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix12000 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
