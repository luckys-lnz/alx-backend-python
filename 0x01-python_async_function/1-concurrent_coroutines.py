#!/usr/bin/env python3
""""spawn wait_random n times with the specified max_delay.
"""

import asyncio
from typing import List
import random
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    task: Spawn 'wait_random' n times with a specified max_delay and return the
    list of delays in ascending order.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay for each 'wait_random' call.

    Returns:
        List[float]: A list of float values representing the delays, sorted
        in ascending order.
    """

    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    # async.as_completed() to get the task as they complete
    delay = [await tasks for tasks in asyncio.as_completed(task)]
    return delay
