# OLMo2 Random16 Negative Audit

This audit expands the OLMo2-0425-1B C++ planner random baseline from 8 to 16
random budget allocations on the same 64-prompt WikiText2 and C4 fake-quant
diagnostics.

## Result

| dataset | target | best random | random mean | target vs best random | target vs random mean |
|---|---:|---:|---:|---:|---:|
| WikiText2-64 | 21.1191 | 21.4637 | 21.6765 | +0.3445 | +0.5573 |
| C4-64 | 35.8428 | 35.5846 | 36.0382 | -0.2582 | +0.1954 |

## Interpretation

The WikiText2 result remains positive after the larger random set. The C4
result is a negative best-random comparison: one random seed beats the
single-split loss-sensitive target, even though the target remains better than
the random mean and uniform INT4.

This should not be hidden. It is evidence that one-split loss-sensitive
allocation is not robust enough by itself on short calibration probes. It
supports the repository's current consensus/stability framing: allocation
claims should be reported with split-stability audits, random-repeat baselines,
and cross-dataset consensus checks rather than a single sensitivity split.

The guarded runs stayed below the requested GPU-memory limit:

```text
WikiText2-64 peak: 4592 / 8151 MiB = 56.34%
C4-64 peak:        4593 / 8151 MiB = 56.35%
```

