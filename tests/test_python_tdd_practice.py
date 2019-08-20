#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_tdd_practice
----------------------------------

Tests for `python_tdd_practice` module.
"""

import pytest


from python_tdd_practice.python_tdd_practice import Calculator


def test_add_two_numbers():
    calculator = Calculator()

    result = calculator.add(4, 5)

    assert result == 9


def test_add_three_numbers():
    calculator = Calculator()

    result = calculator.add(4, 5, 6)

    assert result == 15


def test_add_many_numbers():
    calculator = Calculator()
    numbers = range(100)

    result = calculator.add(*numbers)

    assert result == 4950


def test_subtract_two_numbers():
    calculator = Calculator()

    result = calculator.sub(10, 3)

    assert result == 7


def test_multiply_two_numbers():
    calculator = Calculator()

    result = calculator.mul(10, 3)

    assert result == 30


def test_muliply_many_numbers():
    calculator = Calculator()
    numbers = range(1, 10)

    result = calculator.mul(*numbers)

    assert result == 362880


def test_divide_two_numbers():
    calculator = Calculator()

    result = calculator.div(13, 2)

    assert result == 6.5


def test_divide_by_zero_returns_inf():
    calculator = Calculator()

    result = calculator.div(13, 0)

    assert result == "inf"


def test_multiply_by_zero_raises_exception():
    calculator = Calculator()

    with pytest.raises(ValueError):
        calculator.mul(3, 0)


def test_average():
    calculator = Calculator()

    result = calculator.avg([2, 5, 12, 98])

    assert result == 29.25


def test_average_removes_upper_outliers():
    calculator = Calculator()

    result = calculator.avg([2, 5, 12, 98], ut=90)

    assert result == pytest.approx(6.333333)


def test_average_removes_lower_outliers():
    calculator = Calculator()

    result = calculator.avg([2, 5, 12, 98], lt=10)

    assert result == pytest.approx(55)


def test_average_removes_upper_outliers():
    calculator = Calculator()

    result = calculator.avg([2, 5, 12, 98], ut=98)

    assert result == 29.25


def test_average_removes_lower_outliers():
    calculator = Calculator()

    result = calculator.avg([2, 5, 12, 98], lt=2)

    assert result == 29.25


def test_average_empyt_list():
    calculator = Calculator()

    result = calculator.avg([])

    assert result == 0
