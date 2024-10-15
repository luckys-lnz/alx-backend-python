#!/usr/bin/env python3
"""
Module that measures the total runtime of executing async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Measure the total runtime of running async_comprehension
    four times in parallel.

    This coroutine will execute async_comprehension four times
    concurrently using asyncio.gather, measure the total execution time,
    and return the total time.

    Returns:
        float: The total runtime of executing async_comprehension
                four times in parallel.
    """
    starting_time = time.perf_counter()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    ending_time = time.perf_counter()

    total_runtime = ending_time - starting_time

    return total_runtime
