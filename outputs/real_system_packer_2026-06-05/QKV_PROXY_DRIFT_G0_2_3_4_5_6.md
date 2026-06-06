# QKV Replacement Proxy Drift

Date: `2026-06-06T01:39:47+00:00`
Candidate: `g0_2_3_4_5_6`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Prompt file: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v2.txt`
Prompts: `12`

## Aggregate

| metric | mean | median | max |
|---|---:|---:|---:|
| final hidden rel-L2 | 0.011301 | 0.011467 | 0.012802 |
| last logits rel-L2 | 0.018647 | 0.018860 | 0.022448 |
| KV mean rel-L2 | 0.033858 | 0.034002 | 0.035584 |
| KV max rel-L2 | 0.164967 | 0.165186 | 0.174553 |

## Per Prompt

| id | input len | final hidden rel-L2 | logits rel-L2 | KV mean rel-L2 | KV max rel-L2 | prompt |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 17 | 0.012055 | 0.018899 | 0.032216 | 0.155886 | `Explain calibration-set sensitivity in mixed-bit LLM quantization using exactly two sentences.` |
| 1 | 19 | 0.010155 | 0.016938 | 0.034245 | 0.165891 | `Produce minified JSON with keys policy, evidence, and caveat for a precision-routing experiment.` |
| 2 | 24 | 0.011403 | 0.016366 | 0.032545 | 0.157518 | `How many bytes store 4096 four-bit signed weights when packed densely? Give only the number and ` |
| 3 | 22 | 0.010273 | 0.016938 | 0.034156 | 0.167719 | `Write a C++ declaration for a function that multiplies selected quantized output rows by a dense` |
| 4 | 18 | 0.012802 | 0.022448 | 0.033284 | 0.161635 | `Give two distinct ways a row-level precision search can overfit a tiny generation prompt suite.` |
| 5 | 21 | 0.010978 | 0.017977 | 0.034603 | 0.169808 | `In one sentence, explain why INT8 protection of an attention value projection may still reduce e` |
| 6 | 18 | 0.009979 | 0.018822 | 0.033367 | 0.161898 | `Draft a four-step ablation plan for testing whether a precision guard transfers across prompt sp` |
| 7 | 14 | 0.011640 | 0.019005 | 0.033412 | 0.161478 | `Compare activation reconstruction error and generated-text prefix match in one compact paragraph` |
| 8 | 17 | 0.011733 | 0.021578 | 0.033849 | 0.164482 | `Name two deployment metrics for an edge LLM runtime besides model size and perplexity.` |
| 9 | 20 | 0.010378 | 0.015187 | 0.034792 | 0.170602 | `Write a cautious README sentence explaining that a packed kernel benchmark is not an end-to-end ` |
| 10 | 17 | 0.012688 | 0.019832 | 0.035584 | 0.174553 | `Describe how hidden-state drift could be used as a cheap proxy for selecting sensitive rows.` |
| 11 | 18 | 0.011531 | 0.019777 | 0.034241 | 0.168130 | `State one reason an early transformer layer may need a different quantization policy than middle` |

## Guardrail

This is a teacher-forced continuous proxy. It supports ranking and diagnostics, but it does not prove generation quality by itself.