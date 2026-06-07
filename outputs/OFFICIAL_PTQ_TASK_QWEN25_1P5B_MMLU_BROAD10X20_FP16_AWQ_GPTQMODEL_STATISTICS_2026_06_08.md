# Qwen2.5-1.5B Broad MMLU 10x20 PTQ Bootstrap Statistics

Date: `2026-06-07T22:28:26+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `600`
- total passes across cases: `291`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0950`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 200 | 101 | 0.5050 | 0.4363 | 0.5735 | `outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad10x20_summary_2026_06_08.json` |
| `autoawq` | `mmlu` | 200 | 96 | 0.4800 | 0.4118 | 0.5490 | `outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_broad10x20_summary_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 200 | 94 | 0.4700 | 0.4020 | 0.5391 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad10x20_summary_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 200 | -0.0250 | -0.0800 | 0.0300 | 0.2050 | 17 | 12 |
| `gptqmodel` | `mmlu` | 200 | -0.0350 | -0.0950 | 0.0250 | 0.1315 | 22 | 15 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
