# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix5500 task statistics

Date: `2026-06-08T04:00:50+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `16500`
- total passes across cases: `9429`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0649`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 5500 | 3295 | 0.5991 | 0.5861 | 0.6120 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix5500_2026_06_08.json` |
| `autoawq` | `mmlu` | 5500 | 3134 | 0.5698 | 0.5567 | 0.5828 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix5500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 5500 | 3000 | 0.5455 | 0.5323 | 0.5586 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix5500_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 5500 | -0.0293 | -0.0389 | -0.0196 | 0.0000 | 467 | 306 |
| `gptqmodel` | `mmlu` | 5500 | -0.0536 | -0.0649 | -0.0418 | 0.0000 | 694 | 399 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
