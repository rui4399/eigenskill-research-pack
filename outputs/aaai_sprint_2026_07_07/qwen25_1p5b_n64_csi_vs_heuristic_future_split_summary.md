# Qwen2.5-1.5B n64 CSI-vs-Heuristic Future-Split Check

This is a calibration-sensitivity prediction check, not downstream task-retention evidence. Seeds 2--4 were run under intentional GPU contention; use for stability ranking evidence, not efficiency evidence.

| Score | Pearson | Spearman | Kendall tau |
|---|---:|---:|---:|
| two_split_mean | 0.9951 | 0.8959 | 0.7664 |
| single_split_seed0 | 0.9939 | 0.8715 | 0.7434 |
| two_split_min | 0.9950 | 0.8696 | 0.7627 |
| csi_lcb_proxy | 0.9950 | 0.8696 | 0.7627 |
| single_split_seed1 | 0.9948 | 0.8505 | 0.7192 |
| csi_lcb_per_param | 0.1780 | 0.7209 | 0.5676 |
| param_count | 0.7562 | 0.2905 | 0.2671 |
| random_fixed | -0.0071 | 0.1485 | 0.1244 |
| split_agreement_proxy | -0.4738 | -0.6185 | -0.4641 |

Best by Spearman: `two_split_mean`.
