# Prompt-Suite Failure Analysis

Date: `2026-06-06T00:04:11+00:00`

## Run Summary

| run | exact | mean edit | mean prefix | speed |
|---|---:|---:|---:|---:|
| `full_v8` | 5 / 6 | 0.9383 | 0.9096 | 0.8477x |
| `g0_1_2_4_5_6` | 5 / 6 | 0.9700 | 0.9612 | 0.9378x |
| `g0_1_2_4_5_6_7` | 6 / 6 | 1.0000 | 1.0000 | 0.9314x |
| `g0_1_2_4_5_6_7_repeat` | 6 / 6 | 1.0000 | 1.0000 | 0.9575x |

## Prompt Matrix

| id | prompt | `full_v8` | `g0_1_2_4_5_6` | `g0_1_2_4_5_6_7` | `g0_1_2_4_5_6_7_repeat` | best prefix | best edit |
|---:|---|---:|---:|---:|---:|---|---|
| 0 | Explain mixed-precision quantization in one concise paragraph. | N | Y | Y | Y | `g0_1_2_4_5_6` 1.0000 | `g0_1_2_4_5_6` 1.0000 |
| 1 | Give a short JSON object with fields task, risk, and next_step for mo... | Y | N | Y | Y | `full_v8` 1.0000 | `full_v8` 1.0000 |
| 2 | Solve briefly: if an INT4 row stores 1024 weights, how many packed by... | Y | Y | Y | Y | `full_v8` 1.0000 | `full_v8` 1.0000 |
| 3 | Write a compact C++ function signature for a mixed INT4/INT8 GEMV ker... | Y | Y | Y | Y | `full_v8` 1.0000 | `full_v8` 1.0000 |
| 4 | List two reasons calibration data can make quantization unstable. | Y | Y | Y | Y | `full_v8` 1.0000 | `full_v8` 1.0000 |
| 5 | In one sentence, explain why replacing QKV projections can change gen... | Y | Y | Y | Y | `full_v8` 1.0000 | `full_v8` 1.0000 |

## Hardest Prompts

### Prompt 0

Explain mixed-precision quantization in one concise paragraph.

- `g0_1_2_4_5_6` exact=Y, prefix=1.0000, edit=1.0000; fused: Also, explain the difference between mixed-precision and single-precision. | Also, explain the difference between mix...
- `g0_1_2_4_5_6_7` exact=Y, prefix=1.0000, edit=1.0000; fused: Also, explain the difference between mixed-precision and single-precision. | Also, explain the difference between mix...
- `g0_1_2_4_5_6_7_repeat` exact=Y, prefix=1.0000, edit=1.0000; fused: Also, explain the difference between mixed-precision and single-precision. | Also, explain the difference between mix...
- `full_v8` exact=N, prefix=0.4578, edit=0.6301; fused: Also, explain the difference between mixed-precision and single-precision. Please provide an example of a scenario wh...

### Prompt 1

Give a short JSON object with fields task, risk, and next_step for model quantization.

- `full_v8` exact=Y, prefix=1.0000, edit=1.0000; fused: The task is to implement a model quantization strategy that reduces the model's computational complexity. The model i...
- `g0_1_2_4_5_6_7` exact=Y, prefix=1.0000, edit=1.0000; fused: The task is to implement a model quantization strategy that reduces the model's computational complexity. The model i...
- `g0_1_2_4_5_6_7_repeat` exact=Y, prefix=1.0000, edit=1.0000; fused: The task is to implement a model quantization strategy that reduces the model's computational complexity. The model i...
- `g0_1_2_4_5_6` exact=N, prefix=0.7673, edit=0.8198; fused: The task is to implement a model quantization strategy that reduces the model's computational complexity. The model i...
