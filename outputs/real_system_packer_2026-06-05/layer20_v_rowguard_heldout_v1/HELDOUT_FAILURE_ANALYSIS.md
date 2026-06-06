# Prompt-Suite Failure Analysis

Date: `2026-06-06T00:26:36+00:00`

## Run Summary

| run | exact | mean edit | mean prefix | speed |
|---|---:|---:|---:|---:|
| `baseline_layers17` | 11 / 12 | 0.9398 | 0.9172 | 0.8316x |
| `full_v8` | 11 / 12 | 0.9398 | 0.9172 | 0.9427x |
| `g0_1_2_4_5_6` | 9 / 12 | 0.8456 | 0.7725 | 0.9129x |
| `g0_1_2_4_5_6_7` | 9 / 12 | 0.8456 | 0.7725 | 0.7947x |

## Prompt Matrix

| id | prompt | `baseline_layers17` | `full_v8` | `g0_1_2_4_5_6` | `g0_1_2_4_5_6_7` | best prefix | best edit |
|---:|---|---:|---:|---:|---:|---|---|
| 4 | Name two reasons a prompt-conditioned precision guard might overfit a... | N | N | N | N | `baseline_layers17` 0.0060 | `baseline_layers17` 0.2771 |
| 7 | In one concise paragraph, compare local reconstruction error and gene... | Y | Y | N | N | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 8 | List two metrics besides perplexity for evaluating a real LLM inferen... | Y | Y | N | N | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 0 | Summarize post-training mixed-precision quantization in two short sen... | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 1 | Return a compact JSON object with keys method, failure_mode, and miti... | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 2 | If 2048 INT4 weights are packed two per byte, how many bytes are requ... | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 3 | Write one C++ function prototype for unpacking mixed 4-bit and 8-bit ... | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 5 | Explain in one sentence why higher precision can sometimes make a qua... | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 6 | Give a three-step experiment plan to test whether a row-level precisi... | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 9 | Write a short warning label for a README about not claiming end-to-en... | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 10 | Briefly describe how KV-cache error could guide row selection in atte... | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |
| 11 | Give one sentence explaining why layer 0 may need separate treatment ... | Y | Y | Y | Y | `baseline_layers17` 1.0000 | `baseline_layers17` 1.0000 |

## Hardest Prompts

### Prompt 4

Name two reasons a prompt-conditioned precision guard might overfit a small prompt suite.

- `baseline_layers17` exact=N, prefix=0.0060, edit=0.2771; fused: What are the two reasons? What are the two reasons for overfitting a large prompt suite? What is the difference betwe...
- `full_v8` exact=N, prefix=0.0060, edit=0.2771; fused: What are the two reasons? What are the two reasons for overfitting a large prompt suite? What is the difference betwe...
- `g0_1_2_4_5_6` exact=N, prefix=0.0060, edit=0.2771; fused: What are the two reasons? What are the two reasons for overfitting a large prompt suite? What is the difference betwe...
- `g0_1_2_4_5_6_7` exact=N, prefix=0.0060, edit=0.2771; fused: What are the two reasons? What are the two reasons for overfitting a large prompt suite? What is the difference betwe...
