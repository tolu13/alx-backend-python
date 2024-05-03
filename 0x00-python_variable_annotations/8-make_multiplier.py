#!/usr/bin/env python3
from typing import Callable
"""
A function specifyingg multiplier is a float returns a float

"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ THis function returns a float and takes in a float """
    def multiply(num: float) -> float:
        """ This function returns float """
        return num * multiplier
    return multiply
