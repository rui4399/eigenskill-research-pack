# Consensus Transfer Boundary Gate

Date: `2026-06-06T17:39:28+00:00`
Status: **PASS**

## Summary

- cases: `2`
- slices: `4`
- wins vs left single: `4`
- wins vs right single: `2`
- wins vs best single: `2`
- wins vs worst single: `4`
- mean margin vs worst single: `2.1855`
- min margin vs worst single: `0.8726`
- mean regret vs best single: `0.0043`
- max regret vs best single: `0.3046`

## Cases

| case | slice | left single | right single | consensus | margin vs left | margin vs right | margin vs best | margin vs worst |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `qwen3_0p6b` | `left_eval` | 49.5352 | 45.3513 | 45.6559 | 3.8794 | -0.3046 | -0.3046 | 3.8794 |
| `qwen3_0p6b` | `right_eval` | 47.5872 | 44.8344 | 44.9290 | 2.6582 | -0.0946 | -0.0946 | 2.6582 |
| `qwen3_1p7b` | `left_eval` | 27.6578 | 26.6878 | 26.3260 | 1.3319 | 0.3618 | 0.3618 | 1.3319 |
| `qwen3_1p7b` | `right_eval` | 29.2030 | 28.3505 | 28.3303 | 0.8726 | 0.0201 | 0.0201 | 0.8726 |

## Interpretation

Consensus transfer is treated as boundary evidence: it can avoid the worse single-split policy while still having bounded regret versus the best single-split policy on some slices.

## Failures

- none
