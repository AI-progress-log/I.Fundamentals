from main import replace_vowels


def test_empty_message():
    assert replace_vowels("") == ""


def test_valid_replace_vowels1():
    assert replace_vowels("EPUVT") == "APOVT"


def test_valid_replace_vowels2():
    assert replace_vowels("EPGTQ") == "APGTQ"


def test_valid_replace_vowels3():
    assert replace_vowels("PLIO") == "PLEU"
