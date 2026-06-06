# C++ Evidence Tools

This directory contains standalone C++ tools used by the EigenSkill-Q research
pack. Treat them as reproducibility, packing, and microbenchmark artifacts. They
are not a full LLM inference runtime and do not depend on llama.cpp, RKNN,
ExecuTorch, or a mobile NPU SDK.

Current paper-facing role:

```text
measured sensitivity JSON
  -> C++ allocation / consensus / stability audits
  -> ESMPQ001 package checks and selected-row runtime probes
  -> evidence gates documented at docs/SYSTEM_EVIDENCE_GATES.md
```

## Contribution Tiers

Not every C++ executable has the same research weight. Use this tiering when
describing the repository publicly.

| Tier | Files / executables | What they support | What they do not support |
|---|---|---|---|
| Core system artifacts | `quant_kernels.cpp`, `esmp_format.cpp`, `mixed_precision_packer`, `mixed_precision_runtime_bench`, `esmp_inspect` | Mixed-bit packing, ESMPQ001 binary inspection, selected-row/module-level probes. | End-to-end LLM TTFT, tokens/s, mobile deployment, or production Tensor Core runtime. |
| Algorithm diagnostics | `quant_allocation_planner`, `quant_consensus_builder`, `quant_consensus_audit`, `quant_sensitivity_stability`, `quant_transfer_matrix`, `quant_policy_bypass` | Budget allocation, calibration-split stability checks, deterministic policy-field evaluation. | A new PTQ quantizer or faithful AWQ/GPTQ/QuaRot/Q-Palette implementation. |
| Reporting and guard summaries | `quant_result_summarizer`, `quant_evidence_matrix`, `quant_budget_curve_summary`, `quant_ppl_summary_merge`, `quant_random_baseline_audit`, `quant_seed_coverage_check`, `gpu_guard_summary`, `quant_task_eval_summary`, `quant_task_compare`, `quant_swap_search_summary`, `quant_chunked_eval_plan`, `baseline_install_probe` | Reproducibility, audit trails, result aggregation, and failure visibility. | Systems contribution by themselves. |

## Paper-Facing C++ Boundaries

| Area | Executables | Claim boundary |
|---|---|---|
| Quant-policy bypass | `quant_policy_bypass` | Deterministic decision-field evaluation for the no-leak v1 policy split. |
| Allocation planning | `quant_allocation_planner` | Budgeted `{4,8}` allocation from measured module sensitivity. |
| Consensus and stability audits | `quant_consensus_builder`, `quant_consensus_audit`, `quant_sensitivity_stability`, `quant_transfer_matrix` | Reproducible calibration-split diagnostics, not SOTA quantization. |
| ESMP package layer | `mixed_precision_packer`, `mixed_precision_runtime_bench`, `esmp_inspect` | Real mixed-bit binary packaging and module-level probes, not end-to-end deployment. |
| Kernel checks | `quant_kernel_verify`, `quant_kernel_bench` | Microbenchmark and correctness coverage for low-bit/selected-row paths. |

The historical `eigenskill_bench` low-rank benchmark remains available as a
best-case arithmetic sanity check. It should not be used as evidence for
nonlinear Transformer eigen-routing.

## Build

Windows/MSVC:

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1
```

Targeted Windows builds:

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1 -Target quant-policy
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1 -Target quant-kernel
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1 -Target quant-verify
```

WSL/Linux CMake:

```bash
cmake -S inference_cpp -B inference_cpp/build-wsl -DCMAKE_BUILD_TYPE=Release
cmake --build inference_cpp/build-wsl -j
ctest --test-dir inference_cpp/build-wsl --output-on-failure
```

## Minimal Checks

Deterministic policy bypass:

```bash
./inference_cpp/build-wsl/quant_policy_bypass \
  --data data_eval/eigenskill_quant_v1/eval.jsonl \
  --min-decision-exact 1.0 \
  --out outputs/eigenskill_quant_v1_eval_cpp_policy_summary.json
```

Quant-kernel verifier:

```bash
./inference_cpp/build-wsl/quant_kernel_verify --dim 512 --active-rows 32
```

ESMP package smoke:

```bash
./inference_cpp/build-wsl/mixed_precision_packer \
  --synthetic \
  --rows 64 \
  --cols 96 \
  --default-bits 4 \
  --sensitive-every 8 \
  --sensitive-bits 8 \
  --out build/cpp-wsl/mixed_precision_packer_smoke.esmp \
  --manifest-out build/cpp-wsl/mixed_precision_packer_smoke.json \
  --verify

./inference_cpp/build-wsl/esmp_inspect \
  --input build/cpp-wsl/mixed_precision_packer_smoke.esmp \
  --expect-rows 64 \
  --expect-cols 96 \
  --max-avg-bits 4.6 \
  --min-compression-vs-fp32 4.0 \
  --require-bits 4,8 \
  --verify-row-sums
```

## Important Non-Claims

- The scalar low-bit CPU path is not presented as an INT4 speedup result.
- The selected-row and ESMP tools are module-level evidence, not full TTFT or
  tokens/s deployment proof.
- The low-rank benchmark is historical and does not prove spectral routing
  through nonlinear Transformer layers.
- C++ report generators improve reproducibility; they are not themselves a
  systems contribution unless tied to executable gates and measured artifacts.

For the authoritative claim boundary, see `docs/PAPER_CLAIM_MATRIX.md`.
