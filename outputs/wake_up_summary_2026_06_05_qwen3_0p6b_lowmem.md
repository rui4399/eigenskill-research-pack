# Wake-Up Summary - Qwen3-0.6B Low-Memory Quant Track

Date: 2026-06-05

Completed:

- Qwen3-0.6B full Linear-module sensitivity run completed under guard.
- Allocation produced `{4: 153, 8: 44}` at average 4.4997 bits.
- WikiText2-64 `max_length=96` completed: loss-sensitive PPL 49.5352 vs uniform INT4 54.6542.
- C4-64 evaluation completed: loss-sensitive PPL 47.5872 vs uniform INT4 52.9352.
- Built-in diagnostic prompt smoke completed: loss-sensitive PPL 225.0283 vs uniform INT4 287.3424.
- C++ evidence matrix and GPU guard summaries generated.
- README and `train_python/README.md` updated.

Important caveat:

- A true WikiText2-64 rerun was killed by the 85% guard at 85.06% memory.
- The valid lower-memory WikiText2 row uses `max_length=96` and peaked at 51.97%.
- Do not cite the older misnamed `qwen3_0p6b_loss_sensitive_vs_uniform_ppl_wikitext2_64_summary.json`
  as WikiText2-64; it is now copied to the clearer `default8` filename.

Best next action:

1. Add random/category budget baselines for the Qwen3-0.6B WikiText2-len96 + C4 table.
2. Refactor the evaluator if a full `max_length=128` WikiText2-64 row is still required.
3. Extend the same low-memory path to Qwen3-1.7B or SmolLM3-3B.
