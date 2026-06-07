# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel GSM8K800 task statistics

Date: `2026-06-07T21:19:46+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k']`
- total tasks across cases: `2400`
- total passes across cases: `184`
- bootstrap samples: `10000`
- minimum paired bootstrap delta lower bound: `-0.0238`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `gsm8k` | 800 | 61 | 0.0762 | 0.0598 | 0.0967 | `outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_800_summary_2026_06_08.json` |
| `autoawq` | `gsm8k` | 800 | 65 | 0.0813 | 0.0643 | 0.1022 | `outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8kfull_800_summary_2026_06_08.json` |
| `gptqmodel` | `gsm8k` | 800 | 58 | 0.0725 | 0.0565 | 0.0926 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8kfull_800_summary_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `gsm8k` | 800 | 0.0050 | -0.0163 | 0.0262 | 0.6994 | 36 | 40 |
| `gptqmodel` | `gsm8k` | 800 | -0.0038 | -0.0238 | 0.0163 | 0.3762 | 37 | 34 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
