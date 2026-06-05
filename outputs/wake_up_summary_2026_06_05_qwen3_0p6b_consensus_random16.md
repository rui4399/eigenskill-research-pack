# Wake-up Summary: Qwen3-0.6B Consensus Audit

瑞，这轮把 Qwen3-0.6B 的短周期证据补完整了一截。

## What Changed

- Added a C4 sensitivity probe for Qwen3-0.6B.
- Built a WikiText2+C4 consensus allocation at the same 4.5 average-bit `{4,8}` budget.
- Evaluated the consensus allocation on WikiText2-64 len96 and C4-64.
- Compared against FP16, uniform INT4, WikiText2 single-split, C4 single-split, category baseline, and 15 random seeds.
- Generated C++ evidence matrix, random-seed audit, and GPU guard summaries.

## Main Result

The previous Qwen3-0.6B single-split allocation had one important weakness:
on WikiText2-64 len96, the best random seed beat it by 1.0322 PPL.

The new consensus allocation fixes that failure case:

```text
Qwen3-0.6B consensus, average 4.5 bits:
WikiText2-64 len96:
  FP16 33.9865
  uniform INT4 54.6542
  consensus 45.6559
  random_seed min/mean/max 48.5030 / 50.4787 / 52.6347
  wins/losses/ties vs random_seed 15 / 0 / 0
  margin vs best random +2.8471 PPL

C4-64:
  FP16 36.1380
  uniform INT4 52.9352
  consensus 44.9290
  random_seed min/mean/max 48.3840 / 49.4427 / 50.7971
  wins/losses/ties vs random_seed 15 / 0 / 0
  margin vs best random +3.4551 PPL
```

## GPU Guard

All guarded runs stayed below 85%:

- C4 sensitivity: 4589 / 8151 MiB = 56.30%
- WikiText2 consensus eval: 4867 / 8151 MiB = 59.71%
- C4 consensus eval: 4893 / 8151 MiB = 60.03%

## How To Present It

The clean story is no longer "one loss-sensitive split beats everything."

The better story is:

> single calibration probes are noisy, so EigenSkill-Q uses cross-dataset
> consensus to select modules whose 8-bit protection is stable under a fixed
> bit budget.

Still do not claim SOTA or hardware acceleration yet. This is fake quantization
evidence and C++ audit tooling, not a packed-kernel runtime.
