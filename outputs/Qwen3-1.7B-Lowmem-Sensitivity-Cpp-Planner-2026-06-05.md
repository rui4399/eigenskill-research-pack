# Qwen3-1.7B Low-Memory Sensitivity And C++ Planner Result

Date: `2026-06-05`

## Purpose

This run addresses a concrete resource failure in the first Qwen3-1.7B
sensitivity probe. The original all-at-once implementation was killed by the
GPU guard near `192/197` Linear modules after peaking at `7628/8151 MiB`
(`93.58%`), above the requested `85%` ceiling.

The sensitivity script now supports:

- CPU-side weight backup instead of a full GPU clone.
- Low-memory row-chunk fake quantization.
- Periodic JSON/Markdown checkpoints.
- Resume from a previous sensitivity JSON.

## Low-Memory Sensitivity Probe

Evidence files:

```text
outputs/qwen3_1p7b_sensitivity_lowmem_gpu_guard_limit2_group128.json
outputs/qwen3_1p7b_module_loss_sensitivity_limit2_group128.json
outputs/qwen3_1p7b_module_loss_sensitivity_limit2_group128_report.md
outputs/qwen3_1p7b_loss_sensitive_alloc_4to8_limit2_group128_summary.json
```

GPU guard:

```text
peak: 4520 / 8151 MiB = 55.45%
max utilization: 39%
killed_by_guard: false
```

Sensitivity allocation summary:

| method | avg bits | bit hist | protected positive delta |
|---|---:|---|---:|
| uniform INT4 | 4.0000 | `{"4": 197}` | 0.0000 |
| loss-sensitive {4,8} | 4.4973 | `{"4": 153, "8": 44}` | 0.6048 |

## C++ Planner Allocation

Planner input:

```text
outputs/qwen3_1p7b_module_loss_sensitivity_limit2_group128.json
```

Planner output:

```text
outputs/qwen3_1p7b_cpp_allocation_planner_4p5_summary.json
```

| method | avg bits | bit hist | protected positive delta | expected unprotected delta |
|---|---:|---|---:|---:|
| loss_sensitive_budget | 4.4973 | `{"4": 153, "8": 44}` | 0.6048 | 0.2464 |
| random_budget | 4.4973 | `{"4": 163, "8": 34}` | 0.2331 | 0.4781 |
| category_budget | 4.4827 | `{"4": 130, "8": 67}` | 0.4123 | 0.3664 |

## 16-Prompt WikiText2 PPL Check

Evaluation evidence:

```text
data_eval/eval_configs/qwen3_1p7b_cpp_planner_budget_compare.json
outputs/qwen3_1p7b_cpp_planner_budget_ppl_wikitext2_16_summary.json
outputs/qwen3_1p7b_cpp_planner_budget_gpu_guard_wikitext2_16.json
```

| method | PPL | delta NLL vs FP16 | bit hist |
|---|---:|---:|---|
| FP16 | 18.9664 | 0.0000 | `{"16": 197}` |
| uniform INT4 | 27.4469 | 0.3696 | `{"4": 197}` |
| C++ loss-sensitive budget | 24.7968 | 0.2680 | `{"4": 153, "8": 44}` |
| C++ random budget | 25.3903 | 0.2917 | `{"4": 163, "8": 34}` |
| C++ category budget | 23.8397 | 0.2287 | `{"4": 130, "8": 67}` |

GPU guard:

```text
peak: 4896 / 8151 MiB = 60.07%
max utilization: 55%
killed_by_guard: false
```

## 64-Prompt External Check

The same 2-prompt calibration allocation was evaluated on a larger WikiText2
slice without recalibration:

```text
outputs/qwen3_1p7b_cpp_planner_budget_ppl_wikitext2_64_summary.json
outputs/qwen3_1p7b_cpp_planner_budget_gpu_guard_wikitext2_64.json
```

| method | PPL | delta NLL vs FP16 | bit hist |
|---|---:|---:|---|
| FP16 | 21.6552 | 0.0000 | `{"16": 197}` |
| uniform INT4 | 31.1885 | 0.3648 | `{"4": 197}` |
| C++ loss-sensitive budget | 27.6578 | 0.2447 | `{"4": 153, "8": 44}` |
| C++ random budget | 28.3799 | 0.2704 | `{"4": 163, "8": 34}` |
| C++ category budget | 27.4838 | 0.2384 | `{"4": 130, "8": 67}` |

GPU guard:

```text
peak: 4908 / 8151 MiB = 60.21%
max utilization: 66%
killed_by_guard: false
```

## Interpretation

The low-memory implementation is the main engineering improvement: it turns a
near-complete killed run into a completed run while staying far below the
requested 85% GPU memory ceiling.

The allocation result is mixed:

- C++ loss-sensitive allocation improves over uniform INT4 and random budget
  on both the 16-prompt and 64-prompt WikiText2 slices.
- C++ category budget is slightly better than loss-sensitive on both slices
  despite protecting less measured positive delta. This is a useful negative
  finding: the current two-prompt loss sensitivity score is not yet a
  universally dominant allocator.

This remains fake weight quantization and short-slice PPL evidence. It is not a
packed low-bit runtime, latency result, board-level result, or SOTA
quantization claim.
