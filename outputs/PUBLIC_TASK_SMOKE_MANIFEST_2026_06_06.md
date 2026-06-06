# Public Task Smoke Manifest

Date: `2026-06-06T11:54:34+00:00`
Artifacts: `2`

## Files

| id | dataset | config | split | task format | rows | path |
|---|---|---|---|---|---:|---|
| `gsm8k` | `openai/gsm8k` | `main` | `test` | `gsm8k` | 4 | `data_eval/public_task_smoke_v1/gsm8k_test_smoke.jsonl` |
| `mmlu_abstract_algebra` | `cais/mmlu` | `abstract_algebra` | `test` | `mmlu` | 4 | `data_eval/public_task_smoke_v1/mmlu_abstract_algebra_test_smoke.jsonl` |

## Claim Boundary

- Tiny public benchmark smoke fixtures; not leaderboard-scale evaluation.
- Use these files to verify public-schema task ingestion before running larger benchmark slices.
