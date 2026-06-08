# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix1500 task statistics

Date: `2026-06-08T00:50:13+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `4500`
- total passes across cases: `2420`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0693`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 1500 | 848 | 0.5653 | 0.5401 | 0.5902 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix1500_2026_06_08.json` |
| `autoawq` | `mmlu` | 1500 | 796 | 0.5307 | 0.5054 | 0.5558 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix1500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 1500 | 776 | 0.5173 | 0.4920 | 0.5425 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix1500_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 1500 | -0.0347 | -0.0533 | -0.0153 | 0.0005 | 141 | 89 |
| `gptqmodel` | `mmlu` | 1500 | -0.0480 | -0.0693 | -0.0253 | 0.0000 | 179 | 107 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
