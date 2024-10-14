#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument

Keyword arguments:
max_delay -- Max waiting time between 0-10
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """an async coroutine that takes in an int(max_delay)
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
