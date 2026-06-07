# Artifact Manifest

This file keeps the public repository navigable while the committed `outputs/`
tree is still used as the reproducibility boundary. It is intentionally a map,
not a new result.

Current tracked output footprint:

```text
outputs/ tracked-or-staged artifact files:       1489
outputs/real_system_packer_2026-06-05 files:     744
```

## Paper-Facing Artifacts

These are the first files a reader should inspect when checking the current
paper claims.

| Purpose | Artifact |
|---|---|
| Documentation map | `docs/README.md` |
| Top-level gate ledger | `outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md` |
| Calibration split instability benchmark | `outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md` |
| Sensitivity perturbation matrix | `outputs/SENSITIVITY_PERTURBATION_MATRIX_QWEN25_2026_06_07.md` |
| Calibration robustness stress gate | `outputs/CALIBRATION_ROBUSTNESS_STRESS_GATE_2026_06_07.md` |
| Consensus transfer boundary gate | `outputs/CONSENSUS_TRANSFER_BOUNDARY_GATE_2026_06_07.md` |
| Interaction-aware swap boundary gate | `outputs/INTERACTION_SWAP_BOUNDARY_GATE_2026_06_07.md` |
| Paper evidence alignment gate | `outputs/PAPER_EVIDENCE_ALIGNMENT_GATE_2026_06_07.md` |
| Mean consensus evidence matrix | `outputs/cross_model_quant_evidence_matrix_extended_auto.md` |
| Robust-LCB allocation gate | `outputs/ROBUST_LCB_CONSENSUS_FAMILY_GATE_2026_06_06.md` |
| Robust-LCB downstream boundary gate | `outputs/QWEN3_0P6B_ROBUST_LCB_QUALITY_GATE_2026_06_07.md` |
| Public task benchmark gate | `outputs/PUBLIC_TASK_BENCHMARK_OLLAMA_QWEN25_ABLITERATE_7B_GATE_2026_06_07.md` |
| Public task model ladder gate | `outputs/PUBLIC_TASK_MODEL_LADDER_GATE_2026_06_07.md` |
| Official PTQ task-execution smoke matrix | `outputs/OFFICIAL_PTQ_TASK_RETENTION_SMOKE_MATRIX_2026_06_07.md` |
| Official PTQ PC-side runtime profile | `outputs/OFFICIAL_PTQ_RUNTIME_PROFILE_2026_06_07.md` |
| Official PTQ matched subset50 matrix | `outputs/OFFICIAL_PTQ_TASK_SUBSET50_MATRIX_2026_06_07.md` |
| Official PTQ subset50 runtime profile | `outputs/OFFICIAL_PTQ_SUBSET50_RUNTIME_PROFILE_2026_06_07.md` |
| Official PTQ matched baseline pack | `outputs/OFFICIAL_PTQ_MATCHED_BASELINE_PACK_QWEN25_0P5B_2026_06_07.md` |
| Baseline/readiness gap dashboard | `outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md` |
| Claim matrix | `docs/PAPER_CLAIM_MATRIX.md` |
| System gate index | `docs/SYSTEM_EVIDENCE_GATES.md` |
| System gate command runbook | `docs/SYSTEM_EVIDENCE_RUNBOOK.md` |
| Current research draft | `paper_drafts/eigenskill_q_research_draft_en_2026_06_07.md` |

## Non-Ledger Readiness Probes

These artifacts are useful for environment readiness and reviewer-risk
tracking, but they are not counted in the 28-gate paper-facing ledger.

| Purpose | Artifact | Boundary |
|---|---|---|
| Minimal AutoAWQ package smoke | `outputs/OFFICIAL_AWQ_SMOKE_GATE_2026_06_07.md` | Shows AutoAWQ can quantize and save a tiny local Qwen2.5-0.5B artifact under guard; not a matched AWQ baseline or quality-retention result. |
| Minimal AutoAWQ matched PPL probe | `outputs/OFFICIAL_AWQ_MATCHED_PPL_GATE_2026_06_07.md` | Shows same-prompt FP16-vs-AutoAWQ PPL can run under guard; not a full public-dataset AWQ/GPTQ baseline. |
| Tiny public WikiText2 AutoAWQ PPL probe | `outputs/OFFICIAL_AWQ_MATCHED_PPL_QWEN25_0P5B_WIKITEXT2_GATE_2026_06_07.md` | Shows same-slice FP16-vs-AutoAWQ PPL can run on 8 public WikiText2 prompts under guard; not a full baseline. |
| Tiny public C4 AutoAWQ PPL probe | `outputs/OFFICIAL_AWQ_MATCHED_PPL_QWEN25_0P5B_C4_GATE_2026_06_07.md` | Shows same-slice FP16-vs-AutoAWQ PPL can run on 8 public C4 validation prompts under guard; not a full baseline. |
| Public PPL prompt manifest | `outputs/PUBLIC_PPL_PROMPT_MANIFEST_2026_06_07.md` | Records the tiny public prompt files used by the readiness probes; not a benchmark definition. |
| Public-calibration AutoAWQ bundle gate | `outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_BUNDLE_GATE_2026_06_07.md` | Shows a public-calibrated AutoAWQ W4 group-128 bundle can quantize and run two tiny public PPL eval slices under guard; not GPTQ/AWQ competitive coverage. |
| Public-calibration GPTQModel readiness gate | `outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_BUDGET8_GATE_2026_06_07.md` | Shows GPTQModel W4 group-128 can quantize with 12 public calibration texts, save/reload a local artifact through `gptq_torch`, and run tiny public WikiText2/C4 PPL diagnostics under guard at the same eval token budget as AutoAWQ; not GPTQ/AWQ competitive coverage. |
| Official PTQ readiness matrix | `outputs/OFFICIAL_PTQ_READINESS_MATRIX_QWEN25_0P5B_2026_06_07.md` | Shows AutoAWQ and GPTQModel readiness probes are aligned on model, W4/G128 shape, WikiText2/C4 eval labels, and 1487-token public eval budget per package; not a faithful AWQ/GPTQ competition. |
| Public calibration prompt manifest | `outputs/PUBLIC_CALIB_PROMPT_MANIFEST_2026_06_07.md` | Records the tiny public calibration prompt files; not an evaluation benchmark. |

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

Internal delivery/update notes, wake-up summaries, Notion-ready snippets, and
the old cross-medium swarm concept draft were removed from the tracked artifact
tree because they are process state rather than reproducible evidence.

Reader rule: do not start from the `outputs/` root. Start from
`docs/README.md`, then the claim matrix, then the specific gate artifact.

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
28-gate reproducibility story.
