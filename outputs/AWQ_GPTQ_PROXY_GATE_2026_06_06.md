# AWQ/GPTQ Proxy Gate

Date: `2026-06-06T14:42:50+00:00`
Status: **PASS**
Cases: `2`
Total records: `394`

## Cases

| case | records | packages | methods |
|---|---:|---|---|
| `wikitext2` | 197 | `['optimum']` | `['gptq_loss_hessian_proxy', 'awq_activation_saliency_proxy']` |
| `c4` | 197 | `['optimum']` | `['gptq_loss_hessian_proxy', 'awq_activation_saliency_proxy']` |

## Failures

- none

## Claim Boundary

- Valid claim: AWQ/GPTQ-style proxy artifacts exist and an external PTQ ecosystem package is available. Invalid claim: this is an official AWQ/GPTQ run, GPU PTQ implementation, or SOTA baseline comparison.
