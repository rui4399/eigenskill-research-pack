# Qwen2.5-7B CSI Calibration Scale Summary

Generated: 2026-07-10

| N | Mean Jaccard | Left Jaccard | Right Jaccard | Avg bits | Bit hist | Source |
|---:|---:|---:|---:|---:|---|---|
| 16 | 0.6823 | 0.6273 | 0.7374 | 2.9997 | {'2': 115, '4': 82} | `qwen25_7b_wikitext2_n16_seed0_seed1_csi_consensus_2to4_budget3.json` |
| 32 | 0.6995 | 0.7000 | 0.6990 | 2.9997 | {'2': 115, '4': 82} | `qwen25_7b_wikitext2_n32_seed0_seed1_csi_consensus_2to4_budget3.json` |
| 64 | 0.8254 | 0.8431 | 0.8077 | 2.9997 | {'2': 103, '4': 94} | `qwen25_7b_wikitext2_n64_seed0_seed1_csi_consensus_2to4_budget3.json` |
| 128 | 0.8116 | 0.8269 | 0.7963 | 2.9997 | {'2': 103, '4': 94} | `qwen25_7b_wikitext2pool512_n128_seed0_seed1_csi_consensus_2to4_budget3.json` |

Qwen2.5-7B full-module CSI stability now covers n=16, n=32, n=64, and n=128. The n128 row uses independent 128-sample draws from the 512-prompt WikiText2 public pool; agreement remains high but does not monotonically dominate n64, which is useful reviewer-facing stability evidence rather than a positive-only trend.
