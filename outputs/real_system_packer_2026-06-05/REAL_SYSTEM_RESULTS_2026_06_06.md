# EigenSkill-Q Real-System Results Snapshot

Date: 2026-06-06

This file freezes the current local evidence. It is intentionally conservative: it separates implemented/measured artifacts from claims that still require end-to-end runtime work.

## Tooling State

- CodeGraph CLI is healthy and indexed:
  - 115 files
  - 2,525 nodes
  - 4,645 edges
  - status: up to date
- CodeGraph MCP is registered in `C:\Users\18042\.codex\config.toml` with an absolute command:

```toml
[mcp_servers.codegraph]
command = 'C:\Users\18042\AppData\Roaming\npm\codegraph.cmd'
args = ["serve", "--mcp", "--no-watch"]
```

- Current Codex Desktop tool table may still need a fresh session before direct `mcp__codegraph.*` tools appear. In this running session, use the `codegraph` CLI fallback.
- `understanding-anything@personal` is installed and enabled. `codex plugin list` reports `installed, enabled 0.1.0`; the skill is also mirrored into WSL/Hermes at `/home/rui/.hermes/skills/imported/understanding-anything`.

Latest verification:

- `python -m unittest test_select_failure_aware_role_policy test_analyze_chat_task_regressions test_run_with_gpu_guard_disk test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed: `Ran 25 tests ... OK`.
- Python compile passed for `train_python/select_failure_aware_role_policy.py` and `train_python/test_select_failure_aware_role_policy.py`.
- `python -m unittest test_analyze_chat_task_regressions test_run_with_gpu_guard_disk test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed: `Ran 22 tests ... OK`.
- Python compile passed for `train_python/analyze_chat_task_regressions.py`, `train_python/test_analyze_chat_task_regressions.py`, `train_python/generate_deterministic_task_stress.py`, `train_python/test_generate_deterministic_task_stress.py`, `train_python/eval_chat_task_benchmark.py`, `train_python/select_projection_role_policy.py`, and `train_python/run_with_gpu_guard.py`.
- CodeGraph sync/status passed after the stress-v3 generator expansion: `115 files / 2,525 nodes / 4,645 edges`, index up to date.
- `python3 -m unittest test_run_with_gpu_guard_disk test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed: `Ran 19 tests ... OK`.
- Python compile passed for:
  - `train_python/eval_esmp_module_reconstruction.py`
  - `train_python/measure_esmp_generation_latency.py`
  - `train_python/benchmark_esmp_linear_runtimes.py`
  - `train_python/benchmark_esmp_selected_rows.py`
  - `train_python/benchmark_esmp_fused_selected_rows.py`
  - `train_python/measure_esmp_fused_sidecar_generation.py`
  - `train_python/measure_esmp_fused_qkv_generation.py`
  - `train_python/eval_fused_qkv_prompt_suite.py`
  - `train_python/triton_mixed_gemm.py`
  - `train_python/run_with_gpu_guard.py`
  - `train_python/pack_qwen3_consensus.py`
  - `train_python/repack_qkv_precision_guard.py`
  - `train_python/rank_esmp_row_groups.py`
  - `train_python/sweep_layer20_v_prompt_groups.py`
  - `train_python/compare_prompt_transfer.py`
  - `train_python/select_split_consensus_rowguard.py`
  - `train_python/select_multi_split_rowguard.py`
- C++ CTest passed: 28 / 28 tests.
- C++ packer text fixture passed:
  - tests: `mixed_precision_packer_text_fixture`, `mixed_precision_runtime_bench_text_fixture`
  - input flags: `--weights-text`, `--row-bits-file`
  - manifest: `rows=4`, `cols=8`, `avg_bits=5.25`, bit histogram `{3:1, 4:1, 6:1, 8:1}`, `verify_gemv_rel_l2=0.081011`, `verify_ok=true`
- GPU after the latest local check: about 2187 / 8151 MiB, 5% utilization.
- `repack_qkv_precision_guard.py` now supports `--row-overrides` using the existing C++ packer's `--row-bits-file`, so the current ESMP/Triton runtime can evaluate within-module row-sensitive 4/8-bit packages without format changes.
- `rank_esmp_row_groups.py` ranks ESMP rows/groups by activation-conditioned reconstruction error for follow-up rowguard selection.

## Real Packed Model Artifact

Full Qwen3-0.6B Linear ESMP package:

- model: `Qwen/Qwen3-0.6B`
- packed Linear modules: 197 / 197
- raw FP32 equivalent bytes: 2,383,937,536
- ESMP package bytes: 347,133,248
- compression vs FP32: 6.8675x
- bit histogram:
  - 4-bit: 158 modules
  - 8-bit: 39 modules
- GEMV verification relative L2:
  - mean: 0.1344
  - min: 0.0082
  - max: 0.2229

Local package directory:

```text
outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp
```

Keep `.esmp`, `.f32`, `.raw`, model weights, and similar artifacts local-only.

## ESMP Activation Reconstruction Evidence

Quality-side paired check on real Qwen3-0.6B module activations. This evaluates the real ESMP binary packages by comparing `F.linear(x, original_weight)` against `F.linear(x, ESMP_dequant_weight)` on sampled prompt activations. It is not an end-to-end perplexity or generation benchmark.

Smoke check:

- package: 3-module `qwen3_esmp`
- modules OK: 3 / 3
- median output rel-L2: 0.0762
- median normalized output MSE: 0.005799
- median weight rel-L2: 0.1508
- median compression vs FP32: 7.6409x
- guard peak: 3546 / 8151 MiB = 0.4350

Stratified check:

- package: full Qwen3-0.6B ESMP package
- covered layers: 0, 1, 7, 13, 20, 27
- covered modules: q/k/v/o projections and MLP gate/up/down
- modules OK: 42 / 42
- median output rel-L2: 0.1260
- p90 output rel-L2: 0.2028
- median normalized output MSE: 0.015893
- median weight rel-L2: 0.1555
- median compression vs FP32: 7.6413x
- guard peak: 3547 / 8151 MiB = 0.4352

All-Linear check, excluding `lm_head`:

- modules OK: 196 / 196
- median output rel-L2: 0.1363
- p90 output rel-L2: 0.2114
- median normalized output MSE: 0.018590
- median weight rel-L2: 0.1575
- median compression vs FP32: 7.6414x
- script peak CUDA memory allocated: 1193.70 MiB
- guard peak: 3553 / 8151 MiB = 0.4359

Family-level all-Linear summary:

| family | count | median output rel-L2 | median compression vs FP32 |
|---|---:|---:|---:|
| attention | 112 | 0.1351 | 7.6409x |
| mlp | 84 | 0.1605 | 7.6415x |

Activation reconstruction files:

```text
outputs/real_system_packer_2026-06-05/ESMP_ACTIVATION_SMOKE.md
outputs/real_system_packer_2026-06-05/esmp_activation_smoke.json
outputs/real_system_packer_2026-06-05/ESMP_ACTIVATION_RECONSTRUCTION.md
outputs/real_system_packer_2026-06-05/esmp_activation_reconstruction.json
outputs/real_system_packer_2026-06-05/ESMP_ACTIVATION_ALL_LINEAR.md
outputs/real_system_packer_2026-06-05/esmp_activation_all_linear.json
```

## ESMP-Swapped Generation Smoke

Minimal generation-path wiring check with the first three layer-0 attention projections (`q_proj`, `k_proj`, `v_proj`) replaced by ESMP-backed modules. This is not a high-performance packed runtime yet.

Primary sequential results, all with `Qwen/Qwen3-0.6B`, same prompt, and `max_new_tokens=16`:

| path | replaced modules | selected package compression vs FP32 | TTFT s | elapsed s | tokens/s | script peak CUDA MiB | guard peak MiB | guard ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HF same-loader baseline | 0 | n/a | 0.9489 | 1.6793 | 9.5277 | 1173.30 | 3543 | 0.4347 |
| ESMP cached dequant | 3 | 6.1682x | 0.9542 | 1.7212 | 9.2958 | 1175.30 | 3556 | 0.4363 |
| ESMP on-demand dequant | 3 | 6.1682x | 1.1813 | 2.9897 | 5.3516 | 1170.33 | 3545 | 0.4349 |
| ESMP Triton grouped | 3 | 6.1682x | 1.9611 | 3.2027 | 4.9957 | 1169.85 | 3551 | 0.4357 |

One-warmup steady-state comparison:

| path | runtime | TTFT s | elapsed s | tokens/s | guard peak MiB | guard ratio |
|---|---|---:|---:|---:|---:|---:|
| HF same-loader baseline | dense | 0.0347 | 0.6387 | 25.0523 | 3559 | 0.4366 |
| ESMP cached dequant | dense cached dequant | 0.0320 | 0.5550 | 28.8295 | 3543 | 0.4347 |
| ESMP on-demand dequant | Python dequant per forward | 0.1543 | 1.7552 | 9.1157 | 3544 | 0.4348 |
| ESMP Triton grouped | packed grouped Triton kernel | 0.0458 | 0.7484 | 21.3777 | 3548 | 0.4353 |

Generated text was identical across the primary runs. Interpretation:

- ESMP packages now connect to the generation path for a tested module subset without changing the emitted text.
- Cached dequant is close to the same-loader HF baseline but gives up packed-memory benefits for swapped modules.
- On-demand Python dequant preserves the package boundary but is slow.
- Triton grouped runtime is now wired into generation and beats Python on-demand after warmup, but it still trails dense/cached execution in this tiny 3-module swap. This points to kernel launch overhead, small batch/sequence sizes, and lack of transformer-level fusion as the next bottlenecks.
- Do not compare these 16-token same-loader numbers directly to the earlier 64-token `measure_generation_latency.py` baseline table.

Generation smoke files:

```text
outputs/real_system_packer_2026-06-05/ESMP_SWAPPED_GENERATION_SMOKE.md
outputs/real_system_packer_2026-06-05/qwen3_same_loader_16tok_latency.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_cached_latency_seq.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_ondemand_latency.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_triton_latency.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_triton_warm_latency.json
```

## ESMP Linear Runtime Shape Benchmark

Module-level GPU runtime comparison for the same real ESMP package used by the generation smoke. This isolates Linear-call latency across decode-like and amortized shapes; it is not an end-to-end transformer speed claim.

- model: `Qwen/Qwen3-0.6B`
- modules: layer-0 `q_proj`, `k_proj`, `v_proj`
- batches: 1, 12, 64
- warmup / timed iterations: 10 / 80
- guard peak: 3555 / 8151 MiB = 0.4361
- script peak CUDA memory allocated: 1178.79 MiB

Summary by runtime:

| runtime | cases | median ms | mean ms | median speedup vs dense | median rel-L2 |
|---|---:|---:|---:|---:|---:|
| dense | 9 | 0.014725 | 0.016025 | 1.0000 | 0.000000 |
| cached | 9 | 0.016797 | 0.017905 | 0.8801 | 0.150103 |
| python_on_demand | 9 | 18.072527 | 18.277878 | 0.0009 | 0.150103 |
| triton_grouped | 9 | 0.051871 | 0.054061 | 0.2667 | 0.150103 |

Interpretation:

- The benchmark confirms the real ESMP runtime path works across multiple small batch shapes.
- The current Triton grouped kernel is slower than dense for these Qwen3 layer-0 shapes because the workload is too small to amortize launch and grouped unpack/dequant overhead.
- Cached dequant is close to dense but does not retain packed-memory execution during the Linear call.
- The next kernel work should target decode-specific lower-overhead execution, selected-row execution, or fusion rather than only retuning this standalone grouped kernel.

Runtime-shape files:

```text
outputs/real_system_packer_2026-06-05/ESMP_LINEAR_RUNTIME_SHAPES.md
outputs/real_system_packer_2026-06-05/esmp_linear_runtime_shapes.json
outputs/real_system_packer_2026-06-05/esmp_linear_runtime_shapes.jsonl
outputs/real_system_packer_2026-06-05/esmp_linear_runtime_shapes.csv
outputs/real_system_packer_2026-06-05/esmp_linear_runtime_shapes_gpu_guard.json
```

## ESMP Selected-Row Runtime Benchmark

GPU selected-row execution for the deterministic routing/bypass case. This benchmark avoids materializing the full Linear output and computes only a selected output-row subset. It is a routing/runtime microbenchmark, not a full generation throughput claim.

- model: `Qwen/Qwen3-0.6B`
- modules: layer-0 `q_proj`, `k_proj`, `v_proj`
- batches: 1, 12, 64
- selected output rows: 16, 64, 256
- warmup / timed iterations: 10 / 80
- guard peak: 3561 / 8151 MiB = 0.4369
- script peak CUDA memory allocated: 1177.11 MiB

Summary by runtime:

| runtime | cases | median ms | mean ms | median speedup vs dense full | median speedup vs dense selected | median rel-L2 |
|---|---:|---:|---:|---:|---:|---:|
| dense_full | 27 | 0.019498 | 0.037452 | 1.0000 | 0.8652 | 0.000000 |
| dense_selected | 27 | 0.019366 | 0.031042 | 1.1558 | 1.0000 | 0.000000 |
| cached_selected | 27 | 0.019374 | 0.029179 | 1.2565 | 1.1026 | 0.143407 |
| triton_selected | 27 | 0.048981 | 0.067899 | 0.4235 | 0.4466 | 0.143411 |

Additional counts:

- Triton selected faster than dense full: 4 / 27 cases
- Triton selected faster than dense selected: 4 / 27 cases
- best Triton selected speedup vs dense full: 2.2406x
- best Triton selected speedup vs dense selected: 1.9858x

Interpretation:

- The selected-row packed GPU path is implemented and numerically matches the ESMP dequantized selected rows within the expected quantization error.
- The best cases support the routing/bypass thesis: when the selected slice and shape line up, packed selected-row execution can beat full dense work.
- The median remains slower than dense selected execution, so the honest next step is lower-overhead launch/fusion/tiling work rather than claiming general acceleration.

Selected-row files:

```text
outputs/real_system_packer_2026-06-05/ESMP_SELECTED_ROWS.md
outputs/real_system_packer_2026-06-05/esmp_selected_rows.json
outputs/real_system_packer_2026-06-05/esmp_selected_rows.jsonl
outputs/real_system_packer_2026-06-05/esmp_selected_rows.csv
outputs/real_system_packer_2026-06-05/esmp_selected_rows_gpu_guard.json
outputs/real_system_packer_2026-06-05/ESMP_SELECTED_ROWS_SMOKE.md
```

## ESMP Fused QKV Selected-Row Runtime Benchmark

Same-input multi-module selected-row execution for the deterministic routing/bypass case. This concatenates selected packed rows across QKV projections before launching the INT4/INT8 selected-row kernels, reducing per-module launch overhead. It is still a microbenchmark, not full generation throughput.

- script: `train_python/benchmark_esmp_fused_selected_rows.py`
- model: `Qwen/Qwen3-0.6B`
- modules: QKV projections on layers 0, 1, 7, 13, 20, 27
- batches: 1, 12, 64
- selected output rows per module: 16, 64, 256
- warmup / timed iterations: 10 / 80
- guard peak: 3601 / 8151 MiB = 0.4418
- script peak CUDA memory allocated: 1201.36 MiB

Summary by runtime:

| runtime | cases | median ms | p90 ms | median speedup vs dense full concat | median speedup vs dense selected concat | median speedup vs per-module Triton | median rel-L2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| dense_full_concat | 54 | 0.033235 | 0.080717 | 1.0000 | 0.8388 | 6.9366 | 0.000000 |
| dense_selected_concat | 54 | 0.025728 | 0.084179 | 1.1922 | 1.0000 | 8.5268 | 0.000000 |
| cached_selected_concat | 54 | 0.019379 | 0.073748 | 1.2402 | 1.1350 | 8.9739 | 0.142889 |
| triton_separate_selected | 54 | 0.231445 | 0.448924 | 0.1448 | 0.1173 | 1.0000 | 0.142890 |
| triton_fused_selected | 54 | 0.104230 | 0.201097 | 0.3180 | 0.2753 | 2.0873 | 0.142890 |

Tuned `32x16x64` rerun with the same 10 / 80 timing protocol:

| runtime | cases | median ms | p90 ms | median speedup vs dense full concat | median speedup vs dense selected concat | median speedup vs per-module Triton | median rel-L2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| dense_full_concat | 54 | 0.022409 | 0.072684 | 1.0000 | 0.9670 | 8.2694 | 0.000000 |
| dense_selected_concat | 54 | 0.020298 | 0.064997 | 1.0344 | 1.0000 | 9.2586 | 0.000000 |
| cached_selected_concat | 54 | 0.018727 | 0.059377 | 1.1403 | 1.1453 | 11.2110 | 0.142889 |
| triton_separate_selected | 54 | 0.182602 | 0.297862 | 0.1209 | 0.1082 | 1.0000 | 0.142890 |
| triton_fused_selected | 54 | 0.081686 | 0.148879 | 0.2631 | 0.2515 | 2.3583 | 0.142890 |

Additional counts:

- Fused faster than per-module Triton selected: 52 / 54 cases
- Fused faster than dense full concat: 3 / 54 cases
- Fused faster than dense selected concat: 3 / 54 cases
- best fused speedup vs per-module Triton selected: 10.2491x
- best fused speedup vs dense full concat: 1.1836x
- best fused speedup vs dense selected concat: 1.4580x
- max rel-L2 vs per-module Triton selected: 0.0

Tuned `32x16x64` counts:

- fused faster than per-module Triton selected: 51 / 54 cases
- fused faster than dense full concat: 4 / 54 cases
- fused faster than dense selected concat: 2 / 54 cases
- best fused speedup vs per-module Triton selected: 6.7266x
- best fused speedup vs dense full concat: 1.2170x
- best fused speedup vs dense selected concat: 1.3574x

Compact block sweep:

- tested configs: `16x8x64`, `16x16x64`, `32x8x64`, `32x16x64`, `64x16x128`
- best median speedup vs per-module Triton selected in the sweep: `32x16x64`, 2.4239x median at warmup/iters 6 / 50
- all sweep configs stayed below 44.25% VRAM

Interpretation:

- QKV selected-row fusion is a real systems improvement over launching packed selected kernels independently per module.
- The median still trails dense concat baselines, so this should be framed as launch-overhead reduction evidence and a bridge toward persistent/fused decode kernels, not as a general LLM acceleration claim.

Fused selected-row files:

```text
outputs/real_system_packer_2026-06-05/ESMP_FUSED_SELECTED_ROWS.md
outputs/real_system_packer_2026-06-05/esmp_fused_selected_rows.json
outputs/real_system_packer_2026-06-05/esmp_fused_selected_rows.jsonl
outputs/real_system_packer_2026-06-05/esmp_fused_selected_rows.csv
outputs/real_system_packer_2026-06-05/esmp_fused_selected_rows_gpu_guard.json
outputs/real_system_packer_2026-06-05/ESMP_FUSED_SELECTED_ROWS_TUNED_32x16x64.md
outputs/real_system_packer_2026-06-05/esmp_fused_selected_rows_tuned_32x16x64.json
outputs/real_system_packer_2026-06-05/esmp_fused_selected_rows_tuned_32x16x64_gpu_guard.json
outputs/real_system_packer_2026-06-05/fused_block_sweep/ESMP_FUSED_SELECTED_ROW_BLOCK_SWEEP.md
outputs/real_system_packer_2026-06-05/ESMP_FUSED_SELECTED_ROWS_SMOKE.md
```

## ESMP Fused Selected-Row Sidecar Generation Smoke

Real HF generation with fused selected-row ESMP sidecars attached to QKV inputs. This is a decode-loop integration and overhead check: the sidecar runs on real hidden-state tensors and discards its output; it does not replace dense QKV.

- script: `train_python/measure_esmp_fused_sidecar_generation.py`
- model: `Qwen/Qwen3-0.6B`
- prompt tokens / generated tokens: `12 / 16`
- sidecar suffixes: `q_proj,k_proj,v_proj`
- selected rows per module: `64`
- Triton block config: `32x16x64`

| path | sync mode | sidecar layers | sidecar calls | TTFT s | elapsed s | tokens/s | sidecar CUDA sum ms | sidecar median ms/call | script peak CUDA MiB | guard peak MiB | guard ratio |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| HF same-loader baseline | n/a | 0 | 0 | 0.028981 | 0.543037 | 29.4639 | 0.0000 | 0.0000 | 1173.30 | 3582 | 0.4395 |
| fused ESMP sidecar | per-call | 1 | 16 | 0.041236 | 0.603245 | 26.5232 | 4.6900 | 0.2606 | 1173.43 | 3581 | 0.4393 |
| fused ESMP sidecar | per-call | 3 | 48 | 0.067467 | 0.801341 | 19.9665 | 11.2085 | 0.2218 | 1173.63 | 3588 | 0.4402 |
| fused ESMP sidecar | deferred-end | 1 | 16 | 0.038116 | 0.638191 | 25.0709 | 4.7119 | 0.2653 | 1173.43 | 3582 | 0.4395 |
| fused ESMP sidecar | deferred-end | 3 | 48 | 0.043812 | 0.672049 | 23.8078 | 10.2186 | 0.2062 | 1173.63 | 3583 | 0.4396 |

Interpretation:

- Fused selected-row packed kernels now execute inside the real HF decode loop under GPU guard.
- Throughput drops as expected because this is an extra sidecar, not a replacement path. Per-call synchronization is pessimistic; deferred synchronization improves the 3-layer sidecar from `19.97` to `23.81` tokens/s.
- Memory is essentially unchanged from the same-loader baseline, around `44%` of the 8.15 GiB GPU.
- The next systems step is to replace or fuse actual QKV computation rather than running the sidecar in addition to dense QKV.

Sidecar generation files:

```text
outputs/real_system_packer_2026-06-05/ESMP_FUSED_SIDECAR_GENERATION.md
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_baseline_16tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_baseline_16tok_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_smoke.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_smoke_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_smoke_async.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_smoke_async_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer_async.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer_async_gpu_guard.json
```

## ESMP Fused QKV Replacement Generation Smoke

Real HF generation with selected QKV projections replaced by a shared fused ESMP runtime. This is stronger than the sidecar test: the model's `q_proj`, `k_proj`, and `v_proj` modules are replaced for selected layers. The Q wrapper computes concatenated packed Q/K/V once; K/V read cached slices.

- script: `train_python/measure_esmp_fused_qkv_generation.py`
- model: `Qwen/Qwen3-0.6B`
- runtime: Triton grouped INT4/INT8 packed rows
- block config: `32x16x64`
- sync mode: deferred event sync

| path | replaced layers | max new tokens | TTFT s | elapsed s | tokens/s | speed vs baseline | generated text match | script peak CUDA MiB | guard peak MiB | guard ratio |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| HF same-loader baseline | 0 | 16 | 0.028808 | 0.774345 | 20.6626 | 1.0000x | reference | 1173.30 | 3582 | 0.4395 |
| fused ESMP QKV replacement | 1 | 16 | 0.033764 | 0.488582 | 32.7479 | 1.5850x | exact match | 1168.36 | 3586 | 0.4399 |
| fused ESMP QKV replacement | 3 | 16 | 0.031471 | 0.619774 | 25.8158 | 1.2494x | changed, same topic | 1156.49 | 3592 | 0.4407 |
| HF same-loader baseline | 0 | 64 | 0.048212 | 2.391258 | 26.7642 | 1.0000x | reference | 1178.55 | 3591 | 0.4406 |
| fused ESMP QKV replacement | 1 | 64 | 0.032971 | 2.116118 | 30.2441 | 1.1300x | prefix match, then diverges | 1173.61 | 3587 | 0.4401 |
| fused ESMP QKV replacement | 3 | 64 | 0.032545 | 2.412621 | 26.5272 | 0.9911x | changed, same topic | 1161.74 | 3593 | 0.4408 |

Runtime behavior:

- 1-layer 64-token replacement:
  - compression vs FP32: `6.1682x`
  - wrapper calls / fused compute calls: `192 / 64`
  - cache hits / misses: `128 / 64`
  - fused QKV CUDA event sum: `13.0380 ms`
- 3-layer 64-token replacement:
  - compression vs FP32: `7.0778x`
  - wrapper calls / fused compute calls: `576 / 192`
  - cache hits / misses: `384 / 192`
  - fused QKV CUDA event sum: `29.2797 ms`

Interpretation:

- This is now a true replacement-path smoke, not additive sidecar work.
- The shallow 1-layer replacement shows useful throughput improvement under the same loader and guard.
- Deeper replacement remains near baseline on this prompt but changes generated text. Treat quality preservation as the next bottleneck.
- Do not claim transparent quantized generation yet.

Fused QKV replacement files:

```text
outputs/real_system_packer_2026-06-05/ESMP_FUSED_QKV_REPLACEMENT_GENERATION.md
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_baseline_16tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_1layer.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_baseline_64tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_1layer_64tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_3layer_16tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_3layer_64tok.json
```

## ESMP Fused QKV Prompt-Suite Audit

Deterministic local prompt-suite audit for the true fused QKV replacement path. This reuses the same HF loader, compares baseline and fused outputs across six short prompts, and measures exact text match, common-prefix ratio, character edit similarity, TTFT, tokens/s, CUDA event timing, and guard memory. It is a drift/throughput audit, not a semantic benchmark.

- script: `train_python/eval_fused_qkv_prompt_suite.py`
- model: `Qwen/Qwen3-0.6B`
- max new tokens: `32`
- prompts: `6`
- sync mode: deferred event sync

| path | replaced layers | exact matches | mean edit similarity | mean prefix ratio | mean baseline tokens/s | mean fused tokens/s | fused/baseline speed | median baseline TTFT s | median fused TTFT s | guard peak MiB | guard ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| fused ESMP QKV prompt suite | 1 | 1 / 6 | 0.6051 | 0.3470 | 24.3011 | 20.2237 | 0.8322x | 0.035991 | 0.334715 | 3571 | 0.4381 |
| fused ESMP QKV prompt suite | 3 | 0 / 6 | 0.5221 | 0.1862 | 25.7576 | 21.8530 | 0.8484x | 0.064350 | 0.201079 | 3558 | 0.4365 |

Runtime behavior:

- 1-layer suite:
  - replacement compression vs FP32: `6.1682x`
  - wrapper calls / fused compute calls: `576 / 192`
  - cache hits / misses: `384 / 192`
  - fused CUDA event sum: `2052.3666 ms`
- 3-layer suite:
  - replacement compression vs FP32: `7.0778x`
  - wrapper calls / fused compute calls: `1728 / 576`
  - cache hits / misses: `1152 / 576`
  - fused CUDA event sum: `1515.4567 ms`

Interpretation:

- The one-prompt 16-token speed win does not generalize to this six-prompt audit.
- Both 1-layer and 3-layer replacement are slower than the same-loader dense baseline on mean tokens/s in this suite.
- Output drift is already visible for 1-layer replacement and grows with deeper replacement.
- The next credible step is quality-preserving allocation/search for QKV rows or heads before making broader generation-speed claims.

Prompt-suite files:

```text
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_1LAYER.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_3LAYER.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_3layer.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_3layer_gpu_guard.json
```

### Dense-Role Guard Ablation

`eval_fused_qkv_prompt_suite.py` and `measure_esmp_fused_qkv_generation.py` now support `--dense-roles`, a diagnostic guard that keeps selected QKV roles on the original dense `nn.Linear` while the other roles still use the fused ESMP replacement. This is not a final quantization method; it is an upper-bound/sensitivity probe for which QKV projection should receive higher precision in the next ESMP repack.

| path | replaced layers | dense roles | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | dense role calls | wrapper calls | fused calls | guard peak MiB |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1-layer suite | 1 | none | 1 / 6 | 0.6051 | 0.3470 | 0.8322x | 0 | 576 | 192 | 3571 |
| 1-layer suite | 1 | `q_proj` | 3 / 6 | 0.7448 | 0.6708 | 0.7425x | 192 | 384 | 192 | 3562 |
| 1-layer suite | 1 | `k_proj` | 1 / 6 | 0.5911 | 0.3519 | 0.9673x | 192 | 384 | 192 | 3552 |
| 1-layer suite | 1 | `v_proj` | 1 / 6 | 0.6051 | 0.3470 | 1.0054x | 192 | 384 | 192 | 3553 |
| 1-layer suite | 1 | `q_proj,k_proj` | 4 / 6 | 0.8642 | 0.7722 | 0.9095x | 384 | 192 | 192 | 3553 |
| 3-layer suite | 3 | none | 0 / 6 | 0.5221 | 0.1862 | 0.8484x | 0 | 1728 | 576 | 3558 |
| 3-layer suite | 3 | `q_proj,k_proj` | 0 / 6 | 0.5347 | 0.3397 | 0.9544x | 1152 | 576 | 576 | 3556 |

Interpretation:

- For layer-0 replacement, protecting `q_proj` is the first meaningful quality lever; protecting `k_proj` or `v_proj` alone does not materially improve exact/prefix quality.
- Protecting both `q_proj` and `k_proj` gives the best 1-layer quality recovery while keeping mean speed at `0.9095x` of the same-loader dense baseline.
- The same `q_proj,k_proj` guard does not restore exact matches for 3-layer replacement, so deeper replacement needs layer-specific search or a true higher-precision Q/K ESMP repack rather than a fixed global role rule.

### True Q/K 8-bit Repack Probe

`train_python/repack_qkv_precision_guard.py` creates a small package-summary variant by copying the full Qwen3-0.6B ESMP summary and repacking only selected modules. The first probe repacked layer-0 `q_proj` and `k_proj` at 8-bit, leaving the rest of the package unchanged.

Repacked modules:

| module | bits | verify rel-L2 | package bytes | compression vs FP32 |
|---|---:|---:|---:|---:|
| `model.layers.0.self_attn.q_proj` | 8 | 0.009027 | 2,146,368 | 3.9083x |
| `model.layers.0.self_attn.k_proj` | 8 | 0.008710 | 1,073,216 | 3.9082x |

Package summary:

- output summary: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_layer0_qk8_guard/pack_summary.json`
- overall package compression vs FP32: `6.8365x`

