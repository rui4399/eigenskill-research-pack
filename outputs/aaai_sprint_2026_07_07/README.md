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
- Fixed MMLU `question`/`choices` row normalization so public MMLU JSONL rows
  are evaluated as A/B/C/D choice tasks rather than GSM8K-style numeric tasks.
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
- Completed Qwen2.5-7B WikiText2 n=16 seed0/seed1 full-module sensitivity
  runs and a matching CSI consensus allocation.
- Completed Qwen2.5-7B WikiText2 n=32 seed0/seed1 full-module sensitivity
  runs and a matching CSI consensus allocation.
- Completed Qwen2.5-7B WikiText2 n=64 seed0/seed1 full-module sensitivity
  runs and a matching CSI consensus allocation.
- Extended Qwen2.5-1.5B WikiText2 n=64 seed robustness from seed0/seed1 to
  seeds 0--4.
- Added a Qwen2.5-1.5B n=64 CSI-vs-heuristic future-split sensitivity
  prediction check using seeds 0/1 to predict held-out seeds 2--4.
- Ran a corrected Qwen2.5-1.5B MMLU broad5x20 100-row retention slice covering
  FP16, uniform INT2/INT3/INT4, single-split average-3bit allocation, and CSI
  average-3bit allocation.
- Ran a corrected Qwen2.5-7B MMLU broad5x20 100-row retention slice covering
  FP16, uniform INT3/INT4, single-split average-3bit allocation, and CSI
  average-3bit allocation.
- Completed Qwen2.5-1.5B C4 n=64 seed0/seed1 full-module sensitivity runs,
  a matching CSI consensus allocation, and a WikiText2-vs-C4 domain-shift
  summary.

Not yet completed:

- Larger CSI-guided allocation downstream retention slices beyond the current
  corrected 100-row MMLU slice.
- Formal n=16/32/... calibration runs from the 128-prompt WikiText2/C4 pools.
- Downstream-retention version of CSI vs simple heuristic prediction.
- Calibration size scaling from 16 to 4096 samples.
- Seed robustness with seeds 0--4.
- INT2/INT3/INT4/INT8/FP16 bit-width sweep.
- 7B/14B scale support beyond the current 7B n=16 pair.

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

## Corrected MMLU100 Retention Slice

The MMLU broad5x20 100-row slices use corrected A/B/C/D choice normalization.
The earlier uncorrected `qwen25_1p5b_mmlu100_fp16.json` artifact should not be
used as evidence because public MMLU rows were being interpreted as numeric
GSM8K-style rows.

### Qwen2.5-1.5B

| Method | Bits | MMLU100 |
|---|---:|---:|
| FP16 | 16 | 54/100 |
| Uniform INT2 | 2 | 0/100 |
| Uniform INT3 | 3 | 4/100 |
| Uniform INT4 | 4 | 41/100 |
| Single-split n64 2-to-4 allocation | 2.9999 avg | 0/100 |
| CSI n64 2-to-4 allocation | 2.9999 avg | 1/100 |

This is pressure-boundary evidence. Uniform INT4 retains a substantial fraction
of FP16 performance, while INT2/INT3 and average-3bit mixed allocations collapse
on this slice. CSI slightly exceeds the single-split average-3bit allocation,
but this is not yet positive downstream-dominance evidence.

### Qwen2.5-7B

| Method | Bits | MMLU100 |
|---|---:|---:|
| FP16 | 16 | 65/100 |
| Uniform INT3 | 3 | 8/100 |
| Uniform INT4 | 4 | 63/100 |
| Single-split n64 2-to-4 allocation | 2.9997 avg | 0/100 |
| CSI n64 2-to-4 allocation | 2.9997 avg | 1/100 |

For 7B, uniform INT4 nearly matches FP16 on this slice, but uniform INT3 and the
current average-3bit single/CSI allocations collapse. CSI slightly exceeds the
single-split allocation at the collapse boundary, but this is not positive
downstream-dominance evidence.

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

## 7B Scale Check

