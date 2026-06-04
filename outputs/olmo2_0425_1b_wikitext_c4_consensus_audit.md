# Quant Consensus Audit

Label: `OLMo2-0425-1B-WikiText2-C4`

High bits: `8`

## Inputs

| role | path | method |
|---|---|---|
| left | `outputs/olmo2_0425_1b_loss_sensitive_alloc_4to8_limit2_group128_summary.json` | `loss_sensitive_4to8` |
| right | `outputs/olmo2_0425_1b_loss_sensitive_alloc_4to8_c4_limit2_group128_summary.json` | `loss_sensitive_4to8` |
| consensus | `outputs/olmo2_0425_1b_loss_sensitive_wikitext_c4_consensus_alloc_4to8_group128_summary.json` | `loss_sensitive_consensus_4to8` |

## Allocation Summary

| allocation | modules | avg bits | budget used | bit histogram | high-count |
|---|---:|---:|---:|---|---:|
| `left` | 113 | 4.4984 | 0.9996 | `{4: 90, 8: 23}` | 23 |
| `right` | 113 | 4.4984 | 0.9996 | `{4: 93, 8: 20}` | 20 |
| `consensus` | 113 | 4.4984 | 0.9996 | `{4: 87, 8: 26}` | 26 |

## Overlap

| pair | intersection | union | Jaccard |
|---|---:|---:|---:|
| `left/right` | 6 | 37 | 0.1622 |
| `left/consensus` | 18 | 31 | 0.5806 |
| `right/consensus` | 14 | 32 | 0.4375 |

Positive Jaccard/overlap only describes allocation stability. It does not prove downstream quality; read it with PPL evidence.
