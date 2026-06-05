# EigenSkill-Q Update - Qwen3-0.6B Low-Memory Allocation

Date: 2026-06-05

## Summary

This update adds a complete low-memory Qwen3-0.6B fake-quant diagnostic path:
module sensitivity, constrained {4,8} allocation, PPL checks, C++ evidence
tables, and GPU guard summaries.

This is still PyTorch fake weight quantization. It is not packed-runtime
latency, board-level energy evidence, GPTQ/AWQ superiority, or production
quantized inference.

## What Changed

- Measured all 197 Linear modules in `Qwen/Qwen3-0.6B`.
- Built a loss-sensitive allocation under an average 4.5-bit budget.
- Evaluated the allocation on built-in diagnostic prompts and C4-64.
- Generated C++ evidence matrix and GPU guard summaries.
- Recorded a true WikiText2-64 rerun failure instead of hiding it.

## Allocation

```text
model: Qwen/Qwen3-0.6B
calibration: 4 built-in diagnostic prompts
probe bits: INT4
group size: 128
budget: average 4.5 bits
linear modules: 197 / 197 measured
allocation: 153 modules at 4-bit, 44 modules at 8-bit
average bits: 4.4997
protected positive delta-NLL ratio: 64.72%
```

GPU guard:

```text
max memory: 3310 / 8151 MiB = 40.61%
max utilization: 59%
killed by guard: false
```

## PPL Results

Built-in diagnostic prompts:

| config | PPL | delta NLL vs FP16 |
|---|---:|---:|
| FP16 | 285.9696 | 0.000000 |
| uniform INT4 | 287.3424 | 0.004789 |
| uniform INT3 | 2295.4069 | 2.082780 |
| loss-sensitive {4,8} | 225.0283 | -0.239659 |

C4-64:

| config | PPL | delta NLL vs FP16 |
|---|---:|---:|
| FP16 | 36.1380 | 0.000000 |
| uniform INT4 | 52.9352 | 0.381723 |
| uniform INT3 | 832.2634 | 3.136804 |
| loss-sensitive {4,8} | 47.5872 | 0.275218 |

Interpretation:

- The C4-64 row is the useful cross-text-slice result: the allocation improves
  over uniform INT4 by 5.3480 PPL, but remains worse than FP16.
- The built-in prompt row is a smoke result only. It should not be presented as
  a dataset-level result.
- Uniform INT3 is consistently destructive in this setting.

## Important Negative Evidence

A true WikiText2-64 rerun with `data_eval/text_prompts/wikitext2_validation_128.txt`,
`limit-prompts=64`, and `max-length=128` was killed by the 85% GPU-memory guard:

```text
max memory: 6933 / 8151 MiB = 85.06%
killed by guard: true
```

Do not cite this run as a completed WikiText2-64 quality result. Use it as a
resource-limit note. A lower-memory rerun should use smaller `max-length`,
smaller prompt count, or a stricter evaluator memory path.

## Evidence Files

```text
outputs/qwen3_0p6b_module_loss_sensitivity_limit4_group128.json
outputs/qwen3_0p6b_module_loss_sensitivity_limit4_group128_report.md
outputs/qwen3_0p6b_loss_sensitive_alloc_4to8_limit4_group128_summary.json
outputs/qwen3_0p6b_loss_sensitive_vs_uniform_ppl_default8_summary.json
outputs/qwen3_0p6b_loss_sensitive_vs_uniform_ppl_c4_64_summary.json
outputs/qwen3_0p6b_default8_c4_loss_sensitive_ppl_table.md
outputs/qwen3_0p6b_default8_c4_loss_sensitive_evidence_matrix.md
outputs/qwen3_0p6b_lowmem_gpu_guard_summary.md
outputs/qwen3_0p6b_loss_sensitive_eval_gpu_guard_wikitext2_64_true.json
```

## Next Step

Run a valid low-memory WikiText2 check:

```text
Option A: WikiText2-64, max_length 96
Option B: WikiText2-32, max_length 128
Option C: evaluator refactor to stream one config/prompt at a time with lower activation pressure
```

Only after that should the Qwen3-0.6B result be described as a two-dataset
WikiText2/C4 result.
