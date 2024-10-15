#!#!/usr/bin/env python3
"""async_generator that takes no arguments"""


import asyncio
import random


async def async_generator():
    """
    Asynchronously generate random numbers.

    This coroutine will loop 10 times, asynchronously waiting for 1 second
    on each iteration, and yielding a random floating-point number between
    0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """

    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        i += 1