# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix2000 task statistics

Date: `2026-06-08T01:08:57+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `6000`
- total passes across cases: `3208`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0725`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 2000 | 1128 | 0.5640 | 0.5422 | 0.5856 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix2000_2026_06_08.json` |
| `autoawq` | `mmlu` | 2000 | 1060 | 0.5300 | 0.5081 | 0.5518 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix2000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 2000 | 1020 | 0.5100 | 0.4881 | 0.5319 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix2000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 2000 | -0.0340 | -0.0500 | -0.0170 | 0.0000 | 184 | 116 |
| `gptqmodel` | `mmlu` | 2000 | -0.0540 | -0.0725 | -0.0345 | 0.0000 | 250 | 142 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
