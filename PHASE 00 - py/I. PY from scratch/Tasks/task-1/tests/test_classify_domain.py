from main import classify_domain


def test_empty_domain():
    assert classify_domain("") == ""


def test_valid_com_classify_domain():
    assert classify_domain("user@domain.com") == "Commercial Domain"


def test_valid_edu_classify_domain():
    assert classify_domain("user@domain.edu") == "Educational Domain"


def test_valid_other_classify_domain():
    assert classify_domain("user@domain.eg") == "Other Domain"
