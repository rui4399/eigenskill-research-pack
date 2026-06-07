# Public Task Benchmark Subset100 Manifest

Date: `2026-06-07T09:15:49+00:00`
Artifacts: `2`

## Files

| id | dataset | config | split | task format | rows | path |
|---|---|---|---|---|---:|---|
| `gsm8k` | `openai/gsm8k` | `main` | `test` | `gsm8k` | 100 | `data_eval/public_task_benchmark_v1/gsm8k_test_subset100.jsonl` |
| `mmlu_abstract_algebra` | `cais/mmlu` | `abstract_algebra` | `test` | `mmlu` | 100 | `data_eval/public_task_benchmark_v1/mmlu_abstract_algebra_test_subset100.jsonl` |

## Claim Boundary

- Public MMLU/GSM8K 100-row subset fixtures for guarded subset evaluation; not leaderboard-scale evidence.
- Use these files to verify public-schema task ingestion before running larger benchmark slices.
