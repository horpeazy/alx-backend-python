#!/usr/bin/bash
""" this module contains a function element_length that
    converts a list of strings to a list of tuples conating the string
    and it's length
"""
from typing import Iterable, Sequence, Tuple, List

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ generates a tuple from a list of strings
        lst(list): list containing strings
        return(list): list of tuples
    """
    return [(i, len(i)) for i in lst]
