#!/usr/bin/env python3
"""This module contains an async coroutine"""

from typing import List
import asyncio
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async coroutine that takes in 2 int args, and will
    spawn wait_random x n times with the specified "max_delay"
    Args:
        n: int - number of times wait_random will spawn
        max_delay: int = the maximum delay in seconds
    Return:
        The list of all delays (float values). The list of
        the delays should be in ascending order without using
        sort() because of concurrency
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks = await asyncio.gather(*tasks)
    return completed_tasks