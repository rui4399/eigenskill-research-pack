# Phi-3-mini Cross-Family Summary

Generated: 2026-07-08

Purpose: provide a non-Qwen family check for the AAAI sprint.

## Results

| Task | Method | Exact / 100 | Accuracy |
|---|---|---:|---:|
| GSM8K100 | CSI consensus avg3 | 0 | 0.00 |
| GSM8K100 | FP16 | 2 | 0.02 |
| GSM8K100 | Single split avg3 | 0 | 0.00 |
| GSM8K100 | Uniform INT4 | 2 | 0.02 |
| MMLU100 | CSI consensus avg3 | 8 | 0.08 |
| MMLU100 | FP16 | 41 | 0.41 |
| MMLU100 | Single split avg3 | 9 | 0.09 |
| MMLU100 | Uniform INT4 | 42 | 0.42 |

## CSI Stability

- Standard Linear modules: `129`
- Parameters: `3821079552`
- CSI avg bits: `2.998`
- CSI high-bit overlap Jaccard: left `0.899`, right `0.914`
- Protected delta ratio: `0.881`

## Interpretation

Phi-3-mini confirms the pipeline works on a non-Qwen family with standard Linear modules. Uniform INT4 retains MMLU100/GSM8K100 in this protocol, while avg3 2-to-4 allocation collapses, making this cross-family evidence primarily a stress/failure-boundary result rather than a positive CSI dominance result.
