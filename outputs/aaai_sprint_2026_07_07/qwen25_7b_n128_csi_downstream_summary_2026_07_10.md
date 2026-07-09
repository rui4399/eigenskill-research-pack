# Qwen2.5-7B n128 CSI Downstream Summary

Generated: 2026-07-10

Boundary: this is a 7B n128 avg-3-bit CSI downstream stress/failure-boundary slice. It closes the missing downstream attachment for n128, but it is not positive dominance evidence.

| Item | Value |
|---|---:|
| avg bits | 2.9997 |
| bit hist | {'2': 103, '4': 94} |
| left high-bit Jaccard | 0.8269 |
| right high-bit Jaccard | 0.7963 |
| MMLU100 | 3/100 (0.03) |
| GSM8K100 | 0/100 (0.00) |

Reviewer-facing readout: the n128 CSI allocation is stable at the calibration-allocation level but collapses under the aggressive avg-3-bit downstream task setting. This should be used as failure-boundary evidence and an argument for audit/rejection gates, not as a positive accuracy claim.
