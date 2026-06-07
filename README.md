# EigenSkill-Q

EigenSkill-Q is a curated research artifact for one narrow question:

```text
When mixed-precision LLM quantization relies on very small calibration splits,
how unstable are module-sensitivity rankings, and can cross-split consensus
reduce bad allocation choices under the same bit budget?
```

This repository is **not** a new production quantizer, a deployment-ready
runtime, or a claim of state-of-the-art quality. It is organized so reviewers
can separate supported evidence from exploratory material.

The public branch is now curated as an evidence artifact, not as a running lab
notebook. Local planning notes, Obsidian summaries, NotebookLM material, Notion
drafts, delivery bundles, and speculative concept text are deliberately kept
out of the GitHub tree.

## Start Here

Read the public artifact in this order:

1. [`docs/README.md`](docs/README.md) for the documentation map.
2. [`docs/PAPER_CLAIM_MATRIX.md`](docs/PAPER_CLAIM_MATRIX.md) for every
   supported claim and its evidence boundary.
3. [`docs/SYSTEM_EVIDENCE_GATES.md`](docs/SYSTEM_EVIDENCE_GATES.md) for the
   short gate index.
4. [`outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md`](outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md)
   for the current paper-facing gate ledger.
5. [`docs/ARTIFACT_MANIFEST.md`](docs/ARTIFACT_MANIFEST.md) if you need a map
   through the committed `outputs/` tree.

Do not treat raw `outputs/` browsing as the evidence boundary. A result is
paper-facing only if it appears in the claim matrix or gate ledger. When those
files disagree, follow the claim matrix first.

## Current Status

| Area | Current Evidence | Boundary |
|---|---|---|
| Calibration instability | Qwen3/OLMo2/SmolLM2 distribution-split diagnostics plus Qwen2.5 sample-size/model-scale perturbation matrix | problem evidence |
| Calibration seed stability | Qwen2.5-0.5B six-seed prompt sampling over one public WikiText2 pool with pair-bootstrap CIs | same-model diagnostic, not quality retention |
| CSI vs calibration size | Qwen2.5-0.5B n=2/4/8 six-seed curve; mean Spearman rises 0.3725 -> 0.4324 -> 0.6645 | local calibration-size evidence, not a universal scaling law |
| CSI trend significance | Independent bootstrap gain CIs from n=2 to n=8 are positive for Spearman/top-20/positive-set stability; minimum random pair dominance probability is 0.9422 | local trend evidence, not a universal scaling law |
| Rank-inversion theory | Chebyshev-style plug-in inversion-risk gate over the same n=2/4/8 Qwen2.5 seed artifacts; margin inversion rate falls 0.0969 -> 0.0427 | theory-aligned diagnostic, not a tight bound proof |
| Consensus allocation | gated robustness and transfer diagnostics under fixed bit budgets | allocation diagnostic, not a production PTQ method |
| Official PTQ probes | AutoAWQ/GPTQModel Qwen2.5-0.5B W4/G128 readiness, aligned expanded 16-prompt public PPL gates, tiny task smoke, matched 50-row and true 100-row task subset paths, deterministic IFEval-style execution smoke, and a matched local baseline pack | local evidence only; quantized paths save VRAM but are slower here |
| Runtime probes | ESMP/Triton/C++ module-level gates plus PC-side smoke/subset50/subset100 runtime profiles | not end-to-end deployment |
| Mobile evidence | Redmi K80 Pro harness exists, but no real TTFT/tokens/s/memory log is complete | no mobile claim |

Current ledger status: **37 / 37 gates pass**.

## Curation Contract

- GitHub contains reproducible code, gate scripts, compact documentation, and
  committed artifacts that are referenced by the claim matrix.
- Obsidian is the place for strategy, criticism, mentor-facing notes, and
  private work logs.
- New files should not be added to the public tree unless a gate, runbook row,
  or claim-matrix row needs them.
- Existing claims should be narrowed before new claims are added.

## Supported Reading

You may cite the repository for:

- calibration split instability in the measured small public slices;
- consensus-style mixed-precision allocation diagnostics;
- gated C++/ESMP/Triton prototype evidence at module or smoke level;
- explicit baseline and deployment gaps.

You should not cite it as:

- a production quantization library;
- a faithful broad AWQ/GPTQ/SmoothQuant/rotation baseline comparison;
- an end-to-end latency, memory, energy, or mobile deployment result;
- a proof of nonlinear Transformer spectral routing.

## Quick Checks

```bash
python -m unittest discover -s train_python -p "test_*.py"
python train_python/build_current_evidence_ledger.py --expected-gate-count 37
python train_python/gate_public_repo_hygiene.py \
  --out-json outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/PUBLIC_REPO_HYGIENE_GATE_2026_06_06.md
```

The expanded reproduction commands live in
[`docs/SYSTEM_EVIDENCE_RUNBOOK.md`](docs/SYSTEM_EVIDENCE_RUNBOOK.md).

## Layout

```text
train_python/          Measurement, fake-quant evaluation, gates, summaries
inference_cpp/         C++ allocation, audit, ESMP package, and runtime probes
mobile/redmi_k80_pro/  ADB metric harness and NEON decode prototype
data_eval/             Small public/synthetic prompt slices and configs
docs/                  Claim matrix, evidence gates, related work, readiness
outputs/               Committed gate artifacts used by the evidence ledger
paper_drafts/          Draft text only; claim matrix remains authoritative
```

Large model weights and adapters are not committed. See
[`MODEL_ARTIFACTS.md`](MODEL_ARTIFACTS.md) for local artifact policy.
