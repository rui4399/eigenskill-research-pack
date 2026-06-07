# AAAI-27 Critical Path

Date: 2026-06-08

This note compresses the current reviewer feedback into one execution rule:
ship the AAAI quantization-robustness story first, and keep the systems story as
a gated backup until end-to-end latency is actually faster than FP16.

Official AAAI-27 dates are AoE/UTC-12: abstracts due 2026-07-21, full papers
due 2026-07-28, and supplementary material/code due 2026-07-31.

Source: https://aaai.org/conference/aaai/aaai-27/

## Veto-First Decision

The optimized submission strategy is to avoid a hybrid "algorithm plus systems"
paper until the system path has end-to-end speed evidence. AAAI gets the
statistical story: calibration split instability, uncertainty-aware evaluation,
and conservative consensus allocation. The packed-runtime/Triton/bypass work
stays as artifact evidence and a separate systems-paper track unless it clears
all runtime gates below.

This means the next experiment priority is not another draft and not another
kernel-only speed row. It is a matched downstream-retention row on real
quantized variants:

```text
FP16 vs AutoAWQ vs GPTQModel vs CSI allocation
same model, same public calibration, same task fixture, same guard.
```

The systems track can be promoted only when it reports physical file size,
peak VRAM, TTFT, and tokens/s for the same model against an FP16 baseline.

## Mainline Submission Story

The AAAI-facing paper should be:

```text
Calibration Split Instability in Mixed-Precision LLM Quantization
```

The paper's center of gravity is statistical robustness, not a new quantizer and
not a production runtime. The systems evidence can appear only as a bounded
artifact section unless it proves end-to-end speedup.

## Reviewer Vetoes

| veto | why it can reject the paper | required closure |
|---|---|---|
| Only tiny task subsets. | Reviewers can call the result a toy diagnosis. | Full GSM8K is now covered for both the local 7B public-task row and the guarded Qwen2.5-1.5B FP16/AutoAWQ/GPTQModel row; MMLU has progressed from Broad5x20 to Broad20x20, but full MMLU/IFEval remain open. |
| Native baseline confrontation is still incomplete. | Random and proxy baselines are too weak; current AutoAWQ/GPTQModel rows are local evidence, not full competition. | Full GSM8K matched retention is now covered for Qwen2.5-1.5B; add SmoothQuant or a rotation-family row if feasible. |
| Scale row is public-task only. | The new 7B Ollama row improves model-scale coverage but is not quantized-retention evidence. | Add one quantized 3B/7B or broader 1.5B row if the guard can hold. |
| End-to-end quantized runtime is slower. | Systems reviewers will reject any acceleration claim. | Keep speed claims kernel-only until TTFT/tokens/s beats FP16 in a minimal runtime. |
| Math looks like prose. | The CSI contribution reads as a heuristic. | Promote estimator noise, rank-inversion, bootstrap CI, permutation null, and Holm correction into display equations. |

## Optimized Response To External Critique

The project should treat the critique as a routing problem, not as a request to
merge every direction into one paper.

| track | promote only if | paper role now |
|---|---|---|
| CSI/statistical robustness | equations, seed/bootstrap artifacts, and matched PTQ task retention all stay claim-aligned | AAAI mainline |
| Native PTQ retention | FP16/AutoAWQ/GPTQModel run on the same prompts with paired uncertainty intervals | AAAI evidence table |
| ESMP/Triton kernels | kernel speedup plus real packed-file size and bounded reconstruction drift are both reported | artifact/appendix only |
| Minimal runtime | quantized path beats FP16 on TTFT, tokens/s, and peak VRAM outside hook-based fake quant | separate systems paper |
| Hybrid bypass | token-layer heatmap and per-token latency staircase show a measured skip benefit | separate routing paper |

Hard rule: a systems result that is kernel-fast but end-to-end-slower must be
presented as an integration-risk finding, not as a speedup. Conversely, the
AAAI paper does not need to solve runtime acceleration if it cleanly establishes
calibration split instability and measured retention under native PTQ baselines.

## P0 Work Before Writing

1. **Theory polish.** Convert Section 4 and statistical testing into LaTeX-ready
   equations:
   - sensitivity estimator and calibration noise;
   - Chebyshev/Hoeffding-style estimation error;
   - pairwise rank-inversion probability;
   - bootstrap confidence intervals;
   - null-permutation p-values and Holm-adjusted rejection.
   The draft already has a first equation pass; the remaining work is to trim it
   to the AAAI page budget and ensure every symbol is defined once.

2. **Native PTQ baselines.** Expand the current AutoAWQ/GPTQModel evidence from
   readiness/smoke into matched task/PPL rows. The table must separate:
   FP16, uniform W4, AutoAWQ W4/G128, GPTQModel W4/G128, and CSI allocation.

3. **Task retention.** Move beyond subset100. Full GSM8K is now measured for
   the local 7B public-task path and for actual Qwen2.5-1.5B FP16/AutoAWQ/
   GPTQModel variants. A guarded twenty-subject MMLU Broad20x20 row now broadens
   the abstract-algebra-only evidence; the next target is full MMLU or IFEval
   under the same matched guard protocol.

4. **Scale.** Keep the committed Qwen2.5-abliterate-7B public-task row as
   scale coverage. The next upgrade is quantized retention at 3B/7B scale, or
   broader 1.5B task coverage if local 8GB VRAM blocks it.

5. **CSI-vs-n figure.** Extend the current n=2/4/8 curve if cheap. The most
   valuable figure is stability versus calibration size with bootstrap bands.

## Systems Backup Track

Do not make systems the main AAAI story unless all three gates pass:

1. **Real packed file:** export a real `.eqm`/ESMP artifact and report physical
   file size versus FP16.
2. **Minimal runtime:** run a small forward/generation path outside heavy
   PyTorch hook-based fake quantization.
3. **End-to-end win:** report TTFT, tokens/s, and peak VRAM where the quantized
   path beats FP16. If it remains slower, present it only as integration risk.

Kernel evidence that is currently valid:

- W4A8 shape-family kernels are faster than torch FP16 on bounded local RTX 5070
  GEMM shapes.
- Real Qwen3 activation reconstruction has bounded selected-module drift.

Kernel evidence that is not yet valid:

- full-model quality retention;
- end-to-end generation acceleration;
- mobile/Redmi deployment;
- energy reduction.

## Bypass Backup Track

Bypass should not be merged into the AAAI main claim. It needs its own evidence:

- token-by-layer execution heatmap;
- per-token latency staircase;
- exact parser coverage and failure modes;
- comparison against model-only constrained decoding.

Until those are present, bypass is a separate paper track, not a mainline claim.

## Claim Promotion Rule

A claim can enter the paper only when all four exist:

1. a committed JSON artifact;
2. a generated Markdown gate report;
3. a reproducible command in the runbook;
4. a boundary row in `docs/PAPER_CLAIM_MATRIX.md`.

Anything else stays in future work.

## Next Execution Order

1. Extend the new Qwen2.5-1.5B FP16/AutoAWQ/GPTQModel MMLU Broad20x20 row toward
   either full MMLU or IFEval under the same sharded `--offset` and
   `merge_chat_task_shards.py` protocol.
2. Upgrade the 7B public-task row into quantized retention only if disk and
   VRAM headroom are safe; otherwise broaden the 1.5B matched PTQ matrix.
3. Add a downstream proxy for W4A8 activation quantization before using the
   extended attention/MLP drift audit in any quality argument.
4. Update the paper only after the new gates pass.
