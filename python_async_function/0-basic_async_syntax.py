#!/usr/bin/python3
"""This module contains a async function"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This function contains an asynchronous coroutine that
    takes and int argument to return a random delay
    Args:
        max_delay (default = 10) - max number of delay
    Return:
        random_delay: float  
    """
    random_delay = float(random.uniform(0, max_delay))
    await asyncio.sleep(random_delay)
    return random_delay
