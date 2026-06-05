# Qwen3-1.7B WikiText2-128 Consensus-vs-Random16 Result

This run extends the previous Qwen3-1.7B short-slice diagnostics from 64
WikiText2 prompts to 128 prompts while keeping the same fake-quant setting:

```text
model: Qwen/Qwen3-1.7B
dataset: WikiText2 validation, 128 prompts
max length: 256
dtype: FP16
weight fake quantization: per-row/group128
target: wikitext_c4_consensus
random baselines: 16 random budget allocations
```

## Result

```text
FP16 PPL:                   20.2931
uniform INT4 PPL:           28.2125
wikitext_c4_consensus PPL:  24.2065
best random16 PPL:          25.1876
random16 mean PPL:          26.0827
random16 max PPL:           28.1645
```

Margins:

```text
target vs uniform INT4:     +4.0060 PPL
target vs best random16:    +0.9811 PPL
target vs random16 mean:    +1.8762 PPL
```

## Interpretation

The cross-dataset consensus allocation remains positive on the longer
WikiText2-128 slice and beats all 16 random budget allocations in this run.
This strengthens the current claim that consensus allocation is more robust
than one short calibration split or unstructured random budget placement.

This is still a PyTorch fake-quant diagnostic. It does not claim packed
runtime speedup, board-level energy improvement, GPTQ/AWQ superiority, or
production quantized inference.

## Artifacts

```text
outputs/qwen3_1p7b_wikitext_c4_consensus_random16_ppl_wikitext2_128_summary.json
outputs/qwen3_1p7b_wikitext_c4_consensus_random16_gpu_guard_wikitext2_128.json
outputs/qwen3_1p7b_wikitext_c4_consensus_random16_wikitext2_128_evidence_matrix.md
outputs/qwen3_1p7b_wikitext_c4_consensus_random16_wikitext2_128_evidence_matrix.csv
outputs/qwen3_1p7b_wikitext_c4_consensus_random16_wikitext2_128_evidence_matrix.json
```

GPU guard:

```text
max memory: 5920 / 8151 MiB = 72.63%
max utilization: 70%
killed by guard: false
```

