# Qwen2.5-1.5B Downstream Calibration-Size Scaling

Generated: 2026-07-09

This artifact attaches downstream MMLU100/GSM8K100 retention to the 1.5B calibration-size scaling evidence.

Boundary: n64 and n256 are two-split CSI consensus allocations; n512 is a true 512-prompt full-pool single sensitivity/allocation run, not a two-split consensus result.

| N | Allocation kind | Task | Exact/Total | Accuracy | Bit hist | Artifact |
|---:|---|---|---:|---:|---|---|
| 64 | two_split_csi_consensus | mmlu100 | 1/100 | 0.01 | 2:99, 4:98 | `qwen25_1p5b_mmlu100_csi_n64_budget3_v2.json` |
| 64 | two_split_csi_consensus | gsm8k100 | 0/100 | 0.00 | 2:99, 4:98 | `qwen25_1p5b_gsm8k100_csi_n64_budget3_v2.json` |
| 256 | two_split_csi_consensus | mmlu100 | 5/100 | 0.05 | 2:98, 4:99 | `qwen25_1p5b_mmlu100_csi_n256_budget3_v2.json` |
| 256 | two_split_csi_consensus | gsm8k100 | 0/100 | 0.00 | 2:98, 4:99 | `qwen25_1p5b_gsm8k100_csi_n256_budget3_v2.json` |
| 512 | single_full_pool_sensitivity | mmlu100 | 5/100 | 0.05 | 2:100, 4:97 | `qwen25_1p5b_mmlu100_single_n512_budget3_v2.json` |
| 512 | single_full_pool_sensitivity | gsm8k100 | 0/100 | 0.00 | 2:100, 4:97 | `qwen25_1p5b_gsm8k100_single_n512_budget3_v2.json` |

Reviewer-facing readout: MMLU100 improves from 1/100 at n64 CSI to 5/100 at n256 CSI under the same average 3-bit target, while GSM8K100 remains 0/100 in these low-bit slices. The n512 full-pool single allocation matches the n256 MMLU100 result but should not be presented as n512 CSI consensus.
