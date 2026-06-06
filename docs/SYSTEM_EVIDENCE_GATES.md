# System Evidence Gates

This repository separates exploratory output from evidence that can survive a
paper review. A result should be treated as paper-facing only when it is backed
by an executable gate and an explicit claim boundary.

## Triton Mixed-GEMM Gate

The Triton gate consumes `tuning_results.jsonl` from `train_python/tune_triton_blocks.py`.
It verifies:

- enough valid kernel configurations completed;
- at least one grouped packed INT4/INT8 config beat torch FP16;
- grouped execution beat the row-wise dynamic path;
- grouped relative L2 error stayed below a configured ceiling;
- the GPU guard stayed below the configured VRAM ratio.

Example:

```bash
python train_python/gate_triton_tuning.py \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_smoke_2026_06_06/tuning_results.jsonl \
  --out-json outputs/real_system_packer_2026-06-05/triton_tuning_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/TRITON_TUNING_GATE_2026_06_06.md \
  --min-valid-configs 24 \
  --min-fp16-wins 2 \
  --min-best-fp16-speedup 1.20 \
  --min-rowwise-wins 20 \
  --max-rel-l2 0.20 \
  --max-vram-ratio 0.90
```

The `--input` flag is repeatable, so the same gate can validate a multi-shape
family sweep.

Current Qwen-shape family gate:

```bash
python train_python/gate_triton_tuning.py \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_1024x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_2048x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_3072x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_1024x3072_2026_06_06/tuning_results.jsonl \
  --out-json outputs/real_system_packer_2026-06-05/triton_qwen_shape_family_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_FAMILY_GATE_2026_06_06.md \
  --min-valid-configs 96 \
  --min-fp16-wins 8 \
  --min-best-fp16-speedup 2.00 \
  --min-rowwise-wins 70 \
  --max-rel-l2 0.20 \
  --max-vram-ratio 0.90
```

Passing this gate supports only this narrow claim:

```text
For the measured shape family, grouped packed INT4/INT8 Triton execution can
remove row-wise dispatch overhead and can beat torch FP16 in selected tuned
kernel configurations under the configured VRAM guard.
```

It does not support claims about end-to-end LLM speedup, mobile latency, Tensor
Core production readiness, or quantization SOTA.

## Triton Kernel Config Selector

`train_python/select_triton_kernel_configs.py` converts the measured tuning
family into one deterministic config per shape/batch/high_every group. It is a
deployment-planning artifact for the prototype runtime.

Current selector gate:

```bash
python train_python/select_triton_kernel_configs.py \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_1024x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_2048x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_3072x1024_2026_06_06/tuning_results.jsonl \
  --input outputs/real_system_packer_2026-06-05/gpu_tuning_shape_1024x3072_2026_06_06/tuning_results.jsonl \
  --out-json outputs/real_system_packer_2026-06-05/triton_qwen_shape_kernel_config_selector_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_KERNEL_CONFIG_SELECTOR_2026_06_06.md \
  --max-rel-l2 0.20 \
  --max-vram-ratio 0.90 \
  --min-valid-groups 8 \
  --min-fp16-winning-groups 5 \
  --min-best-fp16-speedup 2.00
```

The current selector passes with 8 valid groups, 6 FP16-winning groups, 7
row-wise-winning groups, and max selected grouped/FP16 speedup 2.7647x.

## Selector-Driven Runtime Wiring

`train_python/measure_esmp_generation_latency.py` accepts
`--kernel-config-selector` for the `triton_grouped` runtime. During each swapped
Linear forward, it matches the module shape and runtime batch size to the
nearest measured selector row and records the chosen config in
`replaced_modules[].runtime_config_summary`.

`train_python/gate_selector_runtime_smoke.py` verifies that this wiring actually
used selector configs under the GPU guard. The current smoke gate passes with 8
configs loaded, 4 selector calls, 7.6413x selected-module compression vs FP32,
4 generated tokens, and 57.21% peak guard memory.

