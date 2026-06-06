# Python Experiment And Evidence Tools

This directory contains the Python side of the current EigenSkill-Q research
pack. Treat these scripts as reproducibility and diagnostic tools for
calibration robustness, packed-artifact validation, and guarded prototype
runtime experiments.

The current paper-facing route is:

```text
calibration split instability -> consensus sensitivity allocation ->
fake-quant PPL/task diagnostics -> ESMP/Triton/C++ gated systems evidence
```

The older SmolLM2 multi-skill routing package is historical proof-of-concept
material only. Its v2 split had severe train/eval overlap and must not be used
as generalization evidence.

## Core Entry Points

| purpose | script |
|---|---|
| measure per-module loss sensitivity | `measure_module_quant_sensitivity.py` |
| build consensus allocations | `build_consensus_allocation.py` |
| build Lagrangian sensitivity allocations | `allocator.py` |
| evaluate fake weight-quant PPL | `eval_weight_quant_ppl.py` |
| build random/heuristic allocation baselines | `build_baseline_allocations.py` |
| aggregate calibration split instability | `build_calibration_instability_benchmark.py` |
| pack real ESMP mixed-precision artifacts | `pack_qwen3_consensus.py` |
| verify ESMP package integrity | `verify_esmp_package.py` |
| tune and gate Triton mixed GEMM | `tune_triton_blocks.py`, `gate_triton_tuning.py` |
| measure prototype generation paths | `measure_esmp_generation_latency.py` |
| build the paper-facing evidence ledger | `build_evidence_ledger.py` |
| gate public repo hygiene | `gate_public_repo_hygiene.py` |
| audit external baseline package availability | `audit_baseline_environment.py` |
| build baseline/readiness gap dashboard | `build_baseline_gap_dashboard.py` |

## Short Reproducibility Checks

Run unit tests:

```bash
python -m unittest discover -s train_python -p "test_*.py"
```

Gate public repository hygiene:

```bash
python train_python/gate_public_repo_hygiene.py \
  --out-json outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/PUBLIC_REPO_HYGIENE_GATE_2026_06_06.md
```

Build the calibration-instability benchmark:

```bash
python train_python/build_calibration_instability_benchmark.py \
  --case qwen3_0p6b=outputs/qwen3_0p6b_module_loss_sensitivity_limit4_group128.json=outputs/qwen3_0p6b_c4_module_loss_sensitivity_limit4_group128.json \
  --case qwen3_1p7b=outputs/qwen3_1p7b_module_loss_sensitivity_limit2_group128.json=outputs/qwen3_1p7b_module_loss_sensitivity_c4_limit2_group128.json \
  --case olmo2_1b=outputs/olmo2_0425_1b_module_loss_sensitivity_limit2_group128.json=outputs/olmo2_0425_1b_module_loss_sensitivity_c4_limit2_group128.json \
  --top-k 10,20,40 \
  --min-cases 3 \
  --min-unstable-cases 3 \
  --instability-spearman-threshold 0.30 \
  --instability-jaccard-threshold 0.55 \
  --out-json outputs/calibration_instability_benchmark_2026_06_06.json \
  --out-md outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md
```

Build the current evidence ledger:

```bash
python train_python/build_evidence_ledger.py \
  --gate public_hygiene=outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --gate calibration_instability=outputs/calibration_instability_benchmark_2026_06_06.json \
  --gate esmp_package=outputs/real_system_packer_2026-06-05/esmp_package_verify_qwen3_0p6b_limit8_2026_06_06.json \
  --gate triton_shape_family=outputs/real_system_packer_2026-06-05/triton_qwen_shape_family_gate_2026_06_06.json \
  --gate selector_runtime=outputs/real_system_packer_2026-06-05/selector_runtime_smoke_gate_2026_06_06.json \
  --gate selected_row=outputs/real_system_packer_2026-06-05/selected_row_benchmark_gate_2026_06_06.json \
  --gate cpp_runtime=outputs/real_system_packer_2026-06-05/cpp_runtime_sweep_gate_2026_06_06.json \
  --gate fused_sidecar=outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate_2026_06_06.json \
  --gate fused_qkv_speed=outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate_2026_06_06.json \
  --gate fused_qkv_quality=outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate_2026_06_06.json \
  --gate chat_task_stress=outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_gate_2026_06_06.json \
  --out-json outputs/real_system_packer_2026-06-05/evidence_ledger_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

Build the baseline/readiness gap dashboard:

```bash
python train_python/build_baseline_gap_dashboard.py \
  --manifest docs/BASELINE_COVERAGE_MANIFEST.json \
  --baseline-audit outputs/baseline_environment_audit.json \
  --out-json outputs/baseline_gap_dashboard_2026_06_06.json \
  --out-md outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md
```

## GPU Guard

Longer model runs should go through `run_with_gpu_guard.py`. The local working
policy is to keep peak VRAM below the configured guard threshold:

```bash
python train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.85 \
  --poll-seconds 0.5 \
  --out outputs/example_gpu_guard.json \
  -- \
  python train_python/eval_weight_quant_ppl.py --help
```

## Claim Boundaries

Valid claims from this directory are narrow:

- measured calibration split instability on the committed small-model cases;
- consensus allocation as a reproducible robustness baseline;
- fake-quant PPL/task diagnostics under explicit prompt slices;
- ESMP package integrity and prototype Triton/C++ runtime gates.

Invalid claims:

- no SOTA quantizer claim;
- no mobile/Redmi latency claim;
- no board-level power claim;
- no full Tensor Core transformer-runtime claim;
- no eigen-routing proof through nonlinear Transformer blocks.
