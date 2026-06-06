# Codex Resume Pointer

Current stop point: 2026-06-06, after CodeGraph/plugin repair, deterministic chat task stress v2 generation, guarded V/Q/K projection-role stress runs, V1 Q/K projection-role ablations, stress-v3 84-row expansion, stress-v3 regression diagnosis, failure-aware role-policy gate, three-split and four-split projection-role selector updates, guarded ESMP Linear/runtime/generation benchmarks, non-layer0 QKV8 layer-subset expansion, layer-20 row-sensitive V-projection probes, prompt-conditioned row-group sweeps through 7-group focus, prompt failure analysis, held-out 12-prompt rowguard validation, full 6-group held-out sweep, prompt-split transfer audit V2, split-consensus rowguard selector, third prompt split validation, multi-split selector, QKV/hidden/logit proxy drift measurement, proxy-augmented selector, 24-prompt v3 task-style audit, v3 rule-scored task wrapper, opt-in chat-template prompt-suite audit, v4 expected-rule scoring, chat task benchmark v1, and disk-aware GPU guard cleanup support. No GitHub commit or push has been made.

When Rui says "继续", first read:

- `outputs/real_system_packer_2026-06-05/RESUME_HANDOFF.md`

Tooling checkpoint from 2026-06-06:

- CodeGraph CLI is healthy and indexed. Use `codegraph status`, `codegraph sync`, and `codegraph query ...` first in this still-running session.
- CodeGraph MCP is registered in `C:\Users\18042\.codex\config.toml` and now uses the absolute command `C:\Users\18042\AppData\Roaming\npm\codegraph.cmd` with args `serve --mcp --no-watch`. This avoids watcher failures on WSL-style venv symlinks such as `.venv-baselines\lib64`; this already-running Codex Desktop turn may still need a fresh session before direct `mcp__codegraph.*` tools hot-load.
- Latest CodeGraph status after failure-aware selector sync: `119 files / 2,575 nodes / 4,742 edges`, index up to date.
- Hermes config also uses `C:/Users/18042/AppData/Roaming/npm/codegraph.cmd` with args `serve --mcp --no-watch` for CodeGraph.
- `understanding-anything` is installed and enabled as `understanding-anything@personal`; `codex plugin list` reports `installed, enabled`.
- `understanding-anything` is also mirrored into WSL/Hermes at `/home/rui/.hermes/skills/imported/understanding-anything`.
- C drive checkpoint after targeted cleanup and the latest stress-v3 runs: about `20.07 GB` decimal free after the latest CodeGraph sync. Low-risk cleanup removed about `1.316 GB` in the first pass and about `918 MB` in the second pass, covering temp crash dumps, refreshed `uv` cache, NVIDIA/D3D shader caches, `CrashDumps`, Explorer thumbnails, and repo-local `__pycache__`. Safe repo caches are no longer the dominant C-drive pressure. The 2026-06-06 storage scan found major C-drive pressure in `C:\Users\18042\AppData\Local\wsl` about `62.8 GB`, Steam about `51.2 GB`, `.codex`, `.ollama`, and `.lmstudio`. Do not delete HuggingFace/Ollama/LM Studio/model caches unless Rui explicitly chooses that tradeoff.

Evidence checkpoint:

