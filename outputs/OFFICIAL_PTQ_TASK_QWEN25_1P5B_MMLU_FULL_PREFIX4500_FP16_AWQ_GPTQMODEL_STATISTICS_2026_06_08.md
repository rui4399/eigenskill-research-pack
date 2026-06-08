# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix4500 task statistics

Date: `2026-06-08T03:16:23+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `13500`
- total passes across cases: `7469`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0691`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 4500 | 2614 | 0.5809 | 0.5664 | 0.5952 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix4500_2026_06_08.json` |
| `autoawq` | `mmlu` | 4500 | 2495 | 0.5544 | 0.5399 | 0.5689 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix4500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 4500 | 2360 | 0.5244 | 0.5098 | 0.5390 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix4500_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 4500 | -0.0264 | -0.0373 | -0.0158 | 0.0000 | 387 | 268 |
| `gptqmodel` | `mmlu` | 4500 | -0.0564 | -0.0691 | -0.0436 | 0.0000 | 587 | 333 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
