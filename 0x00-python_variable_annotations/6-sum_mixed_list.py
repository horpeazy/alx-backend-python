#!/usr/bin/env python3
""" this modules provides a type-annotated function sum_mixed_list
    which takes a list mxd_lst of integers and floats and returns
    their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ calculates the sum of numbers in mxd_lst
        mxd_lst(List[int | float]): list of floats
        return(float): sum of the numbers in mxd_lst
    """
    return sum(mxd_lst)
