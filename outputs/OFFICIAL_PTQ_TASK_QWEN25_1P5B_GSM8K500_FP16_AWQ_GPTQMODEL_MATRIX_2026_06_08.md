# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel GSM8K500 task matrix

Date: `2026-06-07T20:57:18+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k']`
- total tasks across cases: `1500`
- total passes across cases: `129`
- max accuracy drop vs `fp16`: `0.0060`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8295`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `gsm8k` | 500 | 43 | 0.0860 | 5.1042 | 0.490883 | 0.8295 | `outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_500_summary_2026_06_08.json` |
| `autoawq` | `gsm8k` | 500 | 46 | 0.0920 | 13.7360 | 0.197290 | 0.7391 | `outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8kfull_500_summary_2026_06_08.json` |
| `gptqmodel` | `gsm8k` | 500 | 40 | 0.0800 | 10.7755 | 0.256331 | 0.6784 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8kfull_500_summary_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `gsm8k` | 0.0860 | 0.0920 | -0.0060 |
| `gptqmodel` | `gsm8k` | 0.0860 | 0.0800 | 0.0060 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local GSM8K500 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