- Read `outputs/real_system_packer_2026-06-05/REAL_SYSTEM_RESULTS_2026_06_06.md` before writing the paper/report. It contains the current allowed claims and caveats.
- C-drive audit: `outputs/real_system_packer_2026-06-05/C_DRIVE_STORAGE_AUDIT_2026_06_06.md`
- `run_with_gpu_guard.py` now supports `--timeout-sec` and `--max-start-memory-ratio`; timeout records `killed_by_timeout` / `timeout_seconds` and exits `91`. Use `--max-start-memory-ratio 0.45` for long or memory-sensitive GPU commands so experiments do not launch while Windows graphics/game/LM Studio/Ollama processes already hold several GiB of VRAM.
- New stress-v2 evidence:
  - generator/test: `train_python/generate_deterministic_task_stress.py`, `train_python/test_generate_deterministic_task_stress.py`
  - tasks: `data_eval/chat_task_stress_v2.jsonl`, 42 deterministic local rows across 8 native scorer types
  - audit: `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V2_AUDIT.md`
  - IFEval+Stress selector: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_IFEVAL_STRESS.md`
  - result: Q-only layers `1,7` is now the best narrow candidate across IFEval v2 + stress v2 (`22/42 -> 22/42` on stress, `1.0080x` stress tok/s, selector score `0.9006`). V-only and K-only layers `1,7` are rejected on stress v2 because both lose one pass (`22/42 -> 21/42`). This supersedes the smaller-slice V-only-first interpretation.
  - V1 Q-only/K-only 32-token ablations now exist. Q-only preserves V1 pass count (`5/12 -> 5/12`) and runs at `1.1926x` fused/base tok/s; K-only preserves V1 pass count (`5/12 -> 5/12`) but runs at `0.9410x`.
  - three-split selector: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_V1_IFEVAL_STRESS.md`
  - three-split result: Q-only layers `1,7` remains the best candidate across V1 32-token, IFEval v2, and stress v2 (`quality_preserving_speed_neutral`, score `0.9118`, min speed `0.9980x`, max TTFT ratio `0.9761`). V-only and K-only remain rejected due to stress-v2 pass-count regression.
  - stress-v3 84-row expansion now exists: `data_eval/chat_task_stress_v3_84.jsonl`.
  - stress-v3 84-row results on layers `1,7`: Q-only `46/84 -> 45/84`, `0.9272x`; V-only `46/84 -> 43/84`, `0.9653x`; K-only `46/84 -> 45/84`, `0.9746x`.
  - four-split selector: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_V1_IFEVAL_STRESS_V3.md`
  - four-split result: no single-role policy is quality-preserving. `qonly_layers17` is rejected because stress-v3 loses one pass. Do not present Q-only as deployable; present it as a falsified three-split candidate and use this as motivation for larger-slice role/row protection.
  - stress-v3 regression analysis: `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_REGRESSION_ANALYSIS.md` and `outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_regression_analysis.json`.
  - failure localization: Q-only has one MCQ regression and no fixes; V-only has two JSON-key regressions plus one MCQ regression and no fixes; K-only has one JSON-key regression and no fixes. Next policy should protect structured-output/answer-choice sensitive rows or roles rather than pick a single global Q/K/V role.
  - failure-aware policy gate: `outputs/real_system_packer_2026-06-05/FAILURE_AWARE_ROLE_POLICY_STRESS_V3_84.md` and `outputs/real_system_packer_2026-06-05/failure_aware_role_policy_stress_v3_84.json`.
  - diagnostic policy target: on stress-v3, `json_keys` recommends Q-only, `mcq` recommends K-only, and the no-regression types recommend K-only by speed. This must be validated on a fresh split before being described as routing.
  - full-QKV stress-v2 attempt exceeded the 20-minute command timeout and was stopped; no full-QKV stress result is valid yet.
  - GPU stayed high afterward because Windows still had `NeedForSpeedHeat` active; no user process was killed.
  - Latest continuation check still showed `NeedForSpeedHeat` active and GPU at about `96% / 5008 MiB / 86C`; do not start more GPU benchmarks until it drops below the chosen start gate, e.g. `--max-start-memory-ratio 0.45`.
- Full Qwen3-0.6B ESMP package exists: 197 Linear modules, 347,133,248 bytes, 6.8675x compression vs FP32.
- Baseline HF FP16 generation exists:
  - Qwen3-0.6B: TTFT 1.0404 s, 17.5632 tokens/s, script peak 2028 MiB, guard peak 4993 MiB.
  - Qwen3-1.7B: TTFT 1.3376 s, 13.7890 tokens/s, script peak 5063 MiB, guard peak 7216 MiB / 88.53%.
- Current active GPU rule from Rui's goal is at most 90% VRAM. Use `run_with_gpu_guard.py --max-memory-ratio 0.90` for GPU experiments unless Rui tightens the cap again. The prior Qwen3-1.7B 88.53% run is still close to the ceiling; prefer smaller shapes when possible.
- `run_with_gpu_guard.py` now records disk state and supports `--min-disk-free-gb`, `--disk-check-path`, `--cleanup-repo-caches`, `--cleanup-root`, and `--cleanup-dry-run`. The cleanup path is intentionally narrow: repo-local `__pycache__`, `.pytest_cache`, `.ruff_cache`, `*.pyc`, and `*.pyo`, with large evidence/output directories skipped.
- Triton tuning exists: 72 configs, 6 beat torch FP16, 44 beat row-wise dynamic path, max grouped/FP16 speedup 2.0927x.
- Updated Triton cross-shape tuning exists: 216 configs across `2048x1024`, `3072x1024`, `1024x3072`; 26 beat torch FP16, 134 beat row-wise dynamic path, max grouped/FP16 speedup 2.1048x, max grouped/row-wise speedup 5.7507x, max guard VRAM ratio 0.3019.
- Updated C++ ESMP runtime stratified sweep exists: 42 real Qwen3-0.6B modules; median selected-row/full speedup 16.8259x, max 56.4888x, median selected 64-row latency 0.2056 ms.
- ESMP activation reconstruction now exists:
  - script: `train_python/eval_esmp_module_reconstruction.py`
  - smoke: 3/3 modules OK, median output rel-L2 0.0762, guard peak 43.50%.
  - stratified: 42/42 modules OK, median output rel-L2 0.1260, p90 0.2028, guard peak 43.52%.
  - all Linear excluding `lm_head`: 196/196 modules OK, median output rel-L2 0.1363, p90 0.2114, median compression 7.6414x, guard peak 43.59%.
- Minimal ESMP-swapped generation smoke now exists:
  - script: `train_python/measure_esmp_generation_latency.py`
  - swapped modules: layer-0 `q_proj`, `k_proj`, `v_proj`
  - selected package compression vs FP32: 6.1682x
  - same-loader HF baseline, 16 tokens: TTFT 0.9489 s, 9.5277 tokens/s, guard peak 43.47%.
  - cached dequant, 16 tokens: TTFT 0.9542 s, 9.2958 tokens/s, guard peak 43.63%.
  - on-demand dequant, 16 tokens: TTFT 1.1813 s, 5.3516 tokens/s, guard peak 43.49%.
  - Triton grouped, 16 tokens: TTFT 1.9611 s, 4.9957 tokens/s cold; with one warmup, TTFT 0.0458 s and 21.3777 tokens/s.
  - one-warmup comparison: same-loader baseline 25.0523 tokens/s, cached 28.8295 tokens/s, Python on-demand 9.1157 tokens/s, Triton grouped 21.3777 tokens/s.
  - generated text matched across the primary sequential runs.
- ESMP Linear runtime-shape benchmark now exists:
  - script: `train_python/benchmark_esmp_linear_runtimes.py`
  - output: `outputs/real_system_packer_2026-06-05/ESMP_LINEAR_RUNTIME_SHAPES.md`
  - model/modules: `Qwen/Qwen3-0.6B`, layer-0 `q_proj`, `k_proj`, `v_proj`
  - batches: `1, 12, 64`, warmup/iters `10/80`
  - median dense latency: `0.014725 ms`
  - median cached latency: `0.016797 ms`, median speedup vs dense `0.8801x`
  - median Python on-demand latency: `18.072527 ms`, median speedup vs dense `0.0009x`
  - median Triton grouped latency: `0.051871 ms`, median speedup vs dense `0.2667x`
  - guard peak: `3555/8151 MiB = 43.61%`
  - interpretation: standalone Triton grouped works but is slower than dense on these small shapes; next work should be decode-specific/fused/selected-row rather than another generic retune.
- ESMP selected-row GPU benchmark now exists:
  - script: `train_python/benchmark_esmp_selected_rows.py`
  - new kernels: `_int4_selected_matmul_kernel` and `_int8_selected_matmul_kernel` in `train_python/triton_mixed_gemm.py`
  - output: `outputs/real_system_packer_2026-06-05/ESMP_SELECTED_ROWS.md`
  - model/modules: `Qwen/Qwen3-0.6B`, layer-0 `q_proj`, `k_proj`, `v_proj`
  - batches: `1, 12, 64`, selected rows `16, 64, 256`, warmup/iters `10/80`
  - median Triton selected latency: `0.048981 ms`
  - median Triton selected speedup vs dense full: `0.4235x`
  - median Triton selected speedup vs dense selected: `0.4466x`
  - Triton selected faster than dense full: `4/27` cases
  - Triton selected faster than dense selected: `4/27` cases
  - best Triton selected speedup vs dense full: `2.2406x`
  - best Triton selected speedup vs dense selected: `1.9858x`
  - guard peak: `3561/8151 MiB = 43.69%`
  - interpretation: selected-row packed GPU path works and has useful best cases, but median is still launch/tiling limited.
- ESMP fused QKV selected-row GPU benchmark now exists:
  - script: `train_python/benchmark_esmp_fused_selected_rows.py`
  - primary output: `outputs/real_system_packer_2026-06-05/ESMP_FUSED_SELECTED_ROWS.md`
  - tuned output: `outputs/real_system_packer_2026-06-05/ESMP_FUSED_SELECTED_ROWS_TUNED_32x16x64.md`
  - block sweep output: `outputs/real_system_packer_2026-06-05/fused_block_sweep/ESMP_FUSED_SELECTED_ROW_BLOCK_SWEEP.md`
  - model/modules: `Qwen/Qwen3-0.6B`, QKV projections on layers `0, 1, 7, 13, 20, 27`
  - batches: `1, 12, 64`, selected rows per module `16, 64, 256`, warmup/iters `10/80`
  - primary `32x16x128`: median fused latency `0.104230 ms`; median speedup vs per-module Triton selected `2.0873x`; wins `52/54`
  - tuned `32x16x64`: median fused latency `0.081686 ms`; median speedup vs per-module Triton selected `2.3583x`; wins `51/54`
  - tuned fused faster than dense full concat: `4/54` cases; tuned fused faster than dense selected concat: `2/54` cases
  - median rel-L2 vs dense selected concat: `0.142890`; max rel-L2 vs per-module Triton selected: `0.0`
  - guard peak: `3601/8151 MiB = 44.18%`
  - interpretation: QKV fusion materially reduces launch overhead for packed selected rows, but dense concat remains the stronger median baseline.
- ESMP fused selected-row sidecar generation smoke now exists:
  - script: `train_python/measure_esmp_fused_sidecar_generation.py`
  - output: `outputs/real_system_packer_2026-06-05/ESMP_FUSED_SIDECAR_GENERATION.md`
  - model: `Qwen/Qwen3-0.6B`, same HF FP16 loader, 16 generated tokens, one warmup run
  - sidecar executes fused selected-row QKV kernels on real decode hidden-state tensors and discards the result; it does not replace dense QKV.
  - same-loader baseline: TTFT `0.028981 s`, elapsed `0.543037 s`, `29.4639` tokens/s, guard peak `3582/8151 MiB = 43.95%`
  - 1-layer sidecar (`layer 0`): 16 calls, sidecar CUDA sum `4.6900 ms`, median `0.2606 ms/call`, TTFT `0.041236 s`, elapsed `0.603245 s`, `26.5232` tokens/s, guard peak `43.93%`
  - 3-layer sidecar (`layers 0,1,7`): 48 calls, sidecar CUDA sum `11.2085 ms`, median `0.2218 ms/call`, TTFT `0.067467 s`, elapsed `0.801341 s`, `19.9665` tokens/s, guard peak `44.02%`
  - deferred-sync 1-layer sidecar: 16 calls, sidecar CUDA sum `4.7119 ms`, median `0.2653 ms/call`, TTFT `0.038116 s`, elapsed `0.638191 s`, `25.0709` tokens/s, guard peak `43.95%`
  - deferred-sync 3-layer sidecar: 48 calls, sidecar CUDA sum `10.2186 ms`, median `0.2062 ms/call`, TTFT `0.043812 s`, elapsed `0.672049 s`, `23.8078` tokens/s, guard peak `43.96%`
  - generated text matched the baseline in all measured sidecar runs.
  - interpretation: real decode-loop integration works; per-call synchronization is pessimistic; this was followed by the true fused QKV replacement smoke below.
- ESMP fused QKV replacement generation smoke now exists:
  - script: `train_python/measure_esmp_fused_qkv_generation.py`
  - output: `outputs/real_system_packer_2026-06-05/ESMP_FUSED_QKV_REPLACEMENT_GENERATION.md`
  - this replaces selected `q_proj/k_proj/v_proj` modules with shared fused packed QKV wrappers, rather than running an additive sidecar.
  - Q wrapper computes concatenated packed Q/K/V once; K/V wrappers return cached slices.
  - same-script 16-token baseline: TTFT `0.028808 s`, elapsed `0.774345 s`, `20.6626` tokens/s, guard peak `43.95%`
  - 1-layer 16-token replacement: TTFT `0.033764 s`, elapsed `0.488582 s`, `32.7479` tokens/s, exact generated-text match, guard peak `43.99%`
  - 3-layer 16-token replacement: TTFT `0.031471 s`, elapsed `0.619774 s`, `25.8158` tokens/s, text changed but stayed on topic, guard peak `44.07%`
  - same-script 64-token baseline: TTFT `0.048212 s`, elapsed `2.391258 s`, `26.7642` tokens/s, guard peak `44.06%`
  - 1-layer 64-token replacement: TTFT `0.032971 s`, elapsed `2.116118 s`, `30.2441` tokens/s, prefix match then divergence, compression `6.1682x`, wrapper/fused calls `192/64`, cache hits/misses `128/64`, guard peak `44.01%`
  - 3-layer 64-token replacement: TTFT `0.032545 s`, elapsed `2.412621 s`, `26.5272` tokens/s, text changed but stayed on topic, compression `7.0778x`, wrapper/fused calls `576/192`, cache hits/misses `384/192`, guard peak `44.08%`
  - interpretation: true replacement path works and shallow replacement has speed evidence, but quality preservation is now the bottleneck.
- ESMP fused QKV prompt-suite audit now exists:
  - script: `train_python/eval_fused_qkv_prompt_suite.py`
  - outputs: `outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_1LAYER.md` and `outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_3LAYER.md`
  - 1-layer, 6 prompts, 32 tokens: exact `1/6`, mean edit similarity `0.6051`, mean prefix ratio `0.3470`, mean baseline `24.3011` tokens/s, mean fused `20.2237` tokens/s, speed `0.8322x`, guard peak `3571/8151 MiB = 43.81%`
  - 3-layer, 6 prompts, 32 tokens: exact `0/6`, mean edit similarity `0.5221`, mean prefix ratio `0.1862`, mean baseline `25.7576` tokens/s, mean fused `21.8530` tokens/s, speed `0.8484x`, guard peak `3558/8151 MiB = 43.65%`
  - interpretation: the one-prompt shallow speed win does not generalize to this prompt suite; quality-preserving QKV allocation/search is the next blocker.
- Dense-role guard support now exists:
  - scripts changed: `train_python/measure_esmp_fused_qkv_generation.py` and `train_python/eval_fused_qkv_prompt_suite.py`
  - new CLI: `--dense-roles`, accepting QKV suffixes such as `q_proj,k_proj`; selected roles stay on the original dense `nn.Linear` while other roles use fused ESMP. This is a diagnostic upper-bound, not a final quantization method.
  - 1-layer no guard: exact `1/6`, edit `0.6051`, prefix `0.3470`, speed `0.8322x`
  - 1-layer dense `q_proj`: exact `3/6`, edit `0.7448`, prefix `0.6708`, speed `0.7425x`
  - 1-layer dense `k_proj`: exact `1/6`, edit `0.5911`, prefix `0.3519`, speed `0.9673x`
  - 1-layer dense `v_proj`: exact `1/6`, edit `0.6051`, prefix `0.3470`, speed `1.0054x`
  - 1-layer dense `q_proj,k_proj`: exact `4/6`, edit `0.8642`, prefix `0.7722`, speed `0.9095x`
  - 3-layer dense `q_proj,k_proj`: exact `0/6`, edit `0.5347`, prefix `0.3397`, speed `0.9544x`
  - interpretation: Q/K are the first precision-protection targets for layer 0; deeper replacement still needs layer-specific search or real higher-precision Q/K ESMP repack.
- True Q/K 8-bit repack support now exists:
  - script added: `train_python/repack_qkv_precision_guard.py`
  - package variant: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layer0_qk8_guard/pack_summary.json`
  - repacked modules: `model.layers.0.self_attn.q_proj=8` and `model.layers.0.self_attn.k_proj=8`
  - packer verify rel-L2: q `0.009027`, k `0.008710`
  - overall package compression vs FP32: `6.8365x`
  - 1-layer prompt suite with true Q/K 8-bit ESMP, no dense guard: exact `4/6`, edit `0.8248`, prefix `0.7620`, speed `0.9695x`, guard peak `3559/8151 MiB = 43.66%`
  - interpretation: true Q/K 8-bit repack nearly matches the dense Q/K guard's exact recovery while preserving better speed; next step is layer-specific Q/K/head-level precision search for deeper replacement.
