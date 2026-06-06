from __future__ import annotations

import unittest
from unittest import mock

import audit_baseline_environment as audit


class AuditBaselineEnvironmentTests(unittest.TestCase):
    def test_package_status_supports_import_and_distribution_alias(self) -> None:
        with (
            mock.patch.object(audit.importlib.util, "find_spec", return_value=object()) as find_spec,
            mock.patch.object(audit.importlib.metadata, "version", return_value="0.2.9") as version,
        ):
            result = audit.package_status("autoawq", import_name="awq", distribution_name="autoawq")

        self.assertEqual(result["name"], "autoawq")
        self.assertEqual(result["import_name"], "awq")
        self.assertEqual(result["distribution_name"], "autoawq")
        self.assertTrue(result["available"])
        self.assertEqual(result["version"], "0.2.9")
        find_spec.assert_called_once_with("awq")
        version.assert_called_once_with("autoawq")


if __name__ == "__main__":
    unittest.main()
