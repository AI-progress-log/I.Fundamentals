from main import extract_domain


def test_empty_invalid_domain():
    assert extract_domain("") == ""


def test_no_atdot_invalid_domain():
    assert extract_domain("user@") == ""
    assert extract_domain("user.") == ""
    assert extract_domain("user") == ""


def test_multiple_symbols_invalid_domain():
    assert extract_domain("@user.domain.") == "user.domain"
