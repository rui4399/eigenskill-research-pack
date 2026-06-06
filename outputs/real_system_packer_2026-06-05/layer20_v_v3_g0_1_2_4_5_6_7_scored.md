# Scored Prompt Suite

Source: `outputs/real_system_packer_2026-06-05/layer20_v_v3_g0_1_2_4_5_6_7.json`

## Aggregate

| metric | value |
|---|---:|
| prompts | 24 |
| baseline passes | 12 / 24 |
| fused passes | 13 / 24 |
| baseline pass rate | 0.5000 |
| fused pass rate | 0.5417 |
| preserved passes | 12 |
| regressions | 0 |
| improvements | 1 |
| rules used | 16 |

## Rows

| id | rule | baseline | fused | status | expected |
|---:|---|---:|---:|---|---|
| 0 | `sentence_count_2` | true | true | preserved | 2 sentences |
| 1 | `json_keys` | false | false | same_fail | hypothesis,proxy,risk |
| 2 | `byte_count_8192_int4` | false | false | same_fail | 4096 bytes |
| 3 | `cpp_signature` | false | false | same_fail | C++ signature |
| 4 | `selected_row_kernel` | true | true | preserved | selected,row,kernel,benchmark,decode |
| 5 | `drift_proxy` | true | true | preserved | drift,proxy,state,cache |
| 6 | `nonempty_answer` | true | true | preserved | non-empty answer |
| 7 | `nonempty_answer` | true | true | preserved | non-empty answer |
| 8 | `nonempty_answer` | true | true | preserved | non-empty answer |
| 9 | `nonempty_answer` | true | true | preserved | non-empty answer |
| 10 | `layer0_policy` | true | true | preserved | layer,0,qkv,quality,fallback |
| 11 | `nonempty_answer` | true | true | preserved | non-empty answer |
| 12 | `claim_caveat` | false | false | same_fail | not,claim,speed,latency,compression |
| 13 | `reconstruction_vs_generation` | false | false | same_fail | reconstruction,generation,attention,row |
| 14 | `yaml_fields` | false | false | same_fail | model,policy,prompt_splits,allowed_claim |
| 15 | `average_bits_75p4_25p8` | false | false | same_fail | 5 bits |
| 16 | `nonempty_answer` | true | true | preserved | non-empty answer |
| 17 | `claim_caveat` | false | false | same_fail | not,claim,speed,latency,compression |
| 18 | `drift_proxy` | false | false | same_fail | drift,proxy,state,cache |
| 19 | `speed_quality_plan` | false | true | improved | speed,quality,experiment |
| 20 | `triton_dense_shape` | false | false | same_fail | triton,dense,gemm,batch,launch |
| 21 | `json_keys` | false | false | same_fail | symptom,next_test |
| 22 | `sentence_count_1` | true | true | preserved | 1 sentences |
| 23 | `candidate_choice` | true | true | preserved | baseline,full,rowguard |