- 3-layer QK8/QKV8 repack probes now exist:
  - QK8 package variant: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers017_qk8_guard/pack_summary.json`, compression `6.7754x`
  - QKV8 package variant: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers017_qkv8_guard/pack_summary.json`, compression `6.7553x`
  - 3-layer QK8 prompt suite: exact `0/6`, edit `0.5357`, prefix `0.3397`, speed `0.6724x`, guard peak `3552/8151 MiB = 43.58%`
  - 3-layer QKV8 prompt suite: exact `3/6`, edit `0.7692`, prefix `0.6555`, speed `1.0251x`, guard peak `3554/8151 MiB = 43.60%`
  - interpretation: deeper replacement requires V precision as well as Q/K; the current strongest true ESMP fused-generation result is 3-layer QKV8.
- QKV8 layer-subset search now exists:
  - layers `0,1`: exact `4/6`, edit `0.8469`, prefix `0.7710`, speed `0.8711x`
  - layers `0,7`: exact `4/6`, edit `0.8469`, prefix `0.7710`, speed `0.8502x`
  - layers `1,7`: exact `6/6`, edit `1.0000`, prefix `1.0000`, speed `0.8957x`
  - layers `1,7,13`: exact `5/6`, edit `0.9444`, prefix `0.8934`, speed `0.8089x`
  - layers `1,7,20`: exact `5/6`, edit `0.9383`, prefix `0.9096`, speed `0.8477x`
  - layers `1,7,27`: exact `5/6`, edit `0.9223`, prefix `0.8845`, speed `1.0880x`
  - layers `1,7,13,20,27`: exact `4/6`, edit `0.8970`, prefix `0.8709`, speed `0.9641x`, package compression `6.7055x`
  - interpretation: layer 0 is the dominant drift source; layers 1 and 7 can be replaced together with QKV8 and preserve exact output on this prompt suite. Adding any one of 13/20/27 causes one prompt drift, so the next credible move is head/row-sensitive protection rather than more coarse layer inclusion.
