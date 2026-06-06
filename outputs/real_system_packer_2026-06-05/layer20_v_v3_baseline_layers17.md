# Fused ESMP QKV Prompt-Suite Comparison

Date: `2026-06-06T01:55:27Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[1, 7]`
Dense roles: `[]`
Max new tokens: `32`
Sync mode: `end`
Prompts: `24`

## Aggregate

| metric | value |
|---|---:|
| exact matches | 19 / 24 |
| exact match rate | 0.7917 |
| mean char edit similarity | 0.9144 |
| median char edit similarity | 1.0000 |
| mean common prefix ratio | 0.8906 |
| mean baseline tokens/s | 23.9053 |
| mean fused tokens/s | 25.8326 |
| mean fused/baseline speed | 1.0806x |
| median baseline TTFT s | 0.045963 |
| median fused TTFT s | 0.042825 |

## Replacement Runtime

- Replacement compression vs FP32: `3.9082x`
- Dense role calls: `0`
- Wrapper calls / fused compute calls: `4608 / 1536`
- Cache hits / misses: `3072 / 1536`
- Fused CUDA event sum: `1148.8322 ms`
- Peak CUDA memory: `1168.81 MiB`

## Per-Prompt

| id | exact | edit sim | prefix ratio | baseline tok/s | fused tok/s | baseline text | fused text |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | True | 1.0000 | 1.0000 | 22.4456 | 15.2366 | ` Also, explain in two sentences why calibration prompts can bias a mixed-precision row search in a d` | ` Also, explain in two sentences why calibration prompts can bias a mixed-precision row search in a d` |
| 1 | True | 1.0000 | 1.0000 | 22.3220 | 25.9076 | ` The JSON should have a key for each of the three variables and the values should be the number of t` | ` The JSON should have a key for each of the three variables and the values should be the number of t` |
| 2 | True | 1.0000 | 1.0000 | 25.7861 | 18.0714 | ` The answer should be in the format: "packed byte count: 128 bytes".  To compute the packed byte cou` | ` The answer should be in the format: "packed byte count: 128 bytes".  To compute the packed byte cou` |
| 3 | True | 1.0000 | 1.0000 | 23.2485 | 25.0992 | ` The function should be named load, and it should take a single parameter of type vector<vector<int>` | ` The function should be named load, and it should take a single parameter of type vector<vector<int>` |
| 4 | False | 0.5337 | 0.4496 | 23.2746 | 25.6764 | ` Why is this important for the performance of the system?  **A.** The kernel has a large number of r` | ` Why is this important for the performance of the system? Answer: The selected-row kernel can be fas` |
| 5 | False | 0.5714 | 0.4667 | 23.6304 | 30.6279 | ` Also, explain why the same sentence can be used to describe both the KV cache and the text cache in` | ` Also, explain why the same sentence can be used to describe both the problem and the solution. Answ` |
| 6 | True | 1.0000 | 1.0000 | 26.6342 | 20.9775 | ` What are the reasons for the need for these ablations? What are the benefits of using a rowguard ge` | ` What are the reasons for the need for these ablations? What are the benefits of using a rowguard ge` |
| 7 | True | 1.0000 | 1.0000 | 22.7171 | 29.0634 | ` Also, provide a sample of the output for the user. The user is a researcher in the field of machine` | ` Also, provide a sample of the output for the user. The user is a researcher in the field of machine` |
| 8 | True | 1.0000 | 1.0000 | 28.1851 | 27.2197 | ` Also, explain what each metric means in terms of the system's performance and the user's experience` | ` Also, explain what each metric means in terms of the system's performance and the user's experience` |
| 9 | True | 1.0000 | 1.0000 | 25.1475 | 23.9212 | ` The title should be in English, and the subtitle should be in English. The title should be a bit mo` | ` The title should be in English, and the subtitle should be in English. The title should be a bit mo` |
| 10 | True | 1.0000 | 1.0000 | 24.0134 | 30.9347 | ` What are the benefits of using a dense fallback for layer 0 in the context of the QKV replacement s` | ` What are the benefits of using a dense fallback for layer 0 in the context of the QKV replacement s` |
| 11 | False | 0.5116 | 0.3256 | 23.0185 | 22.7851 | ` What is the reason for this failure case?  Answer: The failure case is the case where a row group i` | ` What is the reason for this failure case? What is the solution?  **A.** A row group with 10000 rows` |
| 12 | True | 1.0000 | 1.0000 | 27.4272 | 22.9319 | ` Also, explain why it's important to use a memory management system that supports memory compression` | ` Also, explain why it's important to use a memory management system that supports memory compression` |
| 13 | True | 1.0000 | 1.0000 | 19.3155 | 28.7512 | `   The answer should be in one paragraph, and the answer should be in the form of a sentence.   The ` | `   The answer should be in one paragraph, and the answer should be in the form of a sentence.   The ` |
| 14 | True | 1.0000 | 1.0000 | 25.2936 | 27.4413 | ` The model is a specific model, like "llama-2-70b", and the policy is a specific policy, like "stric` | ` The model is a specific model, like "llama-2-70b", and the policy is a specific policy, like "stric` |
| 15 | True | 1.0000 | 1.0000 | 22.4716 | 24.8558 | ` Also, what is the average bit width if 80 percent of rows use 4-bit and 20 percent use 8-bit?  To f` | ` Also, what is the average bit width if 80 percent of rows use 4-bit and 20 percent use 8-bit?  To f` |
| 16 | True | 1.0000 | 1.0000 | 23.7009 | 27.1136 | ` What are the differences between these benchmarks and perplexity? What are the implications for the` | ` What are the differences between these benchmarks and perplexity? What are the implications for the` |
| 17 | True | 1.0000 | 1.0000 | 20.4203 | 28.4401 | `   The policy is to use a single prompt for all tasks, and the prompt is not a single sentence.   Th` | `   The policy is to use a single prompt for all tasks, and the prompt is not a single sentence.   Th` |
| 18 | False | 0.7532 | 0.6783 | 26.5926 | 23.6965 | ` How to implement this in practice?  As a result of the above, the model can be trained to avoid ove` | ` How to implement this in practice?  As a result of the above, the model can be trained to avoid the` |
| 19 | True | 1.0000 | 1.0000 | 24.1748 | 30.7882 | ` The experiment should include a control group and a treatment group. The experiment should be condu` | ` The experiment should include a control group and a treatment group. The experiment should be condu` |
| 20 | True | 1.0000 | 1.0000 | 21.5076 | 23.9196 | ` What is the purpose of the GEMM in the context of the training of neural networks? What is the purp` | ` What is the purpose of the GEMM in the context of the training of neural networks? What is the purp` |
| 21 | True | 1.0000 | 1.0000 | 21.2790 | 29.0278 | ` The symptom should be a string that describes the symptom of the rowguard failure. The next_test sh` | ` The symptom should be a string that describes the symptom of the rowguard failure. The next_test sh` |
| 22 | False | 0.5746 | 0.4551 | 25.8863 | 29.5499 | `   The prompt-split instability is a phenomenon where the model's performance on a single task is si` | `   The prompt-split instability is a phenomenon where the model's performance on one task is inconsi` |
| 23 | True | 1.0000 | 1.0000 | 25.2360 | 27.9457 | ` What is the difference between rowguard and full-V8? What is the difference between baseline and fu` | ` What is the difference between rowguard and full-V8? What is the difference between baseline and fu` |

## Guardrail

This is a deterministic local text-similarity audit, not a semantic benchmark. It is useful for detecting output drift from fused QKV replacement, but it does not replace MMLU/GSM8K/IFEval-style evaluation.
