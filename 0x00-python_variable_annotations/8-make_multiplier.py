#!/usr/bin/env python3
""" this module contains a type-annotated function make_multiplier that takes
    a float multiplier as argument and returns a function that multiplies
    a float by multiplier.
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ wrapper function that returns a multiplier func
        multiplier(float): multiplier 
        return(function): multiplier function
    """
    def multiplier_func(n: float) -> float:
        """ multiplies a value by it's arg
            n(float): number to numltiply with multiplier
            return(float): result of multiplication
        """
        return multiplier * n
    return multiplier_func