- Row-sensitive repack support now exists:
  - code: `train_python/repack_qkv_precision_guard.py --row-overrides` backed by C++ packer `--row-bits-file`
  - code: `train_python/rank_esmp_row_groups.py` ranks rows/groups by activation-conditioned reconstruction error
  - compile: `python3 -m py_compile train_python/sweep_layer20_v_prompt_groups.py train_python/pack_qwen3_consensus.py train_python/repack_qkv_precision_guard.py train_python/rank_esmp_row_groups.py` passed
  - layer20 V ranking, group size 128: groups `5,2,6,1,4,7,0,3`
  - layer20 QK8/V4 control on layers `1,7,20`: exact `1/6`, edit `0.5789`, prefix `0.3642`, speed `0.8800x`
  - layer20 V front-half rows `0:512` at 8-bit: exact `3/6`, edit `0.6960`, prefix `0.6013`, speed `0.8310x`
  - layer20 V back-half rows `512:1024` at 8-bit: exact `1/6`, edit `0.6741`, prefix `0.4753`, speed `0.9298x`
  - layer20 V top-4 ranked groups `5,2,6,1`: exact `1/6`, edit `0.6365`, prefix `0.5181`, speed `0.9619x`
  - layer20 V top-6 ranked groups `5,2,6,1,4,7`: exact `2/6`, edit `0.7614`, prefix `0.6431`, speed `0.7936x`
  - layer20 full V8 control: exact `5/6`, edit `0.9383`, prefix `0.9096`, speed `0.8477x`
  - prompt-conditioned single 128-row group sweep now exists at `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md`.
  - single-group prompt sweep results: group `0` exact `2/6`, prefix `0.4764`; group `4` exact `2/6`, prefix `0.5374`; every other single group exact `1/6`; full V8 is far better than any single group at exact `5/6`, prefix `0.9096`.
  - prompt-conditioned multi-group candidate sweep now exists at `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_combo_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md`.
  - combo results: `0+4+5+6` exact `4/6`, edit `0.8476`, prefix `0.7418`, speed `0.8819x`; `0+4+6` exact `3/6`, edit `0.7617`, prefix `0.6263`, speed `1.0772x`; other tested combos stay at `1/6` or `2/6`.
  - 5-group expansion sweep now exists at `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_expansion_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md`.
  - expansion results: `0+1+4+5+6` exact `4/6`, prefix `0.7418`; `0+2+4+5+6` exact `3/6`, prefix `0.8286`; `0+3+4+5+6` exact `3/6`, prefix `0.6324`; `0+4+5+6+7` exact `4/6`, prefix `0.7418`.
  - 6-group sweep now exists at `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sixgroup_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md`.
  - best 6-group candidate: `0+1+2+4+5+6` exact `5/6`, edit `0.9700`, prefix `0.9612`, speed `0.9378x`; it fixes prompt 0 but fails prompt 1.
  - 7-group focus now exists at `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sevengroup_focus/LAYER20_V_PROMPT_GROUP_SWEEP.md`.
  - best 7-group candidate: `0+1+2+4+5+6+7` exact `6/6`, edit `1.0000`, prefix `1.0000`, speed `0.9314x`; repeat run also exact `6/6`, edit/prefix `1.0000`, speed `0.9575x`.
  - failure analysis now exists at `outputs/real_system_packer_2026-06-05/LAYER20_V_PROMPT_FAILURE_ANALYSIS.md`.
  - interpretation: this is narrow but important precision-monotonicity failure evidence. Leaving layer20 V group `3` (`384:512`) at 4-bit outperforms full V8 and also outperforms adding group `3`. Do not generalize beyond the six-prompt suite yet.
  - held-out 12-prompt suite now exists at `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v1.txt`.
  - held-out comparison report: `outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/HELDOUT_FAILURE_ANALYSIS.md`.
  - full 6-group held-out sweep report: `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sixgroup_heldout_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md`.
  - held-out results: `1,7` baseline exact `11/12`, full V8 exact `11/12`, original best no-group-3 rowguards `9/12`, and held-out-favored `0+2+3+4+5+6` exact `11/12`.
  - prompt-split transfer audit script: `train_python/compare_prompt_transfer.py`.
  - transfer audit V2 report: `outputs/real_system_packer_2026-06-05/LAYER20_V_ROWGUARD_TRANSFER_AUDIT_V2.md`.
  - split-consensus selector script: `train_python/select_split_consensus_rowguard.py`.
  - split-consensus selector report: `outputs/real_system_packer_2026-06-05/LAYER20_V_SPLIT_CONSENSUS_SELECTOR.md`.
  - selector interpretation: `baseline_layers17` is the safest observed overall policy; `g0_1_2_4_5_6` is only a rowguard candidate needing a third split; no rowguard is currently stable enough to claim generalized deployment.
  - third prompt split: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v2.txt`.
  - third split results: `baseline_layers17` `12/12`, `full_v8` `12/12`, `g0_1_2_4_5_6` `9/12`, `g0_1_2_4_5_6_7` `9/12`, `g0_2_3_4_5_6` `11/12`.
  - multi-split selector script: `train_python/select_multi_split_rowguard.py`.
  - multi-split selector report: `outputs/real_system_packer_2026-06-05/LAYER20_V_MULTI_SPLIT_SELECTOR.md`.
  - multi-split interpretation: `baseline_layers17` remains the only stable reference; best rowguard remains `g0_1_2_4_5_6` but only as `candidate_needs_larger_suite`; stable rowguard remains `none`.
- QKV/hidden/logit proxy drift now exists:
  - script: `train_python/measure_qkv_proxy_drift.py`
  - test: `train_python/test_qkv_proxy_drift.py`
  - selector: `train_python/select_proxy_augmented_rowguard.py`
  - report: `outputs/real_system_packer_2026-06-05/LAYER20_V_PROXY_AUGMENTED_SELECTOR.md`
  - result: `baseline_layers17` is best overall, `full_v8` is second, `g0_1_2_4_5_6_7` is the best rowguard only as a larger-suite candidate, and stable rowguard remains `none`.
  - key proxy drift: rowguards show much larger KV drift than baseline/full-V8; the selector uses this as an early rejection signal before larger generation audits.
- V3 task-style prompt audit now exists:
  - prompt file: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v3_taskstyle.txt`
  - report: `outputs/real_system_packer_2026-06-05/LAYER20_V_V3_TASKSTYLE_AUDIT.md`
  - candidates: `baseline_layers17`, `full_v8`, `g0_1_2_4_5_6_7`
  - results: `baseline_layers17` `19/24`, `full_v8` `19/24`, `g0_1_2_4_5_6_7` `16/24`
  - interpretation: the larger suite reinforces the proxy warning; rowguard remains diagnostic, not deployable.
