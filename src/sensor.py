"""
src/sensor.py
Klasy Sensor i WaterLevelSensor - symulacja fizycznego czujnika w pamięci programu.
"""


class Sensor:
    """Klasa bazowa reprezentująca ogólny czujnik."""

    def __init__(self, sensorID: str) -> None:
        self.sensorID: str = sensorID
        self.status: str = "ACTIVE"


class WaterLevelSensor(Sensor):
    """Czujnik poziomu wody symulujący zachowanie fizycznego urządzenia."""

    def __init__(self, sensorID: str) -> None:
        super().__init__(sensorID)
