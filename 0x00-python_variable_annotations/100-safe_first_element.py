#!/usr/bin/env python3
""" this module contains a function named safe_first_element """
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ returns lst if it's not none """
    if lst:
        return lst[0]
    else:
        return None
