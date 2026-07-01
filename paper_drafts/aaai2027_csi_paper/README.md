# AAAI-27 CSI Paper Draft

This folder contains an anonymous AAAI-style paper draft:

- `main.tex` - main paper text.
- `references.bib` - bibliography entries used by the draft.
- `aaai2027_fallback.sty` - local drafting fallback only.
- `evidence_index.md` - mapping from paper numbers to artifacts.

## Build locally

From this directory:

```powershell
latexmk -pdf -interaction=nonstopmode main.tex
```

The fallback style is only for local review. Before submission, download the
official AAAI-27 author kit, place the official `aaai2027.sty` and `.bst` files
in this directory, rebuild, and check the PDF against the author kit.

## Claim boundary

The paper is intentionally written as a calibration-robustness and measurement
paper. It does not claim:

- state-of-the-art PTQ;
- production inference acceleration;
- mobile deployment;
- universal scaling laws;
- downstream superiority of CSI-derived allocations.

The current revision does include full downstream native-PTQ retention evidence
for Qwen2.5-1.5B:

- full MMLU, 14,042 examples: FP16 0.5864, AutoAWQ 0.5648, GPTQModel 0.5362;
- full GSM8K, 1,319 examples: FP16 0.0811, AutoAWQ 0.0788, GPTQModel 0.0728.

These rows confront native PTQ baselines, but they are not CSI-informed
allocation wins.

The current revision also includes local GPU fake-quant allocation smokes:

- Qwen2.5-0.5B, four WikiText2/C4 PPL slices: CSI/consensus 4-to-8 allocation
  beats uniform INT4 on 4/4 slices;
- Qwen2.5-1.5B, one WikiText2 PPL slice: FP16 10.8203, uniform INT4 15.6317,
  CSI/consensus allocation 13.5063.

These rows exercise the actual allocation path, but they are directional local
smokes. They are not full downstream MMLU/GSM8K retention and not same-budget
uniform INT4 comparisons.

The current revision adds the reviewer-critical AAAI structure requested in the
review notes:

- one-sentence novelty anchor: PTQ allocation as constrained
  calibration-driven optimization;
- final six-figure audit narrative:
  `fig1_pipeline.png`, `fig2_phase_transition.png`, `fig3_cross_model.png`,
  `fig4_risk.png`, `fig5_failure.png`, and `fig6_boundary.png`;
- claim-boundary figure that separates diagnostic evidence, gate-passing audit
  claims, and missing same-budget downstream method-superiority rows;
- failure-separation heatmap for GPTQ/AWQ/SmoothQuant/OmniQuant versus CSI's
  orthogonal allocation gate;
- CSI-versus-allocation-risk proxy figure linking calibration stability to
  allocation audit risk;
- strict mechanism mapping from objective terms to ablation/failure hooks;
- stress/failure section covering calibration collapse, constraint conflict,
  and gate misfire;
- explicit boundary between existing INT2/INT3 scaffolds and missing downstream
  2/3-bit task-retention curves.

The final audit figures are generated with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\make_dominance_figures.ps1
```

They are intentionally written as audit figures. In particular,
`fig4_risk.png` is an allocation-risk proxy derived from calibration stability
and committed stress evidence, not a measured downstream error rate, and
`fig5_failure.png` is a structured failure-mode interpretation rather than a
measured accuracy table. None of these figures should be interpreted as a
completed 2/3-bit SOTA dominance curve until the missing same-budget downstream
rows are measured.

The strongest next experiment is now a direct CSI-informed downstream-retention
row:

```text
FP16 vs uniform W4 vs AWQ W4/G128 vs GPTQModel W4/G128 vs CSI-informed allocation
same model, same public calibration, same task fixture, same guard.
```

The strongest missing AAAI stress experiment is:

```text
FP16 vs uniform W2/W3/W4/W8 vs AWQ/GPTQModel where available vs CSI-informed allocation
same model, same public calibration, same MMLU/GSM8K/IFEval-style fixture,
report accuracy/PPL drop, tokens/s, peak VRAM, and failure cases.
```
