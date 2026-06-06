# Failure-Aware Role Policy Gate

Date: `2026-06-06T06:42:33+00:00`

Use this as a failure-aware diagnostic gate. A per-task-type recommendation must be validated on a fresh split before it becomes a routing policy.

## Task-Type Policies

| task type | decision | recommended | speed | safe candidates | rejected candidates |
|---|---|---|---:|---|---|
| `all_of` | `type_safe_candidate` | `konly_layers17` | 0.9746x | `konly_layers17, vonly_layers17, qonly_layers17` | `n/a` |
| `contains_all` | `type_safe_candidate` | `konly_layers17` | 0.9746x | `konly_layers17, vonly_layers17, qonly_layers17` | `n/a` |
| `contains_none` | `type_safe_candidate` | `konly_layers17` | 0.9746x | `konly_layers17, vonly_layers17, qonly_layers17` | `n/a` |
| `json_keys` | `type_safe_candidate` | `qonly_layers17` | 0.9272x | `qonly_layers17` | `konly_layers17, vonly_layers17` |
| `mcq` | `type_safe_candidate` | `konly_layers17` | 0.9746x | `konly_layers17` | `qonly_layers17, vonly_layers17` |
| `number` | `type_safe_candidate` | `konly_layers17` | 0.9746x | `konly_layers17, vonly_layers17, qonly_layers17` | `n/a` |
| `sentence_count` | `type_safe_candidate` | `konly_layers17` | 0.9746x | `konly_layers17, vonly_layers17, qonly_layers17` | `n/a` |
| `word_count` | `type_safe_candidate` | `konly_layers17` | 0.9746x | `konly_layers17, vonly_layers17, qonly_layers17` | `n/a` |

## Candidate Rejections

| candidate | total regressions | regression types |
|---|---:|---|
| `qonly_layers17` | 1 | `mcq` |
| `vonly_layers17` | 3 | `json_keys, mcq` |
| `konly_layers17` | 1 | `json_keys` |

## Use

- Treat `no_safe_candidate` as a hard stop for that task type under the tested policies.
- Treat a `type_safe_candidate` as a next experiment, not as a deployment claim.
- Validate any task-type-conditioned policy on a fresh split before adding it to a paper claim.
