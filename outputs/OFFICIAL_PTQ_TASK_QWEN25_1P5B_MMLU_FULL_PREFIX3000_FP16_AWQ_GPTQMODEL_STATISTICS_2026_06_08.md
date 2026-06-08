# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix3000 task statistics

Date: `2026-06-08T02:03:07+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `9000`
- total passes across cases: `4816`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0690`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 3000 | 1687 | 0.5623 | 0.5445 | 0.5800 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix3000_2026_06_08.json` |
| `autoawq` | `mmlu` | 3000 | 1601 | 0.5337 | 0.5158 | 0.5515 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix3000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 3000 | 1528 | 0.5093 | 0.4914 | 0.5272 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix3000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 3000 | -0.0287 | -0.0427 | -0.0150 | 0.0003 | 273 | 187 |
| `gptqmodel` | `mmlu` | 3000 | -0.0530 | -0.0690 | -0.0360 | 0.0000 | 387 | 228 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
