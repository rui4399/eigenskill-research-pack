# AAAI Scaling 512 Readiness Audit

Generated: 2026-07-09

Status: `prompt_pool_ready_sensitivity_not_rerun`

The previous n256+ calibration-scaling gap was partly a data-preparation gap. Public WikiText2 and C4 prompt pools with 512 usable prompts each are now materialized in-repo.

| Pool | Dataset | Split | Prompts | Path |
|---|---|---|---:|---|
| wikitext2 | `Salesforce/wikitext` | `test` | 512 | `data_eval/text_prompts/aaai_scaling_512_2026_07_09/wikitext2_test_ppl_prompts.txt` |
| c4 | `allenai/c4` | `validation` | 512 | `data_eval/text_prompts/aaai_scaling_512_2026_07_09/c4_validation_ppl_prompts.txt` |

## Existing Scaling Evidence

- `qwen25_1p5b_n16_n32_n64_n128_csi_scaling_summary.json`
- `qwen25_7b_n16_n32_n64_csi_scale_summary.json`
- `aaai_sprint_calibration_alignment_2026_07_09.json`

## Remaining Work

The expensive module sensitivity and downstream retention runs for n256/n512 have not been executed yet. Use this as scaling readiness evidence, not completed n256/n512 CSI stability results.
