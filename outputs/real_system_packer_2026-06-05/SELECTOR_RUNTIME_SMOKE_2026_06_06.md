# Selector-Driven ESMP Runtime Smoke

Status: **PASS**

This smoke run verifies that measured Triton kernel selector output is consumed
by the prototype ESMP generation runtime. It is a wiring and auditability check,
not an end-to-end speedup claim.

## Command

```bash
python3 train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.90 \
  --max-start-memory-ratio 0.90 \
  --min-disk-free-gb 5 \
  --disk-check-path . \
  --timeout-sec 300 \
  --out outputs/real_system_packer_2026-06-05/selector_runtime_smoke_guard_2026_06_06.json \
  -- python3 train_python/measure_esmp_generation_latency.py \
    --model Qwen/Qwen3-0.6B \
    --local-files-only \
    --runtime triton_grouped \
    --kernel-config-selector outputs/real_system_packer_2026-06-05/triton_qwen_shape_kernel_config_selector_2026_06_06.json \
    --module-filter self_attn.q_proj \
    --layers 0 \
    --max-modules 1 \
    --max-new-tokens 4 \
    --warmup-runs 0 \
    --out outputs/real_system_packer_2026-06-05/qwen3_esmp_selector_triton_1mod_4tok.json
```

## Result

- model: `Qwen/Qwen3-0.6B`
- replaced module: `model.layers.0.self_attn.q_proj`
- runtime: `triton_grouped`
- selector configs loaded: `8`
- package compression for replaced module vs FP32: `7.6413x`
- prompt tokens: `12`
- generated tokens: `4`
- TTFT: `2.4270 s`
- throughput: `1.4233 tok/s`
- peak GPU memory reported by generation script: `1173.0103 MiB`
- guard peak GPU memory: `4663 / 8151 MiB` (`57.21%`)
- guard status: not killed by memory guard or timeout

## Selector Decisions

| requested batch | selected measured batch | shape | BM | BN | BK | selector status | measured grouped/FP16 |
|---:|---:|---|---:|---:|---:|---|---:|
| 12 | 16 | `2048x1024` | 16 | 8 | 128 | `fp16_win` | 1.6543x |
| 1 | 8 | `2048x1024` | 32 | 8 | 128 | `fp16_win` | 1.3194x |

## Claim Boundary

- Valid claim: selector JSON now drives actual ESMP generation runtime choices
  and records those choices in output JSON.
- Invalid claim: this 1-module, 4-token smoke proves end-to-end acceleration,
  production Tensor Core readiness, or mobile deployment performance.
