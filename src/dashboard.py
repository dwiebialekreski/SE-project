from src.sensor import WaterLevelSensor


class Dashboard:

    def __init__(self, sensors: list) -> None:
        self.sensors: list = sensors
        self.displayStatus: str = ""

    def updateChart(self, level: float) -> None:
        self.displayStatus = str(round(level, 2))
