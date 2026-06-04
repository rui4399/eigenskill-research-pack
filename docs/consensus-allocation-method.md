# Cross-Dataset Consensus Allocation

This note defines the current `wikitext_c4_consensus` allocation used in the
Qwen3-1.7B and OLMo2-1B fake-quant diagnostics.

It is a stability heuristic for short-cycle experiments, not a production
quantizer.

## Inputs

For each Linear module `i`, the sensitivity probe quantizes only that module to
INT4, restores the original weight, and records the short-prompt loss increase:

```text
delta_i(D) = max(NLL(W_i -> Q4(W_i); D) - NLL(W; D), 0)
```

The current runs use two calibration datasets:

```text
D_left  = WikiText2 calibration prompts
D_right = C4 calibration prompts
```

Each split first builds a budgeted `{4,8}` allocation with the same weighted
average-bit budget:

```text
sum_i cost_i * bits_i <= B * sum_i cost_i
B = 4.5
bits_i in {4, 8}
```

## Consensus Score

For the consensus file, each module receives an average positive-loss score:

```text
score_i = 0.5 * (delta_i(D_left) + delta_i(D_right)) / cost_i
```

The allocator first locks modules selected as 8-bit by both split allocations
when they fit the budget. It then fills the remaining budget by descending
`score_i`.

This means the allocation is not simply the union of two high-bit sets. It
prioritizes intersection stability first, then spends the remaining budget on
average loss-per-cost.

## Current Evidence

The current evidence is positive on two model families:

```text
Qwen3-1.7B:
WikiText2-64 consensus PPL 26.3260 vs best listed random 27.6685
C4-64        consensus PPL 28.3303 vs best listed random 28.4562

OLMo2-0425-1B-Instruct:
WikiText2-64 consensus PPL 21.0349 vs best listed random 21.4637
C4-64        consensus PPL 35.4726 vs best listed random 35.8512
```

The important claim is narrow: cross-dataset consensus improves this repository's
short-slice fake-quant diagnostic over the earlier one-split allocation and the
listed random repeats. It does not establish a compressed runtime, hardware
speedup, or superiority over GPTQ/AWQ/SmoothQuant/QuaRot-style baselines.

## C++ Audit

The allocation stability audit is implemented in:

```text
inference_cpp/src/quant_consensus_audit.cpp
```

It reports high-bit counts, bit histograms, weighted average bits, budget use,
and high-bit Jaccard overlap between the left, right, and consensus allocations.
Read this audit together with downstream PPL matrices from:

```text
inference_cpp/src/quant_evidence_matrix.cpp
```
