# EigenSkill-Q Update - SmolLM2 Full-Module Swap Search

Date: 2026-06-05

## Summary

This update adds a bounded interaction-aware swap-search audit for the
SmolLM2-1.7B full-module fake-quant allocation. It directly addresses the
question of whether the current sensitivity allocation is only a noisy
one-shot heuristic by testing one-out/one-in 8-bit module swaps under global
PPL feedback.

This remains a PyTorch fake-quant diagnostic. It is not a packed quantizer,
not hardware latency/energy evidence, and not a GPTQ/AWQ/SmoothQuant/QuaRot
comparison.

## Engineering Change

`train_python/search_allocation_swaps.py` now reuses a single loaded model and
restores CPU-captured Linear weights between candidate trials. The previous
repeated-load execution path could trip the 85% GPU-memory guard on this
8GB laptop GPU. The updated path completed under guard.

A new C++ report utility was added:

```text
inference_cpp/src/quant_swap_search_summary.cpp
```

It consumes the swap-search JSON and optional GPU guard JSON, then emits
Markdown, CSV, or JSON summaries. It is covered by a CTest smoke test.

## Results

| dataset | base PPL | best PPL | improvement | swaps | guard peak |
|---|---:|---:|---:|---:|---:|
| WikiText2-32 | 15.1207 | 15.1207 | 0.0000 | 4 | 84.87% |
| C4-64 | 21.4269 | 21.4269 | 0.0000 | 4 | 76.81% |

Interpretation: this is a local-stability negative result. The four tested
top proxy swaps did not improve the full-module allocation on either the
in-family WikiText2 slice or the cross-dataset C4 slice. This does not prove
global optimality; it only rules out this bounded one-swap candidate set.

## Evidence Files

```text
outputs/smollm2_1p7b_full_swap_search_wikitext2_32_summary.json
outputs/smollm2_1p7b_full_swap_search_wikitext2_32_report.md
outputs/smollm2_1p7b_full_swap_search_wikitext2_32_cpp_summary.md
outputs/smollm2_1p7b_full_swap_search_wikitext2_32_guard.json
outputs/smollm2_1p7b_full_swap_search_c4_64_summary.json
outputs/smollm2_1p7b_full_swap_search_c4_64_report.md
outputs/smollm2_1p7b_full_swap_search_c4_64_cpp_summary.md
outputs/smollm2_1p7b_full_swap_search_c4_64_guard.json
outputs/smollm2_1p7b_swap_search_gpu_guard_summary.md
```

## Verification

```text
python3 -m py_compile train_python/search_allocation_swaps.py
ctest --test-dir build/cpp-wsl --output-on-failure
```

CTest result:

```text
12/12 passed
```

## Next Experiments

1. Increase the swap candidate pool only if the guard remains below 85%.
2. Add two-swap beam search or a small simulated annealing pass, but label it
   as search heuristic evidence rather than a closed-form optimum.
3. Build a real GPTQ/AWQ/llm-compressor baseline environment before making any
   baseline-comparison claims.
