# Artifact Manifest

This file keeps the public repository navigable while the committed `outputs/`
tree is still used as the reproducibility boundary. It is intentionally a map,
not a new result.

Current tracked output footprint:

```text
outputs/ tracked files:                         1365
outputs/real_system_packer_2026-06-05 files:     745
```

## Paper-Facing Artifacts

These are the first files a reader should inspect when checking the current
paper claims.

| Purpose | Artifact |
|---|---|
| Top-level gate ledger | `outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md` |
| Calibration split instability benchmark | `outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md` |
| Calibration robustness stress gate | `outputs/CALIBRATION_ROBUSTNESS_STRESS_GATE_2026_06_07.md` |
| Consensus transfer boundary gate | `outputs/CONSENSUS_TRANSFER_BOUNDARY_GATE_2026_06_07.md` |
| Mean consensus evidence matrix | `outputs/cross_model_quant_evidence_matrix_extended_auto.md` |
| Robust-LCB allocation gate | `outputs/ROBUST_LCB_CONSENSUS_FAMILY_GATE_2026_06_06.md` |
| Robust-LCB downstream boundary gate | `outputs/QWEN3_0P6B_ROBUST_LCB_QUALITY_GATE_2026_06_07.md` |
| Baseline/readiness gap dashboard | `outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md` |
| Claim matrix | `docs/PAPER_CLAIM_MATRIX.md` |
| System gate command book | `docs/SYSTEM_EVIDENCE_GATES.md` |

## Supporting System Artifacts

These support the systems-prototype side. They should be cited only with the
scope stated in the claim matrix.

| Purpose | Representative artifacts |
|---|---|
| ESMP package integrity | `outputs/real_system_packer_2026-06-05/ESMP_PACKAGE_VERIFY_QWEN3_0P6B_LIMIT8_2026_06_06.md` |
| Triton shape-family tuning gate | `outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_FAMILY_GATE_2026_06_06.md` |
| Triton selector gate | `outputs/real_system_packer_2026-06-05/SELECTOR_RUNTIME_SMOKE_GATE_2026_06_06.md` |
| Selected-row benchmark gate | `outputs/real_system_packer_2026-06-05/SELECTED_ROW_BENCHMARK_GATE_2026_06_06.md` |
| C++ runtime sweep gate | `outputs/real_system_packer_2026-06-05/CPP_RUNTIME_SWEEP_GATE_2026_06_06.md` |
| Fused sidecar generation gate | `outputs/real_system_packer_2026-06-05/FUSED_SIDECAR_GENERATION_GATE_2026_06_06.md` |
| Fused QKV speed smoke gate | `outputs/real_system_packer_2026-06-05/FUSED_QKV_GENERATION_GATE_2026_06_06.md` |
| Fused QKV prompt-suite quality gate | `outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_GATE_2026_06_06.md` |
| Chat-task stress gate | `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_GATE_2026_06_06.md` |

## Historical Or Non-Paper Artifacts

These files are retained for reproducibility or project history, but they should
not be cited as current paper evidence without an explicit claim-matrix row.

- old v2 skill-routing outputs with known train/eval leakage;
- early SmolLM2 LoRA smoke outputs;
- intermediate random-seed summaries that feed a later evidence matrix;
- raw GPU guard logs when a corresponding gate already summarizes them;
- speculative material described in `docs/HISTORICAL_ARTIFACTS.md`.

## Cleanup Policy

Do not delete committed outputs only because the tree is large. First make sure
one of the following is true:

1. The artifact is superseded by a paper-facing gate and no command references
   the old path.
2. The artifact is moved to a release bundle with a stable checksum.
3. The artifact is explicitly marked historical and removed from README,
   claim-matrix, and gate-ledger dependencies.

Future cleanup should reduce `outputs/` by moving scratch and raw intermediate
files out of the main branch, but not at the cost of breaking the current
19-gate reproducibility story.
