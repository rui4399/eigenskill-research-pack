# EigenSkill-Q Research Pack

Public repository: https://github.com/rui4399/eigenskill-research-pack

EigenSkill-Q is a reproducible research pack for **calibration robustness in
mixed-precision LLM quantization** plus a small set of packed-runtime system
prototypes. The current repository is not presented as a production quantizer,
a SOTA PTQ implementation, or a completed edge-device runtime.

The defensible research question is:

```text
How unstable are module sensitivity rankings across small calibration splits,
and can cross-split allocation policies preserve fake-quant quality better
than uniform or random mixed-precision allocations under the same bit budget?
```

## Current Status

The paper-facing evidence set is indexed by executable gates. The current
ledger passes **18/18 gates**:

- calibration split instability across Qwen3-0.6B, Qwen3-1.7B, and OLMo2-1B;
- calibration-robustness stress evidence across 11 committed fake-quant PPL
  slices;
- consensus and robust-LCB allocation artifacts under a 4.5 average-bit budget;
- guarded Qwen3-0.6B downstream PPL boundary evidence for robust-LCB;
- Q-Palette, AWQ/GPTQ, and QuaRot/SpinQuant-style proxy comparator coverage;
- ESMP package-integrity checks;
- Triton kernel tuning, selected-row, sidecar, and shallow fused-QKV runtime
  gates;
- public-task and chat-task retention smoke gates;
- public repository hygiene checks.

Authoritative ledger:

```text
outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

Claim boundaries:

```text
docs/PAPER_CLAIM_MATRIX.md
docs/SYSTEM_EVIDENCE_GATES.md
docs/ARTIFACT_MANIFEST.md
docs/BASELINE_COVERAGE_MANIFEST.json
outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md
```

## Key Results

### Calibration Split Instability

The benchmark aggregates WikiText2-vs-C4 module-sensitivity comparisons across
three small model families.

```text
cases:                    3 / 3 unstable
mean score/cost Spearman: 0.0713
mean positive-set Jaccard: 0.4349
mean top-20 Jaccard:      0.1022
bootstrap Spearman CI:    [-0.0440, 0.1845]
```

Evidence:

```text
outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md
```

### Mean Consensus Allocation

The strongest current allocation result is still the mean cross-split
consensus policy. On short fake-quant PPL slices, it beats uniform INT4 and
random mixed-precision baselines under the same average-bit budget.

```text
Qwen3-0.6B, group size 128, average 4.5 bits
WikiText2-64 len96:
  FP16 PPL                         33.9865
  uniform INT4 PPL                 54.6542
  mean consensus PPL               45.6559
  random_seed min/mean/max PPL     48.5030 / 50.4787 / 52.6347

C4-64:
  FP16 PPL                         36.1380
  uniform INT4 PPL                 52.9352
  mean consensus PPL               44.9290
  random_seed min/mean/max PPL     48.3840 / 49.4427 / 50.7971
