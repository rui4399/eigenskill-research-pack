# Recent Model Access Probe

Date: 2026-06-05

Probe method: `transformers.AutoConfig.from_pretrained(..., trust_remote_code=False)`
without an HF token.

| model | status | note |
|---|---|---|
| `google/gemma-3-1b-it` | gated | HF access blocked in current environment |
| `meta-llama/Llama-3.2-1B-Instruct` | gated | HF access blocked in current environment |
| `HuggingFaceTB/SmolLM3-3B` | accessible | `model_type=smollm3`, 36 layers, hidden size 2048 |
| `Qwen/Qwen3-0.6B` | accessible | `model_type=qwen3`, 28 layers, hidden size 1024 |

Use the gated models only after HF access is explicitly available. Do not make
claims that depend on them in the current environment.
