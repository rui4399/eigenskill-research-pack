# Qwen2.5-1.5B Budget-Matched Baseline Sanity Report

Date: 2026-06-04

## Purpose

Earlier Qwen2.5-1.5B results compared the loss-sensitive allocation mainly
against uniform INT4. This report adds budget-matched random and structural
heuristic mixed-precision baselines on a small WikiText2 sanity slice.

This is still a fake-quant quality diagnostic, not a packed runtime result.

## Setup

```text
model: /mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct
dataset: WikiText2 validation prompt file
prompts: 16
max_length: 160
tokens: 1607
dtype: float16
group_size: 128
device: CUDA
linear modules: 197
```

## Results

| method | PPL | mean NLL delta vs FP16 | bit histogram | avg bits |
|---|---:|---:|---|---:|
| FP16 | 10.76298 | 0.00000 | 16:197 | 16.0000 |
| uniform INT4 | 15.04498 | 0.33493 | 4:197 | 4.0000 |
| loss-sensitive {4,8} | 13.13882 | 0.19946 | 4:136, 8:61 | 4.4953 |
| random budget-matched {4,8} | 14.18543 | 0.27610 | 4:164, 8:33 | 4.4952 |
| category heuristic budget | 14.43989 | 0.29388 | 4:83, 8:114 | 4.4709 |

## GPU Guard

The first attempt used the old fake-quant path and was killed by the GPU guard:

```text
peak memory: 7643 / 8151 MiB = 93.77%
killed_by_guard: true
```

After changing fake quantization to in-place group-wise updates, the run
completed under the user's 85% target:

```text
peak memory: 4634 / 8151 MiB = 56.85%
max GPU utilization: 62%
killed_by_guard: false
```

## Interpretation

The loss-sensitive allocation improves over uniform INT4 and over two simple
budgeted mixed-precision baselines on this slice. The budget-matched random
baseline protects only 15.87% of measured positive loss increase, while the
loss-sensitive allocation protects 54.45% at nearly the same average-bit
budget.

This result is useful for short-cycle collaborator review, but it should be
expanded to larger prompt counts and standard PTQ baselines before submission.

Evidence:

```text
outputs/qwen25_1p5b_baseline_allocations_4to8_limit8_group128_summary.json
outputs/qwen25_1p5b_baseline_budget_ppl_wikitext2_16_summary.json
outputs/qwen25_1p5b_baseline_eval_gpu_guard.json
outputs/qwen25_1p5b_baseline_eval_gpu_guard_retry.json
```
