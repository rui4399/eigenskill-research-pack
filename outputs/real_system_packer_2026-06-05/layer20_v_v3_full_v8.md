# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-06T01:56:40Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7, 20]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `24`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 19 / 24 |
| exact match rate | 0.7917 |
| mean char edit similarity | 0.8966 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 0.8656 |
| mean baseline tokens/s | 25.2374 |
| mean fused tokens/s | 26.0157 |
| mean fused/baseline speed | 1.0308x |
| median baseline TTFT s | 0.039814 |
| median fused TTFT s | 0.036052 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `6912 / 2304`
- Cache hits / misses: `4608 / 2304`
- Fused CUDA event sum: `684.4586 ms`
- Peak CUDA memory: `1164.88 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 30.4413 | 17.0455 | ` Also, explain in two sentences why calibration prompts can bias a mixed-precision row search in a d` | ` Also, explain in two sentences why calibration prompts can bias a mixed-precision row search in a d` |
| 1 | True | 1.0000 | 1.0000 | 29.1123 | 27.8494 | ` The JSON should have a key for each of the three variables and the values should be the number of t` | ` The JSON should have a key for each of the three variables and the values should be the number of t` |
| 2 | True | 1.0000 | 1.0000 | 20.7199 | 28.9840 | ` The answer should be in the format: "packed byte count: 128 bytes".  To compute the packed byte cou` | ` The answer should be in the format: "packed byte count: 128 bytes".  To compute the packed byte cou` |
| 3 | False | 0.4035 | 0.1988 | 25.2259 | 23.2257 | ` The function should be named load, and it should take a single parameter of type vector<vector<int>` | ` The function should be named loadRowMixedWeight, and it should take the following parameters: - inp` |
| 4 | True | 1.0000 | 1.0000 | 20.3359 | 24.3568 | ` Why is this important for the performance of the system?  **A.** The kernel has a large number of r` | ` Why is this important for the performance of the system?  **A.** The kernel has a large number of r` |
| 5 | True | 1.0000 | 1.0000 | 21.3267 | 27.9466 | ` Also, explain why the same sentence can be used to describe both the KV cache and the text cache in` | ` Also, explain why the same sentence can be used to describe both the KV cache and the text cache in` |
| 6 | True | 1.0000 | 1.0000 | 24.1784 | 27.1101 | ` What are the reasons for the need for these ablations? What are the benefits of using a rowguard ge` | ` What are the reasons for the need for these ablations? What are the benefits of using a rowguard ge` |
| 7 | True | 1.0000 | 1.0000 | 20.6965 | 28.0123 | ` Also, provide a sample of the output for the user. The user is a researcher in the field of machine` | ` Also, provide a sample of the output for the user. The user is a researcher in the field of machine` |
| 8 | True | 1.0000 | 1.0000 | 25.9761 | 28.4229 | ` Also, explain what each metric means in terms of the system's performance and the user's experience` | ` Also, explain what each metric means in terms of the system's performance and the user's experience` |
| 9 | True | 1.0000 | 1.0000 | 29.5594 | 27.2395 | ` The title should be in English, and the subtitle should be in English. The title should be a bit mo` | ` The title should be in English, and the subtitle should be in English. The title should be a bit mo` |
| 10 | True | 1.0000 | 1.0000 | 26.0274 | 21.8494 | ` What are the benefits of using a dense fallback for layer 0 in the context of the QKV replacement s` | ` What are the benefits of using a dense fallback for layer 0 in the context of the QKV replacement s` |
| 11 | False | 0.5116 | 0.3256 | 29.8919 | 30.0439 | ` What is the reason for this failure case?  Answer: The failure case is the case where a row group i` | ` What is the reason for this failure case? What is the solution?  **A.** A row group with 10000 rows` |
| 12 | True | 1.0000 | 1.0000 | 29.8442 | 24.7059 | ` Also, explain why it's important to use a memory management system that supports memory compression` | ` Also, explain why it's important to use a memory management system that supports memory compression` |
| 13 | True | 1.0000 | 1.0000 | 23.3755 | 25.6822 | `   The answer should be in one paragraph, and the answer should be in the form of a sentence.   The ` | `   The answer should be in one paragraph, and the answer should be in the form of a sentence.   The ` |
| 14 | True | 1.0000 | 1.0000 | 28.2133 | 26.4021 | ` The model is a specific model, like "llama-2-70b", and the policy is a specific policy, like "stric` | ` The model is a specific model, like "llama-2-70b", and the policy is a specific policy, like "stric` |
| 15 | True | 1.0000 | 1.0000 | 20.0786 | 23.2331 | ` Also, what is the average bit width if 80 percent of rows use 4-bit and 20 percent use 8-bit?  To f` | ` Also, what is the average bit width if 80 percent of rows use 4-bit and 20 percent use 8-bit?  To f` |
| 16 | False | 0.7624 | 0.7443 | 30.8974 | 30.0628 | ` What are the differences between these benchmarks and perplexity? What are the implications for the` | ` What are the differences between these benchmarks and perplexity? What are the implications for the` |
| 17 | False | 0.2662 | 0.0507 | 30.9877 | 24.1821 | `   The policy is to use a single prompt for all tasks, and the prompt is not a single sentence.   Th` | `   The user is a content creator who wants to use the AI to generate content for a product. The prod` |
| 18 | True | 1.0000 | 1.0000 | 21.9840 | 26.6944 | ` How to implement this in practice?  As a result of the above, the model can be trained to avoid ove` | ` How to implement this in practice?  As a result of the above, the model can be trained to avoid ove` |
| 19 | True | 1.0000 | 1.0000 | 25.9180 | 29.6399 | ` The experiment should include a control group and a treatment group. The experiment should be condu` | ` The experiment should include a control group and a treatment group. The experiment should be condu` |
| 20 | True | 1.0000 | 1.0000 | 19.8982 | 25.8805 | ` What is the purpose of the GEMM in the context of the training of neural networks? What is the purp` | ` What is the purpose of the GEMM in the context of the training of neural networks? What is the purp` |
| 21 | True | 1.0000 | 1.0000 | 21.7719 | 26.0067 | ` The symptom should be a string that describes the symptom of the rowguard failure. The next_test sh` | ` The symptom should be a string that describes the symptom of the rowguard failure. The next_test sh` |
| 22 | False | 0.5746 | 0.4551 | 24.6094 | 25.0378 | `   The prompt-split instability is a phenomenon where the model's performance on a single task is si` | `   The prompt-split instability is a phenomenon where the model's performance on one task is inconsi` |
| 23 | True | 1.0000 | 1.0000 | 24.6282 | 24.7622 | ` What is the difference between rowguard and full-V8? What is the difference between baseline and fu` | ` What is the difference between rowguard and full-V8? What is the difference between baseline and fu` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
