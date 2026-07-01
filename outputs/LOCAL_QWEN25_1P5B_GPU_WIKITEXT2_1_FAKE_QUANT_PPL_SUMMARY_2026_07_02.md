# Local GPU fake-quant PPL smoke - Qwen2.5-1.5B

| case | FP16 PPL | uniform INT4 PPL | consensus 4-to-8 PPL | alloc / INT4 |
|---|---:|---:|---:|---:|
| WikiText2-1 | 10.8203 | 15.6317 | 13.5063 | 0.8640 |

Allocation average bits: 4.4993; uniform INT4 average bits: 4.0.

Sources:

- outputs/LOCAL_QWEN25_1P5B_GPU_WIKITEXT2_1_FP16_ONLY_PPL_2026_07_02.json
- outputs/LOCAL_QWEN25_1P5B_GPU_WIKITEXT2_1_UNIFORM_INT4_ONLY_PPL_2026_07_02.json
- outputs/LOCAL_QWEN25_1P5B_GPU_WIKITEXT2_1_CONSENSUS_ONLY_PPL_2026_07_02.json

Claim boundary: local GPU single-prompt fake-quant PPL smoke for Qwen2.5-1.5B. Useful as feasibility/directional evidence only; not full downstream retention, not same-budget versus INT4, and not AutoAWQ+CSI.
