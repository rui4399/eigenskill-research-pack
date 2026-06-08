# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix1000 task matrix

Date: `2026-06-08T00:30:40+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `3000`
- total passes across cases: `1683`
- max accuracy drop vs `fp16`: `0.0440`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 1000 | 584 | 0.5840 | 4.7503 | 0.409682 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix1000_2026_06_08.json` |
| `autoawq` | `mmlu` | 1000 | 559 | 0.5590 | 10.3844 | 0.146696 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix1000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 1000 | 540 | 0.5400 | 8.4331 | 0.184150 | 0.7149 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix1000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5840 | 0.5590 | 0.0250 |
| `gptqmodel` | `mmlu` | 0.5840 | 0.5400 | 0.0440 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same local full-MMLU first 1000-row task evidence under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
