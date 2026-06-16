from src.sensor import WaterLevelSensor
from src.config import ThresholdConfig


class Dashboard:

    def __init__(self, sensors: list, config: ThresholdConfig = None) -> None:
        self.sensors: list = sensors
        self.config: ThresholdConfig = config
        self.displayStatus: str = ""

    def updateChart(self, level: float) -> None:
        self.displayStatus = str(round(level, 2))

    def checkThreshold(self, level: float) -> str:
        if level >= self.config.criticalLevel:
            return "CRITICAL"
        elif level >= self.config.warningLevel:
            return "WARNING"
        return "NORMAL"
