# Model Artifacts

Large model weights, LoRA adapters, merged checkpoints, and Hugging Face cache
contents are intentionally not committed to this repository.

## What Is Public

The public artifact boundary contains:

- small prompt fixtures under `data_eval/`;
- evaluation configs under `data_eval/eval_configs/`;
- fake-quant PPL summaries, gate JSON, and gate Markdown under `outputs/`;
- ESMP package metadata and integrity checks for selected packed slices;
- source code for measurement, allocation, packing, and gate verification.

These files are enough to inspect the committed evidence ledger, but they are
not a replacement for the original base model checkpoints.

## Referenced Base Models

The current evidence refers to public base models such as:

```text
Qwen/Qwen3-0.6B
Qwen/Qwen3-1.7B
allenai/OLMo-2-0425-1B-Instruct
HuggingFaceTB/SmolLM2-1.7B-Instruct
Qwen/Qwen2.5-0.5B-Instruct
Qwen/Qwen2.5-1.5B-Instruct
```

Exact local cache state can vary by machine. If a model is gated, unavailable,
or not cached, treat that as an environment gap rather than a failed quality
result.

## Historical Local Artifacts

Earlier local runs produced SmolLM2-360M LoRA/merged/INT8 artifacts. They are
not part of the current paper-facing claim set and should not be cited as the
main model evidence.

Historical examples that may exist on the original workstation:

```text
models/eigenskill-smollm2-360m-lora-v2-fp16
models/eigenskill-smollm2-360m-merged-v2-fp16
models/eigenskill-smollm2-360m-int8-v2-dynamic
```

## Weight Release Policy

If future trained adapters or packed model artifacts become paper-facing, they
should be released through one of:

- Hugging Face model repositories;
- GitHub Releases with checksums;
- Git LFS-backed storage if the repository policy allows it.

Until then, this repository should be read as a source-and-evidence pack, not a
model-weight distribution.
