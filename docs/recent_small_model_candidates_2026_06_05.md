# Recent Small-Model Candidate Plan

Updated: 2026-06-07

This note is a queue, not a result table. A model becomes paper-facing evidence
only after it passes the same prompt-slice, random-seed, GPU-guard, and claim
boundary checks as the existing Qwen3/OLMo rows.

## Current Local Constraints

```text
GPU: NVIDIA RTX 5070 Laptop GPU, about 8151 MiB visible memory
guard: train_python/run_with_gpu_guard.py --max-memory-ratio 0.85
C: free space during latest check: about 14.86 GiB
policy: do not download 3B/4B/7B checkpoints until cache pressure is fixed
```

The current storage budget is tight. Prefer experiments that reuse cached
models or tiny public prompt slices. New model downloads should be justified by
baseline value, not curiosity.

## Already Useful Evidence Rows

| model | current role | caveat |
|---|---|---|
| `Qwen/Qwen3-0.6B` | fast reference row with consensus/random evidence | Qwen-family only |
| `Qwen/Qwen3-1.7B` | main small quality row; chunked C4-128 random16 runbook exists | needs GPU-free time for remaining chunks |
| `allenai/OLMo-2-0425-1B-Instruct` | non-Qwen 1B replication row | still short-slice fake quant |
| `HuggingFaceTB/SmolLM2-1.7B-Instruct` | boundary and interaction/swap-search evidence | not a strong headline model |
| `Qwen/Qwen2.5-0.5B-Instruct` | AutoAWQ readiness and public-calibrated smoke | tiny baseline readiness only |

## Low-Risk Next Candidates

| model | why it matters | condition before running |
|---|---|---|
| `ibm-granite/granite-3.3-2b-instruct` | 2B non-Qwen family, useful breadth. | Only after freeing disk or moving HF cache. |
| `LiquidAI/LFM2.5-350M` | explicitly small/on-device oriented. | Use only as compatibility/system smoke; current tokenizer fit is weak. |
| `google/gemma-3-1b-it` | useful 1B non-Qwen family. | Retry only if access and license state are clear. |
| `meta-llama/Llama-3.2-1B-Instruct` | useful Meta 1B reference. | Retry only after HF access/auth is configured. |

## Deferred Stress Rows

| model | reason to defer |
|---|---|
| `HuggingFaceTB/SmolLM3-3B` | likely too close to disk/GPU margin for routine runs. |
| `microsoft/Phi-4-mini-instruct` | strong but above the routine 8GB/low-disk budget. |
| `microsoft/Phi-3.5-mini-instruct` | older than Phi-4-mini and still memory-heavy. |
| `h2oai/h2o-danube3-4b-chat` | 4B stress row, not a near-term baseline. |
| `nvidia/Nemotron-Mini-4B-Instruct` | 4B and license/specialization risk. |

## Next Evaluation Order

1. Finish Qwen3-1.7B C4-128 random16 chunks only when GPU and disk are safe.
2. Extend the public-calibrated AutoAWQ/GPTQ baseline protocol before adding
   more unrelated model families.
3. Add one non-Qwen 1B-2B family only if it can run without stressing C drive.
4. Keep 3B+ models as later stress rows, not required short-cycle evidence.

## Source Links

- Qwen3-0.6B: https://huggingface.co/Qwen/Qwen3-0.6B
- Qwen3-1.7B: https://huggingface.co/Qwen/Qwen3-1.7B
- OLMo-2-0425-1B-Instruct: https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct
- Granite-3.3-2B-Instruct: https://huggingface.co/ibm-granite/granite-3.3-2b-instruct
- LFM2.5-350M: https://huggingface.co/LiquidAI/LFM2.5-350M
- Gemma-3-1B-IT: https://huggingface.co/google/gemma-3-1b-it
- Llama-3.2-1B-Instruct: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
- SmolLM3-3B: https://huggingface.co/HuggingFaceTB/SmolLM3-3B
- Phi-4-mini-instruct: https://huggingface.co/microsoft/Phi-4-mini-instruct
- Phi-3.5-mini-instruct: https://huggingface.co/microsoft/Phi-3.5-mini-instruct
- H2O Danube3 4B Chat: https://huggingface.co/h2oai/h2o-danube3-4b-chat
- Nemotron-Mini-4B-Instruct: https://huggingface.co/nvidia/Nemotron-Mini-4B-Instruct
