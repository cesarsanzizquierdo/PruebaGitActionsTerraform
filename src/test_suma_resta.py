import pytest 

from suma_resta import operaciones


def test_sum():
    assert operaciones.sum_two_numbers(2, 3) == 5


def test_subtract():
    assert operaciones.subtract_two_numbers(10, 4) == 6


def test_multiply():
    assert operaciones.multiply_two_numbers(3, 4) == 12


def test_divide():
    assert operaciones.divide_two_numbers(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        operaciones.divide_two_numbers(5, 0)