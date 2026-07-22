from main import extract_core


def test_empty_extract_message():
    assert extract_core("") == ""


def test_valid_extract_core():
    assert extract_core("###!!@mocleW EPGTQ!!!6789") == "mocleW EPGTQ"


def test_valid_extract_core2():
    assert extract_core("&&&**$gnirtS PLIO!!@1234") == "gnirtS PLIO"


def test_valid_extract_core3():
    assert extract_core("##$$$@!yalpstcejorp EPUVT****9887") == "yalpstcejorp EPUVT"
