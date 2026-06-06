# EigenSkill-Q Real-System Packer Handoff

Stop time: 2026-06-05, before Codex update.

Instruction from Rui: stop, save all local state, and make sure saying "继续" resumes directly.

## Resume Rule

When Rui says "继续":

1. Read this file first.
2. Do not ask him to restate context.
3. Do not commit or push GitHub unless he explicitly asks.
4. Read `REAL_SYSTEM_RESULTS_2026_06_06.md`.
5. Continue from "Next Commands" below.

## Repo

- Workspace: `C:\Users\18042\Documents\Codex\2026-06-01\chatgpt-context-request-algorithm-system-co`
- Repo: `C:\Users\18042\Documents\Codex\2026-06-01\chatgpt-context-request-algorithm-system-co\github_publish\eigenskill-research-pack`
- Branch: `main`
- Remote: `https://github.com/rui4399/eigenskill-research-pack.git`
- Current pushed commit before this work: `0560d8f Add C++ task accuracy comparison gate`
- GitHub commit/push: not done in this stop point.

## What Was Implemented This Round

Real packer and systems path:

- Added `inference_cpp/src/mixed_precision_packer.cpp`
  - Binary format: `ESMPQ001`
  - Header + row metadata + packed payload.
  - Per-row fields: bit width, scale, bit offset, row sum.
  - Supports raw FP32 input and synthetic fixture input.
  - Can reload the binary and verify GEMV correctness.
- Updated `inference_cpp/CMakeLists.txt`
  - Adds executable `mixed_precision_packer`.
  - Adds CTest `mixed_precision_packer_smoke`.
  - Adds CTest coverage for external ASCII row-major weight fixtures:
    - `mixed_precision_packer_text_fixture`
    - `mixed_precision_runtime_bench_text_fixture`
- Updated `.gitignore`
  - Added local-only protection for `*.esmp`, `*.f32`, `*.raw`.
- Added `train_python/pack_qwen3_consensus.py`
  - Loads HF Qwen model.
  - Parses allocation JSON.
  - Exports each selected Linear weight to temporary raw FP32.
  - Calls C++ packer to write `.esmp` and per-module manifests.
- Added `train_python/triton_mixed_gemm.py`
  - Minimal CUDA/Triton row-wise mixed INT4/INT8 dequant matmul benchmark.
  - Reports latency, speedup vs torch fp16, rel-L2, memory.
- Added `train_python/tune_triton_blocks.py`
  - Runs guarded block-size sweeps over packed mixed Triton GEMM.
- Added `train_python/summarize_triton_tuning.py`
  - Aggregates cross-shape Triton tuning JSONL files into JSON/CSV/Markdown.
- Added `train_python/run_esmp_runtime_sweep.py`
  - Runs a stratified C++ ESMP runtime sweep over real packed Qwen3-0.6B modules.
- Added `train_python/eval_esmp_module_reconstruction.py`
  - Loads real ESMP binary packages.
  - Reconstructs signed symmetric per-row mixed INT4/INT8 weights from the `ESMPQ001` bitstream.
  - Samples real Linear-module activations from prompts.
  - Compares `F.linear(x, original_weight)` against `F.linear(x, ESMP_dequant_weight)`.
  - Writes JSON, JSONL, and Markdown quality-side reconstruction reports.
- Added `train_python/measure_esmp_generation_latency.py`
  - Minimal generation-path wiring check for real ESMP packages.
  - Can run `--no-esmp` same-loader baseline, cached dequant, on-demand ESMP dequant, or `--runtime triton_grouped`.
  - Replaces selected `torch.nn.Linear` modules with `EsmpLinear`.
  - Measures TTFT, tokens/sec, generated text, selected package compression, and peak CUDA memory.
- Added `train_python/benchmark_esmp_linear_runtimes.py`
  - Isolates real ESMP-backed Linear runtime latency across batch shapes.
  - Compares dense, cached dequant, Python on-demand dequant, and Triton grouped runtime.
  - Writes JSON, JSONL, CSV, and Markdown reports.
- Added selected-row Triton kernels in `train_python/triton_mixed_gemm.py`
  - `_int4_selected_matmul_kernel`
  - `_int8_selected_matmul_kernel`
- Added `train_python/benchmark_esmp_selected_rows.py`
  - Benchmarks the routing/bypass case where only selected output rows are computed.
  - Compares full dense, dense selected-row, cached-dequant selected-row, and packed Triton selected-row paths.
  - Writes JSON, JSONL, CSV, and Markdown reports.
- Added `train_python/benchmark_esmp_fused_selected_rows.py`
  - Concatenates selected packed rows across same-input QKV modules.
  - Compares strong dense full/selected concat baselines, cached selected concat, per-module Triton selected, and fused Triton selected.
  - Writes JSON, JSONL, CSV, Markdown, and GPU guard evidence.
- Added `train_python/measure_esmp_fused_sidecar_generation.py`
  - Attaches fused QKV selected-row ESMP sidecars to real HF generation through q_proj pre-hooks.
  - Executes packed fused selected-row kernels on live decode hidden states, records CUDA event timing, and discards sidecar output.
  - Measures TTFT, tokens/s, generated text, peak CUDA memory, guard memory, sidecar call counts, and per-call latency.
- Added `train_python/measure_esmp_fused_qkv_generation.py`
  - Replaces selected `q_proj`, `k_proj`, and `v_proj` modules with shared fused packed ESMP QKV wrappers.
  - Q computes the concatenated packed Q/K/V projection once; K/V read cached slices.
  - Measures TTFT, tokens/s, generated text, peak CUDA memory, guard memory, compression, cache hits/misses, and fused CUDA event timing.
- Added `train_python/measure_generation_latency.py`
  - Measures TTFT, tokens/sec, elapsed time, and peak GPU memory for HF generation.
- Extended `train_python/run_with_gpu_guard.py`
  - Adds disk-state recording to guard JSON logs.
  - Adds `--min-disk-free-gb` and `--disk-check-path` for preflight disk pressure checks.
  - Adds opt-in `--cleanup-repo-caches`, `--cleanup-root`, and `--cleanup-dry-run` for post-run repo-local cache cleanup.
  - Cleanup is intentionally narrow: repo-local `__pycache__`, `.pytest_cache`, `.ruff_cache`, `*.pyc`, and `*.pyo`; `.git`, `.codegraph`, `outputs`, `build`, `research_pack_2026-06-03`, and `.venv*` directories are skipped.
- Added `train_python/test_run_with_gpu_guard_disk.py`
  - Covers disk-state reporting.
  - Covers repo-local cache cleanup and verifies `outputs/` caches are preserved.
- Extended `inference_cpp/src/mixed_precision_packer.cpp`
  - Adds `--weights-text path` for small external ASCII row-major float matrix fixtures.
  - Keeps source validation strict: exactly one of `--synthetic`, `--weights-f32`, or `--weights-text`.
  - Manifest `source` now records text, raw-FP32, or synthetic input origin.
- Added packer fixture files:
  - `inference_cpp/testdata/mixed_precision_weights_fixture.txt`
  - `inference_cpp/testdata/mixed_precision_row_bits_fixture.txt`
- Added `mobile/redmi_k80_pro/neon_mixed_decode.cpp`
  - ARM NEON mixed INT4/INT8 decode + GEMV kernel scaffold.
  - Compiles on x86 fallback for smoke; real NEON needs phone/NDK build.

Previous same-session changes already present and still uncommitted:

- README cleanup to calibration split instability / consensus allocation scope.
- Purge of leaked v2 data and speculative swarm/acoustic public artifacts.
- C++ policy bypass regex-free parser and exact decision gate.
- Completion-only LoRA training path.
- AVX2 INT4 kernel updates including maddubs path.
- `train_python/allocator.py` Lagrangian allocator.
- GPU guard max-length ceiling.
- Paper intro update with 0.0 LoRA vs 100% deterministic bypass motivation.

## Verification Completed

C++ build:

```bash
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack && cmake -S inference_cpp -B build/cpp-wsl -DCMAKE_BUILD_TYPE=Release && cmake --build build/cpp-wsl -j2"
```

Result: passed, including `mixed_precision_packer`.

CTest:

```bash
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack && ctest --test-dir build/cpp-wsl --output-on-failure"
```

Result: `100% tests passed, 0 tests failed out of 28`.

Latest text-fixture packer verification:

- manifest: `build/cpp-wsl/mixed_precision_packer_text_fixture.json`
- rows: `4`
- cols: `8`
- average bits: `5.25`
- bit histogram: `{3: 1, 4: 1, 6: 1, 8: 1}`
- verify GEMV rel-L2: `0.081011`
- verify OK: `true`

Python compile:

```bash
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack && python3 -m py_compile train_python/train_lora.py train_python/allocator.py train_python/run_with_gpu_guard.py train_python/parse_quant_kernel_bench.py train_python/pack_qwen3_consensus.py train_python/triton_mixed_gemm.py train_python/measure_generation_latency.py"
```

Result: passed.

Latest Python compile after adding activation reconstruction, ESMP generation smoke, ESMP Linear runtime-shape benchmark, and ESMP selected-row benchmark:

```bash
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack && python3 -m py_compile train_python/eval_esmp_module_reconstruction.py train_python/measure_esmp_generation_latency.py train_python/benchmark_esmp_linear_runtimes.py train_python/benchmark_esmp_selected_rows.py train_python/triton_mixed_gemm.py train_python/run_with_gpu_guard.py"
```

Result: passed.

Latest Python tests after adding disk-aware GPU guard cleanup:

```bash
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/train_python && python3 -m unittest test_run_with_gpu_guard_disk test_generation_prompt_format test_score_prompt_suite test_qkv_proxy_drift"
```

Result: `Ran 11 tests in 0.030s`, passed.

Latest Python tests after adding v4 expected-rule scoring:

```bash
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/train_python && python3 -m unittest test_score_prompt_suite test_run_with_gpu_guard_disk test_generation_prompt_format test_qkv_proxy_drift"
```

Result: `Ran 12 tests in 0.041s`, passed.

Latest Python tests after adding chat task benchmark v1:

```bash
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/train_python && python3 -m unittest test_eval_chat_task_benchmark test_score_prompt_suite test_run_with_gpu_guard_disk test_generation_prompt_format test_qkv_proxy_drift"
```

Result: `Ran 15 tests in 0.036s`, passed.

Latest Python tests after adding zero-download official-format import:

```bash
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/train_python && python3 -m unittest test_eval_chat_task_benchmark test_score_prompt_suite test_run_with_gpu_guard_disk test_generation_prompt_format test_qkv_proxy_drift"
```

Result: `Ran 19 tests in 0.037s`, passed.

Latest Python compile after adding disk-aware GPU guard cleanup:

```bash
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack && python3 -m py_compile train_python/run_with_gpu_guard.py train_python/test_run_with_gpu_guard_disk.py train_python/measure_esmp_generation_latency.py train_python/eval_fused_qkv_prompt_suite.py train_python/score_prompt_suite.py"
```

Result: passed.

Latest Python compile after adding fused sidecar generation smoke:

