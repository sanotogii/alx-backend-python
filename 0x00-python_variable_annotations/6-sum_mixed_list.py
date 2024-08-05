#!/usr/bin/env python3
"""
This module contains a function sum_mixed_list that calculates the
sum of a list containing both integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing both integers and floats.
    """
    return sum(mxd_lst)
