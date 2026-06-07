# Official PTQ Qwen2.5-1.5B Task Subset20 Matrix

Date: `2026-06-07T12:47:22+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16']`
- task formats: `['gsm8k', 'mmlu']`
- total tasks across cases: `80`
- total passes across cases: `21`
- max accuracy drop vs `fp16`: `0.0000`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.6821`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 20 | 8 | 0.4000 | 19.6289 | 0.151401 | 0.6762 | `outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_subset20_summary_2026_06_07.json` |
| `fp16` | `gsm8k` | 20 | 2 | 0.1000 | 19.2592 | 0.194016 | 0.6821 | `outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_subset20_summary_2026_06_07.json` |
| `autoawq` | `mmlu` | 20 | 9 | 0.4500 | 13.1778 | 0.226386 | 0.4961 | `outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_subset20_summary_2026_06_07.json` |
| `autoawq` | `gsm8k` | 20 | 2 | 0.1000 | 14.5865 | 0.271346 | 0.4864 | `outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_subset20_summary_2026_06_07.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `gsm8k` | 0.1000 | 0.1000 | 0.0000 |
| `autoawq` | `mmlu` | 0.4000 | 0.4500 | -0.0500 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same 20-row matched public MMLU/GSM8K subsets on Qwen2.5-1.5B FP16 and AutoAWQ under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
