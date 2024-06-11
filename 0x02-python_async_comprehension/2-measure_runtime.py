#!/usr/bin/env python3
"""Task 2"""
import asyncio
import time


async def measure_runtime() -> float:
    """Returns the execution time"""
    waitTime = __import__("1-async_comprehension").async_comprehension
    startTime = time.perf_counter()
    toWait = []
    for _ in range(4):
        toWait.append(waitTime())
    await asyncio.gather(*toWait)
    endTime = time.perf_counter() - startTime
    return endTime
