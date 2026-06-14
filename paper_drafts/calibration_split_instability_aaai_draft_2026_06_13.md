# Calibration Split Instability in Mixed-Precision LLM Quantization

Date: 2026-06-13

Target route: AAAI / IJCAI / TMLR, with a possible NeurIPS or ICLR workshop
version if positioned as a measurement paper.

Status: route-specific first draft. This draft is intentionally narrower than
`paper_drafts/eigenskill_q_research_draft_en_2026_06_07.md`; it only uses the
CSI evidence line and does not claim production runtime, SOTA quantization, or
mobile deployment.

## Abstract

Post-training quantization of large language models often relies on a small
calibration set to rank modules by sensitivity and allocate scarce precision.
This paper studies a failure mode in that practice: calibration split
instability, where different small prompt samples induce materially different
module-sensitivity rankings. We introduce calibration split instability (CSI)
as an auditable diagnostic for mixed-precision quantization workflows. Across
the current EigenSkill-Q evidence artifacts, Qwen2.5 calibration curves show
that increasing calibration prompt count improves prompt-seed ranking stability.
For Qwen2.5-1.5B, mean pairwise Spearman rises from `0.1410` at `n=2` to
`0.4918` at `n=8`, while top-20 Jaccard rises from `0.2604` to `0.4401` and
positive-set Jaccard rises from `0.4244` to `0.5992`. A cross-scale comparison
shows that the measured Qwen2.5-1.5B curve is less stable than the measured
Qwen2.5-0.5B curve at matched calibration sizes, while both improve as `n`
increases. The contribution is a reproducible measurement and gating framework
for detecting when small-calibration allocation decisions are under-supported.
It is not yet a claim that CSI-derived allocation improves downstream quality.

## 1. Problem

Mixed-precision PTQ workflows usually need to answer a practical question:
which modules deserve higher precision under a fixed bit budget? A common
answer is to score modules on a small calibration set and allocate precision to
the modules that appear most sensitive. The hidden assumption is that the
ranking is stable enough that the selected calibration prompts are not driving
the allocation.

CSI tests that assumption directly. If two equally plausible calibration
samples give different sensitivity rankings, then a single ranking should not
be treated as a robust basis for allocation.

## 2. Current Evidence

Primary artifacts:

- `outputs/CALIBRATION_SEED_STABILITY_QWEN25_1P5B_N2_2026_06_10.md`
- `outputs/CALIBRATION_SEED_STABILITY_QWEN25_1P5B_N4_2026_06_11.md`
- `outputs/CALIBRATION_SEED_STABILITY_QWEN25_1P5B_N8_2026_06_11.md`
- `outputs/CSI_VS_N_CURVE_QWEN25_1P5B_2026_06_11.md`
- `outputs/CSI_TREND_SIGNIFICANCE_QWEN25_1P5B_2026_06_11.md`
- `outputs/CSI_NULL_PERMUTATION_QWEN25_1P5B_2026_06_11.md`
- `outputs/CSI_CROSS_SCALE_QWEN25_0P5B_VS_1P5B_2026_06_11.md`
- `outputs/CSI_CROSS_SCALE_PAPER_ARTIFACTS_QWEN25_0P5B_VS_1P5B_2026_06_12.md`

Current ledger status:

- `75 / 75` evidence gates pass by
  `train_python/build_current_evidence_ledger.py`.
- Paper alignment gate for the main English draft passes with `57` required
  evidence references, `66` referenced repo paths, `0` missing paths, `0` stale
  tokens, and `0` unsafe non-negated claim lines.

## 3. Method Sketch

1. Sample multiple calibration prompt subsets at fixed size `n`.
2. Compute per-module sensitivity rankings for each subset.
3. Compare all seed pairs using rank and set-overlap metrics:
   Spearman, top-k Jaccard, and positive-set Jaccard.
4. Repeat across `n=2/4/8` to measure whether stability improves with
   calibration size.
5. Gate the trend using bootstrap gain checks and a label-shuffle null
   permutation test.
