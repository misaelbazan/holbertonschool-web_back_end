#!/usr/bin/env python3
"""
"""

wait_n = __import__("1-concurrent_coroutines").wait_n
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """Function with ints <n> and <max_delay> as args that measures the total
    wxecution time for wait_n(n, max_delay)
    Args:
        n: int -> times that a random delay must be spawned
        max_delay: int -> maximum delay time
    Return:
        Returns the total_time / n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n