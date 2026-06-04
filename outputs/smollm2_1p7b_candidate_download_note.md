# SmolLM2-1.7B Candidate Download Note

Date: 2026-06-05

Candidate: `HuggingFaceTB/SmolLM2-1.7B-Instruct`

Reason: cached repo metadata was present locally, but the actual model weight
file was incomplete. This model is a useful third 1B+ family candidate for the
fake-quant pipeline because it is not Qwen or OLMo2 and fits the same
short-cycle evaluation protocol.

Initial offline load result:

```text
OSError: HuggingFaceTB/SmolLM2-1.7B-Instruct does not appear to have a file named pytorch_model.bin or model.safetensors.
```

Guarded smoke failed before model load, not because of GPU memory:

```text
max_memory_used_mib: 961 / 8151
max_memory_used_ratio: 0.1179
killed_by_guard: false
```

Action: run `huggingface_hub.snapshot_download()` to resume the incomplete
safetensors download. Do not report this as a model-quality failure.