`train_python/benchmark_esmp_linear_runtimes.py` also accepts the selector. The
current 1-module Qwen3-0.6B q_proj benchmark confirms selector calls for batch
1 and batch 12, but `triton_grouped` remains slower than dense/cached in those
small-batch cases. Treat this as evidence for the next systems work item:
fusion, persistent scheduling, or a lower-launch-overhead decode path.

## Selected-Row Runtime Gate

`train_python/gate_selected_row_benchmark.py` gates the selected-row routing
benchmark. The current formal gate uses
`outputs/real_system_packer_2026-06-05/esmp_selected_rows.json` and passes with:

- 108 successful rows and 0 failed rows;
- 27 `triton_selected` cases;
- 4 `triton_selected` wins over dense full output;
- best `triton_selected` speedup vs dense full: 2.2406x;
- median `cached_selected` speedup vs dense full: 1.2565x;
- peak guard memory below 90%.

A fresh focused q_proj batch-12 selected-64 smoke was also run. It confirms the
selected-row cached path can win on the current environment (`1.1767x` vs dense
full), while `triton_selected` remains launch-bound (`0.5668x` vs dense full).
Use this as a constraint for kernel/runtime work, not as an acceleration claim.

## Fused Sidecar Generation Gate

`train_python/gate_fused_sidecar_generation.py` gates the fused selected-row
sidecar smoke. This is an integration check, not a replacement claim: sidecar
kernels run on real HF generation activations and discard their outputs while
the dense Transformer path still executes.

Current gate:

```bash
python train_python/gate_fused_sidecar_generation.py \
  --generation-json outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer_async.json \
  --baseline-json outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_baseline_16tok.json \
  --guard-json outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer_async_gpu_guard.json \
  --out-json outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/FUSED_SIDECAR_GENERATION_GATE_2026_06_06.md \
  --min-layers 3 \
  --min-sidecars 3 \
  --min-sidecar-calls 48 \
  --min-calls-per-sidecar 16 \
  --min-selected-rows-total 192 \
  --min-generated-tokens 16 \
  --min-tokens-per-second 20.0 \
  --max-median-sidecar-ms 0.30 \
  --max-max-sidecar-ms 0.50 \
  --require-prefill-shape \
  --require-decode-shape \
  --min-tps-ratio-vs-baseline 0.75 \
  --max-memory-ratio 0.90
```

The current gate passes with 3 sidecars, 48 sidecar calls, exact generated-text
match versus the same-loader baseline, 0.8080x baseline throughput, 0.206160 ms
median sidecar CUDA event time, and 43.96% peak guard memory.

Valid claim:

- fused selected-row ESMP kernels execute inside the real HF generation loop
  with measured CUDA event timing and bounded additive overhead.

Invalid claim:

- sidecar execution proves end-to-end acceleration. It does not replace dense
  QKV computation.

## Fused QKV Replacement Generation Gate

`train_python/gate_fused_qkv_generation.py` gates the stronger replacement
smoke from `train_python/measure_esmp_fused_qkv_generation.py`. This path
actually replaces selected `q_proj`, `k_proj`, and `v_proj` modules with a
shared fused ESMP runtime. The gate checks generation success, compression,
TTFT/throughput versus a same-loader baseline, GPU guard compliance, and the
QKV cache invariant:

```text
wrapper_calls == fused_compute_calls + cache_hits
fused_compute_calls == cache_misses
```

Current gate:

```bash
python train_python/gate_fused_qkv_generation.py \
  --generation-json outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_1layer_64tok.json \
  --baseline-json outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_baseline_64tok.json \
  --guard-json outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_1layer_64tok_gpu_guard.json \
  --out-json outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/FUSED_QKV_GENERATION_GATE_2026_06_06.md \
  --min-replacements 1 \
  --min-generated-tokens 64 \
  --min-tokens-per-second 25.0 \
  --min-compression-vs-fp32 6.0 \
  --max-median-replacement-ms 0.25 \
  --max-max-replacement-ms 0.70 \
  --min-wrapper-calls-per-replacement 192 \
  --min-fused-compute-calls-per-replacement 64 \
  --min-cache-hits-per-replacement 128 \
  --min-cache-misses-per-replacement 64 \
  --min-tps-ratio-vs-baseline 1.05 \
  --max-ttft-ratio-vs-baseline 1.00 \
  --min-common-prefix-chars 100 \
  --max-memory-ratio 0.90
```

