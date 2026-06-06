# Projection-Role Policy Selector

Date: `2026-06-06T06:15:25+00:00`
Splits: `v1_32tok, ifeval_v2, stress_v2, stress_v3_84`

This selector ranks ESMP projection-role policies across deterministic task slices. Any split-level pass-count regression is rejected before speed is considered.

## Recommendations

- `best_overall`: `konly_layers17` (`reject_quality_regression`), score `0.3107`, min speed `0.9366x`, max TTFT ratio `0.9746`
- `best_quality_preserving`: none
- `best_rejected`: `konly_layers17` (`reject_quality_regression`), score `0.3107`, min speed `0.9366x`, max TTFT ratio `0.9746`

## Ranking

| rank | label | family | decision | score | total pass delta | min acc delta | min speed | max TTFT ratio | v1_32tok pass delta | ifeval_v2 pass delta | stress_v2 pass delta | stress_v3_84 pass delta | v1_32tok speed | ifeval_v2 speed | stress_v2 speed | stress_v3_84 speed |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | konly_layers17 | k_only | reject_quality_regression | 0.3107 | -2 | -0.0238 | 0.9366x | 0.9746 | 0 | 0 | -1 | -1 | 0.9410x | 0.9366x | 1.0028x | 0.9746x |
| 2 | qonly_layers17 | q_only | reject_quality_regression | 0.3075 | -1 | -0.0119 | 0.9272x | 1.1942 | 0 | 0 | 0 | -1 | 1.1926x | 0.9980x | 1.0080x | 0.9272x |
| 3 | vonly_layers17 | v_only | reject_quality_regression | 0.2984 | -4 | -0.0357 | 0.9653x | 1.3856 | 0 | 0 | -1 | -3 | 1.0142x | 1.0872x | 0.9924x | 0.9653x |

## Interpretation

- Quality regression on any split is a hard rejection for now.
- Speed is treated as secondary because deterministic task pass count is currently the scarce resource.
- A conservative candidate is not a deployment claim; it is the next policy to validate on larger task slices and real runtime paths.
