#!/usr/bin/env python3
"""
A function that returns tuple containing string, float

"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ A function that returns tuple containing string, float """
    return k, float(v) ** 2