```bash
wsl.exe -e bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack && python3 -m py_compile train_python/measure_esmp_fused_sidecar_generation.py"
```

Result: passed.

Latest Python compile after adding fused QKV replacement generation smoke:

```bash
wsl.exe -e bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack && python3 -m py_compile train_python/measure_esmp_fused_qkv_generation.py"
```

Result: passed.

Latest Python compile after adding layer20 V prompt-conditioned sweep support:

```bash
wsl.exe -e bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack && python3 -m py_compile train_python/sweep_layer20_v_prompt_groups.py train_python/pack_qwen3_consensus.py train_python/repack_qkv_precision_guard.py train_python/rank_esmp_row_groups.py"
```

Result: passed.

Packer synthetic run:

```bash
./build/cpp-wsl/mixed_precision_packer --synthetic --rows 1024 --cols 1024 --default-bits 4 --sensitive-every 16 --sensitive-bits 8 --out outputs/real_system_packer_2026-06-05/synthetic_qwen_style_1024x1024.esmp --manifest-out outputs/real_system_packer_2026-06-05/synthetic_qwen_style_1024x1024_manifest.json --verify
```

Result:

- `ok: true`
- format: `ESMPQ001`
- raw FP32 bytes: `4194304`
- total package bytes: `581696`
- compression ratio vs FP32: `7.210474`
- verify GEMV rel-L2: `0.105745`

C++ AVX2 kernel benchmark:

- Output: `outputs/real_system_packer_2026-06-05/eigenskill_quant_kernel_benchmark_avx2_maddubs.txt`
- Parsed summary: `outputs/real_system_packer_2026-06-05/eigenskill_quant_kernel_benchmark_avx2_maddubs_summary.json`
- Key result: `int4_maddubs_faster_than_dense_cases = 9`
- Best full INT4 maddubs speedup: `21.53x` vs scalar dense in the benchmark table.
- Important caveat: rel-L2 for INT4/maddubs is about `0.13-0.15`; this is a speed/approximation result, not lossless inference.
- Mixed generic full path is still slow; selected-row mixed path has useful cases.

Lagrangian allocator smoke:

- Output JSON: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_lagrangian_alloc_4to8_summary.json`
- Output report: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_lagrangian_alloc_4to8_report.md`
- Result:
  - average bits: `4.499670112161865`
  - bit histogram: `{4: 153, 8: 44}`

Mobile kernel smoke on x86 fallback:

- Source: `mobile/redmi_k80_pro/neon_mixed_decode.cpp`
- Output JSON: `outputs/real_system_packer_2026-06-05/neon_mixed_decode_x86_smoke.json`
- Result:
  - rows: `128`
  - cols: `256`
  - `neon_enabled: false`
  - mixed ms: `0.173234`
  - rel-L2 vs FP32 dense: `0.113049`

GPU/dependency check before stopping:

- GPU: `NVIDIA GeForce RTX 5070 Laptop GPU`
- VRAM current at check: `2813 / 8151 MiB`
- GPU util at check: `20%`
- Python deps in WSL:
  - `torch OK 2.12.0+cu130`
  - `transformers OK 5.8.1`
  - `triton OK 3.7.0`
  - `safetensors OK 0.7.0`
  - `cuda_available True`

## Local Output Files

Directory:

`C:\Users\18042\Documents\Codex\2026-06-01\chatgpt-context-request-algorithm-system-co\github_publish\eigenskill-research-pack\outputs\real_system_packer_2026-06-05`

Known files:

- `synthetic_qwen_style_1024x1024.esmp`
- `synthetic_qwen_style_1024x1024_manifest.json`
- `mixed_precision_packer_synthetic_stdout.json`
- `eigenskill_quant_kernel_benchmark_avx2_maddubs.txt`
- `eigenskill_quant_kernel_benchmark_avx2_maddubs_summary.json`
- `qwen3_0p6b_lagrangian_alloc_4to8_summary.json`
- `qwen3_0p6b_lagrangian_alloc_4to8_report.md`
- `neon_mixed_decode_x86_smoke`
- `neon_mixed_decode_x86_smoke.json`
- `RESUME_HANDOFF.md`
- `REAL_SYSTEM_RESULTS_2026_06_06.md`
- `TRITON_CROSS_SHAPE_SUMMARY.md`
- `triton_cross_shape_summary.json`
- `triton_cross_shape_summary.csv`
- `triton_tuning/tuning_results.jsonl`
- `triton_tuning_3072x1024/tuning_results.jsonl`
- `triton_tuning_1024x3072/tuning_results.jsonl`
- `ESMP_RUNTIME_STRATIFIED_SWEEP.md`
- `esmp_runtime_stratified_sweep.jsonl`
- `esmp_runtime_stratified_sweep.csv`
- `ESMP_ACTIVATION_SMOKE.md`
- `esmp_activation_smoke.json`
- `esmp_activation_smoke.jsonl`
- `esmp_activation_smoke_gpu_guard.json`
- `ESMP_ACTIVATION_RECONSTRUCTION.md`
- `esmp_activation_reconstruction.json`
- `esmp_activation_reconstruction.jsonl`
- `esmp_activation_reconstruction_gpu_guard.json`
- `ESMP_ACTIVATION_ALL_LINEAR.md`
- `esmp_activation_all_linear.json`
- `esmp_activation_all_linear.jsonl`
- `esmp_activation_all_linear_gpu_guard.json`
- `ESMP_SWAPPED_GENERATION_SMOKE.md`
- `qwen3_same_loader_16tok_latency.json`
- `qwen3_same_loader_16tok_gpu_guard.json`
- `qwen3_esmp_swapped_3mod_cached_latency_seq.json`
- `qwen3_esmp_swapped_3mod_cached_gpu_guard_seq.json`
- `qwen3_esmp_swapped_3mod_ondemand_latency.json`
- `qwen3_esmp_swapped_3mod_ondemand_gpu_guard.json`
- `qwen3_esmp_swapped_3mod_triton_latency.json`
- `qwen3_esmp_swapped_3mod_triton_gpu_guard.json`
- `qwen3_same_loader_16tok_warm_latency.json`
- `qwen3_same_loader_16tok_warm_gpu_guard.json`
- `qwen3_esmp_swapped_3mod_cached_warm_latency.json`
- `qwen3_esmp_swapped_3mod_cached_warm_gpu_guard.json`
- `qwen3_esmp_swapped_3mod_ondemand_warm_latency.json`
- `qwen3_esmp_swapped_3mod_ondemand_warm_gpu_guard.json`
- `qwen3_esmp_swapped_3mod_triton_warm_latency.json`
- `qwen3_esmp_swapped_3mod_triton_warm_gpu_guard.json`
- `ESMP_LINEAR_RUNTIME_SHAPES.md`
- `esmp_linear_runtime_shapes.json`
- `esmp_linear_runtime_shapes.jsonl`
- `esmp_linear_runtime_shapes.csv`
- `esmp_linear_runtime_shapes_gpu_guard.json`
- `ESMP_SELECTED_ROWS.md`
- `esmp_selected_rows.json`
- `esmp_selected_rows.jsonl`
- `esmp_selected_rows.csv`
- `esmp_selected_rows_gpu_guard.json`
- `ESMP_SELECTED_ROWS_SMOKE.md`
- `esmp_selected_rows_smoke.json`
- `esmp_selected_rows_smoke.jsonl`
- `esmp_selected_rows_smoke.csv`
- `esmp_selected_rows_smoke_gpu_guard.json`

## Latest Results Added After Resume

Triton cross-shape tuning:

- total configs: `216`
- valid configs: `216`
- configs faster than torch FP16: `26`
- configs faster than row-wise dynamic mixed path: `134`
- max grouped/FP16 speedup: `2.1048x`
- p90 grouped/FP16 speedup: `1.2625x`
- max grouped/row-wise speedup: `5.7507x`
- median compression vs FP16: `3.6203x`
- median grouped rel-L2: `0.1375`
- max guard VRAM ratio: `0.3019`

C++ ESMP runtime stratified sweep:

- module runs: `42`
- successful: `42`
- layers: `0, 1, 7, 13, 20, 27`
- modules: q/k/v/o projections and MLP gate/up/down
- median full packed GEMV: `6.3678 ms`
- median selected 64-row GEMV: `0.2056 ms`
- median selected/full speedup: `16.8259x`
- max selected/full speedup: `56.4888x`
- median compression vs FP32: `7.6413x`

ESMP activation reconstruction:

- script: `train_python/eval_esmp_module_reconstruction.py`
- smoke package: 3 modules, all successful
  - median output rel-L2: `0.0762`
  - median normalized output MSE: `0.005799`
  - median weight rel-L2: `0.1508`
  - guard peak: `3546/8151 MiB = 43.50%`
- stratified full-package check:
  - module runs: `42`
  - successful: `42`
  - layers: `0, 1, 7, 13, 20, 27`
  - modules: q/k/v/o projections and MLP gate/up/down
  - median output rel-L2: `0.1260`
  - p90 output rel-L2: `0.2028`
  - median normalized output MSE: `0.015893`
  - median compression vs FP32: `7.6413x`
  - guard peak: `3547/8151 MiB = 43.52%`
- all-Linear full-package check, excluding `lm_head`:
  - module runs: `196`
  - successful: `196`
  - median output rel-L2: `0.1363`
  - p90 output rel-L2: `0.2114`
  - median normalized output MSE: `0.018590`
  - median weight rel-L2: `0.1575`
  - median compression vs FP32: `7.6414x`
  - family medians:
    - attention: `112` modules, output rel-L2 `0.1351`
    - mlp: `84` modules, output rel-L2 `0.1605`
  - guard peak: `3553/8151 MiB = 43.59%`

ESMP-swapped generation smoke:

- script: `train_python/measure_esmp_generation_latency.py`
- swapped modules: layer-0 `q_proj`, `k_proj`, `v_proj`
- selected package compression vs FP32: `6.1682x`
- primary sequential runs, `max_new_tokens=16`:
  - same-loader HF baseline: TTFT `0.9489 s`, elapsed `1.6793 s`, `9.5277 tokens/s`, guard peak `3543/8151 MiB = 43.47%`
  - cached dequant: TTFT `0.9542 s`, elapsed `1.7212 s`, `9.2958 tokens/s`, guard peak `3556/8151 MiB = 43.63%`
  - on-demand dequant: TTFT `1.1813 s`, elapsed `2.9897 s`, `5.3516 tokens/s`, guard peak `3545/8151 MiB = 43.49%`
  - Triton grouped: TTFT `1.9611 s`, elapsed `3.2027 s`, `4.9957 tokens/s`, guard peak `3551/8151 MiB = 43.57%`
- one-warmup sequential runs, `max_new_tokens=16`:
  - same-loader HF baseline: TTFT `0.0347 s`, elapsed `0.6387 s`, `25.0523 tokens/s`, guard peak `3559/8151 MiB = 43.66%`
  - cached dequant: TTFT `0.0320 s`, elapsed `0.5550 s`, `28.8295 tokens/s`, guard peak `3543/8151 MiB = 43.47%`
  - on-demand dequant: TTFT `0.1543 s`, elapsed `1.7552 s`, `9.1157 tokens/s`, guard peak `3544/8151 MiB = 43.48%`
  - Triton grouped: TTFT `0.0458 s`, elapsed `0.7484 s`, `21.3777 tokens/s`, guard peak `3548/8151 MiB = 43.53%`
