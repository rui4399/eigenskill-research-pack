# Paper Targets And Readiness

Date: 2026-06-07

This file is the single publication-readiness note for the public repository.
Older venue lists were folded here so the project does not present several
competing submission stories.

## Current Defensible Contribution

The strongest current paper direction is:

```text
Calibration split instability in mixed-precision LLM quantization, with
consensus sensitivity allocation and gated packed-system evidence.
```

The current evidence supports:

- calibration-split instability diagnostics on Qwen3-0.6B, Qwen3-1.7B,
  OLMo-2-0425-1B-Instruct, and SmolLM2-1.7B boundary cases;
- WikiText2/C4 short-slice fake-quant PPL comparisons and random-repeat
  allocation audits around the 4.5 average-bit budget;
- budget and robustness gates for mean consensus, robust-LCB, transfer
  boundaries, and bounded interaction-aware swap search;
- a Qwen2.5-0.5B calibration prompt-seed stability gate showing 6 sampled
  prompt selections, 15 pairwise comparisons, mean Spearman 0.4324 with
  bootstrap 95% CI [0.3557, 0.5174], and minimum top-20 Jaccard 0.3793 under
  the same 16-prompt WikiText2 pool;
- a Qwen2.5-0.5B CSI-vs-calibration-size gate over six-seed n=2/4/8 prompt
  samples, where mean Spearman rises 0.3725 -> 0.4324 -> 0.6645 and mean
  top-20 Jaccard rises 0.3797 -> 0.4672 -> 0.6449;
- a Qwen2.5-0.5B CSI trend-significance gate showing positive n=8-vs-n=2
  bootstrap mean-gain CIs across Spearman/top-20/positive-set stability, with
  minimum lower CI bound 0.1352 and minimum random pair dominance probability
  0.9422;
- a Qwen2.5-0.5B CSI null-permutation gate showing that the same full-range
  stability gains reject a pooled n=2/n=8 label-shuffle null with maximum
  Holm-adjusted p-value 0.000149993 under 20,000 Monte-Carlo samples;
- a rank-inversion theory gate over the same n=2/4/8 artifacts, where mean
  empirical inversion falls 0.2418 -> 0.1442 and top-quartile-margin inversion
  falls 0.0969 -> 0.0427 under a Chebyshev-style variance/gap proxy;
- a Q-Palette-style closed-form Lagrangian allocation proxy over measured Qwen3
  and Qwen2.5 sensitivity artifacts, gated for finite lambda, budget use, and
  non-trivial bit histograms;
- a public-calibrated AutoAWQ W4 group-128 readiness bundle on
  Qwen2.5-0.5B-Instruct with tiny public WikiText2/C4 matched PPL slices;
- expanded 16-prompt-per-split AutoAWQ and GPTQModel public PPL gates for the
  same public-calibrated Qwen2.5-0.5B W4/G128 setting, aligned in the official
  PTQ readiness matrix;
- a Qwen2.5-1.5B AutoAWQ W4/G128 public-calibration scale-up smoke that
  quantizes under an 85% VRAM guard and evaluates 16 WikiText2 plus 16 C4 public
  PPL prompts with max PPL ratio 1.1344;
- a Qwen2.5-1.5B FP16-vs-AutoAWQ matched 20-row public MMLU/GSM8K task subset
  matrix, covering 80 task executions with no measured accuracy drop versus
  FP16 in this tiny local slice and peak guarded VRAM ratio 0.6821;
- a Qwen2.5-1.5B FP16/AutoAWQ/GPTQModel matched 100-row public MMLU/GSM8K task
  subset matrix, covering 600 task executions: FP16 gets 33/100 MMLU and
  12/100 GSM8K, AutoAWQ gets 34/100 MMLU and 11/100 GSM8K, GPTQModel gets
  25/100 MMLU and 8/100 GSM8K, max drop versus FP16 is 0.08, and peak guarded
  VRAM falls from 6531 MiB to 4919 MiB for AutoAWQ and 5438 MiB for GPTQModel
  while both quantized local loader paths are slower than FP16;
- a larger Qwen2.5-1.5B FP16/AutoAWQ/GPTQModel GSM8K200/MMLU100 task-retention
  matrix, covering 900 task executions: FP16 gets 33/100 MMLU and 19/200
  GSM8K, AutoAWQ gets 34/100 MMLU and 22/200 GSM8K, GPTQModel gets 25/100 MMLU
  and 20/200 GSM8K, with max measured drop 0.08 versus FP16 and peak guarded
  VRAM ratio 0.8295;
