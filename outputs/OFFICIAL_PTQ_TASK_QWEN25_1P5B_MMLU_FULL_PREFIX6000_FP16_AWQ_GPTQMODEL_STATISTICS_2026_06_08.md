# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix6000 task statistics

Date: `2026-06-08T04:24:32+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `18000`
- total passes across cases: `10413`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0627`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 6000 | 3630 | 0.6050 | 0.5926 | 0.6173 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix6000_2026_06_08.json` |
| `autoawq` | `mmlu` | 6000 | 3463 | 0.5772 | 0.5646 | 0.5896 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix6000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 6000 | 3320 | 0.5533 | 0.5407 | 0.5659 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix6000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 6000 | -0.0278 | -0.0370 | -0.0187 | 0.0000 | 503 | 336 |
| `gptqmodel` | `mmlu` | 6000 | -0.0517 | -0.0627 | -0.0407 | 0.0000 | 741 | 431 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
