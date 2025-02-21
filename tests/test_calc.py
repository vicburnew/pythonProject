import pytest

from calc import subtract, add_num, divide, calc_log, calculate_logarithm


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

def test_calc_log():
    assert calc_log(8, 2) == 3

    with pytest.raises(ValueError) as exc_info:
        calc_log(-1, 2)
        assert str(exc_info.value) == 1

def test_calculate_logarithm_with_negative_number():
    with pytest.raises(ValueError) as exc_info:
        calculate_logarithm(-1)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Логарифм можно вычислить только для положительных чисел"
