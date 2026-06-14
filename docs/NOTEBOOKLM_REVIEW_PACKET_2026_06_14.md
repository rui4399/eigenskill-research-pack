# NotebookLM Review Packet 2026-06-14

This packet is prepared for a manual NotebookLM review pass. The local
NotebookLM connector reports no configured personal public API and no
Enterprise project/token, so this file is the durable handoff artifact for
browser upload or copy/paste review.

## One-Sentence Thesis

EigenSkill-Q is currently strongest as a measurement paper: small calibration
splits can make module-sensitivity rankings unstable, and CSI gates make that
instability visible before mixed-precision allocation claims are made.

## Sources To Upload Or Paste First

Use these project files as the NotebookLM source set:

1. `docs/PAPER_CLAIM_MATRIX.md`
2. `docs/PROGRESS_SYNC_2026_06_12.md`
3. `docs/VENUE_GAP_ANALYSIS_2026_06_13.md`
4. `docs/RELATED_WORK_AND_GAP_SCAN_2026_06_14.md`
5. `paper_drafts/calibration_split_instability_aaai_draft_2026_06_13.md`
6. `outputs/CSI_VS_N_CURVE_QWEN25_1P5B_2026_06_11.md`
7. `outputs/CSI_TREND_SIGNIFICANCE_QWEN25_1P5B_2026_06_11.md`
8. `outputs/CSI_NULL_PERMUTATION_QWEN25_1P5B_2026_06_11.md`
9. `outputs/CSI_CROSS_SCALE_PAPER_ARTIFACTS_QWEN25_0P5B_VS_1P5B_2026_06_12.md`
10. `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_IFEVAL_PARTIAL_2026_06_13.md`

The IFEval source is partial and should be used only to understand the current
blocker. It is not evidence of matched FP16 retention.

## Questions For NotebookLM

Ask these in order:

1. Based only on the uploaded sources, what is the strongest claim this paper
   can safely make?
2. Which sentences in the CSI draft sound like they overclaim beyond the
   evidence ledger?
3. What related-work paragraph should be added so GPTQ, AWQ, SmoothQuant,
   OmniQuant, QuaRot, SpinQuant, calibration-data impact work, and LLMC are
   represented fairly?
4. What would a skeptical AAAI/IJCAI/TMLR reviewer reject first?
5. Does the draft make it clear that CSI is a diagnostic and not a new
   production quantizer?
6. What experiment would most efficiently convert the diagnostic into a
   stronger paper claim?
7. Which figures or tables should be in the first two pages?
8. What limitation statement should be moved from appendix-style language into
   the main text?

## Current Safe Answer Key

Expected safe answers:

- Strongest claim: CSI measures calibration split instability in
  module-sensitivity rankings, and the current Qwen2.5 artifacts show improved
  seed-pair ranking stability as n increases.
- Main missing evidence: downstream retention from acting on CSI or
  robust-consensus allocation.
- Related-work stance: present GPTQ/AWQ/SmoothQuant/OmniQuant as algorithm
  baselines; present calibration-data impact work as the closest conceptual
  neighbor; present QuaRot/SpinQuant as rotation/outlier-family context; present
  LLMC as benchmark/toolkit context.
- Submission risk: the diagnostic may be considered interesting but incomplete
  until it changes allocation outcomes or task retention.

## Non-Claims To Preserve

- No SOTA quantization claim.
- No universal scaling-law claim.
- No downstream retention claim until a matched downstream gate is complete.
- No production runtime, mobile deployment, or energy claim.
- No claim that the partial Qwen2.5-1.5B IFEval probe closes the FP16 gap.

## Suggested Draft Patch After NotebookLM Review

If NotebookLM agrees with the safe answer key, the next draft edit should:

1. Add a compact related-work section after the method sketch.
2. Add a falsification paragraph near limitations.
3. Move the downstream-retention gap into the abstract's final sentence only as
   a limitation, not as an implied result.
4. Convert the main CSI table into a first-page figure/table candidate.
