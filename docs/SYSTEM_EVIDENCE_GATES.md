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

Current status: **22 / 22 gates pass**.

Valid claim:

- the listed evidence artifacts passed their executable gates under the
  committed thresholds.

Invalid claim:

- the ledger proves SOTA quantization, official PTQ superiority, production
  Tensor Core runtime, mobile deployment, or full paper readiness.

## Gate Index

| gate | category | primary artifact | paper-facing claim boundary |
|---|---|---|---|
| `public_hygiene` | repo hygiene | `outputs/real_system_packer_2026-06-05/PUBLIC_REPO_HYGIENE_GATE_2026_06_06.md` | Public tree excludes private/process artifacts, speculative swarm/acoustic drafts, blank placeholders, and generated delivery bundles. |
| `paper_evidence_alignment` | paper alignment | `outputs/PAPER_EVIDENCE_ALIGNMENT_GATE_2026_06_07.md` | Current paper draft cites required evidence and avoids unsafe non-negated high-risk claims. |
| `calibration_instability` | calibration robustness | `outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md` | Small calibration splits induce unstable module-sensitivity rankings in the measured model/dataset cases. |
| `calibration_robustness_stress` | calibration robustness | `outputs/CALIBRATION_ROBUSTNESS_STRESS_GATE_2026_06_07.md` | Current target policies beat uniform INT4, best random seed, and random mean across committed short fake-quant PPL slices. |
| `consensus_transfer_boundary` | allocation boundary | `outputs/CONSENSUS_TRANSFER_BOUNDARY_GATE_2026_06_07.md` | Consensus avoids the worse single-split policy on paired Qwen3 transfer slices with bounded best-single regret. |
| `interaction_swap_boundary` | allocation boundary | `outputs/INTERACTION_SWAP_BOUNDARY_GATE_2026_06_07.md` | Bounded global-feedback swap search exposes interaction effects beyond additive module ranking. |
| `allocation_family_proxy` | comparator proxy | `outputs/Q_PALETTE_STYLE_ALLOCATION_FAMILY_GATE_2026_06_06.md` | A Q-Palette-style rate-distortion allocation proxy is executable on measured sensitivity artifacts. |
| `robust_lcb_consensus` | allocation proxy | `outputs/ROBUST_LCB_CONSENSUS_FAMILY_GATE_2026_06_06.md` | Robust-LCB consensus allocation artifacts are budget-respecting across the current measured model family. |
| `robust_lcb_quality` | quality boundary | `outputs/QWEN3_0P6B_ROBUST_LCB_QUALITY_GATE_2026_06_07.md` | Robust-LCB beats uniform INT4 on two guarded Qwen3-0.6B PPL slices, but not mean consensus. |
| `rotation_family_proxy` | comparator proxy | `outputs/QUAROT_SPINQUANT_ROTATION_FAMILY_GATE_2026_06_06.md` | A QuaRot/SpinQuant-style rotation-family proxy is executable; it is not a faithful rotation implementation. |
| `awq_gptq_proxy` | comparator proxy | `outputs/AWQ_GPTQ_PROXY_GATE_2026_06_06.md` | AWQ/GPTQ-style proxy policies are executable; this is not an official AWQ/GPTQ run. |
| `public_task_benchmark` | public task coverage | `outputs/PUBLIC_TASK_BENCHMARK_OLLAMA_QWEN25_ABLITERATE_7B_GATE_2026_06_07.md` | A local Ollama 7B model ran 100 MMLU/GSM8K subset rows under GPU guard. |
| `public_task_model_ladder` | public task coverage | `outputs/PUBLIC_TASK_MODEL_LADDER_GATE_2026_06_07.md` | Public-task evidence is shown as a guarded two-model ladder, not a single cherry-picked result. |
| `esmp_package` | artifact integrity | `outputs/real_system_packer_2026-06-05/ESMP_PACKAGE_VERIFY_QWEN3_0P6B_LIMIT8_2026_06_06.md` | ESMP package metadata, manifest, and binary headers are independently checkable. |
| `triton_shape_family` | kernel | `outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_FAMILY_GATE_2026_06_06.md` | Tuned grouped packed INT4/INT8 Triton kernels can beat torch FP16 on selected measured shapes. |
| `selector_runtime` | runtime wiring | `outputs/real_system_packer_2026-06-05/SELECTOR_RUNTIME_SMOKE_GATE_2026_06_06.md` | Selector-driven runtime wiring loads measured kernel configs and records selector calls. |
| `selected_row` | selected-row routing | `outputs/real_system_packer_2026-06-05/SELECTED_ROW_BENCHMARK_GATE_2026_06_06.md` | Selected-row routing can reduce module-level work when the active row set is small. |
| `cpp_runtime` | C++ runtime | `outputs/real_system_packer_2026-06-05/CPP_RUNTIME_SWEEP_GATE_2026_06_06.md` | C++ ESMP selected-row sweep supports module-level bypass/runtime claims only. |
| `fused_sidecar` | decode integration | `outputs/real_system_packer_2026-06-05/FUSED_SIDECAR_GENERATION_GATE_2026_06_06.md` | Fused selected-row sidecars execute in the HF generation loop with bounded additive overhead. |
| `fused_qkv_speed` | QKV replacement smoke | `outputs/real_system_packer_2026-06-05/FUSED_QKV_GENERATION_GATE_2026_06_06.md` | A shallow fused packed QKV replacement has guarded smoke-level speed/memory evidence. |
| `fused_qkv_quality` | QKV quality smoke | `outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_GATE_2026_06_06.md` | A conservative QKV8 repack candidate preserves a six-prompt suite under a quality gate. |
| `chat_task_stress` | deterministic task retention | `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_GATE_2026_06_06.md` | The selected K-only candidate survives an 84-task deterministic stress suite with one allowed regression. |

