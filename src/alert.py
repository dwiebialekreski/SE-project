class AlertManager:

    def __init__(self) -> None:
        self.emailApi = None

    def triggerVisualAlert(self, level: float) -> None:
        pass

    def dispatchEmail(self, operatorID: str) -> None:
        self.emailApi.send(to=operatorID, subject="ALERT", body="Water level critical")
