# Recent Small-Model Candidate List

Date: 2026-06-05

Purpose: move the quantization-track experiments beyond Qwen2.5-era baselines
and toward small 2024-2026 models that fit an 8GB laptop GPU under the 85%
guard.

## Priority Candidates

| priority | model | reason | expected risk |
|---:|---|---|---|
| 1 | `LiquidAI/LFM2.5-350M` | 2026-era, very small, edge-friendly, already runs locally | WikiText2 smoke PPL is high; tokenizer/task fit needs audit |
| 2 | `Qwen/Qwen3-0.6B` | 2025-era, already has repo evidence, low VRAM | Qwen-family overlap with current work |
| 3 | `Qwen/Qwen3-1.7B` | 2025-era, stronger small baseline, already partly audited | 8GB VRAM limits full sweeps |
| 4 | `google/gemma-3-1b-it` | 2025-era mainstream small model | may require HF license/auth gate |
| 5 | `meta-llama/Llama-3.2-1B-Instruct` | 2024-era mainstream small model | may require HF license/auth gate |
| 6 | `HuggingFaceTB/SmolLM3-3B` | 2025-era stronger small model | may exceed comfortable 8GB fake-quant sweeps |

## Completed Smoke

`LiquidAI/LFM2.5-350M` loaded and evaluated on WikiText2-32 under the GPU guard:

```text
FP16 PPL         163.9448
uniform INT4 PPL 135.0303
guard peak       3092 / 8151 MiB = 37.93%
```

This is only a compatibility smoke, not a quality claim. The unexpectedly high
FP16 PPL and lower INT4 PPL indicate that the prompt slice/tokenization/model
fit needs audit before using this model in headline comparisons.

`Qwen/Qwen3-0.6B` also loaded and evaluated on WikiText2-32:

```text
FP16 PPL         31.6892
uniform INT4 PPL 49.9061
guard peak       3195 / 8151 MiB = 39.20%
```

This is a cleaner near-term small-model baseline than the LFM2.5 smoke because
uniform INT4 degrades PPL as expected on the same prompt slice.

## Access Probe

```text
google/gemma-3-1b-it: gated in the current HF environment
meta-llama/Llama-3.2-1B-Instruct: gated in the current HF environment
HuggingFaceTB/SmolLM3-3B: accessible, larger follow-up candidate
Qwen/Qwen3-0.6B: accessible, low-VRAM follow-up candidate
```

## Next Model Steps

1. Run a Qwen3-0.6B sensitivity allocation and transfer check because the
   uniform smoke is stable and low-VRAM.
2. Audit LFM2.5 tokenizer/template behavior on plain text and add a second
   prompt source before sensitivity allocation.
3. Probe Gemma 3 1B and Llama 3.2 1B only after confirming license access in
   the current HF environment.
4. Keep all claims as fake-quant diagnostics until a packed runtime baseline
   is implemented.
