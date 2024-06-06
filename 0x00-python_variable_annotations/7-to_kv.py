#!/usr/bin/env python3
"""Task 7"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Type-annotated function that returns a tuple consisting of passed arguments
    """
    return (k, v ** 2)
