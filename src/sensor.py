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

    def __init__(self, sensorID: str, initial_level: float = 0.0) -> None:
        super().__init__(sensorID)
        self.currentLevel: float = initial_level

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

    def transmitData(self, force_level: float = None) -> None:
        """
        Symuluje nowy odczyt czujnika.

        Domyślnie inkrementuje poziom wody o 1.0.
        Opcjonalny parametr force_level pozwala wymusić konkretną wartość
        (np. na potrzeby testowania alertów).

        Args:
            force_level (float, optional): Wartość do wymuszenia. Jeśli None,
                                           poziom wody jest inkrementowany o 1.0.
        """
        if force_level is not None:
            self.currentLevel = force_level
        else:
            self.currentLevel += 1.0

