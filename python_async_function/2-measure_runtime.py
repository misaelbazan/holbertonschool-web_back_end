#!/usr/bin/env python3
"""
"""

wait_n = __import__("1-concurrent_coroutines").wait_n
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time / n