- a full Qwen2.5-1.5B FP16/AutoAWQ/GPTQModel GSM8K1319 task-retention row,
  covering 3957 task executions over all 1319 GSM8K test rows: FP16 gets
  107/1319, AutoAWQ gets 104/1319, GPTQModel gets 96/1319, with max measured
  drop 0.00834 versus FP16 and peak guarded VRAM ratio 0.8295;
- a paired statistical-interval gate over the same Qwen2.5-1.5B matrix:
  AutoAWQ-minus-FP16 delta is +0.015 with 95% bootstrap CI [-0.035, +0.065] on
  GSM8K and +0.010 with CI [-0.100, +0.120] on MMLU; GPTQModel-minus-FP16 delta
  is +0.005 with CI [-0.040, +0.050] on GSM8K and -0.080 with CI [-0.190,
  +0.030] on MMLU, reported as uncertainty disclosure rather than superiority
  evidence;
- a representative 7B public-task coverage row through Ollama
  Qwen2.5-abliterate-7B, covering 100 MMLU abstract-algebra rows plus 200 GSM8K
  rows under guard: 84/300 total passes, mean throughput 19.9987 tokens/s, mean
  TTFT 0.478812 s, and peak guarded VRAM ratio 0.7135;
- a full single-task GSM8K coverage row for the same Ollama 7B model, covering
  all 1319 GSM8K test rows under guard: 183/1319 passes, mean throughput
  16.8942 tokens/s, mean TTFT 0.463880 s, and peak guarded VRAM ratio 0.6934;
- a local matched AutoAWQ/GPTQModel Qwen2.5-0.5B W4/G128 baseline pack that
  ties public-calibration PPL, subset50 MMLU/GSM8K execution, and PC-side
  runtime/VRAM into one explicit claim boundary;
- a true 100-row matched official PTQ subset gate over the same
  FP16/AutoAWQ/GPTQModel Qwen2.5-0.5B variants, covering 600 public MMLU/GSM8K
  executions with max drop 0.03 versus FP16 and a paired PC-side runtime profile;
- deterministic IFEval-style execution and runtime smoke gates for the same
  FP16/AutoAWQ/GPTQModel Qwen2.5-0.5B variants, treated as execution-path
  evidence because the FP16 baseline is 0/8;
- ESMP package integrity, Triton shape-family kernels, selected-row probes, and
  shallow generation integration gates;
- W4A8 real-activation reconstruction gates on selected Qwen3-0.6B modules:
  the first self-attention-only gate bounds added A8 drift at 0.048561 rel-L2,
  while the 24-module attention/MLP extension reports max added drift 0.084533
  and exposes MLP down projections as the worst integration-risk cases;
- explicit gap tracking for official baselines, task retention, and mobile
  deployment.

The current evidence does not support a broad quantization-method claim, a
production runtime claim, or a real-device deployment claim.

## Best-Fit Near-Term Venues

These are fit hypotheses, not acceptance claims. School and CCF/CAS recognition
rules drift, so verify the latest official list before choosing a target.

## AAAI-27 Sprint Window

The official AAAI-27 timetable lists all author deadlines as UTC-12: author
registration opens on 2026-06-17, paper submission opens on 2026-06-24,
abstracts are due on 2026-07-21, full papers are due on 2026-07-28, and
supplementary material/code is due on 2026-07-31. Treat the internal freeze as
at least 48 hours earlier than each official deadline.

Source: `https://aaai.org/conference/aaai/aaai-27/`

Current AAAI-facing critical path:

1. Theory: keep the estimator-noise, trend-significance, permutation-null, and
   Chebyshev inversion-risk CSI sections concise and tied to the measured
   seed/bootstrap artifacts.
2. Real quantization: expand the AutoAWQ/GPTQModel matched pack beyond the
   0.5B readiness setting and report negative runtime results honestly.
   Qwen2.5-1.5B now has public-calibration AutoAWQ/GPTQModel PPL readiness,
   matched FP16/AutoAWQ/GPTQModel subset100, GSM8K200/MMLU100, sharded
   GSM8K500, and full GSM8K1319 task/runtime matrices, with paired uncertainty
   reporting. SmoothQuant,
   rotation baselines, broader subjects, and full benchmark retention still need
   scale-up.
3. Downstream tasks: full GSM8K is now measured for the local 7B public-task
   path; move next toward broader MMLU/IFEval and stronger retention on actual
   quantized variants.
4. Scale: keep the committed 7B public-task row as coverage evidence; upgrade
   it to quantized retention only if the 8GB local GPU can hold the run, else
   broaden the 1.5B matched PTQ matrix.
