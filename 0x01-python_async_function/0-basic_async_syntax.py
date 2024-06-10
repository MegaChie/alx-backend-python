#!/usr/bin/env python3
"""Task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits a random time up to 10 seconds then return the time waited"""
    waitTime = random.uniform(0, max_delay)
    await asyncio.sleep(waitTime)
    return waitTime