Prompt-suite result with true Q/K 8-bit repack, no dense-role guard:

| path | replaced layers | package change | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | guard peak MiB |
|---|---:|---|---:|---:|---:|---:|---:|
| 1-layer suite | 1 | layer-0 Q/K repacked to 8-bit | 4 / 6 | 0.8248 | 0.7620 | 0.9695x | 3559 |

Interpretation:

- The true Q/K 8-bit ESMP repack nearly matches the dense `q_proj,k_proj` guard's exact-match recovery (`4/6`) while improving mean speed from `0.9095x` to `0.9695x`.
- This is the first concrete quality-preserving ESMP allocation result in the fused generation path.
- The next step is to extend this from module-level Q/K 8-bit to layer-specific Q/K/head-level precision search, then rerun the 3-layer suite.

### 3-layer QK8 vs QKV8 Repack Probe

The layer-0 Q/K result was extended to layers `0,1,7` to identify whether deeper drift is caused by Q/K alone or by the whole attention projection triplet.

| path | replaced layers | package change | package compression vs FP32 | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | guard peak MiB |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| 3-layer suite | 3 | Q/K repacked to 8-bit on layers 0,1,7 | 6.7754x | 0 / 6 | 0.5357 | 0.3397 | 0.6724x | 3552 |
| 3-layer suite | 3 | Q/K/V repacked to 8-bit on layers 0,1,7 | 6.7553x | 3 / 6 | 0.7692 | 0.6555 | 1.0251x | 3554 |

