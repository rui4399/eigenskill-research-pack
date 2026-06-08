# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix12000 task statistics

Date: `2026-06-08T08:03:06+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `36000`
- total passes across cases: `20051`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0558`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 12000 | 6968 | 0.5807 | 0.5718 | 0.5895 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix12000_2026_06_08.json` |
| `autoawq` | `mmlu` | 12000 | 6694 | 0.5578 | 0.5489 | 0.5667 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix12000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 12000 | 6389 | 0.5324 | 0.5235 | 0.5413 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix12000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 12000 | -0.0228 | -0.0294 | -0.0164 | 0.0000 | 922 | 648 |
| `gptqmodel` | `mmlu` | 12000 | -0.0483 | -0.0558 | -0.0406 | 0.0000 | 1398 | 819 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
