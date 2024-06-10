#!/usr/bin/env python3
"""Task 3"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a task object"""
    randWait = __import__("0-basic_async_syntax").wait_random
    return asyncio.create_task(randWait(max_delay))
