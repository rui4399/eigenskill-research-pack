# Qwen2.5-1.5B CSI Calibration Scaling Summary

Generated: 2026-07-09

| N | Mean high-bit Jaccard | Left Jaccard | Right Jaccard | Avg bits | Bit hist | Note |
|---:|---:|---:|---:|---:|---|---|
| 16 | 0.677 | 0.708 | 0.645 | 2.9999 | {'2': 108, '4': 89} | distinct sampled splits |
| 32 | 0.740 | 0.752 | 0.727 | 2.9999 | {'2': 108, '4': 89} | distinct sampled splits |
| 64 | 0.849 | 0.849 | 0.849 | 2.9999 | {'2': 99, '4': 98} | distinct sampled splits |
| 128 | 0.990 | 0.990 | 0.990 | 2.9999 | {'2': 94, '4': 103} | full-pool upper bound; seed0/seed1 select same 128-prompt pool |
| 256 | 0.908 | 0.931 | 0.885 | 2.9999 | {'2': 98, '4': 99} | distinct sampled splits from 512-prompt public WikiText2 pool |

## Interpretation

Agreement improves from n=16 to n=64; n=128 is a legacy full-pool upper bound, while n=256 uses the new 512-prompt public pool and remains high but below the full-pool ceiling.

The n256 row is new evidence from the 512-prompt public WikiText2 pool and should replace the earlier readiness-only wording in the sprint audit.
