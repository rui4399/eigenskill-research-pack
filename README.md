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
| Official PTQ baselines | AutoAWQ smoke passes; faithful matched AWQ/GPTQ baselines are still blockers | readiness only |
| Mobile/Redmi evidence | no real TTFT/tokens/s/memory logs yet | no deployment claim |

Current paper-facing ledger:

```text
outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

Current ledger status: **22 / 22 gates pass**. This means the committed gate
artifacts are internally consistent; it does **not** mean the paper is ready for
SOTA or deployment claims.

## Read First

1. `docs/PAPER_CLAIM_MATRIX.md` defines allowed and rejected claims.
2. `outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md`
   lists every current gate.
3. `outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md` shows paper-blocking gaps
   and separates AutoAWQ smoke from matched AWQ/GPTQ baselines.
4. `docs/SYSTEM_EVIDENCE_GATES.md` is the short gate index.
5. `docs/SYSTEM_EVIDENCE_RUNBOOK.md` contains the long reproduction commands.

## Supported Claims

- Small calibration splits can produce unstable module-sensitivity rankings in
  the measured cases.
- Consensus-style allocation can reduce several short-slice fake-quant risks
  versus uniform INT4 and random budget-matched allocations.
- Packed artifacts and runtime probes are executable through explicit gates.
- Proxy comparators are separated from faithful official baselines in the gap
  dashboard.

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
