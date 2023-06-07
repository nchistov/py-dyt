from src.py_dyt import translate


def test_simple():
    expected = 'Hello, Nick!'
    actual = translate('Hello, $name$!', {'name': 'Nick'})

    assert actual == expected


def test_number():
    expected = "Hello, Nick! It's 5 o'clock"
    actual = translate("Hello, $name$! It's $time$ o'clock", {'name': 'Nick', 'time': 5})

    assert actual == expected
