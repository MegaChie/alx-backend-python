#!/usr/bin/env python3
"""Task 1"""
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all delays in an ascending order"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    res = []
    for task in asyncio.as_completed(tasks):
        res.append(await task)
    return res
