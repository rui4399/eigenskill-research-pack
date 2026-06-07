# Official GPTQModel Qwen2.5-1.5B Subset100 Task-Execution Matrix

Date: `2026-06-07T19:03:07+00:00`
Status: **PASS**

## Summary

- variants: `['gptqmodel']`
- task formats: `['gsm8k', 'mmlu']`
- total tasks across cases: `200`
- total passes across cases: `33`
- max accuracy drop vs `gptqmodel`: `0.0000`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.6672`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `gptqmodel` | `mmlu` | 100 | 25 | 0.2500 | 10.2403 | 0.207707 | 0.6672 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_subset100_summary_2026_06_08.json` |
| `gptqmodel` | `gsm8k` | 100 | 8 | 0.0800 | 11.0534 | 0.264654 | 0.6672 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_subset100_summary_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same GPTQModel Qwen2.5-1.5B MMLU100/GSM8K100 task-execution slice under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
