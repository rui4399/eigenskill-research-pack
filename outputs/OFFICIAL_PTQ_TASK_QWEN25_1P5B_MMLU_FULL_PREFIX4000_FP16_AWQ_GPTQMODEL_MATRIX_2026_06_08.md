# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix4000 task matrix

Date: `2026-06-08T02:54:10+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `12000`
- total passes across cases: `6762`
- max accuracy drop vs `fp16`: `0.0553`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 4000 | 2366 | 0.5915 | 4.8154 | 0.416089 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix4000_2026_06_08.json` |
| `autoawq` | `mmlu` | 4000 | 2251 | 0.5627 | 10.7702 | 0.158048 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix4000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 4000 | 2145 | 0.5363 | 8.8304 | 0.187847 | 0.7232 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix4000_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5915 | 0.5627 | 0.0288 |
| `gptqmodel` | `mmlu` | 0.5915 | 0.5363 | 0.0553 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU prefix4000 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