- generated text matched across all four primary sequential runs
- generated text also matched across the Triton grouped runs
- important caveat: earlier non-`seq` baseline/cached JSON files were produced concurrently and should not be used for timing claims

ESMP Linear runtime-shape benchmark:

- script: `train_python/benchmark_esmp_linear_runtimes.py`
- output report: `outputs/real_system_packer_2026-06-05/ESMP_LINEAR_RUNTIME_SHAPES.md`
- model: `Qwen/Qwen3-0.6B`
- modules: layer-0 `q_proj`, `k_proj`, `v_proj`
- batches: `1, 12, 64`
- warmup / iters: `10 / 80`
- guard peak: `3555/8151 MiB = 43.61%`
- script peak CUDA memory allocated: `1178.79 MiB`
- summary:
  - dense median: `0.014725 ms`
  - cached median: `0.016797 ms`, median speedup vs dense `0.8801x`, median rel-L2 `0.150103`
  - Python on-demand median: `18.072527 ms`, median speedup vs dense `0.0009x`
  - Triton grouped median: `0.051871 ms`, median speedup vs dense `0.2667x`
- interpretation: the ESMP Linear runtime path works, but the current standalone Triton grouped kernel is slower than dense for these small Qwen3 layer-0 shapes. Next kernel work should target decode-specific lower-overhead execution, selected-row execution, or fusion.

ESMP selected-row GPU benchmark:

- new kernels:
  - `train_python/triton_mixed_gemm.py::_int4_selected_matmul_kernel`
  - `train_python/triton_mixed_gemm.py::_int8_selected_matmul_kernel`
- script: `train_python/benchmark_esmp_selected_rows.py`
- output report: `outputs/real_system_packer_2026-06-05/ESMP_SELECTED_ROWS.md`
- model: `Qwen/Qwen3-0.6B`
- modules: layer-0 `q_proj`, `k_proj`, `v_proj`
- batches: `1, 12, 64`
- selected rows: `16, 64, 256`
- warmup / iters: `10 / 80`
- guard peak: `3561/8151 MiB = 43.69%`
- script peak CUDA memory allocated: `1177.11 MiB`
- summary:
  - dense full median: `0.019498 ms`
  - dense selected median: `0.020063 ms`
  - cached selected median: `0.020115 ms`
  - Triton selected median: `0.049162 ms`
  - Triton selected faster than dense full: `4/27` cases
  - Triton selected faster than dense selected: `4/27` cases
  - best Triton selected speedup vs dense full: `2.2406x`
  - best Triton selected speedup vs dense selected: `1.9858x`
- interpretation: selected-row packed GPU execution is implemented and has useful best-case evidence, but the median remains slower due to launch/tiling overhead.

ESMP fused QKV selected-row GPU benchmark:

- script: `train_python/benchmark_esmp_fused_selected_rows.py`
- output report: `outputs/real_system_packer_2026-06-05/ESMP_FUSED_SELECTED_ROWS.md`
- model: `Qwen/Qwen3-0.6B`
- modules: QKV projections on layers `0, 1, 7, 13, 20, 27`
- batches: `1, 12, 64`
- selected rows per module: `16, 64, 256`
- warmup / iters: `10 / 80`
- guard peak: `3601/8151 MiB = 44.18%`
- script peak CUDA memory allocated: `1201.36 MiB`
- summary:
  - dense full concat median: `0.033235 ms`
  - dense selected concat median: `0.025728 ms`
  - cached selected concat median: `0.019379 ms`
  - per-module Triton selected median: `0.231445 ms`
  - fused Triton selected median: `0.104230 ms`
  - fused faster than per-module Triton selected: `52/54` cases
  - median fused speedup vs per-module Triton selected: `2.0873x`
  - best fused speedup vs per-module Triton selected: `10.2491x`
  - fused faster than dense full concat: `3/54` cases
  - fused faster than dense selected concat: `3/54` cases
  - median fused rel-L2 vs dense selected concat: `0.142890`
  - max fused rel-L2 vs per-module Triton selected: `0.0`
- interpretation: QKV fusion reduces packed selected-row launch overhead and is a useful systems contribution, but dense concat remains the stronger median baseline.

ESMP fused QKV selected-row block tuning:

- sweep report: `outputs/real_system_packer_2026-06-05/fused_block_sweep/ESMP_FUSED_SELECTED_ROW_BLOCK_SWEEP.md`
- configs tested at warmup/iters `6/50`: `16x8x64`, `16x16x64`, `32x8x64`, `32x16x64`, `64x16x128`
- best median speedup vs per-module Triton selected in the sweep: `32x16x64`, `2.4239x`
- tuned 10/80 rerun:
  - report: `outputs/real_system_packer_2026-06-05/ESMP_FUSED_SELECTED_ROWS_TUNED_32x16x64.md`
  - fused median latency: `0.081686 ms`
  - per-module Triton selected median latency: `0.182602 ms`
  - median fused speedup vs per-module Triton selected: `2.3583x`
  - fused faster than per-module Triton selected: `51/54` cases
  - fused faster than dense full concat: `4/54` cases
  - fused faster than dense selected concat: `2/54` cases
  - guard peak: `3601/8151 MiB = 44.18%`
  - caveat: tuned fused still loses to dense concat median; claim launch-overhead reduction only.

ESMP fused selected-row sidecar generation smoke:

- script: `train_python/measure_esmp_fused_sidecar_generation.py`
- report: `outputs/real_system_packer_2026-06-05/ESMP_FUSED_SIDECAR_GENERATION.md`
- model: `Qwen/Qwen3-0.6B`
- loader: HF FP16 same-loader path
- prompt/generated tokens: `12/16`
- selected rows per module: `64`
- block config: `32x16x64`
- same-loader baseline:
  - TTFT `0.028981 s`
  - elapsed `0.543037 s`
  - throughput `29.4639 tokens/s`
  - guard peak `3582/8151 MiB = 43.95%`
- 1-layer sidecar (`layer 0`):
  - sidecar calls `16`
  - sidecar CUDA sum `4.6900 ms`
  - median sidecar call `0.2606 ms`
  - TTFT `0.041236 s`
  - elapsed `0.603245 s`
  - throughput `26.5232 tokens/s`
  - guard peak `3581/8151 MiB = 43.93%`
- 3-layer sidecar (`layers 0,1,7`):
  - sidecar calls `48`
  - sidecar CUDA sum `11.2085 ms`
  - median sidecar call `0.2218 ms`
  - TTFT `0.067467 s`
  - elapsed `0.801341 s`
  - throughput `19.9665 tokens/s`
  - guard peak `3588/8151 MiB = 44.02%`
- deferred-sync sidecar mode:
  - flag: `--sidecar-sync-mode end`
  - purpose: record CUDA events in the hook but defer event synchronization until the generation run finishes, avoiding per-call CPU/GPU stalls.
- deferred-sync 1-layer sidecar (`layer 0`):
  - sidecar calls `16`
  - sidecar CUDA sum `4.7119 ms`
  - median sidecar call `0.2653 ms`
  - TTFT `0.038116 s`
  - elapsed `0.638191 s`
  - throughput `25.0709 tokens/s`
  - guard peak `3582/8151 MiB = 43.95%`
- deferred-sync 3-layer sidecar (`layers 0,1,7`):
  - sidecar calls `48`
  - sidecar CUDA sum `10.2186 ms`
  - median sidecar call `0.2062 ms`
  - TTFT `0.043812 s`
  - elapsed `0.672049 s`
  - throughput `23.8078 tokens/s`
  - guard peak `3583/8151 MiB = 43.96%`
- generated text matched the same-loader baseline in all measured sidecar runs.
- interpretation: the fused selected-row runtime can execute inside the real HF decode loop, but this sidecar is additive overhead. Per-call synchronization is pessimistic; this was followed by the true fused QKV replacement smoke below.

ESMP fused QKV replacement generation smoke:

- script: `train_python/measure_esmp_fused_qkv_generation.py`
- report: `outputs/real_system_packer_2026-06-05/ESMP_FUSED_QKV_REPLACEMENT_GENERATION.md`
- model: `Qwen/Qwen3-0.6B`
- runtime: Triton grouped INT4/INT8 packed rows
- block config: `32x16x64`
- sync mode: deferred event sync
- 16-token same-script baseline:
  - TTFT `0.028808 s`
  - elapsed `0.774345 s`
  - throughput `20.6626 tokens/s`
  - guard peak `3582/8151 MiB = 43.95%`
- 1-layer 16-token replacement:
  - TTFT `0.033764 s`
  - elapsed `0.488582 s`
  - throughput `32.7479 tokens/s`
  - generated text exactly matched baseline
  - guard peak `3586/8151 MiB = 43.99%`
- 3-layer 16-token replacement:
  - TTFT `0.031471 s`
  - elapsed `0.619774 s`
  - throughput `25.8158 tokens/s`
  - text changed but stayed on topic
  - guard peak `3592/8151 MiB = 44.07%`
- 64-token same-script baseline:
  - TTFT `0.048212 s`
  - elapsed `2.391258 s`
  - throughput `26.7642 tokens/s`
  - guard peak `3591/8151 MiB = 44.06%`
- 1-layer 64-token replacement:
  - TTFT `0.032971 s`
  - elapsed `2.116118 s`
  - throughput `30.2441 tokens/s`
  - compression vs FP32 `6.1682x`
  - wrapper/fused calls `192/64`
  - cache hits/misses `128/64`
  - text prefix matched then diverged
  - guard peak `3587/8151 MiB = 44.01%`
- 3-layer 64-token replacement:
  - TTFT `0.032545 s`
  - elapsed `2.412621 s`
  - throughput `26.5272 tokens/s`
  - compression vs FP32 `7.0778x`
  - wrapper/fused calls `576/192`
  - cache hits/misses `384/192`
  - text changed but stayed on topic
  - guard peak `3593/8151 MiB = 44.08%`
- interpretation: true replacement path works; shallow replacement has useful speed evidence; quality preservation is now the main bottleneck.

ESMP fused QKV prompt-suite audit:

- script: `train_python/eval_fused_qkv_prompt_suite.py`
- reports:
  - `outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_1LAYER.md`
  - `outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_3LAYER.md`
- model: `Qwen/Qwen3-0.6B`
- max new tokens: `32`
- prompts: `6`
- 1-layer suite:
  - exact matches `1/6`
  - mean char edit similarity `0.6051`
  - mean common prefix ratio `0.3470`
  - mean baseline throughput `24.3011 tokens/s`
  - mean fused throughput `20.2237 tokens/s`
  - fused/baseline speed `0.8322x`
  - median baseline TTFT `0.035991 s`
  - median fused TTFT `0.334715 s`
  - guard peak `3571/8151 MiB = 43.81%`
