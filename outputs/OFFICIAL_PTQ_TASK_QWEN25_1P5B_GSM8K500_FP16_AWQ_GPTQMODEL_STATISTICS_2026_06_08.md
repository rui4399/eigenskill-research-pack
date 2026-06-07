# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel GSM8K500 task statistics

Date: `2026-06-07T20:57:21+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k']`
- total tasks across cases: `1500`
- total passes across cases: `129`
- bootstrap samples: `10000`
- minimum paired bootstrap delta lower bound: `-0.0340`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `gsm8k` | 500 | 43 | 0.0860 | 0.0645 | 0.1138 | `outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_500_summary_2026_06_08.json` |
| `autoawq` | `gsm8k` | 500 | 46 | 0.0920 | 0.0697 | 0.1205 | `outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8kfull_500_summary_2026_06_08.json` |
| `gptqmodel` | `gsm8k` | 500 | 40 | 0.0800 | 0.0593 | 0.1071 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8kfull_500_summary_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `gsm8k` | 500 | 0.0060 | -0.0220 | 0.0340 | 0.6897 | 25 | 28 |
| `gptqmodel` | `gsm8k` | 500 | -0.0060 | -0.0340 | 0.0220 | 0.3656 | 28 | 25 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
