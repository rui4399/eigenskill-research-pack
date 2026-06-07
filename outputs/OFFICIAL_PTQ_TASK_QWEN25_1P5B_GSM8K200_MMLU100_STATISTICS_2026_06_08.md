# Qwen2.5-1.5B FP16 vs AutoAWQ GSM8K200/MMLU100 task statistics

Date: `2026-06-07T17:54:34+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16']`
- task formats: `['gsm8k', 'mmlu']`
- total tasks across cases: `600`
- total passes across cases: `108`
- bootstrap samples: `10000`
- minimum paired bootstrap delta lower bound: `-0.1000`

## Case Accuracy Intervals

| variant | format | tasks | passes | accuracy | Wilson low | Wilson high | source |
|---|---|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 100 | 33 | 0.3300 | 0.2456 | 0.4269 | `outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json` |
| `fp16` | `gsm8k` | 200 | 19 | 0.0950 | 0.0617 | 0.1436 | `outputs/official_ptq_task_fp16_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json` |
| `autoawq` | `mmlu` | 100 | 34 | 0.3400 | 0.2546 | 0.4372 | `outputs/official_ptq_task_awq_qwen25_1p5b_mmlu_gsm8k200_mmlu100_summary_2026_06_08.json` |
| `autoawq` | `gsm8k` | 200 | 22 | 0.1100 | 0.0738 | 0.1609 | `outputs/official_ptq_task_awq_qwen25_1p5b_gsm8k_gsm8k200_mmlu100_summary_2026_06_08.json` |

## Paired Comparisons

| variant | format | shared tasks | delta cand-base | CI low | CI high | P(delta>=0) | b-only | cand-only |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `autoawq` | `gsm8k` | 200 | 0.0150 | -0.0350 | 0.0650 | 0.7583 | 12 | 15 |
| `autoawq` | `mmlu` | 100 | 0.0100 | -0.1000 | 0.1300 | 0.5903 | 16 | 17 |

## Failures

- none

## Claim Boundary

- Valid claim: this gate reports statistical uncertainty for an already-guarded local official-PTQ task matrix, including Wilson accuracy intervals, paired bootstrap candidate-minus-baseline deltas, and discordant-pair counts. Invalid claim: this does not prove leaderboard-scale retention, statistical superiority, SOTA PTQ quality, production speedup, mobile deployment, or energy savings.
