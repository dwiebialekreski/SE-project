import unittest

from src.config import ThresholdConfig


class TestThresholdConfigInit(unittest.TestCase):

    def test_has_warning_level(self):
        config = ThresholdConfig(warningLevel=50.0, criticalLevel=80.0)
        self.assertEqual(config.warningLevel, 50.0)

    def test_has_critical_level(self):
        config = ThresholdConfig(warningLevel=50.0, criticalLevel=80.0)
        self.assertEqual(config.criticalLevel, 80.0)

    def test_warning_and_critical_are_floats(self):
        config = ThresholdConfig(warningLevel=50.0, criticalLevel=80.0)
        self.assertIsInstance(config.warningLevel, float)
        self.assertIsInstance(config.criticalLevel, float)


if __name__ == "__main__":
    unittest.main()
