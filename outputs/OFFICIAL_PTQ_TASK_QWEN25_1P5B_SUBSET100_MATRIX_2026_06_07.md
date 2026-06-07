# Qwen2.5-1.5B FP16 vs AutoAWQ subset100 task matrix

Date: `2026-06-07T14:07:54+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16']`
- task formats: `['gsm8k', 'mmlu']`
- total tasks across cases: `400`
- total passes across cases: `90`
- max accuracy drop vs `fp16`: `0.0100`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8013`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 100 | 33 | 0.3300 | 17.6514 | 0.122733 | 0.8013 | `outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_subset100_summary_2026_06_07.json` |
| `fp16` | `gsm8k` | 100 | 12 | 0.1200 | 19.0182 | 0.137708 | 0.8010 | `outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_subset100_summary_2026_06_07.json` |
| `autoawq` | `mmlu` | 100 | 34 | 0.3400 | 11.0783 | 0.188065 | 0.6035 | `outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_subset100_summary_2026_06_07.json` |
| `autoawq` | `gsm8k` | 100 | 11 | 0.1100 | 12.4491 | 0.229782 | 0.6031 | `outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_subset100_summary_2026_06_07.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `gsm8k` | 0.1200 | 0.1100 | 0.0100 |
| `autoawq` | `mmlu` | 0.3300 | 0.3400 | -0.0100 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same Matched Qwen2.5-1.5B local subset100 task evidence under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
