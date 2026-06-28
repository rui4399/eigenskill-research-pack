#!/usr/bin/env bash
set -euo pipefail

mkdir -p /mnt/e/hf_cache/hub /mnt/e/hf_cache/transformers /mnt/e/cache /mnt/e/tmp \
  /mnt/e/triton_cache /mnt/e/torchinductor_cache

export HF_HOME=/mnt/e/hf_cache
export HF_HUB_CACHE=/mnt/e/hf_cache/hub
export TRANSFORMERS_CACHE=/mnt/e/hf_cache/transformers
export XDG_CACHE_HOME=/mnt/e/cache
export TMPDIR=/mnt/e/tmp
export TEMP=/mnt/e/tmp
export TMP=/mnt/e/tmp
export TRITON_CACHE_DIR=/mnt/e/triton_cache
export TORCHINDUCTOR_CACHE_DIR=/mnt/e/torchinductor_cache

cd /mnt/e/eigenskill-rtx3090-experiments-2026-06-16

PY=/home/dell/anaconda3/envs/zr3090/bin/python3
MODEL=/mnt/e/hf_cache/hub/models--HuggingFaceTB--SmolLM2-360M-Instruct/snapshots/a10cc1512eabd3dde888204e902eca88bddb4951
PROMPTS=data_eval/text_prompts/wikitext2_validation_32.txt
DATE=2026_06_16

is_complete() {
  local json_path="$1"
  [[ -f "$json_path" ]] || return 1
  "$PY" -c 'import json,sys; data=json.load(open(sys.argv[1])); sys.exit(0 if data.get("complete") is True else 1)' "$json_path"
}

for n in 4 8 16; do
  for seed in 0 1 2 3 4 5; do
    seed2=$(printf "%02d" "$seed")
    prompt_seed=$((20261600 + n * 100 + seed))
    out_json="outputs/smollm2_360m_n${n}_seed${seed2}_second_pool_module_loss_sensitivity_group128_${DATE}.json"
    out_md="outputs/SMOLLM2_360M_N${n}_SEED${seed2}_SECOND_POOL_MODULE_LOSS_SENSITIVITY_GROUP128_${DATE}.md"
    out_alloc="outputs/smollm2_360m_n${n}_seed${seed2}_second_pool_loss_sensitive_alloc_4to8_${DATE}.json"
    guard_json="outputs/smollm2_360m_n${n}_seed${seed2}_second_pool_gpu_guard_${DATE}.json"

    if is_complete "$out_json"; then
      echo "{\"skip_complete\":\"$out_json\"}"
      continue
    fi

    echo "{\"run\":{\"n\":$n,\"seed\":\"$seed2\",\"prompt_seed\":$prompt_seed,\"out_json\":\"$out_json\"}}"
    "$PY" train_python/run_with_gpu_guard.py \
      --max-memory-ratio 0.92 --max-start-memory-ratio 0.92 \
      --poll-seconds 2 --timeout-sec 3600 \
      --cleanup-repo-caches --cleanup-root . \
      --min-disk-free-gb 8 --disk-check-path /mnt/e \
      --out "$guard_json" \
      "$PY" train_python/measure_module_quant_sensitivity.py \
        --model "$MODEL" \
        --prompts "$PROMPTS" \
        --limit-prompts "$n" \
        --prompt-sample-size "$n" \
        --prompt-seed "$prompt_seed" \
        --max-length 96 \
        --device cuda \
        --dtype float16 \
        --probe-bits 4 \
        --group-size 128 \
        --max-modules 0 \
        --progress-every 45 \
        --checkpoint-every 45 \
        --lowmem-row-chunk 16 \
        --out-json "$out_json" \
        --out-md "$out_md" \
        --out-allocation "$out_alloc"
  done
done
