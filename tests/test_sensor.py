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


class TestWaterLevelSensorGetWaterLevel(unittest.TestCase):

    def test_get_water_level_returns_float(self):
        """getWaterLevel() powinien zwracać wartość typu float."""
        sensor = WaterLevelSensor(sensorID="sensor-003")
        result = sensor.getWaterLevel()
        self.assertIsInstance(result, float)

    def test_get_water_level_returns_current_level(self):
        """getWaterLevel() powinien zwracać wartość pola currentLevel."""
        sensor = WaterLevelSensor(sensorID="sensor-003")
        self.assertEqual(sensor.getWaterLevel(), sensor.currentLevel)

    def test_get_water_level_with_injected_initial_value(self):
        """Konstruktor powinien przyjmować initial_level i ustawiać currentLevel."""
        sensor = WaterLevelSensor(sensorID="sensor-003", initial_level=5.75)
        self.assertEqual(sensor.getWaterLevel(), 5.75)


class TestWaterLevelSensorTransmitData(unittest.TestCase):

    def test_transmit_data_changes_current_level(self):
        """transmitData() powinien zmienić wartość pola currentLevel."""
        sensor = WaterLevelSensor(sensorID="sensor-004", initial_level=10.0)
        level_before = sensor.getWaterLevel()
        sensor.transmitData()
        self.assertNotEqual(sensor.getWaterLevel(), level_before)

    def test_transmit_data_increments_level(self):
        """transmitData() powinien inkrementować poziom wody."""
        sensor = WaterLevelSensor(sensorID="sensor-004", initial_level=10.0)
        sensor.transmitData()
        self.assertGreater(sensor.getWaterLevel(), 10.0)

    def test_transmit_data_force_level_sets_exact_value(self):
        """transmitData(force_level=X) powinien ustawić currentLevel na X."""
        sensor = WaterLevelSensor(sensorID="sensor-004", initial_level=10.0)
        sensor.transmitData(force_level=99.5)
        self.assertEqual(sensor.getWaterLevel(), 99.5)


if __name__ == "__main__":
    unittest.main()
