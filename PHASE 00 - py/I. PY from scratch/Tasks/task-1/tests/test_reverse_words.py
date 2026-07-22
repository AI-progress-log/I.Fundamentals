from main import reverse_words


def test_reverse_empty_words():
    assert reverse_words("") == ""


def test_valid_reverse_words1():
    assert reverse_words("emocleW") == "Welcome"


def test_valid_reverse_words2():
    assert reverse_words("gnirtS") == "String"


def test_valid_reverse_words3():
    assert reverse_words("yalpstcejorp") == "projectsplay"
