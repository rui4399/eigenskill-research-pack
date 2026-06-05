#!/usr/bin/env bash
set -euo pipefail

# Low-memory mode: reload per config instead of caching all Linear weights.
# This is slower but avoids the 85% VRAM guard failure seen with --reuse-model.

# Check planned random-seed coverage before spending GPU time.
build/cpp-wsl/quant_seed_coverage_check \
  --input data_eval/eval_configs/qwen3_1p7b_c4_128_consensus_random4_compare.json \
  --input data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch1_20260608_11.json \
  --input data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch2_20260612_15.json \
  --input data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch3_20260616_19.json \
  --prefix random_budget_seed_ \
  --start 20260604 \
  --end 20260619 \
  --require-name fp16 \
  --require-name uniform_int4 \
  --require-name wikitext_c4_consensus \
  --require-name cpp_category_budget \
  --emit markdown

# Existing batch batch0: outputs/qwen3_1p7b_c4_128_consensus_random4_ppl_summary.json
# Run batch1
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.85 --poll-seconds 0.5 --out outputs/qwen3_1p7b_c4_128_random16_batch1_gpu_guard.json -- \
  python3 train_python/eval_weight_quant_ppl.py \
    --model Qwen/Qwen3-1.7B \
    --prompts data_eval/text_prompts/c4_en_validation_128.txt \
    --limit-prompts 128 \
    --max-length 128 \
    --device cuda \
    --dtype float16 \
    --config-json data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch1_20260608_11.json \
    --group-size 128 \
    --out outputs/qwen3_1p7b_c4_128_random16_batch1_ppl_summary.json

# Run batch2
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.85 --poll-seconds 0.5 --out outputs/qwen3_1p7b_c4_128_random16_batch2_gpu_guard.json -- \
  python3 train_python/eval_weight_quant_ppl.py \
    --model Qwen/Qwen3-1.7B \
    --prompts data_eval/text_prompts/c4_en_validation_128.txt \
    --limit-prompts 128 \
    --max-length 128 \
    --device cuda \
    --dtype float16 \
    --config-json data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch2_20260612_15.json \
    --group-size 128 \
    --out outputs/qwen3_1p7b_c4_128_random16_batch2_ppl_summary.json

# Run batch3
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.85 --poll-seconds 0.5 --out outputs/qwen3_1p7b_c4_128_random16_batch3_gpu_guard.json -- \
  python3 train_python/eval_weight_quant_ppl.py \
    --model Qwen/Qwen3-1.7B \
    --prompts data_eval/text_prompts/c4_en_validation_128.txt \
    --limit-prompts 128 \
    --max-length 128 \
    --device cuda \
    --dtype float16 \
    --config-json data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch3_20260616_19.json \
    --group-size 128 \
    --out outputs/qwen3_1p7b_c4_128_random16_batch3_ppl_summary.json

# Merge chunked summaries and regenerate evidence artifacts.
build/cpp-wsl/quant_ppl_summary_merge \
  --input outputs/qwen3_1p7b_c4_128_consensus_random4_ppl_summary.json \
  --input outputs/qwen3_1p7b_c4_128_random16_batch1_ppl_summary.json \
  --input outputs/qwen3_1p7b_c4_128_random16_batch2_ppl_summary.json \
  --input outputs/qwen3_1p7b_c4_128_random16_batch3_ppl_summary.json \
  --out outputs/qwen3_1p7b_c4_128_consensus_random16_merged_ppl_summary.json

build/cpp-wsl/quant_evidence_matrix \
  --input outputs/qwen3_1p7b_c4_128_consensus_random16_merged_ppl_summary.json \
  --dataset c4_128 \
  --target wikitext_c4_consensus \
  --emit markdown > outputs/qwen3_1p7b_c4_128_consensus_random16_evidence_matrix.md

build/cpp-wsl/quant_random_baseline_audit \
  --input outputs/qwen3_1p7b_c4_128_consensus_random16_merged_ppl_summary.json \
  --dataset c4_128 \
  --target wikitext_c4_consensus \
  --emit markdown > outputs/qwen3_1p7b_c4_128_consensus_random16_random_seed_audit.md

build/cpp-wsl/gpu_guard_summary \
  --input batch0=outputs/qwen3_1p7b_c4_128_consensus_random4_gpu_guard.json \
  --input batch1=outputs/qwen3_1p7b_c4_128_random16_batch1_gpu_guard.json \
  --input batch2=outputs/qwen3_1p7b_c4_128_random16_batch2_gpu_guard.json \
  --input batch3=outputs/qwen3_1p7b_c4_128_random16_batch3_gpu_guard.json \
  --emit markdown > outputs/qwen3_1p7b_c4_128_consensus_random16_gpu_guard_summary.md
