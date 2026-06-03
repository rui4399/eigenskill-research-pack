# EigenSkill v0 Model Package Report

Date: 2026-06-02

Owner note: this is an MVP artifact for attracting collaborators. It should be presented as a working v0 pipeline, not as proof that the full EigenSkill invariant-subspace theory is solved.

## Summary

This v0 package trains eight low-entropy EigenSkill tasks on `HuggingFaceTB/SmolLM2-360M-Instruct` with LoRA, then exports:

- a LoRA adapter package;
- a merged FP16 model;
- a dynamic INT8 CPU state dict package.

The training run completed successfully on the local NVIDIA GPU. After the user requested lower VRAM usage, the running generation evaluation was stopped and all subsequent export/evaluation commands were forced onto CPU with `CUDA_VISIBLE_DEVICES=""`.

The concrete deliverable is a reproducible small-model skill specialization pipeline:

1. generate synthetic skill data;
2. train a high-precision LoRA adapter;
3. export a merged FP16 model;
4. export a CPU dynamic INT8 package;
5. evaluate generation-level task behavior;
6. use the results to decide which skills are ready and which require prompt/data repair.

This is intentionally narrower than the full EigenSkill research agenda. It gives the project a credible first artifact while keeping the larger claims honest.

## Skills

- `intent_routing`
- `json_repair`
- `field_extraction`
- `command_normalization`
- `sensor_event_triage`
- `packet_encode`
- `safety_gate`
- `unit_time_normalize`

Dataset manifest:

- Train examples: 4800
- Eval examples: 960
- Train per skill: 600
- Eval per skill: 120
- Seed: 42

## Why These Skills Were Chosen

The first batch favors low-entropy structured tasks because they make success measurable and are plausible edge-device workloads. The goal is not open-ended chat quality; it is fast, reliable execution of narrow "skill kernels".

| Skill | Why it fits v0 | Output style | Edge use case |
| --- | --- | --- | --- |
| `intent_routing` | Small label space, easy to score | Class label | Route user/device requests into local handlers. |
| `json_repair` | Clear correctness target | JSON | Clean corrupted packets or tool outputs. |
| `field_extraction` | Useful but harder than pure classification | JSON | Extract slots from natural-language commands. |
| `command_normalization` | Maps language to actuator commands | JSON | Smart-home/robot command canonicalization. |
| `sensor_event_triage` | Natural AIoT workload | Class label | Classify sensor alerts locally. |
| `packet_encode` | Deterministic structured output | JSON | Encode compact latent/skill messages. |
| `safety_gate` | Small label space and high utility | Class label | Decide allow/review/block before execution. |
| `unit_time_normalize` | Common practical parser | JSON | Normalize units, time, and reminders. |

The generation check shows that classification and deterministic packet-style tasks are currently stronger than open slot extraction or time normalization.

## Delivered Model Artifacts

| Artifact | Path | Size | Notes |
| --- | --- | ---: | --- |
| LoRA adapter | `models/eigenskill-smollm2-360m-lora-fp16` | 244 MB | Includes final adapter plus `checkpoint-400` and `checkpoint-600`. |
| Merged FP16 model | `models/eigenskill-smollm2-360m-merged-fp16` | 694 MB | `model.safetensors` merged from SmolLM2-360M base + EigenSkill LoRA. |
| Dynamic INT8 CPU package | `models/eigenskill-smollm2-360m-int8-dynamic` | 529 MB | PyTorch dynamic INT8 state dict; not GGUF. |

Key files:

- `models/eigenskill-smollm2-360m-lora-fp16/adapter_model.safetensors` - 34,793,120 bytes
- `models/eigenskill-smollm2-360m-merged-fp16/model.safetensors` - 723,674,624 bytes
- `models/eigenskill-smollm2-360m-int8-dynamic/pytorch_model_int8_dynamic_state_dict.pt` - 551,063,743 bytes

## How To Use The Packages

### LoRA Adapter

Use this when you want to keep the base model separate and swap skill adapters.

```bash
python3 train_python/eval_skills.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-fp16 \
  --data data_eval/eigenskill_v0/eval.jsonl \
  --out outputs/eigenskill_v0_eval.json
```

Low-VRAM CPU-only version:

```bash
CUDA_VISIBLE_DEVICES="" python3 train_python/eval_skills.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-fp16 \
  --data data_eval/eigenskill_v0/eval.jsonl \
  --out outputs/eigenskill_v0_eval_cpu.json
```

### Merged FP16 Model

