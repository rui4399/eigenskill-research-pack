# Swap Search Summary

Label: `smollm2_1p7b_wikitext2_32`

| model | prompts | max length | group size | reuse model |
|---|---:|---:|---:|---:|
| HuggingFaceTB/SmolLM2-1.7B-Instruct | 32 | 128 | 128 | true |

| base PPL | best PPL | improvement | trials | best swap |
|---:|---:|---:|---:|---|
| 15.1207 | 15.1207 | 0.0000 | 4 | none |

| guard status | max memory | max ratio | max util | limit |
|---|---:|---:|---:|---:|
| pass | 6918 / 8151 MiB | 84.87% | 69% | 85.00% |

Interpretation: positive improvement means the one-step global-PPL swap search beat the base allocation. Zero or negative improvement is a local-stability or negative-result signal, not a runtime claim.
