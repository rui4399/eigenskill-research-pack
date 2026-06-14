# Paper Draft Index

Date: 2026-06-12

The monolithic EigenSkill research pack has been split into five independent
paper/artifact tracks. Use the child repository that matches the paper claim.

## Currently Committed Drafts

| Draft | Role |
|---|---|
| `paper_drafts/eigenskill_q_research_draft_en_2026_06_07.md` | Current evidence-grounded English research draft. |
| `paper_drafts/calibration_split_instability_aaai_draft_2026_06_13.md` | Route-specific CSI first draft for AAAI/IJCAI/TMLR-style review. |
| `paper_drafts/eigenskill_q_ccf_style_draft_zh.md` | Chinese reader/historical CCF-style draft; use the English draft and claim matrix when they disagree. |

## Planned Split Draft Routes

The files below are route targets, not all currently committed draft files.
Create or update them only when the evidence boundary for that track is clear.

| Track | Draft | Public Repository |
|---|---|---|
| CSI quantization robustness | `paper_drafts/calibration_split_instability_aaai_draft_2026_06_13.md` | <https://github.com/rui4399/eigenskill-q-calibration-robustness> |
| ESMP packed runtime | planned: `paper_drafts/esmp_packed_runtime_draft_2026_06_12.md` | <https://github.com/rui4399/eigenskill-esmp-runtime> |
| Hybrid deterministic bypass | planned: `paper_drafts/hybridskill_bypass_draft_2026_06_12.md` | <https://github.com/rui4399/hybridskill-bypass-runtime> |
| CSI benchmark suite | planned: `paper_drafts/csi_benchmark_suite_draft_2026_06_12.md` | <https://github.com/rui4399/csi-benchmark-suite> |
| Eigen-Swarm vision | deferred local/private route; do not mix with the CSI quantization paper | <https://github.com/rui4399/eigenswarm-vision> |

## Boundary Rule

Do not merge the swarm vision text into the AAAI quantization paper. Do not use
runtime prototype evidence as a quantization-quality claim. Do not use CSI
method evidence as proof that ESMP kernels accelerate inference.

For the immediate AAAI-27 sprint, use `docs/AAAI_2027_CRITICAL_PATH.md` as the
priority order. It is the current reviewer-veto checklist and overrides broader
portfolio ambitions when time or GPU budget conflicts.

Use `docs/VENUE_GAP_ANALYSIS_2026_06_13.md` for the current venue-fit and
reviewer-gap map.

Use `docs/RELATED_WORK_AND_GAP_SCAN_2026_06_14.md` and
`docs/NOTEBOOKLM_REVIEW_PACKET_2026_06_14.md` for the current related-work
positioning pass and manual NotebookLM review handoff.
