#!/usr/bin/env python3
"""
This module contains a function safe_first_element that retrieves
the first element of a list safely, or returns None if the list is empty.
"""
from typing import List, Optional, TypeVar
T = TypeVar('T')


def safe_first_element(lst: List[T]) -> Optional[T]:
    """
    Retrieve the first element of a list safely.
    """
    if lst:
        return lst[0]
    else:
        return None
