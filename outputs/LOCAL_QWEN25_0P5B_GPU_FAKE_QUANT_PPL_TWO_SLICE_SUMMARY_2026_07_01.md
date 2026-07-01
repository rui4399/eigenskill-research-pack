# Local GPU fake-quant PPL two-slice summary - Qwen2.5-0.5B

| case | FP16 PPL | uniform INT4 PPL | uniform INT3 PPL | consensus 4-to-8 PPL | alloc / INT4 |
|---|---:|---:|---:|---:|---:|
| WikiText2-8 | 24.7333 | 41.4982 | 915.6022 | 32.7832 | 0.7900 |
| C4-8 | 30.6394 | 47.2644 | 1138.7431 | 40.3546 | 0.8538 |

Allocation average bits: `4.4997`; uniform INT4 average bits: `4.0`.

Sources:

- `outputs/LOCAL_QWEN25_0P5B_GPU_WIKITEXT2_8_FAKE_QUANT_PPL_2026_07_01.json`
- `outputs/LOCAL_QWEN25_0P5B_GPU_C4_8_FAKE_QUANT_PPL_2026_07_01.json`

Claim boundary: local GPU fake-quant PPL smoke over two 8-prompt public slices. This supports feasibility and directional evidence for CSI/consensus allocation, but is not full downstream retention, not same-budget versus INT4, not AutoAWQ+CSI, and not SOTA evidence.