6. Report only bounded diagnostic claims unless downstream retention evidence
   is present.

## 4. Related Work Position

CSI should be positioned beside calibration-aware PTQ work, not above it. GPTQ,
AWQ, SmoothQuant, and OmniQuant are algorithm families for producing accurate
quantized models under practical calibration or reconstruction constraints.
QuaRot and SpinQuant represent a rotation/outlier-mitigation family that changes
the quantization surface itself. Recent calibration-data studies and
benchmark-toolkit work show that calibration choices and standardized settings
matter for compression evaluation.

The missing measurement targeted here is narrower: before claiming that a
small calibration set supports a mixed-precision allocation, measure whether
equally plausible calibration prompt splits induce stable module-sensitivity
rankings. This makes CSI a diagnostic and falsification tool, not a replacement
for faithful AWQ/GPTQ/SmoothQuant/rotation baselines.

The current related-work and gap scan is tracked in
`docs/RELATED_WORK_AND_GAP_SCAN_2026_06_14.md`.

## 5. Main Results To Present

| Model | n | Mean Spearman | Top-20 Jaccard | Positive-set Jaccard |
|---|---:|---:|---:|---:|
| Qwen2.5-1.5B | 2 | 0.1410 | 0.2604 | 0.4244 |
| Qwen2.5-1.5B | 4 | 0.2869 | 0.3313 | 0.5189 |
| Qwen2.5-1.5B | 8 | 0.4918 | 0.4401 | 0.5992 |

Valid wording:

```text
In the current same-prompt-pool Qwen2.5 artifacts, the 1.5B curve is less
stable than the 0.5B curve at matched calibration sizes, while both improve
with additional calibration prompts.
```

Invalid wording:

- CSI proves a universal scaling law.
- CSI-derived allocation improves downstream retention.
- Do not claim that the method is SOTA PTQ.
- The current artifact is production or mobile deployment evidence.

## 6. Venue Positioning

AAAI / IJCAI / TMLR:
position as a reliable AI measurement and robustness paper. The title should
emphasize calibration instability and auditable gates, not a new quantizer.

NeurIPS / ICLR workshop:
position as a benchmark-style study of how calibration sampling affects
quantization allocation decisions.

ACL / EMNLP Findings:
possible only if the next experiments connect CSI to language-task retention
on MMLU/GSM8K or another NLP task suite in a way that changes conclusions.

MLSys:
do not use this draft as the systems submission. Systems claims belong in an
ESMP/W4A8 runtime draft; no current end-to-end latency or memory evidence is
claimed here.

## 7. Critical Missing Experiments

1. Downstream retention:
   compare a CSI-informed or robust-consensus allocation against FP16, AutoAWQ,
   and GPTQModel on matched task fixtures.
2. Prompt-pool generality:
   repeat Qwen2.5-1.5B `n=2/4/8` on a second public calibration prompt pool,
   preferably C4.
3. Broader family coverage:
   add at least one additional model family before making broad calibration
   robustness claims.
4. Baseline breadth:
   add a faithful SmoothQuant or rotation-family baseline only if the official
   implementation can be run under the same guarded evidence discipline.
5. Statistical packaging:
   convert gate outputs into paper tables with confidence intervals, not only
   pass/fail reports.

## 8. Falsification And Submission Risk

The current draft is defensible as a measurement artifact, but not as a top-tier
main-track submission yet. The main reviewer objection is predictable: the
diagnostic is interesting, but the paper must show that acting on the diagnostic
changes downstream quantization outcomes. The next experiment should therefore
be a downstream-retention gate before more writing polish.

Concrete falsification checks:

- a second prompt pool fails to reproduce the n=2/4/8 stability trend;
- another model family shows stable rankings even at very small n;
- downstream task retention is insensitive to the CSI ranking instability;
- faithful AWQ/GPTQ/SmoothQuant/rotation baselines make the same allocation
  decision across calibration splits;
- CSI-informed allocation fails against a simpler matched-budget heuristic.
