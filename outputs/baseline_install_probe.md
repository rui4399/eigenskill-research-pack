# Baseline Install Probe

This report summarizes local attempts to install public quantization baseline packages. It is an environment-readiness artifact, not a completed GPTQ/AWQ baseline evaluation.

| probe | success | timeout | no-deps | installed packages | failure hint |
|---|---:|---:|---:|---|---|
| `full_dependency_install` | false | true | false |  | `network_read_timeout` |
| `nodeps_metadata_install` | true | false | true | `gptqmodel==7.0.0`<br>`optimum==2.1.0` | `` |

## Interpretation

- A full dependency install must complete before claiming a runnable GPTQ/AWQ/Optimum baseline.
- A no-deps install only proves package metadata/build availability; it does not prove the baseline can run.
- Until runnable baselines are installed and evaluated, current claims remain limited to fake-quant diagnostics.
