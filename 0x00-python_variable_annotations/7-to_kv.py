#!/usr/bin/env python3
""" this modules contains a type-annotated function to_kv that takes
    a string k and an int OR float v as arguments and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int | float]) -> Tuple[str, float]:
    """ create and returns a tuple from args
        k(str): string argument
        v(int | float): int ot float argument
        return(tuple): tuple formed from args
    """
    return (k, v**2)
