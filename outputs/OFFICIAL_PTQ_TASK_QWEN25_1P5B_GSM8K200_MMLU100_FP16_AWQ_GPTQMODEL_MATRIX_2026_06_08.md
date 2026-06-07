# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel GSM8K200/MMLU100 task matrix

Date: `2026-06-07T19:33:42+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k', 'mmlu']`
- total tasks across cases: `900`
- total passes across cases: `153`
- max accuracy drop vs `fp16`: `0.0800`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8295`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 100 | 33 | 0.3300 | 4.8916 | 0.411118 | 0.8292 | `outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json` |
| `fp16` | `gsm8k` | 200 | 19 | 0.0950 | 5.1380 | 0.496600 | 0.8295 | `outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json` |
| `autoawq` | `mmlu` | 100 | 34 | 0.3400 | 12.5189 | 0.164839 | 0.7391 | `outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json` |
| `autoawq` | `gsm8k` | 200 | 22 | 0.1100 | 13.4012 | 0.210373 | 0.7391 | `outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 100 | 25 | 0.2500 | 10.3074 | 0.206272 | 0.6761 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json` |
| `gptqmodel` | `gsm8k` | 200 | 20 | 0.1000 | 10.8337 | 0.262601 | 0.6767 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `gsm8k` | 0.0950 | 0.1100 | -0.0150 |
| `gptqmodel` | `gsm8k` | 0.0950 | 0.1000 | -0.0050 |
| `autoawq` | `mmlu` | 0.3300 | 0.3400 | -0.0100 |
| `gptqmodel` | `mmlu` | 0.3300 | 0.2500 | 0.0800 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local GSM8K200 plus MMLU100 task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
