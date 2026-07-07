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
- Completed two formal Qwen2.5-1.5B WikiText2 n=16 calibration splits under
  contended RTX3090 load and built a robust-LCB CSI consensus allocation.
- Ran a 40-row GSM8K downstream retention slice for FP16, uniform INT2/INT3/INT4,
  single-split 2-to-4 average-3bit allocation, and CSI consensus 2-to-4
  average-3bit allocation.
- Completed Qwen2.5-1.5B WikiText2 n=32 seed0/seed1 full-module sensitivity
  runs and a matching CSI consensus allocation.
- Completed Qwen2.5-1.5B WikiText2 n=64 seed0/seed1 full-module sensitivity
  runs and a matching CSI consensus allocation.
- Completed Qwen2.5-1.5B WikiText2 n=128 full-pool sensitivity upper-bound
  runs and a matching CSI consensus allocation.

Not yet completed:

- CSI-guided allocation downstream retention.
- Larger downstream retention slices after prompt/scoring cleanup.
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

## Early Contended-GPU Results

The first downstream slice is intentionally recorded as a contended-GPU run:
runtime should not be used as efficiency evidence.

| Method | Bits | GSM8K task40 |
|---|---:|---:|
| FP16 | 16 | 2/40 |
| Uniform INT2 | 2 | 0/40 |
| Uniform INT3 | 3 | 0/40 |
| Uniform INT4 | 4 | 1/40 |
| Single-split 2-to-4 allocation | 2.9984 avg | 0/40 |
| CSI consensus 2-to-4 allocation | 2.9999 avg | 0/40 |
| Single-split 2-to-4 allocation | 3.5038 avg | 0/40 |
| CSI consensus 2-to-4 allocation | 4.0000 avg | 1/40 |

This is currently a collapse-boundary/failure-analysis result, not positive
evidence that CSI improves downstream retention.

## Calibration Scaling Check

| Calibration n | Mean high-bit Jaccard |
|---:|---:|
| 16 | 0.6767 |
| 32 | 0.7398 |
| 64 | 0.8491 |
| 128 | 0.9903 |

For the measured seed0/seed1 pair, increasing calibration samples from 16 to 32
to 64 improves consensus agreement with both single-split high-bit sets. The
128-row case is a full-pool upper bound: both seeds select the same 128-prompt
pool, so it should not be interpreted as independent seed robustness.

## Key Files

| File | Purpose |
|---|---|
| `experiment_matrix.json` | Pending run matrix covering P0/P1 experiments. |
| `summary_empty_or_partial.json` | Current summarizer output over completed local records. |

## Execution Constraint

At the start of this sprint, the RTX3090 was already under heavy utilization.
GPU-heavy retention and quantization runs should start only when GPU utilization
and memory pressure are low enough to avoid corrupting measurements.
