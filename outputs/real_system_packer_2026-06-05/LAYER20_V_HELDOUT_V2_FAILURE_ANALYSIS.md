# Prompt-Suite Failure Analysis

Date: `2026-06-06T01:24:39+00:00`

## Run Summary

| run | exact | mean edit | mean prefix | speed |
|---|---:|---:|---:|---:|
| `baseline_layers17` | 12 / 12 | 1.0000 | 1.0000 | 0.9148x |
| `full_v8` | 12 / 12 | 1.0000 | 1.0000 | 0.8368x |
| `g0_1_2_4_5_6` | 9 / 12 | 0.9046 | 0.8112 | 0.9049x |
| `g0_1_2_4_5_6_7` | 9 / 12 | 0.9196 | 0.8295 | 0.9064x |
| `g0_2_3_4_5_6` | 11 / 12 | 0.9610 | 0.9373 | 0.9080x |

## Prompt Matrix

| id | prompt | `baseline_layers17` | `full_v8` | `g0_1_2_4_5_6` | `g0_1_2_4_5_6_7` | `g0_2_3_4_5_6` | best prefix | best edit |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 0 | Explain calibration-set sensitivity in mixed-bit LLM quantization usi... | Y | Y | N | N | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 3 | Write a C++ declaration for a function that multiplies selected quant... | Y | Y | N | Y | N | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 8 | Name two deployment metrics for an edge LLM runtime besides model siz... | Y | Y | N | N | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 11 | State one reason an early transformer layer may need a different quan... | Y | Y | Y | N | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 1 | Produce minified JSON with keys policy, evidence, and caveat for a pr... | Y | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 2 | How many bytes store 4096 four-bit signed weights when packed densely... | Y | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 4 | Give two distinct ways a row-level precision search can overfit a tin... | Y | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 5 | In one sentence, explain why INT8 protection of an attention value pr... | Y | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 6 | Draft a four-step ablation plan for testing whether a precision guard... | Y | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 7 | Compare activation reconstruction error and generated-text prefix mat... | Y | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 9 | Write a cautious README sentence explaining that a packed kernel benc... | Y | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 10 | Describe how hidden-state drift could be used as a cheap proxy for se... | Y | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |

## Hardest Prompts

### Prompt 0

Explain calibration-set sensitivity in mixed-bit LLM quantization using exactly two sentences.

- `baseline_layers17` exact=Y, prefix=1.0000, edit=1.0000; fused: Also, explain the role of the calibration set in the process of quantization. Additionally, explain the difference be...
- `full_v8` exact=Y, prefix=1.0000, edit=1.0000; fused: Also, explain the role of the calibration set in the process of quantization. Additionally, explain the difference be...
- `g0_2_3_4_5_6` exact=Y, prefix=1.0000, edit=1.0000; fused: Also, explain the role of the calibration set in the process of quantization. Additionally, explain the difference be...
- `g0_1_2_4_5_6` exact=N, prefix=0.3017, edit=0.8771; fused: Also, explain the role of the calibration set in the quantization process. Additionally, explain the difference betwe...
- `g0_1_2_4_5_6_7` exact=N, prefix=0.3017, edit=0.8771; fused: Also, explain the role of the calibration set in the quantization process. Additionally, explain the difference betwe...

### Prompt 3

Write a C++ declaration for a function that multiplies selected quantized output rows by a dense activation vector.

- `baseline_layers17` exact=Y, prefix=1.0000, edit=1.0000; fused: The function should be named `multiply` and have parameters `input` and `output`, each of which is a 2D array of size 10
- `full_v8` exact=Y, prefix=1.0000, edit=1.0000; fused: The function should be named `multiply` and have parameters `input` and `output`, each of which is a 2D array of size 10
- `g0_1_2_4_5_6_7` exact=Y, prefix=1.0000, edit=1.0000; fused: The function should be named `multiply` and have parameters `input` and `output`, each of which is a 2D array of size 10
- `g0_1_2_4_5_6` exact=N, prefix=0.3223, edit=0.5686; fused: The function should be named `multiply_quantized`, and the parameters should be `input`, `output`, and `activation` w...
- `g0_2_3_4_5_6` exact=N, prefix=0.2479, edit=0.5321; fused: The function should be named 'multiply_quantized' and have parameters 'input', 'output', and 'activation' as paramete...

### Prompt 8

Name two deployment metrics for an edge LLM runtime besides model size and perplexity.

- `baseline_layers17` exact=Y, prefix=1.0000, edit=1.0000; fused: Also, explain what each metric means. Answer: The question asks for **two deployment metrics** for an **edge LLM runt...
- `full_v8` exact=Y, prefix=1.0000, edit=1.0000; fused: Also, explain what each metric means. Answer: The question asks for **two deployment metrics** for an **edge LLM runt...
- `g0_2_3_4_5_6` exact=Y, prefix=1.0000, edit=1.0000; fused: Also, explain what each metric means. Answer: The question asks for **two deployment metrics** for an **edge LLM runt...
- `g0_1_2_4_5_6` exact=N, prefix=0.1104, edit=0.4091; fused: Also, explain why they are important for the deployment. **A.** **Model size and perplexity** **B.** **Model size and...
- `g0_1_2_4_5_6_7` exact=N, prefix=0.1104, edit=0.4091; fused: Also, explain why they are important for the deployment. **A.** **Model size and perplexity** **B.** **Model size and...
