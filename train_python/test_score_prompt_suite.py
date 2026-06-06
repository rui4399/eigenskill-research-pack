import json
import tempfile
import unittest
from pathlib import Path

import score_prompt_suite as scorer


class ScorePromptSuiteTests(unittest.TestCase):
    def test_json_key_rule_accepts_required_keys(self) -> None:
        rule = scorer.rule_for_prompt("Write minified JSON with keys hypothesis, proxy, and risk.")
        self.assertEqual(rule.name, "json_keys")
        self.assertTrue(rule.score('{"hypothesis":"h","proxy":"p","risk":"r"}').passed)
        self.assertFalse(rule.score('{"hypothesis":"h","risk":"r"}').passed)

    def test_arithmetic_rule_checks_expected_byte_count(self) -> None:
        rule = scorer.rule_for_prompt("Compute the packed byte count for 8192 signed 4-bit values.")
        self.assertEqual(rule.name, "byte_count_8192_int4")
        self.assertTrue(rule.score("4096 bytes").passed)
        self.assertFalse(rule.score("8192 bytes").passed)

    def test_scores_baseline_and_fused_rows_from_prompt_suite_json(self) -> None:
        payload = {
            "rows": [
                {
                    "id": 0,
                    "prompt": "Compute the packed byte count for 8192 signed 4-bit values.",
                    "baseline": {"generated_text": "4096 bytes"},
                    "fused": {"generated_text": "8192 bytes"},
                },
                {
                    "id": 1,
                    "prompt": "Write minified JSON with keys hypothesis, proxy, and risk.",
                    "baseline": {"generated_text": '{"hypothesis":"h","proxy":"p","risk":"r"}'},
                    "fused": {"generated_text": '{"hypothesis":"h","risk":"r"}'},
                },
            ]
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "suite.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            result = scorer.score_file(path)

        self.assertEqual(result["aggregate"]["prompts"], 2)
        self.assertEqual(result["aggregate"]["baseline_passes"], 2)
        self.assertEqual(result["aggregate"]["fused_passes"], 0)
        self.assertEqual(result["rows"][0]["rule"], "byte_count_8192_int4")

    def test_expected_jsonl_overrides_prompt_inference(self) -> None:
        payload = {
            "rows": [
                {
                    "id": 7,
                    "prompt": "Say anything.",
                    "baseline": {"generated_text": "calibration split instability"},
                    "fused": {"generated_text": "calibration only"},
                }
            ]
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "suite.json"
            expected_path = Path(tmp) / "expected.jsonl"
            path.write_text(json.dumps(payload), encoding="utf-8")
            expected_path.write_text(
                json.dumps(
                    {
                        "id": 7,
                        "prompt": "Say anything.",
                        "rule": "contains_all",
                        "expected": ["calibration", "split", "instability"],
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            specs = scorer.load_expected_specs(expected_path)
            result = scorer.score_file(path, expected_specs=specs)

        self.assertEqual(result["rows"][0]["rule"], "contains_all")
        self.assertTrue(result["rows"][0]["baseline"]["passed"])
        self.assertFalse(result["rows"][0]["fused"]["passed"])
        self.assertTrue(result["rows"][0]["regressed"])


if __name__ == "__main__":
    unittest.main()
