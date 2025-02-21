import pytest

from calc import subtract, add_num, divide


def test_add_num():
    assert add_num(2, 2) == 4
    assert add_num(-2, 2) == 0
    assert add_num(0, -1) == -1
    assert add_num(2.5, 2) == 4.5

def test_subtract():
    assert subtract(2, 2) == 0
    assert subtract(-2, 2) == -4
    assert subtract(0, 2) == -2
    assert subtract(3, 2) == 1

def test_divide():
    assert divide(2, 1) == 2
    assert divide(10, 3) == 3.3333333333333335
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)


