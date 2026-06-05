# EigenSkill-Q Night Progress

Date: 2026-06-05

This note summarizes the verified overnight progress after tightening the
project toward a credible mixed-precision quantization diagnostic rather than
a broad architecture proposal.

## 1. C++ Reporting Path

Added a standalone C++ budget-curve summarizer:

```text
inference_cpp/src/quant_budget_curve_summary.cpp
```

It reads evaluator PPL summary JSON and regenerates:

```text
outputs/consensus_budget_curve_report.md
outputs/consensus_budget_curve_summary.csv
outputs/consensus_budget_curve_summary.json
outputs/consensus_budget_curve.svg
```

This removes NumPy/matplotlib from the budget-curve reporting path. Model
loading and fake-quant PPL evaluation still use Python/PyTorch.

Verification:

```text
CTest: 7/7 passed
JSON validation: passed
No tracked/untracked model weight leak found
```

GitHub commit:

```text
45b95ef Add C++ budget curve summarizer
```

## 2. Qwen3-0.6B Random16 Stress Test

The existing Qwen3-0.6B 4-prompt sensitivity calibration was stress-tested
against 16 budget-matched random allocations on two evaluation distributions.

Configuration:

```text
model: Qwen/Qwen3-0.6B
group size: 128
average bits: about 4.5
target: cpp_loss_sensitive_budget
random repeats: 16
evaluation slices: WikiText2-64 and C4-64
GPU guard: max_memory_ratio 0.85
```

Results:

| dataset | FP16 | uniform INT4 | target | category | random min/mean/max | target vs best random | target vs random mean |
|---|---:|---:|---:|---:|---|---:|---:|
| WikiText2-64 | 31.1808 | 49.7895 | 39.0053 | 42.1917 | 41.9059 / 44.0596 / 46.3992 | +2.9006 | +5.0543 |
| C4-64 | 36.1380 | 52.9352 | 45.0623 | 47.7182 | 47.1666 / 48.5346 / 50.0268 | +2.1043 | +3.4723 |

Positive margins mean the target has lower PPL than the comparator.

GPU guard:

```text
WikiText2-64 peak: 2663 / 8151 MiB = 32.67%
C4-64 peak:        3345 / 8151 MiB = 41.04%
```

Evidence files:

```text
data_eval/eval_configs/qwen3_0p6b_cpp_random16_compare.json
outputs/qwen3_0p6b_cpp_allocation_planner_random16_4p5_summary.json
outputs/qwen3_0p6b_cpp_random16_ppl_wikitext2_64_summary.json
outputs/qwen3_0p6b_cpp_random16_gpu_guard_wikitext2_64.json
outputs/qwen3_0p6b_cpp_random16_ppl_c4_64_summary.json
outputs/qwen3_0p6b_cpp_random16_gpu_guard_c4_64.json
outputs/qwen3_0p6b_cpp_random16_wikitext_c4_evidence_matrix.md
outputs/qwen3_0p6b_cpp_random16_wikitext_c4_evidence_matrix.csv
```

GitHub commits:

```text
258aa60 Add Qwen3 0.6B random16 evidence
b5899ce Add Qwen3 0.6B C4 random16 evidence
```

## 3. SmolLM2-1.7B Candidate Status

Candidate:

```text
HuggingFaceTB/SmolLM2-1.7B-Instruct
```

The local Hugging Face cache contained repo metadata but not a complete model
weight file. Offline loading failed before any meaningful GPU work:

```text
OSError: HuggingFaceTB/SmolLM2-1.7B-Instruct does not appear to have a file named pytorch_model.bin or model.safetensors.
```

Guarded smoke result:

```text
max_memory_used_mib: 961 / 8151
max_memory_used_ratio: 0.1179
killed_by_guard: false
```

Interpretation: this is a cache/download issue, not a model-quality result.
The `snapshot_download()` resume path was started, but the unauthenticated HF
download stalled at an incomplete safetensors blob during this run.

Evidence:

```text
outputs/smollm2_1p7b_candidate_download_note.md
outputs/smollm2_1p7b_uniform_ppl_wikitext2_16_guard.json
```

## 4. Current Claim Boundary

## 4. Baseline Dependency Audit

The current WSL Python environment does not have public quantization packages
installed:

```text
auto_gptq: no
awq: no
llmcompressor: no
optimum: no
bitsandbytes: no
gptqmodel: no
```

Therefore this run did not attempt GPTQ/AWQ/SmoothQuant/QuaRot-style
comparisons. Installing those packages is a separate environment change and
should be done deliberately, ideally in a pinned virtual environment, because
the current project already depends on a working CUDA/PyTorch/Transformers
stack.

The available in-repository baselines for this run were:

```text
uniform INT4
structural category budget
budget-matched random repeats
C++ evidence matrix over random min/mean/max
```

## 5. Current Claim Boundary

The strongest current claim remains narrow:

```text
Measured sensitivity plus C++ budget allocation can beat uniform INT4,
category heuristics, and budget-matched random repeats in short-slice PyTorch
fake-quant diagnostics on selected small LLMs.
```

Do not claim:

```text
production quantizer
packed INT4 runtime
hardware latency or energy speedup
superiority over GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant
true eigen-routing through Transformer nonlinearities
```

The next scientific step is to add at least one stronger published baseline
family, preferably RTN/AWQ/GPTQ-style comparisons on the same prompt slices,
then expand calibration seeds and prompt counts.
