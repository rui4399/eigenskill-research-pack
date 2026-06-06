# Layer-20 V Rowguard Split-Consensus Selector

Date: `2026-06-06T01:01:34+00:00`

This selector ranks precision policies with a conservative split-consensus score. It is a policy-selection audit, not a new generation benchmark.

## Recommendations

- `best_overall`: `baseline_layers17` (`stable_reference`), score `0.8339`, min exact `0.9167`, held-out exact `0.9167`, gap `0.0833`
- `best_rowguard`: `g0_1_2_4_5_6` (`candidate_needs_third_split`), score `0.6920`, min exact `0.7500`, held-out exact `0.7500`, gap `0.0833`
- `stable_rowguard`: none

## Ranking

| rank | label | family | decision | score | train exact | held-out exact | min exact | harmonic | abs gap | held-out prefix | held-out speed | risk |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | baseline_layers17 | baseline | stable_reference | 0.8339 | 1.0000 | 0.9167 | 0.9167 | 0.9565 | 0.0833 | 0.9172 | 0.8316x | small_gap |
| 2 | full_v8 | full_precision_probe | candidate_needs_third_split | 0.7855 | 0.8333 | 0.9167 | 0.8333 | 0.8730 | 0.0833 | 0.9172 | 0.9427x | stable_or_improved |
| 3 | g0_1_2_4_5_6 | rowguard | candidate_needs_third_split | 0.6920 | 0.8333 | 0.7500 | 0.7500 | 0.7895 | 0.0833 | 0.7725 | 0.9520x | small_gap |
| 4 | g0_1_2_4_5_6_7 | rowguard | diagnostic_only_gap_sensitive | 0.6759 | 1.0000 | 0.7500 | 0.7500 | 0.8571 | 0.2500 | 0.7725 | 0.7947x | high_overfit |
| 5 | g0_1_2_3_4_5_6 | rowguard | reject_for_now | 0.6588 | 0.6667 | 0.9167 | 0.6667 | 0.7719 | 0.2500 | 0.9172 | 0.8546x | stable_or_improved |
| 6 | g0_1_4_5_6_7 | rowguard | reject_for_now | 0.6334 | 0.6667 | 0.6667 | 0.6667 | 0.6667 | 0.0000 | 0.7777 | 0.9146x | stable_or_improved |
| 7 | g0_1_3_4_5_6 | rowguard | reject_for_now | 0.5610 | 0.6667 | 0.5833 | 0.5833 | 0.6222 | 0.0833 | 0.6949 | 0.9597x | small_gap |
| 8 | g0_2_4_5_6_7 | rowguard | reject_for_now | 0.5402 | 0.5000 | 0.8333 | 0.5000 | 0.6250 | 0.3333 | 0.8553 | 0.9793x | stable_or_improved |
| 9 | g0_2_3_4_5_6 | rowguard | reject_for_now | 0.5292 | 0.5000 | 0.9167 | 0.5000 | 0.6471 | 0.4167 | 0.9172 | 0.9720x | stable_or_improved |
| 10 | g0_3_4_5_6_7 | rowguard | reject_for_now | 0.5104 | 0.5000 | 0.7500 | 0.5000 | 0.6000 | 0.2500 | 0.8413 | 0.9778x | stable_or_improved |

## Conservative Interpretation

- The safest observed policy remains the existing baseline precision guard when optimizing worst-split exact match.
- No rowguard policy should be presented as generalized yet unless it also survives a third prompt split or a larger held-out suite.
- The strongest rowguard result is useful as a next candidate, not as a deployment claim.
