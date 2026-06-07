# Official PTQ task statistics: Qwen2.5-1.5B GSM8K full

Date: `2026-06-07T21:36:11+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['gsm8k']`
- total tasks across cases: `3957`
- total passes across cases: `307`
- bootstrap samples: `10000`
- minimum paired bootstrap delta lower bound: `-0.0243`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `gsm8k` | 1319 | 107 | 0.0811 | 0.0676 | 0.0971 | `outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8kfull_1319_summary_2026_06_08.json` |
| `autoawq` | `gsm8k` | 1319 | 104 | 0.0788 | 0.0655 | 0.0946 | `outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8kfull_1319_summary_2026_06_08.json` |
| `gptqmodel` | `gsm8k` | 1319 | 96 | 0.0728 | 0.0600 | 0.0881 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_gsm8k_gsm8kfull_1319_summary_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `gsm8k` | 1319 | -0.0023 | -0.0190 | 0.0144 | 0.4175 | 65 | 62 |
| `gptqmodel` | `gsm8k` | 1319 | -0.0083 | -0.0243 | 0.0076 | 0.1645 | 64 | 53 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
