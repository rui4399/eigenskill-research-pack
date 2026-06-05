# Random Baseline Audit

Target: `wikitext_c4_consensus`

Only `random_seed_*` rows are counted as random seeds; aggregate configs such as `cpp_random_budget` are excluded.

| dataset | target PPL | seed count | win/loss/tie | win rate | best seed | seed min/mean/max | margin vs best seed | margin vs seed mean |
|---|---:|---:|---:|---:|---|---|---:|---:|
| wikitext2_64_len96 | 45.6559 | 15 | 15/0/0 | 100.00% | `random_seed_20260609` | 48.5030 / 50.4787 / 52.6347 | 2.8471 | 4.8229 |
| c4_64 | 44.9290 | 15 | 15/0/0 | 100.00% | `random_seed_20260609` | 48.3840 / 49.4427 / 50.7971 | 3.4551 | 4.5138 |

Positive margins mean the target has lower PPL than the random comparator. Negative margins identify a random seed that beat the target.
