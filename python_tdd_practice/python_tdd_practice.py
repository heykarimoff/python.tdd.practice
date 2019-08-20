# -*- coding: utf-8 -*-
from functools import reduce


class Calculator:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        def _mul(a, b):
            return a * b

        return reduce(_mul, args)
