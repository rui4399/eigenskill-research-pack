# Official GPTQModel Task-Execution Smoke Matrix

Date: `2026-06-07T18:48:32+00:00`
Status: **PASS**

## Summary

- variants: `['gptqmodel']`
- task formats: `['gsm8k', 'mmlu']`
- total tasks across cases: `40`
- total passes across cases: `8`
- max accuracy drop vs `gptqmodel`: `0.0000`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.6672`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `gptqmodel` | `mmlu` | 20 | 7 | 0.3500 | 8.9403 | 0.315917 | 0.6672 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu20_summary_2026_06_08.json` |
| `gptqmodel` | `gsm8k` | 20 | 1 | 0.0500 | 11.1966 | 0.389499 | 0.6672 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k20_summary_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same GPTQModel Qwen2.5-1.5B MMLU20/GSM8K20 task-execution smokes under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
