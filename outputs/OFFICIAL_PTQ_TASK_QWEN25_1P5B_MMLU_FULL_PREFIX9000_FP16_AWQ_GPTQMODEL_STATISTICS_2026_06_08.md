# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU prefix9000 task statistics

Date: `2026-06-08T05:55:57+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `27000`
- total passes across cases: `15956`
- bootstrap samples: `4000`
- minimum paired bootstrap delta lower bound: `-0.0591`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 9000 | 5539 | 0.6154 | 0.6053 | 0.6254 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix9000_2026_06_08.json` |
| `autoawq` | `mmlu` | 9000 | 5331 | 0.5923 | 0.5821 | 0.6024 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_prefix9000_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 9000 | 5086 | 0.5651 | 0.5548 | 0.5753 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_prefix9000_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `mmlu` | 9000 | -0.0231 | -0.0306 | -0.0159 | 0.0000 | 689 | 481 |
| `gptqmodel` | `mmlu` | 9000 | -0.0503 | -0.0591 | -0.0413 | 0.0000 | 1050 | 597 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
