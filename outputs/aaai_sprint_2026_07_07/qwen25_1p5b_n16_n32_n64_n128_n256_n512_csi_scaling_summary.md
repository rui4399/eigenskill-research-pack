# Qwen2.5-1.5B CSI Calibration Scaling Summary

Generated: 2026-07-09

| N | Evidence type | Mean high-bit Jaccard | Avg bits | Protected positive delta | Bit hist | Note |
|---:|---|---:|---:|---:|---|---|
| 16 | two_split_consensus | 0.677 | 2.9999 | 0.8889 | {'2': 108, '4': 89} | distinct sampled splits |
| 32 | two_split_consensus | 0.740 | 2.9999 | 0.9104 | {'2': 108, '4': 89} | distinct sampled splits |
| 64 | two_split_consensus | 0.849 | 2.9999 | 0.9222 | {'2': 99, '4': 98} | distinct sampled splits |
| 128 | two_split_consensus | 0.990 | 2.9999 | 0.9260 | {'2': 94, '4': 103} | legacy full-pool upper bound; seed0/seed1 select same 128-prompt pool |
| 256 | two_split_consensus | 0.908 | 2.9999 | 0.9113 | {'2': 98, '4': 99} | distinct sampled splits from 512-prompt public WikiText2 pool |
| 512 | single_full_pool_sensitivity | n/a | 2.9988 | 0.9136 | {'2': 100, '4': 97} | completed 512-prompt full-pool sensitivity/allocation; not seed-perturbation or two-split consensus evidence |

## Interpretation

Agreement improves from n=16 to n=64. n128 is a legacy full-pool upper bound, n256 is the larger distinct-split point, and n512 closes the sensitivity/allocation side as a completed full-pool run rather than a seed-perturbation curve point.

The n512 row is a true 512-prompt measurement (`prompt_count=512`, 197/197 modules), but it is intentionally not reported as split agreement because no independent second full-pool split was completed.