Interpretation:

- Q/K-only protection does not restore deeper replacement. V precision is also necessary once multiple layers are replaced.
- QKV8 on layers `0,1,7` is the strongest current true ESMP fused-generation result: it restores half of exact matches and slightly exceeds the same-loader dense baseline mean speed in this small prompt suite.
- The remaining failures indicate that layer/head-specific precision is still needed; do not generalize this to broad end-to-end acceleration yet.

### QKV8 Layer-Subset Search

Using the same `qwen3_0p6b_layers017_qkv8_guard` package, the prompt suite was first rerun on two-layer subsets to isolate layer sensitivity. A follow-up package then repacked Q/K/V to 8-bit on layers `1,7,13,20,27` while still leaving layer `0` out:

```text
outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers1_7_13_20_27_qkv8_guard/pack_summary.json
```

The five-layer non-layer0 QKV8 package repacked 15 Q/K/V modules, all with `verify_ok=true`; overall compression vs FP32 is `6.7055x`. The repack guard peak was `2203 / 8151 MiB = 27.03%`.

| path | replaced layers | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | guard peak MiB |
|---|---|---:|---:|---:|---:|---:|
| QKV8 subset | `0,1` | 4 / 6 | 0.8469 | 0.7710 | 0.8711x | 3552 |
| QKV8 subset | `0,7` | 4 / 6 | 0.8469 | 0.7710 | 0.8502x | 3553 |
| QKV8 subset | `1,7` | 6 / 6 | 1.0000 | 1.0000 | 0.8957x | 3553 |
| QKV8 full tested set | `0,1,7` | 3 / 6 | 0.7692 | 0.6555 | 1.0251x | 3554 |
| QKV8 non-layer0 expansion | `1,7,13` | 5 / 6 | 0.9444 | 0.8934 | 0.8089x | 3552 |
| QKV8 non-layer0 expansion | `1,7,20` | 5 / 6 | 0.9383 | 0.9096 | 0.8477x | 3554 |
| QKV8 non-layer0 expansion | `1,7,27` | 5 / 6 | 0.9223 | 0.8845 | 1.0880x | 3554 |
| QKV8 non-layer0 expansion | `1,7,13,20,27` | 4 / 6 | 0.8970 | 0.8709 | 0.9641x | 3577 |

Interpretation:

- Layers `1,7` can be replaced together with QKV8 and preserve exact output on this prompt suite.
- Layer `0` is the dominant drift source even at QKV8; any broader policy should treat layer 0 separately, likely via dense fallback, per-head INT8/FP16 protection, or leaving it un-replaced.
- Adding any one of layers `13`, `20`, or `27` to the exact-preserving `1,7` set causes one prompt to drift. Layer `20` has the best prefix score among the tested three-layer subsets; layer `27` has the best measured speed but lower prefix preservation.
- Replacing five non-layer0 QKV8 layers preserves most prefixes but drops exact matches to `4/6`. The next search should therefore move from coarse layer inclusion to head/row-sensitive protection, or use the exact-preserving `1,7` set as the conservative local optimum.

### Row-Sensitive Layer-20 Probe

The row-sensitive repacker was then used to test whether layer `20` could be added to the exact-preserving `1,7` set with partial V-projection protection. In the base `qwen3_0p6b_layers017_qkv8_guard` package, layer-20 Q/K are already 8-bit while V is 4-bit. Therefore the meaningful row-sensitive knob for this layer is V.

An activation-conditioned row/group ranking was computed for layer-20 V using 512 sampled input rows and 128-row groups. The top groups by group score were: `5 (640:768)`, `2 (256:384)`, `6 (768:896)`, `1 (128:256)`, `4 (512:640)`, `7 (896:1024)`, `0 (0:128)`, `3 (384:512)`.

