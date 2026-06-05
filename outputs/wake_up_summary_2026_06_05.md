# Wake-Up Summary - 2026-06-05

## Repository

```text
https://github.com/rui4399/eigenskill-research-pack
visibility: PUBLIC
latest main: ddf7000
```

## What Changed

The repo now has a stronger, more honest EigenSkill-Q evidence package:

- SmolLM2-1.7B full-module sensitivity probe: `169 / 169` Linear modules.
- Mixed-precision allocation: `156 x 4-bit`, `13 x 8-bit`, average `4.5` bits.
- Random baseline: budget-matched random16.
- Evaluation slices: WikiText2-16, WikiText2-64, WikiText2-128, C4-64.
- All SmolLM2 full-module rows beat the best random16 allocation.
- Added C++ `gpu_guard_summary` and extended C++ `quant_evidence_matrix --target auto`.
- Added active runtime baseline probe showing GPTQ/AWQ packages are not available in the current WSL runtime.

## Main Numbers

| slice | target vs best random16 |
|---|---:|
| WikiText2-16 | +0.7474 PPL |
| WikiText2-64 | +0.7777 PPL |
| WikiText2-128 | +0.8409 PPL |
| C4-64 | +1.1260 PPL |

GPU guard:

```text
max observed memory: 5679 / 8151 MiB = 69.67%
requested ceiling: 85%
CTest: 11/11 passed
weight leak scan: clean
```

## Key Files

```text
README.md
train_python/README.md
outputs/nightly_delivery_2026_06_05.md
outputs/smollm2_1p7b_full_random16_result.md
outputs/smollm2_1p7b_full_random16_multi_slice_evidence_matrix.md
outputs/cross_model_quant_evidence_matrix_extended_auto.md
outputs/smollm2_1p7b_full_gpu_guard_summary.md
outputs/baseline_runtime_import_probe_2026_06_05.md
outputs/notion_ready_update_2026_06_05_smolllm2_full_audit.md
```

## Claims To Avoid

Do not claim:

- production quantizer
- packed INT4 runtime
- hardware latency or energy win
- SOTA versus GPTQ/AWQ/SmoothQuant/QuaRot
- true Eigen-routing through nonlinear Transformer layers

Current safe claim:

```text
Sensitivity-guided mixed precision beats uniform INT4 and a budget-matched
random16 pool across short WikiText2/C4 fake-quant diagnostic slices on several
small LLM families.
```

## Next Best Steps

1. Build a real runnable GPTQ/AWQ/llm-compressor baseline environment, or keep
   the current baseline limitation explicit.
2. Extend one model to a larger public eval slice, if runtime allows.
3. Add an interaction-aware swap/search stage on top of the full-module
   allocation, but report negative results honestly.
4. Sync `outputs/notion_ready_update_2026_06_05_smolllm2_full_audit.md` into
   Notion when Notion MCP tools are visible again.

