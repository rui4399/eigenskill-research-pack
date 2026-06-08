# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix10000 task statistics

Date: `2026-06-08T06:25:59+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `30000`
- total passes across cases: `17421`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0582`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 10000 | 6054 | 0.6054 | 0.5958 | 0.6149 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix10000_2026_06_08.json` |
| `autoawq` | `mmlu` | 10000 | 5814 | 0.5814 | 0.5717 | 0.5910 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix10000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 10000 | 5553 | 0.5553 | 0.5455 | 0.5650 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix10000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 10000 | -0.0240 | -0.0310 | -0.0173 | 0.0000 | 764 | 524 |
| `gptqmodel` | `mmlu` | 10000 | -0.0501 | -0.0582 | -0.0415 | 0.0000 | 1165 | 664 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