| path | layer-20 precision change | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | replacement compression vs FP32 | guard peak MiB |
|---|---|---:|---:|---:|---:|---:|---:|
| QK8/V4 control | Q/K 8-bit, V 4-bit | 1 / 6 | 0.5789 | 0.3642 | 0.8800x | 4.0741x | 3566 |
| V front-half rowguard | V rows `0:512` at 8-bit, rest 4-bit | 3 / 6 | 0.6960 | 0.6013 | 0.8310x | 3.9894x | 3546 |
| V back-half rowguard | V rows `512:1024` at 8-bit, rest 4-bit | 1 / 6 | 0.6741 | 0.4753 | 0.9298x | 3.9894x | 3546 |
| V top-4 ranked groups | V groups `5,2,6,1` at 8-bit, rest 4-bit | 1 / 6 | 0.6365 | 0.5181 | 0.9619x | 3.9894x | 3555 |
| V top-6 ranked groups | V groups `5,2,6,1,4,7` at 8-bit, rest 4-bit | 2 / 6 | 0.7614 | 0.6431 | 0.7936x | 3.9428x | 3559 |
| full V8 control | Q/K/V all 8-bit (`1,7,20` row in table above) | 5 / 6 | 0.9383 | 0.9096 | 0.8477x | 3.9082x | 3554 |

Prompt-conditioned single-group sweep, 128 V rows per run:

| V group | rows | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | package compression vs FP32 | guard peak MiB |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0 | `0:128` | 2 / 6 | 0.6421 | 0.4764 | 0.8473x | 6.7540x | 3561 |
| 1 | `128:256` | 1 / 6 | 0.5424 | 0.3256 | 0.9272x | 6.7540x | 3554 |
| 2 | `256:384` | 1 / 6 | 0.5498 | 0.3569 | 0.8657x | 6.7540x | 3554 |
| 3 | `384:512` | 1 / 6 | 0.5605 | 0.3141 | 0.9490x | 6.7540x | 3554 |
| 4 | `512:640` | 2 / 6 | 0.7169 | 0.5374 | 0.9750x | 6.7540x | 3554 |
| 5 | `640:768` | 1 / 6 | 0.5789 | 0.3642 | 1.0029x | 6.7540x | 3558 |
| 6 | `768:896` | 1 / 6 | 0.6673 | 0.4753 | 0.9540x | 6.7540x | 3557 |
| 7 | `896:1024` | 1 / 6 | 0.5789 | 0.3642 | 0.9965x | 6.7540x | 3555 |

Prompt-conditioned multi-group candidates:

| V group(s) | rows | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | package compression vs FP32 | guard peak MiB |
|---|---|---:|---:|---:|---:|---:|---:|
| `0+4` | `0:128,512:640` | 2 / 6 | 0.7373 | 0.5875 | 0.6961x | 6.7528x | 3558 |
| `0+4+5` | `0:128,512:640,640:768` | 2 / 6 | 0.7380 | 0.6100 | 0.7066x | 6.7515x | 3553 |
| `0+4+5+6` | `0:128,512:640,640:768,768:896` | 4 / 6 | 0.8476 | 0.7418 | 0.8819x | 6.7503x | 3559 |
| `0+4+6` | `0:128,512:640,768:896` | 3 / 6 | 0.7617 | 0.6263 | 1.0772x | 6.7515x | 3552 |
| `0+6` | `0:128,768:896` | 1 / 6 | 0.6639 | 0.4753 | 0.9710x | 6.7528x | 3553 |
| `4+5+6` | `512:640,640:768,768:896` | 2 / 6 | 0.7322 | 0.5875 | 0.8802x | 6.7515x | 3558 |
| `4+6` | `512:640,768:896` | 2 / 6 | 0.7322 | 0.5875 | 0.9384x | 6.7528x | 3553 |

Prompt-conditioned 5-group expansion around `0+4+5+6`:

| V group(s) | rows | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | package compression vs FP32 | guard peak MiB |
|---|---|---:|---:|---:|---:|---:|---:|
| `0+1+4+5+6` | `0:128,128:256,512:640,640:768,768:896` | 4 / 6 | 0.8476 | 0.7418 | 0.8015x | 6.7490x | 3554 |
| `0+2+4+5+6` | `0:128,256:384,512:640,640:768,768:896` | 3 / 6 | 0.8774 | 0.8286 | 0.9580x | 6.7490x | 3559 |
| `0+3+4+5+6` | `0:128,384:512,512:640,640:768,768:896` | 3 / 6 | 0.7562 | 0.6324 | 0.9144x | 6.7490x | 3554 |
| `0+4+5+6+7` | `0:128,512:640,640:768,768:896,896:1024` | 4 / 6 | 0.8476 | 0.7418 | 0.8340x | 6.7490x | 3553 |

Prompt-conditioned 6-group sweep:

| V group(s) | rows | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | package compression vs FP32 | guard peak MiB |
|---|---|---:|---:|---:|---:|---:|---:|
| `0+1+2+4+5+6` | `0:128,128:256,256:384,512:640,640:768,768:896` | 5 / 6 | 0.9700 | 0.9612 | 0.9378x | 6.7478x | 3559 |
| `0+1+3+4+5+6` | `0:128,128:256,384:512,512:640,640:768,768:896` | 4 / 6 | 0.8519 | 0.7418 | 0.9482x | 6.7478x | 3552 |
| `0+1+4+5+6+7` | `0:128,128:256,512:640,640:768,768:896,896:1024` | 4 / 6 | 0.8476 | 0.7418 | 0.9427x | 6.7478x | 3554 |
| `0+2+3+4+5+6` | `0:128,256:384,384:512,512:640,640:768,768:896` | 3 / 6 | 0.8073 | 0.7391 | 1.0271x | 6.7478x | 3552 |
| `0+2+4+5+6+7` | `0:128,256:384,512:640,640:768,768:896,896:1024` | 3 / 6 | 0.8774 | 0.8286 | 0.9617x | 6.7478x | 3552 |
| `0+3+4+5+6+7` | `0:128,384:512,512:640,640:768,768:896,896:1024` | 3 / 6 | 0.7617 | 0.6263 | 0.8845x | 6.7478x | 3558 |

Prompt-conditioned 7-group focus:

| V group(s) | rows | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | package compression vs FP32 | guard peak MiB |
|---|---|---:|---:|---:|---:|---:|---:|
| `0+1+2+3+4+5+6` | `0:128,128:256,256:384,384:512,512:640,640:768,768:896` | 4 / 6 | 0.8923 | 0.8457 | 0.7253x | 6.7465x | 3554 |
| `0+1+2+4+5+6+7` | `0:128,128:256,256:384,512:640,640:768,768:896,896:1024` | 6 / 6 | 1.0000 | 1.0000 | 0.9314x | 6.7465x | 3554 |

Failure-matrix confirmation:

| run | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed |
|---|---:|---:|---:|---:|
| `full_v8` | 5 / 6 | 0.9383 | 0.9096 | 0.8477x |
| `g0_1_2_4_5_6` | 5 / 6 | 0.9700 | 0.9612 | 0.9378x |
| `g0_1_2_4_5_6_7` | 6 / 6 | 1.0000 | 1.0000 | 0.9314x |
| `g0_1_2_4_5_6_7_repeat` | 6 / 6 | 1.0000 | 1.0000 | 0.9575x |

Interpretation:

- The row-sensitive machinery works end to end: Python generates row-bit files, the C++ packer emits mixed-row `.esmp`, and the existing Triton fused QKV replacement evaluates the result.
- For layer `20`, row-sensitive V protection is not monotonic. The best current setting is not full V8: keeping groups `0+1+2+4+5+6+7` at 8-bit while leaving group `3` (`384:512`) at 4-bit reaches `6/6` exact, edit `1.0000`, and prefix `1.0000` on the six-prompt suite.
- Activation-ranked groups were also insufficient in this first proxy. This is a useful negative result: local row reconstruction error alone does not predict prompt-suite exact preservation here.
- A direct prompt-conditioned single-group sweep confirms the same bottleneck: the best single 128-row group is group `4` (`512:640`) with only `2/6` exact and prefix `0.5374`, still far below full V8 (`5/6`, prefix `0.9096`).
- Multi-group prompt-conditioned selection improves the quality frontier step by step: `0+4+5+6` reaches `4/6`, `0+1+2+4+5+6` reaches `5/6`, and `0+1+2+4+5+6+7` reaches `6/6`.
- Adding group `3` is harmful only on this original six-prompt suite: `0+1+2+3+4+5+6` drops to `4/6`, and full V8 remains only `5/6`. The held-out split below contradicts any global claim about group `3`, so this should be framed as prompt-conditioned precision-monotonicity failure rather than a stable row identity.
- The repeat run for `0+1+2+4+5+6+7` also reaches `6/6` with edit/prefix `1.0000`; however, this is still a six-prompt suite result, not a broad quality guarantee.

New row-guard reports:

```text
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sixgroup_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sevengroup_focus/LAYER20_V_PROMPT_GROUP_SWEEP.md
outputs/real_system_packer_2026-06-05/LAYER20_V_PROMPT_FAILURE_ANALYSIS.md
```

Held-out prompt-suite validation:

To check prompt-suite overfitting, a new 12-prompt held-out suite was created at:

```text
outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v1.txt
```

The held-out comparison reused existing ESMP packages and changed only the prompt file.

| run | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | guard peak MiB |
|---|---:|---:|---:|---:|---:|
| `baseline_layers17` | 11 / 12 | 0.9398 | 0.9172 | 0.8316x | 3558 |
| `full_v8` | 11 / 12 | 0.9398 | 0.9172 | 0.9427x | 3558 |
| `g0_1_2_4_5_6` | 9 / 12 | 0.8456 | 0.7725 | 0.9129x | 3556 |
| `g0_1_2_4_5_6_7` | 9 / 12 | 0.8456 | 0.7725 | 0.7947x | 3555 |
| `g0_1_2_3_4_5_6` | 11 / 12 | 0.9398 | 0.9172 | 0.8546x | 3562 |

Additional 6-group held-out sweep:

| group(s) | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | guard peak MiB |
|---|---:|---:|---:|---:|---:|
| `0+1+2+4+5+6` | 9 / 12 | 0.8456 | 0.7725 | 0.9520x | 3555 |
| `0+1+3+4+5+6` | 7 / 12 | 0.8252 | 0.6949 | 0.9597x | 3558 |
| `0+1+4+5+6+7` | 8 / 12 | 0.8855 | 0.7777 | 0.9146x | 3554 |
| `0+2+3+4+5+6` | 11 / 12 | 0.9398 | 0.9172 | 0.9720x | 3554 |
| `0+2+4+5+6+7` | 10 / 12 | 0.9058 | 0.8553 | 0.9793x | 3558 |
| `0+3+4+5+6+7` | 9 / 12 | 0.9054 | 0.8413 | 0.9778x | 3560 |

Interpretation:

- The 7-group rowguard does not generalize cleanly to this held-out suite: it drops from `6/6` on the original suite to `9/12`, while full V8 and the conservative `1,7` baseline both reach `11/12`.
- The six-prompt positive result should therefore be presented as a diagnostic precision-monotonicity failure, not as a deployable rowguard policy.
- The held-out failures localize to prompts 7 and 8 for both rowguards; prompt 4 fails for all runs and is not specific to the rowguard.
- The `0+1+2+3+4+5+6` negative control is especially important: it is worse on the original prompt suite (`4/6`) but better on held-out (`11/12`). This shows that the apparent harm from adding group `3` is prompt-split dependent, not a global property of that row group.
- The full 6-group held-out sweep makes the inversion sharper: `0+2+3+4+5+6` is bad on the original suite (`3/6`) but strong on held-out (`11/12`), while the original best no-group-3 variants fall to `9/12`.

Prompt-split transfer audit V2:

