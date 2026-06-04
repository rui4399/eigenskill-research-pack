# Model Artifacts

Large trained model artifacts are intentionally not committed to this GitHub
repository.

Verified local artifacts from the current run:

```text
models/eigenskill-smollm2-360m-lora-v2-fp16
models/eigenskill-smollm2-360m-merged-v2-fp16
models/eigenskill-smollm2-360m-int8-v2-dynamic
```

Additional public base model used for fake-quant baseline evaluation:

```text
Qwen/Qwen2.5-0.5B-Instruct
```

This is downloaded through the Hugging Face cache and is not committed to the
repository. The committed evidence is the evaluation configuration and JSON
summaries:

```text
data_eval/eval_configs/qwen25_uniform_group128.json
outputs/qwen25_0p5b_fake_quant_ppl_uniform_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_uniform_group128_c4_en_validation_64_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_group128_c4_en_validation_64_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_limit8_group128_wikitext2_128_summary.json
outputs/qwen25_0p5b_fake_quant_ppl_loss_sensitive_limit8_group128_c4_en_validation_64_summary.json
```

Expected local sizes:

```text
LoRA adapter v2:       about 243 MiB
Merged FP16 v2:        about 694 MiB
Dynamic INT8 CPU v2:   about 529 MiB
```

The package manifest with exact paths and verification results is available at:

```text
outputs/eigenskill_v2_package_manifest.json
```

Recommended next delivery target for model weights:

```text
Hugging Face model repository or Git LFS-backed private storage
```