- 3-layer suite:
  - exact matches `0/6`
  - mean char edit similarity `0.5221`
  - mean common prefix ratio `0.1862`
  - mean baseline throughput `25.7576 tokens/s`
  - mean fused throughput `21.8530 tokens/s`
  - fused/baseline speed `0.8484x`
  - median baseline TTFT `0.064350 s`
  - median fused TTFT `0.201079 s`
  - guard peak `3558/8151 MiB = 43.65%`
- interpretation: the one-prompt shallow speed result does not generalize to the six-prompt suite. The next work must improve quality-preserving row/head allocation before broader runtime claims.

Dense-role guard ablation:

- scripts changed:
  - `train_python/measure_esmp_fused_qkv_generation.py`
  - `train_python/eval_fused_qkv_prompt_suite.py`
- new CLI: `--dense-roles`, accepting QKV suffixes such as `q_proj,k_proj`; selected roles stay on original dense `nn.Linear`, while other roles use fused ESMP. This is a diagnostic upper-bound, not the final quantization method.
- 1-layer no guard: exact `1/6`, mean edit `0.6051`, mean prefix `0.3470`, speed `0.8322x`
- 1-layer dense `q_proj`: exact `3/6`, mean edit `0.7448`, mean prefix `0.6708`, speed `0.7425x`, guard peak `43.70%`
- 1-layer dense `k_proj`: exact `1/6`, mean edit `0.5911`, mean prefix `0.3519`, speed `0.9673x`, guard peak `43.58%`
- 1-layer dense `v_proj`: exact `1/6`, mean edit `0.6051`, mean prefix `0.3470`, speed `1.0054x`, guard peak `43.59%`
- 1-layer dense `q_proj,k_proj`: exact `4/6`, mean edit `0.8642`, mean prefix `0.7722`, speed `0.9095x`, guard peak `43.59%`
- 3-layer dense `q_proj,k_proj`: exact `0/6`, mean edit `0.5347`, mean prefix `0.3397`, speed `0.9544x`, guard peak `43.63%`
- interpretation: Q/K are the first precision-protection targets for layer 0; deeper replacement still needs layer-specific search or real higher-precision Q/K ESMP repack.

True Q/K 8-bit repack probe:

- script added: `train_python/repack_qkv_precision_guard.py`
- package variant: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layer0_qk8_guard/pack_summary.json`
- repacked modules:
  - `model.layers.0.self_attn.q_proj=8`, verify rel-L2 `0.009027`, package bytes `2,146,368`
  - `model.layers.0.self_attn.k_proj=8`, verify rel-L2 `0.008710`, package bytes `1,073,216`
- overall package compression vs FP32: `6.8365x`
- 1-layer prompt suite with true Q/K 8-bit ESMP and no dense guard:
  - exact `4/6`
  - mean edit `0.8248`
  - mean prefix `0.7620`
  - speed `0.9695x`
  - guard peak `3559/8151 MiB = 43.66%`
- interpretation: true Q/K 8-bit repack nearly matches dense Q/K guard quality while preserving better speed; extend this to layer-specific Q/K or head-level precision search.

3-layer QK8/QKV8 repack probes:

- QK8 package variant: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers017_qk8_guard/pack_summary.json`, compression `6.7754x`
- QKV8 package variant: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers017_qkv8_guard/pack_summary.json`, compression `6.7553x`
- 3-layer QK8 prompt suite:
  - exact `0/6`
  - mean edit `0.5357`
  - mean prefix `0.3397`
  - speed `0.6724x`
  - guard peak `3552/8151 MiB = 43.58%`
- 3-layer QKV8 prompt suite:
  - exact `3/6`
  - mean edit `0.7692`
  - mean prefix `0.6555`
  - speed `1.0251x`
  - guard peak `3554/8151 MiB = 43.60%`
- interpretation: deeper replacement needs V precision too; the current strongest true ESMP fused-generation result is 3-layer QKV8.

QKV8 layer-subset search:

- layers `0,1`: exact `4/6`, mean edit `0.8469`, mean prefix `0.7710`, speed `0.8711x`, guard peak `43.58%`
- layers `0,7`: exact `4/6`, mean edit `0.8469`, mean prefix `0.7710`, speed `0.8502x`, guard peak `43.59%`
- layers `1,7`: exact `6/6`, mean edit `1.0000`, mean prefix `1.0000`, speed `0.8957x`, guard peak `43.59%`
- layers `1,7,13`: exact `5/6`, mean edit `0.9444`, mean prefix `0.8934`, speed `0.8089x`, guard peak `43.58%`
- layers `1,7,20`: exact `5/6`, mean edit `0.9383`, mean prefix `0.9096`, speed `0.8477x`, guard peak `43.60%`
- layers `1,7,27`: exact `5/6`, mean edit `0.9223`, mean prefix `0.8845`, speed `1.0880x`, guard peak `43.60%`
- layers `1,7,13,20,27`: exact `4/6`, mean edit `0.8970`, mean prefix `0.8709`, speed `0.9641x`, guard peak `43.88%`
- non-layer0 QKV8 package: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers1_7_13_20_27_qkv8_guard/pack_summary.json`, compression `6.7055x`, 15 repacked Q/K/V modules all verified OK.
- interpretation: layer 0 is the dominant drift source; layers 1 and 7 can be replaced together with QKV8 and preserve exact output on this prompt suite. Adding any one of 13/20/27 causes one prompt drift, so next work should target head/row-sensitive protection instead of adding more whole layers.

Row-sensitive layer20 V-projection probes:

- implementation: `train_python/repack_qkv_precision_guard.py --row-overrides`, using the existing C++ packer `--row-bits-file`; Python compile passed for `pack_qwen3_consensus.py` and `repack_qkv_precision_guard.py`.
- ranking tool: `train_python/rank_esmp_row_groups.py`; Python compile passed. Layer20 V group-size 128 ranking produced groups `5,2,6,1,4,7,0,3`.
- base fact: in `qwen3_0p6b_layers017_qkv8_guard`, layer20 Q/K are already 8-bit while V is 4-bit.
- layer20 QK8/V4 control on layers `1,7,20`: exact `1/6`, mean edit `0.5789`, mean prefix `0.3642`, speed `0.8800x`.
- layer20 V front-half rows `0:512` at 8-bit: exact `3/6`, mean edit `0.6960`, mean prefix `0.6013`, speed `0.8310x`, package `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers17_layer20_qkv_halfrow8_guard/pack_summary.json`.
- layer20 V back-half rows `512:1024` at 8-bit: exact `1/6`, mean edit `0.6741`, mean prefix `0.4753`, speed `0.9298x`, package `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers17_layer20_v_backhalf8_guard/pack_summary.json`.
- layer20 V top-4 ranked groups `5,2,6,1`: exact `1/6`, mean edit `0.6365`, mean prefix `0.5181`, speed `0.9619x`, package `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers17_layer20_v_top4ranked8_guard/pack_summary.json`.
- layer20 V top-6 ranked groups `5,2,6,1,4,7`: exact `2/6`, mean edit `0.7614`, mean prefix `0.6431`, speed `0.7936x`, package `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers17_layer20_v_top6ranked8_guard/pack_summary.json`.
- layer20 full V8 control: exact `5/6`, mean edit `0.9383`, mean prefix `0.9096`, speed `0.8477x`.
- prompt-conditioned single 128-row V group sweep exists:
  - report: `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md`
  - group `0` rows `0:128`: exact `2/6`, mean edit `0.6421`, mean prefix `0.4764`, speed `0.8473x`.
  - group `4` rows `512:640`: exact `2/6`, mean edit `0.7169`, mean prefix `0.5374`, speed `0.9750x`.
  - groups `1,2,3,5,6,7` each remain exact `1/6`; full table is in the report.
- prompt-conditioned multi-group V candidate sweep exists:
  - report: `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_combo_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md`
  - tested combos: `0+4`, `0+4+5`, `0+4+5+6`, `0+4+6`, `0+6`, `4+5+6`, `4+6`.
  - best quality combo: `0+4+5+6`, exact `4/6`, mean edit `0.8476`, mean prefix `0.7418`, speed `0.8819x`.
  - best speed-positive combo: `0+4+6`, exact `3/6`, mean edit `0.7617`, mean prefix `0.6263`, speed `1.0772x`.
  - all tested combos in this first combo set still trail full V8: exact `5/6`, mean prefix `0.9096`, speed `0.8477x`.
- prompt-conditioned 5-group expansion sweep exists:
  - report: `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_expansion_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md`
  - tested combos: `0+1+4+5+6`, `0+2+4+5+6`, `0+3+4+5+6`, `0+4+5+6+7`.
  - best exact candidates: `0+1+4+5+6` and `0+4+5+6+7`, both exact `4/6`, mean prefix `0.7418`.
  - highest prefix candidate: `0+2+4+5+6`, exact `3/6`, mean edit `0.8774`, mean prefix `0.8286`, speed `0.9580x`.
- prompt-conditioned 6-group sweep exists:
  - report: `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sixgroup_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md`
  - best candidate: `0+1+2+4+5+6`, exact `5/6`, mean edit `0.9700`, mean prefix `0.9612`, speed `0.9378x`.
- prompt-conditioned 7-group focus exists:
  - report: `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sevengroup_focus/LAYER20_V_PROMPT_GROUP_SWEEP.md`
  - best candidate: `0+1+2+4+5+6+7`, exact `6/6`, mean edit `1.0000`, mean prefix `1.0000`, speed `0.9314x`.
  - repeat run: `0+1+2+4+5+6+7`, exact `6/6`, mean edit `1.0000`, mean prefix `1.0000`, speed `0.9575x`.
- prompt-suite failure analysis exists:
  - report: `outputs/real_system_packer_2026-06-05/LAYER20_V_PROMPT_FAILURE_ANALYSIS.md`
  - summary: full V8 fails prompt 0; `0+1+2+4+5+6` fixes prompt 0 but fails prompt 1; `0+1+2+4+5+6+7` fixes all six prompts in both runs.