| candidate | train exact | held-out exact | exact gap | min exact rate | train prefix | held-out prefix | held-out speed | risk |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `baseline_layers17` | 6 / 6 | 11 / 12 | 0.0833 | 0.9167 | 1.0000 | 0.9172 | 0.8316x | small_gap |
| `full_v8` | 5 / 6 | 11 / 12 | -0.0833 | 0.8333 | 0.9096 | 0.9172 | 0.9427x | stable_or_improved |
| `g0_1_2_4_5_6` | 5 / 6 | 9 / 12 | 0.0833 | 0.7500 | 0.9612 | 0.7725 | 0.9520x | small_gap |
| `g0_1_2_4_5_6_7` | 6 / 6 | 9 / 12 | 0.2500 | 0.7500 | 1.0000 | 0.7725 | 0.7947x | high_overfit |
| `g0_1_2_3_4_5_6` | 4 / 6 | 11 / 12 | -0.2500 | 0.6667 | 0.8457 | 0.9172 | 0.8546x | stable_or_improved |
| `g0_1_4_5_6_7` | 4 / 6 | 8 / 12 | 0.0000 | 0.6667 | 0.7418 | 0.7777 | 0.9146x | stable_or_improved |
| `g0_1_3_4_5_6` | 4 / 6 | 7 / 12 | 0.0833 | 0.5833 | 0.7418 | 0.6949 | 0.9597x | small_gap |
| `g0_2_3_4_5_6` | 3 / 6 | 11 / 12 | -0.4167 | 0.5000 | 0.7391 | 0.9172 | 0.9720x | stable_or_improved |
| `g0_2_4_5_6_7` | 3 / 6 | 10 / 12 | -0.3333 | 0.5000 | 0.8286 | 0.8553 | 0.9793x | stable_or_improved |
| `g0_3_4_5_6_7` | 3 / 6 | 9 / 12 | -0.2500 | 0.5000 | 0.6263 | 0.8413 | 0.9778x | stable_or_improved |

This turns the rowguard result into a stronger research claim: prompt-conditioned precision search can overfit the search prompt split and invert conclusions about which row groups are harmful. The most conservative policy in this slice is still `1,7` QKV8, not a layer-20 V rowguard.

Split-consensus selector:

| recommendation | selected policy | decision | score | min exact | held-out exact | exact gap |
|---|---|---|---:|---:|---:|---:|
| best overall | `baseline_layers17` | stable_reference | 0.8339 | 0.9167 | 0.9167 | 0.0833 |
| best rowguard | `g0_1_2_4_5_6` | candidate_needs_third_split | 0.6920 | 0.7500 | 0.7500 | 0.0833 |
| stable rowguard | none | n/a | n/a | n/a | n/a | n/a |

The selector is deliberately conservative: it ranks by worst-split exact match and harmonic exact/prefix, then penalizes train-to-held-out gaps. It recommends no generalized rowguard yet; the next proper test is a third prompt split or a larger held-out suite.

Third prompt-split validation:

A new third prompt file was added at:

```text
outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v2.txt
```

Only selector-relevant candidates were evaluated.

| run | exact matches | mean edit similarity | mean prefix ratio | fused/baseline speed | guard peak MiB |
|---|---:|---:|---:|---:|---:|
| `baseline_layers17` | 12 / 12 | 1.0000 | 1.0000 | 0.9148x | 3588 |
| `full_v8` | 12 / 12 | 1.0000 | 1.0000 | 0.8368x | 3586 |
| `g0_1_2_4_5_6` | 9 / 12 | 0.9046 | 0.8112 | 0.9049x | 3589 |
| `g0_1_2_4_5_6_7` | 9 / 12 | 0.9196 | 0.8295 | 0.9064x | 3592 |
| `g0_2_3_4_5_6` | 11 / 12 | 0.9610 | 0.9373 | 0.9080x | 3589 |

Multi-split selector over search + held-out v1 + held-out v2:

| rank | policy | decision | score | search exact | heldout v1 exact | heldout v2 exact | min exact | exact span | min prefix | mean speed |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `baseline_layers17` | stable_reference | 0.8290 | 1.0000 | 0.9167 | 1.0000 | 0.9167 | 0.0833 | 0.9172 | 0.8807x |
| 2 | `full_v8` | candidate_needs_larger_suite | 0.7661 | 0.8333 | 0.9167 | 1.0000 | 0.8333 | 0.1667 | 0.9096 | 0.8757x |
| 3 | `g0_1_2_4_5_6` | candidate_needs_larger_suite | 0.6818 | 0.8333 | 0.7500 | 0.7500 | 0.7500 | 0.0833 | 0.7725 | 0.9316x |
| 4 | `g0_1_2_4_5_6_7` | candidate_needs_larger_suite | 0.6761 | 1.0000 | 0.7500 | 0.7500 | 0.7500 | 0.2500 | 0.7725 | 0.8775x |
| 5 | `g0_2_3_4_5_6` | reject_for_now | 0.5201 | 0.5000 | 0.9167 | 0.9167 | 0.5000 | 0.4167 | 0.7391 | 0.9691x |

Proxy-augmented selector:

The next selector adds continuous teacher-forced drift on the same held-out prompts:

- final hidden-state relative L2 / normalized MSE
- last-token logits relative L2 / normalized MSE
- selected-layer KV-cache relative L2 / normalized MSE

| rank | policy | family | augmented score | prompt score | proxy penalty | min exact | final hidden rel-L2 | logits rel-L2 | KV mean rel-L2 | KV max rel-L2 |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `baseline_layers17` | baseline | 0.8718 | 0.8290 | 0.0000 | 0.9167 | 0.003705 | 0.003827 | 0.007135 | 0.013254 |
| 2 | `full_v8` | full_precision_probe | 0.7923 | 0.7661 | 0.1293 | 0.8333 | 0.005322 | 0.006759 | 0.009603 | 0.019436 |
| 3 | `g0_1_2_4_5_6_7` | rowguard | 0.6027 | 0.6761 | 0.6176 | 0.7500 | 0.009189 | 0.015244 | 0.021926 | 0.093375 |
| 4 | `g0_1_2_4_5_6` | rowguard | 0.5337 | 0.6818 | 0.9106 | 0.7500 | 0.011246 | 0.020944 | 0.029307 | 0.137661 |
| 5 | `g0_2_3_4_5_6` | rowguard | 0.3985 | 0.5201 | 0.9665 | 0.5000 | 0.011301 | 0.018647 | 0.033858 | 0.164967 |

Recommendations:

- best overall: `baseline_layers17`
- best rowguard after proxy: `g0_1_2_4_5_6_7`, but only as `candidate_needs_larger_suite`
- stable rowguard: none

This third split and proxy pass support the conservative conclusion: the `1,7` baseline remains the only stable reference, while no layer-20 rowguard clears a generalized deployment bar. The continuous proxy is useful because it separates prompt-exact coincidences from hidden/logit/KV drift before spending more generation-audit time. The best rowguard is still a research candidate, not a claim.

V3 task-style prompt audit:

The proxy-filtered candidates were then evaluated on a larger 24-prompt task-style suite:

```text
outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v3_taskstyle.txt
```

| policy | prompts | exact | mean edit | mean prefix | fused/baseline speed | guard peak |
|---|---:|---:|---:|---:|---:|---:|
| `baseline_layers17` | 24 | 19 / 24 | 0.9144 | 0.8906 | 1.0806x | 3588 MiB / 44.02% |
| `full_v8` | 24 | 19 / 24 | 0.8966 | 0.8656 | 1.0308x | 3596 MiB / 44.12% |
| `g0_1_2_4_5_6_7` | 24 | 16 / 24 | 0.8727 | 0.8278 | 0.9788x | 3597 MiB / 44.13% |

The larger v3 suite reinforces the proxy-augmented selector: the rowguard that was perfect on the original six-prompt search split is weaker than both conservative references on a broader task-style split. `baseline_layers17` and `full_v8` tie on exact match, with `baseline_layers17` showing better edit/prefix preservation in this run. The speed ratios are local same-script evidence only; do not promote them to a general end-to-end acceleration claim.

V3 rule-scored task audit:

A lightweight rule scorer was added to check shallow external task properties beyond dense-vs-fused exact text match. It checks rules such as JSON keys, packed-byte arithmetic, sentence count, YAML fields, C++ signature shape, and claim-caveat keywords.

| policy | baseline rule passes | fused rule passes | preserved passes | regressions | improvements | rules used |
|---|---:|---:|---:|---:|---:|---:|
| `baseline_layers17` | 12 / 24 | 13 / 24 | 12 | 0 | 1 | 16 |
| `full_v8` | 12 / 24 | 12 / 24 | 12 | 0 | 0 | 16 |
| `g0_1_2_4_5_6_7` | 12 / 24 | 13 / 24 | 12 | 0 | 1 | 16 |

This scoring layer shows no shallow task-rule regression for these three candidates, but the baseline pass rate is only `12/24`, so it is a diagnostic wrapper rather than a strong benchmark. It complements, but does not replace, the exact/prefix drift evidence. The next quality step should use deterministic expected-answer tasks or established task benchmarks.

V3 chat-template audit:

`eval_fused_qkv_prompt_suite.py` and `measure_esmp_generation_latency.py` now support an opt-in `--chat-template` mode. This formats prompts as user chat messages for instruct models. If the local Transformers path cannot render `apply_chat_template` because `jinja2` is too old, the code falls back to a Qwen/ChatML-style prompt. Default raw-prompt behavior is unchanged for reproducibility.

| policy | prompts | exact | mean edit | mean prefix | fused/baseline speed | rule passes | regressions | guard peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `baseline_layers17` | 24 | 24 / 24 | 1.0000 | 1.0000 | 0.9016x | 15 / 24 | 0 | 3590 MiB / 44.04% |
| `full_v8` | 24 | 23 / 24 | 0.9978 | 0.9824 | 1.0297x | 15 / 24 | 0 | 3585 MiB / 43.98% |
| `g0_1_2_4_5_6_7` | 24 | 22 / 24 | 0.9890 | 0.9469 | 0.9136x | 15 / 24 | 0 | 3599 MiB / 44.15% |

This is the strongest prompt-suite quality evidence so far. It shows raw-prompt evaluation was underestimating instruction-following stability. The conservative `baseline_layers17` policy reaches `24/24` exact against the dense reference under chat-template prompting. `full_v8` and the rowguard remain slightly weaker, so the rowguard caution still stands.

V4 expected-rule task audit:

`score_prompt_suite.py` now supports `--expected-jsonl`, allowing explicit per-row scoring rules instead of inferring rules from prompt wording alone. The expected suite is:

```text
outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v4_expected.jsonl
```

Existing chat-template v3 generation JSONs were rescored with this explicit suite:

| candidate | baseline passes | fused passes | regressions |
|---|---:|---:|---:|
| `baseline_layers17` | 15 / 24 | 15 / 24 | 0 |
| `full_v8` | 15 / 24 | 15 / 24 | 0 |
| `g0_1_2_4_5_6_7` | 15 / 24 | 15 / 24 | 0 |

This removes one source of scorer ambiguity, but remains a shallow deterministic audit. Several strict structured rows fail for both dense baseline and fused outputs, especially JSON/YAML, exact arithmetic-only, and exact sentence-count prompts. The useful claim is narrow: no shallow expected-rule regressions were detected in the existing chat-template v3 outputs.

Chat task benchmark v1:

We added `train_python/eval_chat_task_benchmark.py` and `data_eval/chat_task_benchmark_v1.jsonl`. The local suite is self-contained and uses MMLU-style multiple choice, GSM8K-style numeric answers, IFEval-style JSON/constraint following, and deployment-specific instruction checks. The runner now also supports zero-download local JSONL import through `--task-format native|mmlu|gsm8k|ifeval`; IFEval currently covers the deterministic `keywords:existence` subset. This is not a substitute for full official benchmark suites, but it is stricter and easier to audit than free-form text similarity.

| run | tasks | baseline passes | fused passes | baseline tok/s | fused tok/s | fused/base tok/s | baseline TTFT s | fused TTFT s | guard peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline, chat-template | 12 | 2 | N/A | 22.7031 | N/A | N/A | 0.171191 | N/A | 3601 MiB / 44.18% |
| baseline, chat-template, `/no_think` | 12 | 3 | N/A | 23.9036 | N/A | N/A | 0.152990 | N/A | 3599 MiB / 44.15% |
| fused layers `1,7`, chat-template, `/no_think` | 12 | 3 | 3 | 22.8676 | 19.4066 | 0.8486x | 0.174316 | 0.247880 | 3590 MiB / 44.04% |

