#!/usr/bin/env python3
"""This module contains an async coroutine"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for a list of random delays.

    Arguments:
    - n: number of random delays to wait
    - max_delay: the maximum value that a delay can have

    Returns:
    - List of delay times, in ascending order
    """
    delay_list = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
    return sorted(delay_list)