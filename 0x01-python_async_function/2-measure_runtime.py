#!/usr/bin/env python3
"""Task 2"""
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """Returns the execution time"""
    waitTime = __import__("1-concurrent_coroutines").wait_n
    startTime = time.perf_counter()
    asyncio.run(waitTime(n, max_delay))
    endTime = time.perf_counter() - startTime
    return endTime / n
