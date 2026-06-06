# EigenSkill-Q

EigenSkill-Q is a reproducible research artifact for **calibration split
instability in mixed-precision LLM quantization**. It studies a narrow problem:

```text
Small calibration splits can give inconsistent module-sensitivity rankings.
Can a cross-split consensus policy reduce worst-split risk under the same
mixed-precision bit budget?
```

The repository also contains packed-system prototypes, but they are kept behind
explicit evidence gates. This is not presented as a production quantizer, a
state-of-the-art PTQ implementation, or a completed mobile/edge runtime.

## Current Evidence

The current paper-facing evidence ledger passes **21 / 21 gates**:

```text
outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

The strongest supported findings are:

| Finding | Current evidence | Boundary |
|---|---:|---|
| Calibration split rankings are unstable across small public model slices. | 3 / 3 measured cases unstable; mean score/cost Spearman `0.0713`; top-20 Jaccard `0.1022`. | Establishes the problem setting, not method superiority. |
| Consensus-style target policies pass the committed fake-quant stress gate. | 11 / 11 wins vs uniform INT4, best random seed, and random mean; one-sided sign-test p `0.000488` vs best random. | Short-slice fake-quant PPL only. |
| Consensus reduces worse-single-split risk on paired Qwen3 transfer slices. | 4 / 4 wins vs the worse single-split policy; 2 / 4 wins vs the best single-split policy; max best-single regret `0.3046` PPL. | Robustness boundary evidence, not an oracle claim. |
| Bounded global-feedback swap search exposes interaction effects. | 3 search cases, 16 trials, 5 improved trials, and 5 locally-negative-but-globally-improved counterexamples; transfer max regret `0.0087` PPL. | Interaction-aware fake-quant diagnostic, not a production allocator. |
| Public task coverage is guarded beyond schema smoke. | Local Ollama Qwen2.5-abliterate-7B gets `39 / 100` passes on 50 MMLU abstract-algebra and 50 GSM8K rows; peak guard VRAM ratio `0.8865`. | Local subset evidence only, not leaderboard or fused-retention evidence. |
| Packed-system components are executable and gated. | ESMP package integrity, Triton shape-family, selector, selected-row, C++ runtime, fused-sidecar, and shallow QKV gates pass. | Prototype/module-level evidence, not end-to-end deployment. |

Start here for exact claim boundaries:

```text
docs/PAPER_CLAIM_MATRIX.md
docs/SYSTEM_EVIDENCE_GATES.md
docs/ARTIFACT_MANIFEST.md
outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md
```

## What This Repository Claims

Supported:

- small calibration splits can produce unstable sensitivity rankings;
- cross-split consensus allocation can improve robustness over uniform and
  random mixed-precision allocations on the committed short fake-quant slices;
- current packed artifacts and runtime probes are machine-checkable through
  gates;
- missing baselines and hardware evidence are explicitly tracked.

Not supported yet:

- state-of-the-art quantization quality;
- faithful official GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant reproduction;
- real Redmi K80 Pro, board-level latency, energy, or memory evidence;
- production Tensor Core or mobile LLM runtime readiness;
- proof that spectral/eigen routing survives nonlinear Transformer blocks;
- the old leaked v2 routing result as generalization evidence.

## Repository Layout

```text
train_python/          Measurement, fake-quant evaluation, gates, summaries
inference_cpp/         C++ allocation, audit, ESMP package, and runtime probes
mobile/redmi_k80_pro/  ADB metric harness and NEON decode prototype
data_eval/             Small prompt slices and evaluation configs
docs/                  Claim matrix, evidence gates, related work, readiness
outputs/               Committed gate artifacts used by the evidence ledger
paper_drafts/          Draft text; not the authoritative evidence boundary
```

The large `outputs/` tree is intentional for the current artifact branch because
the evidence ledger points to committed JSON/Markdown files. Historical delivery
notes, private NotebookLM/Obsidian exports, and speculative swarm/acoustic
concept drafts are not part of the public artifact boundary.

## Quick Checks

Run the unit tests:

```bash
python -m unittest discover -s train_python -p "test_*.py"
```

Run the public repository hygiene gate:

```bash
python train_python/gate_public_repo_hygiene.py \
  --out-json outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/PUBLIC_REPO_HYGIENE_GATE_2026_06_06.md
```

For the full ledger rebuild command, see:

```bash
python train_python/build_current_evidence_ledger.py
```

For detailed gate commands and claim boundaries, see:

```text
docs/SYSTEM_EVIDENCE_GATES.md
```

## Model Weights

Large model weights and adapters are not committed. The public repository tracks
evaluation configs, small fixtures, package metadata, and evidence summaries.
See:

```text
MODEL_ARTIFACTS.md
```

## Paper Framing

The most defensible current title shape is:

```text
Calibration Split Instability in Mixed-Precision LLM Quantization:
Consensus Sensitivity Allocation with Gated Packed-System Evidence
```

This is narrower than the original EigenSkill vision, but it is reviewable:
it defines a measurable instability problem, gives a conservative allocation
response, and keeps system claims behind executable gates.

Current paper draft:

```text
paper_drafts/eigenskill_q_iclr_ccfa_draft_en_2026_06_07.md
```
