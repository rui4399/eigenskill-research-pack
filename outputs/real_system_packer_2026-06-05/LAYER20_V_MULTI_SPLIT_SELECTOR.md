# Layer-20 V Rowguard Multi-Split Selector

Date: `2026-06-06T01:23:43+00:00`
Splits: `search, heldout_v1, heldout_v2`

This selector ranks candidates across all supplied prompt splits. It treats worst-split exact match as the primary signal and penalizes split-to-split instability.

## Recommendations

- `best_overall`: `baseline_layers17` (`stable_reference`), score `0.8290`, min exact `0.9167`, exact span `0.0833`
- `best_rowguard`: `g0_1_2_4_5_6` (`candidate_needs_larger_suite`), score `0.6818`, min exact `0.7500`, exact span `0.0833`
- `stable_rowguard`: none

## Ranking

| rank | label | family | decision | score | search exact | heldout_v1 exact | heldout_v2 exact | min exact | exact span | min prefix | mean speed |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | baseline_layers17 | baseline | stable_reference | 0.8290 | 1.0000 | 0.9167 | 1.0000 | 0.9167 | 0.0833 | 0.9172 | 0.8807x |
| 2 | full_v8 | full_precision_probe | candidate_needs_larger_suite | 0.7661 | 0.8333 | 0.9167 | 1.0000 | 0.8333 | 0.1667 | 0.9096 | 0.8757x |
| 3 | g0_1_2_4_5_6 | rowguard | candidate_needs_larger_suite | 0.6818 | 0.8333 | 0.7500 | 0.7500 | 0.7500 | 0.0833 | 0.7725 | 0.9316x |
| 4 | g0_1_2_4_5_6_7 | rowguard | candidate_needs_larger_suite | 0.6761 | 1.0000 | 0.7500 | 0.7500 | 0.7500 | 0.2500 | 0.7725 | 0.8775x |
| 5 | g0_2_3_4_5_6 | rowguard | reject_for_now | 0.5201 | 0.5000 | 0.9167 | 0.9167 | 0.5000 | 0.4167 | 0.7391 | 0.9691x |

## Interpretation

- A rowguard that is perfect on one split but weak on another should remain diagnostic-only.
- A stable deployment claim requires high worst-split exact match across more prompts or task benchmarks.
- The current scoring intentionally favors robustness over speed because these prompt-suite timings are noisy and quality failures dominate.
