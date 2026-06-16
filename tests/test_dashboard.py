import unittest

from src.sensor import WaterLevelSensor
from src.dashboard import Dashboard


class TestDashboardInit(unittest.TestCase):

    def test_dashboard_stores_sensors(self):
        sensors = [WaterLevelSensor("s-001"), WaterLevelSensor("s-002")]
        dashboard = Dashboard(sensors)
        self.assertEqual(dashboard.sensors, sensors)

    def test_dashboard_sensors_is_list(self):
        sensors = [WaterLevelSensor("s-001")]
        dashboard = Dashboard(sensors)
        self.assertIsInstance(dashboard.sensors, list)

    def test_dashboard_accepts_empty_sensor_list(self):
        dashboard = Dashboard([])
        self.assertEqual(dashboard.sensors, [])


class TestDashboardUpdateChart(unittest.TestCase):

    def test_update_chart_sets_display_status(self):
        dashboard = Dashboard([])
        dashboard.updateChart(42.5)
        self.assertIsNotNone(dashboard.displayStatus)

    def test_update_chart_stores_level_in_display_status(self):
        dashboard = Dashboard([])
        dashboard.updateChart(42.5)
        self.assertIn("42.5", str(dashboard.displayStatus))

    def test_update_chart_rounds_to_two_decimal_places(self):
        dashboard = Dashboard([])
        dashboard.updateChart(42.5678)
        self.assertEqual(dashboard.displayStatus, "42.57")


class TestDashboardCheckThreshold(unittest.TestCase):

    def setUp(self):
        from src.config import ThresholdConfig
        self.config = ThresholdConfig(warningLevel=50.0, criticalLevel=80.0)
        self.dashboard = Dashboard([], self.config)

    def test_check_threshold_returns_critical(self):
        self.assertEqual(self.dashboard.checkThreshold(90.0), "CRITICAL")

    def test_check_threshold_returns_warning(self):
        self.assertEqual(self.dashboard.checkThreshold(60.0), "WARNING")

    def test_check_threshold_returns_normal(self):
        self.assertEqual(self.dashboard.checkThreshold(30.0), "NORMAL")


if __name__ == "__main__":
    unittest.main()
