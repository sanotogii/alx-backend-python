#!/usr/bin/env python3
"""
This module contains a function safely_get_value that retrieves
a value from a dictionary safely, with a default fallback.
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T], key: Any, default: Union[T, None] = None
) -> Union[T, None]:
    """
    Retrieve a value from a dictionary safely with a default fallback.
    """
    if key in dct:
        return dct[key]
    else:
        return default