5. Figures: promote the committed CSI-vs-calibration-size SVG/JSON into the
   paper figure pipeline, then add bootstrap bands or a larger n grid if time
   allows.

See `docs/AAAI_2027_CRITICAL_PATH.md` for the current veto-first execution
order. It deliberately keeps the AAAI quantization-robustness paper separate
from the systems-runtime backup track until end-to-end TTFT/tokens/s evidence
beats FP16.

| Route | Why it fits | What must improve first |
|---|---|---|
| ACL Findings / EMNLP Findings / COLING | Compression diagnostic, calibration robustness, public task subsets. | Larger slices, stronger task retention, clearer baseline table. |
| AAAI / IJCAI | Resource-aware optimization with empirical robustness. | Official AWQ/GPTQ or faithful comparator, more seeds, more models. |
| TMLR | Clean problem definition plus negative evidence and ablations. | Stronger theory/variance framing and reproducible baseline package. |
| Neural Networks / Information Sciences | Journal-length robustness and optimization study. | Broader model ladder, statistical tests, official baselines. |
| Engineering Applications of Artificial Intelligence | Engineering artifact with gated systems evidence. | Runtime or device metrics beyond module-level probes. |
| Efficient-LLM / model-compression workshops | Short-cycle artifact release and focused feedback. | Clean tables, exact scripts, and conservative claims. |

Avoid positioning the current artifact for ASPLOS/ISCA/MICRO/OSDI-style systems
venues until there is real runtime integration, end-to-end TTFT/tokens/s, memory
and power evidence. Avoid TNNLS/TPAMI-style claims until the theory and task
evidence become much deeper.

## Not Ready For Mainline Submission

The blockers are concrete:

1. Official baselines: the local AutoAWQ/GPTQModel 0.5B matched pack, expanded
   16-prompt public PPL gates, and Qwen2.5-1.5B matched FP16/AutoAWQ/GPTQModel
   subset100 plus GSM8K200/MMLU100 rows are useful but not enough; SmoothQuant,
   at least one faithful rotation or mixed-precision allocation comparator, and
   broader task subjects are still missing.
2. Larger evaluation: more WikiText2/C4 prompts and broader calibration-seed sweeps.
3. Downstream retention: broader MMLU/IFEval or similar task slices on the
   actual quantized/fused variants; full GSM8K is measured for both the local
   Ollama 7B public-task path and Qwen2.5-1.5B FP16/AutoAWQ/GPTQModel PTQ
   variants, current IFEval-style evidence is only an 8-row
   deterministic execution smoke, and current public PTQ task evidence is still
   local subset coverage rather than leaderboard-scale.
4. Statistical robustness: the first n=2/4/8 CSI curve, trend-significance
   gate, permutation-null gate, and rank-inversion theory gate are now
   committed, but larger n grids, more prompt pools, and
   consensus-vs-single-split confidence intervals are still needed.
5. Runtime evidence: packed quantized weights integrated into an inference path;
   PyTorch fake quant cannot justify latency, memory, or energy claims.
6. Mobile evidence: Redmi K80 Pro or another real device needs TTFT, tokens/s,
   peak memory, thermal and power logs before any deployment language is used.

## Near-Term Artifact Path

The next credible public milestone is a technical report or workshop artifact:

```text
Calibration Split Instability in Mixed-Precision LLM Quantization:
Consensus Sensitivity Allocation with Gated Packed-System Evidence
```

Before releasing that version:

- scale the public-calibrated AutoAWQ/GPTQModel pack beyond tiny slices and
  beyond Qwen2.5-0.5B;
- add SmoothQuant and at least one faithful rotation-family or allocation
  comparator under the same calibration and evaluation protocol;
- rerun core fake-quant rows with more calibration seeds;
- include the budget-curve figure from `outputs/consensus_budget_curve.svg`;
- keep C++ reporting tools framed as reproducibility infrastructure unless tied
  to measured kernel/runtime gates.

## Stronger Paper Shape

A stronger journal or recognized-conference version should define:

- a noisy sensitivity estimator `s_i(D)` over calibration data;
- a consensus estimator across calibration distributions or splits;
- a constrained bit-allocation objective under a fixed average-bit budget;
- a robustness objective over calibration perturbations;
- downstream risk measured by PPL and task degradation.

The systems contribution should remain scoped until the runtime catches up:

- ESMP packaging and C++ inspection are real artifact infrastructure;
- Triton and selected-row kernels are module-level probes;
- no end-to-end speed or mobile claim should appear without physical
  measurements.
