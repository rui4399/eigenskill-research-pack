# Small Model Candidates

Date: 2026-06-05

This note tracks near-term model candidates for extending EigenSkill-Q beyond
Qwen/Qwen2.5. The goal is to add recent small-model breadth without exhausting
the current local disk budget.

Current machine constraint:

```text
GPU: NVIDIA RTX 5070 Laptop GPU, 8151 MiB visible memory
guard: train_python/run_with_gpu_guard.py --max-memory-ratio 0.85
C: free space: about 33 GiB
HF cache: about 13 GiB
```

Do not download 3B/4B/7B models until disk pressure is addressed or a separate
cache path is configured.

## Already Cached / Tested

```text
HuggingFaceTB/SmolLM2-360M-Instruct
Qwen/Qwen2.5-0.5B-Instruct
Qwen/Qwen2.5-1.5B-Instruct
Qwen/Qwen3-0.6B
Qwen/Qwen3-1.7B
allenai/OLMo-2-0425-1B-Instruct
```

OLMo2 is the current non-Qwen positive allocator signal.

## Low-Risk Next Candidates

```text
meta-llama/Llama-3.2-1B-Instruct
created: 2024-09-18
reason: strong 1B reference model; useful non-Qwen/non-OLMo breadth
risk: license/access or tokenizer/model compatibility
status: attempted, blocked by gated Hugging Face access in this environment
evidence: outputs/llama32_1b_uniform_gpu_guard_wikitext2_16.json
guard: return code 1, not killed by guard, peak 871/8151 MiB = 10.69%
action: retry only after HF access/auth is configured
```

```text
HuggingFaceTB/SmolLM2-1.7B-Instruct
created: 2024-10-31
reason: same family as existing 360M but larger and still small enough to try
risk: less model-family breadth than Llama/OLMo because SmolLM2-360M is already tested
status: attempted after Llama access block; process made no visible progress for several minutes and was terminated
evidence: no PPL or guard summary was produced, so do not report it as a model result
action: retry later with explicit HF cache/download diagnostics or a separate cache path
```

```text
google/gemma-3-1b-it
created: 2025-03-10
reason: recent 1B family; useful if accessible
risk: previous run was blocked by gated access in this environment
action: keep as blocked until access is granted or a compatible open checkpoint is selected
```

## Deferred Candidates

```text
HuggingFaceTB/SmolLM3-3B
created: 2025-07-08
reason: recent and relevant, but likely too large for the current disk/GPU margin
action: defer until disk/cache path is fixed
```

```text
microsoft/Phi-4-mini-instruct
created: 2025-02-19
reason: strong modern small model, but about 3.8B parameters
action: defer until disk/cache path is fixed
```

```text
stabilityai/stablelm-2-1_6b-chat
created: 2024-04-08
reason: small enough, but older than the best current candidates and lower priority
action: optional fallback
```

```text
facebook/MobileLLM-125M
created: 2024-10-30
reason: edge-oriented, tiny, but may be too small or not instruction-tuned enough for PPL conclusions
action: useful for systems microbenchmarks, not primary quant-quality evidence
```

## Trial Order

1. retry `HuggingFaceTB/SmolLM2-1.7B-Instruct` only with better download diagnostics
2. revisit `meta-llama/Llama-3.2-1B-Instruct` only after HF access/auth is configured
3. revisit `google/gemma-3-1b-it` only if access is fixed
4. defer 3B+ models until storage is safer
