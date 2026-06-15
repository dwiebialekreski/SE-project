"""
src/sensor.py
Symulacja fizycznego czujnika poziomu wody dla systemu EDODS.
Brak połączeń z zewnętrznym sprzętem — wartości generowane w pamięci programu.
"""


class Sensor:
    """Klasa bazowa reprezentująca ogólny czujnik pomiarowy."""

    def __init__(self, sensorID: str) -> None:
        self.sensorID: str = sensorID
        self.status: str = "ACTIVE"


class WaterLevelSensor(Sensor):
    """
    Czujnik poziomu wody symulujący zachowanie fizycznego urządzenia.

    Nie wymaga połączenia ze sprzętem — działa wyłącznie w pamięci programu.
    """

    def __init__(self, sensorID: str) -> None:
        super().__init__(sensorID)
        self.currentLevel: float = 0.0

    def pingStatus(self) -> bool:
        """
        Sprawdza dostępność (responsywność) czujnika.

        Returns:
            bool: True jeśli czujnik jest aktywny i odpowiada na zapytania.
        """
        return True

    def getWaterLevel(self) -> float:
        """
        Zwraca aktualny poziom wody zarejestrowany przez czujnik.

        Returns:
            float: Aktualny poziom wody (currentLevel).
        """
        return self.currentLevel

