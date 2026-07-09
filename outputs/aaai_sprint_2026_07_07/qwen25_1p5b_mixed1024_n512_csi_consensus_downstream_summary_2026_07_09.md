# Qwen2.5-1.5B Mixed1024 n512 CSI Consensus Downstream Summary

Generated: 2026-07-09

This artifact records a true n512 split-consensus run using two independent 512-sample draws from a mixed public 1024-prompt pool (512 WikiText2 + 512 C4).

Boundary: this is mixed-domain public calibration evidence, not pure WikiText2 n512 two-split consensus.

| Item | Value |
|---|---:|
| seed0 complete modules | 197/197 |
| seed1 complete modules | 197/197 |
| consensus avg bits | 2.9999 |
| consensus bit hist | {'4': 103, '2': 94} |
| left high-bit Jaccard | 0.8727 |
| right high-bit Jaccard | 0.8899 |
| MMLU100 | 4/100 (0.04) |
| GSM8K100 | 0/100 (0.00) |

Reviewer-facing readout: n512 split-consensus is now demonstrated under a mixed-domain 1024-prompt calibration pool. It remains a stress/closure slice; it should not be claimed as pure WikiText2 n512 consensus or as positive-only dominance evidence.
