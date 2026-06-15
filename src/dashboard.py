from src.sensor import WaterLevelSensor


class Dashboard:

    def __init__(self, sensors: list) -> None:
        self.sensors: list = sensors
