# Qwen3-1.7B C4-128 Random16 Chunked Runbook

This runbook completes the C4-128 random16 audit without exceeding the 85% GPU-memory guard. The existing random4 summary is used as batch0 because it already contains FP16, uniform INT4, consensus, category, and random seeds 20260604-20260607.

## Batch Commands

Run these only when the GPU is free enough for the guard to start below 85%.

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.85 --poll-seconds 0.5 \
  --out outputs/qwen3_1p7b_c4_128_random16_batch1_gpu_guard.json -- \
  python3 train_python/eval_weight_quant_ppl.py \
    --model Qwen/Qwen3-1.7B \
    --prompts data_eval/text_prompts/c4_en_validation_128.txt \
    --limit-prompts 128 \
    --max-length 128 \
    --device cuda \
    --dtype float16 \
    --config-json data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch1_20260608_11.json \
    --group-size 128 \
    --reuse-model \
    --out outputs/qwen3_1p7b_c4_128_random16_batch1_ppl_summary.json

python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.85 --poll-seconds 0.5 \
  --out outputs/qwen3_1p7b_c4_128_random16_batch2_gpu_guard.json -- \
  python3 train_python/eval_weight_quant_ppl.py \
    --model Qwen/Qwen3-1.7B \
    --prompts data_eval/text_prompts/c4_en_validation_128.txt \
    --limit-prompts 128 \
    --max-length 128 \
    --device cuda \
    --dtype float16 \
    --config-json data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch2_20260612_15.json \
    --group-size 128 \
    --reuse-model \
    --out outputs/qwen3_1p7b_c4_128_random16_batch2_ppl_summary.json

python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.85 --poll-seconds 0.5 \
  --out outputs/qwen3_1p7b_c4_128_random16_batch3_gpu_guard.json -- \
  python3 train_python/eval_weight_quant_ppl.py \
    --model Qwen/Qwen3-1.7B \
    --prompts data_eval/text_prompts/c4_en_validation_128.txt \
    --limit-prompts 128 \
    --max-length 128 \
    --device cuda \
    --dtype float16 \
    --config-json data_eval/eval_configs/qwen3_1p7b_c4_128_random16_batch3_20260616_19.json \
    --group-size 128 \
    --reuse-model \
    --out outputs/qwen3_1p7b_c4_128_random16_batch3_ppl_summary.json
```

## Merge And Audit

```bash
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
```

## Current Constraint

Do not start these GPU batches while another process already occupies several GiB of VRAM. The guard refuses to start above 85%, and prior full random16 attempts were killed around 86.3%.
