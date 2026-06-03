#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 train_python/generate_skill_data.py \
  --out data_eval/eigenskill_v1 \
  --train-per-skill 800 \
  --eval-per-skill 160 \
  --seed 3407

python3 train_python/train_lora.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --data data_eval/eigenskill_v1/train.jsonl \
  --eval-data data_eval/eigenskill_v1/eval.jsonl \
  --out models/eigenskill-smollm2-360m-lora-v1-fp16 \
  --epochs 2 \
  --batch-size 1 \
  --grad-accum 16 \
  --lr 1.6e-4 \
  --max-length 512 \
  --lora-r 16 \
  --lora-alpha 32

python3 train_python/eval_skills.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-v1-fp16 \
  --data data_eval/eigenskill_v1/eval.jsonl \
  --out outputs/eigenskill_v1_eval.json \
  --max-new-tokens 160

CUDA_VISIBLE_DEVICES="" python3 train_python/export_model.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-v1-fp16 \
  --out models/eigenskill-smollm2-360m-merged-v1-fp16 \
  --precision fp16

CUDA_VISIBLE_DEVICES="" python3 train_python/export_int8_dynamic.py \
  --model-dir models/eigenskill-smollm2-360m-merged-v1-fp16 \
  --out models/eigenskill-smollm2-360m-int8-v1-dynamic
