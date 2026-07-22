from main import extract_username


def test_extract_empty_username():
    assert extract_username("") == ""


def test_existing_at_symbol():
    assert extract_username("keke@") == "keke"
    assert extract_username("keke@@") == "keke"


def test_invalid_username():
    assert extract_username("@keke@") == ""
    assert extract_username("keke") == ""
