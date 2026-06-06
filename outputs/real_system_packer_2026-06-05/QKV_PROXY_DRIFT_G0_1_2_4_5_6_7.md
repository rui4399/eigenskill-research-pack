# QKV Replacement Proxy Drift

Date: `2026-06-06T01:39:06+00:00`
Candidate: `g0_1_2_4_5_6_7`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Prompt file: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v2.txt`
Prompts: `12`

## Aggregate

| metric | mean | median | max |
|---|---:|---:|---:|
| final hidden rel-L2 | 0.009189 | 0.008991 | 0.011128 |
| last logits rel-L2 | 0.015244 | 0.015777 | 0.020612 |
| KV mean rel-L2 | 0.021926 | 0.022078 | 0.022752 |
| KV max rel-L2 | 0.093375 | 0.093949 | 0.097559 |

## Per Prompt

| id | input len | final hidden rel-L2 | logits rel-L2 | KV mean rel-L2 | KV max rel-L2 | prompt |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 17 | 0.009619 | 0.017687 | 0.021367 | 0.090794 | `Explain calibration-set sensitivity in mixed-bit LLM quantization using exactly two sentences.` |
| 1 | 19 | 0.009838 | 0.018241 | 0.022050 | 0.092724 | `Produce minified JSON with keys policy, evidence, and caveat for a precision-routing experiment.` |
| 2 | 24 | 0.010681 | 0.020612 | 0.021105 | 0.088881 | `How many bytes store 4096 four-bit signed weights when packed densely? Give only the number and ` |
| 3 | 22 | 0.008251 | 0.010038 | 0.021858 | 0.093931 | `Write a C++ declaration for a function that multiplies selected quantized output rows by a dense` |
| 4 | 18 | 0.008870 | 0.016414 | 0.021289 | 0.089664 | `Give two distinct ways a row-level precision search can overfit a tiny generation prompt suite.` |
| 5 | 21 | 0.008872 | 0.012306 | 0.022112 | 0.094863 | `In one sentence, explain why INT8 protection of an attention value projection may still reduce e` |
| 6 | 18 | 0.008180 | 0.012797 | 0.021813 | 0.092576 | `Draft a four-step ablation plan for testing whether a precision guard transfers across prompt sp` |
| 7 | 14 | 0.009186 | 0.017892 | 0.022160 | 0.093967 | `Compare activation reconstruction error and generated-text prefix match in one compact paragraph` |
| 8 | 17 | 0.011128 | 0.017544 | 0.022166 | 0.094385 | `Name two deployment metrics for an edge LLM runtime besides model size and perplexity.` |
| 9 | 20 | 0.008208 | 0.012382 | 0.022105 | 0.094479 | `Write a cautious README sentence explaining that a packed kernel benchmark is not an end-to-end ` |
| 10 | 17 | 0.008327 | 0.011874 | 0.022752 | 0.097559 | `Describe how hidden-state drift could be used as a cheap proxy for selecting sensitive rows.` |
| 11 | 18 | 0.009110 | 0.015141 | 0.022333 | 0.096680 | `State one reason an early transformer layer may need a different quantization policy than middle` |

## Guardrail

This is a teacher-forced continuous proxy. It supports ranking and diagnostics, but it does not prove generation quality by itself.