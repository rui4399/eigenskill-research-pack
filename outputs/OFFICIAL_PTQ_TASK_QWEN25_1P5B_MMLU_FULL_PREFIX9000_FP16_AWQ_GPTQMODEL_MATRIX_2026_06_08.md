# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix9000 task matrix

Date: `2026-06-08T05:55:19+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `27000`
- total passes across cases: `15956`
- max accuracy drop vs `fp16`: `0.0503`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8794`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 9000 | 5539 | 0.6154 | 4.9513 | 0.408208 | 0.8794 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix9000_2026_06_08.json` |
| `autoawq` | `mmlu` | 9000 | 5331 | 0.5923 | 11.0402 | 0.156399 | 0.8138 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix9000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 9000 | 5086 | 0.5651 | 9.0592 | 0.186965 | 0.7566 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix9000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.6154 | 0.5923 | 0.0231 |
| `gptqmodel` | `mmlu` | 0.6154 | 0.5651 | 0.0503 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix9000 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
