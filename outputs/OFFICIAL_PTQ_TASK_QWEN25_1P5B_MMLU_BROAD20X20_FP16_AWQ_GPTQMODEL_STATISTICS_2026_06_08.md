# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel MMLU broad20x20 task statistics

Date: `2026-06-07T23:12:14+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `1200`
- total passes across cases: `616`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0825`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 400 | 214 | 0.5350 | 0.4860 | 0.5833 | `outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json` |
| `autoawq` | `mmlu` | 400 | 204 | 0.5100 | 0.4611 | 0.5587 | `outputs/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 400 | 198 | 0.4950 | 0.4463 | 0.5438 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 400 | -0.0250 | -0.0600 | 0.0125 | 0.1035 | 33 | 23 |
| `gptqmodel` | `mmlu` | 400 | -0.0400 | -0.0825 | 0.0075 | 0.0465 | 51 | 35 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
