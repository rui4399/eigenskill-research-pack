# Chat Task Stress V2 Audit

Date: `2026-06-06`

This is a zero-download deterministic role-policy stress slice, not an official benchmark. It is intended to make projection-role replacement failures easier to falsify before spending time on larger official suites.

## Artifacts

- Generator: `train_python/generate_deterministic_task_stress.py`
- Tests: `train_python/test_generate_deterministic_task_stress.py`
- Task file: `data_eval/chat_task_stress_v2.jsonl`
- Task count: `42`
- Task types: `mcq=6`, `number=6`, `json_keys=6`, `contains_all=6`, `contains_none=6`, `sentence_count=3`, `word_count=3`, `all_of=6`
- Selector report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_IFEVAL_STRESS.md`

## Verification

- `python -m unittest test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy`
  - passed: `Ran 15 tests ... OK`
- `python -m py_compile generate_deterministic_task_stress.py test_generate_deterministic_task_stress.py eval_chat_task_benchmark.py select_projection_role_policy.py`
  - passed
- Loader check:
  - `stress_tasks=42`
  - `types={'mcq': 6, 'number': 6, 'json_keys': 6, 'contains_all': 6, 'contains_none': 6, 'sentence_count': 3, 'word_count': 3, 'all_of': 6}`

## Guarded Qwen3-0.6B Results

All runs used:

- Model: `Qwen/Qwen3-0.6B`
- Task format: `native`
- Prompting: chat template + `/no_think`
- Max new tokens: `32`
- Package summary: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp/pack_summary.json`
- Guard: `--max-memory-ratio 0.90 --min-disk-free-gb 15 --cleanup-repo-caches --cleanup-root .`

| policy | output | baseline passes | fused passes | fused/base tok/s | baseline TTFT s | fused TTFT s | guard peak |
|---|---|---:|---:|---:|---:|---:|---:|
| V-only layers `1,7` | `chat_task_stress_v2_qwen3_0p6b_no_think_layers17_vonly_32tok.json` | 22/42 | 21/42 | 0.9924x | 0.111859 | 0.154996 | 3759/8151 MiB = 46.12% |
| Q-only layers `1,7` | `chat_task_stress_v2_qwen3_0p6b_no_think_layers17_qonly_32tok.json` | 22/42 | 22/42 | 1.0080x | 0.104977 | 0.102466 | 3774/8151 MiB = 46.30% |
| K-only layers `1,7` | `chat_task_stress_v2_qwen3_0p6b_no_think_layers17_konly_32tok.json` | 22/42 | 21/42 | 1.0028x | 0.120815 | 0.108046 | 4266/8151 MiB = 52.34% |

## Selector Update

The IFEval-v2 + Stress-v2 selector changes the active role-policy conclusion:

- `qonly_layers17`: `quality_preserving_speed_neutral`, score `0.9006`, no pass-count regression on either split, min speed `0.9980x`, max TTFT ratio `0.9761`
- `vonly_layers17`: rejected due to stress-v2 pass-count regression (`22/42 -> 21/42`)
- `konly_layers17`: rejected due to stress-v2 pass-count regression (`22/42 -> 21/42`)

This supersedes the earlier V-only-first interpretation from the smaller V1/IFEval slices. The current best narrow policy is Q-only on layers `1,7`, but it is still a diagnostic candidate rather than a deployment claim.

## Failed / Stopped Run

Full-QKV layers `1,7` on stress v2 exceeded the 20-minute command timeout and was manually stopped. No result file should be treated as valid for this run.

After stopping, no WSL `eval_chat_task_benchmark.py` or `run_with_gpu_guard.py` process remained. GPU utilization stayed high because Windows still had a `NeedForSpeedHeat` graphics process active; no user process was killed.

## Interpretation

- The larger deterministic slice is useful because it falsified the previous V-only preference.
- Q-only is the next policy to validate on V1 and more official-format task slices when GPU is idle.
- Stress v2 exposes that Qwen3-0.6B baseline itself is weak on numeric and strict structured rows, so pass-count preservation is more important than absolute accuracy for this local diagnostic.
- Do not claim broad quality preservation or end-to-end acceleration from this result.
