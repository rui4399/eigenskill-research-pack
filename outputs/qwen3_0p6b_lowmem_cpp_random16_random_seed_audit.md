# Random Baseline Audit

Target: `cpp_loss_sensitive_budget`

Only `random_seed_*` rows are counted as random seeds; aggregate configs such as `cpp_random_budget` are excluded.

| dataset | target PPL | seed count | win/loss/tie | win rate | best seed | seed min/mean/max | margin vs best seed | margin vs seed mean |
|---|---:|---:|---:|---:|---|---|---:|---:|
| wikitext2_64_len96 | 49.5352 | 15 | 12/3/0 | 80.00% | `random_seed_20260609` | 48.5030 / 50.4787 / 52.6347 | -1.0322 | 0.9435 |
| c4_64 | 47.5872 | 15 | 15/0/0 | 100.00% | `random_seed_20260609` | 48.3840 / 49.4427 / 50.7971 | 0.7969 | 1.8556 |

Positive margins mean the target has lower PPL than the random comparator. Negative margins identify a random seed that beat the target.
