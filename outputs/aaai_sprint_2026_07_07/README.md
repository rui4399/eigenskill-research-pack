# AAAI Sprint Execution Log

Date: 2026-07-07

This directory stores execution artifacts for the AAAI CSI decision-framework
experiment sprint. It is intentionally separate from older RTX3090 outputs so
new evidence can be audited without mixing it with prior feasibility runs.

## Current Status

Completed so far:

- Generated the machine-readable experiment matrix.
- Added and verified the result summarizer for win/loss, average rank, and seed
  stability.
- Expanded the matrix to the stricter AAAI closure requirements: equal-budget
  INT2/INT3/INT4 allocation, Qwen2.5-7B downstream allocation retention, and
  Qwen2.5-7B/14B calibration-size plus seed-robustness curves.
- Added fake-quant allocation support to the downstream JSONL task evaluator so
  MMLU/GSM8K subsets can be run under uniform or allocation-based bit policies.
- Completed one Qwen2.5-1.5B full-module sensitivity path check over the
  available 8-prompt public WikiText2 pool and saved it as `n8_effective`.

Not yet completed:

- CSI-guided allocation downstream retention.
- Formal n=16/32/... calibration runs from the 128-prompt WikiText2/C4 pools.
- CSI vs simple heuristic prediction of future retention drop.
- Calibration size scaling from 16 to 4096 samples.
- Seed robustness with seeds 0--4.
- INT2/INT3/INT4/INT8/FP16 bit-width sweep.
- 7B/14B scale support runs.

## Matrix Scope

The current matrix contains 624 runs:

| Experiment | Runs |
|---|---:|
| `p0_csi_allocation_retention` | 252 |
| `p0_calibration_size_scaling` | 72 |
| `p0_seed_robustness` | 200 |
| `p0_csi_vs_heuristics` | 48 |
| `p1_bit_width_sweep` | 40 |
| `p1_scale_support` | 12 |

The allocation-retention block now covers Qwen2.5-1.5B, Qwen2.5-3B, and
Qwen2.5-7B under average 2-bit, 3-bit, and 4-bit budgets.

## Key Files

| File | Purpose |
|---|---|
| `experiment_matrix.json` | Pending run matrix covering P0/P1 experiments. |
| `summary_empty_or_partial.json` | Current summarizer output over completed local records. |

## Execution Constraint

At the start of this sprint, the RTX3090 was already under heavy utilization.
GPU-heavy retention and quantization runs should start only when GPU utilization
and memory pressure are low enough to avoid corrupting measurements.
