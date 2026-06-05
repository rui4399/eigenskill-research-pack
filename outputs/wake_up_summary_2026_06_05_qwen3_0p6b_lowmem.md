# Wake-Up Summary - Qwen3-0.6B Low-Memory Quant Track

Date: 2026-06-05

Completed:

- Qwen3-0.6B full Linear-module sensitivity run completed under guard.
- Allocation produced `{4: 153, 8: 44}` at average 4.4997 bits.
- C4-64 evaluation completed: loss-sensitive PPL 47.5872 vs uniform INT4 52.9352.
- Built-in diagnostic prompt smoke completed: loss-sensitive PPL 225.0283 vs uniform INT4 287.3424.
- C++ evidence matrix and GPU guard summaries generated.
- README and `train_python/README.md` updated.

Important caveat:

- A true WikiText2-64 rerun was killed by the 85% guard at 85.06% memory.
- Do not cite the older misnamed `qwen3_0p6b_loss_sensitive_vs_uniform_ppl_wikitext2_64_summary.json`
  as WikiText2-64; it is now copied to the clearer `default8` filename.

Best next action:

1. Re-run WikiText2 with lower memory pressure (`max_length=96` or `limit-prompts=32`).
2. If valid, regenerate Qwen3-0.6B evidence matrix with `wikitext2_lowmem` + `c4_64`.
3. Then extend the same low-memory evaluator cleanup to Qwen3-1.7B or SmolLM3-3B.