The current gate passes on Qwen3-0.6B layer-0 QKV replacement with 64 generated
tokens, 1.1300x tokens/s versus the same-loader baseline, 0.6839x TTFT ratio,
6.1682x compression versus FP32, 192/64/128/64 wrapper/fused/hit/miss calls,
0.192896 ms median replacement CUDA event time, and 44.01% peak guard memory.
The generated text is not an exact match, but it keeps a 210-character common
prefix in this smoke; quality preservation remains a separate open gate.

Valid claim:

- a shallow fused packed QKV replacement can execute inside HF generation and
  shows guarded smoke-level speed and memory evidence.

Invalid claim:

- this establishes full-model quality-preserving quantized generation.

## Fused QKV Prompt-Suite Quality Gate

`train_python/gate_fused_qkv_prompt_suite.py` gates the prompt-suite quality
audit from `train_python/eval_fused_qkv_prompt_suite.py`, optionally combined
with deterministic shallow task scoring from `train_python/score_prompt_suite.py`.
This gate deliberately separates quality preservation from speed. It checks:

- exact/similarity/prefix preservation across the prompt suite;
- optional rule-scored pass-rate preservation and zero new regressions;
- replacement compression and median CUDA event latency;
- QKV cache invariants;
- GPU guard compliance.

Current gate:

```bash
python train_python/score_prompt_suite.py \
  --input-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack.json \
  --out-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack_scored.json \
  --out-md outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS17_QKV8_REPACK_SCORED.md

python train_python/gate_fused_qkv_prompt_suite.py \
  --prompt-suite-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack.json \
  --scored-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack_scored.json \
  --guard-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack_gpu_guard.json \
  --out-json outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_GATE_2026_06_06.md \
  --min-prompts 6 \
  --min-exact-matches 6 \
  --min-exact-match-rate 1.0 \
  --min-mean-char-edit-similarity 0.99 \
  --min-median-char-edit-similarity 0.99 \
  --min-mean-common-prefix-ratio 0.99 \
  --min-mean-speed-ratio 0.80 \
  --max-median-ttft-ratio 1.25 \
  --min-compression-vs-fp32 3.5 \
  --max-median-replacement-ms 0.25 \
  --min-wrapper-calls 1152 \
  --min-fused-compute-calls 384 \
  --min-cache-hits 768 \
  --min-cache-misses 384 \
  --min-scored-prompts 6 \
  --max-rule-regressions 0 \
  --min-fused-rule-pass-rate 0.80 \
  --max-fused-rule-pass-drop 0 \
  --max-memory-ratio 0.90
```

The current gate passes on the layers `[1, 7]` QKV8 repack candidate with 6/6
exact prompt-suite matches, 1.0 mean edit similarity, 0 rule regressions,
3.9082x compression versus FP32, 1152/384/768/384 wrapper/fused/hit/miss calls,
0.141008 ms median replacement CUDA event time, and 43.59% peak guard memory.
It is slower than the baseline on this suite (0.8957x mean tokens/s), so it is
quality-preservation evidence rather than acceleration evidence.

Valid claim:

- a conservative QKV8 repack candidate preserves the measured prompt-suite
  outputs and shallow rule scores under the configured gate.

Invalid claim:

- this proves semantic quality preservation across tasks, datasets, or larger
  prompt distributions.

## Chat Task Stress-Retention Gate

