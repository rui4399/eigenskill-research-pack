# EigenSkill-Q 2026-06-05 Update: Qwen3-0.6B Consensus vs Random16

## Summary

This update addresses the main weakness in the previous Qwen3-0.6B
random16 audit. The single WikiText2-calibrated loss-sensitive allocation
improved over uniform INT4 and random-seed mean, but one WikiText2 random seed
still beat it. The new run builds a cross-dataset consensus allocation from
two short calibration probes:

- WikiText2 sensitivity probe
- C4 sensitivity probe

The consensus allocation then evaluates against FP16, uniform INT4, the
single-split allocations, a C++ category baseline, and 15 explicit
budget-matched random seeds on both WikiText2-64 len96 and C4-64.

This is still PyTorch fake quantization, not a packed runtime or hardware
result. The value is narrower: it gives cleaner in-repository evidence that
cross-dataset agreement is a better bit-allocation signal than a single noisy
calibration split.

## Allocation

Qwen3-0.6B has 197 measured Linear modules in this experiment.

| Allocation | 4-bit modules | 8-bit modules | Average bits |
|---|---:|---:|---:|
| WikiText2 single split | 153 | 44 | 4.4997 |
| C4 single split | 156 | 41 | 4.4997 |
| WikiText2+C4 consensus | 151 | 46 | 4.4997 |

Consensus construction:

- intersection candidates selected first: 14
- left overlap with WikiText2 allocation: 37 / 44
- right overlap with C4 allocation: 23 / 41
- remaining budget filled by averaged positive loss-per-cost score

## Main Numbers

| Dataset | FP16 | uniform INT4 | WikiText2 split | C4 split | consensus | category | random_seed min/mean/max |
|---|---:|---:|---:|---:|---:|---:|---:|
| WikiText2-64 len96 | 33.9865 | 54.6542 | 49.5352 | 45.3513 | 45.6559 | 50.4746 | 48.5030 / 50.4787 / 52.6347 |
| C4-64 | 36.1380 | 52.9352 | 47.5872 | 44.8344 | 44.9290 | 48.6222 | 48.3840 / 49.4427 / 50.7971 |

Consensus random-seed audit:

| Dataset | consensus PPL | seed count | win/loss/tie | margin vs best seed | margin vs seed mean |
|---|---:|---:|---:|---:|---:|
| WikiText2-64 len96 | 45.6559 | 15 | 15 / 0 / 0 | +2.8471 | +4.8229 |
| C4-64 | 44.9290 | 15 | 15 / 0 / 0 | +3.4551 | +4.5138 |

Positive margin means the consensus target has lower PPL.

## GPU Guard

All runs stayed below Rui's requested 85% VRAM ceiling.

| Run | Peak VRAM | Peak Ratio | Peak GPU Util | Guard |
|---|---:|---:|---:|---|
| C4 sensitivity probe | 4589 / 8151 MiB | 56.30% | 36% | pass |
| WikiText2 consensus eval | 4867 / 8151 MiB | 59.71% | 57% | pass |
| C4 consensus eval | 4893 / 8151 MiB | 60.03% | 55% | pass |

## Generated Evidence

```text
outputs/qwen3_0p6b_c4_module_loss_sensitivity_limit4_group128.json
outputs/qwen3_0p6b_c4_module_loss_sensitivity_limit4_group128_report.md
outputs/qwen3_0p6b_c4_loss_sensitive_alloc_4to8_limit4_group128_summary.json
outputs/qwen3_0p6b_wikitext2_c4_consensus_alloc_4to8_limit4_group128_summary.json
outputs/qwen3_0p6b_wikitext2_c4_consensus_alloc_4to8_limit4_group128_report.md
outputs/qwen3_0p6b_lowmem_consensus_random16_ppl_wikitext2_64_len96_summary.json
outputs/qwen3_0p6b_lowmem_consensus_random16_ppl_c4_64_summary.json
outputs/qwen3_0p6b_lowmem_consensus_random16_evidence_matrix.md
outputs/qwen3_0p6b_lowmem_consensus_random16_random_seed_audit.md
outputs/qwen3_0p6b_lowmem_consensus_random16_gpu_guard_summary.md
```

## Interpretation

Clean claim:

> On Qwen3-0.6B short public-text slices, a WikiText2+C4 consensus
> mixed-precision allocation under a 4.5 average-bit budget improves over
> uniform INT4, a structural category heuristic, and all 15 listed
> budget-matched random-seed allocations on both WikiText2-64 len96 and C4-64.

Honest caveat:

> This is a diagnostic fake-quant experiment. It does not prove a packed
> runtime, hardware latency/energy savings, or SOTA quantization quality.

Research implication:

> The evidence now supports writing the project around sensitivity stability,
> calibration-split consensus, and reproducible allocation audits, rather than
> around unproved eigen-routing or physical swarm claims.

## Reproduce

```bash
build/cpp-wsl/quant_evidence_matrix \
  --input outputs/qwen3_0p6b_lowmem_consensus_random16_ppl_wikitext2_64_len96_summary.json \
  --dataset wikitext2_64_len96 \
  --input outputs/qwen3_0p6b_lowmem_consensus_random16_ppl_c4_64_summary.json \
  --dataset c4_64 \
  --target wikitext_c4_consensus \
  --emit markdown

build/cpp-wsl/quant_random_baseline_audit \
  --input outputs/qwen3_0p6b_lowmem_consensus_random16_ppl_wikitext2_64_len96_summary.json \
  --dataset wikitext2_64_len96 \
  --input outputs/qwen3_0p6b_lowmem_consensus_random16_ppl_c4_64_summary.json \
  --dataset c4_64 \
  --target wikitext_c4_consensus \
  --emit markdown

build/cpp-wsl/gpu_guard_summary \
  --input c4_sensitivity=outputs/qwen3_0p6b_c4_module_loss_sensitivity_limit4_group128_gpu_guard.json \
  --input consensus_wikitext2=outputs/qwen3_0p6b_lowmem_consensus_random16_gpu_guard_wikitext2_64_len96.json \
  --input consensus_c4=outputs/qwen3_0p6b_lowmem_consensus_random16_gpu_guard_c4_64.json \
  --emit markdown \
  --max-memory-ratio 0.85
```

## Next

1. Promote the consensus framing into the paper draft.
2. Add real quantization baselines where possible: GPTQ/AWQ/SmoothQuant and rotation methods.
3. Continue stronger-model evidence under the 85% guard, prioritizing Qwen3-1.7B and accessible edge-oriented models.
4. Keep adding C++ artifacts that audit allocations and eventually move toward packed runtime checks.
