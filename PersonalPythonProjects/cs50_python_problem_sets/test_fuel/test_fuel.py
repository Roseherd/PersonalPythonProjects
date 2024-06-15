import pytest
from fuel import convert, gauge


def test_acceptable_fractions():
    assert convert("3/4") == 75
    assert gauge(convert("3/4"))  == "75%"
    assert convert("4/7") == 57
    assert gauge(convert("4/7")) == "57%"


def test_non_integers():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("30/cat")
        convert("dog/6")


def test_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/4")
        convert("8/6")
        convert("92/57")


def test_y_is_0():
    with pytest.raises(ZeroDivisionError):
        convert("7/0")
        convert("95/0")
        convert("16/0")


def test_empty_gauge():
    assert convert("2/200") == 1
    assert gauge(convert("2/200")) == "E"
    assert convert("1/300") == 0
    assert gauge(convert("1/300")) == "E"


def test_full_gauge():
    assert convert("99/100") == 99
    assert gauge(convert("99/100")) == "F"
    assert convert("200/200") == 100
    assert gauge(convert("200/200")) == "F"
