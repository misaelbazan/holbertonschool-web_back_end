#!/usr/bin/env python3
"""This module contains a function
"""

wait_random = __import__("0-basic_async_syntax").wait_random
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """This function creates and returns and asyncronous task
    Args:
        max_delay: int - max delay to be passed to the wait_random function
    Return:
        task - the task create when wait_random() was called with create_class()
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task