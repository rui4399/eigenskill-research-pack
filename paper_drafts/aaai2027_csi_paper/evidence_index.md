# Evidence Index for `main.tex`

This index maps paper-facing numbers to committed local artifacts. The claim
boundary follows `docs/PAPER_CLAIM_MATRIX.md`: a result should stay in the
paper only when it has a JSON artifact, a generated Markdown gate report, a
runbook command, and a matrix row.

## AAAI-27 format facts

- Official submission instructions checked on 2026-07-01:
  <https://aaai.org/conference/aaai/aaai-27/submission-instructions/>
- Regular paper abstracts are due 2026-07-21 and full papers are due
  2026-07-28, both UTC-12.
- Submissions are anonymous and can contain up to 7 pages of technical content
  plus reference/checklist pages.

## Main CSI evidence

- Qwen2.5-1.5B n=2/4/8 table:
  `outputs/CSI_VS_N_CURVE_QWEN25_1P5B_2026_06_11.md`
- Qwen2.5-1.5B trend significance:
  `outputs/CSI_TREND_SIGNIFICANCE_QWEN25_1P5B_2026_06_11.md`
- Qwen2.5-1.5B null permutation:
  `outputs/CSI_NULL_PERMUTATION_QWEN25_1P5B_2026_06_11.md`
- Qwen2.5 0.5B vs 1.5B cross-scale table:
  `outputs/CSI_CROSS_SCALE_PAPER_ARTIFACTS_QWEN25_0P5B_VS_1P5B_2026_06_12.md`

## Second-pool replication

- SmolLM2-360M n=4/8/16 table:
  `outputs/CSI_VS_N_CURVE_SMOLLM2_360M_SECOND_POOL_2026_06_16.md`
- SmolLM2-360M trend significance:
  `outputs/CSI_TREND_SIGNIFICANCE_SMOLLM2_360M_SECOND_POOL_2026_06_16.md`
- SmolLM2-360M null permutation:
  `outputs/CSI_NULL_PERMUTATION_SMOLLM2_360M_SECOND_POOL_2026_06_16.md`
- RTX3090 experiment report context:
  `outputs/RTX3090_EXPERIMENT_REPORT_2026_06_16.md`

## Full downstream native PTQ retention

- Qwen2.5-1.5B full MMLU 57-subject matched FP16/AutoAWQ/GPTQModel matrix:
  `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_MMLU_FULL_PREFIX14042_FP16_AWQ_GPTQMODEL_MATRIX_2026_06_08.md`
- Qwen2.5-1.5B full MMLU statistical intervals:
  `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_MMLU_FULL_PREFIX14042_FP16_AWQ_GPTQMODEL_STATISTICS_2026_06_08.md`
  Key values: FP16 8234/14042 = 0.5864; AutoAWQ 7931/14042 = 0.5648,
  paired delta -0.0216 CI [-0.0273, -0.0155]; GPTQModel 7529/14042 =
  0.5362, paired delta -0.0502 CI [-0.0570, -0.0432].
- Qwen2.5-1.5B full GSM8K matched FP16/AutoAWQ/GPTQModel matrix:
  `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_GSM8KFULL_FP16_AWQ_GPTQMODEL_MATRIX_2026_06_08.md`
- Qwen2.5-1.5B full GSM8K statistical intervals:
  `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_GSM8KFULL_FP16_AWQ_GPTQMODEL_STATISTICS_2026_06_08.md`
  Key values: FP16 107/1319 = 0.0811; AutoAWQ 104/1319 = 0.0788,
  paired delta -0.0023 CI [-0.0190, 0.0144]; GPTQModel 96/1319 =
  0.0728, paired delta -0.0083 CI [-0.0243, 0.0076].

## Allocation stress and feasibility

- Consensus/fake-quant stress gate:
  `outputs/CALIBRATION_ROBUSTNESS_STRESS_GATE_2026_06_07.md`
