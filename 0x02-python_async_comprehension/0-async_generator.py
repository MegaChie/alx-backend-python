#!/usr/bin/env python3
"""Task 0"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a random float between 0 and 10 every second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
