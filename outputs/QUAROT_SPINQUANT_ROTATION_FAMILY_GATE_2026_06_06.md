# Rotation Family Proxy Gate

Date: `2026-06-06T14:05:20+00:00`
Status: **PASS**
Cases: `2`
Total records: `394`
Total rotated: `167`

## Cases

| case | method | records | rotated | cost frac | budget | reduction | policies |
|---|---|---:|---:|---:|---:|---:|---|
| `wikitext2` | `quarot_spinquant_style_rotation_baseline_proxy` | 197 | 82 | 0.348362 | 0.350000 | 0.084759 | `{'none': 115, 'quarot_static_hadamard_proxy': 24, 'spinquant_learned_rotation_proxy': 58}` |
| `c4` | `quarot_spinquant_style_rotation_baseline_proxy` | 197 | 85 | 0.348362 | 0.350000 | 0.101966 | `{'quarot_static_hadamard_proxy': 25, 'none': 112, 'spinquant_learned_rotation_proxy': 60}` |

## Failures

- none

## Claim Boundary

- Valid claim: QuaRot/SpinQuant-style rotation-family proxy artifacts exist, rotate measured modules under budget, and record projected sensitivity reduction. Invalid claim: this is a faithful official QuaRot/SpinQuant reproduction or proof of activation-rotation quality retention.
