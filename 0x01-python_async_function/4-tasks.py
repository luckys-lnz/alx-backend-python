#!/usr/bin/env python3
"""
task_wait_n module.

This module defines a function task_wait_n that spawns task_wait_random
'n' times with a specified max_delay and returns a list of the delays in
ascending order.
"""

import asyncio
from typing import List
task_wait_random = __import__("3-tasks").wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random 'n' times with max_delay and return the list
    of delays in ascending order.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """

    # Create a list of tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # asyncio.as_completed() collects the results in the order they finish
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
