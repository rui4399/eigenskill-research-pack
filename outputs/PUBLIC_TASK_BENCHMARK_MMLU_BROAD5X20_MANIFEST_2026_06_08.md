# Public Task Benchmark Manifest: MMLU Broad5x20

Date: `2026-06-07T21:55:52+00:00`
Artifacts: `6`

## Files

| id | dataset | config | split | task format | rows | path |
|---|---|---|---|---|---:|---|
| `mmlu_abstract_algebra` | `cais/mmlu` | `abstract_algebra` | `test` | `mmlu` | 20 | `data_eval/public_task_benchmark_v1/mmlu_abstract_algebra_test_mmlu_broad5x20.jsonl` |
| `mmlu_anatomy` | `cais/mmlu` | `anatomy` | `test` | `mmlu` | 20 | `data_eval/public_task_benchmark_v1/mmlu_anatomy_test_mmlu_broad5x20.jsonl` |
| `mmlu_business_ethics` | `cais/mmlu` | `business_ethics` | `test` | `mmlu` | 20 | `data_eval/public_task_benchmark_v1/mmlu_business_ethics_test_mmlu_broad5x20.jsonl` |
| `mmlu_computer_security` | `cais/mmlu` | `computer_security` | `test` | `mmlu` | 20 | `data_eval/public_task_benchmark_v1/mmlu_computer_security_test_mmlu_broad5x20.jsonl` |
| `mmlu_high_school_us_history` | `cais/mmlu` | `high_school_us_history` | `test` | `mmlu` | 20 | `data_eval/public_task_benchmark_v1/mmlu_high_school_us_history_test_mmlu_broad5x20.jsonl` |
| `mmlu_combined` | `cais/mmlu` | `abstract_algebra,anatomy,business_ethics,computer_security,high_school_us_history` | `test` | `mmlu` | 100 | `data_eval/public_task_benchmark_v1/mmlu_broad5x20_test.jsonl` |

## Claim Boundary

- Five-subject 100-row MMLU fixture for guarded local task-retention evidence; not full MMLU leaderboard evaluation.
- Use these files to verify public-schema task ingestion before running larger benchmark slices.
