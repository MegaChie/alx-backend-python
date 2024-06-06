#!/usr/bin/env python3
"""Task 8"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type-annotated function that returns the multiplication of two floats"""
    def mult(num: float) -> float:
        return multiplier * num
    return mult
