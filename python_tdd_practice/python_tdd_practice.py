# -*- coding: utf-8 -*-
from functools import reduce


class Calculator:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "inf"

    def avg(self, iterable, lt=None, ut=None):
        if not len(iterable):
            return 0

        if lt is None:
            lt = min(iterable)

        if ut is None:
            ut = max(iterable)

        _it = [x for x in iterable if lt <= x <= ut]

        return sum(_it) / len(_it)
