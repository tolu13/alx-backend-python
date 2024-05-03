#!/usr/bin/env python3
"""
This module defines a function for safely retrieving values from a dictionary.

"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('~T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary based on dict

    """
    if key in dct:
        return dct[key]
    else:
        return default
