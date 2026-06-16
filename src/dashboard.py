from enum import Enum

from src.sensor import WaterLevelSensor
from src.config import ThresholdConfig


class ThresholdStatus(Enum):
    NORMAL = "NORMAL"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


class Dashboard:

    def __init__(self, sensors: list, config: ThresholdConfig = None) -> None:
        self.sensors: list = sensors
        self.config: ThresholdConfig = config
        self.displayStatus: str = ""

    def updateChart(self, level: float) -> None:
        self.displayStatus = str(round(level, 2))

    def checkThreshold(self, level: float) -> ThresholdStatus:
        if level >= self.config.criticalLevel:
            return ThresholdStatus.CRITICAL
        elif level >= self.config.warningLevel:
            return ThresholdStatus.WARNING
        return ThresholdStatus.NORMAL
