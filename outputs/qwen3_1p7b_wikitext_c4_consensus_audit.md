# Quant Consensus Audit

Label: `Qwen3-1.7B-WikiText2-C4`

High bits: `8`

## Inputs

| role | path | method |
|---|---|---|
| left | `outputs/qwen3_1p7b_loss_sensitive_alloc_4to8_limit2_group128_summary.json` | `loss_sensitive_4to8` |
| right | `outputs/qwen3_1p7b_loss_sensitive_alloc_4to8_c4_limit2_group128_summary.json` | `loss_sensitive_4to8` |
| consensus | `outputs/qwen3_1p7b_loss_sensitive_wikitext_c4_consensus_alloc_4to8_group128_summary.json` | `loss_sensitive_consensus_4to8` |

## Allocation Summary

| allocation | modules | avg bits | budget used | bit histogram | high-count |
|---|---:|---:|---:|---|---:|
| `left` | 197 | 4.4973 | 0.9994 | `{4: 153, 8: 44}` | 44 |
| `right` | 197 | 4.4973 | 0.9994 | `{4: 157, 8: 40}` | 40 |
| `consensus` | 197 | 4.4973 | 0.9994 | `{4: 147, 8: 50}` | 50 |

## Overlap

| pair | intersection | union | Jaccard |
|---|---:|---:|---:|
| `left/right` | 10 | 74 | 0.1351 |
| `left/consensus` | 36 | 58 | 0.6207 |
| `right/consensus` | 23 | 67 | 0.3433 |

Positive Jaccard/overlap only describes allocation stability. It does not prove downstream quality; read it with PPL evidence.
