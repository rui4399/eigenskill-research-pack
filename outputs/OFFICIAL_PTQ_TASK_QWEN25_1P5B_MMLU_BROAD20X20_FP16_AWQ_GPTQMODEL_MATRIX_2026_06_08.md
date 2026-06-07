# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel MMLU broad20x20 task matrix

Date: `2026-06-07T23:12:13+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `1200`
- total passes across cases: `616`
- max accuracy drop vs `fp16`: `0.0400`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8201`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 400 | 214 | 0.5350 | 5.2316 | 0.407572 | 0.8201 | `outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json` |
| `autoawq` | `mmlu` | 400 | 204 | 0.5100 | 11.8433 | 0.157150 | 0.7265 | `outputs/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 400 | 198 | 0.4950 | 9.4272 | 0.204092 | 0.6921 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5350 | 0.5100 | 0.0250 |
| `gptqmodel` | `mmlu` | 0.5350 | 0.4950 | 0.0400 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local MMLU broad20x20 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
