# EigenSkill Multi-Skill Training Pipeline

This folder contains the first trainable EigenSkill model-package pipeline.

The first release targets 8 narrow, low-entropy skills:

```text
intent_routing
json_repair
field_extraction
command_normalization
sensor_event_triage
packet_encode
safety_gate
unit_time_normalize
```

The intended base model is:

```text
HuggingFaceTB/SmolLM2-360M-Instruct
```

The default training format is LoRA/adapter fine-tuning. The default exported
precision is high precision:

```text
adapter: fp32/fp16 safe tensors depending on trainer
merged model: fp16
optional quantized model: int8 dynamic CPU export
```

No INT4, 1-bit, or 1.58-bit quantization is used in the first model package.

## WSL Setup

```bash
cd /mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co
python3 -m venv .venv-wsl
source .venv-wsl/bin/activate
python -m pip install -U pip wheel setuptools
python -m pip install --index-url https://download.pytorch.org/whl/cu128 torch
python -m pip install transformers datasets peft accelerate trl safetensors pyyaml scikit-learn tqdm
```

## Generate Data

```bash
source .venv-wsl/bin/activate
python train_python/generate_skill_data.py --out data_eval/eigenskill_v0 --train-per-skill 600 --eval-per-skill 120
```

For a fast smoke test:

```bash
python train_python/generate_skill_data.py --out data_eval/eigenskill_smoke --train-per-skill 16 --eval-per-skill 4
```

## Train LoRA Skill Model

```bash
source .venv-wsl/bin/activate
python train_python/train_lora.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --data data_eval/eigenskill_v0/train.jsonl \
  --eval-data data_eval/eigenskill_v0/eval.jsonl \
  --out models/eigenskill-smollm2-360m-lora-fp16 \
  --epochs 2 \
  --batch-size 2 \
  --grad-accum 8 \
  --lr 2e-4 \
  --max-length 384
```

With an 8GB laptop GPU, keep batch size low and use gradient accumulation.

## Evaluate

```bash
python train_python/eval_skills.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-fp16 \
  --data data_eval/eigenskill_v0/eval.jsonl \
  --out outputs/eigenskill_eval.json
```

## v2 Hybrid Runtime

The current strongest package is v2:

```text
models/eigenskill-smollm2-360m-lora-v2-fp16
models/eigenskill-smollm2-360m-merged-v2-fp16
models/eigenskill-smollm2-360m-int8-v2-dynamic
```

The v2 pure-model eval is:

```text
1391/1440 exact = 96.60%
```

The v2 hybrid runtime eval is:

```text
1439/1440 exact = 99.93%
```

The hybrid runtime routes `unit_time_normalize` through a deterministic bypass
micro-kernel and sends the other skills to the merged FP16 model.

Run a bypass-only request:

```bash
python3 train_python/run_hybrid_skill.py \
  --skill unit_time_normalize \
  --input "750克是多少千克，只输出JSON" \
  --deterministic-only
```

Run a model-backed request:

```bash
python3 train_python/run_hybrid_skill.py \
  --skill intent_routing \
  --input "打开客厅灯" \
  --max-new-tokens 8
```

Recheck the hybrid eval without reloading the model:

```bash
python3 train_python/hybrid_eval_skills.py \
  --model-eval outputs/eigenskill_v2_eval.json \
  --data data_eval/eigenskill_v2/eval.jsonl \
  --out outputs/eigenskill_v2_hybrid_eval_recheck.json
```

Verify the full v2 package manifest:

```bash
python3 train_python/verify_v2_package.py
```

This writes:

```text
outputs/eigenskill_v2_package_manifest.json
```

## Quant Diagnostic Reproduction

The OLMo2 consensus repair check is the current most useful guarded GPU
reproduction path. It reruns the C4/WikiText2 64-prompt fake-quant evaluator
with the same random16 pool and regenerates the C++ evidence matrix:

```bash
bash train_python/run_olmo2_consensus_repair.sh
```

It uses:

```text
train_python/run_with_gpu_guard.py --max-memory-ratio 0.85
```

Expected headline from the committed run:

```text
WikiText2-64 consensus PPL 21.0349 vs best random16 21.4637
C4-64        consensus PPL 35.4726 vs best random16 35.5846
```

## Export High-Precision Model

```bash
python train_python/export_model.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-fp16 \
  --out models/eigenskill-smollm2-360m-merged-fp16 \
  --precision fp16
```
