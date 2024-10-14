#!/usr/bin/env python3
"""This function measures the total runtime of the asynchronous
`wait_n` function which spawns `n` coroutines, each with a maximum
delay of `max_delay` seconds.
It returns the average execution time per coroutine.
"""

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for calling wait_n(n, max_delay) and
    returns the average time per coroutine.

    Args:
        n (int): The number of times wait_random is spawned by wait_n.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: The average runtime per coroutine (total_time / n).
    """

    # start time
    starting_time = time.time()
    # async wait_n function in the await loop
    asyncio.run(wait_n(n, max_delay))
    # end time
    ending_time = time.time()
    # total execution time
    time_total = ending_time - starting_time
    # average routing time per coroutine
    return time_total / n
