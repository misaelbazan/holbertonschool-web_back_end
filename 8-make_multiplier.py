#!/usr/bin/env python3
"""This module contains one function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function takes a float and returns a function
    that multiplies its input by this float
    Args:
        multiplier: float
    Return:
        A function that multiplies its input by multiplier
    """

    def multiplier_function(value: float) -> float:
        """Inner function that multiplies the given value
        by the outer function's multiplier
        """
        return value * multiplier
    
    return multiplier_function