- interpretation: naive contiguous row/head protection, local reconstruction-error ranking, and single-group prompt-conditioned selection are not enough. The new stronger result is non-monotonic: leaving layer20 V group `3` (`384:512`) at 4-bit while keeping `0+1+2+4+5+6+7` at 8-bit beats full V8 on the six-prompt suite. Treat this as narrow prompt-conditioned precision-monotonicity failure evidence, not a broad quality guarantee.
- held-out 12-prompt rowguard validation exists:
  - prompt file: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v1.txt`
  - report: `outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/HELDOUT_FAILURE_ANALYSIS.md`
  - compared runs: `baseline_layers17`, `full_v8`, `g0_1_2_4_5_6`, `g0_1_2_4_5_6_7`, `g0_1_2_3_4_5_6`.
  - results: `baseline_layers17` exact `11/12`, edit `0.9398`, prefix `0.9172`, speed `0.8316x`; `full_v8` exact `11/12`, edit `0.9398`, prefix `0.9172`, speed `0.9427x`; `g0_1_2_4_5_6` exact `9/12`, edit `0.8456`, prefix `0.7725`, speed `0.9129x`; `g0_1_2_4_5_6_7` exact `9/12`, edit `0.8456`, prefix `0.7725`, speed `0.7947x`; `g0_1_2_3_4_5_6` exact `11/12`, edit `0.9398`, prefix `0.9172`, speed `0.8546x`.
  - interpretation: the 7-group rowguard fails the first held-out generalization check. The original positive result should be framed as a diagnostic precision-monotonicity failure, not as a deployable policy.
- full 6-group held-out sweep exists:
  - report: `outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sixgroup_heldout_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md`
  - results: `0+1+2+4+5+6` exact `9/12`, `0+1+3+4+5+6` exact `7/12`, `0+1+4+5+6+7` exact `8/12`, `0+2+3+4+5+6` exact `11/12`, `0+2+4+5+6+7` exact `10/12`, `0+3+4+5+6+7` exact `9/12`.
  - interpretation: the search-vs-heldout inversion is now stronger; `0+2+3+4+5+6` is weak on the original split (`3/6`) but strong on held-out (`11/12`).
- prompt-split transfer audit exists:
  - script: `train_python/compare_prompt_transfer.py`
  - report: `outputs/real_system_packer_2026-06-05/LAYER20_V_ROWGUARD_TRANSFER_AUDIT_V2.md`
  - key result: `g0_1_2_4_5_6_7` is `6/6` on the search suite but `9/12` on held-out, transfer gap `0.2500`, risk `high_overfit`.
  - key inversion: `g0_1_2_3_4_5_6` is bad on the search suite (`4/6`) but strong on held-out (`11/12`), and `g0_2_3_4_5_6` is even more inverted (`3/6` search, `11/12` held-out), so group `3` is not globally harmful.
- split-consensus selector exists:
  - script: `train_python/select_split_consensus_rowguard.py`
  - report: `outputs/real_system_packer_2026-06-05/LAYER20_V_SPLIT_CONSENSUS_SELECTOR.md`
  - outputs: `outputs/real_system_packer_2026-06-05/layer20_v_split_consensus_selector.json`, `outputs/real_system_packer_2026-06-05/layer20_v_split_consensus_selector.csv`
  - result: best overall is `baseline_layers17` (`stable_reference`, score `0.8339`); best rowguard is `g0_1_2_4_5_6` (`candidate_needs_third_split`, score `0.6920`); stable rowguard is `none`.
- third prompt split validation exists:
  - prompt file: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v2.txt`
  - output dir: `outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v2/`
  - failure analysis: `outputs/real_system_packer_2026-06-05/LAYER20_V_HELDOUT_V2_FAILURE_ANALYSIS.md`
  - results: `baseline_layers17` `12/12`, `full_v8` `12/12`, `g0_1_2_4_5_6` `9/12`, `g0_1_2_4_5_6_7` `9/12`, `g0_2_3_4_5_6` `11/12`.
- multi-split selector exists:
  - script: `train_python/select_multi_split_rowguard.py`
  - report: `outputs/real_system_packer_2026-06-05/LAYER20_V_MULTI_SPLIT_SELECTOR.md`
  - outputs: `outputs/real_system_packer_2026-06-05/layer20_v_multi_split_selector.json`, `outputs/real_system_packer_2026-06-05/layer20_v_multi_split_selector.csv`
  - result: best overall is `baseline_layers17`; best rowguard is `g0_1_2_4_5_6`; stable rowguard is `none`. The original `g0_1_2_4_5_6_7` remains diagnostic because it is `6/6` on search but `9/12` on both held-out splits.
- QKV/hidden/logit proxy drift and proxy-augmented selector now exist:
  - script: `train_python/measure_qkv_proxy_drift.py`
  - test: `train_python/test_qkv_proxy_drift.py`
  - selector: `train_python/select_proxy_augmented_rowguard.py`
  - drift reports:
    - `outputs/real_system_packer_2026-06-05/QKV_PROXY_DRIFT_BASELINE_LAYERS17.md`
    - `outputs/real_system_packer_2026-06-05/QKV_PROXY_DRIFT_FULL_V8.md`
    - `outputs/real_system_packer_2026-06-05/QKV_PROXY_DRIFT_G0_1_2_4_5_6.md`
    - `outputs/real_system_packer_2026-06-05/QKV_PROXY_DRIFT_G0_1_2_4_5_6_7.md`
    - `outputs/real_system_packer_2026-06-05/QKV_PROXY_DRIFT_G0_2_3_4_5_6.md`
  - selector report: `outputs/real_system_packer_2026-06-05/LAYER20_V_PROXY_AUGMENTED_SELECTOR.md`
  - result: best overall is `baseline_layers17`; best rowguard is `g0_1_2_4_5_6_7`, but only as `candidate_needs_larger_suite`; stable rowguard is `none`.
  - interpretation: rowguards have much larger KV drift than baseline/full-V8, so proxy drift is now an early filter before larger prompt or task audits.
- V3 task-style prompt audit now exists:
  - prompt file: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v3_taskstyle.txt`
  - report: `outputs/real_system_packer_2026-06-05/LAYER20_V_V3_TASKSTYLE_AUDIT.md`
  - candidates: `baseline_layers17`, `full_v8`, `g0_1_2_4_5_6_7`
  - result: `baseline_layers17` `19/24`, `full_v8` `19/24`, `g0_1_2_4_5_6_7` `16/24`
  - guard peak: `3597/8151 MiB = 44.13%`
  - interpretation: rowguard remains weaker on a broader task-style prompt suite, consistent with the proxy warning.
- V3 rule-scored task wrapper now exists:
  - script: `train_python/score_prompt_suite.py`
  - test: `train_python/test_score_prompt_suite.py`
  - report: `outputs/real_system_packer_2026-06-05/V3_RULE_SCORED_TASK_AUDIT.md`
  - results: no shallow rule regressions; `baseline_layers17` and `g0_1_2_4_5_6_7` fused outputs pass `13/24` rules, `full_v8` passes `12/24`.
  - caveat: baseline rule pass rate is only `12/24`, so this is diagnostic, not a strong task benchmark.
- Chat-template prompt-suite support and v3 chat audit now exist:
  - changed scripts: `train_python/measure_esmp_generation_latency.py`, `train_python/eval_fused_qkv_prompt_suite.py`
  - test: `train_python/test_generation_prompt_format.py`
  - new CLI: `--chat-template`, default off
  - fallback: Qwen/ChatML rendering when `tokenizer.apply_chat_template` fails because local `jinja2` is too old
  - report: `outputs/real_system_packer_2026-06-05/V3_CHAT_TEMPLATE_AUDIT.md`
  - results: `baseline_layers17` `24/24`, `full_v8` `23/24`, `g0_1_2_4_5_6_7` `22/24`
  - scored chat results: all three candidates `15/24`, zero shallow regressions
  - guard peak: `3599/8151 MiB = 44.15%`
  - interpretation: future instruct-model prompt audits should use `--chat-template`; old raw-prompt audits are completion-style stress tests.
- V4 expected-rule prompt audit now exists:
  - expected suite: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v4_expected.jsonl`
  - report: `outputs/real_system_packer_2026-06-05/V4_EXPECTED_RULE_SCORED_AUDIT.md`
  - scorer CLI: `train_python/score_prompt_suite.py --expected-jsonl ...`
  - results on existing chat-template v3 outputs: all three candidates baseline `15/24`, fused `15/24`, regressions `0`
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

## Current Git State

There are many uncommitted changes. This is intentional.

Modified:

- `.gitignore`
- `README.md`
- `inference_cpp/CMakeLists.txt`
- `inference_cpp/include/eigenskill/quant_kernels.hpp`
- `inference_cpp/src/quant_kernel_bench.cpp`
- `inference_cpp/src/quant_kernel_verify.cpp`
- `inference_cpp/src/quant_kernels.cpp`
- `inference_cpp/src/quant_policy_bypass.cpp`
- `outputs/paper_delivery_2026-06-04/EigenSkill-Q_CCF-A_Draft_v2_Loss_Sensitive.md`
- `train_python/parse_quant_kernel_bench.py`
- `train_python/run_with_gpu_guard.py`
- `train_python/train_lora.py`

Added/untracked:

- `CODEX_RESUME.md`
- `inference_cpp/src/mixed_precision_packer.cpp`
- `mobile/redmi_k80_pro/neon_mixed_decode.cpp`
- `outputs/real_system_packer_2026-06-05/`
- `train_python/allocator.py`
- `train_python/eval_fused_qkv_prompt_suite.py`
- `train_python/eval_esmp_module_reconstruction.py`
- `train_python/benchmark_esmp_linear_runtimes.py`
- `train_python/benchmark_esmp_selected_rows.py`
- `train_python/measure_esmp_fused_sidecar_generation.py`
- `train_python/measure_esmp_fused_qkv_generation.py`
- `train_python/measure_esmp_generation_latency.py`
- `train_python/measure_generation_latency.py`
- `train_python/pack_qwen3_consensus.py`
- `train_python/repack_qkv_precision_guard.py`
- `train_python/triton_mixed_gemm.py`

Deleted with intent from earlier cleanup:

- leaked `data_eval/eigenskill_v2/*`
- speculative Eigen-Swarm docs
- old v2 outputs/logs/scripts

## Next Commands

Run these after Codex update if Rui says "继续".

GPU rule:

- Rui's current active goal cap is 90% VRAM. Use `run_with_gpu_guard.py --max-memory-ratio 0.90` by default unless he tightens the cap again.
- The prior Qwen3-1.7B baseline peaked at 7216/8151 MiB = 88.53%; it fits under 90% but remains close enough that smaller shapes are safer for long experiments.

First sanity check:

```powershell
cd C:\Users\18042\Documents\Codex\2026-06-01\chatgpt-context-request-algorithm-system-co\github_publish\eigenskill-research-pack
git status --short
```

The 216-config Triton tuning, 42-module ESMP runtime sweep, 42-module activation reconstruction, 196-module activation reconstruction, 3-module ESMP-swapped generation smoke, 3-module ESMP Linear runtime-shape benchmark, 3-module ESMP selected-row benchmark, 6-layer fused QKV selected-row benchmark, fused block sweep, fused selected-row sidecar generation smoke, fused QKV replacement generation smoke, fused QKV prompt-suite audit, dense-role guard ablation, true layer-0 Q/K 8-bit repack probe, true 3-layer QK8/QKV8 repack probes, QKV8 layer-subset search, non-layer0 QKV8 expansion, layer20 row-sensitive V probes, layer20 V row/group ranking, layer20 V prompt-conditioned single-group sweep, layer20 V prompt-conditioned multi-group candidate sweep, layer20 V 5-group expansion sweep, layer20 V 6-group sweep, layer20 V 7-group focus, layer20 V prompt failure analysis, held-out 12-prompt rowguard validation, full 6-group held-out sweep, prompt-split transfer audit V2, split-consensus selector, third prompt split validation, multi-split selector, QKV/hidden/logit proxy drift, proxy-augmented selector, v3 task-style prompt audit, v3 rule-scored task wrapper, v3 chat-template audit, v4 expected-rule prompt audit, and chat task benchmark v1 are complete. Do not rerun them unless changing the kernel, runtime, module selection, prompt set, or ESMP package.

