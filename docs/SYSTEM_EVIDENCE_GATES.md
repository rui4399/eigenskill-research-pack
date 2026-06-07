# System Evidence Gates

This file is the short evidence map for the public artifact. It answers three
reviewer-facing questions:

1. Which results are paper-facing?
2. Which executable gate proves each result exists?
3. What can and cannot be claimed from that gate?

Detailed reproduction commands are intentionally moved to
`docs/SYSTEM_EVIDENCE_RUNBOOK.md`. Keep this file short enough to read before
opening the full command book.

## Current Ledger

Stable public entry point:

```bash
python train_python/build_current_evidence_ledger.py
```

Current ledger artifact:

```text
outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

Current status: **42 / 42 gates pass**.

Valid claim:

- the listed evidence artifacts passed their executable gates under the
  committed thresholds.

Invalid claim:

- the ledger proves SOTA quantization, official PTQ superiority, production
  Tensor Core runtime, mobile deployment, or full paper readiness.

## Gate Index

| gate | category | primary artifact | paper-facing claim boundary |
|---|---|---|---|
| `public_hygiene` | repo hygiene | `outputs/real_system_packer_2026-06-05/PUBLIC_REPO_HYGIENE_GATE_2026_06_06.md` | Public tree excludes private/process artifacts, generated delivery bundles, blank placeholders, stale positioning, root clutter, and risky root README terms. |
| `paper_evidence_alignment` | paper alignment | `outputs/PAPER_EVIDENCE_ALIGNMENT_GATE_2026_06_07.md` | Current paper draft cites required evidence and avoids unsafe non-negated high-risk claims. |
| `calibration_instability` | calibration robustness | `outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md` | Small calibration splits induce unstable module-sensitivity rankings in the measured model/dataset cases. |
| `sensitivity_perturbation_matrix` | calibration robustness | `outputs/SENSITIVITY_PERTURBATION_MATRIX_QWEN25_2026_06_07.md` | Qwen2.5 sensitivity rankings are more stable under within-model calibration sample-size changes than under cross-model-scale transfer; this is not downstream quality evidence. |
| `calibration_seed_stability` | calibration robustness | `outputs/CALIBRATION_SEED_STABILITY_QWEN25_0P5B_2026_06_07.md` | Qwen2.5-0.5B deterministic six-seed prompt-sensitivity runs over the same 16-prompt pool show moderate mean rank agreement with pair-bootstrap CIs but drifting top-sensitive module sets; this is not quality-retention or deployment evidence. |
| `csi_vs_n_curve` | calibration robustness | `outputs/CSI_VS_N_CURVE_QWEN25_0P5B_2026_06_07.md` | Qwen2.5-0.5B six-seed sensitivity gates at n=2, n=4, and n=8 show monotonic stability gains in mean Spearman, top-20 Jaccard, and positive-set Jaccard; this is local calibration-size evidence, not a universal scaling law. |
| `csi_trend_significance` | calibration robustness | `outputs/CSI_TREND_SIGNIFICANCE_QWEN25_0P5B_2026_06_07.md` | Independent bootstrap trend checks show positive n=8-vs-n=2 mean-gain CIs for all audited CSI stability metrics and minimum random pair dominance probability 0.9422; this is local trend evidence, not a universal scaling law. |
| `csi_null_permutation` | calibration robustness | `outputs/CSI_NULL_PERMUTATION_QWEN25_0P5B_2026_06_07.md` | Monte-Carlo label-shuffle permutation tests over pooled n=2/n=8 seed-pair metrics give max Holm-adjusted p-value 0.00015 for the audited stability gains; this is local null-test evidence, not downstream retention. |
| `rank_inversion_theory` | theory | `outputs/RANK_INVERSION_THEORY_QWEN25_0P5B_2026_06_07.md` | A Chebyshev-style plug-in rank-inversion analysis over the same Qwen2.5 seed artifacts shows decreasing empirical inversion risk and variance/gap^2 bound proxies from n=2 to n=8; this is not a tight-bound proof. |
| `calibration_robustness_stress` | calibration robustness | `outputs/CALIBRATION_ROBUSTNESS_STRESS_GATE_2026_06_07.md` | Current target policies beat uniform INT4, best random seed, and random mean across committed short fake-quant PPL slices. |
| `consensus_transfer_boundary` | allocation boundary | `outputs/CONSENSUS_TRANSFER_BOUNDARY_GATE_2026_06_07.md` | Consensus avoids the worse single-split policy on paired Qwen3 transfer slices with bounded best-single regret. |
| `interaction_swap_boundary` | allocation boundary | `outputs/INTERACTION_SWAP_BOUNDARY_GATE_2026_06_07.md` | Bounded global-feedback swap search exposes interaction effects beyond additive module ranking. |
| `allocation_family_proxy` | comparator proxy | `outputs/Q_PALETTE_STYLE_ALLOCATION_FAMILY_GATE_2026_06_06.md` | A Q-Palette-style closed-form Lagrangian allocation proxy is executable on measured Qwen3 and Qwen2.5 sensitivity artifacts, with 6 cases, 1126 records, finite lambdas, and strict budget checks. |
| `robust_lcb_consensus` | allocation proxy | `outputs/ROBUST_LCB_CONSENSUS_FAMILY_GATE_2026_06_06.md` | Robust-LCB consensus allocation artifacts are budget-respecting across the current measured model family. |
| `robust_lcb_quality` | quality boundary | `outputs/QWEN3_0P6B_ROBUST_LCB_QUALITY_GATE_2026_06_07.md` | Robust-LCB beats uniform INT4 on two guarded Qwen3-0.6B PPL slices, but not mean consensus. |
| `rotation_family_proxy` | comparator proxy | `outputs/QUAROT_SPINQUANT_ROTATION_FAMILY_GATE_2026_06_06.md` | A QuaRot/SpinQuant-style rotation-family proxy is executable; it is not a faithful rotation implementation. |
| `awq_gptq_proxy` | comparator proxy | `outputs/AWQ_GPTQ_PROXY_GATE_2026_06_06.md` | AWQ/GPTQ-style proxy policies are executable; this is not an official AWQ/GPTQ run. |
| `public_task_benchmark` | public task coverage | `outputs/PUBLIC_TASK_BENCHMARK_OLLAMA_QWEN25_ABLITERATE_7B_GATE_2026_06_07.md` | A local Ollama 7B model ran 100 MMLU/GSM8K subset rows under GPU guard. |
| `public_task_model_ladder` | public task coverage | `outputs/PUBLIC_TASK_MODEL_LADDER_GATE_2026_06_07.md` | Public-task evidence is shown as a guarded two-model ladder, not a single cherry-picked result. |
| `official_ptq_task_retention` | task execution smoke | `outputs/OFFICIAL_PTQ_TASK_RETENTION_SMOKE_MATRIX_2026_06_07.md` | FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants load and run the same tiny public MMLU/GSM8K smoke tasks under GPU guard; this is not leaderboard-scale retention, and zero-FP16 formats are execution-only. |
| `official_ptq_runtime_profile` | runtime profile | `outputs/OFFICIAL_PTQ_RUNTIME_PROFILE_2026_06_07.md` | PC-side TTFT/tokens/s/VRAM are summarized from the same guarded official PTQ task-smoke path; this is not mobile deployment or production runtime speedup. |
| `official_ptq_task_subset50` | task execution subset | `outputs/OFFICIAL_PTQ_TASK_SUBSET50_MATRIX_2026_06_07.md` | FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants run the same 50-row public MMLU and 50-row public GSM8K subsets under GPU guard; GSM8K remains execution-only because FP16 is 0/50. |
| `official_ptq_subset50_runtime_profile` | runtime profile | `outputs/OFFICIAL_PTQ_SUBSET50_RUNTIME_PROFILE_2026_06_07.md` | PC-side TTFT/tokens/s/VRAM are summarized from the 300-task subset50 matrix; the quantized packages use less VRAM but are slower than FP16 on this local Transformers/GPTQModel path. |
| `official_ptq_task_subset100` | task execution subset | `outputs/OFFICIAL_PTQ_TASK_SUBSET100_MATRIX_2026_06_07.md` | FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants run the same true 100-row public MMLU and 100-row public GSM8K subsets under GPU guard; max drop versus FP16 is 0.03, but this remains local subset evidence. |
| `official_ptq_subset100_runtime_profile` | runtime profile | `outputs/OFFICIAL_PTQ_SUBSET100_RUNTIME_PROFILE_2026_06_07.md` | PC-side TTFT/tokens/s/VRAM are summarized from the 600-task subset100 matrix; quantized packages use less guarded VRAM but remain slower than FP16 on this local package-loader path. |
| `official_ptq_ifeval_v2` | task execution smoke | `outputs/OFFICIAL_PTQ_TASK_IFEVAL_V2_MATRIX_2026_06_07.md` | FP16, AutoAWQ, and GPTQModel Qwen2.5-0.5B variants run the same deterministic IFEval-style instruction-following tasks under GPU guard; the FP16 baseline is 0/8, so this is execution-path evidence rather than task-retention evidence. |
| `official_ptq_ifeval_v2_runtime_profile` | runtime profile | `outputs/OFFICIAL_PTQ_RUNTIME_IFEVAL_V2_PROFILE_2026_06_07.md` | PC-side TTFT/tokens/s/VRAM are summarized from the IFEval-style matrix; quantized paths reduce guarded VRAM in this run but this is not a production speed or mobile claim. |
| `official_ptq_matched_baseline_pack` | matched PTQ baseline | `outputs/OFFICIAL_PTQ_MATCHED_BASELINE_PACK_QWEN25_0P5B_2026_06_07.md` | AutoAWQ/GPTQModel Qwen2.5-0.5B W4/G128 public-calibration PPL, subset50 task, and subset50 runtime evidence are cited together with explicit local-only and no-speedup boundaries. |
| `official_awq_public_calib_16_eval` | official PTQ readiness | `outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_BUNDLE_16_GATE_2026_06_07.md` | The public-calibrated AutoAWQ W4 group-128 Qwen2.5-0.5B bundle is re-evaluated on 16 WikiText2 prompts and 16 C4 prompts, totaling 2857 PPL tokens with max PPL ratio 1.2114; this is expanded local readiness evidence, not a complete AWQ/GPTQ baseline. |
| `official_awq_public_calib_1p5b_16_eval` | official PTQ readiness | `outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_1P5B_BUNDLE_16_GATE_2026_06_07.md` | A public-calibrated AutoAWQ W4 group-128 Qwen2.5-1.5B artifact is quantized under an 85% VRAM guard and evaluated on 16 WikiText2 plus 16 C4 prompts, totaling 2857 PPL tokens with max PPL ratio 1.1344; this is a scale-up readiness smoke, not a complete AWQ/GPTQ baseline or speed claim. |
| `official_ptq_task_qwen25_1p5b_subset100` | task execution subset | `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_SUBSET100_MATRIX_2026_06_07.md` | FP16 and AutoAWQ Qwen2.5-1.5B variants run matched 100-row public MMLU/GSM8K task subsets under GPU guard; max drop versus FP16 is 0.01 and peak guard VRAM ratio is 0.8013, but this remains local subset evidence. |
| `official_ptq_qwen25_1p5b_subset100_runtime_profile` | runtime profile | `outputs/OFFICIAL_PTQ_QWEN25_1P5B_SUBSET100_RUNTIME_PROFILE_2026_06_07.md` | PC-side TTFT/tokens/s/VRAM are summarized from the 400-task Qwen2.5-1.5B subset100 matrix; AutoAWQ uses less peak guarded VRAM than FP16 but is slower on this local loader path. |
| `esmp_package` | artifact integrity | `outputs/real_system_packer_2026-06-05/ESMP_PACKAGE_VERIFY_QWEN3_0P6B_LIMIT8_2026_06_06.md` | ESMP package metadata, manifest, and binary headers are independently checkable. |
| `triton_shape_family` | kernel | `outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_FAMILY_GATE_2026_06_06.md` | Tuned grouped packed INT4/INT8 Triton kernels can beat torch FP16 on selected measured shapes. |
| `w4a8_activation_reconstruction` | module reconstruction | `outputs/w4a8_activation_reconstruction_2026_06_08/W4A8_ACTIVATION_RECONSTRUCTION_GATE.md` | Selected real Qwen3 self-attention module activations have bounded added drift from A8 activation quantization; this is not full-model quality retention or end-to-end speed evidence. |
| `selector_runtime` | runtime wiring | `outputs/real_system_packer_2026-06-05/SELECTOR_RUNTIME_SMOKE_GATE_2026_06_06.md` | Selector-driven runtime wiring loads measured kernel configs and records selector calls. |
| `selected_row` | selected-row routing | `outputs/real_system_packer_2026-06-05/SELECTED_ROW_BENCHMARK_GATE_2026_06_06.md` | Selected-row routing can reduce module-level work when the active row set is small. |
| `cpp_runtime` | C++ runtime | `outputs/real_system_packer_2026-06-05/CPP_RUNTIME_SWEEP_GATE_2026_06_06.md` | C++ ESMP selected-row sweep supports module-level bypass/runtime claims only. |
| `fused_sidecar` | decode integration | `outputs/real_system_packer_2026-06-05/FUSED_SIDECAR_GENERATION_GATE_2026_06_06.md` | Fused selected-row sidecars execute in the HF generation loop with bounded additive overhead. |
| `fused_qkv_speed` | QKV replacement smoke | `outputs/real_system_packer_2026-06-05/FUSED_QKV_GENERATION_GATE_2026_06_06.md` | A shallow fused packed QKV replacement has guarded smoke-level speed/memory evidence. |
| `fused_qkv_quality` | QKV quality smoke | `outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_GATE_2026_06_06.md` | A conservative QKV8 repack candidate preserves a six-prompt suite under a quality gate. |
| `chat_task_stress` | deterministic task retention | `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_GATE_2026_06_06.md` | The selected K-only candidate survives an 84-task deterministic stress suite with one allowed regression. |

## Non-Ledger Readiness Probes

These probes are tracked because they reduce environment uncertainty, but they
are not counted in the current 42-gate paper-facing ledger.

| probe | category | primary artifact | boundary |
|---|---|---|---|
| `official_awq_smoke` | external PTQ readiness | `outputs/OFFICIAL_AWQ_SMOKE_GATE_2026_06_07.md` | AutoAWQ 0.2.9 can quantize and save a tiny Qwen2.5-0.5B artifact under guard; this is not a matched AWQ/GPTQ baseline or quality-retention result. |
| `official_awq_matched_ppl` | external PTQ readiness | `outputs/OFFICIAL_AWQ_MATCHED_PPL_GATE_2026_06_07.md` | The same four-prompt slice can be evaluated under FP16 and local AutoAWQ W4 group-128 with PPL ratio 1.1789; this is not a full public-dataset AWQ/GPTQ baseline. |
| `official_awq_public_wikitext2_ppl` | external PTQ readiness | `outputs/OFFICIAL_AWQ_MATCHED_PPL_QWEN25_0P5B_WIKITEXT2_GATE_2026_06_07.md` | A tiny public WikiText2 slice runs under FP16 and local AutoAWQ W4 group-128 with PPL ratio 1.2705 over 760 tokens; this is not a complete AWQ/GPTQ baseline. |
| `official_awq_public_c4_ppl` | external PTQ readiness | `outputs/OFFICIAL_AWQ_MATCHED_PPL_QWEN25_0P5B_C4_GATE_2026_06_07.md` | A tiny public C4 validation slice runs under FP16 and local AutoAWQ W4 group-128 with PPL ratio 1.1824 over 727 tokens; this is not a complete AWQ/GPTQ baseline. |
| `official_awq_public_calib_bundle` | external PTQ readiness | `outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_BUNDLE_GATE_2026_06_07.md` | A public-calibration AutoAWQ W4 group-128 bundle quantizes under guard and evaluates tiny public WikiText2/C4 PPL slices; this is partial official-package evidence, not GPTQ/AWQ competitive coverage. |
| `official_gptqmodel_public_calib_smoke` | external PTQ readiness | `outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_BUDGET8_GATE_2026_06_07.md` | A public-calibration GPTQModel W4 group-128 gate quantizes under guard with 12 public calibration texts, saves/reloads a local artifact with `gptq_torch`, and evaluates tiny public WikiText2/C4 PPL slices; this is partial official-package evidence, not GPTQ/AWQ competitive coverage. |
| `official_gptqmodel_public_calib_16_eval` | external PTQ readiness | `outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_BUDGET8_16_GATE_2026_06_07.md` | The same public-calibrated GPTQModel W4 group-128 artifact is re-evaluated on 16 WikiText2 prompts and 16 C4 prompts, totaling 2857 PPL tokens with max PPL ratio 1.2570; this is expanded local readiness evidence, not a complete GPTQ/AWQ baseline. |
| `official_ptq_readiness_matrix` | external PTQ readiness | `outputs/OFFICIAL_PTQ_READINESS_MATRIX_QWEN25_0P5B_2026_06_07.md` | AutoAWQ and GPTQModel readiness probes are normalized into one matrix over the same model, W4/G128 shape, WikiText2/C4 eval labels, and 2857-token public eval budget per package; this is presentation hygiene, not a faithful competitive baseline. |
| `official_ptq_task_qwen25_1p5b_subset20` | task execution subset | `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_SUBSET20_MATRIX_2026_06_07.md` | FP16 and AutoAWQ Qwen2.5-1.5B variants run matched 20-row public MMLU/GSM8K task subsets under GPU guard; this is scale-up task-path evidence, not leaderboard-scale retention or SOTA PTQ. |

## Readiness Gaps

The following remain explicit non-claims:

- official matched GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant baselines are not
  faithfully reproduced; current AWQ/GPTQ smoke/matched-PPL/proxy, rotation
  proxy, and allocation proxy artifacts are diagnostics, and the baseline dashboard keeps
  them separate from official competitive coverage;
- no Redmi K80 Pro or board-level TTFT, tokens/s, energy, thermal, or physical
  memory evidence is complete;
- no production Tensor Core or mobile LLM runtime is claimed;
- public task evidence is local subset coverage, not leaderboard-scale
  capability retention;
- spectral/eigen routing through nonlinear Transformer blocks remains outside
  the current evidence boundary.

For the tracked gap dashboard, see:

```text
outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md
```

## Command Runbook

Use the runbook when reproducing a gate or auditing thresholds:

```text
docs/SYSTEM_EVIDENCE_RUNBOOK.md
```

Do not copy long gate commands back into the README or paper unless a reviewer
specifically asks for the expanded form.
