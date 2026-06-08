# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix2500 task statistics

Date: `2026-06-08T01:37:57+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `7500`
- total passes across cases: `3950`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0712`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 2500 | 1387 | 0.5548 | 0.5352 | 0.5742 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix2500_2026_06_08.json` |
| `autoawq` | `mmlu` | 2500 | 1311 | 0.5244 | 0.5048 | 0.5439 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix2500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 2500 | 1252 | 0.5008 | 0.4812 | 0.5204 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix2500_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 2500 | -0.0304 | -0.0452 | -0.0144 | 0.0000 | 231 | 155 |
| `gptqmodel` | `mmlu` | 2500 | -0.0540 | -0.0712 | -0.0368 | 0.0000 | 323 | 188 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
