import pytest 

from suma_resta import (
    divide_two_numbers,
    multiply_two_numbers,
    subtract_two_numbers,
    sum_two_numbers,
)


def test_sum():
    assert sum_two_numbers(2, 3) == 5


def test_subtract():
    assert subtract_two_numbers(10, 4) == 6


def test_multiply():
    assert multiply_two_numbers(3, 4) == 12


def test_divide():
    assert divide_two_numbers(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_two_numbers(5, 0)