from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import measure_module_quant_sensitivity as sens


class PromptSelectionTests(unittest.TestCase):
    def test_default_prompt_loading_preserves_prefix_behavior(self) -> None:
        prompts = sens.load_prompts("", 3)
        self.assertEqual(prompts, sens.DEFAULT_PROMPTS[:3])

    def test_seeded_prompt_sampling_is_reproducible_and_records_indices(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "prompts.txt"
            path.write_text("\n".join(f"prompt {idx}" for idx in range(12)), encoding="utf-8")

            left, left_meta = sens.load_prompts_with_metadata(str(path), limit=0, sample_size=4, seed=11)
            again, again_meta = sens.load_prompts_with_metadata(str(path), limit=0, sample_size=4, seed=11)
            right, right_meta = sens.load_prompts_with_metadata(str(path), limit=0, sample_size=4, seed=12)

            self.assertEqual(left, again)
            self.assertEqual(left_meta["selected_indices"], again_meta["selected_indices"])
            self.assertNotEqual(left_meta["selected_indices"], right_meta["selected_indices"])
            self.assertEqual(len(left), 4)
            self.assertEqual(len(right), 4)
            self.assertEqual(left_meta["pool_size"], 12)

    def test_limit_applies_after_sampling(self) -> None:
        indices = sens.select_prompt_indices(20, limit=3, sample_size=8, seed=7)
        self.assertEqual(len(indices), 3)
        self.assertEqual(indices, sorted(indices))


if __name__ == "__main__":
    unittest.main()
