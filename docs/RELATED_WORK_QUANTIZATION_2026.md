# Quantization Related Work Map, 2026-06-06

This note keeps the paper story grounded against recent LLM quantization work.
It is a worklist for baselines and positioning, not evidence that EigenSkill-Q is
competitive with these systems yet.

## Mixed-Precision Allocation

- [Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment](https://arxiv.org/abs/2509.20214)
  Relevant because it directly studies fractional-bit quantizers and
  resource-constrained allocation. EigenSkill-Q must not claim novelty merely
  for assigning mixed bit widths; the defensible delta is calibration split
  instability and gated system evidence.
- [IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs](https://arxiv.org/abs/2509.15455)
  Relevant because it models interaction among layer choices rather than treating
  each layer independently. EigenSkill-Q currently uses module-level sensitivity
  and consensus; interaction-aware allocation is an important baseline or
  extension.
- [WINDQuant: Weight-Informed Neural Decision-Making for Global Mixed-Precision LLM Quantization](https://arxiv.org/abs/2605.26660)
  Relevant as a 2026 global mixed-precision allocation direction. Treat as a
  fresh arXiv baseline candidate, not a settled benchmark standard.
- [Mixed-Precision Graph Neural Quantization for Low Bit Large Language Models](https://arxiv.org/abs/2501.18154)
  Relevant because it treats allocation as a graph/dependency problem. It is a
  natural comparator for the claim that sensitivity ranking alone is unstable.
- [GANQ: GPU-Adaptive Non-Uniform Quantization for Large Language Models](https://arxiv.org/abs/2501.12956)
  Relevant because it ties non-uniform quantization to hardware-efficient
  lookup-table mpGEMM. EigenSkill-Q's ESMP/Triton direction should be compared
  against hardware-aware non-uniform quantization, not only allocation heuristics.

## Calibration-Free And Low-Calibration PTQ

- [SINQ: Sinkhorn-Normalized Quantization for Calibration-Free Low-Precision LLM Weights](https://arxiv.org/abs/2509.22944)
  Relevant because calibration-free quantization attacks the same pain point
  from the opposite direction: avoid calibration dependence rather than robustly
  aggregating multiple calibration views.
- [Q-Palette](https://arxiv.org/abs/2509.20214) also matters here because its
  setup uses little or no calibration data.

## Rotation And Outlier Mitigation

- [QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs](https://arxiv.org/abs/2404.00456)
  Relevant because it makes 4-bit weight/activation/KV quantization easier by
  applying rotations that preserve full-precision computation.
- [SpinQuant: LLM Quantization with Learned Rotations](https://arxiv.org/abs/2405.16406)
  Relevant because learned rotations improve over fixed rotations and are a
  strong baseline family for low-bit activation/KV settings.
- [BASE-Q: Bias and Asymmetric Scaling Enhanced Rotational Quantization for Large Language Models](https://arxiv.org/abs/2506.15689)
  Relevant as a newer rotation-family method addressing limitations of pure
  rotation.
- [ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference](https://arxiv.org/abs/2511.10645)
  Relevant because it combines optimizable Givens rotations, channel-wise
  scaling, and kernel co-design for reasoning models. It is a strong warning
  that rotation methods should be evaluated jointly with runtime overhead, not
  only proxy sensitivity reduction.

## KV Cache And Long-Context Quantization

- [KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference](https://arxiv.org/abs/2502.04420)
  Relevant because it applies sensitivity-aware mixed precision to KV cache.
  EigenSkill-Q's QKV replacement and selected-row runtime evidence should stay
  separate from KV-cache quantization claims until comparable KV experiments are
  added.
- [Rotate, Clip, and Partition: Towards W2A4KV4 Quantization](https://aclanthology.org/2025.findings-emnlp.400/)
  Relevant for combined low-bit weight, activation, and KV settings.

## Numeric Formats And Kernel Co-Design

- [Benchmarking Post-Training Quantization of Large Language Models under Microscaling Floating Point Formats](https://arxiv.org/abs/2601.09555)
  Relevant because it studies PTQ under MXFP formats across multiple algorithms,
  benchmarks, and model families. EigenSkill-Q currently uses integer fake-quant
  diagnostics; MXFP4/MXFP8 behavior is a separate baseline family before making
  claims about modern low-precision formats.
- [LUT Tensor Core: Lookup Table Enables Efficient Low-Bit LLM Inference Acceleration](https://arxiv.org/abs/2408.06003)
  Relevant because it frames low-bit inference around mpGEMM and lookup-table
  hardware/software co-design. It is not a direct software baseline for the
  current repo, but it helps define what a real systems contribution would need
  beyond Python fake-quant and module-level microbenchmarks.

## Positioning Rule For EigenSkill-Q

Do not position the current repository as a new SOTA quantizer. The current
paper-facing angle is narrower:

```text
Calibration split instability is measurable across multiple small public model
families, and consensus sensitivity allocation plus gated packed-system evidence
is a reproducible baseline for studying that instability.
```

Required next baselines:

- compare against at least one rotation-family PTQ method (`QuaRot` or
  `SpinQuant`; `ParoQuant` if reasoning/runtime co-design claims are made) when
  activation/KV claims are made;
- compare against at least one allocation-family method (`Q-Palette`, `IMPQ`, or
  a practical AWQ/GPTQ-style baseline with explicit bit allocation);
- add a hardware-aware non-uniform quantization baseline (`GANQ`-style or
  LUT/mpGEMM-inspired) before claiming kernel-level competitiveness;
- add MXFP-format diagnostics before claiming relevance to MXFP4/MXFP8 PTQ;
- add public task benchmarks beyond PPL before claiming capability retention;
- keep ESMP/Triton runtime claims separate from fake-quant PPL claims.