Use this when you want a self-contained Hugging Face model directory without loading PEFT separately.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_dir = "models/eigenskill-smollm2-360m-merged-fp16"
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="cpu")
```

### Dynamic INT8 CPU Package

This is a PyTorch dynamic INT8 state dict for CPU-side experiments. It is not GGUF and is not directly compatible with `llama.cpp`.

Good use cases:

- quick local CPU experiments;
- comparing FP16 vs INT8 output drift;
- future C++/micro-kernel export planning.

Not good use cases yet:

- direct RKNN/NPU deployment;
- direct GGUF deployment;
- claiming production quantization quality.

## Training Metrics

Command ran for 600 optimizer steps over 2 epochs.

Final Trainer metrics from `checkpoint-600/trainer_state.json`:

- `global_step`: 600
- `train_runtime`: about 3383 seconds
- `train_loss`: 0.08271
- final `eval_loss`: 0.000727792
- final `eval_mean_token_accuracy`: 1.0
- final `eval_entropy`: 0.007153

These token-level metrics show the model fit the synthetic instruction format, but generation-level behavior still needs task-specific checking.

Training interpretation:

- The synthetic training objective converged cleanly.
- The final token-level eval accuracy reached 1.0, which means the model learned the teacher-forced format on the eval split.
- This does not guarantee robust autoregressive generation; the CPU generation check below is the stronger practical test.
- The gap between token-level metrics and generation-level exactness is expected for small models trained on repetitive synthetic JSON tasks.

## Low-VRAM Generation Check

To reduce VRAM use, full 960-example generation evaluation was stopped. A CPU-only 80-example check was run instead:

`outputs/eigenskill_v0_eval_cpu_limit80.json`

Results:

| Skill | n | Exact | JSON valid |
| --- | ---: | ---: | ---: |
| `safety_gate` | 9 | 1.000 | 0.000 |
| `json_repair` | 9 | 1.000 | 1.000 |
| `unit_time_normalize` | 15 | 0.000 | 0.467 |
| `field_extraction` | 12 | 0.417 | 0.417 |
| `packet_encode` | 10 | 1.000 | 1.000 |
| `command_normalization` | 7 | 0.714 | 0.714 |
| `intent_routing` | 9 | 0.889 | 0.000 |
| `sensor_event_triage` | 9 | 1.000 | 0.000 |

Notes:

- `json_valid` is only meaningful for tasks whose gold answer starts with `{` or `[`.
- `unit_time_normalize` and `field_extraction` are not ready as-is; they often output a fragment instead of the full JSON object.
- `command_normalization` has some semantic mistakes such as mapping dimming to close/off.

Readiness summary:

| Skill | v0 status | Main issue |
| --- | --- | --- |
| `json_repair` | Ready for demo | Needs broader malformed JSON patterns later. |
| `packet_encode` | Ready for demo | Needs binary/CRC variants later. |
| `safety_gate` | Ready for demo | Needs adversarial safety cases later. |
| `sensor_event_triage` | Ready for demo | Needs noisy sensor distributions later. |
| `intent_routing` | Mostly ready | Needs more paraphrase diversity. |
| `command_normalization` | Partial | Some slot semantics confuse dim/off/open/close. |
| `field_extraction` | Needs repair | Often emits one field instead of the full object. |
| `unit_time_normalize` | Needs repair | Sometimes collapses to a scalar/time fragment. |

Representative failures:

```text
Skill: unit_time_normalize
Input: 明天上午九点
Gold : {"date":"tomorrow","time":"09:00"}
Pred : 14:30

Skill: field_extraction
Input: 明天早上8点提醒我给妈妈打电话
Gold : {"date":"明天","time":"早上8点","person":"妈妈","action":"打电话"}
Pred : 早上8点

Skill: command_normalization
Input: 把卧室灯调暗一点
Gold : {"command":"set_device_state","slots":{"device":"卧室灯","state":"dim"}}
Pred : 设置卧室灯关闭
```

## Likely Cause Of Weak Skills

The weaker tasks share the same failure mode: the model learned salient spans but did not consistently learn the required full-object schema. Examples:

- `field_extraction` outputs `早上8点` instead of `{"date":"明天","time":"早上8点","person":"妈妈","action":"打电话"}`.
- `unit_time_normalize` outputs `14:30` or `1500dprinting` instead of a JSON object.

This suggests the v0 prompt/data format is under-constrained for JSON-only generation. The fix should not be "train longer"; the token metrics already saturate. The next improvement should be data and decoding discipline.

Recommended data changes:

1. Prefix every JSON task prompt with a strict contract, e.g. `只输出一行 JSON，不要解释，不要输出片段。`
2. Add negative examples where span-only answers are explicitly corrected.
3. Make every schema key appear in every training example for the same task family, using `null` when absent.
4. Add duplicate semantic variants with different surface wording.
5. Balance examples so common phrases like `明天上午九点` do not map to unrelated memorized outputs.

Recommended decoding changes:

1. Stop generation when a full JSON object closes.
2. Reject non-JSON outputs and retry once with a stricter system suffix.
3. For edge runtime, pair the model with a lightweight schema validator.
4. For deterministic tasks, consider constrained decoding instead of plain greedy generation.

## VRAM Status

After stopping the generation evaluation:

- no WSL `python3` training/evaluation processes were running;
- `nvidia-smi` showed about 3490 MiB used out of 8151 MiB;
- the NVIDIA process table showed no WSL compute process.

The remaining GPU memory appears to be driver/display/Windows graphics context memory rather than this training pipeline. Subsequent commands were run with `CUDA_VISIBLE_DEVICES=""`.

Low-VRAM operating rule:

- Training can use GPU.
- Export should use CPU.
- Long generation evaluation should either run on CPU or be explicitly scheduled when GPU memory is free.
- If GPU memory needs to stay low, use `CUDA_VISIBLE_DEVICES=""` on every command.

Example:

```bash
CUDA_VISIBLE_DEVICES="" python3 train_python/eval_skills.py ...
```

## Reproducibility Commands

Generate data:

```bash
python3 train_python/generate_skill_data.py \
  --schema train_python/skill_schema.yaml \
  --out-dir data_eval/eigenskill_v0 \
  --train-per-skill 600 \
  --eval-per-skill 120 \
  --seed 42
```

Train LoRA:

```bash
python3 train_python/train_lora.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --data data_eval/eigenskill_v0/train.jsonl \
  --eval-data data_eval/eigenskill_v0/eval.jsonl \
  --out models/eigenskill-smollm2-360m-lora-fp16 \
  --epochs 2 \
  --batch-size 1 \
  --grad-accum 16 \
  --lr 2e-4 \
  --max-length 384
```

Export merged FP16:

```bash
CUDA_VISIBLE_DEVICES="" python3 train_python/export_model.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-fp16 \
  --out models/eigenskill-smollm2-360m-merged-fp16 \
  --precision fp16
```

Export dynamic INT8:

```bash
CUDA_VISIBLE_DEVICES="" python3 train_python/export_int8_dynamic.py \
  --model-dir models/eigenskill-smollm2-360m-merged-fp16 \
  --out models/eigenskill-smollm2-360m-int8-dynamic
```

Run low-VRAM smoke evaluation:

```bash
CUDA_VISIBLE_DEVICES="" python3 train_python/eval_skills.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-fp16 \
  --data data_eval/eigenskill_v0/eval.jsonl \
  --out outputs/eigenskill_v0_eval_cpu_limit80.json \
  --limit 80 \
  --max-new-tokens 96
```

## Demo Narrative

For collaborators, describe v0 like this:

> We have a small, reproducible EigenSkill MVP on SmolLM2-360M. It specializes eight structured edge skills with LoRA, exports both merged FP16 and CPU INT8 packages, and includes a C++ low-rank bypass microbenchmark. The current result is not yet a proof of nonlinear Transformer eigen-routing, but it gives us a measurable path: stable structured skills first, then spectral regularization and C++ runtime bypass second.

What to demo:

1. Show the C++ microbenchmark speedup from dense GEMV to low-rank skill path.
2. Show the trained adapter and merged FP16 model directories.
3. Run `json_repair`, `packet_encode`, `safety_gate`, or `sensor_event_triage` examples.
4. Show the report honestly flags weak tasks and gives a repair plan.

What not to claim yet:

- Do not claim true Transformer-wide `O(d)` inference has been achieved.
- Do not claim nonlinear invariance through LayerNorm/SwiGLU is solved.
- Do not claim the INT8 package is deployment-ready for RK3588/RKNN/NPU.
- Do not claim full skill generalization beyond the synthetic distribution.

## Next Sprint

The next useful sprint should focus on generation reliability rather than more theory:

1. Patch `skill_schema.yaml` prompts for strict JSON-only output.
2. Regenerate v1 data with more paraphrases and schema-consistent outputs.
3. Retrain LoRA for 1 epoch first; compare generation exactness before running 2 epochs.
4. Add a JSON schema validator to `eval_skills.py`.
5. Run a full 960-example CPU or scheduled GPU generation evaluation.
6. Only after exactness improves, start adding Eigen-regularization probes to specific linear layers.

## Recommended Next Fixes

1. Add explicit output-schema delimiters to the prompts, such as `OUTPUT_JSON_ONLY:`.
2. Oversample `unit_time_normalize` and `field_extraction` with more varied examples.
3. Add a constrained JSON decoding/post-processing layer for JSON tasks.
4. Re-run a CPU or GPU full 960-example generation evaluation after schema fixes.
5. Keep FP16/INT8 first; avoid INT4/GPTQ/AWQ until generation exactness is stable.
