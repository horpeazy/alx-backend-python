#!/usr/bin/env python3
""" this modules provides a type-annotated function sum_list
    which takes a list input_list of floats as argument and
    returns their sum as a float.
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """ calculates the sum of numbers in input_list
        input_list(list[float]): list of floats
        return(float): sum of the numbers in input_list
    """
    return sum(input_list)
