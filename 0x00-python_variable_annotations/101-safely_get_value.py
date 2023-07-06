#!/usr/bin/env python3
"""
Contains a function safely_get_value that safely returns the item in a dict
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
        -> Union[Any, T]:
    """ returns an item in a dict """
    if key in dct:
        return dct[key]
    else:
        return default