- Consensus transfer boundary:
  `outputs/CONSENSUS_TRANSFER_BOUNDARY_GATE_2026_06_07.md`
- Interaction-aware swap boundary:
  `outputs/INTERACTION_SWAP_BOUNDARY_GATE_2026_06_07.md`
- Q-Palette-style budget/Lagrangian proxy:
  `outputs/Q_PALETTE_STYLE_ALLOCATION_FAMILY_GATE_2026_06_06.md`
- Robust-LCB consensus family gate:
  `outputs/ROBUST_LCB_CONSENSUS_FAMILY_GATE_2026_06_06.md`
- Extreme-bit rate-distortion scaffold:
  `outputs/rate_distortion_allocation_budget26_report.md`
  and `outputs/rate_distortion_allocation_budget36_report.md`
- Random-seed audit failure boundary:
  `outputs/qwen3_0p6b_lowmem_cpp_random16_random_seed_audit.md`
- RTX3090 guarded 7B and 14B rows:
  `outputs/RTX3090_EXPERIMENT_REPORT_2026_06_16.md`
- Local GPU Qwen2.5-0.5B CSI/consensus fake-quant PPL smoke:
  `outputs/LOCAL_QWEN25_0P5B_GPU_FAKE_QUANT_PPL_MULTI_SLICE_SUMMARY_2026_07_01.md`
  Directional values: consensus 4-to-8 allocation beats uniform INT4 on 4/4
  public WikiText2/C4 PPL smoke slices, but uses 4.4997 average bits versus
  uniform INT4's 4.0 and is not full downstream retention.
- Local GPU Qwen2.5-1.5B CSI/consensus fake-quant PPL smoke:
  `outputs/LOCAL_QWEN25_1P5B_GPU_WIKITEXT2_1_FAKE_QUANT_PPL_SUMMARY_2026_07_02.md`
  Directional values: FP16 10.8203, uniform INT4 15.6317, CSI/consensus
  allocation 13.5063 on a one-prompt WikiText2 smoke. The consensus allocation
  uses 4.4993 average bits versus uniform INT4's 4.0, so this is not a
  same-budget downstream claim.
- Superseded local Qwen2.5-1.5B GPU attempt log:
  `outputs/LOCAL_QWEN25_1P5B_GPU_FAKE_QUANT_ATTEMPT_2026_07_01.md`
  The earlier 1.5B attempt did not produce a result under desktop memory
  pressure. The 2026-07-02 split-config run above supersedes it.

## Generated paper figures

- Framework overview:
  `paper_drafts/aaai2027_csi_paper/figures/framework_overview.png`
- CSI stability curves:
  `paper_drafts/aaai2027_csi_paper/figures/csi_stability_curves.png`
- Stress/failure margins:
  `paper_drafts/aaai2027_csi_paper/figures/stress_failure_margins.png`

## Remaining submission-critical gap

- A direct CSI-informed downstream 2/3/4/8-bit retention curve is still
  missing. Current full downstream rows cover native FP16/AutoAWQ/GPTQModel
  retention, while INT2/INT3 evidence is a rate-distortion scaffold and local
  fake-quant stress boundary, not a full task-retention result. The local
  0.5B and 1.5B GPU fake-quant smokes are directional evidence only and should
  not be promoted to the main Table 4 claim without broader task/PPL coverage
  and matched-budget controls.

## Draft sources integrated

- Narrow AAAI CSI draft:
  `paper_drafts/calibration_split_instability_aaai_draft_2026_06_13.md`
- Unified constraint-guided framework draft:
  `paper_drafts/unified_constraint_guided_calibration_framework_2026_06_28.md`
- RTX3090 extension draft:
  `paper_drafts/eigenskill_q_rtx3090_extended_draft_2026_06_16.md`
- Claim matrix:
  `docs/PAPER_CLAIM_MATRIX.md`
- Critical path:
  `docs/AAAI_2027_CRITICAL_PATH.md`
