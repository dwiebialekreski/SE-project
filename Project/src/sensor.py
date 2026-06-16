class Sensor:

    def __init__(self, sensorID: str) -> None:
        self.sensorID: str = sensorID
        self.status: str = "ACTIVE"


class WaterLevelSensor(Sensor):

    def __init__(self, sensorID: str, initial_level: float = 0.0) -> None:
        super().__init__(sensorID)
        self.currentLevel: float = initial_level

    def pingStatus(self) -> bool:
        return True

    def getWaterLevel(self) -> float:
        return self.currentLevel

    def transmitData(self, force_level: float = None) -> None:
        if force_level is not None:
            self.currentLevel = force_level
        else:
            self.currentLevel += 1.0