- V3 rule-scored task wrapper now exists:
  - script: `train_python/score_prompt_suite.py`
  - test: `train_python/test_score_prompt_suite.py`
  - report: `outputs/real_system_packer_2026-06-05/V3_RULE_SCORED_TASK_AUDIT.md`
  - results: `baseline_layers17` baseline/fused rule passes `12/24 -> 13/24`, `full_v8` `12/24 -> 12/24`, `g0_1_2_4_5_6_7` `12/24 -> 13/24`; no shallow rule regressions.
  - caveat: baseline rule pass rate is only `12/24`, so this is a diagnostic wrapper, not a strong benchmark.
- Chat-template prompt-suite support and v3 chat audit now exist:
  - changed scripts: `train_python/measure_esmp_generation_latency.py`, `train_python/eval_fused_qkv_prompt_suite.py`
  - new test: `train_python/test_generation_prompt_format.py`
  - new CLI: `--chat-template`, default off
  - fallback: if `apply_chat_template` fails because local `jinja2` is too old, use Qwen/ChatML-style prompt rendering
  - report: `outputs/real_system_packer_2026-06-05/V3_CHAT_TEMPLATE_AUDIT.md`
  - results: `baseline_layers17` `24/24`, `full_v8` `23/24`, `g0_1_2_4_5_6_7` `22/24`
  - rule-scored chat results: all three candidates `15/24` with zero shallow regressions
  - interpretation: future instruct-model prompt audits should use `--chat-template`; raw-prompt results are completion-style stress tests.