Next strongest step: keep `1,7` QKV8 as the conservative baseline and use the zero-download import path on cached official-format MMLU/GSM8K slices, expand IFEval checker coverage beyond `keywords:existence`, or improve strict structured-output prompting for rows where dense baseline also fails. Use the proxy-augmented selector as a candidate filter, not final proof. Treat layer `0` separately later with dense fallback or FP16/INT8 head protection. Keep the speed claim narrow because prompt-suite speed is noisy and quality preservation is not yet broad.

Run Qwen3 TTFT/tokens/s if VRAM still under 90%:

```powershell
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack && python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --out outputs/real_system_packer_2026-06-05/qwen3_ttft_gpu_guard.json -- python3 train_python/measure_generation_latency.py --model Qwen/Qwen3-0.6B --device cuda --dtype float16 --max-new-tokens 64 --out outputs/real_system_packer_2026-06-05/qwen3_0p6b_ttft_tokens_memory.json"
```

Try real Qwen3 ESMP packing for a small module subset:

```powershell
wsl.exe bash -lc "cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack && python3 train_python/pack_qwen3_consensus.py --model Qwen/Qwen3-0.6B --allocation outputs/qwen3_0p6b_cpp_allocation_planner_4p5_summary.json --method loss_sensitive_budget --packer build/cpp-wsl/mixed_precision_packer --out-dir outputs/real_system_packer_2026-06-05/qwen3_esmp --device cpu --dtype float16 --limit-modules 3 --verify"
```

If the allocation parser fails, inspect the structure of `outputs/qwen3_0p6b_cpp_allocation_planner_4p5_summary.json` and update `allocation_bits()` in `train_python/pack_qwen3_consensus.py`; do not abandon the packer path.

## Caveats To Preserve

- Do not claim real Tensor Core acceleration until the Triton benchmark has actually run and the output JSON exists.
- Do not claim Redmi K80 Pro physical TTFT/tokens/s until adb/phone/NDK measurement has actually run.
- Do not claim full LLM runtime integration yet. Current real artifacts are packer, binary package format, CPU kernels, Triton kernel benchmark entry, TTFT measurement entry, and NEON decode kernel source.
- Keep `.esmp` and raw model artifacts local.
- Before any future commit: run secret scan and staged-weight scan.

## CodeGraph Repair Note

Rui asked to fix codegraph before continuing experiments.

Current state after repair:

- Latest `codegraph sync .` succeeded.
- Latest `codegraph status .` reports the index is up to date:
  - files: `111`
  - nodes: `2444`
  - edges: `4499`
  - C++ files: `27`
- `codegraph query allocate_bits_lagrangian` finds:
  - `github_publish/eigenskill-research-pack/train_python/allocator.py:197`
- `codegraph query mixed_precision_runtime` finds:
  - `github_publish/eigenskill-research-pack/inference_cpp/src/mixed_precision_runtime_bench.cpp:1`
- `C:\Users\18042\.codex\config.toml` now contains:

```toml
[mcp_servers.codegraph]
command = 'C:\Users\18042\AppData\Roaming\npm\codegraph.cmd'
args = ["serve", "--mcp", "--no-watch"]
```

- `C:\Users\18042\.hermes\config.yaml` now points CodeGraph to:

```yaml
codegraph:
  command: C:/Users/18042/AppData/Roaming/npm/codegraph.cmd
  args:
    - serve
    - --mcp
    - --no-watch
```

Important limitation:

- In this already-running Codex Desktop session, direct `mcp__codegraph.*` tools may still be absent from the tool table.
- This appears to be a hot-reload/tool-table issue, not an index issue. Use `codegraph` CLI as the fallback in this session. After restarting/opening a new Codex session, the registered MCP server should load from the absolute command path with `--no-watch`.
- This installed CodeGraph CLI uses `query`, not `search`; `codegraph search ...` fails with `unknown command 'search'`.
- Old watch-enabled CodeGraph MCP processes launched as plain `serve --mcp` were stopped on 2026-06-06 because watcher logs showed EACCES errors under `.venv-baselines`. Keep `--no-watch`.

## Understanding Anything Plugin Note

Rui asked to add an Understanding Anything plugin while fixing CodeGraph.

Current state:

- Existing skill source:
  - `C:\Users\18042\.codex\skills\understanding-anything\SKILL.md`
- Plugin source:
  - `C:\Users\18042\plugins\understanding-anything`
- Marketplace:
  - `C:\Users\18042\.agents\plugins\marketplace.json`
- Installed cache:
  - `C:\Users\18042\.codex\plugins\cache\personal\understanding-anything\0.1.0`
- Config entry:
  - `[plugins."understanding-anything@personal"]`
  - `enabled = true`
- `codex plugin list` now reports:
  - `understanding-anything@personal installed, enabled 0.1.0`
- Hermes/WSL mirror now exists:
  - `/home/rui/.hermes/skills/imported/understanding-anything/SKILL.md`

Verification:

- `python C:\Users\18042\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\18042\plugins\understanding-anything`
  - passed.
- `codex plugin add understanding-anything@personal`
  - reported success and copied the plugin into cache.
- Latest `codex plugin list` still reports:
  - `understanding-anything@personal installed, enabled 0.1.0`

Previous CLI quirk:

- Earlier `codex plugin list` reported `understanding-anything@personal` as `not installed` even after `codex plugin add` succeeded. This is now resolved in the current CLI listing.

## C Drive / WSL Disk Note

Rui asked to keep C drive pressure down.

Current state after cleanup attempts and the latest disk-aware guard update on 2026-06-06:

- C drive free: latest readback about `19.19 GB` after this toolchain recheck. It was about `19.5 GB` earlier in the same recheck.
- D drive free: about `57.30 GB`.
- `uv cache clean` removed about `169.7 MiB` from C.
- `python -m pip cache purge` removed about `6.46 GB`, but pip cache is at `d:\caches\pip`, so it mostly helped D rather than C.
- `npm cache clean --force` completed.
- WSL `npm cache clean --force` completed after the selected-row benchmark.
- Repo-local `train_python\__pycache__` from the latest Python compile/runs was removed after verifying the resolved path stayed inside the repo; total reclaimed was small, under `1 MiB`.
- Latest post-selector repo-local cache cleanup removed about `0.139 MiB`; WSL apt archive cache is about `72 KiB`.
- Latest post-multi-selector repo-local cache cleanup removed about `0.131 MiB`; safe caches are no longer the dominant C-drive pressure.
- Latest post-proxy-selector repo-local cache cleanup removed about `0.126 MiB`; C: stayed around `19.70 GB` because active logs/WSL VHDX growth dominate tiny repo-cache savings.
- Latest post-v3-audit repo-local cache cleanup removed about `0.106 MiB`; latest C: reading is about `19.83 GB` free.
- Latest post-compile repo-local `__pycache__` / `.pytest_cache` / `.ruff_cache` cleanup removed about `0.136 MiB`.
- Latest post-combo-sweep repo-local cache cleanup removed about `0.124 MiB`.
- Latest post-expansion-sweep repo-local cache cleanup removed about `0.115 MiB`.
- Latest disk-aware guard cleanup:
  - output: `outputs/real_system_packer_2026-06-05/post_pruned_repo_cache_cleanup_guard.json`
  - removed repo-local `train_python/__pycache__`, about `0.160 MiB`
  - guard GPU peak: `2239/8151 MiB = 27.47%`
  - end GPU state: `2257/8151 MiB = 27.69%`
  - end disk state from guard JSON: C: about `19.65 GB` free; latest Windows readback: about `19.68 GB` free
- Latest post-v4 expected-rule cleanup:
  - output: `outputs/real_system_packer_2026-06-05/post_v4_expected_repo_cache_cleanup_guard.json`
  - removed repo-local `train_python/__pycache__`, about `0.152 MiB`
  - guard GPU peak: `2219/8151 MiB = 27.22%`
  - end GPU state: `2233/8151 MiB = 27.40%`
  - end disk state from guard JSON: C: about `19.52 GB` free; latest Windows readback after CodeGraph sync was about `19.49 GB`
- Latest CodeGraph/disk recheck:
  - output: `outputs/real_system_packer_2026-06-05/codegraph_disk_cleanup_dry_run_guard.json`
  - repo-local cleanup dry-run found `0` targets and `0` bytes reclaimable
  - guard GPU peak: `2226/8151 MiB = 27.31%`
  - Windows readback around this check: C: about `19.19 GB` free at final readback
  - targeted visible pressure points: `.ollama` about `8.56 GB`, `.codex` about `8.03 GB`, active workspace root about `5.33 GB`, user temp about `0.96 GB`, `.cache` about `0.89 GB`

## 2026-06-06 Deterministic Task Benchmark Update

Rui wanted stronger, less toy-like task evidence. The latest completed method step expanded deterministic scoring and reran small guarded Qwen3-0.6B task checks without downloading new models or datasets.

Changed files:

- `train_python/eval_chat_task_benchmark.py`
- `train_python/test_eval_chat_task_benchmark.py`
- `train_python/measure_esmp_generation_latency.py`
- `train_python/test_qkv_proxy_drift.py`
- `data_eval/ifeval_deterministic_v2.jsonl`
- `outputs/real_system_packer_2026-06-05/IFEVAL_V2_DETERMINISTIC_AUDIT.md`
- `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_AUDIT.md`
- `outputs/real_system_packer_2026-06-05/REAL_SYSTEM_RESULTS_2026_06_06.md`
- `CODEX_RESUME.md`

Scorer changes:

- Strip visible `<think>...</think>` before deterministic matching.
- Fix undercounted Qwen MCQ answers like `<think>...</think>\n\nB. peak GPU memory`.
- Add IFEval deterministic subset import for:
  - `keywords:existence`
  - `keywords:forbidden_words`
  - `detectable_format:json_format`
  - `length_constraints:number_sentences`
  - `length_constraints:number_words`
  - multi-instruction `all_of`
- Add strict task types: `contains_none`, `json_valid`, `sentence_count`, `word_count`, `all_of`.

Verification:

- Windows: `python -m unittest test_eval_chat_task_benchmark test_score_prompt_suite test_run_with_gpu_guard_disk test_generation_prompt_format test_qkv_proxy_drift`
  - passed: `Ran 21 tests ... OK (skipped=3)` because Windows Python lacks torch
- Windows py_compile with temp pycache:
  - passed for `eval_chat_task_benchmark.py`, `test_eval_chat_task_benchmark.py`, `measure_esmp_generation_latency.py`, `test_generation_prompt_format.py`, `test_qkv_proxy_drift.py`
- WSL CUDA:
  - `python3 -m unittest test_qkv_proxy_drift test_eval_chat_task_benchmark`
  - passed: `Ran 12 tests ... OK`
