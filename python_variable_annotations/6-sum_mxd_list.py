#!/usr/bin/python3
"""This module contains one function"""


from typing import List, Union


def sum_mxd_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function takes a list of ints and floats and
    returns their sum as float
    Args:
        mxd_lst: List[Union[int, float]] - should be a
        list that only contains both int, float
    Returns:
        float(sum(mxd_lst)) - sum of elements in mxd_lst as float
    """
    return float(sum(mxd_lst))