- V4 expected-rule prompt audit now exists:
  - expected suite: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v4_expected.jsonl`
  - report: `outputs/real_system_packer_2026-06-05/V4_EXPECTED_RULE_SCORED_AUDIT.md`
  - scorer CLI: `train_python/score_prompt_suite.py --expected-jsonl ...`
  - results on existing chat-template v3 outputs: all three candidates baseline `15/24`, fused `15/24`, regressions `0`.
  - caveat: strict JSON/YAML/arithmetic/sentence-count rows still fail for both dense baseline and fused outputs; this is a shallow deterministic audit, not an established benchmark.
- Chat task benchmark v1 now exists:
  - runner: `train_python/eval_chat_task_benchmark.py`
  - test: `train_python/test_eval_chat_task_benchmark.py`
  - task file: `data_eval/chat_task_benchmark_v1.jsonl`
  - report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_AUDIT.md`
  - zero-download import path: `--task-format native|mmlu|gsm8k|ifeval`; IFEval currently supports the deterministic `keywords:existence` subset.
  - Qwen3-0.6B baseline, chat-template: `2/12`, mean `22.7031` tok/s, guard peak `3601/8151 MiB = 44.18%`
  - Qwen3-0.6B baseline, chat-template + `/no_think`: `3/12`, mean `23.9036` tok/s, guard peak `3599/8151 MiB = 44.15%`
  - Qwen3-0.6B fused layers `1,7`, chat-template + `/no_think`: baseline `3/12`, fused `3/12`, fused/base tok/s `0.8486x`, guard peak `3590/8151 MiB = 44.04%`
  - interpretation: task accuracy is preserved on this weak smoke baseline, but end-to-end task throughput is not improved.
