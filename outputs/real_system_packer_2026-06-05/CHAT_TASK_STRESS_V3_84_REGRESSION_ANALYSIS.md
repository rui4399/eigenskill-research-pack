# Chat Task Regression Analysis

Date: `2026-06-06T06:29:34+00:00`

This report compares baseline and fused rows from `eval_chat_task_benchmark.py` outputs. Regressions are rows where baseline passed and fused failed; fixes are the reverse.

## Candidate Summary

| candidate | passes | pass delta | speed | regressions | fixes |
|---|---:|---:|---:|---:|---:|
| `qonly_layers17` | 46 -> 45 / 84 | -1 | 0.9272x | 1 | 0 |
| `vonly_layers17` | 46 -> 43 / 84 | -3 | 0.9653x | 3 | 0 |
| `konly_layers17` | 46 -> 45 / 84 | -1 | 0.9746x | 1 | 0 |

## `qonly_layers17` Type Summary

| type | tasks | baseline pass | fused pass | regressions | fixes | both pass | both fail |
|---|---:|---:|---:|---:|---:|---:|---:|
| `all_of` | 12 | 9 | 9 | 0 | 0 | 9 | 3 |
| `contains_all` | 12 | 0 | 0 | 0 | 0 | 0 | 12 |
| `contains_none` | 12 | 12 | 12 | 0 | 0 | 12 | 0 |
| `json_keys` | 12 | 7 | 7 | 0 | 0 | 7 | 5 |
| `mcq` | 12 | 10 | 9 | 1 | 0 | 9 | 2 |
| `number` | 12 | 3 | 3 | 0 | 0 | 3 | 9 |
| `sentence_count` | 6 | 4 | 4 | 0 | 0 | 4 | 2 |
| `word_count` | 6 | 1 | 1 | 0 | 0 | 1 | 5 |

### `qonly_layers17` Regressions

| id | type | expected | baseline | fused |
|---|---|---|---|---|
| `stress_mcq_extra_000` | `mcq` | `A` | `<think> </think> A. ESMP binaries` | `<think> </think> B. README text` |

### `qonly_layers17` Fixes

| id | type | expected | baseline | fused |
|---|---|---|---|---|
| n/a | n/a | n/a | n/a | n/a |

## `vonly_layers17` Type Summary

| type | tasks | baseline pass | fused pass | regressions | fixes | both pass | both fail |
|---|---:|---:|---:|---:|---:|---:|---:|
| `all_of` | 12 | 9 | 9 | 0 | 0 | 9 | 3 |
| `contains_all` | 12 | 0 | 0 | 0 | 0 | 0 | 12 |
| `contains_none` | 12 | 12 | 12 | 0 | 0 | 12 | 0 |
| `json_keys` | 12 | 7 | 5 | 2 | 0 | 5 | 5 |
| `mcq` | 12 | 10 | 9 | 1 | 0 | 9 | 2 |
| `number` | 12 | 3 | 3 | 0 | 0 | 3 | 9 |
| `sentence_count` | 6 | 4 | 4 | 0 | 0 | 4 | 2 |
| `word_count` | 6 | 1 | 1 | 0 | 0 | 1 | 5 |

### `vonly_layers17` Regressions

| id | type | expected | baseline | fused |
|---|---|---|---|---|
| `stress_json_keys_001` | `json_keys` | `['risk', 'evidence']` | `<think> </think> ```json { "risk": "calibration_split_instability", "evidence": "calibration_split_instability" }` | `<think> </think> ```json { "risk": "calibration_split_inconsistency", "evidence": "calibration_split_inconsistency` |
| `stress_json_keys_extra_004` | `json_keys` | `['benchmark', 'caveat']` | `<think> </think> ```json {"benchmark": "minified", "caveat": "only"} ```` | `<think> </think> ```json {"benchmark": "caveat"} ```` |
| `stress_mcq_extra_003` | `mcq` | `A` | `<think> </think> A. Q only` | `<think> </think> D. Full QKV` |

### `vonly_layers17` Fixes

| id | type | expected | baseline | fused |
|---|---|---|---|---|
| n/a | n/a | n/a | n/a | n/a |

## `konly_layers17` Type Summary

| type | tasks | baseline pass | fused pass | regressions | fixes | both pass | both fail |
|---|---:|---:|---:|---:|---:|---:|---:|
| `all_of` | 12 | 9 | 9 | 0 | 0 | 9 | 3 |
| `contains_all` | 12 | 0 | 0 | 0 | 0 | 0 | 12 |
| `contains_none` | 12 | 12 | 12 | 0 | 0 | 12 | 0 |
| `json_keys` | 12 | 7 | 6 | 1 | 0 | 6 | 5 |
| `mcq` | 12 | 10 | 10 | 0 | 0 | 10 | 2 |
| `number` | 12 | 3 | 3 | 0 | 0 | 3 | 9 |
| `sentence_count` | 6 | 4 | 4 | 0 | 0 | 4 | 2 |
| `word_count` | 6 | 1 | 1 | 0 | 0 | 1 | 5 |

### `konly_layers17` Regressions

| id | type | expected | baseline | fused |
|---|---|---|---|---|
| `stress_json_keys_001` | `json_keys` | `['risk', 'evidence']` | `<think> </think> ```json { "risk": "calibration_split_instability", "evidence": "calibration_split_instability" }` | `<think> </think> ```json { "risk": "calibration_split_inconsistency", "evidence": "calibration_split_inconsistency` |

### `konly_layers17` Fixes

| id | type | expected | baseline | fused |
|---|---|---|---|---|
| n/a | n/a | n/a | n/a | n/a |