Interpretation: `/no_think` is necessary for Qwen3-0.6B strict short-answer evaluation. The baseline remains weak (`3/12`), but the conservative fused layers `1,7` preserve that task accuracy (`3/12 -> 3/12`). Throughput is still worse than dense in this end-to-end task smoke (`0.8486x`), so no end-to-end task-speed claim is allowed from this result.

Held-out reports:

```text
outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/BASELINE_LAYERS17.md
outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/FULL_V8.md
outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/G0_1_2_4_5_6.md
outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/G0_1_2_4_5_6_7.md
outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/G0_1_2_3_4_5_6.md
outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v1/HELDOUT_FAILURE_ANALYSIS.md
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sixgroup_heldout_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md
outputs/real_system_packer_2026-06-05/LAYER20_V_ROWGUARD_TRANSFER_AUDIT_V2.md
outputs/real_system_packer_2026-06-05/LAYER20_V_HELDOUT_ALL_FAILURE_ANALYSIS.md
outputs/real_system_packer_2026-06-05/LAYER20_V_SPLIT_CONSENSUS_SELECTOR.md
outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v2.txt
outputs/real_system_packer_2026-06-05/layer20_v_rowguard_heldout_v2/
outputs/real_system_packer_2026-06-05/LAYER20_V_HELDOUT_V2_FAILURE_ANALYSIS.md
outputs/real_system_packer_2026-06-05/LAYER20_V_MULTI_SPLIT_SELECTOR.md
outputs/real_system_packer_2026-06-05/QKV_PROXY_DRIFT_BASELINE_LAYERS17.md
outputs/real_system_packer_2026-06-05/QKV_PROXY_DRIFT_FULL_V8.md
outputs/real_system_packer_2026-06-05/QKV_PROXY_DRIFT_G0_1_2_4_5_6.md
outputs/real_system_packer_2026-06-05/QKV_PROXY_DRIFT_G0_1_2_4_5_6_7.md
outputs/real_system_packer_2026-06-05/QKV_PROXY_DRIFT_G0_2_3_4_5_6.md
outputs/real_system_packer_2026-06-05/LAYER20_V_PROXY_AUGMENTED_SELECTOR.md
outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v3_taskstyle.txt
outputs/real_system_packer_2026-06-05/LAYER20_V_V3_TASKSTYLE_AUDIT.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_baseline_layers17.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_full_v8.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_g0_1_2_4_5_6_7.md
outputs/real_system_packer_2026-06-05/V3_RULE_SCORED_TASK_AUDIT.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_baseline_layers17_scored.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_full_v8_scored.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_g0_1_2_4_5_6_7_scored.md
outputs/real_system_packer_2026-06-05/V3_CHAT_TEMPLATE_AUDIT.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_baseline_layers17.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_full_v8.md
outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_g0_1_2_4_5_6_7.md
```

Dense-role ablation files:

```text
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_1LAYER_DENSE_Q.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_dense_q.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_dense_q_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_1LAYER_DENSE_K.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_dense_k.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_dense_k_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_1LAYER_DENSE_V.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_dense_v.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_dense_v_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_1LAYER_DENSE_QK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_dense_qk.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_dense_qk_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_3LAYER_DENSE_QK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_3layer_dense_qk.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_3layer_dense_qk_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_0p6b_layer0_qk8_guard/pack_summary.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_1LAYER_QK8_REPACK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_qk8_repack.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_1layer_qk8_repack_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers017_qk8_guard/pack_summary.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_3LAYER_QK8_REPACK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_3layer_qk8_repack.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_3layer_qk8_repack_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers017_qkv8_guard/pack_summary.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_3LAYER_QKV8_REPACK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_3layer_qkv8_repack.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_3layer_qkv8_repack_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS01_QKV8_REPACK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers01_qkv8_repack.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers01_qkv8_repack_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS07_QKV8_REPACK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers07_qkv8_repack.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers07_qkv8_repack_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS17_QKV8_REPACK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers17_qkv8_repack_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers1_7_13_20_27_qkv8_guard/pack_summary.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS1_7_13_QKV8_REPACK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_13_qkv8_repack.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_13_qkv8_repack_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS1_7_20_QKV8_REPACK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_qkv8_repack.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_qkv8_repack_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS1_7_27_QKV8_REPACK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_27_qkv8_repack.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_27_qkv8_repack_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS1_7_13_20_27_QKV8_REPACK.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_13_20_27_qkv8_repack.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_13_20_27_qkv8_repack_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers17_layer20_qkv_halfrow8_guard/pack_summary.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS1_7_20_VHALFROW8.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_vhalfrow8.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_vhalfrow8_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers17_layer20_v_backhalf8_guard/pack_summary.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS1_7_20_VBACKHALF8.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_vbackhalf8.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_vbackhalf8_gpu_guard.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS1_7_20_QK8_V4.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_qk8_v4.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_qk8_v4_gpu_guard.json
outputs/real_system_packer_2026-06-05/LAYER20_V_ROW_GROUP_RANKING.md
outputs/real_system_packer_2026-06-05/layer20_v_row_group_ranking.json
outputs/real_system_packer_2026-06-05/layer20_v_row_group_ranking_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers17_layer20_v_top4ranked8_guard/pack_summary.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS1_7_20_VTOP4RANKED8.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_vtop4ranked8.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_vtop4ranked8_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_0p6b_layers17_layer20_v_top6ranked8_guard/pack_summary.json
outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_LAYERS1_7_20_VTOP6RANKED8.md
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_vtop6ranked8.json
outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_layers1_7_20_vtop6ranked8_gpu_guard.json
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sweep/layer20_v_prompt_group_sweep.json
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_sweep/layer20_v_prompt_group_sweep.csv
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_combo_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_combo_sweep/layer20_v_prompt_group_sweep.json
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_combo_sweep/layer20_v_prompt_group_sweep.csv
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_expansion_sweep/LAYER20_V_PROMPT_GROUP_SWEEP.md
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_expansion_sweep/layer20_v_prompt_group_sweep.json
outputs/real_system_packer_2026-06-05/layer20_v_prompt_group_expansion_sweep/layer20_v_prompt_group_sweep.csv
```

## End-to-End HF Generation Baseline

These are baseline HF FP16 generation metrics, not ESMP runtime metrics.

| model | dtype | TTFT s | tokens/s | script peak GPU memory MiB | guard peak MiB | guard peak ratio |
|---|---|---:|---:|---:|---:|---:|
| Qwen/Qwen3-0.6B | FP16 | 1.0404 | 17.5632 | 2028.14 | 4993 | 0.6126 |
| Qwen/Qwen3-1.7B | FP16 | 1.3376 | 13.7890 | 5063.25 | 7216 | 0.8853 |

Interpretation:

- Qwen3-1.7B fits but is close to the current 90% VRAM ceiling on this machine.
- Current active GPU rule from Rui's goal is at most 90% VRAM. Use guard defaults that keep runs below that cap; the prior Qwen3-1.7B run peaked at 88.53%, so smaller shapes are still safer for long experiments.

## Triton Packed Mixed GEMM Evidence

Real GPU packed-storage benchmark on RTX 5070 Laptop GPU.

Sweep highlights:

- `2048x1024 batch=16 high_every=8`
  - grouped mixed: 0.043845 ms
  - torch FP16: 0.049066 ms
  - grouped/FP16 speedup: 1.119x
  - compression vs FP16: 3.50x
  - rel-L2: 0.1327
- `2048x1024 batch=1 high_every=16`, tuned best:
  - grouped mixed: 0.036570 ms
  - torch FP16: 0.076529 ms
  - grouped/FP16 speedup: 2.0927x
  - compression vs FP16: 3.70x
  - rel-L2: 0.1363

Block tuning summary:

- configurations tested: 216 across `2048x1024`, `3072x1024`, and `1024x3072`
- grouped low-bit faster than torch FP16: 26 / 216 configs
- grouped faster than row-wise dynamic path: 134 / 216 configs
- max grouped/FP16 speedup: 2.1048x
- p90 grouped/FP16 speedup: 1.2625x
- median grouped/FP16 speedup: 0.4113x
- max grouped/row-wise speedup: 5.7507x
- median grouped/row-wise speedup: 1.5889x
- median compression vs FP16: 3.6203x
- median grouped rel-L2: 0.1375
- max observed VRAM during tuning: 0.3019 of 8151 MiB

Cross-shape summary files:

```text
outputs/real_system_packer_2026-06-05/TRITON_CROSS_SHAPE_SUMMARY.md
outputs/real_system_packer_2026-06-05/triton_cross_shape_summary.json
outputs/real_system_packer_2026-06-05/triton_cross_shape_summary.csv
```

Interpretation:

- This is real packed low-bit GPU execution evidence.
- It is still a prototype GEMM benchmark, not a fused transformer runtime.
- The honest claim is "grouped packed execution reduces dynamic row-wise overhead and can beat FP16 in tuned subcases while compressing weights", not "general SOTA LLM acceleration".

## C++ ESMP Runtime Evidence

Module-level CPU ESMP runtime on real Qwen3-0.6B packed modules:

- stratified module runs: 42 / 42 successful
- covered layers: 0, 1, 7, 13, 20, 27
- covered module types: q/k/v/o projections and MLP gate/up/down
- median full packed GEMV: 6.3678 ms
- median selected 64-row GEMV: 0.2056 ms
- median selected/full speedup: 16.8259x
- max selected/full speedup: 56.4888x
- median compression vs FP32: 7.6413x
- fastest selected-row run: 0.1801 ms
- slowest full packed GEMV in this sweep: 15.2639 ms

Family-level summary:

| family | count | median full ms | median selected ms | median selected/full speedup | median compression vs FP32 |
|---|---:|---:|---:|---:|---:|
| attention | 24 | 5.5207 | 0.2056 | 16.3918x | 7.6409x |
| mlp | 18 | 9.2310 | 0.2078 | 46.3437x | 7.6415x |

Runtime sweep files:

```text
outputs/real_system_packer_2026-06-05/ESMP_RUNTIME_STRATIFIED_SWEEP.md
outputs/real_system_packer_2026-06-05/esmp_runtime_stratified_sweep.jsonl
outputs/real_system_packer_2026-06-05/esmp_runtime_stratified_sweep.csv
```

Interpretation:

- Full CPU low-bit GEMV is not enough for an end-to-end win yet.
- Selected-row execution is strong evidence for deterministic routing/bypass: when the runtime can avoid full-row work, latency falls by more than an order of magnitude across the 42-module stratified sweep.

## Current C Drive State

Storage snapshot after safe cache cleanup and the disk-aware guard update:

- C: about 19.5 GB free / 500.41 GB total after the latest v4 expected-rule update and repo-local cache cleanup
- D: 57.30 GB free / 421.25 GB total
- F: 23.42 GB free / 29.99 GB total

Safe cleanups already run:

