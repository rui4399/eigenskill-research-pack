# Projection-Role Policy Selector

Date: `2026-06-06T04:23:20+00:00`
Splits: `ifeval_v2`

This selector ranks ESMP projection-role policies across deterministic task slices. Any split-level pass-count regression is rejected before speed is considered.

## Recommendations

- `best_overall`: `vonly_layers17` (`conservative_candidate`), score `0.9174`, min speed `1.0872x`, max TTFT ratio `0.6632`
- `best_quality_preserving`: `vonly_layers17` (`conservative_candidate`), score `0.9174`, min speed `1.0872x`, max TTFT ratio `0.6632`
- `best_rejected`: `full_qkv_layers17` (`reject_quality_regression`), score `0.2888`, min speed `1.0334x`, max TTFT ratio `1.0932`

## Ranking

| rank | label | family | decision | score | total pass delta | min acc delta | min speed | max TTFT ratio | ifeval_v2 pass delta | ifeval_v2 speed |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | vonly_layers17 | v_only | conservative_candidate | 0.9174 | 0 | 0.0000 | 1.0872x | 0.6632 | 0 | 1.0872x |
| 2 | qonly_layers17 | q_only | quality_preserving_speed_neutral | 0.8996 | 0 | 0.0000 | 0.9980x | 0.7391 | 0 | 0.9980x |
| 3 | konly_layers17 | k_only | diagnostic_runtime_regression | 0.6655 | 0 | 0.0000 | 0.9366x | 0.7842 | 0 | 0.9366x |
| 4 | full_qkv_layers17 | full_qkv | reject_quality_regression | 0.2888 | -1 | -0.1250 | 1.0334x | 1.0932 | -1 | 1.0334x |
| 5 | vonly_layers1720 | v_only | reject_quality_regression | 0.2579 | -1 | -0.1250 | 0.8516x | 1.7579 | -1 | 0.8516x |

## Interpretation

- Quality regression on any split is a hard rejection for now.
- Speed is treated as secondary because deterministic task pass count is currently the scarce resource.
- A conservative candidate is not a deployment claim; it is the next policy to validate on larger task slices and real runtime paths.
