# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix8000 task statistics

Date: `2026-06-08T05:26:01+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `24000`
- total passes across cases: `14582`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0583`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 8000 | 5059 | 0.6324 | 0.6217 | 0.6429 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix8000_2026_06_08.json` |
| `autoawq` | `mmlu` | 8000 | 4858 | 0.6072 | 0.5965 | 0.6179 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix8000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 8000 | 4665 | 0.5831 | 0.5723 | 0.5939 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix8000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 8000 | -0.0251 | -0.0328 | -0.0175 | 0.0000 | 627 | 426 |
| `gptqmodel` | `mmlu` | 8000 | -0.0493 | -0.0583 | -0.0400 | 0.0000 | 930 | 536 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