- `uv cache clean`: removed about 169.7 MiB from `C:\Users\18042\AppData\Local\uv\cache`
- `python -m pip cache purge`: removed about 6.46 GB from `d:\caches\pip`, so it mostly helped D, not C
- `npm cache clean --force`: completed
- repo-local `train_python\__pycache__`: removed after ESMP activation/generation script compile-runs; total reclaimed was small, under 1 MiB
- latest invalid empty-layer prompt-suite artifacts from a failed shell-variable loop were removed from `outputs/real_system_packer_2026-06-05`
- latest repo-local `__pycache__` cleanups removed about 0.40 MiB; Windows free space remains around 20 GB because the dominant pressure is WSL VHDX, app assets, and model/cache directories that were intentionally not deleted
- latest post-compile repo-local `__pycache__` / `.pytest_cache` / `.ruff_cache` cleanup removed about 0.136 MiB; WSL cache check now shows apt archives at about 72 KiB, Triton cache at about 18 MiB, and NVIDIA ComputeCache at about 4 KiB
- latest post-combo-sweep repo-local cache cleanup removed about 0.124 MiB
- latest post-expansion-sweep repo-local cache cleanup removed about 0.115 MiB
- latest post-selector repo-local cache cleanup removed about 0.139 MiB; WSL apt archive cache is about 72 KiB
- latest post-multi-selector repo-local cache cleanup removed about 0.131 MiB; safe caches are no longer the dominant C-drive pressure
- latest post-proxy-selector repo-local cache cleanup removed about 0.126 MiB; C: remained around 19.70 GB because active logs/WSL VHDX growth dominate tiny repo-cache savings
- latest post-v3-audit repo-local cache cleanup removed about 0.106 MiB; latest C: reading is about 19.83 GB free
- latest post-chat-template-audit repo-local cache cleanup removed about 0.157 MiB; latest C: reading is about 19.87 GB free
- latest disk-aware guard cleanup removed about 0.160 MiB from repo-local Python caches; guard JSON recorded about 19.65 GB free, and the next Windows readback was about 19.68 GB free
- latest post-v4 expected-rule cleanup removed about 0.152 MiB from repo-local Python caches; latest guard JSON recorded about 19.52 GB free, with later Windows readback around 19.49 GB after CodeGraph sync
- latest CodeGraph/disk recheck cleanup dry-run found no repo-local cache targets:
  - output: `outputs/real_system_packer_2026-06-05/codegraph_disk_cleanup_dry_run_guard.json`
  - reclaimable bytes: `0`
  - guard GPU peak: `2226/8151 MiB = 27.31%`
  - Windows readback around the recheck: C: about `19.19 GB` free at final readback
  - targeted visible pressure points: `.ollama` about `8.56 GB`, `.codex` about `8.03 GB`, active workspace root about `5.33 GB`, user temp about `0.96 GB`, `.cache` about `0.89 GB`
- latest manual low-risk Windows cleanup removed about `1.316 GB` from `C:\Users\18042\AppData\Local\Temp\d54byrr5`, `C:\Users\18042\AppData\Local\uv\cache`, and repo-local `train_python\__pycache__`; C: moved from about `18.99 GB` free to `20.31 GB` free before the next guarded evals.
- latest IFEval v2 projection-role ablation runs used the disk-aware guard with `--min-disk-free-gb 15` and repo-local cache cleanup:
  - V-only guard peak `3761/8151 MiB = 46.14%`; cleanup removed about `0.107 MiB`; end disk state about `19.21 GB` free
  - Q-only guard peak `3753/8151 MiB = 46.04%`; cleanup removed about `0.107 MiB`; end disk state about `19.20 GB` free
  - K-only guard peak `3755/8151 MiB = 46.07%`; cleanup removed about `0.107 MiB`; end disk state about `19.20 GB` free
- latest V1 V-only task ablations also used the disk-aware guard:
  - 32-token V-only guard peak `3763/8151 MiB = 46.17%`; cleanup removed about `0.107 MiB`; end disk state about `19.20 GB` free
  - 64-token V-only guard peak `3766/8151 MiB = 46.20%`; cleanup removed about `0.107 MiB`; end disk state about `19.20 GB` free
  - 32-token V-only layers `1,7,20` guard peak `3763/8151 MiB = 46.17%`; cleanup removed about `0.107 MiB`; end disk state about `19.20 GB` free
  - IFEval v2 V-only layers `1,7,20` guard peak `3758/8151 MiB = 46.10%`; cleanup removed about `0.107 MiB`; end disk state about `19.20 GB` free
- post-selector repo-local cleanup:
  - output: `outputs/real_system_packer_2026-06-05/post_projection_selector_repo_cache_cleanup_guard.json`
  - guard peak `2397/8151 MiB = 29.41%`
  - cleanup removed about `0.058 MiB` from `train_python/__pycache__`
  - latest Windows readback: C: about `19.19 GB` free
- latest V1 Q/K role ablation guards:
  - Q-only guard peak `4033/8151 MiB = 49.48%`; repo cleanup removed about `0.107 MiB`; end disk state about `20.27 GB` free.
  - K-only guard peak `3848/8151 MiB = 47.21%`; repo cleanup removed about `0.107 MiB`; end disk state about `20.27 GB` free.
