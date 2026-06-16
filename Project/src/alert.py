EMAIL_SUBJECT = "EDODS ALERT: Critical Water Level"
EMAIL_BODY = "Water level has exceeded the critical threshold. Immediate action required."


class AlertManager:

    def __init__(self) -> None:
        self.emailApi = None

    def triggerVisualAlert(self, level: float) -> None:
        pass

    def dispatchEmail(self, operatorID: str) -> None:
        self.emailApi.send(to=operatorID, subject=EMAIL_SUBJECT, body=EMAIL_BODY)
