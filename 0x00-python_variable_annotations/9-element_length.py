#!/usr/bin/env python3
"""
This module contains a function element_length that calculates
the length of each element in a list of sequences.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in a list of sequences.
    """
    return [(i, len(i)) for i in lst]
