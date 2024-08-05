#!/usr/bin/env python3
"""
This module contains a function to_kv that creates
a tuple from a string and a number.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.
    """
    return (k, float(v ** 2))
