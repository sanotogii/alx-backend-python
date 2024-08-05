#!/usr/bin/env python3
"""
This module contains a function make_multiplier that returns
a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a given float by a specified multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiply the input float by the multiplier.
        """
        return value * multiplier
    return multiplier_function
