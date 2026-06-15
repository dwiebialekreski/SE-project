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


class TestThresholdConfigUpdate(unittest.TestCase):

    def test_update_thresholds_changes_warning_level(self):
        config = ThresholdConfig(warningLevel=50.0, criticalLevel=80.0)
        config.updateThresholds(60.0, 90.0)
        self.assertEqual(config.warningLevel, 60.0)

    def test_update_thresholds_changes_critical_level(self):
        config = ThresholdConfig(warningLevel=50.0, criticalLevel=80.0)
        config.updateThresholds(60.0, 90.0)
        self.assertEqual(config.criticalLevel, 90.0)

    def test_update_thresholds_raises_when_warn_equals_crit(self):
        config = ThresholdConfig(warningLevel=50.0, criticalLevel=80.0)
        with self.assertRaises(ValueError):
            config.updateThresholds(80.0, 80.0)

    def test_update_thresholds_raises_when_warn_greater_than_crit(self):
        config = ThresholdConfig(warningLevel=50.0, criticalLevel=80.0)
        with self.assertRaises(ValueError):
            config.updateThresholds(90.0, 70.0)


if __name__ == "__main__":
    unittest.main()
