#!/usr/bin/env python3

"""
This module contains a function for safely retrieving .

"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element from the input list.

    """
    if lst:
        return lst[0]
    else:
        return None