`train_python/gate_chat_task_regression_analysis.py` gates deterministic
chat-task retention results from `train_python/eval_chat_task_benchmark.py` and
`train_python/analyze_chat_task_regressions.py`. This is stronger than pure
text similarity because rows are scored by task-specific rules, but it is still
a local stress suite rather than a public benchmark replacement.

Current gate:

```bash
python train_python/gate_chat_task_regression_analysis.py \
  --analysis-json outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_regression_analysis.json \
  --candidate konly_layers17 \
  --guard-json outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_qwen3_0p6b_no_think_layers17_konly_32tok_gpu_guard.json \
  --out-json outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_GATE_2026_06_06.md \
  --min-candidates 3 \
  --min-tasks 84 \
  --min-task-types 8 \
  --min-baseline-passes 46 \
  --min-fused-passes 45 \
  --min-fused-accuracy 0.535 \
  --max-pass-loss 1 \
  --max-regressions 1 \
  --max-regressions-per-type 1 \
  --min-speedup 0.95 \
  --max-memory-ratio 0.90
```

The current gate passes for `konly_layers17` with 84 tasks across 8 task types.
Baseline passes 46/84 and fused passes 45/84, so the candidate has one allowed
regression and a pass delta of -1. Mean fused/baseline speed is 0.9746x and
peak guard memory is 54.69%. The single regression is preserved in the report:
`stress_json_keys_001` loses a required JSON-key parse.

Valid claim:

- the K-only layers `[1, 7]` replacement candidate survives a deterministic
  84-task stress-retention gate under a one-regression budget.

Invalid claim:

- this is a public benchmark result or proof of broad task-quality
  preservation.

## C++ ESMP Runtime Sweep Gate

`train_python/gate_cpp_runtime_sweep.py` gates the C++ ESMP selected-row runtime
sweep. The current gate uses
`outputs/real_system_packer_2026-06-05/esmp_runtime_stratified_sweep.jsonl` and
passes with:

- 42 successful module runs and 0 failures;
- 42/42 selected-row wins over full mixed GEMV;
- min selected/full speedup: 12.7607x;
- median selected/full speedup: 16.8259x;
- best selected/full speedup: 56.4888x;
- median selected-row latency: 0.205620 ms;
- median compression vs FP32: 7.6413x.

A fresh C++ q_proj focus bench was also run against the current binary and
package, giving 29.1892x selected/full speedup for 64 active rows. This is the
strongest current systems evidence for deterministic routed/bypass execution,
but it is still module-level evidence rather than end-to-end generation
latency.

Valid claim:

- measured Triton tuning artifacts can now drive the prototype ESMP generation
  path instead of remaining an offline report;
- output JSON exposes which measured block config was used.
- a small selector-driven runtime smoke is automatically gated for selector use,
  compression, generated-token presence, and GPU memory guard compliance.
- selector-driven module-runtime benchmark records per-case selector calls and
  currently exposes low-batch kernel overhead rather than speedup.
- selected-row routing has a formal gate for module-level evidence, while the
  focused current-environment smoke keeps the low-batch Triton limitation
  explicit.
- fused selected-row sidecars have a formal decode-loop integration gate with
  bounded additive overhead.
- fused packed QKV replacement has a formal guarded smoke gate for shallow
  replacement, including cache-invariant checks.
- fused QKV prompt-suite quality has a formal gate for the conservative
  layers `[1, 7]` QKV8 repack candidate.
- chat-task stress retention has a formal 84-task gate with the remaining
  one-row regression explicitly reported.
- C++ ESMP selected-row runtime has a formal sweep gate; it supports
  module-level bypass claims but not full LLM acceleration claims.

Invalid claim:

- selector-driven generation is faster end-to-end;
- selector coverage generalizes to unmeasured shapes;
- fused QKV replacement is quality-preserving across prompts or layers;
- prompt-suite exact preservation on six prompts is a broad semantic benchmark;
- deterministic chat-task stress passing under a regression budget replaces
  public MMLU/GSM8K/IFEval-style evaluation;
- mobile, Tensor Core production, or CCF-A system claims are established.
