# AWQ/GPTQ-Style PTQ Baseline Proxy

Date: `2026-06-06T14:42:17+00:00`
Method: `awq_gptq_style_ptq_baseline_proxy`
Source: `outputs\qwen3_0p6b_c4_module_loss_sensitivity_limit4_group128.json`
Records: `197`

## Package Audit Snapshot

| package | available | version |
|---|---:|---|
| `auto_gptq` | False | `` |
| `awq` | False | `` |
| `optimum` | True | `2.1.0` |
| `gptqmodel` | False | `` |

## Proxy Methods

| method | avg bits | budget | protected | protected sensitivity | bit hist |
|---|---:|---:|---:|---:|---|
| `gptq_loss_hessian_proxy` | 4.499670 | true | 39 | 0.586456 | `{'4': 158, '8': 39}` |
| `awq_activation_saliency_proxy` | 4.499670 | true | 35 | 0.577225 | `{'4': 162, '8': 35}` |

## Claim Boundary

- Valid claim: executable AWQ/GPTQ-style proxy baselines exist over measured module sensitivity records. Invalid claim: this is an official AWQ/GPTQ quantizer run, a CUDA PTQ implementation, or a SOTA comparison.
