#!/usr/bin/env python3

"""
This module contains a function for calculating the length of elements

"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each element in the input list.

    """
    return [(i, len(i)) for i in lst]
