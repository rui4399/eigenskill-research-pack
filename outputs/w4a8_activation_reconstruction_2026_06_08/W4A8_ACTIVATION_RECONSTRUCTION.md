# W4A8 Activation Reconstruction Report

Date: `2026-06-08`
Model: `Qwen/Qwen3-0.6B`
Package summary: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp/pack_summary.json`
Device: `cuda`
Prompts: `4`; max length: `96`

## Aggregate

- Modules OK: `8/8`
- Median W4A16 output rel-L2: `0.120722`
- Median W4A8 output rel-L2: `0.123810`
- P90 W4A8 output rel-L2: `0.190244`
- Max W4A8 output rel-L2: `0.201512`
- Median activation-added rel-L2 vs W4A16: `0.023160`
- P90 activation-added rel-L2 vs W4A16: `0.034111`
- Max activation-added rel-L2 vs W4A16: `0.048561`
- Median activation input rel-L2: `0.023349`
- Max activation saturation fraction: `0.000992`
- Median compression vs FP32: `7.6411x`
- Peak CUDA allocated: `1186.64 MiB`
- Peak CUDA allocation ratio: `0.1456`

## Per-Module Results

| module | bits | samples | W4A16 rel-L2 | W4A8 rel-L2 | activation-added rel-L2 | activation input rel-L2 | compression |
|---|---:|---:|---:|---:|---:|---:|---:|
| `model.layers.7.self_attn.v_proj` | 4 | 64 | 0.195561 | 0.201512 | 0.048561 | 0.035115 | 7.6409x |
| `model.layers.7.self_attn.q_proj` | 4 | 64 | 0.123708 | 0.126668 | 0.027919 | 0.035115 | 7.6413x |
| `model.layers.7.self_attn.k_proj` | 4 | 64 | 0.117737 | 0.120952 | 0.027117 | 0.035115 | 7.6409x |
| `model.layers.0.self_attn.v_proj` | 8 | 64 | 0.009847 | 0.028746 | 0.027041 | 0.023349 | 3.9082x |
| `model.layers.7.self_attn.o_proj` | 4 | 64 | 0.184458 | 0.185414 | 0.019280 | 0.017763 | 7.8163x |
| `model.layers.0.self_attn.q_proj` | 4 | 64 | 0.097103 | 0.098047 | 0.013929 | 0.023349 | 7.6413x |
| `model.layers.0.self_attn.k_proj` | 4 | 64 | 0.076405 | 0.077349 | 0.011883 | 0.023349 | 7.6409x |
| `model.layers.0.self_attn.o_proj` | 4 | 64 | 0.144144 | 0.144574 | 0.010566 | 0.013771 | 7.8163x |

## Claim Boundary

Valid claim: on selected real Qwen3 module activations, the extra drift from per-row A8 activation quantization is measured and bounded.

Invalid claim: this does not prove end-to-end generation speedup, full-model quality retention, mobile deployment, or SOTA quantization.
