# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix5000 task statistics

Date: `2026-06-08T03:39:39+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `15000`
- total passes across cases: `8346`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0670`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 5000 | 2921 | 0.5842 | 0.5705 | 0.5978 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix5000_2026_06_08.json` |
| `autoawq` | `mmlu` | 5000 | 2778 | 0.5556 | 0.5418 | 0.5693 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix5000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 5000 | 2647 | 0.5294 | 0.5155 | 0.5432 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix5000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 5000 | -0.0286 | -0.0388 | -0.0182 | 0.0000 | 432 | 289 |
| `gptqmodel` | `mmlu` | 5000 | -0.0548 | -0.0670 | -0.0426 | 0.0000 | 644 | 370 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
