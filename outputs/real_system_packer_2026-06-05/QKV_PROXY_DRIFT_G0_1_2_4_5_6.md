# QKV Replacement Proxy Drift

Date: `2026-06-06T01:38:25+00:00`
Candidate: `g0_1_2_4_5_6`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Prompt file: `outputs/real_system_packer_2026-06-05/heldout_prompt_suite_v2.txt`
Prompts: `12`

## Aggregate

| metric | mean | median | max |
|---|---:|---:|---:|
| final hidden rel-L2 | 0.011246 | 0.011127 | 0.013026 |
| last logits rel-L2 | 0.020944 | 0.021262 | 0.026978 |
| KV mean rel-L2 | 0.029307 | 0.029360 | 0.030684 |
| KV max rel-L2 | 0.137661 | 0.137148 | 0.145149 |

## Per Prompt

| id | input len | final hidden rel-L2 | logits rel-L2 | KV mean rel-L2 | KV max rel-L2 | prompt |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 17 | 0.011709 | 0.025692 | 0.028389 | 0.132928 | `Explain calibration-set sensitivity in mixed-bit LLM quantization using exactly two sentences.` |
| 1 | 19 | 0.011654 | 0.021570 | 0.029354 | 0.136546 | `Produce minified JSON with keys policy, evidence, and caveat for a precision-routing experiment.` |
| 2 | 24 | 0.012606 | 0.023027 | 0.028004 | 0.130275 | `How many bytes store 4096 four-bit signed weights when packed densely? Give only the number and ` |
| 3 | 22 | 0.010362 | 0.014929 | 0.029365 | 0.138975 | `Write a C++ declaration for a function that multiplies selected quantized output rows by a dense` |
| 4 | 18 | 0.011005 | 0.022192 | 0.028739 | 0.134362 | `Give two distinct ways a row-level precision search can overfit a tiny generation prompt suite.` |
| 5 | 21 | 0.010770 | 0.016862 | 0.029875 | 0.141444 | `In one sentence, explain why INT8 protection of an attention value projection may still reduce e` |
| 6 | 18 | 0.009854 | 0.018449 | 0.028948 | 0.135384 | `Draft a four-step ablation plan for testing whether a precision guard transfers across prompt sp` |
| 7 | 14 | 0.011248 | 0.020953 | 0.029368 | 0.137214 | `Compare activation reconstruction error and generated-text prefix match in one compact paragraph` |
| 8 | 17 | 0.013026 | 0.026978 | 0.029282 | 0.137082 | `Name two deployment metrics for an edge LLM runtime besides model size and perplexity.` |
| 9 | 20 | 0.010718 | 0.017580 | 0.029870 | 0.141067 | `Write a cautious README sentence explaining that a packed kernel benchmark is not an end-to-end ` |
| 10 | 17 | 0.010273 | 0.019342 | 0.030684 | 0.145149 | `Describe how hidden-state drift could be used as a cheap proxy for selecting sensitive rows.` |
| 11 | 18 | 0.011733 | 0.023750 | 0.029804 | 0.141508 | `State one reason an early transformer layer may need a different quantization policy than middle` |

## Guardrail

This is a teacher-forced continuous proxy. It supports ranking and diagnostics, but it does not prove generation quality by itself.