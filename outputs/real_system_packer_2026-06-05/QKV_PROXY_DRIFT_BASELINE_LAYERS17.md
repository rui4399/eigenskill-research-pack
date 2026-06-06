# QKV Replacement Proxy Drift

Date: `2026-06-06T01:37:08+00:00`
Candidate: `baseline_layers17`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7]`
Prompt file: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v2.txt`
Prompts: `12`

## Aggregate

| metric | mean | median | max |
|---|---:|---:|---:|
| final hidden rel-L2 | 0.003705 | 0.003646 | 0.005023 |
| last logits rel-L2 | 0.003827 | 0.003603 | 0.005210 |
| KV mean rel-L2 | 0.007135 | 0.007114 | 0.007366 |
| KV max rel-L2 | 0.013254 | 0.013181 | 0.013952 |

## Per Prompt

| id | input len | final hidden rel-L2 | logits rel-L2 | KV mean rel-L2 | KV max rel-L2 | prompt |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 17 | 0.004269 | 0.004430 | 0.006950 | 0.012780 | `Explain calibration-set sensitivity in mixed-bit LLM quantization using exactly two sentences.` |
| 1 | 19 | 0.004350 | 0.005210 | 0.007366 | 0.013952 | `Produce minified JSON with keys policy, evidence, and caveat for a precision-routing experiment.` |
| 2 | 24 | 0.003780 | 0.004832 | 0.007056 | 0.013193 | `How many bytes store 4096 four-bit signed weights when packed densely? Give only the number and ` |
| 3 | 22 | 0.002978 | 0.003377 | 0.007008 | 0.012956 | `Write a C++ declaration for a function that multiplies selected quantized output rows by a dense` |
| 4 | 18 | 0.005023 | 0.004396 | 0.007103 | 0.012983 | `Give two distinct ways a row-level precision search can overfit a tiny generation prompt suite.` |
| 5 | 21 | 0.003541 | 0.002952 | 0.007087 | 0.013168 | `In one sentence, explain why INT8 protection of an attention value projection may still reduce e` |
| 6 | 18 | 0.003938 | 0.003114 | 0.007126 | 0.013516 | `Draft a four-step ablation plan for testing whether a precision guard transfers across prompt sp` |
| 7 | 14 | 0.003751 | 0.004819 | 0.007256 | 0.013649 | `Compare activation reconstruction error and generated-text prefix match in one compact paragraph` |
| 8 | 17 | 0.003280 | 0.003073 | 0.007187 | 0.013048 | `Name two deployment metrics for an edge LLM runtime besides model size and perplexity.` |
| 9 | 20 | 0.003027 | 0.003199 | 0.007137 | 0.013305 | `Write a cautious README sentence explaining that a packed kernel benchmark is not an end-to-end ` |
| 10 | 17 | 0.003419 | 0.002700 | 0.007312 | 0.013868 | `Describe how hidden-state drift could be used as a cheap proxy for selecting sensitive rows.` |
| 11 | 18 | 0.003109 | 0.003828 | 0.007033 | 0.012625 | `State one reason an early transformer layer may need a different quantization policy than middle` |

## Guardrail

This is a teacher-forced continuous proxy. It supports ranking and diagnostics, but it does not prove generation quality by itself.