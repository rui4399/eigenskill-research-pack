# Venue Gap Analysis 2026-06-13

This document compares the current EigenSkill-Q evidence state with plausible
top-tier venue expectations. It is a planning artifact, not a claim that the
work is ready for any venue.

## Current Strongest Claim

The strongest current paper is a CSI measurement paper:

```text
Small calibration splits can produce unstable module-sensitivity rankings; in
the measured Qwen2.5 artifacts, increasing calibration prompt count improves
prompt-seed ranking stability.
```

Evidence boundary:

- `75 / 75` current evidence gates pass.
- Codegraph is live for repo code intelligence: `231` files, `4276` nodes,
  `8416` edges.
- Tooling/MCP/skills are configured and locally healthy for this workflow, but
  remote SaaS plugin authentication is not globally verified.

## Venue Fit Matrix

| Route | Best fit | Current readiness | Main gap |
|---|---|---:|---|
| AAAI / IJCAI | CSI as robust AI evaluation and reliability diagnostic | medium | downstream retention showing the diagnostic changes allocation outcomes |
| TMLR | reproducible measurement paper with careful claim boundaries | medium | broader model/prompt-pool coverage and clearer falsification cases |
| NeurIPS / ICLR workshop | calibration robustness benchmark and artifact track | medium-high | benchmark packaging and broader baselines |
| ACL / EMNLP Findings | NLP task-retention caveat for LLM PTQ | low-medium | stronger link from CSI to language-task accuracy/retention |
| MLSys / systems workshop | ESMP/W4A8 runtime artifact | low-medium | end-to-end latency, memory, throughput, energy, deployment data |
| Neural Networks / Information Sciences | extended journal version | medium | more ablations, faithful baselines, and statistical consolidation |

## What A Strong Reviewer Will Ask

1. Does CSI only measure instability, or does it improve a decision?
2. Are the findings specific to one prompt pool?
3. Are the findings specific to Qwen2.5?
4. How does this compare to existing PTQ calibration robustness or data
   selection work?
5. Are AutoAWQ and GPTQModel baselines faithful and matched?
6. Are reported improvements task-visible, not just proxy-visible?
7. Can another lab reproduce the gates without hidden local state?

## Current Answers

| Question | Current answer | Confidence |
|---|---|---:|
| Does CSI measure instability? | yes, with seed-pair metrics, bootstrap trend gates, and null permutation gates | high |
| Does CSI improve downstream allocation? | not yet proven | low |
| Is it prompt-pool general? | not yet; current Qwen2.5 curves are same-prompt-pool artifacts | low |
| Is it model-family general? | partial; broader earlier diagnostics exist, but the clean n-curve/cross-scale story is Qwen2.5-centered | medium-low |
| Are official baselines present? | AutoAWQ/GPTQModel task/runtime evidence exists for Qwen2.5-1.5B | medium |
| Is there production runtime evidence? | no | high |

## 2026-06-14 Related-Work Scan

The current online scan is recorded in:

- `docs/RELATED_WORK_AND_GAP_SCAN_2026_06_14.md`

Main update:

```text
The closest defensible gap is not "a better quantizer." It is an auditable
diagnostic for calibration split instability in module-sensitivity rankings,
positioned beside GPTQ/AWQ/SmoothQuant/OmniQuant, rotation-family PTQ,
calibration-data impact studies, and LLMC-style benchmark/toolkit work.
```

This strengthens the reviewer answer to question 4, but it does not close the
downstream-retention, second-prompt-pool, or faithful-baseline gaps.

## 2026-06-13 IFEval Probe

A small Qwen2.5-1.5B IFEval probe was attempted after this gap map was created.
AutoAWQ and GPTQModel completed the 8-row deterministic IFEval fixture under
GPU guard, but the matched FP16 row timed out while loading/materializing the
incomplete local Hugging Face cache. The partial result is recorded at:

- `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_IFEVAL_PARTIAL_2026_06_13.md`

This does not close the IFEval retention gap. It narrows the next action to
materializing a complete FP16 local snapshot and rerunning the same fixture.

## Priority Experiments

1. Downstream-retention gate:
   Qwen2.5-1.5B, CSI `n=8` or robust-consensus allocation, compare against
   FP16, AutoAWQ, and GPTQModel on Broad20x20 and GSM8K500 if disk/GPU budget
   permits.
2. Second prompt pool:
   repeat Qwen2.5-1.5B CSI `n=2/4/8` on C4 prompts.
3. Model-family extension:
   choose one additional small open model where storage and runtime are
   manageable, then run the same CSI curve.
4. Baseline breadth:
   add a SmoothQuant-style or rotation-family baseline only after confirming
   the implementation can be audited and rerun.
5. Systems split:
   keep ESMP/W4A8 runtime work separate until there is end-to-end latency and
   memory evidence.

## Drafting Guidance

For AAAI/IJCAI/TMLR, the abstract should avoid "new quantizer" framing. Use:

```text
We introduce an auditable diagnostic for calibration split instability in
mixed-precision LLM quantization and show that calibration size materially
changes module-ranking stability in current Qwen2.5 artifacts.
```

Avoid:

```text
We achieve state-of-the-art quantization or deployment speed.
```

The next writing milestone is not more prose. It is a table that links each
venue-facing claim to a gate, a result artifact, and a reviewer objection.
