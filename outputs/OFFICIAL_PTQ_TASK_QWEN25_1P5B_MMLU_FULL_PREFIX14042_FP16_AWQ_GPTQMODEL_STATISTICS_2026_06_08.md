# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix14042 task statistics

Date: `2026-06-08T10:36:42+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `42126`
- total passes across cases: `23694`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0570`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 14042 | 8234 | 0.5864 | 0.5782 | 0.5945 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix14042_2026_06_08.json` |
| `autoawq` | `mmlu` | 14042 | 7931 | 0.5648 | 0.5566 | 0.5730 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix14042_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 14042 | 7529 | 0.5362 | 0.5279 | 0.5444 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix14042_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 14042 | -0.0216 | -0.0273 | -0.0155 | 0.0000 | 1058 | 755 |
| `gptqmodel` | `mmlu` | 14042 | -0.0502 | -0.0570 | -0.0432 | 0.0000 | 1627 | 922 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