- Chat task benchmark scorer and IFEval subset were extended:
  - changed files: `train_python/eval_chat_task_benchmark.py`, `train_python/test_eval_chat_task_benchmark.py`, `train_python/measure_esmp_generation_latency.py`, `train_python/test_qkv_proxy_drift.py`
  - new task file: `data_eval/ifeval_deterministic_v2.jsonl`
  - new report: `outputs/real_system_packer_2026-06-05/IFEVAL_V2_DETERMINISTIC_AUDIT.md`
  - scorer now strips visible `<think>...</think>` blocks before deterministic matching; this fixes Qwen answers such as `<think>...</think>\n\nB. ...`.
  - IFEval import now supports deterministic subsets: `keywords:existence`, `keywords:forbidden_words`, `detectable_format:json_format`, `length_constraints:number_sentences`, `length_constraints:number_words`, plus multi-instruction `all_of`.
  - V1 no-think layers `1,7` rerun under the updated scorer: baseline `5/12`, fused `5/12`, fused/base tok/s `0.9157x`, guard peak `3592/8151 MiB = 44.07%`.
  - V1 no-think layers `1,7` V-only role ablation: 32-token result baseline `5/12`, fused `5/12`, fused/base tok/s `1.0142x`, guard peak `3763/8151 MiB = 46.17%`; separate 64-token rerun baseline `7/12`, fused `7/12`, fused/base tok/s `0.9713x`, guard peak `3766/8151 MiB = 46.20%`.
  - V1 no-think layers `1,7,20` V-only expansion: 32-token result baseline `5/12`, fused `5/12`, but fused/base tok/s drops to `0.6903x`, guard peak `3763/8151 MiB = 46.17%`.
  - IFEval-style deterministic v2, layers `1,7`: baseline `2/8`, fused `1/8`, fused/base tok/s `1.0334x`, guard peak `3595/8151 MiB = 44.11%`.
  - IFEval-style deterministic v2 projection-role ablation, layers `1,7`: V-only packed with Q/K dense reaches `2/8 -> 2/8`, fused/base tok/s `1.0872x`, guard peak `3761/8151 MiB = 46.14%`; Q-only reaches `2/8 -> 2/8`, `0.9980x`, guard peak `3753/8151 MiB = 46.04%`; K-only reaches `2/8 -> 2/8`, `0.9366x`, guard peak `3755/8151 MiB = 46.07%`.
  - IFEval-style deterministic v2 V-only expansion to layers `1,7,20`: baseline `2/8`, fused `1/8`, fused/base tok/s `0.8516x`, guard peak `3758/8151 MiB = 46.10%`.
  - interpretation: the stricter IFEval-style slice is negative quality evidence for the fused candidate and should not be presented as a speed win despite slightly higher mean tok/s on this short run.
  - role-ablation interpretation: full QKV replacement regresses IFEval v2, while single-role packed replacement does not on the current small layers `1,7` slices. V-only is the next conservative candidate, but coarse expansion to layer `20` is negative; keep `1,7` as the current boundary and treat layer `20` as needing row/role-specific protection.
- Projection-role selector now exists:
  - script: `train_python/select_projection_role_policy.py`
  - test: `train_python/test_select_projection_role_policy.py`
  - cross-slice report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR.md`
  - IFEval-only report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_IFEVAL_ONLY.md`
  - cross-slice result: `vonly_layers17` is selected as `conservative_candidate`, score `0.9099`, min speed `1.0142x`, max TTFT ratio `0.9302`; full-QKV and layer-20 V-only expansion are rejected for IFEval v2 pass-count regression.
  - IFEval-only result: V-only ranks first, Q-only second, K-only third; full-QKV and layer-20 expansion are rejected.
  - verification: `python -m unittest test_select_projection_role_policy` passed, `python -m py_compile train_python\select_projection_role_policy.py train_python\test_select_projection_role_policy.py` passed, and `python -m unittest test_select_projection_role_policy test_eval_chat_task_benchmark` passed with `Ran 12 tests ... OK`.
- Latest verification:
  - `python3 train_python/test_qkv_proxy_drift.py` passed: `Ran 3 tests ... OK`.
  - `python3 -m py_compile train_python/measure_qkv_proxy_drift.py train_python/test_qkv_proxy_drift.py train_python/select_proxy_augmented_rowguard.py` passed.
  - `python3 train_python/test_score_prompt_suite.py` passed: `Ran 3 tests ... OK`.
  - `python3 -m py_compile train_python/score_prompt_suite.py train_python/test_score_prompt_suite.py` passed.
  - `python3 train_python/test_generation_prompt_format.py` passed: `Ran 3 tests ... OK`.
  - `python3 -m py_compile train_python/measure_esmp_generation_latency.py train_python/eval_fused_qkv_prompt_suite.py train_python/test_generation_prompt_format.py` passed.
  - `cd train_python && python3 -m unittest test_run_with_gpu_guard_disk test_generation_prompt_format test_score_prompt_suite test_qkv_proxy_drift` passed: `Ran 11 tests ... OK`.
  - `cd train_python && python3 -m unittest test_score_prompt_suite test_run_with_gpu_guard_disk test_generation_prompt_format test_qkv_proxy_drift` passed after v4 scoring support: `Ran 12 tests ... OK`.
  - `cd train_python && python3 -m unittest test_eval_chat_task_benchmark test_score_prompt_suite test_run_with_gpu_guard_disk test_generation_prompt_format test_qkv_proxy_drift` passed after official-format importer support: `Ran 19 tests ... OK`.
  - `python3 -m py_compile train_python/run_with_gpu_guard.py train_python/test_run_with_gpu_guard_disk.py train_python/measure_esmp_generation_latency.py train_python/eval_fused_qkv_prompt_suite.py train_python/score_prompt_suite.py` passed.
  - `python3 -m py_compile train_python/eval_chat_task_benchmark.py train_python/test_eval_chat_task_benchmark.py train_python/score_prompt_suite.py train_python/run_with_gpu_guard.py` passed.
  - Python compile passed for `eval_esmp_module_reconstruction.py`, `measure_esmp_generation_latency.py`, `benchmark_esmp_linear_runtimes.py`, `benchmark_esmp_selected_rows.py`, `benchmark_esmp_fused_selected_rows.py`, `measure_esmp_fused_sidecar_generation.py`, `measure_esmp_fused_qkv_generation.py`, `eval_fused_qkv_prompt_suite.py`, `triton_mixed_gemm.py`, and `run_with_gpu_guard.py`.
  - C++ `ctest --test-dir build/cpp-wsl --output-on-failure` passed 28/28.
  - New C++ packer text fixture path is covered by `mixed_precision_packer_text_fixture` and `mixed_precision_runtime_bench_text_fixture`; manifest reports `rows=4`, `cols=8`, `avg_bits=5.25`, bit histogram `{3:1, 4:1, 6:1, 8:1}`, `verify_gemv_rel_l2=0.081011`, `verify_ok=true`.
  - V3 raw guarded generation audits peaked at `3597/8151 MiB = 44.13%`, under the 90% cap.
  - V3 chat-template guarded generation audits peaked at `3599/8151 MiB = 44.15%`, under the 90% cap.
  - GPU after latest local check ended around `2257/8151 MiB` after the disk-aware guard cleanup run.

