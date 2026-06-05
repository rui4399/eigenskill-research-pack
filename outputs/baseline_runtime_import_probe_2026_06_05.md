# Baseline Runtime Import Probe - 2026-06-05

This probe checks the active WSL Python runtime used by the fake-quant
experiments. It is separate from the earlier isolated `baseline_venv`
metadata/install probe.

## Command

```bash
python3 - <<'PY'
mods = ["torch", "transformers", "optimum", "gptqmodel", "awq", "auto_gptq", "llmcompressor"]
import importlib.util
for m in mods:
    spec = importlib.util.find_spec(m)
    print(f"{m}:", "FOUND" if spec else "missing")
PY
```

## Result

```text
torch: FOUND
transformers: FOUND
optimum: missing
gptqmodel: missing
awq: missing
auto_gptq: missing
llmcompressor: missing
```

Installed relevant packages:

```text
accelerate   1.13.0
torch        2.12.0+cu130
torchaudio   2.11.0+cu130
torchvision  0.27.0+cu130
transformers 5.8.1
```

## Interpretation

The active experiment runtime can run the current PyTorch fake-quant evaluator,
but it is not a runnable GPTQ/AWQ/SparseML/llm-compressor baseline environment.
The earlier `baseline_install_probe` only established that public package names
are discoverable and that a no-dependency metadata install can succeed in an
isolated venv. It did not make these baselines available in the active runtime.

Do not claim comparison against GPTQ/AWQ/SmoothQuant/QuaRot from this runtime.

