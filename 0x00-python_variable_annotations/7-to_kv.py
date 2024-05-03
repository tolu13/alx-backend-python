#!/usr/bin/env python3
from typing import Union, Tuple
"""
A function that returns tuple containing string, float

"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ A function that returns tuple containing string, float """
    return k, float(v) ** 2
