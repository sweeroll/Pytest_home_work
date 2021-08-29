import pytest, logging

from main import valid_email

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize("email_data", ["sweeroll@gmail.com", "example@example.com", "utc@inno.ru"])
def test_email(email_data):
    LOGGER.info(email_data)
    assert valid_email(email_data) == 1


@pytest.mark.parametrize("email_data", ["email'test@test.", "w@", "@tt"])
def test_email_invalid(email_data):
    LOGGER.info(email_data)
    assert valid_email(email_data) == 0
