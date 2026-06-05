# Recent Small-Model Candidate Plan

Updated: 2026-06-05

This list is for the next EigenSkill-Q evaluation wave. It is not a result
table. A model becomes evidence only after it completes the same fake-quant
PPL, random-seed, seed-coverage, and GPU-guard audit as the existing Qwen3 and
OLMo2 rows.

## Selection Rules

- Prefer 2024-2026 model families over Qwen2.5-era baselines.
- Prefer models up to 3B parameters for routine 8GB-GPU runs.
- Keep 3-4B models as stress candidates, not mandatory baselines.
- Prefer public Hugging Face models with standard `AutoModelForCausalLM`
  loading.
- Treat gated or terms-restricted models as optional probes.
- Do not claim "best in branch" until the same random-seed audit passes across
  at least two text slices.

## Priority A: Run Next

| model | status | why it matters | caveat |
|---|---|---|---|
| `Qwen/Qwen3-0.6B` | already evaluated | fast reference row with clean consensus random16 evidence | Qwen-family only |
| `Qwen/Qwen3-1.7B` | partially evaluated | current main quality row; C4-128 random16 is ready as chunks | needs GPU-free time for remaining batches |
| `allenai/OLMo-2-0425-1B-Instruct` | already evaluated | non-Qwen 1B replication row | extend only if more non-Qwen evidence is needed |
| `ibm-granite/granite-3.3-2b-instruct` | candidate | 2025 Apache-2.0 2B model with 128K context and multilingual support | not yet locally smoke-tested |
| `HuggingFaceTB/SmolLM3-3B` | candidate | strong open 3B boundary case; likely the most relevant <=3B competitor | may sit close to 8GB guard |

## Priority B: Useful Probes

| model | status | why it matters | caveat |
|---|---|---|---|
| `LiquidAI/LFM2.5-350M` | compatibility smoke done | explicitly edge/on-device oriented and very small | current prompt/tokenizer fit looks poor; do not headline |
| `google/gemma-3-1b-it` | candidate | useful 1B Google baseline | terms/access may block reproducibility |
| `meta-llama/Llama-3.2-1B-Instruct` | candidate | useful Meta 1B baseline | gated/terms model; optional only |
| `apple/OpenELM-1_1B-Instruct` | low priority | edge-oriented architecture comparison | older and may require `trust_remote_code` |

## Priority C: Stress Rows Above The Routine Budget

| model | status | why it matters | caveat |
|---|---|---|---|
| `microsoft/Phi-4-mini-instruct` | stress candidate | strong 3.8B newer Phi-family row | above preferred <=3B target; memory risk |
| `microsoft/Phi-3.5-mini-instruct` | stress candidate | 2024 long-context small model | older than Phi-4-mini and above 3B |
| `h2oai/h2o-danube3-4b-chat` | stress candidate | phone/offline oriented 4B model | over routine memory budget |
| `nvidia/Nemotron-Mini-4B-Instruct` | stress candidate | compressed/distilled 4B model for on-device/RAG/function calling | special license and 4B size |

## Next Evaluation Order

1. Finish Qwen3-1.7B C4-128 random16 chunks when the GPU is free.
2. Smoke `ibm-granite/granite-3.3-2b-instruct` on WikiText2-32 and C4-32.
3. Smoke `HuggingFaceTB/SmolLM3-3B` with the same guard.
4. If memory permits, run 64-prompt consensus/random4 before random16.
5. Use Gemma/Llama/Phi only after access and memory behavior are confirmed.

## Source Links

- Qwen3-0.6B: https://huggingface.co/Qwen/Qwen3-0.6B
- Qwen3-1.7B: https://huggingface.co/Qwen/Qwen3-1.7B
- OLMo-2-0425-1B-Instruct: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct
- Granite-3.3-2B-Instruct: https://huggingface.co/ibm-granite/granite-3.3-2b-instruct
- SmolLM3-3B: https://huggingface.co/HuggingFaceTB/SmolLM3-3B
- LFM2.5-350M: https://huggingface.co/LiquidAI/LFM2.5-350M
- Gemma-3-1B-IT: https://huggingface.co/google/gemma-3-1b-it
- Llama-3.2-1B-Instruct: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- OpenELM-1.1B-Instruct: https://huggingface.co/apple/OpenELM-1_1B-Instruct
- Phi-4-mini-instruct: https://huggingface.co/microsoft/Phi-4-mini-instruct
- Phi-3.5-mini-instruct: https://huggingface.co/microsoft/Phi-3.5-mini-instruct
- H2O Danube3 4B Chat: https://huggingface.co/h2oai/h2o-danube3-4b-chat
- Nemotron-Mini-4B-Instruct: https://huggingface.co/nvidia/Nemotron-Mini-4B-Instruct
