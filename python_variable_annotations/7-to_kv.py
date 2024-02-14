#!/usr/bin/env python3
"""This module contains one function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function takes a string and and int or float
    as arguments and returns a tuple
    Args:
        k: str - should contain a string
        v: Union[int, float] - Should contains int or float
    Return:
        A tuple that contains the "k" and the square of "v"
    """
    square_v = (v * v)
    return (str(k), square_v)
