class ThresholdConfig:

    def __init__(self, warningLevel: float, criticalLevel: float) -> None:
        self.warningLevel: float = warningLevel
        self.criticalLevel: float = criticalLevel

    def updateThresholds(self, warn: float, crit: float) -> None:
        if warn >= crit:
            raise ValueError("warningLevel must be less than criticalLevel")
        self.warningLevel = warn
        self.criticalLevel = crit
