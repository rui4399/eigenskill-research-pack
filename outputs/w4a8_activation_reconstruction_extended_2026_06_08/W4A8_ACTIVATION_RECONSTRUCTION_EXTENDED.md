# W4A8 Activation Reconstruction Report

Date: `2026-06-08`
Model: `Qwen/Qwen3-0.6B`
Package summary: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp/pack_summary.json`
Device: `cuda`
Prompts: `4`; max length: `96`

## Aggregate

- Modules OK: `24/24`
- Median W4A16 output rel-L2: `0.142812`
- Median W4A8 output rel-L2: `0.144851`
- P90 W4A8 output rel-L2: `0.212923`
- Max W4A8 output rel-L2: `0.252123`
- Median activation-added rel-L2 vs W4A16: `0.031801`
- P90 activation-added rel-L2 vs W4A16: `0.051058`
- Max activation-added rel-L2 vs W4A16: `0.084533`
- Median activation input rel-L2: `0.035115`
- Max activation saturation fraction: `0.000992`
- Median compression vs FP32: `7.6413x`
- Peak CUDA allocated: `1195.39 MiB`
- Peak CUDA allocation ratio: `0.1467`

## Per-Module Results

| module | bits | samples | W4A16 rel-L2 | W4A8 rel-L2 | activation-added rel-L2 | activation input rel-L2 | compression |
|---|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.7.mlp.down_proj` | 4 | 64 | 0.199340 | 0.217814 | 0.084533 | 0.079086 | 7.8766x |
| `model.layers.14.mlp.down_proj` | 4 | 64 | 0.234684 | 0.242772 | 0.061703 | 0.054124 | 7.8766x |
| `model.layers.21.self_attn.v_proj` | 4 | 64 | 0.246552 | 0.252123 | 0.052128 | 0.032259 | 7.6409x |
| `model.layers.7.self_attn.v_proj` | 4 | 64 | 0.195561 | 0.201512 | 0.048561 | 0.035115 | 7.6409x |
| `model.layers.0.mlp.down_proj` | 8 | 64 | 0.008772 | 0.048292 | 0.047528 | 0.052727 | 3.9689x |
| `model.layers.14.mlp.up_proj` | 4 | 64 | 0.179938 | 0.186145 | 0.046466 | 0.040091 | 7.6415x |
| `model.layers.7.mlp.up_proj` | 4 | 64 | 0.170109 | 0.175342 | 0.041355 | 0.035820 | 7.6415x |
| `model.layers.0.mlp.up_proj` | 4 | 64 | 0.161309 | 0.165689 | 0.036947 | 0.034188 | 7.6415x |
| `model.layers.14.self_attn.o_proj` | 4 | 64 | 0.153098 | 0.156303 | 0.032944 | 0.037628 | 7.8163x |
| `model.layers.21.self_attn.q_proj` | 4 | 64 | 0.158016 | 0.161585 | 0.032786 | 0.032259 | 7.6413x |
| `model.layers.21.self_attn.k_proj` | 4 | 64 | 0.171212 | 0.174175 | 0.032257 | 0.032259 | 7.6409x |
| `model.layers.14.mlp.gate_proj` | 4 | 64 | 0.129440 | 0.133376 | 0.031943 | 0.040091 | 7.6415x |
| `model.layers.14.self_attn.q_proj` | 4 | 64 | 0.141480 | 0.145129 | 0.031660 | 0.035152 | 7.6413x |
| `model.layers.7.self_attn.q_proj` | 4 | 64 | 0.123708 | 0.126668 | 0.027919 | 0.035115 | 7.6413x |
| `model.layers.7.self_attn.k_proj` | 4 | 64 | 0.117737 | 0.120952 | 0.027117 | 0.035115 | 7.6409x |
| `model.layers.0.self_attn.v_proj` | 8 | 64 | 0.009847 | 0.028746 | 0.027041 | 0.023349 | 3.9082x |
| `model.layers.14.self_attn.v_proj` | 8 | 64 | 0.006255 | 0.027688 | 0.026974 | 0.035152 | 3.9082x |
| `model.layers.7.mlp.gate_proj` | 4 | 64 | 0.099068 | 0.102030 | 0.024003 | 0.035820 | 7.6415x |
| `model.layers.0.mlp.gate_proj` | 4 | 64 | 0.095733 | 0.098226 | 0.021757 | 0.034188 | 7.6415x |
| `model.layers.7.self_attn.o_proj` | 4 | 64 | 0.184458 | 0.185414 | 0.019280 | 0.017763 | 7.8163x |
| `model.layers.14.self_attn.k_proj` | 4 | 64 | 0.081767 | 0.083556 | 0.017110 | 0.035152 | 7.6409x |
| `model.layers.0.self_attn.q_proj` | 4 | 64 | 0.097103 | 0.098047 | 0.013929 | 0.023349 | 7.6413x |
| `model.layers.0.self_attn.k_proj` | 4 | 64 | 0.076405 | 0.077349 | 0.011883 | 0.023349 | 7.6409x |
| `model.layers.0.self_attn.o_proj` | 4 | 64 | 0.144144 | 0.144574 | 0.010566 | 0.013771 | 7.8163x |

## Claim Boundary

Valid claim: on selected real Qwen3 module activations, the extra drift from per-row A8 activation quantization is measured and bounded.

Invalid claim: this does not prove end-to-end generation speedup, full-model quality retention, mobile deployment, or SOTA quantization.