- Projection-role selector:
  - `python -m unittest test_select_projection_role_policy` passed: `Ran 3 tests ... OK`
  - `python -m py_compile train_python\select_projection_role_policy.py train_python\test_select_projection_role_policy.py` passed
  - `python -m unittest test_select_projection_role_policy test_eval_chat_task_benchmark` passed: `Ran 12 tests ... OK`

New guarded benchmark results:

- V1 no-think layers `1,7` rerun under updated scorer:
  - output: `outputs/real_system_packer_2026-06-05/chat_task_benchmark_v1_qwen3_0p6b_no_think_layers17_rescore.json`
  - report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS17_RESCORE.md`
  - baseline `5/12`, fused `5/12`
  - fused/base tok/s `0.9157x`
  - guard peak `3592/8151 MiB = 44.07%`
- V1 no-think layers `1,7` V-only packed role ablation:
  - 32-token output: `outputs/real_system_packer_2026-06-05/chat_task_benchmark_v1_qwen3_0p6b_no_think_layers17_vonly_32tok.json`
  - 32-token report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS17_VONLY_32TOK.md`
  - 32-token result: baseline `5/12`, fused `5/12`, fused/base tok/s `1.0142x`, guard peak `3763/8151 MiB = 46.17%`
  - 64-token output: `outputs/real_system_packer_2026-06-05/chat_task_benchmark_v1_qwen3_0p6b_no_think_layers17_vonly.json`
  - 64-token report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS17_VONLY.md`
  - 64-token result: baseline `7/12`, fused `7/12`, fused/base tok/s `0.9713x`, guard peak `3766/8151 MiB = 46.20%`
- V1 no-think layers `1,7,20` V-only packed expansion:
  - output: `outputs/real_system_packer_2026-06-05/chat_task_benchmark_v1_qwen3_0p6b_no_think_layers1720_vonly_32tok.json`
  - report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS1720_VONLY_32TOK.md`
  - result: baseline `5/12`, fused `5/12`, fused/base tok/s `0.6903x`, guard peak `3763/8151 MiB = 46.17%`
- IFEval-style deterministic v2:
  - task file: `data_eval/ifeval_deterministic_v2.jsonl`
  - output: `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers17.json`
  - report: `outputs/real_system_packer_2026-06-05/IFEVAL_V2_QWEN3_0P6B_NO_THINK_LAYERS17.md`
  - audit: `outputs/real_system_packer_2026-06-05/IFEVAL_V2_DETERMINISTIC_AUDIT.md`
  - baseline `2/8`, fused `1/8`
  - fused/base tok/s `1.0334x`
  - guard peak `3595/8151 MiB = 44.11%`
- IFEval-style deterministic v2 projection-role ablation on layers `1,7`:
  - V-only packed, Q/K dense:
    - output: `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers17_vonly.json`
    - report: `outputs/real_system_packer_2026-06-05/IFEVAL_V2_QWEN3_0P6B_NO_THINK_LAYERS17_VONLY.md`
    - baseline `2/8`, fused `2/8`, fused/base tok/s `1.0872x`, guard peak `3761/8151 MiB = 46.14%`
  - Q-only packed, K/V dense:
    - output: `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers17_qonly.json`
    - report: `outputs/real_system_packer_2026-06-05/IFEVAL_V2_QWEN3_0P6B_NO_THINK_LAYERS17_QONLY.md`
    - baseline `2/8`, fused `2/8`, fused/base tok/s `0.9980x`, guard peak `3753/8151 MiB = 46.04%`
  - K-only packed, Q/V dense:
    - output: `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers17_konly.json`
    - report: `outputs/real_system_packer_2026-06-05/IFEVAL_V2_QWEN3_0P6B_NO_THINK_LAYERS17_KONLY.md`
    - baseline `2/8`, fused `2/8`, fused/base tok/s `0.9366x`, guard peak `3755/8151 MiB = 46.07%`
  - V-only packed layers `1,7,20`, Q/K dense:
    - output: `outputs/real_system_packer_2026-06-05/ifeval_v2_qwen3_0p6b_no_think_layers1720_vonly.json`
    - report: `outputs/real_system_packer_2026-06-05/IFEVAL_V2_QWEN3_0P6B_NO_THINK_LAYERS1720_VONLY.md`
    - baseline `2/8`, fused `1/8`, fused/base tok/s `0.8516x`, guard peak `3758/8151 MiB = 46.10%`
- Projection-role selector:
  - script: `train_python/select_projection_role_policy.py`
  - test: `train_python/test_select_projection_role_policy.py`
  - cross-slice report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR.md`
  - cross-slice JSON/CSV:
    - `outputs/real_system_packer_2026-06-05/projection_role_policy_selector.json`
    - `outputs/real_system_packer_2026-06-05/projection_role_policy_selector.csv`
  - IFEval-only report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_IFEVAL_ONLY.md`
  - IFEval-only JSON/CSV:
    - `outputs/real_system_packer_2026-06-05/projection_role_policy_selector_ifeval_only.json`
    - `outputs/real_system_packer_2026-06-05/projection_role_policy_selector_ifeval_only.csv`
  - cross-slice result: `vonly_layers17` is selected as `conservative_candidate`, score `0.9099`, min speed `1.0142x`, max TTFT ratio `0.9302`; full-QKV and layer-20 V-only expansion are rejected for IFEval v2 quality regression.
  - IFEval-only result: V-only ranks first, Q-only second, K-only third; full-QKV and layer-20 expansion are rejected.
- Chat task stress v2:
  - generator: `train_python/generate_deterministic_task_stress.py`
  - test: `train_python/test_generate_deterministic_task_stress.py`
  - task file: `data_eval/chat_task_stress_v2.jsonl`
  - audit: `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V2_AUDIT.md`
  - selector report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_IFEVAL_STRESS.md`
  - verification: `python -m unittest test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed (`15` tests); py_compile passed for the new generator/test and affected evaluator/selector.
  - stress V-only layers `1,7`: baseline `22/42`, fused `21/42`, fused/base tok/s `0.9924x`, guard peak `3759/8151 MiB = 46.12%`.
  - stress Q-only layers `1,7`: baseline `22/42`, fused `22/42`, fused/base tok/s `1.0080x`, guard peak `3774/8151 MiB = 46.30%`.
  - stress K-only layers `1,7`: baseline `22/42`, fused `21/42`, fused/base tok/s `1.0028x`, guard peak `4266/8151 MiB = 52.34%`.
  - IFEval+Stress selector now selects `qonly_layers17` as `quality_preserving_speed_neutral`, score `0.9006`, no pass-count regression on either split, min speed `0.9980x`, max TTFT ratio `0.9761`. This supersedes the smaller-slice V-only-first interpretation.
  - Full-QKV layers `1,7` stress run exceeded a 20-minute command timeout and was stopped. No full-QKV stress result should be cited.
  - After stopping full-QKV, no WSL eval/guard process remained. GPU stayed high because Windows still had `NeedForSpeedHeat` active; do not kill user graphics/game processes without explicit permission.
  - Latest continuation check still showed `NeedForSpeedHeat` active and GPU at about `96% / 5008 MiB / 86C`; hold further GPU runs until the card drops below the chosen start gate.

Interpretation:

- The updated V1 scorer corrects a prior undercount; old `3/12 -> 3/12` should be treated as superseded by `5/12 -> 5/12`.
- The 32-token V1 V-only result is directly comparable to the updated 32-token full-QKV run: it preserves `5/12 -> 5/12` and is faster in this short run, while full-QKV preserves accuracy but is slower.
- The stricter IFEval-style v2 result is negative quality evidence for the fused layers `1,7` candidate. Do not claim quality preservation on structured instruction following.
- The v2 token-rate bump is not a deployment win because fused accuracy regresses.
- Projection-role ablation narrows the failure: full QKV packed replacement regresses, while single-role packed replacement does not regress this small deterministic slice. V-only is the next conservative candidate to expand, but it is still diagnostic evidence, not a deployment claim.
- The first V-only expansion to layer `20` is negative for structured tasks: V1 keeps pass count but slows badly, and IFEval v2 regresses to `1/8`. Keep current conservative V-only boundary at layers `1,7`; treat layer `20` as needing row/role-specific protection.
- The selector converts the hand-picked role-ablation table into a reproducible policy gate: any split-level pass-count regression is rejected before speed is considered. This is useful for the paper's calibration/role-stability story, but the slices are still small.
- The larger stress-v2 slice falsifies the previous V-only preference and shifts the next role-policy candidate to Q-only layers `1,7`. This is a stronger story than hard-coding one role, but still not a deployment claim.
- New guard command pattern for future experiments:
  - `python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.45 --min-disk-free-gb 15 --timeout-sec <seconds> --cleanup-repo-caches --cleanup-root . --out <guard.json> -- <command>`
  - `--timeout-sec` is now guard-native; it records `killed_by_timeout` / `timeout_seconds` and exits `91`, avoiding orphan child processes from outer shell timeouts.
  - `--max-start-memory-ratio` is the start-line idle gate; use it when Windows graphics/game/LM Studio/Ollama processes may already hold several GiB of VRAM.
- Latest WSL cache check: apt archives about `72 KiB`, Triton cache about `18 MiB`, NVIDIA ComputeCache about `4 KiB`.
- WSL internal root filesystem reports only about `40 GB` used, but the Windows VHD file is still about `62.82 GB`.
- VHD path:
  - `C:\Users\18042\AppData\Local\wsl\{437898f7-8f9f-4634-98cd-99603dd9b5ec}\ext4.vhdx`
- `diskpart compact vdisk` was attempted from Codex but failed because Windows requires elevated/admin permissions.
- `wsl.exe --manage Ubuntu-22.04 --set-sparse true` was attempted and rejected by WSL, which requested `--allow-unsafe`; do not use the unsafe flag without Rui's explicit approval.
- WSL was used again for the latest benchmark. Do not shut it down for VHD compaction while experiments are running.
- The latest IFEval v2 and V1 V-only ablations used `--min-disk-free-gb 15` and `--cleanup-repo-caches`; each cleanup only removed `train_python/__pycache__` at about `0.107 MiB`. Repo-local caches are not the meaningful C-drive pressure source.
- Post-selector repo-local cleanup:
  - output: `outputs/real_system_packer_2026-06-05/post_projection_selector_repo_cache_cleanup_guard.json`
  - guard peak `2397/8151 MiB = 29.41%`
  - removed about `0.058 MiB` from `train_python/__pycache__`
  - latest Windows C: readback about `19.19 GB` free
- CodeGraph status after selector sync: `113 files / 2,485 nodes / 4,583 edges`, index up to date.

Latest storage scan:

