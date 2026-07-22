from main import validate_email


def test_empty_invalid_email():
    assert validate_email("") is False


def test_missing_at_symbol_invalid_email():
    assert validate_email("user") is False


def test_multiple_at_symbols_invalid_email():
    assert validate_email("@user@") is False


def test_missing_dot_after_at_invalid_email():
    assert validate_email(".@user") is False


def test_valid_email():
    assert validate_email("user@domain.com") is True


def test_invalid_email():
    assert validate_email("user@.") is True
    assert validate_email(" @ ") is False
    assert validate_email("@..") is True
    assert validate_email("user@domain.") is True