Do not restart from planning. Continue from the saved local state:

1. Verify the working tree is still the same with `git status --short`.
2. Continue with the next method step: validate the failure-aware task-type policy on a fresh deterministic split or cached official-format MMLU/GSM8K/IFEval slices. Treat layer `0` separately later with dense fallback or FP16/INT8 head protection. Do not repeat completed sweeps/smokes/prompt-suite audits unless the kernel, runtime, module selection, prompt set, or ESMP package changes materially.
3. Keep all generated model binaries local; do not commit `.esmp`, `.f32`, `.raw`, model weights, or large runtime artifacts.
4. Do not commit or push GitHub until Rui explicitly asks again.
5. If C drive free space is under 25 GB, avoid downloading new large models until WSL VHD compaction or user-approved cache/model cleanup. Use the guard form `python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --min-disk-free-gb 15 --cleanup-repo-caches --cleanup-root . --out <guard.json> -- <command>` for future GPU runs. WSL `/home/rui/.cache/huggingface` is about 17 GB but is currently experiment-critical; Ollama/LM Studio caches on Windows are also visible pressure points and should not be deleted without Rui's explicit choice.

If C drive space becomes urgent, run this from an elevated PowerShell after closing WSL:

```powershell
wsl.exe --shutdown
$vhd = 'C:\Users\18042\AppData\Local\wsl\{437898f7-8f9f-4634-98cd-99603dd9b5ec}\ext4.vhdx'
$script = "$env:TEMP\compact-wsl-vhd.txt"
@"
select vdisk file="$vhd"
attach vdisk readonly
compact vdisk
detach vdisk
exit
"@ | Set-Content -LiteralPath $script -Encoding ASCII
diskpart.exe /s $script
Remove-Item -LiteralPath $script -Force
```

## 2026-06-06 Toolchain Recheck: CodeGraph, Understanding Anything, Disk

Rui asked to fix CodeGraph first, add/confirm the Understanding Anything plugin, and keep C drive pressure down before continuing experiments.

Current verified state:

- `codegraph sync .` succeeded from the repo.
- `codegraph status .` reports the index is up to date:
  - files: `111`
  - nodes: `2444`
  - edges: `4499`
  - backend: `node:sqlite - built-in (full WAL)`
- `codegraph query run_with_gpu_guard` works and finds `train_python/run_with_gpu_guard.py`.
- The current CLI uses `query`, not `search`; `codegraph search ...` is an invalid subcommand in this installed version.
- Old CodeGraph MCP processes launched as plain `serve --mcp` were stopped because the watcher had previously hit `.venv-baselines` permission errors.
- `C:\Users\18042\.codex\config.toml` still contains CodeGraph as:

```toml
[mcp_servers.codegraph]
command = 'C:\Users\18042\AppData\Roaming\npm\codegraph.cmd'
args = ["serve", "--mcp", "--no-watch"]
```

- `C:\Users\18042\.hermes\config.yaml` also contains a Windows CodeGraph MCP entry with `serve --mcp --no-watch`.
- Direct `mcp__codegraph.*` tools may still be absent in this already-running Codex Desktop session; use the CodeGraph CLI fallback until a fresh session reloads the MCP tool table.
- `understanding-anything@personal` is installed and enabled according to `codex plugin list`.
- Skill source exists at `C:\Users\18042\.codex\skills\understanding-anything\SKILL.md`.
- Plugin cache exists at `C:\Users\18042\.codex\plugins\cache\personal\understanding-anything\0.1.0`.
- WSL/Hermes skill mirror exists at `/home/rui/.hermes/skills/imported/understanding-anything/SKILL.md`.

Latest C drive snapshot:

- C: latest readback about `19.19 GB` free. It was about `19.5 GB` earlier in the same recheck, then dropped as active Codex/runtime files continued growing.
- GPU idle-ish check around this recheck: `2224-2238 / 8151 MiB`, about `27%` VRAM, utilization about `5%`.
- Targeted visible pressure points:
  - `C:\Users\18042\.ollama`: about `8.56 GB`; do not delete without Rui's explicit choice.
  - `C:\Users\18042\.codex`: about `8.03 GB`; active logs/backups are present, do not delete active Codex logs mid-session.
  - active workspace root: about `5.33 GB`.
  - `C:\Users\18042\AppData\Local\Temp`: about `0.96 GB`.
  - `C:\Users\18042\.cache`: about `0.89 GB`.
- Repo-local guard dry-run:
  - output: `outputs/real_system_packer_2026-06-05/codegraph_disk_cleanup_dry_run_guard.json`
  - `--cleanup-repo-caches --cleanup-dry-run` found `0` targets and `0` bytes reclaimable.
- Latest IFEval v2 and V1 V-only projection-role ablations all used `--min-disk-free-gb 15` and repo-local cleanup. Each cleanup only removed `train_python/__pycache__` at about `0.107 MiB`, so meaningful C-drive relief requires WSL VHD compaction or user-approved model/app cache cleanup, not more repo-cache deletion.
- Continue future GPU runs with:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --min-disk-free-gb 15 --cleanup-repo-caches --cleanup-root . --out <guard.json> -- <command>
```

Do not download additional large models while C: remains below `25 GB` unless the experiment is truly necessary. Prefer cached models and zero-download benchmark slices.
