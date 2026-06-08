# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix3500 task statistics

Date: `2026-06-08T02:24:16+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `10500`
- total passes across cases: `5725`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0646`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 3500 | 1999 | 0.5711 | 0.5547 | 0.5875 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix3500_2026_06_08.json` |
| `autoawq` | `mmlu` | 3500 | 1902 | 0.5434 | 0.5269 | 0.5599 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix3500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 3500 | 1824 | 0.5211 | 0.5046 | 0.5377 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix3500_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 3500 | -0.0277 | -0.0403 | -0.0151 | 0.0000 | 307 | 210 |
| `gptqmodel` | `mmlu` | 3500 | -0.0500 | -0.0646 | -0.0346 | 0.0000 | 445 | 270 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
