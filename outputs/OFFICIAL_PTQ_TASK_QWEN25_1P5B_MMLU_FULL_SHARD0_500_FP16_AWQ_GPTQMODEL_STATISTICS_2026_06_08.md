# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU first-shard task statistics

Date: `2026-06-08T00:05:02+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `1500`
- total passes across cases: `815`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0880`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 500 | 284 | 0.5680 | 0.5242 | 0.6107 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_0_500_2026_06_08.json` |
| `autoawq` | `mmlu` | 500 | 271 | 0.5420 | 0.4982 | 0.5852 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_0_500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 500 | 260 | 0.5200 | 0.4762 | 0.5635 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_0_500_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 500 | -0.0260 | -0.0620 | 0.0120 | 0.0978 | 52 | 39 |
| `gptqmodel` | `mmlu` | 500 | -0.0480 | -0.0880 | -0.0080 | 0.0120 | 63 | 39 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
