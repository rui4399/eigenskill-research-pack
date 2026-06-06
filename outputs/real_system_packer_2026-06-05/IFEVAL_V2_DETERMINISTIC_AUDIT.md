# IFEval-Style Deterministic V2 Audit

Date: `2026-06-06`

Purpose: expand the task benchmark beyond keyword existence by adding an official-format-shaped local IFEval slice with deterministic JSON, forbidden-word, sentence-count, word-count, and multi-constraint scoring. This is a zero-download local slice, not a claim of full official IFEval coverage.

## Artifacts

- Task file: `data_eval/ifeval_deterministic_v2.jsonl`
- Runner: `train_python/eval_chat_task_benchmark.py`
- Tests: `train_python/test_eval_chat_task_benchmark.py`
- Output JSON: `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers17.json`
- Output markdown: `outputs/real_system_packer_2026-06-05/IFEVAL_V2_QWEN3_0P6B_NO_THINK_LAYERS17.md`
- Guard JSON: `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers17_gpu_guard.json`
- Projection-role ablation JSON:
  - `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers17_vonly.json`
  - `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers17_qonly.json`
  - `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers17_konly.json`
  - `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers1720_vonly.json`
- Projection-role ablation reports:
  - `outputs/real_system_packer_2026-06-05/IFEVAL_V2_QWEN3_0P6B_NO_THINK_LAYERS17_VONLY.md`
  - `outputs/real_system_packer_2026-06-05/IFEVAL_V2_QWEN3_0P6B_NO_THINK_LAYERS17_QONLY.md`
  - `outputs/real_system_packer_2026-06-05/IFEVAL_V2_QWEN3_0P6B_NO_THINK_LAYERS17_KONLY.md`
  - `outputs/real_system_packer_2026-06-05/IFEVAL_V2_QWEN3_0P6B_NO_THINK_LAYERS1720_VONLY.md`
- Projection-role selector report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_IFEVAL_ONLY.md`

## Scoring Updates

- Added `keywords:forbidden_words` import as `contains_none`.
- Added `detectable_format:json_format` import as strict `json_valid`.
- Added `length_constraints:number_sentences` as `sentence_count`.
- Added `length_constraints:number_words` as `word_count`.
- Added multi-instruction IFEval rows as `all_of`.
- Stripped visible `<think>...</think>` blocks before deterministic scoring, so Qwen empty thinking wrappers do not mask the actual answer.

## Results

| run | model | tasks | baseline passes | fused passes | baseline tok/s | fused tok/s | fused/base tok/s | baseline TTFT s | fused TTFT s | guard peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| layers `1,7` fused, chat-template, `/no_think` | Qwen3-0.6B | 8 | 2 | 1 | 20.9845 | 21.6848 | 1.0334x | 0.269126 | 0.294206 | 3595 MiB / 44.11% |
| layers `1,7`, V-only packed, Q/K dense | Qwen3-0.6B | 8 | 2 | 2 | 24.2374 | 26.3511 | 1.0872x | 0.227321 | 0.150757 | 3761 MiB / 46.14% |
| layers `1,7`, Q-only packed, K/V dense | Qwen3-0.6B | 8 | 2 | 2 | 24.7679 | 24.7172 | 0.9980x | 0.229129 | 0.169360 | 3753 MiB / 46.04% |
| layers `1,7`, K-only packed, Q/V dense | Qwen3-0.6B | 8 | 2 | 2 | 21.8401 | 20.4550 | 0.9366x | 0.218562 | 0.171394 | 3755 MiB / 46.07% |
| layers `1,7,20`, V-only packed, Q/K dense | Qwen3-0.6B | 8 | 2 | 1 | 25.9604 | 22.1076 | 0.8516x | 0.193870 | 0.340813 | 3758 MiB / 46.10% |

## Interpretation

- The stricter IFEval-style slice exposes weaknesses that the previous native v1 suite did not isolate: fenced JSON fails strict JSON, several answers omit required deployment terms, and exact sentence/word constraints remain fragile.
- The conservative fused layers `1,7` candidate regresses on this stricter slice (`2/8 -> 1/8`) even though its mean token rate is slightly higher in this short run. This should be treated as negative quality evidence, not a deployment win.
- Projection-role ablation narrows the failure mode. Single-role packed replacement on layers `1,7` did not regress this 8-row deterministic slice (`2/8 -> 2/8` for Q-only, K-only, and V-only), while full QKV replacement did regress. The strongest short-run candidate is V-only because it preserved the pass count and had the best fused/base token-rate ratio in this run.
- Expanding V-only to layer `20` regresses the stricter IFEval-style slice (`2/8 -> 1/8`) and slows the run (`0.8516x`). This makes layers `1,7` the current conservative V-only boundary; layer `20` still needs separate row/role protection rather than coarse inclusion.
- The IFEval-only selector ranks `vonly_layers17` first (`conservative_candidate`, score `0.9174`), then `qonly_layers17` (`quality_preserving_speed_neutral`, score `0.8996`), then `konly_layers17` (`diagnostic_runtime_regression`, score `0.6655`). It rejects full-QKV and V-only layer-20 expansion because both lose one pass on this stricter slice.
- These role ablations are still small-slice diagnostics. They support the next method step, not a deployment claim: keep Q/K protected or separately higher precision, then evaluate V-only or role-selective ESMP replacement on larger structured instruction suites.
- This improves the paper story by making the benchmark less forgiving and more falsifiable. It also strengthens the current honest boundary: ESMP fused replacement must be validated against structured instruction constraints before any broad quality-preservation claim.

## Verification

- `python -m unittest test_eval_chat_task_benchmark` passed on Windows.
- `python -m unittest test_eval_chat_task_benchmark test_score_prompt_suite test_run_with_gpu_guard_disk test_generation_prompt_format test_qkv_proxy_drift` passed on Windows with the torch-only proxy tests skipped when torch is unavailable.
- WSL CUDA tests passed: `python3 -m unittest test_qkv_proxy_drift test_eval_chat_task_benchmark`.
- Guarded benchmark stayed under the 90% VRAM cap: `3595/8151 MiB = 44.11%`.
- Repo-local cleanup removed only `train_python/__pycache__`, about `0.321 MiB`.
- Projection-role ablation guard peaks also stayed under the 90% VRAM cap:
  - V-only: `3761/8151 MiB = 46.14%`; repo-local cleanup removed about `0.107 MiB`.
  - Q-only: `3753/8151 MiB = 46.04%`; repo-local cleanup removed about `0.107 MiB`.
  - K-only: `3755/8151 MiB = 46.07%`; repo-local cleanup removed about `0.107 MiB`.
  - V-only layers `1,7,20`: `3758/8151 MiB = 46.10%`; repo-local cleanup removed about `0.107 MiB`.
- Selector tests passed on Windows: `python -m unittest test_select_projection_role_policy test_eval_chat_task_benchmark` ran `12` tests OK.
