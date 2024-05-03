#!/usr/bin/env python3
"""
This module defines a function for zooming in on an array by duplicating its elements.

Author: [Your Name]

"""

from typing import List

def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zooms in on the input array by duplicating each element based on the specified factor.

    Args:
        lst (List[int]): The input array to be zoomed in.
        factor (int): The factor by which each element in the array should be duplicated. Default is 2.

    Returns:
        List[int]: The zoomed-in array with each element duplicated according to the factor.

    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
