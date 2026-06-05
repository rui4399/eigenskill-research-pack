# EigenSkill-Q 2026-06-05 Update: Task Eval Smoke Path

## Summary

This update adds a minimal task-evaluation path beyond PPL. It is not a formal
MMLU/GSM8K/IFEval benchmark; it is a pipeline smoke test so future work can
evaluate task accuracy instead of only perplexity.

## Added Files

```text
data_eval/task_prompts/quant_task_smoke.jsonl
train_python/eval_task_jsonl.py
inference_cpp/src/quant_task_eval_summary.cpp
inference_cpp/testdata/task_eval_fixture.json
outputs/qwen3_0p6b_task_smoke_summary.json
outputs/qwen3_0p6b_task_smoke_summary.md
outputs/qwen3_0p6b_task_smoke_cpp_summary.json
outputs/qwen3_0p6b_task_smoke_gpu_guard.json
```

## Result

Qwen3-0.6B task smoke:

```text
total: 5
exact: 3
accuracy: 0.6000
gsm8k_smoke: 1/2
mmlu_smoke: 2/2
ifeval_smoke: 0/1
GPU peak: 3048/8151 MiB = 37.39%
```

## Interpretation

This is a useful negative/positive mixed signal:

- arithmetic and JSON-format following are still weak under the current prompt;
- the small MMLU-style multiple-choice cases pass;
- the evaluator, GPU guard, JSON summary, and C++ report path are wired.

The next paper-facing step should connect this interface to real benchmark
subsets and report ability retention under quantization, not just PPL.

## Verification

```text
python3 -m py_compile train_python/eval_task_jsonl.py
ctest --test-dir build/cpp-wsl --output-on-failure
```

Result:

```text
22/22 C++ tests passed
```

