# Wake-up Summary - 2026-06-05 Swap Search Extension

GitHub repo: https://github.com/rui4399/eigenskill-research-pack
Latest remote main: 3718b5653f0601b5bb3f31025e1eaf87df616ac7

## What changed

1. `train_python/search_allocation_swaps.py` now reuses one loaded model and restores CPU-captured Linear weights between allocation trials. This fixed the repeated-load path that hit the 85% GPU guard.
2. Added C++ tool `inference_cpp/src/quant_swap_search_summary.cpp` with CTest coverage.
3. Added SmolLM2-1.7B full-module interaction-aware swap-search evidence.
4. Updated README, training README, and Notion-ready update page.

## Results

| dataset | base PPL | best PPL | improvement | swaps | guard peak |
|---|---:|---:|---:|---:|---:|
| WikiText2-32 | 15.1207 | 15.1207 | 0.0000 | 4 | 84.87% |
| WikiText2-64 | 14.8877 | 14.8376 | 0.0502 | 8 | 76.91% |
| C4-64 | 21.4269 | 21.4269 | 0.0000 | 4 | 76.81% |

Interpretation: WikiText2-64 shows a small interaction-aware improvement from one global-PPL swap; C4-64 remains the cross-dataset caution. These are fake-quant diagnostics, not packed runtime or hardware claims.

## Verification

- `python3 -m py_compile train_python/search_allocation_swaps.py`
- `ctest --test-dir build/cpp-wsl --output-on-failure` -> 12/12 passed
- Weight leak scan for `.safetensors|.bin|.pt|.pth|.gguf|.onnx` -> empty

## Notion status

Notion write tools were not exposed in this session. The sync-ready page is:

`outputs/notion_ready_update_2026_06_05_swap_search.md`
