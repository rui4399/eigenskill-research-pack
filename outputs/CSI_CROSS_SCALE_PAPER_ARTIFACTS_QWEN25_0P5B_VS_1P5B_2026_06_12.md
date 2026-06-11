# CSI Cross-Scale Paper Artifacts

Date: `2026-06-11T17:06:57+00:00`
Status: **PASS**
Figure: `outputs\CSI_CROSS_SCALE_DUAL_CURVE_QWEN25_0P5B_VS_1P5B_2026_06_12.svg`

## Same-n Stability Table

| n | metric | 0.5B | 1.5B | 1.5B - 0.5B |
|---:|---|---:|---:|---:|
| 2 | Spearman | 0.3725 | 0.1410 | -0.2315 |
| 2 | Top-20 Jaccard | 0.3797 | 0.2604 | -0.1193 |
| 2 | Positive Jaccard | 0.5485 | 0.4244 | -0.1240 |
| 4 | Spearman | 0.4324 | 0.2869 | -0.1455 |
| 4 | Top-20 Jaccard | 0.4672 | 0.3313 | -0.1359 |
| 4 | Positive Jaccard | 0.5734 | 0.5189 | -0.0545 |
| 8 | Spearman | 0.6645 | 0.4918 | -0.1727 |
| 8 | Top-20 Jaccard | 0.6449 | 0.4401 | -0.2048 |
| 8 | Positive Jaccard | 0.7282 | 0.5992 | -0.1291 |

## n=2 to n=8 Gain Table

| metric | n range | 0.5B gain | 1.5B gain | 1.5B gain - 0.5B gain |
|---|---|---:|---:|---:|
| Spearman | 2 -> 8 | 0.2920 | 0.3508 | 0.0588 |
| Top-20 Jaccard | 2 -> 8 | 0.2651 | 0.1797 | -0.0855 |
| Positive Jaccard | 2 -> 8 | 0.1797 | 0.1747 | -0.0050 |

## Paper Claim

For the audited Qwen2.5 artifacts, 1.5B has lower CSI stability than 0.5B at each shared n in all three metrics, while both scales improve from n=2 to n=8. This is a cross-scale replication and comparison, not a causal scaling-law claim.

## Source Artifacts

- `Qwen2.5-0.5B`: `outputs\csi_vs_n_curve_qwen25_0p5b_2026_06_07.json`
- `Qwen2.5-1.5B`: `outputs\csi_vs_n_curve_qwen25_1p5b_2026_06_11.json`

## Failures

- none
