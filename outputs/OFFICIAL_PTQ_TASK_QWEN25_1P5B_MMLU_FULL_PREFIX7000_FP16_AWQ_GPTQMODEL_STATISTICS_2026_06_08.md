# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix7000 task statistics

Date: `2026-06-08T05:00:06+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `21000`
- total passes across cases: `12387`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0590`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 7000 | 4305 | 0.6150 | 0.6035 | 0.6263 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix7000_2026_06_08.json` |
| `autoawq` | `mmlu` | 7000 | 4121 | 0.5887 | 0.5771 | 0.6002 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix7000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 7000 | 3961 | 0.5659 | 0.5542 | 0.5774 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix7000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 7000 | -0.0263 | -0.0351 | -0.0180 | 0.0000 | 572 | 388 |
| `gptqmodel` | `mmlu` | 7000 | -0.0491 | -0.0590 | -0.0393 | 0.0000 | 832 | 488 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
