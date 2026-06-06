# Chat Task Regression Gate

Status: **PASS**

## Summary

- candidate: `konly_layers17`
- tasks: 84
- task types: 8
- baseline passes: 46 (0.5476)
- fused passes: 45 (0.5357)
- pass delta: -1
- regressions / fixes: 1 / 0
- mean speed ratio fused/baseline: 0.9746x
- guard peak memory: 4458 / 8151 MiB (0.5469)

## By Task Type

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

## Regressions

| id | type | expected | baseline | fused |
|---|---|---|---|---|
| `stress_json_keys_001` | `json_keys` | `['risk', 'evidence']` | `<think> </think> ```json { "risk": "calibration_split_instability", "evidence": "calibration_split_instability" }` | `<think> </think> ```json { "risk": "calibration_split_inconsistency", "evidence": "calibration_split_inconsistency` |

## Failures

- none

## Claim Boundary

- Valid claim: this candidate passes a deterministic 84-task stress-retention gate under the configured regression budget.
- Invalid claim: this is a broad benchmark replacement for MMLU/GSM8K/IFEval or evidence of full quality preservation.
