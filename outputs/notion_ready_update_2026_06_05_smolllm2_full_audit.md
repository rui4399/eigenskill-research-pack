# EigenSkill-Q Update - 2026-06-05

## Current Result

SmolLM2-1.7B now has a full-module mixed-precision fake-quant audit:

- Model: `HuggingFaceTB/SmolLM2-1.7B-Instruct`
- Measured modules: `169 / 169` Linear modules
- Allocation: `156 x 4-bit`, `13 x 8-bit`
- Average bit budget: `4.5`
- Random baseline: budget-matched random16 allocation pool
- GPU guard: `train_python/run_with_gpu_guard.py --max-memory-ratio 0.85`

## Evidence Matrix

| slice | FP16 | uniform INT4 | loss_sensitive_full | best random16 | margin vs best random16 |
|---|---:|---:|---:|---:|---:|
| WikiText2-16 | 12.6903 | 18.1431 | 13.9866 | 14.7340 | +0.7474 |
| WikiText2-64 | 12.6568 | 18.5164 | 14.8877 | 15.6654 | +0.7777 |
| WikiText2-128 | 13.2171 | 18.7966 | 15.3641 | 16.2050 | +0.8409 |
| C4-64 | 18.4497 | 26.3475 | 21.4269 | 22.5529 | +1.1260 |

## Interpretation

This is a stronger result than the earlier 32-module SmolLM2 attempt. The
small 32-module allocation beat uniform INT4 but lost narrowly to the best
random16 seed. The full-module allocation is positive on all committed slices,
including a C4-64 overfitting check even though the allocation was calibrated
from WikiText2 prompts.

This still must be described conservatively:

- It is PyTorch fake quantization, not a packed quantized runtime.
- It is a short-slice diagnostic, not a production LLM quantization benchmark.
- It does not prove hardware latency or energy gains.
- It does not compare against GPTQ/AWQ/SmoothQuant/QuaRot as a SOTA baseline.

## GitHub Commits

Latest pushed commit:

```text
125b19f Add active baseline runtime probe
```

Relevant pushed commits:

```text
ca5b163 Add SmolLM2 full-module random16 evidence
bfd34d5 Extend SmolLM2 full-module audit to WikiText2 64
1feab0f Add SmolLM2 C4 overfitting audit
c3f7be1 Add SmolLM2 multi-slice evidence matrix
756aa23 Extend SmolLM2 full-module audit to WikiText2 128
a8a9960 Document SmolLM2 full audit reproduction
e4544d4 Add Notion-ready SmolLM2 audit update
7e80a9a Add C++ GPU guard summary utility
2d4df43 Add extended cross-model quant evidence matrix
125b19f Add active baseline runtime probe
```

Repository:

```text
https://github.com/rui4399/eigenskill-research-pack
```

## Key Artifacts

```text
outputs/smollm2_1p7b_full_random16_result.md
outputs/smollm2_1p7b_full_random16_multi_slice_evidence_matrix.md
outputs/smollm2_1p7b_full_gpu_guard_summary.md
outputs/cross_model_quant_evidence_matrix_extended_auto.md
outputs/baseline_runtime_import_probe_2026_06_05.md
train_python/README.md
```

## Verification

```text
CTest: 11/11 passed
Weight leak scan: no untracked .safetensors/.bin/.pt/.pth/.gguf/.onnx files
GPU memory peaks: 61.67% to 69.67%, below the requested 85% ceiling
```
