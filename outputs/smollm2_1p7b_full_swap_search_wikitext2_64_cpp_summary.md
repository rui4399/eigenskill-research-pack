# Swap Search Summary

Label: `smollm2_1p7b_wikitext2_64`

| model | prompts | max length | group size | reuse model |
|---|---:|---:|---:|---:|
| HuggingFaceTB/SmolLM2-1.7B-Instruct | 64 | 128 | 128 | true |

| base PPL | best PPL | improvement | trials | best swap |
|---:|---:|---:|---:|---|
| 14.8877 | 14.8376 | 0.0502 | 8 | model.layers.12.self_attn.v_proj -> model.layers.22.self_attn.v_proj |

| guard status | max memory | max ratio | max util | limit |
|---|---:|---:|---:|---:|
| pass | 6269 / 8151 MiB | 76.91% | 68% | 85.00% |

Interpretation: positive improvement means the one-step global-PPL swap search beat the base allocation. Zero or negative improvement is a local-stability or negative-result signal, not a runtime claim.
