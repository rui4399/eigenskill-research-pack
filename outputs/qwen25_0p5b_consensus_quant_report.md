# Qwen2.5-0.5B Consensus Quantization Report

This report adds a stability-oriented consensus allocation on top of the
previous 2-prompt and 8-prompt measured loss-sensitive allocations.

## Allocation

Model: `Qwen/Qwen2.5-0.5B-Instruct`

Quantization scaffold: group-wise symmetric fake weight quantization, group
size 128.

Policy:

1. start from 4-bit for every Linear module;
2. keep the modules selected as 8-bit by both the 2-prompt and 8-prompt probes;
3. spend the remaining 4.5 average-bit budget by average positive
   delta-NLL-per-cost across the two probes.

```text
Linear modules              169
consensus 8-bit modules      60
bit histogram                4-bit=109, 8-bit=60
weighted average bits        4.4997
budget used                  99.99%
2p 8-bit overlap             49 / 55
8p 8-bit overlap             49 / 57
locked intersection modules  38
ranked additions             22
```

The 8-bit set Jaccard against the original allocations improves from 0.5135
between 2p and 8p to 0.7424 against 2p and 0.7206 against 8p.

## PPL Results

| dataset | FP16 | uniform INT4 | uniform INT3 | 2p loss-sensitive | 8p loss-sensitive | consensus |
|---|---:|---:|---:|---:|---:|---:|
| WikiText2-128 | 17.4294 | 27.7411 | 514.0862 | 22.4605 | 21.9762 | 22.0848 |
| C4-64 | 23.9539 | 36.5128 | 779.2680 | 31.2151 | 30.7970 | 30.8017 |

## Interpretation

The consensus allocation is not the absolute best WikiText2 result, but it is
the better paper-facing stability point:

- it keeps most of the 8-prompt quality gain over the weaker 2-prompt probe;
- it is nearly tied with the 8-prompt allocation on C4;
- it has substantially higher overlap with both calibration probes than the
  raw 2p/8p pair has with each other.

This is still fake quantization, not a packed runtime result. The result should
be used as evidence for calibration-stability analysis and constrained
allocation policy design, not as an INT4 inference-speed claim.

## Evidence Files

```text
train_python/build_consensus_allocation.py
data_eval/eval_configs/qwen25_group128_with_consensus.json
outputs/qwen25_0p5b_loss_sensitive_consensus_alloc_4to8_group128_summary.json
outputs/qwen25_0p5b_loss_sensitive_consensus_alloc_4to8_group128_report.md
outputs/qwen25_0p5b_fake_quant_ppl_consensus_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_consensus_group128_c4_en_validation_64_summary.json
```
