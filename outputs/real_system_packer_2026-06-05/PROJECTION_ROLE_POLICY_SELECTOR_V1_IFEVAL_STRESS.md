# Projection-Role Policy Selector

Date: `2026-06-06T05:55:21+00:00`
Splits: `v1_32tok, ifeval_v2, stress_v2`

This selector ranks ESMP projection-role policies across deterministic task slices. Any split-level pass-count regression is rejected before speed is considered.

## Recommendations

- `best_overall`: `qonly_layers17` (`quality_preserving_speed_neutral`), score `0.9118`, min speed `0.9980x`, max TTFT ratio `0.9761`
- `best_quality_preserving`: `qonly_layers17` (`quality_preserving_speed_neutral`), score `0.9118`, min speed `0.9980x`, max TTFT ratio `0.9761`
- `best_rejected`: `konly_layers17` (`reject_quality_regression`), score `0.3106`, min speed `0.9366x`, max TTFT ratio `0.8943`

## Ranking

| rank | label | family | decision | score | total pass delta | min acc delta | min speed | max TTFT ratio | v1_32tok pass delta | ifeval_v2 pass delta | stress_v2 pass delta | v1_32tok speed | ifeval_v2 speed | stress_v2 speed |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | qonly_layers17 | q_only | quality_preserving_speed_neutral | 0.9118 | 0 | 0.0000 | 0.9980x | 0.9761 | 0 | 0 | 0 | 1.1926x | 0.9980x | 1.0080x |
| 2 | konly_layers17 | k_only | reject_quality_regression | 0.3106 | -1 | -0.0238 | 0.9366x | 0.8943 | 0 | 0 | -1 | 0.9410x | 0.9366x | 1.0028x |
| 3 | vonly_layers17 | v_only | reject_quality_regression | 0.3009 | -1 | -0.0238 | 0.9924x | 1.3856 | 0 | 0 | -1 | 1.0142x | 1.0872x | 0.9924x |

## Interpretation

- Quality regression on any split is a hard rejection for now.
- Speed is treated as secondary because deterministic task pass count is currently the scarce resource.
- A conservative candidate is not a deployment claim; it is the next policy to validate on larger task slices and real runtime paths.
