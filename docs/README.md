# Documentation Map

Start here before reading the raw `outputs/` tree. The repository is large
because it commits gate artifacts for reproducibility, but only a small subset
is paper-facing.

## Authoritative Boundaries

| Need | File |
|---|---|
| One-line project scope and non-claims | `docs/scope-and-claims.md` |
| Paper-facing claim firewall | `docs/PAPER_CLAIM_MATRIX.md` |
| Short gate index | `docs/SYSTEM_EVIDENCE_GATES.md` |
| Expanded reproduction commands | `docs/SYSTEM_EVIDENCE_RUNBOOK.md` |
| Curated artifact map | `docs/ARTIFACT_MANIFEST.md` |
| Baseline/readiness tracker | `docs/BASELINE_COVERAGE_MANIFEST.json` |

## Method And Positioning

| Need | File |
|---|---|
| Consensus allocation method | `docs/consensus-allocation-method.md` |
| Calibration instability framing | `docs/calibration_split_instability_position_2026_06_05.md` |
| Quantization related-work map | `docs/RELATED_WORK_QUANTIZATION_2026.md` |
| Paper targets and readiness | `docs/paper-targets-and-readiness.md` |
| Current small-model candidate queue | `docs/recent_small_model_candidates_2026_06_05.md` |

## Historical Or Narrow Runbooks

| Need | File |
|---|---|
| Removed private/speculative artifacts | `docs/HISTORICAL_ARTIFACTS.md` |
| Qwen3-1.7B C4-128 chunked random16 run | `docs/qwen3_1p7b_c4_128_random16_chunked_runbook.md` |
| ESMP binary package format | `docs/ESMPQ001_FORMAT.md` |

## Reading Rule

The fastest way to misread this project is to browse `outputs/` from the root
and promote every report to a paper claim. Use the claim matrix first, then open
only the artifacts referenced by a gate.
