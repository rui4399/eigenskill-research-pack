# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix6500 task statistics

Date: `2026-06-08T04:44:41+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `19500`
- total passes across cases: `11419`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0598`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 6500 | 3972 | 0.6111 | 0.5992 | 0.6229 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix6500_2026_06_08.json` |
| `autoawq` | `mmlu` | 6500 | 3795 | 0.5838 | 0.5718 | 0.5958 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix6500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 6500 | 3652 | 0.5618 | 0.5498 | 0.5739 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix6500_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 6500 | -0.0272 | -0.0362 | -0.0183 | 0.0000 | 540 | 363 |
| `gptqmodel` | `mmlu` | 6500 | -0.0492 | -0.0598 | -0.0386 | 0.0000 | 781 | 461 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
