# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU second-shard task statistics

Date: `2026-06-08T00:28:49+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `1500`
- total passes across cases: `868`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0720`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 500 | 300 | 0.6000 | 0.5565 | 0.6420 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_500_1000_2026_06_08.json` |
| `autoawq` | `mmlu` | 500 | 288 | 0.5760 | 0.5323 | 0.6186 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_500_1000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 500 | 280 | 0.5600 | 0.5162 | 0.6029 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_500_1000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 500 | -0.0240 | -0.0560 | 0.0080 | 0.0747 | 37 | 25 |
| `gptqmodel` | `mmlu` | 500 | -0.0400 | -0.0720 | -0.0060 | 0.0125 | 46 | 26 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
