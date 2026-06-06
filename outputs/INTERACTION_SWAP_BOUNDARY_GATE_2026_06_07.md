# Interaction-Aware Swap Boundary Gate

Date: `2026-06-06T18:13:04+00:00`
Status: **PASS**

## Summary

- cases: `3`
- total trials: `16`
- improved cases: `1`
- improved trials: `5`
- interaction counterexamples: `5`
- mean best improvement PPL: `0.0167`
- max best improvement PPL: `0.0502`
- transfer rows: `2`
- transfer positive rows: `1`
- transfer max regret PPL: `0.0087`
- max guard VRAM ratio: `0.8487`

## Search Cases

| case | prompts | trials | base PPL | best PPL | improvement | interaction counterexamples | best swap | best proxy gain |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| `wikitext2_32` | 32 | 4 | 15.1207 | 15.1207 | 0.0000 | 0 | `- -> -` | n/a |
| `wikitext2_64` | 64 | 8 | 14.8877 | 14.8376 | 0.0502 | 5 | `model.layers.12.self_attn.v_proj -> model.layers.22.self_attn.v_proj` | -0.000744 |
| `c4_64` | 64 | 4 | 21.4269 | 21.4269 | 0.0000 | 0 | `- -> -` | n/a |

## Transfer Rows

| dataset | base PPL | target PPL | improvement | regret | guard |
|---|---:|---:|---:|---:|---|
| `wikitext2_128` | 15.3641 | 15.3127 | 0.0514 | 0.0000 | `pass` |
| `c4_64` | 21.4269 | 21.4356 | -0.0087 | 0.0087 | `pass` |

## Interpretation

This gate supports a narrow interaction-aware diagnostic claim: bounded global-PPL swap search can find at least one improvement missed by the additive proxy, while current cross-split transfer evidence is only a small bounded-regret result.

Valid claim: bounded global-PPL feedback exposes interaction effects beyond independent module ranking.

Invalid claim: this is not a production allocator, SOTA quantizer, or broad transfer guarantee.

## Failures

- none
