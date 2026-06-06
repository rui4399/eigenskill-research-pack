# Projection-Role Policy Selector

Date: `2026-06-06T04:23:20+00:00`
Splits: `v1_32, ifeval_v2`

This selector ranks ESMP projection-role policies across deterministic task slices. Any split-level pass-count regression is rejected before speed is considered.

## Recommendations

- `best_overall`: `vonly_layers17` (`conservative_candidate`), score `0.9099`, min speed `1.0142x`, max TTFT ratio `0.9302`
- `best_quality_preserving`: `vonly_layers17` (`conservative_candidate`), score `0.9099`, min speed `1.0142x`, max TTFT ratio `0.9302`
- `best_rejected`: `full_qkv_layers17` (`reject_quality_regression`), score `0.2841`, min speed `0.9157x`, max TTFT ratio `1.4734`

## Ranking

| rank | label | family | decision | score | total pass delta | min acc delta | min speed | max TTFT ratio | v1_32 pass delta | ifeval_v2 pass delta | v1_32 speed | ifeval_v2 speed |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | vonly_layers17 | v_only | conservative_candidate | 0.9099 | 0 | 0.0000 | 1.0142x | 0.9302 | 0 | 0 | 1.0142x | 1.0872x |
| 2 | full_qkv_layers17 | full_qkv | reject_quality_regression | 0.2841 | -1 | -0.1250 | 0.9157x | 1.4734 | 0 | -1 | 0.9157x | 1.0334x |
| 3 | vonly_layers1720 | v_only | reject_quality_regression | 0.2528 | -1 | -0.1250 | 0.6903x | 2.7642 | 0 | -1 | 0.6903x | 0.8516x |

## Interpretation

- Quality regression on any split is a hard rejection for now.
- Speed is treated as secondary because deterministic task pass count is currently the scarce resource.
- A conservative candidate is not a deployment claim; it is the next policy to validate on larger task slices and real runtime paths.
