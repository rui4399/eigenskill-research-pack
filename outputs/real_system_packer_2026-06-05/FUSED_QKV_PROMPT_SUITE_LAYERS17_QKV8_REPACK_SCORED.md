# Scored Prompt Suite

Source: `outputs\real_system_packer_2026-06-05\fused_qkv_prompt_suite_layers17_qkv8_repack.json`

## Aggregate

| metric | value |
|---|---:|
| prompts | 6 |
| baseline passes | 5 / 6 |
| fused passes | 5 / 6 |
| baseline pass rate | 0.8333 |
| fused pass rate | 0.8333 |
| preserved passes | 5 |
| regressions | 0 |
| improvements | 0 |
| rules used | 2 |

## Rows

| id | rule | baseline | fused | status | expected |
|---:|---|---:|---:|---|---|
| 0 | `nonempty_answer` | true | true | preserved | non-empty answer |
| 1 | `nonempty_answer` | true | true | preserved | non-empty answer |
| 2 | `nonempty_answer` | true | true | preserved | non-empty answer |
| 3 | `cpp_signature` | false | false | same_fail | C++ signature |
| 4 | `nonempty_answer` | true | true | preserved | non-empty answer |
| 5 | `nonempty_answer` | true | true | preserved | non-empty answer |
