# EigenSkill-Q C++ Planner And Qwen3 Smoke Update

Date: `2026-06-05`

## What Changed

- Added a standalone C++ budgeted mixed-precision allocation planner:
  `inference_cpp/src/quant_allocation_planner.cpp`.
- Added a CTest fixture:
  `inference_cpp/testdata/allocation_fixture.csv`.
- The planner reads measured module-sensitivity JSON directly and emits
  evaluator-compatible `groups`, `allocations`, and `summaries`.
- Added a newer-model Qwen3-0.6B uniform fake-quant smoke baseline.

## C++ Planner Result

Input:

```text
outputs/qwen25_1p5b_module_loss_sensitivity_limit8_group128.json
```

Planner output:

```text
outputs/qwen25_1p5b_cpp_allocation_planner_4p5_summary.json
```

Protected positive NLL ratio:

| method | avg bits | protected ratio |
|---|---:|---:|
| loss_sensitive_budget | 4.4953 | 0.5445 |
| random_budget | 4.4993 | 0.2373 |
| category_budget | 4.4749 | 0.3860 |

PPL on Qwen2.5-1.5B, WikiText2 16 prompts:

| method | PPL | delta NLL vs FP16 | bit hist |
|---|---:|---:|---|
| FP16 | 10.7630 | 0.0000 | `{"16": 197}` |
| uniform INT4 | 15.0450 | 0.3349 | `{"4": 197}` |
| C++ loss-sensitive | 13.1388 | 0.1995 | `{"4": 136, "8": 61}` |
| C++ random budget | 13.7469 | 0.2447 | `{"4": 161, "8": 36}` |
| C++ category budget | 14.2839 | 0.2830 | `{"4": 120, "8": 77}` |

GPU guard:

```text
peak: 4678 / 8151 MiB = 57.39%
max utilization: 62%
killed_by_guard: false
```

## Qwen3-0.6B Loss-Sensitive Follow-Up

Sensitivity calibration:

```text
outputs/qwen3_0p6b_module_loss_sensitivity_limit4_group128.json
```

C++ planner allocation:

```text
outputs/qwen3_0p6b_cpp_allocation_planner_4p5_summary.json
```

Protected positive NLL ratio:

| method | avg bits | protected ratio |
|---|---:|---:|
| loss_sensitive_budget | 4.4997 | 0.5787 |
| random_budget | 4.4997 | 0.2815 |
| category_budget | 4.4997 | 0.3175 |

PPL on Qwen3-0.6B, WikiText2 16 prompts:

| method | PPL | delta NLL vs FP16 | bit hist |
|---|---:|---:|---|
| FP16 | 27.8160 | 0.0000 | `{"16": 197}` |
| uniform INT4 | 44.5656 | 0.4714 | `{"4": 197}` |
| C++ loss-sensitive | 34.8407 | 0.2252 | `{"4": 158, "8": 39}` |
| C++ random budget | 39.1800 | 0.3426 | `{"4": 160, "8": 37}` |
| C++ category budget | 37.5722 | 0.3007 | `{"4": 142, "8": 55}` |

External check on WikiText2 64 prompts using the same 4-prompt calibration
allocation:

| method | PPL | delta NLL vs FP16 | bit hist |
|---|---:|---:|---|
| FP16 | 29.4918 | 0.0000 | `{"16": 197}` |
| uniform INT4 | 47.3150 | 0.4727 | `{"4": 197}` |
| C++ loss-sensitive | 37.1018 | 0.2296 | `{"4": 158, "8": 39}` |
| C++ random budget | 41.6263 | 0.3446 | `{"4": 160, "8": 37}` |
| C++ category budget | 40.1396 | 0.3083 | `{"4": 142, "8": 55}` |

GPU guard:

```text
sensitivity peak: 4711 / 8151 MiB = 57.80%
16-prompt PPL eval peak: 2721 / 8151 MiB = 33.38%
64-prompt PPL eval peak: 2732 / 8151 MiB = 33.52%
killed_by_guard: false
```

## Qwen3-0.6B Uniform Smoke

Command output:

```text
outputs/qwen3_0p6b_uniform_fake_quant_ppl_wikitext2_16_summary.json
```

| method | PPL | delta NLL vs FP16 | bit hist |
|---|---:|---:|---|
| FP16 | 27.8160 | 0.0000 | `{"16": 197}` |
| uniform INT4 | 44.5656 | 0.4714 | `{"4": 197}` |
| uniform INT3 | 1079.7941 | 3.6589 | `{"3": 197}` |

GPU guard:

```text
peak: 2841 / 8151 MiB = 34.85%
max utilization: 34%
killed_by_guard: false
```

## Claim Boundary

This is still fake weight quantization plus a C++ allocation artifact. It does
not prove packed low-bit runtime speed, memory reduction, board-level latency,
or SOTA quantization quality. It does strengthen the repo by moving one core
allocation step out of Python and showing the same short-cycle signal on a
newer Qwen3 small model.
