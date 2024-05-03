#!/usr/bin/env python3
from typing import List, Union
"""
A function specifying mxd_list containing elemts of int or float

"""


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ A function list that returns mixed list like int,float """
    return sum(mxd_list)
