# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel GSM8K800 task matrix

Date: `2026-06-07T21:19:40+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k']`
- total tasks across cases: `2400`
- total passes across cases: `184`
- max accuracy drop vs `fp16`: `0.0038`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8295`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `gsm8k` | 800 | 61 | 0.0762 | 5.1468 | 0.495307 | 0.8295 | `outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_800_summary_2026_06_08.json` |
| `autoawq` | `gsm8k` | 800 | 65 | 0.0813 | 13.7211 | 0.198943 | 0.7391 | `outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8kfull_800_summary_2026_06_08.json` |
| `gptqmodel` | `gsm8k` | 800 | 58 | 0.0725 | 10.8905 | 0.257396 | 0.6791 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8kfull_800_summary_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `gsm8k` | 0.0762 | 0.0813 | -0.0050 |
| `gptqmodel` | `gsm8k` | 0.0762 | 0.0725 | 0.0038 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local GSM8K800 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
