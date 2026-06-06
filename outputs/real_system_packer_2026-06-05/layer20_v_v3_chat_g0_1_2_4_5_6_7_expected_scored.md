# Scored Prompt Suite

Source: `outputs/real_system_packer_2026-06-05/layer20_v_v3_chat_g0_1_2_4_5_6_7.json`

## Aggregate

| metric | value |
|---|---:|
| prompts | 24 |
| baseline passes | 15 / 24 |
| fused passes | 15 / 24 |
| baseline pass rate | 0.6250 |
| fused pass rate | 0.6250 |
| preserved passes | 15 |
| regressions | 0 |
| improvements | 0 |
| rules used | 8 |

## Rows

| id | rule | baseline | fused | status | expected |
|---:|---|---:|---:|---|---|
| 0 | `sentence_count_2` | false | false | same_fail | 2 sentences |
| 1 | `json_keys` | false | false | same_fail | hypothesis,proxy,risk |
| 2 | `byte_count_8192_int4` | false | false | same_fail | 4096 bytes |
| 3 | `cpp_signature` | false | false | same_fail | C++ signature |
| 4 | `keyword_min_hits` | true | true | preserved | selected,row,kernel,microbenchmark,decoding |
| 5 | `keyword_min_hits` | true | true | preserved | kv,cache,drift,quantization,exact |
| 6 | `keyword_min_hits` | true | true | preserved | ablation,rowguard,generalize,prompt,split |
| 7 | `keyword_min_hits` | true | true | preserved | exact,logit,l2,evaluation,signal |
| 8 | `keyword_min_hits` | false | false | same_fail | latency,memory,power,energy,ttft |
| 9 | `keyword_min_hits` | true | true | preserved | calibration,split,instability,study |
| 10 | `keyword_min_hits` | true | true | preserved | dense,fallback,layer,qkv,quality |
| 11 | `keyword_min_hits` | true | true | preserved | failure,int4,int8,row,generation |
| 12 | `keyword_min_hits` | true | true | preserved | packed,memory,compression,latency,speedup |
| 13 | `keyword_min_hits` | true | true | preserved | reconstruction,error,rank,attention,generation |
| 14 | `yaml_fields` | false | false | same_fail | model,policy,prompt_splits,allowed_claim |
| 15 | `average_bits_75p4_25p8` | false | false | same_fail | 5 bits |
| 16 | `keyword_min_hits` | false | false | same_fail | mmlu,gsm8k,humaneval,ifeval,bbh,gpqa |
| 17 | `keyword_min_hits` | true | true | preserved | warning,tuning,precision,test,prompt |
| 18 | `keyword_min_hits` | true | true | preserved | proxy,penalize,hidden,drift,exact |
| 19 | `keyword_min_hits` | true | true | preserved | speed,quality,evidence,experiment,plan |
| 20 | `keyword_min_hits` | true | true | preserved | triton,dense,gemm,batch,shape |
| 21 | `json_keys` | false | false | same_fail | symptom,next_test |
| 22 | `contains_all` | true | true | preserved | prompt,split,instability |
| 23 | `keyword_min_hits` | true | true | preserved | baseline,full,rowguard,candidate |