Qwen2.5-7B n=16 seed0/seed1 full-module sensitivity completed. The resulting
CSI consensus allocation has average bits `2.9997`, bit histogram `{2: 115,
4: 82}`, and mean high-bit Jaccard `0.6823`.

Qwen2.5-7B n=32 seed0/seed1 full-module sensitivity also completed. The
resulting CSI consensus allocation has average bits `2.9997`, bit histogram
`{2: 115, 4: 82}`, and mean high-bit Jaccard `0.6995`.

| Calibration n | Mean high-bit Jaccard | Avg bits |
|---:|---:|---:|
| 16 | 0.6823 | 2.9997 |
| 32 | 0.6995 | 2.9997 |
| 64 | 0.8254 | 2.9997 |

The n=64 run improves agreement substantially over n=16/n=32, while the lower
budget rows remain far from saturated. This strengthens the scale-level claim
that 7B allocation decisions remain sensitive to calibration perturbations
under smaller calibration budgets.

## Seed Robustness Check

Qwen2.5-1.5B WikiText2 n=64 now covers seeds 0--4. Seeds 2--4 were run under
intentional GPU contention with a concurrent 7B job, so these rows are stability
evidence rather than efficiency evidence.

| Metric | Value |
|---|---:|
| Avg bits mean | 2.9992 |
| Avg bits std | 0.0009 |
| Protected-ratio mean | 0.9297 |
| Protected-ratio std | 0.0060 |
| Pairwise high-bit Jaccard mean | 0.7167 |
| Pairwise high-bit Jaccard std | 0.0367 |
| Pairwise high-bit Jaccard min | 0.6585 |
| Pairwise high-bit Jaccard max | 0.7982 |

This is the first formal five-seed stability slice for the AAAI sprint. It
shows that equal-budget allocations keep a tight average-bit distribution, but
the selected high-bit layer sets still vary meaningfully across calibration
sampling seeds.

## CSI-vs-Heuristic Future-Split Check

Using Qwen2.5-1.5B WikiText2 n=64, seed0/seed1 scores were used to predict the
mean per-module positive delta-NLL on held-out seeds 2--4. This is a
calibration-sensitivity prediction check, not downstream task-retention
evidence.

| Score | Pearson | Spearman | Kendall tau |
|---|---:|---:|---:|
| Two-split mean | 0.9951 | 0.8959 | 0.7664 |
| Single split seed0 | 0.9939 | 0.8715 | 0.7434 |
| Two-split min / CSI LCB proxy | 0.9950 | 0.8696 | 0.7627 |
| Single split seed1 | 0.9948 | 0.8505 | 0.7192 |
| CSI LCB per parameter | 0.1780 | 0.7209 | 0.5676 |
| Parameter count | 0.7562 | 0.2905 | 0.2671 |
| Random fixed | -0.0071 | 0.1485 | 0.1244 |

The strongest ranking signal in this slice is the two-split mean, which beats
both single-split scores on Spearman and Kendall tau. The conservative LCB
proxy is close to the stronger single split but does not dominate the mean
score in this setting.

## Calibration Domain-Shift Check

Qwen2.5-1.5B n=64 seed0/seed1 was repeated with C4 calibration prompts and
compared against the matched WikiText2 n=64 pair.

| Calibration source | Mean high-bit Jaccard | Avg bits |
|---|---:|---:|
| WikiText2 | 0.8491 | 2.9999 |
| C4 | 0.7873 | 2.9999 |

In this measured pair, C4 produces lower cross-split agreement than WikiText2.
This is useful domain-shift evidence: the allocation policy remains equal
budget, while the calibration source changes the stability profile.

## Key Files

| File | Purpose |
|---|---|
| `experiment_matrix.json` | Pending run matrix covering P0/P1 experiments. |
| `summary_empty_or_partial.json` | Current summarizer output over completed local records. |

## Execution Constraint

At the start of this sprint, the RTX3090 was already under heavy utilization.
GPU-heavy retention and quantization runs should start only when GPU utilization
and memory pressure are low enough to avoid corrupting measurements.
