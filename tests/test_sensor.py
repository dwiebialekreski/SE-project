"""
tests/test_sensor.py
Krok 1 - FAZA RED: Test inicjalizacji i atrybutów czujnika WaterLevelSensor.
"""
import unittest

from src.sensor import WaterLevelSensor


class TestWaterLevelSensorInit(unittest.TestCase):

    def test_sensor_has_sensorID(self):
        """Czujnik powinien posiadać atrybut sensorID."""
        sensor = WaterLevelSensor(sensorID="sensor-001")
        self.assertEqual(sensor.sensorID, "sensor-001")

    def test_sensor_has_status(self):
        """Czujnik powinien posiadać atrybut status."""
        sensor = WaterLevelSensor(sensorID="sensor-001")
        self.assertIsNotNone(sensor.status)

    def test_sensor_default_status_is_active(self):
        """Domyślny status czujnika powinien wynosić 'ACTIVE'."""
        sensor = WaterLevelSensor(sensorID="sensor-001")
        self.assertEqual(sensor.status, "ACTIVE")


class TestWaterLevelSensorPingStatus(unittest.TestCase):

    def test_ping_status_returns_bool(self):
        """pingStatus() powinien zwracać wartość typu bool."""
        sensor = WaterLevelSensor(sensorID="sensor-002")
        result = sensor.pingStatus()
        self.assertIsInstance(result, bool)

    def test_ping_status_returns_true(self):
        """pingStatus() powinien zwracać True dla aktywnego czujnika."""
        sensor = WaterLevelSensor(sensorID="sensor-002")
        self.assertTrue(sensor.pingStatus())


if __name__ == "__main__":
    unittest.main()