- latest stress-v3 84-row guards peaked at `4397/8151 MiB = 53.94%` for Q-only, `4450/8151 MiB = 54.59%` for V-only, and `4458/8151 MiB = 54.69%` for K-only.
- stress-v3 regression-analysis artifacts now exist:
  - report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_REGRESSION_ANALYSIS.md`
  - JSON: `outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_regression_analysis.json`
  - Q-only: one MCQ regression, no fixes.
  - V-only: two JSON-key regressions and one MCQ regression, no fixes.
  - K-only: one JSON-key regression, no fixes.
- latest Windows readback after stress-v3 runs and CodeGraph sync: C: about `20.05 GB` free
- second low-risk Windows cleanup pass removed about `918 MB` from `wsl-crashes`, refreshed `uv` cache, NVIDIA/D3D shader caches, `CrashDumps`, Explorer thumbnail cache, and repo-local `__pycache__`; no model caches were deleted. C: readback after this pass was about `20.17 GB` free, and the final readback after the latest CodeGraph sync was about `20.07 GB` free.
- CodeGraph status after latest sync: `119 files / 2,575 nodes / 4,742 edges`, index up to date

`train_python/run_with_gpu_guard.py` now records disk state and supports these storage controls:

- `--min-disk-free-gb`
- `--disk-check-path`
- `--cleanup-repo-caches`
- `--cleanup-root`
- `--cleanup-dry-run`

The cleanup scope is intentionally narrow: repo-local `__pycache__`, `.pytest_cache`, `.ruff_cache`, `*.pyc`, and `*.pyo`; `.git`, `.codegraph`, `outputs`, `build`, `research_pack_2026-06-03`, and `.venv*` are skipped.

Main C-drive pressure points:

- WSL VHDX: `C:\Users\18042\AppData\Local\wsl\{437898f7-8f9f-4634-98cd-99603dd9b5ec}\ext4.vhdx`, about 62.82 GB
- WSL internal rootfs uses about 41 GB, so VHD compaction can reclaim some Windows-side space
- WSL `/home/rui/.cache/huggingface` is about 17 GB and should be kept for the current Qwen/OLMo experiments unless space becomes urgent
- Windows model/app caches currently visible from the targeted scan: `C:\Users\18042\.ollama` about 8.56 GB, `C:\Users\18042\.lmstudio` about 3.38 GB, `C:\Users\18042\.cache` about 0.89 GB, and `C:\Users\18042\AppData\Local\Temp` about 0.61 GB. Do not delete Ollama/LM Studio/model caches without Rui's explicit choice.
- Other cache candidates inside WSL: `/var/cache/apt/archives` about 1.2 GB, `/home/rui/.npm/_cacache` about 398 MB, `/home/rui/.triton/cache` about 98 MB
- `.codex` logs/backups are large, but active session/log deletion should not be done while Codex Desktop is running
- Steam/Epic/Lenovo/Docker are also large, but they are user/application assets and should not be removed automatically

WSL was used for the latest guarded benchmark, so do not shut it down in the middle of experiment work. Compacting the VHD requires closing WSL and running elevated/admin PowerShell:

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

Do not use `wsl.exe --manage Ubuntu-22.04 --set-sparse true` without reviewing `--allow-unsafe`; the current WSL build rejected the safer invocation and requested an unsafe flag.

## Claims Allowed Now

- We implemented a real mixed-precision binary packer (`ESMPQ001`) and packed all Qwen3-0.6B Linear modules.
- We have C++ runtime benches that execute the packed ESMP module format.
- We have C++ runtime benches across 42 real packed Qwen3-0.6B modules, showing median 16.83x selected-row speedup over full packed GEMV.
- We have a Triton GPU packed-storage mixed INT4/INT8 GEMM prototype with 216 measured cross-shape tuning configurations, measured compression, latency, rel-L2, and guard VRAM.
- We have quality-side activation reconstruction checks for real ESMP binary packages: 3-module smoke, 42-module stratified, and 196-module all-Linear excluding `lm_head`.
- We have a minimal ESMP-swapped generation smoke test for 3 layer-0 attention modules, with same-loader baseline, cached dequant, Python on-demand, and Triton grouped timing plus identical generated text.
- We have a real ESMP Linear runtime-shape benchmark across batch 1/12/64 for the same 3 swapped modules, showing that the current standalone Triton grouped path works but is slower than dense on these small shapes.
- We have a real GPU selected-row ESMP benchmark with new Triton selected INT4/INT8 kernels; it shows useful best-case wins but no median acceleration yet.
- We have a real HF generation sidecar integration: fused QKV selected-row ESMP kernels execute on live decode activations, with TTFT/tokens/s/memory and sidecar CUDA event timing.
- We have a true fused ESMP QKV replacement smoke inside HF generation, including cache-hit evidence, compression, TTFT/tokens/s, memory, and text-change analysis.
- We have a six-prompt drift/throughput audit for true fused QKV replacement; it shows prompt-suite negative speed and quality evidence that must be fixed before broad claims.
- We have a dense-role guard ablation showing that layer-0 Q/K projections are more quality-sensitive than V under this prompt suite; this motivates targeted Q/K higher-precision repacking rather than uniform role replacement.
- We have a true layer-0 Q/K 8-bit ESMP repack probe: exact `4/6`, mean prefix `0.7620`, and mean speed `0.9695x` in the 1-layer prompt suite, with overall package compression still `6.8365x`.
- We have a true 3-layer QKV8 ESMP repack probe on layers `0,1,7`: exact `3/6`, mean prefix `0.6555`, speed `1.0251x`, and overall package compression `6.7553x`; QK8 alone failed on exact match.
- We have a QKV8 layer-subset search showing layers `1,7` preserve exact output together (`6/6`), while combinations containing layer `0` drift. A follow-up non-layer0 expansion shows adding one of `13`, `20`, or `27` to `1,7` yields `5/6`, and replacing `1,7,13,20,27` yields `4/6`.
- We have implemented and tested row-sensitive repacking via `--row-overrides` and added `rank_esmp_row_groups.py`, `sweep_layer20_v_prompt_groups.py`, `analyze_prompt_suite_failures.py`, `compare_prompt_transfer.py`, and `select_split_consensus_rowguard.py`. For layer `20`, QK8/V4 scores `1/6`, V front-half 8-bit scores `3/6`, V back-half 8-bit scores `1/6`, V top-4 ranked groups score `1/6`, V top-6 ranked groups score `2/6`, prompt-conditioned single 128-row groups top out at `2/6`, initial multi-group candidates reach `4/6`, 6-group search reaches `5/6`, and the 7-group rowguard `0+1+2+4+5+6+7` reaches repeat-verified `6/6` with edit/prefix `1.0000`. This is narrow evidence of prompt-conditioned precision-monotonicity failure on the original six-prompt suite, not a generalized rowguard claim.
- We have a held-out 12-prompt validation and a full 6-group held-out sweep. The original 7-group rowguard drops to `9/12`, while full V8 and the conservative `1,7` baseline reach `11/12`; a different 6-group candidate `0+2+3+4+5+6` also reaches `11/12` on held-out despite being poor on the original suite (`3/6`). This strengthens the prompt-split instability story and weakens any deployability claim for the current rowguards.
- We have a prompt-split transfer audit V2 showing exact-rate inversion across prompt splits: `g0_1_2_4_5_6_7` is perfect on the search suite but `high_overfit` on held-out, while candidates such as `g0_2_3_4_5_6` are weak on search (`3/6`) but strong on held-out (`11/12`). This is concrete evidence for prompt-split instability in prompt-conditioned precision search.
- We have a split-consensus selector report. It selects `baseline_layers17` as the safest overall policy and `g0_1_2_4_5_6` only as a rowguard candidate that needs a third split. It recommends no stable generalized rowguard yet.
- We have now run a third prompt split for the selector-relevant policies. `baseline_layers17` and `full_v8` reach `12/12`; the original no-group-3 rowguards remain at `9/12`; `g0_2_3_4_5_6` reaches `11/12` on both held-out splits but is only `3/6` on search. The multi-split selector still recommends no stable generalized rowguard.
- We have added a QKV/hidden/logit continuous proxy and a proxy-augmented selector. It ranks `baseline_layers17` first, `full_v8` second, and strongly penalizes rowguards because their KV drift is much higher than their prompt exact rates suggest. No stable rowguard is recommended.
- We have run a 24-prompt v3 task-style audit for the proxy-filtered candidates. `baseline_layers17` and `full_v8` tie at `19/24`, while the rowguard `g0_1_2_4_5_6_7` drops to `16/24`, reinforcing the prompt-conditioned overfitting story.
- We have added a rule-scored task wrapper with TDD coverage. On the v3 outputs, it shows no shallow task-rule regressions, but baseline task-rule pass rate is limited; this is a diagnostic layer, not a paper-grade task benchmark yet.
- We have added opt-in chat-template prompting for instruct-model evaluation. On the v3 chat-template audit, `baseline_layers17` reaches `24/24`, `full_v8` `23/24`, and rowguard `22/24`; rule scoring shows no shallow regressions. Future instruct-model prompt audits should use `--chat-template`.
- We have added v4 explicit expected-rule scoring. Rescoring the existing chat-template v3 outputs gives `15/24` baseline and fused passes for all three candidates, with zero regressions, while exposing that strict structured-output rows are weak for the dense baseline too.
- We have added chat task benchmark v1 with TDD coverage and zero-download local JSONL import for MMLU/GSM8K/IFEval-style slices. On Qwen3-0.6B, `/no_think` improves strict short-answer accuracy from `2/12` to `3/12`; fused layers `1,7` preserve `3/12` but are slower end-to-end (`0.8486x` tokens/s vs dense).
- We have extended the deterministic task scorer and IFEval-style import path. The scorer now strips visible `<think>...</think>` blocks before deterministic matching, which corrects undercounted Qwen MCQ answers such as `<think>...</think>\n\nB. ...`. The IFEval subset now covers `keywords:existence`, `keywords:forbidden_words`, `detectable_format:json_format`, `length_constraints:number_sentences`, `length_constraints:number_words`, and multi-instruction `all_of` rows.
- Under the updated scorer, the Qwen3-0.6B V1 no-think layers `1,7` rerun reaches baseline `5/12` and fused `5/12`, with fused/base token rate `0.9157x` and guard peak `3592/8151 MiB = 44.07%`.
- Under the same 32-token V1 setup, a V-only role ablation on layers `1,7` reaches baseline `5/12` and fused `5/12`, with fused/base token rate `1.0142x` and guard peak `3763/8151 MiB = 46.17%`. A separate 64-token V-only rerun reaches `7/12 -> 7/12`, with fused/base token rate `0.9713x` and guard peak `3766/8151 MiB = 46.20%`.
- Under the same 32-token V1 setup, Q-only and K-only role ablations now exist:
  - Q-only layers `1,7`: baseline `5/12`, fused `5/12`, fused/base tok/s `1.1926x`, guard peak `4033/8151 MiB = 49.48%`
  - K-only layers `1,7`: baseline `5/12`, fused `5/12`, fused/base tok/s `0.9410x`, guard peak `3848/8151 MiB = 47.21%`
- Expanding V-only to layers `1,7,20` preserves V1 32-token pass count (`5/12 -> 5/12`) but slows sharply (`0.6903x`) and increases TTFT. On IFEval v2, the same expansion regresses quality (`2/8 -> 1/8`) and runs at `0.8516x`. This makes layers `1,7` the current conservative V-only boundary.
- A new zero-download IFEval-style deterministic v2 slice exists at `data_eval/ifeval_deterministic_v2.jsonl`, with audit `outputs/real_system_packer_2026-06-05/IFEVAL_V2_DETERMINISTIC_AUDIT.md`. On Qwen3-0.6B layers `1,7`, baseline reaches `2/8` while fused reaches `1/8`, guard peak `3595/8151 MiB = 44.11%`. This is negative quality evidence for the fused candidate.
- IFEval-style v2 projection-role ablation now exists for layers `1,7`. Single-role packed replacement preserved the small-slice pass count for all three roles: V-only `2/8 -> 2/8` with `1.0872x` fused/base tok/s, Q-only `2/8 -> 2/8` with `0.9980x`, and K-only `2/8 -> 2/8` with `0.9366x`. This narrows the full-QKV regression to role interactions and makes V-only the next conservative candidate, not a finished deployment claim.
- Projection-role selector now exists:
  - script: `train_python/select_projection_role_policy.py`
  - test: `train_python/test_select_projection_role_policy.py`
  - cross-slice report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR.md`
  - IFEval-only role report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_IFEVAL_ONLY.md`
  - cross-slice result: selects `vonly_layers17` as `conservative_candidate`, score `0.9099`, min speed `1.0142x`, max TTFT ratio `0.9302`; rejects `full_qkv_layers17` and `vonly_layers1720` due to IFEval v2 pass-count regression.
  - IFEval-only result: ranks V-only first, Q-only second, K-only third; rejects full-QKV and layer-20 V-only expansion.
- Chat task stress v2 now exists:
  - generator/test: `train_python/generate_deterministic_task_stress.py`, `train_python/test_generate_deterministic_task_stress.py`
  - task file: `data_eval/chat_task_stress_v2.jsonl`
  - audit: `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V2_AUDIT.md`
  - task count/types: 42 deterministic local rows covering `mcq`, `number`, `json_keys`, `contains_all`, `contains_none`, `sentence_count`, `word_count`, and `all_of`
  - tests: `python -m unittest test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed (`15` tests)
  - V-only layers `1,7`: stress baseline `22/42`, fused `21/42`, fused/base tok/s `0.9924x`, guard peak `3759/8151 MiB = 46.12%`
  - Q-only layers `1,7`: stress baseline `22/42`, fused `22/42`, fused/base tok/s `1.0080x`, guard peak `3774/8151 MiB = 46.30%`
  - K-only layers `1,7`: stress baseline `22/42`, fused `21/42`, fused/base tok/s `1.0028x`, guard peak `4266/8151 MiB = 52.34%`
  - IFEval+Stress selector report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_IFEVAL_STRESS.md`
  - IFEval+Stress result: selects `qonly_layers17` as `quality_preserving_speed_neutral`, score `0.9006`, no pass-count regression on either split, min speed `0.9980x`, max TTFT ratio `0.9761`; rejects V-only and K-only because both regress stress v2.
  - V1+IFEval+Stress selector report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_V1_IFEVAL_STRESS.md`
  - V1+IFEval+Stress result: selects `qonly_layers17` as `quality_preserving_speed_neutral`, score `0.9118`, no pass-count regression on any of the three splits, min speed `0.9980x`, max TTFT ratio `0.9761`. V-only and K-only are rejected due to stress-v2 pass-count regression. Full-QKV is not included because its stress-v2 run timed out and has no valid result.
  - stress-v3 84-row expansion:
    - task file: `data_eval/chat_task_stress_v3_84.jsonl`
    - Q-only layers `1,7`: baseline `46/84`, fused `45/84`, fused/base tok/s `0.9272x`, guard peak `4397/8151 MiB = 53.94%`
    - V-only layers `1,7`: baseline `46/84`, fused `43/84`, fused/base tok/s `0.9653x`, guard peak `4450/8151 MiB = 54.59%`
    - K-only layers `1,7`: baseline `46/84`, fused `45/84`, fused/base tok/s `0.9746x`, guard peak `4458/8151 MiB = 54.69%`
  - V1+IFEval+Stress+Stress-v3 selector report: `outputs/real_system_packer_2026-06-05/PROJECTION_ROLE_POLICY_SELECTOR_V1_IFEVAL_STRESS_V3.md`
  - four-split result: no single-role policy is quality-preserving. Q-only is rejected because stress-v3 loses one pass; V-only and K-only are also rejected. This supersedes the three-split Q-only candidate interpretation.
  - stress-v3 regression analysis:
    - report: `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_REGRESSION_ANALYSIS.md`
    - JSON: `outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_regression_analysis.json`
    - Q-only regression: `stress_mcq_extra_000` changes the answer from `A` to `B`.
    - V-only regressions: two `json_keys` rows and one MCQ row; this suggests V replacement is brittle for structured-key preservation on this slice.
    - K-only regression: the same `stress_json_keys_001` JSON-key row seen in V-only; this suggests structured-output rows need row/role protection rather than a single global role choice.
    - No candidate produced any fix rows on stress-v3.
  - failure-aware role-policy gate:
    - script/test: `train_python/select_failure_aware_role_policy.py`, `train_python/test_select_failure_aware_role_policy.py`
    - report: `outputs/real_system_packer_2026-06-05/FAILURE_AWARE_ROLE_POLICY_STRESS_V3_84.md`
    - JSON: `outputs/real_system_packer_2026-06-05/failure_aware_role_policy_stress_v3_84.json`
    - stress-v3 diagnostic recommendation: use Q-only for `json_keys`, K-only for `mcq`, and K-only for the no-regression task types if choosing by tested task type. This is a fresh-split validation target, not a deployment policy.
  - Current interpretation: Q-only layers `1,7` is a falsified three-split candidate, not a deployable policy. The next method step should use these failure rows to design stricter role/row protection or larger-slice selection.
  - Full-QKV layers `1,7` on stress v2 exceeded the 20-minute command timeout and was stopped. No full-QKV stress result is valid yet.
- GPU guard timeout support now exists:
  - script: `train_python/run_with_gpu_guard.py`
  - test: `train_python/test_run_with_gpu_guard_disk.py`
  - new CLI: `--timeout-sec` and `--max-start-memory-ratio`
  - `--timeout-sec` records `killed_by_timeout` and `timeout_seconds`; timeout exits with code `91`
  - `--max-start-memory-ratio` rejects before launch when the GPU is already too occupied by a game, LM Studio, Ollama, or another process.
  - verification: `python -m unittest test_run_with_gpu_guard_disk test_generate_deterministic_task_stress test_eval_chat_task_benchmark test_select_projection_role_policy` passed (`19` tests)
- We have FP16 HF TTFT/tokens/s baselines for Qwen3-0.6B and Qwen3-1.7B.
- We have a mobile NEON decode source scaffold, but not physical Redmi K80 Pro results yet.
- We have a three-split role-policy gate across V1 32-token, IFEval v2, and stress v2 that initially selects Q-only layers `1,7`, and a four-split gate including stress-v3 84-row expansion that rejects all tested single-role policies. A dedicated stress-v3 regression analysis localizes the failures to MCQ rows for Q-only and JSON-key/MCQ rows for V-only/K-only. A failure-aware diagnostic gate converts that into task-type-conditioned next candidates (`json_keys` -> Q-only, `mcq` -> K-only on stress-v3). This is useful negative evidence for calibration/task-split instability and for motivating stricter role/row protection; it is not a deployment claim.

## Claims Not Allowed Yet

- Do not claim end-to-end ESMP LLM runtime acceleration.
- Do not claim transparent quality preservation for fused QKV replacement; generated text changes for deeper/longer replacement and the six-prompt suite is negative on exact match and mean speed.
- Do not claim Tensor Core SOTA or GPTQ/AWQ superiority.
- Do not claim Redmi K80 Pro TTFT/tokens/s until measured on the phone.
- Do not claim Qwen3-1.7B has been fully ESMP-packed; only Qwen3-0.6B has the full package.
- Do not claim any layer-20 rowguard generalizes beyond the observed prompt splits; the held-out validation and split-consensus selector are negative for that claim.
- Do not claim group `3` is globally harmful. The held-out validation contradicts that broad claim.

## Next Experiments

1. Validate the failure-aware task-type policy on a fresh deterministic split or cached official-format MMLU/GSM8K/IFEval slices before using JSON/YAML/arithmetic rows as quality evidence.
2. Extend the continuous proxy across more layers/candidates if a new rowguard candidate appears promising.
3. Add a phone-side or NDK/OpenCL measurement path for Redmi K80 Pro once device access is available.
4. If C drive stays below 25 GB free, compact WSL VHD from elevated PowerShell before downloading more models.
5. Keep using CodeGraph CLI first in this running session; after a fresh Codex session, verify direct MCP tools are present.
6. Keep GPU guard at `--max-memory-ratio 0.90` unless Rui tightens the cap again.
