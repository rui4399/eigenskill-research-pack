# Public Task Benchmark GSM8K200 MMLU100 Manifest

Date: `2026-06-07T17:12:19+00:00`
Artifacts: `2`

## Files

| id | dataset | config | split | task format | rows | path |
|---|---|---|---|---|---:|---|
| `gsm8k` | `openai/gsm8k` | `main` | `test` | `gsm8k` | 200 | `data_eval/public_task_benchmark_v1/gsm8k_test_gsm8k200_mmlu100.jsonl` |
| `mmlu_abstract_algebra` | `cais/mmlu` | `abstract_algebra` | `test` | `mmlu` | 100 | `data_eval/public_task_benchmark_v1/mmlu_abstract_algebra_test_gsm8k200_mmlu100.jsonl` |

## Claim Boundary

- 200-row public GSM8K plus full 100-row MMLU abstract-algebra fixtures for guarded local task retention; not leaderboard-scale evaluation.
- Use these files to verify public-schema task ingestion before running larger benchmark slices.
