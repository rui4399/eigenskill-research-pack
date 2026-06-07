# Qwen2.5-1.5B Broad MMLU 5x20 PTQ Bootstrap Statistics

Date: `2026-06-07T22:05:24+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `300`
- total passes across cases: `160`
- bootstrap samples: `2000`
- minimum paired bootstrap delta lower bound: `-0.1500`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 100 | 56 | 0.5600 | 0.4623 | 0.6533 | `outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad5x20_summary_2026_06_08.json` |
| `autoawq` | `mmlu` | 100 | 54 | 0.5400 | 0.4426 | 0.6344 | `outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_broad5x20_summary_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 100 | 50 | 0.5000 | 0.4038 | 0.5962 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad5x20_summary_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 100 | -0.0200 | -0.1000 | 0.0600 | 0.3635 | 9 | 7 |
| `gptqmodel` | `mmlu` | 100 | -0.0600 | -0.1500 | 0.0300 | 0.1070 | 13 | 7 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
