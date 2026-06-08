# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix11000 task statistics

Date: `2026-06-08T07:05:50+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `33000`
- total passes across cases: `18860`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0575`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 11000 | 6554 | 0.5958 | 0.5866 | 0.6050 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix11000_2026_06_08.json` |
| `autoawq` | `mmlu` | 11000 | 6295 | 0.5723 | 0.5630 | 0.5815 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix11000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 11000 | 6011 | 0.5465 | 0.5371 | 0.5557 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix11000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 11000 | -0.0235 | -0.0301 | -0.0168 | 0.0000 | 839 | 580 |
| `gptqmodel` | `mmlu` | 11000 | -0.0494 | -0.0575 | -0.0415 | 0.0000 | 1284 | 741 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
