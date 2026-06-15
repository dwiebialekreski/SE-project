import unittest

from src.sensor import WaterLevelSensor


class TestWaterLevelSensorInit(unittest.TestCase):

    def test_sensor_has_sensorID(self):
        sensor = WaterLevelSensor(sensorID="sensor-001")
        self.assertEqual(sensor.sensorID, "sensor-001")

    def test_sensor_has_status(self):
        sensor = WaterLevelSensor(sensorID="sensor-001")
        self.assertIsNotNone(sensor.status)

    def test_sensor_default_status_is_active(self):
        sensor = WaterLevelSensor(sensorID="sensor-001")
        self.assertEqual(sensor.status, "ACTIVE")


class TestWaterLevelSensorPingStatus(unittest.TestCase):

    def test_ping_status_returns_bool(self):
        sensor = WaterLevelSensor(sensorID="sensor-002")
        result = sensor.pingStatus()
        self.assertIsInstance(result, bool)

    def test_ping_status_returns_true(self):
        sensor = WaterLevelSensor(sensorID="sensor-002")
        self.assertTrue(sensor.pingStatus())


class TestWaterLevelSensorGetWaterLevel(unittest.TestCase):

    def test_get_water_level_returns_float(self):
        sensor = WaterLevelSensor(sensorID="sensor-003")
        result = sensor.getWaterLevel()
        self.assertIsInstance(result, float)

    def test_get_water_level_returns_current_level(self):
        sensor = WaterLevelSensor(sensorID="sensor-003")
        self.assertEqual(sensor.getWaterLevel(), sensor.currentLevel)

    def test_get_water_level_with_injected_initial_value(self):
        sensor = WaterLevelSensor(sensorID="sensor-003", initial_level=5.75)
        self.assertEqual(sensor.getWaterLevel(), 5.75)


class TestWaterLevelSensorTransmitData(unittest.TestCase):

    def test_transmit_data_changes_current_level(self):
        sensor = WaterLevelSensor(sensorID="sensor-004", initial_level=10.0)
        level_before = sensor.getWaterLevel()
        sensor.transmitData()
        self.assertNotEqual(sensor.getWaterLevel(), level_before)

    def test_transmit_data_increments_level(self):
        sensor = WaterLevelSensor(sensorID="sensor-004", initial_level=10.0)
        sensor.transmitData()
        self.assertGreater(sensor.getWaterLevel(), 10.0)

    def test_transmit_data_force_level_sets_exact_value(self):
        sensor = WaterLevelSensor(sensorID="sensor-004", initial_level=10.0)
        sensor.transmitData(force_level=99.5)
        self.assertEqual(sensor.getWaterLevel(), 99.5)


if __name__ == "__main__":
    unittest.main()
