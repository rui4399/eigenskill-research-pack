# OLMo2 1B Uniform Fake-Quant Smoke

Date: 2026-06-05

This note records a short non-Qwen model-family smoke test for the
EigenSkill-Q fake-quant diagnostic harness. It is not a mixed-precision
allocator result and should not be reported as a production quantizer.

## Model And Setup

```text
model: allenai/OLMo-2-0425-1B-Instruct
prompt file: data_eval/text_prompts/wikitext2_validation_128.txt
prompt limit: 16
max length: 160
device: cuda
dtype: float16
group size: 128
config: data_eval/eval_configs/qwen25_uniform_group128.json
linear modules touched: 113
```

The run used the GPU guard with `--max-memory-ratio 0.85`.

## Result

```text
FP16          PPL 17.1191
uniform INT4  PPL 20.6993   delta NLL vs FP16 0.1899
uniform INT3  PPL 58.8374   delta NLL vs FP16 1.2346
```

GPU guard evidence:

```text
return code: 0
killed by guard: false
peak memory: 4004/8151 MiB = 49.12%
peak utilization: 50%
```

## Interpretation

This gives the repository a working 2025-era, non-Qwen 1B model smoke check.
Uniform INT4 is meaningfully worse than FP16 but still in the same order of
magnitude on this short slice. Uniform INT3 is much more destructive. The next
useful step is to run low-memory per-module sensitivity on the same model and
feed the resulting JSON into the C++ allocation planner.

## Gated Candidate Note

`google/gemma-3-1b-it` was also attempted with the same command shape, but the
Hugging Face repository was gated in this environment. The guard log is kept as
access-blocker evidence only:

```text
outputs/gemma3_1b_uniform_gpu_guard_wikitext2_16.json
```

Do not report Gemma as an experiment result unless access is granted and the
PPL summary is produced.

## Evidence Files

```text
outputs/olmo2_0425_1b_instruct_uniform_fake_quant_ppl_wikitext2_16_summary.json
outputs/olmo2_0425_1b_instruct_uniform_gpu_guard_wikitext2_16.json
outputs/gemma3_1b_uniform_gpu_guard_wikitext2_16.json
```
