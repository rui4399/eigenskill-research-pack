# QKV Replacement Proxy Drift

Date: `2026-06-06T01:37:47+00:00`
Candidate: `full_v8`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Prompt file: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v2.txt`
Prompts: `12`

## Aggregate

| metric | mean | median | max |
|---|---:|---:|---:|
| final hidden rel-L2 | 0.005322 | 0.005430 | 0.005739 |
| last logits rel-L2 | 0.006759 | 0.006693 | 0.008289 |
| KV mean rel-L2 | 0.009603 | 0.009591 | 0.009937 |
| KV max rel-L2 | 0.019436 | 0.019440 | 0.020670 |

## Per Prompt

| id | input len | final hidden rel-L2 | logits rel-L2 | KV mean rel-L2 | KV max rel-L2 | prompt |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 17 | 0.005541 | 0.006998 | 0.009316 | 0.018486 | `Explain calibration-set sensitivity in mixed-bit LLM quantization using exactly two sentences.` |
| 1 | 19 | 0.005739 | 0.007860 | 0.009871 | 0.019645 | `Produce minified JSON with keys policy, evidence, and caveat for a precision-routing experiment.` |
| 2 | 24 | 0.005632 | 0.007210 | 0.009337 | 0.018272 | `How many bytes store 4096 four-bit signed weights when packed densely? Give only the number and ` |
| 3 | 22 | 0.004821 | 0.005732 | 0.009431 | 0.019370 | `Write a C++ declaration for a function that multiplies selected quantized output rows by a dense` |
| 4 | 18 | 0.005630 | 0.007578 | 0.009531 | 0.019115 | `Give two distinct ways a row-level precision search can overfit a tiny generation prompt suite.` |
| 5 | 21 | 0.005319 | 0.006275 | 0.009563 | 0.019568 | `In one sentence, explain why INT8 protection of an attention value projection may still reduce e` |
| 6 | 18 | 0.005247 | 0.005862 | 0.009619 | 0.019414 | `Draft a four-step ablation plan for testing whether a precision guard transfers across prompt sp` |
| 7 | 14 | 0.005731 | 0.008289 | 0.009722 | 0.019335 | `Compare activation reconstruction error and generated-text prefix match in one compact paragraph` |
| 8 | 17 | 0.005588 | 0.006911 | 0.009680 | 0.019467 | `Name two deployment metrics for an edge LLM runtime besides model size and perplexity.` |
| 9 | 20 | 0.004842 | 0.006309 | 0.009694 | 0.020011 | `Write a cautious README sentence explaining that a packed kernel benchmark is not an end-to-end ` |
| 10 | 17 | 0.004833 | 0.005612 | 0.009937 | 0.020670 | `Describe how hidden-state drift could be used as a cheap proxy for selecting sensitive rows.` |
| 11 | 18 | 0.004939 | 0.006474 | 0.009532 | 0.019876 | `State one reason an early transformer layer may need a different quantization policy than middle` |

## Guardrail

This is a teacher-forced continuous proxy. It supports ranking and diagnostics, but it does not prove generation quality by itself.