- C-drive audit summary: `outputs/real_system_packer_2026-06-05/C_DRIVE_STORAGE_AUDIT_2026_06_06.md`
- `C:\Users\18042\AppData\Local\wsl`: about `62.82 GB`.
- `C:\Users\18042\AppData\Local\Docker`: about `8.96 GB`.
- `C:\Users\18042\.codex\tools`: about `4.82 GB`.
- `C:\Users\18042\.codex\logs_2.sqlite`: about `2.05 GB`.
- `C:\Users\18042\.ollama`: about `8.56 GB`; do not delete without Rui's explicit choice.
- `C:\Users\18042\.lmstudio`: about `3.38 GB`; do not delete without Rui's explicit choice.
- `C:\Users\18042\.cache`: about `0.89 GB`.
- `C:\Users\18042\AppData\Local\Temp`: about `0.61 GB`.
- workspace `models`: about `4.68 GB`; keep unless Rui explicitly chooses to archive/delete old SmolLM variants.
- WSL `/home/rui/.cache/huggingface`: about `17 GB`; keep for Qwen/OLMo experiments unless urgent.
- WSL `/var/cache/apt/archives`: now about `72 KiB` after prior cleanup.
- WSL `/home/rui/.npm/_cacache`: previously about `398 MB`; current command produced no meaningful cache entry.
- WSL `/home/rui/.triton/cache`: now about `18 MB`.

Main C-drive pressure points from the storage scan:

- WSL VHDX: about `62.82 GB`.
- Steam under `C:\Program Files (x86)\Steam`: about `51.2 GB`.
- Lenovo / Epic Games / Visual Studio / Docker are also large installed assets.
- `.codex` contains large active logs/backups; do not delete active logs while Codex Desktop is running.

WSL HuggingFace cache inside the VHD:

- `Qwen/Qwen3-0.6B`: about `1.5 GB`, keep.
- `Qwen/Qwen3-1.7B`: about `3.8 GB`, keep for current experiments.
- `allenai/OLMo-2-0425-1B-Instruct`: about `2.8 GB`, keep unless space becomes urgent.
- `ibm-granite/granite-3.3-2b-instruct`: about `3.5 GB`, optional cleanup candidate.
- `allenai/c4`: about `2.1 GB`, keep if continuing calibration/PPL experiments.

If reclaiming C drive space becomes urgent, run the VHD compaction from an elevated PowerShell:

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

## 2026-06-06 Continuation: V1 Q/K Ablations, Three-Split Selector, C-Drive Cleanup

Rui asked to continue after CodeGraph repair and to keep C-drive pressure down.

Tooling and storage:

- Direct `mcp__codegraph.*` tools are still absent in this already-running Codex Desktop tool table, but CodeGraph CLI is healthy.
- Latest CodeGraph status after sync: `115 files / 2,525 nodes / 4,645 edges`, index up to date.
- `understanding-anything` skill was read and remains available at `C:\Users\18042\.codex\skills\understanding-anything\SKILL.md`.
- Low-risk Windows cleanup removed about `1.316 GB`:
  - `C:\Users\18042\AppData\Local\Temp\d54byrr5`: about `1265.66 MB`
  - `C:\Users\18042\AppData\Local\uv\cache`: about `121.86 MB`
  - repo-local `train_python\__pycache__`: about `0.20 MB`
- C: moved from about `18.99 GB` free to `20.31 GB` free before the next evals; latest readback after eval logs and CodeGraph sync is about `20.09 GB` free.
- WSL `/home/rui/.cache/huggingface` is about `17 GB`; it was kept. Do not delete or move HuggingFace/Ollama/LM Studio/model caches without Rui explicitly choosing that tradeoff.
- D: has enough room to host a migrated HuggingFace cache, but moving WSL/HF cache plus VHD compaction is a structural migration and was not performed.

New guarded V1 role ablations:

- Q-only layers `1,7` on V1 32-token:
  - output: `outputs/real_system_packer_2026-06-05/chat_task_benchmark_v1_qwen3_0p6b_no_think_layers17_qonly_32tok.json`
  - report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS17_QONLY_32TOK.md`
  - result: baseline `5/12`, fused `5/12`, fused/base tok/s `1.1926x`, guard peak `4033/8151 MiB = 49.48%`
- K-only layers `1,7` on V1 32-token:
  - output: `outputs/real_system_packer_2026-06-05/chat_task_benchmark_v1_qwen3_0p6b_no_think_layers17_konly_32tok.json`
  - report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_BENCHMARK_V1_QWEN3_0P6B_NO_THINK_LAYERS17_KONLY_32TOK.md`
  - result: baseline `5/12`, fused `5/12`, fused/base tok/s `0.9410x`, guard peak `3848/8151 MiB = 47.21%`

Three-split selector:

- report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_V1_IFEVAL_STRESS.md`
- JSON/CSV:
  - `outputs/real_system_packer_2026-06-05/projection_role_policy_selector_v1_ifeval_stress.json`
  - `outputs/real_system_packer_2026-06-05/projection_role_policy_selector_v1_ifeval_stress.csv`
- result: `qonly_layers17` is selected as `quality_preserving_speed_neutral`, score `0.9118`, no pass-count regression on V1 32-token, IFEval v2, or stress v2, min speed `0.9980x`, max TTFT ratio `0.9761`.
- V-only and K-only are rejected because both lose one pass on stress v2.
- Full-QKV is not included because the stress-v2 run timed out; do not cite a full-QKV stress result.

Verification:

- `python3 -m unittest test_run_with_gpu_guard_disk test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed: `Ran 19 tests ... OK`.
- `codegraph sync .` completed and `codegraph status .` reports up to date.

Next concrete method step:

1. Treat `qonly_layers17` as the current narrow policy candidate.
2. Validate it on a larger deterministic task slice or cached official-format MMLU/GSM8K/IFEval slices.
3. Keep using:

```bash
python3 train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.90 \
  --max-start-memory-ratio 0.45 \
  --min-disk-free-gb 15 \
  --timeout-sec <seconds> \
  --cleanup-repo-caches \
  --cleanup-root . \
  --out <guard.json> \
  -- <command>
```

## 2026-06-06 Continuation: Stress-v3 84-Row Falsification

After the three-split selector picked `qonly_layers17`, the next run expanded the deterministic native stress slice from 42 to 84 rows and reran all single-role policies on layers `1,7`.

Changed files:

- `train_python/generate_deterministic_task_stress.py`
- `train_python/test_generate_deterministic_task_stress.py`
- `data_eval/chat_task_stress_v3_84.jsonl`

TDD/verification:

- RED observed first: `generate_tasks(84)` raised `ValueError: count must be <= 42`.
- After implementation:
  - `python3 -m unittest test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed: `Ran 16 tests ... OK`.
  - `python3 -m unittest test_run_with_gpu_guard_disk test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed: `Ran 20 tests ... OK`.
  - `python3 -m py_compile train_python/generate_deterministic_task_stress.py train_python/test_generate_deterministic_task_stress.py train_python/eval_chat_task_benchmark.py train_python/select_projection_role_policy.py train_python/run_with_gpu_guard.py` passed.

Stress-v3 outputs:

- Q-only:
  - `outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_qwen3_0p6b_no_think_layers17_qonly_32tok.json`
  - baseline `46/84`, fused `45/84`, fused/base tok/s `0.9272x`, guard peak `4397/8151 MiB = 53.94%`
- V-only:
  - `outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_qwen3_0p6b_no_think_layers17_vonly_32tok.json`
  - baseline `46/84`, fused `43/84`, fused/base tok/s `0.9653x`, guard peak `4450/8151 MiB = 54.59%`
- K-only:
  - `outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_qwen3_0p6b_no_think_layers17_konly_32tok.json`
  - baseline `46/84`, fused `45/84`, fused/base tok/s `0.9746x`, guard peak `4458/8151 MiB = 54.69%`

Four-split selector:

- report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_V1_IFEVAL_STRESS_V3.md`
- JSON/CSV:
  - `outputs/real_system_packer_2026-06-05/projection_role_policy_selector_v1_ifeval_stress_v3.json`
  - `outputs/real_system_packer_2026-06-05/projection_role_policy_selector_v1_ifeval_stress_v3.csv`
- result: no quality-preserving single-role policy. Q-only loses one pass on stress-v3, V-only loses three, K-only loses one plus the stress-v2 loss.
- Important paper interpretation: Q-only was a useful three-split candidate but is falsified by the larger 84-row stress slice. Do not present Q-only as deployable. Present this as calibration/task-split instability and use it to motivate stricter role/row protection.

Stress-v3 regression diagnosis:

- tool: `train_python/analyze_chat_task_regressions.py`
- test: `train_python/test_analyze_chat_task_regressions.py`
- report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_REGRESSION_ANALYSIS.md`
- JSON: `outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_regression_analysis.json`
- summary:
  - Q-only: `46 -> 45 / 84`, one MCQ regression (`stress_mcq_extra_000`), zero fixes.
  - V-only: `46 -> 43 / 84`, two JSON-key regressions plus one MCQ regression, zero fixes.
  - K-only: `46 -> 45 / 84`, one JSON-key regression (`stress_json_keys_001`), zero fixes.
- interpretation: the stress-v3 failure pattern is structured-output and answer-choice brittle, not a general throughput issue. The next policy should protect rows/roles that preserve JSON key structure and answer-choice logits instead of selecting one global Q/K/V role.
- failure-aware role-policy gate:
  - script: `train_python/select_failure_aware_role_policy.py`
  - test: `train_python/test_select_failure_aware_role_policy.py`
  - report: `outputs/real_system_packer_2026-06-05/FAILURE_AWARE_ROLE_POLICY_STRESS_V3_84.md`
  - JSON: `outputs/real_system_packer_2026-06-05/failure_aware_role_policy_stress_v3_84.json`
  - diagnostic output on stress-v3: `json_keys` recommends Q-only because V/K regress; `mcq` recommends K-only because Q/V regress; all other no-regression task types recommend K-only by speed among tested candidates.
  - caveat: this is a fresh-split validation target, not a deployable router.
- verification:
  - `python -m unittest test_select_failure_aware_role_policy test_analyze_chat_task_regressions test_run_with_gpu_guard_disk test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed: `Ran 25 tests ... OK`.
  - `python -m py_compile train_python/select_failure_aware_role_policy.py train_python/test_select_failure_aware_role_policy.py` passed.
  - `python -m unittest test_analyze_chat_task_regressions test_run_with_gpu_guard_disk test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed: `Ran 22 tests ... OK`.
  - `python -m py_compile train_python/analyze_chat_task_regressions.py train_python/test_analyze_chat_task_regressions.py train_python/generate_deterministic_task_stress.py train_python/test_generate_deterministic_task_stress.py train_python/eval_chat_task_benchmark.py train_python/select_projection_role_policy.py train_python/run_with_gpu_guard.py` passed.
  - CodeGraph status after sync: `119 files / 2,575 nodes / 4,742 edges`, index up to date.

Storage after this run and cleanup:

- Latest Windows readback after the first stress-v3 CodeGraph sync: C: about `20.05 GB` free.
- A second low-risk cleanup pass removed about `918 MB` from `wsl-crashes`, refreshed `uv` cache, NVIDIA/D3D shader caches, `CrashDumps`, Explorer thumbnail cache, and repo-local `__pycache__`.
- C: readback after the second cleanup pass was about `20.17 GB` free; final readback after the latest CodeGraph sync was about `20.07 GB` free.
- No HuggingFace/Ollama/LM Studio/model caches were deleted.
