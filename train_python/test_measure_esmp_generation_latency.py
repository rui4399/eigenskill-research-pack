import unittest

import measure_esmp_generation_latency as gen


class MeasureEsmpGenerationLatencyTests(unittest.TestCase):
    def test_resolve_model_device_uses_inner_wrapper_device(self) -> None:
        class Inner:
            device = "cuda:0"

        class Wrapper:
            model = Inner()

        self.assertEqual(gen.resolve_model_device(Wrapper()), "cuda:0")


if __name__ == "__main__":
    unittest.main()
