#!/usr/bin/env python3
"""Task 1"""
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """Returns a list of floats yielded by the imported function"""
    maker = __import__("0-async_generator").async_generator
    res = [i async for i in maker()]
    return res
