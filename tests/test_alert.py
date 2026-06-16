import unittest
from unittest.mock import MagicMock, patch

from src.alert import AlertManager, EMAIL_SUBJECT, EMAIL_BODY


class TestAlertManagerDispatchEmail(unittest.TestCase):

    def test_dispatch_email_calls_external_api_once(self):
        alert = AlertManager()
        mock_email_api = MagicMock()
        alert.emailApi = mock_email_api
        alert.dispatchEmail(operatorID="op-001")
        mock_email_api.send.assert_called_once()

    def test_dispatch_email_sends_to_correct_operator(self):
        alert = AlertManager()
        mock_email_api = MagicMock()
        alert.emailApi = mock_email_api
        alert.dispatchEmail(operatorID="op-001")
        call_kwargs = mock_email_api.send.call_args
        assert "op-001" in str(call_kwargs)

    def test_dispatch_email_not_called_without_invoke(self):
        alert = AlertManager()
        mock_email_api = MagicMock()
        alert.emailApi = mock_email_api
        mock_email_api.send.assert_not_called()

    def test_dispatch_email_uses_email_subject_constant(self):
        alert = AlertManager()
        mock_email_api = MagicMock()
        alert.emailApi = mock_email_api
        alert.dispatchEmail(operatorID="op-001")
        call_kwargs = mock_email_api.send.call_args
        self.assertEqual(call_kwargs.kwargs["subject"], EMAIL_SUBJECT)


if __name__ == "__main__":
    unittest.main()
