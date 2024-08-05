#!/usr/bin/env python3
"""
 Type Checking
"""
from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
     Type Checking
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
