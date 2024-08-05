#!/usr/bin/env python3
"""
This module contains a function safe_first_element that retrieves
the first element of a list safely, or returns None if the list is empty.
"""
from typing import List, Optional, TypeVar


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieve the first element of a list safely.
    """
    if lst:
        return lst[0]
    else:
        return None
