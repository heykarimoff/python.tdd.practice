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
