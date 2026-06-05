# OLMo2 Consensus Repairs Random16 Negative Case

This note closes the OLMo2 random16 audit. A single-split loss-sensitive
allocation lost to the best C4 random seed, so the next check evaluates the
cross-dataset WikiText2+C4 consensus allocation against the same random16 pool.

## Result

| dataset | consensus PPL | best random16 PPL | random16 mean PPL | consensus vs best random | consensus vs random mean |
|---|---:|---:|---:|---:|---:|
| WikiText2-64 | 21.0349 | 21.4637 | 21.6765 | +0.4288 | +0.6416 |
| C4-64 | 35.4726 | 35.5846 | 36.0382 | +0.1120 | +0.5656 |

The C4 row is the important repair. In the single-split audit,
`cpp_loss_sensitive_budget` scored `35.8428` PPL and lost to random seed
`20260619` at `35.5846` PPL. The consensus allocation scores `35.4726` PPL on
the same C4 prompt slice and therefore beats that best random seed by `0.1120`
PPL.

## Interpretation

This does not prove a production quantizer. It is a bounded fake-quant
diagnostic showing that the consensus heuristic is doing useful work in this
failure case: it converts a best-random loss into a positive best-random margin
without changing the evaluator, prompt slice, model, or random pool.

This strengthens the narrow paper story:

```text
short calibration probes are noisy -> one-split allocation can fail ->
cross-dataset consensus stabilizes the selected high-bit modules
```

The guarded consensus-vs-random16 runs stayed below the requested GPU-memory
limit:

```text
WikiText2-64 peak: 4593 / 8151 MiB = 56.35%
C4-64 peak:        4586 / 8151 MiB = 56.26%
```

