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


if __name__ == "__main__":
    unittest.main()
