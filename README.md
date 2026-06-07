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
paper-facing only if it appears in the claim matrix or gate ledger.

## Current Status

| Area | Current Evidence | Boundary |
|---|---|---|
| Calibration instability | Qwen3/OLMo2/SmolLM2 short-slice fake-quant diagnostics | problem evidence |
| Consensus allocation | gated robustness and transfer diagnostics under fixed bit budgets | allocation diagnostic, not a production PTQ method |
| Official PTQ probes | AutoAWQ/GPTQModel Qwen2.5-0.5B W4/G128 readiness, tiny task smoke, and matched 20-row task subset paths | readiness only |
| Runtime probes | ESMP/Triton/C++ module-level gates plus PC-side smoke/subset runtime profiles | not end-to-end deployment |
| Mobile evidence | Redmi K80 Pro harness exists, but no real TTFT/tokens/s/memory log is complete | no mobile claim |

Current ledger status: **26 / 26 gates pass**.

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
python train_python/build_current_evidence_ledger.py --expected-gate-count 26
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
paper_drafts/          Draft text; not the authoritative evidence boundary
```

Large model weights and adapters are not committed. See
[`MODEL_ARTIFACTS.md`](MODEL_ARTIFACTS.md) for local artifact policy.
