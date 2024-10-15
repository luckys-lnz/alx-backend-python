#!/usr/bin/env python3
"""
task_wait_random module.

This module defines a function task_wait_random that takes an integer max_delay
and returns an asyncio.Task for wait_random with the given max_delay.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task for wait_random.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: An asyncio task that runs the wait_random coroutine
        with the specified max_delay.
    """
    # return asyncio.Task
    return asyncio.create_task(wait_random(max_delay))