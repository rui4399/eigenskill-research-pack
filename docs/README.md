# Documentation Map

Start here before reading the raw `outputs/` tree. The repository is large
because it commits gate artifacts for reproducibility, but only a small subset
is paper-facing. Treat this directory as the navigation layer; the root README
is intentionally short.

## Authoritative Boundaries

| Need | File |
|---|---|
| Mentor/Notion-ready progress report | `docs/MENTOR_NOTION_REPORT_2026_06_08.md` |
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
| Multi-paper/repository split plan | `docs/RESEARCH_PORTFOLIO_SPLIT.md` |

## Workbench And Historical Notes

| Need | File |
|---|---|
| Current small-model candidate queue | `docs/recent_small_model_candidates_2026_06_05.md` |
| Removed private/speculative artifacts | `docs/HISTORICAL_ARTIFACTS.md` |
| Qwen3-1.7B C4-128 chunked random16 run | `docs/qwen3_1p7b_c4_128_random16_chunked_runbook.md` |
| ESMP binary package format | `docs/ESMPQ001_FORMAT.md` |

## Public Repository Curation

The public branch should look like a reproducible artifact, not a running lab
notebook. In practice this means:

- the root directory stays small and contains only release-entry files;
- historical concept material lives only in `docs/HISTORICAL_ARTIFACTS.md`;
- raw `outputs/` files are supporting evidence only when a gate references
  them;
- paper drafts do not override the claim matrix.

The hygiene gate enforces root clutter, generated delivery bundles, private
process exports, blank placeholders, stale positioning, and risky root README
terms.

## Edit Discipline

Use this rule when deciding whether to change the repository:

```text
If a file does not help another reader reproduce, verify, or bound a claim, keep
it in local notes instead of GitHub.
```

Allowed public changes should usually do one of three things:

- make an existing claim narrower and more checkable;
- connect a gate command to a committed artifact;
- remove or block confusing historical/process material.

## Reading Rule

The fastest way to misread this project is to browse `outputs/` from the root
and promote every report to a paper claim. Use the claim matrix first, then open
only the artifacts referenced by a gate.
