# Related Work And Gap Scan 2026-06-14

This note records the current online literature scan for the CSI paper route.
It is a positioning and review-prep artifact, not evidence that EigenSkill-Q
beats or fully reproduces any of the systems below.

## Search Scope

Scan date: 2026-06-14.

Search focus:

- LLM post-training quantization under small calibration sets.
- Calibration data sensitivity, selection, and robustness.
- GPTQ/AWQ/SmoothQuant/OmniQuant/rotation-family baselines.
- Mixed-precision allocation and benchmark-toolkit papers.

The useful framing after this scan is:

```text
Existing work mostly optimizes PTQ algorithms, calibration transforms, or final
task metrics. The CSI paper should focus on a narrower missing diagnostic:
whether tiny calibration splits produce stable module-sensitivity rankings
before those rankings are used for allocation.
```

## Literature Map

| Work | What it contributes | Calibration assumption or surface | Gap relative to CSI |
|---|---|---|---|
| [GPTQ](https://arxiv.org/abs/2210.17323) | One-shot weight quantization using approximate second-order information for large generative transformers | Uses calibration activations for block/layer reconstruction-style weight quantization | Strong baseline family, but the paper does not make calibration split ranking stability the main object of measurement |
| [SmoothQuant](https://arxiv.org/abs/2211.10438) | Training-free W8A8 PTQ by migrating activation outlier difficulty into weights | Offline activation statistics drive equivalent smoothing transforms | Important activation-outlier baseline; CSI should not claim activation-quantization novelty |
| [AWQ](https://arxiv.org/abs/2306.00978) | Activation-aware low-bit weight quantization that protects salient channels through scaling | Salient channels are identified using activation distributions collected offline | Directly relevant because activation statistics drive protection decisions; CSI asks whether small prompt samples make such sensitivity/protection decisions unstable |
| [OmniQuant](https://arxiv.org/abs/2308.13137) | Block-wise PTQ with learnable weight clipping and learnable equivalent transforms | Optimizes quantization parameters using calibration samples and block-wise error minimization | Stronger calibration-aware PTQ family; CSI should compare as related calibration optimization, not as proof of downstream retention |
| [On the Impact of Calibration Data in PTQ and Pruning](https://arxiv.org/abs/2311.09755) | Empirical study showing calibration data can materially affect compression outcomes | Treats calibration data choice as an explanatory variable for downstream compression performance | Closest related work; CSI narrows the lens from final performance variance to the intermediate ranking/allocation instability that can explain why choices drift |
| [QuaRot](https://arxiv.org/abs/2404.00456) | Rotation-based 4-bit inference for weights, activations, and KV cache; includes calibration-free RTN settings at higher bits | Reduces outliers through output-preserving rotations rather than selecting retained high-precision channels | Rotation-family baseline; CSI should avoid claiming outlier-removal or W4A4/KV novelty |
| [SpinQuant](https://arxiv.org/abs/2405.16406) | Learned rotations for LLM quantization; shows rotation choice can change downstream reasoning performance | Optimizes rotation matrices to improve quantized accuracy | Useful reviewer contrast: if random rotation choice can move downstream metrics, calibration split choice can plausibly move ranking decisions, but this remains a hypothesis until downstream retention is tested |
| [LLMC](https://arxiv.org/abs/2405.06001) | Benchmarking and toolkit paper covering algorithms, calibration data, formats, and mixed precision | Compares quantization configurations more systematically than single-method papers | Good benchmark-toolkit reference; CSI can be positioned as a complementary gate that reports split-stability before claiming fair downstream comparisons |
| [ZeroQuant](https://arxiv.org/abs/2206.01861) | Efficient PTQ/quantization framework for large transformers with layer-wise knowledge distillation and hardware-oriented goals | Uses calibration/training-free or lightweight data paths depending on setting | Systems/compression context only; not a direct CSI comparator unless the repo adds a faithful implementation |

## Reviewer-Relevant Synthesis

### What Existing Work Already Covers

- High-quality PTQ algorithms exist; EigenSkill-Q should not present itself as
  a new SOTA quantizer.
- Activation-aware and transform-based methods already use calibration
  activations in sophisticated ways.
- Calibration data has already been shown to affect compression outcomes in
  downstream metrics.
- Benchmark/toolkit work already warns that fair quantization comparisons need
  standardized configurations.

### What The CSI Route Can Still Own

- A small, auditable diagnostic that asks whether module-sensitivity rankings
  are stable across equally plausible calibration prompt samples.
- Seed-pair rank and set-overlap metrics before allocation decisions are
  promoted to paper claims.
- Gate artifacts that force the paper to separate diagnostic evidence from
  downstream retention evidence.
- A reviewer-facing failure mode: if small calibration splits induce different
  high-precision module choices, then a single allocation ranking is
  under-supported.

## Claim Boundary After The Scan

Safe wording:

```text
CSI is a diagnostic for calibration split instability in module-sensitivity
rankings. In the current Qwen2.5 same-prompt-pool artifacts, increasing
calibration prompt count improves seed-pair ranking stability.
```

Unsafe wording:

- CSI is a new SOTA PTQ method.
- CSI-derived allocation improves downstream task retention.
- The observed Qwen2.5 cross-scale gap proves a universal model-size law.
- Current ESMP or C++ probes are production deployment evidence.
- Partial IFEval AWQ/GPTQModel rows close the matched FP16 retention gap.

## Falsification Checklist

The paper should explicitly name evidence that could weaken or falsify its
current story:

1. A second public prompt pool does not reproduce the n=2/4/8 stability trend.
2. Another model family shows stable rankings even at very small n.
3. Downstream task retention is insensitive to the ranking instability measured
   by CSI.
4. A faithful AWQ/GPTQ/SmoothQuant/rotation baseline makes the same allocation
   decision across calibration splits.
5. CSI-informed or robust-consensus allocation fails against a simpler
   allocation heuristic under a matched bit budget.

## Near-Term Paper Edits

- Add related-work language that treats GPTQ/AWQ/SmoothQuant/OmniQuant as
  algorithm baselines, not defeated baselines.
- Cite the calibration-data impact paper as the closest conceptual neighbor.
- Use LLMC as the benchmark/toolkit anchor for why standardized settings matter.
- Keep QuaRot and SpinQuant in a separate rotation/outlier paragraph.
- Put the falsification checklist near limitations or reviewer-risk sections.
