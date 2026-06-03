# Model Artifacts

Large trained model artifacts are intentionally not committed to this GitHub
repository.

Verified local artifacts from the current run:

```text
models/eigenskill-smollm2-360m-lora-v2-fp16
models/eigenskill-smollm2-360m-merged-v2-fp16
models/eigenskill-smollm2-360m-int8-v2-dynamic
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