## Non-Ledger Readiness Probes

These probes are tracked because they reduce environment uncertainty, but they
are not counted in the current 22-gate paper-facing ledger.

| probe | category | primary artifact | boundary |
|---|---|---|---|
| `official_awq_smoke` | external PTQ readiness | `outputs/OFFICIAL_AWQ_SMOKE_GATE_2026_06_07.md` | AutoAWQ 0.2.9 can quantize and save a tiny Qwen2.5-0.5B artifact under guard; this is not a matched AWQ/GPTQ baseline or quality-retention result. |
| `official_awq_matched_ppl` | external PTQ readiness | `outputs/OFFICIAL_AWQ_MATCHED_PPL_GATE_2026_06_07.md` | The same four-prompt slice can be evaluated under FP16 and local AutoAWQ W4 group-128 with PPL ratio 1.1789; this is not a full public-dataset AWQ/GPTQ baseline. |
| `official_awq_public_wikitext2_ppl` | external PTQ readiness | `outputs/OFFICIAL_AWQ_MATCHED_PPL_QWEN25_0P5B_WIKITEXT2_GATE_2026_06_07.md` | A tiny public WikiText2 slice runs under FP16 and local AutoAWQ W4 group-128 with PPL ratio 1.2705 over 760 tokens; this is not a complete AWQ/GPTQ baseline. |
| `official_awq_public_c4_ppl` | external PTQ readiness | `outputs/OFFICIAL_AWQ_MATCHED_PPL_QWEN25_0P5B_C4_GATE_2026_06_07.md` | A tiny public C4 validation slice runs under FP16 and local AutoAWQ W4 group-128 with PPL ratio 1.1824 over 727 tokens; this is not a complete AWQ/GPTQ baseline. |
| `official_awq_public_calib_bundle` | external PTQ readiness | `outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_BUNDLE_GATE_2026_06_07.md` | A public-calibration AutoAWQ W4 group-128 bundle quantizes under guard and evaluates tiny public WikiText2/C4 PPL slices; this is partial official-package evidence, not GPTQ/AWQ competitive coverage. |

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
