# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix1000 task statistics

Date: `2026-06-08T00:30:43+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `3000`
- total passes across cases: `1683`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0710`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 1000 | 584 | 0.5840 | 0.5532 | 0.6142 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix1000_2026_06_08.json` |
| `autoawq` | `mmlu` | 1000 | 559 | 0.5590 | 0.5281 | 0.5895 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix1000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 1000 | 540 | 0.5400 | 0.5090 | 0.5707 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix1000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 1000 | -0.0250 | -0.0480 | -0.0010 | 0.0243 | 89 | 64 |
| `gptqmodel` | `mmlu` | 1000 | -0.0440 | -0.0710 | -0.0180 | 0.0003 | 109 | 65 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