```

Cross-model summaries:

```text
outputs/cross_model_quant_evidence_matrix_extended_auto.md
```

### Calibration Robustness Stress

The stress gate converts the committed PPL summaries into a machine-checkable
risk table over 11 short fake-quant slices. It measures whether the selected
target policy beats uniform INT4, the best random mixed-precision seed, and the
random mean under the same budget.

```text
cases:                         11
wins vs uniform INT4:          11 / 11
wins vs best random seed:      11 / 11
wins vs random-seed mean:      11 / 11
mean margin vs uniform:        +4.2942 PPL
worst margin vs best random:   +0.1120 PPL
mean FP16 regret:              +4.1683 PPL
```

Evidence:

```text
outputs/CALIBRATION_ROBUSTNESS_STRESS_GATE_2026_06_07.md
```

### Robust-LCB Boundary Evidence

Robust-LCB discounts one-sided calibration spikes. It is useful as a conservative
allocation candidate, but the current downstream evidence is deliberately
reported as a boundary result rather than a win over mean consensus.

```text
Qwen3-0.6B robust-LCB quality gate
cases:                  2
wins vs uniform INT4:   2 / 2
wins vs mean consensus: 0 / 2
mean margin vs uniform: +5.6188 PPL
mean margin vs mean:    -2.8834 PPL
max guard VRAM ratio:   0.7032
```

Evidence:

```text
outputs/QWEN3_0P6B_ROBUST_LCB_QUALITY_GATE_2026_06_07.md
outputs/ROBUST_LCB_CONSENSUS_FAMILY_GATE_2026_06_06.md
```

### Packed-System Evidence

The system side is a prototype, not a complete runtime. Current evidence is
split by gate:

- ESMPQ001 package format integrity and manifest/header checks;
- Triton packed INT4/INT8 kernel tuning for selected shapes;
- selected-row module-level runtime wins;
- fused sidecar execution inside HF generation with bounded overhead;
- shallow fused-QKV replacement smoke with cache-invariant checks;
- prompt-suite quality and chat-task stress gates for narrow retention checks.

Main index:

```text
docs/SYSTEM_EVIDENCE_GATES.md
```

## Not Claimed

This repository currently does **not** claim:

- SOTA quantization quality;
- faithful official GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant reproduction;
- real Redmi K80 Pro or board-level latency/energy evidence;
- production Tensor Core LLM runtime readiness;
- full-model quality-preserving fused generation;
- proof that spectral/eigen routing survives nonlinear Transformer blocks;
- that the old leaked v2 routing result demonstrates generalization.

## Repository Layout

```text
train_python/          Measurement, fake-quant evaluation, gates, summaries
inference_cpp/         C++ policy/runtime tools and ESMP utilities
mobile/redmi_k80_pro/  ADB metric harness and NEON decode prototype
data_eval/             Prompt slices and eval configs
docs/                  Claim matrix, evidence gates, related work, readiness
outputs/               Committed evidence artifacts used by the ledger
```

The large `outputs/` tree is intentional for now because the evidence ledger
links directly to committed artifacts. Future cleanup should move non-paper
historical outputs into a manifest or release artifact without breaking
reproducibility.

Artifact navigation:

```text
docs/ARTIFACT_MANIFEST.md
```

## Quick Verification

Run the unit tests:

```bash
python -m unittest discover -s train_python -p "test_*.py"
```

Run the public hygiene gate:

```bash
python train_python/gate_public_repo_hygiene.py \
  --out-json outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/PUBLIC_REPO_HYGIENE_GATE_2026_06_06.md
```

Rebuild the evidence ledger:

```bash
python train_python/build_evidence_ledger.py \
  --gate public_hygiene=outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --gate calibration_instability=outputs/calibration_instability_benchmark_2026_06_06.json \
  --gate calibration_robustness_stress=outputs/calibration_robustness_stress_gate_2026_06_07.json \
  --gate esmp_package=outputs/real_system_packer_2026-06-05/esmp_package_verify_qwen3_0p6b_limit8_2026_06_06.json \
  --gate triton_shape_family=outputs/real_system_packer_2026-06-05/triton_qwen_shape_family_gate_2026_06_06.json \
  --gate selector_runtime=outputs/real_system_packer_2026-06-05/selector_runtime_smoke_gate_2026_06_06.json \
  --gate selected_row=outputs/real_system_packer_2026-06-05/selected_row_benchmark_gate_2026_06_06.json \
  --gate cpp_runtime=outputs/real_system_packer_2026-06-05/cpp_runtime_sweep_gate_2026_06_06.json \
  --gate fused_sidecar=outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate_2026_06_06.json \
  --gate fused_qkv_speed=outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate_2026_06_06.json \
  --gate fused_qkv_quality=outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate_2026_06_06.json \
  --gate chat_task_stress=outputs/real_system_packer_2026-06-05/chat_task_stress_v3_84_gate_2026_06_06.json \
  --gate public_task_benchmark=outputs/public_task_benchmark_ollama_qwen35_4b_gate_2026_06_06.json \
  --gate allocation_family_proxy=outputs/q_palette_style_allocation_family_gate_2026_06_06.json \
  --gate robust_lcb_consensus=outputs/robust_lcb_consensus_family_gate_2026_06_06.json \
  --gate robust_lcb_quality=outputs/qwen3_0p6b_robust_lcb_quality_gate_2026_06_07.json \
  --gate rotation_family_proxy=outputs/quarot_spinquant_rotation_family_gate_2026_06_06.json \
  --gate awq_gptq_proxy=outputs/awq_gptq_proxy_gate_2026_06_06.json \
  --out-json outputs/real_system_packer_2026-06-05/evidence_ledger_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

## Paper Direction

The best current framing is:

```text
Calibration Split Instability in Mixed-Precision LLM Quantization:
Consensus Sensitivity Allocation with Gated Packed-System Evidence
```

This is narrower than the original EigenSkill vision, but it is reviewable:
it defines a measurable robustness problem, provides allocation responses, and
keeps system claims behind executable gates.
