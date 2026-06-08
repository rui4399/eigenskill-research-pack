# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix4000 task statistics

Date: `2026-06-08T02:54:21+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `12000`
- total passes across cases: `6762`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0685`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 4000 | 2366 | 0.5915 | 0.5762 | 0.6066 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix4000_2026_06_08.json` |
| `autoawq` | `mmlu` | 4000 | 2251 | 0.5627 | 0.5473 | 0.5781 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix4000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 4000 | 2145 | 0.5363 | 0.5208 | 0.5517 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix4000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 4000 | -0.0288 | -0.0405 | -0.0173 | 0.0000 | 342 | 227 |
| `gptqmodel` | `mmlu` | 4000 | -0.0553 | -0.0685 | -0.0413 | 0.0000 | 502 | 281 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
