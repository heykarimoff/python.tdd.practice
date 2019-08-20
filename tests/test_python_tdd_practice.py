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
