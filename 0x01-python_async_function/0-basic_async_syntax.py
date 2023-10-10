#!/usr/bin/env python3
"""
An async coroutine that takes int arg
"""
import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """
    waits for a random delay beetween 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
