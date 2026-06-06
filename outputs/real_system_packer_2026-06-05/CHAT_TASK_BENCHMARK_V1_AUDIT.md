# Chat Task Benchmark V1 Audit

Date: `2026-06-06`

Purpose: add a deterministic, task-style benchmark runner that is closer to established evaluation formats than free-form prompt similarity. The benchmark is local and self-contained; it uses MMLU-style multiple choice, GSM8K-style numeric answers, IFEval-style JSON/constraint following, and deployment-specific instruction checks.

## Artifacts

- Runner: `train_python/eval_chat_task_benchmark.py`
- Tests: `train_python/test_eval_chat_task_benchmark.py`
- Task file: `data_eval/chat_task_benchmark_v1.jsonl`
- Zero-download import path: `--task-format native|mmlu|gsm8k|ifeval`
- Baseline report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_BASELINE.md`
- No-think baseline report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_BASELINE.md`
- No-think layers-1/7 fused report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS17.md`
- Rescored no-think layers-1/7 fused report after visible-think stripping: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS17_RESCORE.md`
- V-only no-think layers-1/7 report, 32-token budget: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS17_VONLY_32TOK.md`
- V-only no-think layers-1/7 report, 64-token budget: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS17_VONLY.md`
- V-only no-think layers-1/7/20 report, 32-token budget: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS1720_VONLY_32TOK.md`
- Projection-role selector:
  - script: `train_python/select_projection_role_policy.py`
  - test: `train_python/test_select_projection_role_policy.py`
  - cross-slice report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR.md`
  - IFEval-only role report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_IFEVAL_ONLY.md`

## Results

| run | model | tasks | baseline passes | fused passes | baseline tok/s | fused tok/s | fused/base tok/s | baseline TTFT s | fused TTFT s | guard peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline, chat-template | Qwen3-0.6B | 12 | 2 | N/A | 22.7031 | N/A | N/A | 0.171191 | N/A | 3601 MiB / 44.18% |
| baseline, chat-template, `/no_think` | Qwen3-0.6B | 12 | 3 | N/A | 23.9036 | N/A | N/A | 0.152990 | N/A | 3599 MiB / 44.15% |
| layers `1,7` fused, chat-template, `/no_think` | Qwen3-0.6B | 12 | 3 | 3 | 22.8676 | 19.4066 | 0.8486x | 0.174316 | 0.247880 | 3590 MiB / 44.04% |
| layers `1,7` fused, chat-template, `/no_think`, rescored/rerun | Qwen3-0.6B | 12 | 5 | 5 | 22.0725 | 20.2123 | 0.9157x | 0.187943 | 0.276915 | 3592 MiB / 44.07% |
| layers `1,7`, V-only packed with Q/K dense, chat-template, `/no_think`, 32-token budget | Qwen3-0.6B | 12 | 5 | 5 | 23.9942 | 24.3342 | 1.0142x | 0.155008 | 0.144196 | 3763 MiB / 46.17% |
| layers `1,7`, V-only packed with Q/K dense, chat-template, `/no_think`, 64-token budget | Qwen3-0.6B | 12 | 7 | 7 | 24.4976 | 23.7956 | 0.9713x | 0.159114 | 0.124476 | 3766 MiB / 46.20% |
| layers `1,7,20`, V-only packed with Q/K dense, chat-template, `/no_think`, 32-token budget | Qwen3-0.6B | 12 | 5 | 5 | 24.2795 | 16.7591 | 0.6903x | 0.156842 | 0.433537 | 3763 MiB / 46.17% |

## Interpretation

- `/no_think` is necessary for Qwen3-0.6B strict short-answer evaluation. Without it, generation often spends the 32-token budget inside `<think>` and fails to emit the requested answer.
- The task suite is intentionally strict. After the scorer strips visible `<think>...</think>` wrappers before deterministic matching, Qwen3-0.6B reaches `5/12` rather than the old `3/12`; this is still a weak smoke baseline, not a strong capability result.
- The conservative ESMP fused layers `1,7` run preserves this weak task accuracy under the updated scorer (`5/12 -> 5/12`) but is slower on this small batch-one benchmark (`0.9157x` tokens/s vs baseline in the rescored/rerun table).
- The V-only projection-role ablation is stronger than full-QKV replacement on this V1 slice. Under the same 32-token budget as the rescored run, V-only preserves `5/12 -> 5/12` and reaches `1.0142x` fused/base token rate in this short run. At 64 tokens it also preserves pass count (`7/12 -> 7/12`) but is slightly slower (`0.9713x`).
- Expanding V-only from layers `1,7` to `1,7,20` preserves V1 pass count (`5/12 -> 5/12`) but is much slower (`0.6903x`) and has a worse TTFT. This is not an attractive expansion under the current runtime.
- The projection-role selector makes the decision rule explicit. Across V1 32-token and IFEval v2, it selects `vonly_layers17` as `conservative_candidate` with score `0.9099`, min speed `1.0142x`, and no pass-count regressions. It rejects `full_qkv_layers17` and `vonly_layers1720` because both regress IFEval v2.
- Treat the 64-token row as a separate longer-generation rerun, not a replacement for the 32-token baseline. The useful signal is that V-only is a conservative candidate worth larger validation.
- This reinforces the current honest claim boundary: quality-preserving shallow ESMP replacement is possible on narrow task checks, but end-to-end task throughput is not yet improved.

## Official-Format Import Path

`eval_chat_task_benchmark.py` now accepts local JSONL slices without downloading datasets:

- `--task-format mmlu`: converts records with `question`, `choices`, and `answer` into multiple-choice tasks.
- `--task-format gsm8k`: converts records with `question` and `answer`; final numeric answers are extracted from the `####` marker when present.
- `--task-format ifeval`: supports deterministic subsets for `keywords:existence`, `keywords:forbidden_words`, `detectable_format:json_format`, `length_constraints:number_sentences`, and `length_constraints:number_words`. Multi-instruction rows are scored as `all_of`.

This is an import path, not a claim that full official benchmark coverage is complete. Full IFEval requires many instruction-specific checkers and should be added incrementally with tests.

## Next Method Step

Use the zero-download import path on cached official-format MMLU/GSM8K slices, and continue expanding IFEval coverage beyond the current deterministic subset. The new local IFEval-style v2 audit is documented in `outputs/real_system_packer_2026-06-05/IFEVAL_V2_DETERMINISTIC_AUDIT.md`.
