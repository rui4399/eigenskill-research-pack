# Random Baseline Audit

Target: `wikitext_c4_consensus`

Only explicit random-seed rows are counted as random seeds. Accepted prefixes are `random_seed_*` and `random_budget_seed_*`; aggregate configs such as `cpp_random_budget` are excluded.

| dataset | target PPL | seed count | win/loss/tie | win rate | best seed | seed min/mean/max | margin vs best seed | margin vs seed mean |
|---|---:|---:|---:|---:|---|---|---:|---:|
| c4_128 | 32.8806 | 16 | 16/0/0 | 100.00% | `random_budget_seed_20260612` | 33.1374 / 34.3623 / 35.1416 | 0.2568 | 1.4817 |

Positive margins mean the target has lower PPL than the random comparator. Negative margins identify a random seed that beat the target.
