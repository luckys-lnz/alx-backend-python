#!/usr/bin/env python3
"""
Module containing an async comprehension function to collect
random numbers from an async generator.
"""


import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collect 10 random numbers using async comprehension over async_generator.

    This coroutine uses an async comprehension to iterate over the values
    yielded by async_generator, collects 10 random numbers, and then returns
    them in a list.

    Returns:
        list: A list of 10 random floating-point numbers generated
              asynchronously by async_generator.
    """
    return [i async for i in async_generator()]
