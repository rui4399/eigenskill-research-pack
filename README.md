# EigenSkill-Q

EigenSkill-Q is a reproducible artifact for one narrow research question:

```text
When mixed-precision LLM quantization uses very small calibration splits,
how unstable are module-sensitivity rankings, and can cross-split consensus
reduce worst-split allocation risk under the same bit budget?
```

This repository is intentionally **not** presented as a new production
quantizer, a SOTA PTQ method, or a completed mobile runtime. The public tree is
organized around evidence boundaries so that a reviewer can tell which claims
are supported, which are proxies, and which are still blockers.

## Status Snapshot

| area | current state | allowed reading |
|---|---|---|
| Calibration instability | measured on small public model/dataset slices | problem evidence |
| Consensus allocation | passes committed short fake-quant stress gates | robustness diagnostic |
| Public task coverage | guarded local subset ladder, not leaderboard-scale | capability smoke |
| Packed runtime | gated ESMP/Triton/C++ prototypes | module-level system evidence |
| Official PTQ baselines | AutoAWQ smoke/public-calibrated W4 bundle plus GPTQModel public-calibrated W4 smoke pass on tiny public slices; faithful AWQ/GPTQ competitive baselines are still blockers | partial readiness only |
| Mobile/Redmi evidence | no real TTFT/tokens/s/memory logs yet | no deployment claim |

Current paper-facing ledger:

```text
outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

Current ledger status: **22 / 22 gates pass**. This means the committed gate
artifacts are internally consistent; it does **not** mean the paper is ready for
SOTA or deployment claims.

## Core Evidence Path

Read the repository in this order:

1. `docs/README.md` for the documentation map.
2. `docs/PAPER_CLAIM_MATRIX.md` for the claim firewall.
3. `outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md`
   for the current 22 paper-facing gates.
4. `outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md` for missing official
   baselines and mobile/runtime blockers.
5. `docs/ARTIFACT_MANIFEST.md` for the curated artifact map.

The many helper scripts and raw `outputs/` files are supporting material. They
should not be read as independent paper claims unless the claim matrix lists
the corresponding gate and boundary.

## Supported Claims

- Small calibration splits can produce unstable module-sensitivity rankings in
  the measured cases.
- Consensus-style allocation can reduce several short-slice fake-quant risks
  versus uniform INT4 and random budget-matched allocations.
- Packed artifacts and runtime probes are executable through explicit gates.
- Proxy comparators are separated from faithful official baselines in the gap
  dashboard.
- Minimal AutoAWQ matched PPL probes can run under guard on tiny prompt slices,
  including public WikiText2/C4 text slices; this is readiness evidence only.
- Public-calibrated AutoAWQ and GPTQModel W4 group-128 smoke runs can quantize,
  save local artifacts, and evaluate tiny public PPL slices under guard; this is
  still not a full AWQ/GPTQ competitive baseline.

## Non-Claims

- No SOTA quantization quality claim.
- No faithful matched GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant comparison yet.
- No Redmi K80 Pro, board-level latency, energy, thermal, or physical memory
  evidence yet.
- No production Tensor Core or mobile LLM runtime claim.
- No proof that spectral/eigen routing survives nonlinear Transformer blocks.
- No use of the old leaked v2 routing result as generalization evidence.

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

Do not treat the number of Markdown reports, C++ files, or output artifacts as a
research contribution. The paper-facing contribution is the gated evidence set
and its claim boundaries.

## C++ Scope

The C++ tree is intentionally tiered:

- core system artifacts: ESMPQ001 packing, inspection, selected-row/runtime
  probes, and kernel checks;
- algorithm diagnostics: allocation, consensus, split-stability, and policy
  bypass tools;
- reporting tools: JSON/Markdown summaries that make experiments auditable but
  are not systems contributions by themselves.

See `inference_cpp/README.md` before citing C++ percentage or executable count
as evidence.

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
docs/SYSTEM_EVIDENCE_RUNBOOK.md
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
