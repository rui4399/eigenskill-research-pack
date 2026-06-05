# SmolLM2-1.7B Retry Smoke Result

This records the retry after the earlier SmolLM2-1.7B load failure.

## Cache Status

`HuggingFaceTB/SmolLM2-1.7B-Instruct` now has the PyTorch
`model.safetensors` file available and can be loaded by `transformers`.
The broader repository cache still contains incomplete ONNX-side blobs, so
the cache audit remains:

```text
status: incomplete_cache
incomplete files: 2
```

That means this is valid for PyTorch fake-quant smoke evaluation, but it is
not a complete full-repository Hugging Face snapshot.

## Smoke Evaluation

Command output:

```text
model: HuggingFaceTB/SmolLM2-1.7B-Instruct
dataset: WikiText2 validation, 16 prompts
max length: 128
group size: 128
FP16 PPL:         12.6903
uniform INT4 PPL: 18.1431
uniform INT3 PPL: 197.0120
```

GPU guard:

```text
max memory: 5109 / 8151 MiB = 62.68%
max utilization: 52%
killed by guard: false
```

## Interpretation

The retry confirms SmolLM2-1.7B is now a runnable third 1B+ model family for
the PyTorch fake-quant pipeline. It is not yet a full consensus-vs-random16
result; the next step is to measure or adapt allocation evidence for this
model before placing it in the cross-model matrix.

Artifacts:

```text
outputs/smollm2_1p7b_predownload_retry_report.md
outputs/smollm2_1p7b_predownload_retry_summary.json
outputs/smollm2_1p7b_uniform_ppl_wikitext2_16_retry_summary.json
outputs/smollm2_1p7b_uniform_ppl_wikitext2_16_retry_guard.json
```

