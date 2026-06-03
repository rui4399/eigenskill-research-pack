# EigenSkill-Q quant_v0 Training Update

Date: 2026-06-03

This update adds a no-leak quantization-policy skill dataset and a verified 1-epoch LoRA training run.

## Dataset

Path:

`	ext
data_eval/eigenskill_quant_v0/
`

Skills:

`	ext
outlier_detect
bit_allocate
rotation_select
residual_patch
kv_policy
`

Audit:

`json
{
  "counts": {
    "train": 900,
    "eval": 300,
    "test": 300
  },
  "train_eval_exact_overlap": 0,
  "train_eval_input_overlap": 0,
  "train_test_exact_overlap": 0,
  "train_test_input_overlap": 0,
  "eval_test_exact_overlap": 0,
  "eval_test_input_overlap": 0,
  "per_skill": {
    "train": {
      "rotation_select": 180,
      "residual_patch": 180,
      "outlier_detect": 180,
      "kv_policy": 180,
      "bit_allocate": 180
    },
    "eval": {
      "rotation_select": 60,
      "bit_allocate": 60,
      "kv_policy": 60,
      "residual_patch": 60,
      "outlier_detect": 60
    },
    "test": {
      "residual_patch": 60,
      "outlier_detect": 60,
      "bit_allocate": 60,
      "rotation_select": 60,
      "kv_policy": 60
    }
  },
  "skills": [
    "outlier_detect",
    "bit_allocate",
    "rotation_select",
    "residual_patch",
    "kv_policy"
  ],
  "seed": 1314,
  "template_split": "disjoint_by_split"
}
`

## 1-epoch LoRA training

Local model artifact is intentionally not committed:

`	ext
models/eigenskill-quant-v0-smollm2-360m-lora-fp16
`

Command:

`ash
CUDA_VISIBLE_DEVICES=0 python3 train_python/train_lora.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --data data_eval/eigenskill_quant_v0/train.jsonl \
  --eval-data data_eval/eigenskill_quant_v0/eval.jsonl \
  --out models/eigenskill-quant-v0-smollm2-360m-lora-fp16 \
  --epochs 1 \
  --batch-size 1 \
  --grad-accum 8 \
  --lr 1.2e-4 \
  --max-length 384 \
  --lora-r 8 \
  --lora-alpha 16
`

Final observed metrics:

`	ext
eval_loss = 0.7816
eval_mean_token_accuracy = 0.7962
train_loss = 1.063
epoch = 1
train_runtime = 470s
`

## Publication note

The old v2 skill benchmark is still only an engineering PoC because it has train/eval leakage. This quant_v0 dataset is a cleaner starting point for EigenSkill-Q, but formal publication still requires public LLM quantization benchmarks and baselines such as RTN/GPTQ/AWQ/SmoothQuant/QuaRot.
