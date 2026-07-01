# Local GPU fake-quant PPL multi-slice summary - Qwen2.5-0.5B

| case | prompts | FP16 PPL | uniform INT4 PPL | uniform INT3 PPL | consensus 4-to-8 PPL | alloc / INT4 |
|---|---:|---:|---:|---:|---:|---:|
| WikiText2-8 | 8 | 24.7333 | 41.4982 | 915.6022 | 32.7832 | 0.7900 |
| C4-8 | 8 | 30.6394 | 47.2644 | 1138.7431 | 40.3546 | 0.8538 |
| WikiText2-16 | 16 | 25.0074 | 42.2284 | 804.8320 | 32.3409 | 0.7659 |
| C4-16 | 16 | 28.8456 | 44.8635 | 962.4010 | 38.2107 | 0.8517 |

Allocation average bits: 4.4997; uniform INT4 average bits: 4.0.

Result: consensus allocation beats uniform INT4 on 4/4 local PPL smoke cases.

Claim boundary: local GPU fake-quant PPL smoke over public WikiText2/C4 prompt slices. It supports feasibility/directional evidence for CSI/consensus allocation. It is not full downstream retention, not same-budget versus INT4, not AutoAWQ+CSI, and not SOTA evidence.
